#!/usr/bin/env python3
"""Reproducible Bradley--Terry analysis for the SUV comfort corpus.

The primary analysis gives each source statement total mass one, excludes
non-first-hand opinions, and reports both a global fit and within-segment fits.
Scores are regularized MAP estimates; bootstrap intervals describe stability
inside this collected corpus, not uncertainty for the population of SUV owners.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Iterable, Sequence

try:
    import numpy as np
    from scipy.optimize import minimize
    from scipy.special import expit
except ImportError as exc:  # pragma: no cover - exercised by the CLI error path
    raise SystemExit(
        "rank.py requires numpy and scipy. Install the project dependencies or run "
        "`nix-shell -p python3Packages.numpy python3Packages.scipy --run "
        "\"python3 src/rank.py\"`."
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "comparisons.csv"
DEFAULT_SEED = 20260819
DEFAULT_BOOTSTRAP_REPS = 2000
PRIOR_SD = 2.5
MIN_RESPONDENTS = 5
MIN_OPPONENTS = 3

NOT_SUV = {"Lexus ES", "Audi A7"}

FIRST_HAND_EVIDENCE = {
    "owned_both",
    "test_drove_both",
    "owned_one_td_other",
    "owned_one_family",
    "owned_one_loaner",
    "owned_one_rode_other",
    "passenger",
}

OWNER_EVIDENCE = {
    "owned_both",
    "owned_one_td_other",
    "owned_one_family",
    "owned_one_loaner",
    "owned_one_rode_other",
}

EVIDENCE_WEIGHT = {
    "owned_both": 3.0,
    "test_drove_both": 2.0,
    "owned_one_td_other": 1.5,
    "owned_one_family": 1.5,
    "owned_one_loaner": 1.5,
    "owned_one_rode_other": 1.5,
    "opinion_plus_drive": 1.2,
    "passenger": 1.0,
    "opinion": 0.7,
}

VALID_AXES = {"ride", "seats", "nvh", "overall", "long_trip"}

SEGMENTS = {
    "compact": {
        "Honda CR-V", "Subaru Outback", "Subaru Outback 2026",
        "Subaru Crosstrek", "Mazda CX-5", "Mazda CX-50", "Mazda CX-9",
        "Toyota RAV4", "Toyota Venza", "Volvo XC60", "Audi Q5",
        "Mercedes GLC", "Volkswagen Tiguan", "Lincoln Nautilus", "Lexus NX",
        "Porsche Macan", "BMW X3", "BMW X1", "Subaru Forester",
        "Cadillac XT5", "Lincoln Corsair", "Nissan Murano",
    },
    "mid_luxury": {
        "BMW X5", "Mercedes GLE", "Mercedes GLE AMG", "Lexus RX",
        "Volvo XC90", "Audi Q8", "Audi Q7", "Porsche Cayenne",
        "Genesis GV80", "Genesis GV70", "Lincoln Aviator", "Acura MDX",
        "Range Rover Sport", "Land Rover Defender", "Lexus GX",
        "Lexus GX 550", "Toyota 4Runner", "Lexus TX", "Rivian R1S",
        "Tesla Model X", "Tesla Model Y", "BMW iX", "Toyota Land Cruiser",
        "Jeep Grand Cherokee",
    },
    "family_3row": {
        "Hyundai Palisade", "Kia Telluride", "Toyota Highlander",
        "Toyota Grand Highlander", "Honda Pilot", "Honda Passport",
        "Mazda CX-90", "Subaru Ascent", "Volkswagen Atlas", "Ford Explorer",
        "Kia Sorento", "Nissan Pathfinder", "Jeep Grand Cherokee L",
        "Cadillac XT6", "Buick Enclave", "Hyundai Santa Fe",
    },
    "flagship": {
        "Range Rover", "Mercedes GLS", "Mercedes EQS SUV",
        "Cadillac Escalade", "Lincoln Navigator", "BMW X7", "Lexus LX",
        "Land Rover", "Chevrolet Suburban", "Chevrolet Tahoe", "GMC Yukon",
        "Jeep Grand Wagoneer", "Infiniti QX80", "Cadillac Escalade IQ",
        "Toyota Sequoia", "Ford Expedition",
    },
}

SEGMENT_OF = {model: segment for segment, models in SEGMENTS.items() for model in models}


@dataclass(frozen=True)
class Observation:
    row_id: str
    winner: str
    loser: str
    weight: float
    axis: str
    source: str
    evidence: str
    url: str
    statement_id: str
    respondent_id: str
    thread_id: str
    community_affinity: str
    collection_batch: str


@dataclass
class FitResult:
    names: list[str]
    theta: np.ndarray
    objective: float
    max_abs_gradient: float
    success: bool
    message: str

    @property
    def scores(self) -> dict[str, float]:
        return {name: float(self.theta[i]) for i, name in enumerate(self.names)}


def _fallback_id(prefix: str, *parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}_{hashlib.sha256(payload).hexdigest()[:16]}"


def _raw_rows() -> list[dict[str, str]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def validate_raw_rows(rows: Sequence[dict[str, str]]) -> None:
    ids = [row.get("id", "") for row in rows]
    if len(ids) != len(set(ids)):
        duplicates = sorted(k for k, v in Counter(ids).items() if v > 1)
        raise ValueError(f"duplicate row ids: {duplicates}")
    for row in rows:
        rid = row.get("id", "<missing>")
        if not row.get("winner") or not row.get("loser"):
            raise ValueError(f"row {rid}: winner and loser are required")
        if row.get("winner") == row.get("loser") and row.get("evidence") != "exclude":
            raise ValueError(f"row {rid}: self-comparison must be excluded")


def _metadata(row: dict[str, str]) -> tuple[str, str, str, str]:
    rid = row["id"]
    url = row.get("url", "").strip()
    statement = row.get("statement_id", "").strip() or _fallback_id(
        "stmt", row.get("source", ""), url, row.get("quote", ""), rid
    )
    respondent = row.get("respondent_id", "").strip() or _fallback_id(
        "resp", row.get("source", ""), statement
    )
    thread = row.get("thread_id", "").strip() or _fallback_id(
        "thread", row.get("source", ""), url
    )
    affinity = row.get("community_affinity", "").strip() or (
        "winner" if row.get("home_team", "0").strip() == "1" else "neutral"
    )
    return statement, respondent, thread, affinity


def _eligible_raw(row: dict[str, str], evidence: set[str], axis: str | None) -> bool:
    winner, loser = row["winner"].strip(), row["loser"].strip()
    if winner == loser or winner in NOT_SUV or loser in NOT_SUV:
        return False
    if row.get("evidence", "").strip() not in evidence:
        return False
    row_axis = row.get("comfort_axis", "").strip()
    if row_axis not in VALID_AXES or (axis is not None and row_axis != axis):
        return False
    return True


def build_observations(
    raw_rows: Sequence[dict[str, str]],
    *,
    evidence: set[str] = FIRST_HAND_EVIDENCE,
    axis: str | None = None,
    neutral_only: bool = False,
    exclude_home_team_wins: bool = False,
    sources: set[str] | None = None,
    legacy_weights: bool = False,
) -> list[Observation]:
    """Build deduplicated observations with one unit of mass per statement.

    Repeated judgments by one respondent about the same unordered pair and axis
    collapse to one. If that respondent expressed both directions, neither
    direction enters the composite primary fit.
    """
    candidates: list[tuple[int, dict[str, str], str, str, str, str]] = []
    for order, row in enumerate(raw_rows):
        if not _eligible_raw(row, evidence, axis):
            continue
        statement, respondent, thread, affinity = _metadata(row)
        if neutral_only and affinity != "neutral":
            continue
        if exclude_home_team_wins and row.get("home_team", "0").strip() == "1":
            continue
        source = row.get("source", "").strip()
        if sources is not None and source not in sources:
            continue
        candidates.append((order, row, statement, respondent, thread, affinity))

    # One row per exact judgment inside a statement.
    unique: list[tuple[int, dict[str, str], str, str, str, str]] = []
    seen_statement_judgment: set[tuple[str, str, str, str]] = set()
    for item in candidates:
        _, row, statement, _, _, _ = item
        key = (statement, row["winner"].strip(), row["loser"].strip(), row["comfort_axis"].strip())
        if key not in seen_statement_judgment:
            seen_statement_judgment.add(key)
            unique.append(item)

    # Collapse respondent restatements. Conflicting directions cancel.
    by_person_pair: dict[tuple[str, tuple[str, str], str], list[tuple]] = defaultdict(list)
    for item in unique:
        _, row, _, respondent, _, _ = item
        pair = tuple(sorted((row["winner"].strip(), row["loser"].strip())))
        by_person_pair[(respondent, pair, row["comfort_axis"].strip())].append(item)

    kept: list[tuple[int, dict[str, str], str, str, str, str]] = []
    for items in by_person_pair.values():
        directions = {(item[1]["winner"].strip(), item[1]["loser"].strip()) for item in items}
        if len(directions) > 1:
            continue
        kept.append(min(items, key=lambda item: item[0]))

    per_statement = Counter(item[2] for item in kept)
    observations: list[Observation] = []
    for _, row, statement, respondent, thread, affinity in kept:
        if legacy_weights:
            weight = EVIDENCE_WEIGHT[row["evidence"].strip()]
            if row.get("home_team", "0").strip() == "1":
                weight *= 0.6
        else:
            weight = 1.0 / per_statement[statement]
        observations.append(
            Observation(
                row_id=row["id"],
                winner=row["winner"].strip(),
                loser=row["loser"].strip(),
                weight=weight,
                axis=row["comfort_axis"].strip(),
                source=row.get("source", "").strip(),
                evidence=row["evidence"].strip(),
                url=row.get("url", "").strip(),
                statement_id=statement,
                respondent_id=respondent,
                thread_id=thread,
                community_affinity=affinity,
                collection_batch=row.get("collection_batch", "").strip() or "unknown",
            )
        )
    return observations


def graph_components(observations: Sequence[Observation]) -> list[set[str]]:
    nodes = {o.winner for o in observations} | {o.loser for o in observations}
    adjacency = {node: set() for node in nodes}
    for obs in observations:
        adjacency[obs.winner].add(obs.loser)
        adjacency[obs.loser].add(obs.winner)
    components: list[set[str]] = []
    unseen = set(nodes)
    while unseen:
        start = min(unseen)
        stack = [start]
        component = {start}
        unseen.remove(start)
        while stack:
            node = stack.pop()
            for other in adjacency[node]:
                if other in unseen:
                    unseen.remove(other)
                    component.add(other)
                    stack.append(other)
        components.append(component)
    return sorted(components, key=lambda component: (-len(component), sorted(component)))


def graph_bridges(observations: Sequence[Observation]) -> list[tuple[str, str]]:
    """Return model-pair edges whose removal disconnects the simple graph."""
    adjacency: dict[str, set[str]] = defaultdict(set)
    for obs in observations:
        adjacency[obs.winner].add(obs.loser)
        adjacency[obs.loser].add(obs.winner)
    discovery: dict[str, int] = {}
    low: dict[str, int] = {}
    parent: dict[str, str | None] = {}
    bridges: list[tuple[str, str]] = []
    clock = 0

    def visit(node: str) -> None:
        nonlocal clock
        clock += 1
        discovery[node] = low[node] = clock
        for other in sorted(adjacency[node]):
            if other not in discovery:
                parent[other] = node
                visit(other)
                low[node] = min(low[node], low[other])
                if low[other] > discovery[node]:
                    bridges.append(tuple(sorted((node, other))))
            elif parent.get(node) != other:
                low[node] = min(low[node], discovery[other])

    for node in sorted(adjacency):
        if node not in discovery:
            parent[node] = None
            visit(node)
    return sorted(set(bridges))


def _arrays(
    observations: Sequence[Observation], names: Sequence[str]
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    index = {name: i for i, name in enumerate(names)}
    winner = np.fromiter((index[o.winner] for o in observations), dtype=np.int64)
    loser = np.fromiter((index[o.loser] for o in observations), dtype=np.int64)
    weight = np.fromiter((o.weight for o in observations), dtype=np.float64)
    return winner, loser, weight


def fit_bradley_terry(
    observations: Sequence[Observation],
    *,
    models: Sequence[str] | None = None,
    prior_sd: float = PRIOR_SD,
    weight_multiplier: np.ndarray | None = None,
    initial: np.ndarray | None = None,
) -> FitResult:
    names = sorted(models or ({o.winner for o in observations} | {o.loser for o in observations}))
    if len(names) < 2 or not observations:
        return FitResult(names, np.zeros(len(names)), 0.0, 0.0, False, "no estimable comparisons")
    allowed = set(names)
    used = [o for o in observations if o.winner in allowed and o.loser in allowed]
    winner, loser, base_weight = _arrays(used, names)
    weights = base_weight if weight_multiplier is None else base_weight * weight_multiplier
    precision = 1.0 / (prior_sd * prior_sd)

    def objective(theta: np.ndarray) -> tuple[float, np.ndarray]:
        difference = theta[winner] - theta[loser]
        value = float(np.dot(weights, np.logaddexp(0.0, -difference)))
        value += 0.5 * precision * float(np.dot(theta, theta))
        residual = -weights * expit(-difference)
        gradient = precision * theta.copy()
        np.add.at(gradient, winner, residual)
        np.add.at(gradient, loser, -residual)
        return value, gradient

    def hessian(theta: np.ndarray) -> np.ndarray:
        difference = theta[winner] - theta[loser]
        curvature = weights * expit(difference) * expit(-difference)
        matrix = np.eye(len(names), dtype=float) * precision
        np.add.at(matrix, (winner, winner), curvature)
        np.add.at(matrix, (loser, loser), curvature)
        np.add.at(matrix, (winner, loser), -curvature)
        np.add.at(matrix, (loser, winner), -curvature)
        return matrix

    start = np.zeros(len(names)) if initial is None else np.asarray(initial, dtype=float)
    result = minimize(
        objective,
        start,
        jac=True,
        method="L-BFGS-B",
        options={"maxiter": 4000, "ftol": 0.0, "gtol": 1e-9, "maxls": 50},
    )
    value, gradient = objective(result.x)
    if float(np.max(np.abs(gradient))) >= 1e-6:
        # L-BFGS occasionally reports an abnormal line-search termination a few
        # floating-point ulps from the solution. A positive-definite Newton
        # refinement gives us an independent success criterion and avoids
        # silently accepting that status.
        result = minimize(
            objective,
            result.x,
            jac=True,
            hess=hessian,
            method="trust-exact",
            options={"maxiter": 200, "gtol": 1e-9},
        )
        value, gradient = objective(result.x)
    candidate = np.asarray(result.x, dtype=float)
    if float(np.max(np.abs(gradient))) >= 1e-6:
        # Finish with explicit damped Newton steps. The objective is strictly
        # convex because of the prior, so this is a safe last-mile refinement
        # for rare bootstrap samples where a library line search stops early.
        for _ in range(25):
            value, gradient = objective(candidate)
            if float(np.max(np.abs(gradient))) < 1e-7:
                break
            delta = np.linalg.solve(hessian(candidate), gradient)
            predicted = float(np.dot(gradient, delta))
            scale = 1.0
            while scale >= 1e-12:
                proposed = candidate - scale * delta
                proposed_value, _ = objective(proposed)
                if proposed_value <= value - 1e-4 * scale * predicted:
                    candidate = proposed
                    break
                scale *= 0.5
            if scale < 1e-12:
                break
        value, gradient = objective(candidate)
    theta = candidate
    theta -= theta.mean()
    value, gradient = objective(theta)
    max_gradient = float(np.max(np.abs(gradient)))
    success = bool(np.isfinite(value) and np.all(np.isfinite(theta)) and max_gradient < 1e-6)
    message = str(result.message)
    if success and not result.success:
        message = f"first-order convergence ({message})"
    if not success:
        raise RuntimeError(
            f"Bradley-Terry optimizer did not converge: {message}; "
            f"max |gradient|={max_gradient:.3g}"
        )
    return FitResult(names, theta, float(value), max_gradient, success, message)


def _support(observations: Sequence[Observation]) -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = defaultdict(
        lambda: {"wins": 0, "losses": 0, "statements": set(), "respondents": set(), "opponents": set()}
    )
    for obs in observations:
        result[obs.winner]["wins"] += 1
        result[obs.loser]["losses"] += 1
        for model, other in ((obs.winner, obs.loser), (obs.loser, obs.winner)):
            result[model]["statements"].add(obs.statement_id)
            result[model]["respondents"].add(obs.respondent_id)
            result[model]["opponents"].add(other)
    return result


def _eligibility(
    observations: Sequence[Observation], models: Sequence[str]
) -> tuple[dict[str, str], set[str]]:
    support = _support(observations)
    components = graph_components(observations)
    main_component = components[0] if components else set()
    status: dict[str, str] = {}
    eligible: set[str] = set()
    for model in models:
        if model not in main_component:
            status[model] = "disconnected"
        elif len(support[model]["respondents"]) < MIN_RESPONDENTS:
            status[model] = "insufficient_respondents"
        elif len(support[model]["opponents"]) < MIN_OPPONENTS:
            status[model] = "insufficient_opponents"
        else:
            status[model] = "ranked"
            eligible.add(model)
    return status, eligible


def _rank_map(scores: dict[str, float], eligible: set[str]) -> dict[str, int]:
    ordered = sorted(eligible, key=lambda model: (-scores[model], model))
    return {model: i + 1 for i, model in enumerate(ordered)}


def _bootstrap_scope(
    observations: Sequence[Observation],
    fit: FitResult,
    eligible: set[str],
    *,
    reps: int,
    seed: int,
    cluster_field: str = "respondent_id",
) -> dict[str, dict[str, float]]:
    if reps <= 0 or not eligible:
        return {}
    clusters: dict[str, list[int]] = defaultdict(list)
    for i, obs in enumerate(observations):
        clusters[getattr(obs, cluster_field)].append(i)
    cluster_ids = sorted(clusters)
    rng = np.random.default_rng(seed)
    theta_samples = {model: np.empty(reps) for model in fit.names}
    rank_samples = {model: np.empty(reps) for model in eligible}
    base_weights = np.ones(len(observations), dtype=float)
    name_index = {name: i for i, name in enumerate(fit.names)}

    for rep in range(reps):
        sampled = rng.integers(0, len(cluster_ids), size=len(cluster_ids))
        counts = np.bincount(sampled, minlength=len(cluster_ids))
        multiplier = base_weights.copy()
        for cluster_index, cluster_id in enumerate(cluster_ids):
            multiplier[clusters[cluster_id]] = counts[cluster_index]
        boot = fit_bradley_terry(
            observations,
            models=fit.names,
            weight_multiplier=multiplier,
            initial=fit.theta,
        )
        scores = boot.scores
        ranks = _rank_map(scores, eligible)
        for model in fit.names:
            theta_samples[model][rep] = boot.theta[name_index[model]]
        for model in eligible:
            rank_samples[model][rep] = ranks[model]

    result: dict[str, dict[str, float]] = {}
    for model in fit.names:
        theta = theta_samples[model]
        probability = expit(theta)
        record = {
            "theta_lo": float(np.quantile(theta, 0.05)),
            "theta_hi": float(np.quantile(theta, 0.95)),
            "p_lo": float(np.quantile(probability, 0.05)),
            "p_hi": float(np.quantile(probability, 0.95)),
        }
        if model in eligible:
            record["rank_lo"] = int(math.floor(float(np.quantile(rank_samples[model], 0.05))))
            record["rank_hi"] = int(math.ceil(float(np.quantile(rank_samples[model], 0.95))))
        result[model] = record
    return result


def analyse_scope(
    scope: str,
    observations: Sequence[Observation],
    *,
    bootstrap_reps: int,
    seed: int,
) -> tuple[list[dict[str, object]], FitResult, dict[str, object]]:
    components = graph_components(observations)
    models = sorted({o.winner for o in observations} | {o.loser for o in observations})
    fit = fit_bradley_terry(observations, models=models)
    scores = fit.scores
    support = _support(observations)
    status, eligible = _eligibility(observations, models)
    ranks = _rank_map(scores, eligible)
    intervals = _bootstrap_scope(
        observations, fit, eligible, reps=bootstrap_reps, seed=seed
    )
    records: list[dict[str, object]] = []
    for model in sorted(models, key=lambda name: (-scores[name], name)):
        s = support[model]
        interval = intervals.get(model, {})
        records.append(
            {
                "scope": scope,
                "rank": ranks.get(model, ""),
                "model": model,
                "theta": scores[model],
                "wins": s["wins"],
                "losses": s["losses"],
                "appearances": s["wins"] + s["losses"],
                "segment": SEGMENT_OF.get(model, ""),
                "p_vs_average": float(expit(scores[model])),
                "theta_lo": interval.get("theta_lo", ""),
                "theta_hi": interval.get("theta_hi", ""),
                "p_lo": interval.get("p_lo", ""),
                "p_hi": interval.get("p_hi", ""),
                "rank_lo": interval.get("rank_lo", ""),
                "rank_hi": interval.get("rank_hi", ""),
                "n_statements": len(s["statements"]),
                "n_respondents": len(s["respondents"]),
                "n_opponents": len(s["opponents"]),
                "status": status[model],
            }
        )
    diagnostics = {
        "scope": scope,
        "observations": len(observations),
        "statement_mass": sum(o.weight for o in observations),
        "statements": len({o.statement_id for o in observations}),
        "respondents": len({o.respondent_id for o in observations}),
        "models": len(models),
        "ranked_models": len(eligible),
        "components": [sorted(component) for component in components],
        "unique_pairs": len({tuple(sorted((o.winner, o.loser))) for o in observations}),
        "bridges": [list(pair) for pair in graph_bridges(observations)],
        "cross_segment_observations": sum(
            SEGMENT_OF.get(o.winner) != SEGMENT_OF.get(o.loser) for o in observations
        ),
        "cross_segment_statement_mass": sum(
            o.weight for o in observations if SEGMENT_OF.get(o.winner) != SEGMENT_OF.get(o.loser)
        ),
        "objective": fit.objective,
        "max_abs_gradient": fit.max_abs_gradient,
    }
    return records, fit, diagnostics


def _scenario_observations(raw_rows: Sequence[dict[str, str]]) -> dict[str, list[Observation]]:
    primary = build_observations(raw_rows)
    scenarios = {
        "owners_only": build_observations(raw_rows, evidence=OWNER_EVIDENCE),
        "lived_with_both": build_observations(raw_rows, evidence={"owned_both"}),
        "neutral_forums": build_observations(raw_rows, neutral_only=True),
        "exclude_home_team_wins": build_observations(
            raw_rows, exclude_home_team_wins=True
        ),
        "reddit_only": build_observations(raw_rows, sources={"reddit"}),
        "consumer_reviews_only": build_observations(raw_rows, sources={"edmunds", "cars.com"}),
        "legacy_weights": build_observations(
            raw_rows,
            evidence=set(EVIDENCE_WEIGHT),
            legacy_weights=True,
        ),
        "prior_sd_1_5": primary,
        "prior_sd_5_0": primary,
        **{
            f"axis_{axis}": build_observations(raw_rows, axis=axis)
            for axis in ("ride", "seats", "nvh", "overall", "long_trip")
        },
    }
    for batch in sorted({o.collection_batch for o in primary}):
        scenarios[f"exclude_{batch}"] = [o for o in primary if o.collection_batch != batch]
    return scenarios


def analyse_sensitivities(raw_rows: Sequence[dict[str, str]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for scenario, observations in _scenario_observations(raw_rows).items():
        if len(observations) < 2:
            continue
        models = sorted({o.winner for o in observations} | {o.loser for o in observations})
        prior_sd = 1.5 if scenario == "prior_sd_1_5" else 5.0 if scenario == "prior_sd_5_0" else PRIOR_SD
        fit = fit_bradley_terry(observations, models=models, prior_sd=prior_sd)
        support = _support(observations)
        status, eligible = _eligibility(observations, models)
        ranks = _rank_map(fit.scores, eligible)
        for model in sorted(models, key=lambda name: (-fit.scores[name], name)):
            output.append(
                {
                    "scenario": scenario,
                    "rank": ranks.get(model, ""),
                    "model": model,
                    "theta": fit.scores[model],
                    "p_vs_average": float(expit(fit.scores[model])),
                    "n_statements": len(support[model]["statements"]),
                    "n_respondents": len(support[model]["respondents"]),
                    "n_opponents": len(support[model]["opponents"]),
                    "status": status[model],
                }
            )
    return output


def grouped_cross_validation(
    observations: Sequence[Observation], *, folds: int = 5
) -> dict[str, float]:
    fold_of = {
        respondent: int(hashlib.sha256(respondent.encode()).hexdigest()[:8], 16) % folds
        for respondent in {o.respondent_id for o in observations}
    }
    losses: list[float] = []
    briers: list[float] = []
    weights: list[float] = []
    all_models = sorted({o.winner for o in observations} | {o.loser for o in observations})
    for fold in range(folds):
        train = [o for o in observations if fold_of[o.respondent_id] != fold]
        test = [o for o in observations if fold_of[o.respondent_id] == fold]
        if not train or not test:
            continue
        fit = fit_bradley_terry(train, models=all_models)
        scores = fit.scores
        for obs in test:
            probability = float(expit(scores[obs.winner] - scores[obs.loser]))
            probability = min(max(probability, 1e-12), 1 - 1e-12)
            losses.append(-math.log(probability))
            briers.append((1.0 - probability) ** 2)
            weights.append(obs.weight)
    return {
        "folds": folds,
        "log_loss": float(np.average(losses, weights=weights)),
        "brier": float(np.average(briers, weights=weights)),
        "even_odds_log_loss": math.log(2.0),
        "even_odds_brier": 0.25,
    }


def influential_threads(
    observations: Sequence[Observation], fit: FitResult, eligible: set[str], limit: int = 15
) -> list[dict[str, object]]:
    base_ranks = _rank_map(fit.scores, eligible)
    by_thread: dict[str, list[Observation]] = defaultdict(list)
    for obs in observations:
        by_thread[obs.thread_id].append(obs)
    results: list[dict[str, object]] = []
    for thread, thread_rows in by_thread.items():
        # Single, fractional observations cannot move a useful rank enough to
        # justify hundreds of nearly identical refits.
        if sum(o.weight for o in thread_rows) < 1.5:
            continue
        reduced = [o for o in observations if o.thread_id != thread]
        reduced_fit = fit_bradley_terry(reduced, models=fit.names, initial=fit.theta)
        ranks = _rank_map(reduced_fit.scores, eligible)
        changes = {model: abs(ranks[model] - base_ranks[model]) for model in eligible}
        model = max(changes, key=lambda name: (changes[name], name))
        results.append(
            {
                "thread_id": thread,
                "statement_mass": sum(o.weight for o in thread_rows),
                "rows": len(thread_rows),
                "max_rank_change": changes[model],
                "most_affected_model": model,
            }
        )
    return sorted(
        results,
        key=lambda row: (-int(row["max_rank_change"]), -float(row["statement_mass"]), str(row["thread_id"])),
    )[:limit]


def largest_pair_residuals(
    observations: Sequence[Observation], fit: FitResult, limit: int = 15
) -> list[dict[str, object]]:
    """Largest observed-minus-fitted pair discrepancies with usable support."""
    pairs: dict[tuple[str, str], dict[str, object]] = defaultdict(
        lambda: {"a_wins": 0.0, "total": 0.0, "respondents": set(), "rows": 0}
    )
    for obs in observations:
        a, b = sorted((obs.winner, obs.loser))
        record = pairs[(a, b)]
        record["total"] += obs.weight
        record["rows"] += 1
        record["respondents"].add(obs.respondent_id)
        if obs.winner == a:
            record["a_wins"] += obs.weight
    scores = fit.scores
    output: list[dict[str, object]] = []
    for (a, b), record in pairs.items():
        if len(record["respondents"]) < 3:
            continue
        observed = float(record["a_wins"]) / float(record["total"])
        predicted = float(expit(scores[a] - scores[b]))
        output.append(
            {
                "pair": [a, b],
                "observed_a_share": observed,
                "predicted_a_share": predicted,
                "absolute_residual": abs(observed - predicted),
                "respondents": len(record["respondents"]),
                "rows": record["rows"],
            }
        )
    return sorted(
        output,
        key=lambda row: (-float(row["absolute_residual"]), -int(row["respondents"]), row["pair"]),
    )[:limit]


RANK_FIELDS = [
    "rank", "model", "theta", "wins", "losses", "appearances", "segment",
    "p_vs_average", "theta_lo", "theta_hi", "p_lo", "p_hi", "rank_lo",
    "rank_hi", "n_statements", "n_respondents", "n_opponents", "status",
]

SEGMENT_FIELDS = ["scope", *RANK_FIELDS]
SENSITIVITY_FIELDS = [
    "scenario", "rank", "model", "theta", "p_vs_average", "n_statements",
    "n_respondents", "n_opponents", "status", "theta_lo", "theta_hi",
    "p_lo", "p_hi", "rank_lo", "rank_hi",
]
OBSERVATION_FIELDS = [
    "id", "winner", "loser", "analysis_weight", "comfort_axis", "source",
    "evidence", "statement_id", "respondent_id", "thread_id",
    "community_affinity", "url",
    "collection_batch",
]


def _format_value(value: object) -> object:
    if isinstance(value, float):
        return f"{value:.6f}"
    return value


def csv_text(records: Sequence[dict[str, object]], fields: Sequence[str]) -> str:
    handle = io.StringIO(newline="")
    writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    for record in records:
        writer.writerow({field: _format_value(record.get(field, "")) for field in fields})
    return handle.getvalue()


def observation_records(observations: Sequence[Observation]) -> list[dict[str, object]]:
    return [
        {
            "id": o.row_id,
            "winner": o.winner,
            "loser": o.loser,
            "analysis_weight": o.weight,
            "comfort_axis": o.axis,
            "source": o.source,
            "evidence": o.evidence,
            "statement_id": o.statement_id,
            "respondent_id": o.respondent_id,
            "thread_id": o.thread_id,
            "community_affinity": o.community_affinity,
            "url": o.url,
            "collection_batch": o.collection_batch,
        }
        for o in observations
    ]


def diagnostics_markdown(summary: dict[str, object]) -> str:
    global_diag = summary["scopes"]["global"]
    cv = summary["cross_validation"]
    lines = [
        "# Model diagnostics",
        "",
        "Generated by `python3 src/rank.py`. Intervals are corpus-resampling stability intervals, not population confidence intervals.",
        "",
        "## Primary analysis",
        "",
        f"- {summary['primary']['raw_rows']} coded rows; {summary['primary']['observations']} deduplicated pair-axis observations.",
        f"- {summary['primary']['statements']} source statements from {summary['primary']['respondents']} respondent clusters.",
        f"- Total normalized statement mass: {summary['primary']['statement_mass']:.2f}.",
        f"- Global comparison graph: {len(global_diag['components'])} component(s); {global_diag['ranked_models']} models meet coverage rules.",
        f"- {global_diag['unique_pairs']} unique model pairs; {global_diag['cross_segment_observations']} observations cross shopping segments.",
        f"- Graph bridges: {len(global_diag['bridges'])} model-pair edge(s).",
        f"- Optimizer maximum absolute gradient: {global_diag['max_abs_gradient']:.3g}.",
        "",
        "## Grouped predictive check",
        "",
        f"Five-fold respondent-grouped log loss: **{cv['log_loss']:.3f}** (even-odds baseline {cv['even_odds_log_loss']:.3f}).",
        f" Brier score: **{cv['brier']:.3f}** (even-odds baseline {cv['even_odds_brier']:.3f}).",
        "",
        "## Scope connectivity",
        "",
        "| Scope | Observations | Statements | Respondents | Components | Ranked models |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for scope, diag in summary["scopes"].items():
        lines.append(
            f"| {scope} | {diag['observations']} | {diag['statements']} | {diag['respondents']} | "
            f"{len(diag['components'])} | {diag['ranked_models']} |"
        )
    lines.extend([
        "",
        "## Most influential threads",
        "",
        "Leave-one-thread-out changes among coverage-qualified global models.",
        "",
        "| Thread | Statement mass | Rows | Largest rank change | Most affected model |",
        "|---|---:|---:|---:|---|",
    ])
    for row in summary["influential_threads"]:
        lines.append(
            f"| `{row['thread_id']}` | {row['statement_mass']:.2f} | {row['rows']} | "
            f"{row['max_rank_change']} | {row['most_affected_model']} |"
        )
    lines.extend([
        "",
        "## Largest pair residuals",
        "",
        "These supported head-to-heads disagree most with the one-dimensional global scale.",
        "",
        "| Pair (alphabetical) | Observed first-model share | Fitted share | Absolute gap | Respondents |",
        "|---|---:|---:|---:|---:|",
    ])
    for row in summary["largest_pair_residuals"]:
        a, b = row["pair"]
        lines.append(
            f"| {a} / {b} | {row['observed_a_share']:.2f} | {row['predicted_a_share']:.2f} | "
            f"{row['absolute_residual']:.2f} | {row['respondents']} |"
        )
    lines.extend([
        "",
        "## Interpretation guardrails",
        "",
        "- The corpus was assembled purposively and is dominated by Reddit; resampling cannot remove selection bias.",
        "- Global ranks depend on cross-segment bridge comparisons. Segment scores are centered independently and cannot be compared across panels.",
        "- Statements that did not choose a winner are absent, so estimates are conditional on an expressed preference.",
        "- `status` in the ranking CSVs suppresses ranks for disconnected or weakly covered models.",
        "",
    ])
    return "\n".join(lines)


def _percent(value: object) -> str:
    return "—" if value == "" else f"{100 * float(value):.0f}%"


def rankings_markdown(
    global_records: Sequence[dict[str, object]],
    segment_records: Sequence[dict[str, object]],
    summary: dict[str, object],
) -> str:
    primary = summary["primary"]
    lines = [
        "# Global and segment SUV comfort rankings",
        "",
        "These are generated results for preferences expressed in the collected online corpus. They are not a survey of SUV owners. Each source statement has total mass one, and the intervals show stability when respondent clusters are resampled.",
        "",
        f"**Primary corpus:** {primary['observations']} pair-axis judgments from {primary['statements']} statements and {primary['respondents']} respondent clusters. "
        f"See [methodology.md](methodology.md) and [model_diagnostics.md](model_diagnostics.md).",
        "",
        "## Global ranking",
        "",
        "`P vs avg` is the modeled chance of beating an average model on the global latent scale. The 90% columns are corpus-resampling stability ranges, not population confidence intervals.",
        "",
        "| Rank | Model | P vs avg | 90% P range | 90% rank range | Respondents | Opponents |",
        "|---:|---|---:|---:|---:|---:|---:|",
    ]
    for row in global_records:
        if row["status"] != "ranked":
            continue
        rank_range = "—" if row["rank_lo"] == "" else f"{row['rank_lo']}–{row['rank_hi']}"
        lines.append(
            f"| {row['rank']} | {row['model']} | {_percent(row['p_vs_average'])} | "
            f"{_percent(row['p_lo'])}–{_percent(row['p_hi'])} | {rank_range} | "
            f"{row['n_respondents']} | {row['n_opponents']} |"
        )
    withheld = [row for row in global_records if row["status"] != "ranked"]
    if withheld:
        lines.extend([
            "",
            "### Global coverage withheld",
            "",
            "These models remain in the machine table but do not receive an ordinal rank.",
            "",
            "| Model | Status | Respondents | Opponents |",
            "|---|---|---:|---:|",
        ])
        for row in withheld:
            lines.append(
                f"| {row['model']} | `{row['status']}` | {row['n_respondents']} | {row['n_opponents']} |"
            )

    lines.extend([
        "",
        "## Within-segment rankings",
        "",
        "Each segment is fitted only from comparisons whose two models are in that segment. Segment scores are centered separately and cannot be compared across sections.",
    ])
    by_scope: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in segment_records:
        by_scope[str(row["scope"])].append(row)
    titles = {
        "compact": "Compact / small-mid",
        "mid_luxury": "Midsize luxury",
        "family_3row": "Three-row family",
        "flagship": "Flagship / large",
    }
    for scope in ("flagship", "mid_luxury", "family_3row", "compact"):
        lines.extend([
            "",
            f"### {titles[scope]}",
            "",
            "| Rank | Model | P vs segment avg | 90% P range | 90% rank range | Respondents | Opponents |",
            "|---:|---|---:|---:|---:|---:|---:|",
        ])
        for row in by_scope[scope]:
            if row["status"] != "ranked":
                continue
            rank_range = "—" if row["rank_lo"] == "" else f"{row['rank_lo']}–{row['rank_hi']}"
            lines.append(
                f"| {row['rank']} | {row['model']} | {_percent(row['p_vs_average'])} | "
                f"{_percent(row['p_lo'])}–{_percent(row['p_hi'])} | {rank_range} | "
                f"{row['n_respondents']} | {row['n_opponents']} |"
            )
        not_ranked = [row for row in by_scope[scope] if row["status"] != "ranked"]
        if not_ranked:
            text = "; ".join(f"{row['model']} ({row['status']})" for row in not_ranked)
            lines.extend(["", f"Coverage withheld: {text}."])

    lines.extend([
        "",
        "## Sensitivity and diagnostics",
        "",
        "The machine-readable [sensitivity table](../data/ranking_sensitivity.csv) contains owners-only, lived-with-both, neutral-forum, same-team-win exclusion, source, prior, comfort-axis, collection-batch, legacy-weight, and thread-cluster scenarios. Use [model diagnostics](model_diagnostics.md) for connectivity, grouped predictive performance, influential threads, and pair residuals.",
        "",
    ])
    return "\n".join(lines)


def composite_pointer_markdown() -> str:
    return """# Composite ranking retired

The hand-authored composite chain has been replaced by the reproducible [global and segment rankings](rankings.md), which include respondent support, coverage gates, and corpus-resampling stability intervals.

The former chain and research-pass narrative are preserved in [collection_history.md](collection_history.md) as an archival record; they are not current statistical results.
"""


def _write_or_check(path: Path, content: str, check: bool) -> None:
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            raise SystemExit(f"generated file is stale: {path.relative_to(ROOT)}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run_analysis(
    *,
    bootstrap_reps: int = DEFAULT_BOOTSTRAP_REPS,
    seed: int = DEFAULT_SEED,
    check: bool = False,
    influence: bool = True,
) -> dict[str, object]:
    raw_rows = _raw_rows()
    validate_raw_rows(raw_rows)
    primary = build_observations(raw_rows)
    global_records, global_fit, global_diag = analyse_scope(
        "global", primary, bootstrap_reps=bootstrap_reps, seed=seed
    )

    segment_records: list[dict[str, object]] = []
    scope_diagnostics: dict[str, dict[str, object]] = {"global": global_diag}
    for offset, (segment, models) in enumerate(SEGMENTS.items(), 1):
        subset = [o for o in primary if o.winner in models and o.loser in models]
        records, _, diagnostics = analyse_scope(
            segment,
            subset,
            bootstrap_reps=bootstrap_reps,
            seed=seed + offset,
        )
        segment_records.extend(records)
        scope_diagnostics[segment] = diagnostics

    status, eligible = _eligibility(primary, global_fit.names)
    del status
    sensitivity_records = analyse_sensitivities(raw_rows)
    thread_reps = bootstrap_reps // 2
    thread_intervals = _bootstrap_scope(
        primary,
        global_fit,
        eligible,
        reps=thread_reps,
        seed=seed + 100,
        cluster_field="thread_id",
    )
    global_support = _support(primary)
    global_ranks = _rank_map(global_fit.scores, eligible)
    global_status, _ = _eligibility(primary, global_fit.names)
    for model in sorted(global_fit.names, key=lambda name: (-global_fit.scores[name], name)):
        interval = thread_intervals.get(model, {})
        support = global_support[model]
        sensitivity_records.append(
            {
                "scenario": "thread_cluster_bootstrap",
                "rank": global_ranks.get(model, ""),
                "model": model,
                "theta": global_fit.scores[model],
                "p_vs_average": float(expit(global_fit.scores[model])),
                "n_statements": len(support["statements"]),
                "n_respondents": len(support["respondents"]),
                "n_opponents": len(support["opponents"]),
                "status": global_status[model],
                **interval,
            }
        )
    cv = grouped_cross_validation(primary)
    influential = influential_threads(primary, global_fit, eligible) if influence else []
    summary: dict[str, object] = {
        "generated_by": "src/rank.py",
        "seed": seed,
        "bootstrap_reps": bootstrap_reps,
        "thread_bootstrap_reps": thread_reps,
        "estimand": "preferences expressed in the collected online corpus",
        "primary": {
            "raw_rows": len(raw_rows),
            "observations": len(primary),
            "statements": len({o.statement_id for o in primary}),
            "respondents": len({o.respondent_id for o in primary}),
            "threads": len({o.thread_id for o in primary}),
            "statement_mass": sum(o.weight for o in primary),
            "sources": dict(sorted(Counter(o.source for o in primary).items())),
            "axes": dict(sorted(Counter(o.axis for o in primary).items())),
            "collection_batches": dict(sorted(Counter(o.collection_batch for o in primary).items())),
        },
        "coverage_rules": {
            "min_respondents": MIN_RESPONDENTS,
            "min_opponents": MIN_OPPONENTS,
        },
        "scopes": scope_diagnostics,
        "cross_validation": cv,
        "influential_threads": influential,
        "largest_pair_residuals": largest_pair_residuals(primary, global_fit),
    }

    owners_compat, _, _ = analyse_scope(
        "owners_only",
        build_observations(raw_rows, evidence=OWNER_EVIDENCE),
        bootstrap_reps=0,
        seed=seed,
    )

    generated = {
        ROOT / "data" / "ranking.csv": csv_text(global_records, RANK_FIELDS),
        ROOT / "data" / "ranking_segments.csv": csv_text(segment_records, SEGMENT_FIELDS),
        ROOT / "data" / "ranking_sensitivity.csv": csv_text(sensitivity_records, SENSITIVITY_FIELDS),
        ROOT / "data" / "ranking_owners.csv": csv_text(owners_compat, RANK_FIELDS),
        ROOT / "data" / "analysis_observations.csv": csv_text(observation_records(primary), OBSERVATION_FIELDS),
        ROOT / "data" / "analysis_summary.json": json.dumps(summary, indent=2, sort_keys=True) + "\n",
        ROOT / "reports" / "model_diagnostics.md": diagnostics_markdown(summary),
        ROOT / "reports" / "rankings.md": rankings_markdown(global_records, segment_records, summary),
        ROOT / "reports" / "composite_ranking.md": composite_pointer_markdown(),
    }
    for path, content in generated.items():
        _write_or_check(path, content, check)

    print(
        f"Primary corpus: {len(primary)} pair-axis observations from "
        f"{summary['primary']['statements']} statements / {summary['primary']['respondents']} respondent clusters"
    )
    print(
        f"Global fit: {len(global_fit.names)} models; max |gradient| "
        f"{global_fit.max_abs_gradient:.2g}; {bootstrap_reps} respondent-cluster bootstrap refits"
    )
    print(
        f"Grouped CV log loss {cv['log_loss']:.3f} vs {cv['even_odds_log_loss']:.3f} even-odds baseline"
    )
    return summary


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bootstrap-reps", type=int, default=DEFAULT_BOOTSTRAP_REPS)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--no-bootstrap", action="store_true", help="skip resampling intervals")
    parser.add_argument("--skip-influence", action="store_true", help="skip leave-one-thread-out diagnostics")
    parser.add_argument("--check", action="store_true", help="fail if generated analysis files are stale")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    reps = 0 if args.no_bootstrap else args.bootstrap_reps
    if reps < 0:
        raise SystemExit("--bootstrap-reps must be non-negative")
    run_analysis(
        bootstrap_reps=reps,
        seed=args.seed,
        check=args.check,
        influence=not args.skip_influence,
    )


if __name__ == "__main__":
    main()
