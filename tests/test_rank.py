from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import numpy as np
import pytest
from scipy.special import expit

from src import rank


def observation(
    winner: str,
    loser: str,
    index: int,
    *,
    weight: float = 1.0,
    respondent: str | None = None,
    statement: str | None = None,
) -> rank.Observation:
    """Create a small, fully identified observation for model-level tests."""
    return rank.Observation(
        row_id=f"row-{index}",
        winner=winner,
        loser=loser,
        weight=weight,
        axis="overall",
        source="test",
        evidence="owned_both",
        url=f"https://example.test/thread#{index}",
        statement_id=statement or f"statement-{index}",
        respondent_id=respondent or f"respondent-{index}",
        thread_id=f"thread-{index}",
        community_affinity="neutral",
        collection_batch="test-fixture",
    )


def raw_row(
    index: int,
    winner: str,
    loser: str,
    *,
    statement: str,
    respondent: str,
    axis: str = "overall",
) -> dict[str, str]:
    """Create a valid comparison row for preprocessing tests."""
    return {
        "id": f"raw-{index}",
        "winner": winner,
        "loser": loser,
        "comfort_axis": axis,
        "evidence": "owned_both",
        "source": "reddit",
        "url": f"https://example.test/comments/thread/comment-{index}",
        "quote": f"comparison {index}",
        "statement_id": statement,
        "respondent_id": respondent,
        "thread_id": "thread-1",
        "community_affinity": "neutral",
        "collection_batch": "test-fixture",
        "home_team": "0",
    }


def round_robin_observations() -> list[rank.Observation]:
    """All four models face all opponents and clear both coverage thresholds."""
    rows: list[rank.Observation] = []
    index = 0
    models = ["A", "B", "C", "D"]
    for left_index, left in enumerate(models):
        for right in models[left_index + 1 :]:
            rows.append(observation(left, right, index))
            index += 1
            rows.append(observation(right, left, index))
            index += 1
    return rows


def test_analytic_gradient_matches_finite_differences(monkeypatch: pytest.MonkeyPatch) -> None:
    rows = [
        observation("A", "B", 1, weight=3.0),
        observation("B", "C", 2, weight=2.0),
        observation("A", "C", 3, weight=1.5),
        observation("C", "A", 4, weight=0.5),
    ]
    original_minimize = rank.minimize
    comparisons: list[tuple[np.ndarray, np.ndarray]] = []

    def checking_minimize(function, initial, *args, **kwargs):
        point = np.linspace(-0.35, 0.4, len(initial))
        _, analytic = function(point)
        epsilon = 1e-6
        numerical = np.empty_like(point)
        for coordinate in range(len(point)):
            step = np.zeros_like(point)
            step[coordinate] = epsilon
            numerical[coordinate] = (
                function(point + step)[0] - function(point - step)[0]
            ) / (2.0 * epsilon)
        comparisons.append((analytic, numerical))
        return original_minimize(function, initial, *args, **kwargs)

    monkeypatch.setattr(rank, "minimize", checking_minimize)
    fit = rank.fit_bradley_terry(rows)

    assert fit.success
    assert comparisons
    for analytic, numerical in comparisons:
        np.testing.assert_allclose(analytic, numerical, rtol=1e-6, atol=1e-7)


def test_fit_recovers_known_synthetic_scores() -> None:
    true_scores = {"A": 1.0, "B": 0.0, "C": -1.0}
    rows: list[rank.Observation] = []
    index = 0
    total_pair_mass = 5_000.0
    for left, right in (("A", "B"), ("A", "C"), ("B", "C")):
        probability = float(expit(true_scores[left] - true_scores[right]))
        rows.append(observation(left, right, index, weight=total_pair_mass * probability))
        index += 1
        rows.append(observation(right, left, index, weight=total_pair_mass * (1.0 - probability)))
        index += 1

    scores = rank.fit_bradley_terry(rows).scores

    assert scores["A"] > scores["B"] > scores["C"]
    for model, expected in true_scores.items():
        assert scores[model] == pytest.approx(expected, abs=0.01)


def test_regularization_keeps_undefeated_model_estimates_finite() -> None:
    rows = [
        observation("A", "B", 1, weight=100.0),
        observation("A", "C", 2, weight=100.0),
        observation("B", "C", 3, weight=100.0),
    ]

    fit = rank.fit_bradley_terry(rows)

    assert fit.success
    assert np.all(np.isfinite(fit.theta))
    assert fit.max_abs_gradient < 1e-6
    assert fit.scores["A"] > fit.scores["B"] > fit.scores["C"]


def test_graph_components_are_separated_and_deterministic() -> None:
    rows = [
        observation("B", "C", 1),
        observation("A", "B", 2),
        observation("Y", "X", 3),
    ]

    assert rank.graph_components(rows) == [{"A", "B", "C"}, {"X", "Y"}]


def test_each_retained_statement_has_total_weight_one() -> None:
    rows = [
        raw_row(1, "A", "B", statement="statement-a", respondent="person-a"),
        raw_row(2, "A", "C", statement="statement-a", respondent="person-a"),
        raw_row(3, "D", "A", statement="statement-b", respondent="person-b"),
    ]

    observations = rank.build_observations(rows)
    mass: dict[str, float] = defaultdict(float)
    for item in observations:
        mass[item.statement_id] += item.weight

    assert mass == pytest.approx({"statement-a": 1.0, "statement-b": 1.0})
    assert sorted(item.weight for item in observations) == [0.5, 0.5, 1.0]


def test_repeated_same_direction_judgments_collapse_to_first_row() -> None:
    rows = [
        raw_row(1, "A", "B", statement="statement-1", respondent="person-a"),
        raw_row(2, "A", "B", statement="statement-2", respondent="person-a"),
        raw_row(3, "C", "D", statement="statement-3", respondent="person-b"),
    ]

    observations = rank.build_observations(rows)

    assert [item.row_id for item in observations] == ["raw-1", "raw-3"]
    assert all(item.weight == 1.0 for item in observations)


def test_conflicting_directions_from_one_respondent_cancel() -> None:
    rows = [
        raw_row(1, "A", "B", statement="statement-1", respondent="person-a"),
        raw_row(2, "B", "A", statement="statement-2", respondent="person-a"),
        raw_row(3, "C", "D", statement="statement-3", respondent="person-b"),
    ]

    observations = rank.build_observations(rows)

    assert [(item.winner, item.loser) for item in observations] == [("C", "D")]


def test_coverage_rules_gate_rank_and_distinguish_failure_reasons() -> None:
    rows = [
        observation("A", "B", 1, respondent="r1"),
        observation("A", "B", 2, respondent="r2"),
        observation("A", "C", 3, respondent="r3"),
        observation("A", "C", 4, respondent="r4"),
        observation("D", "A", 5, respondent="r5"),
        observation("E", "A", 6, respondent="e1"),
        observation("E", "A", 7, respondent="e2"),
        observation("E", "A", 8, respondent="e3"),
        observation("E", "B", 9, respondent="e4"),
        observation("E", "B", 10, respondent="e5"),
        observation("X", "Y", 11, respondent="x1"),
        observation("X", "Y", 12, respondent="x2"),
        observation("X", "Y", 13, respondent="x3"),
        observation("X", "Y", 14, respondent="x4"),
        observation("X", "Y", 15, respondent="x5"),
    ]

    records, _, _ = rank.analyse_scope("test", rows, bootstrap_reps=0, seed=17)
    by_model = {str(record["model"]): record for record in records}

    assert by_model["A"]["status"] == "ranked"
    assert by_model["A"]["rank"] == 1
    assert by_model["E"]["status"] == "insufficient_opponents"
    assert by_model["B"]["status"] == "insufficient_respondents"
    assert by_model["X"]["status"] == "disconnected"
    assert by_model["Y"]["status"] == "disconnected"
    assert by_model["E"]["rank"] == ""


def test_seeded_bootstrap_analysis_is_deterministic() -> None:
    rows = round_robin_observations()

    first_records, first_fit, first_diagnostics = rank.analyse_scope(
        "test", rows, bootstrap_reps=6, seed=20260819
    )
    second_records, second_fit, second_diagnostics = rank.analyse_scope(
        "test", rows, bootstrap_reps=6, seed=20260819
    )

    assert first_records == second_records
    np.testing.assert_array_equal(first_fit.theta, second_fit.theta)
    assert first_diagnostics == second_diagnostics
    assert all(record["rank_lo"] != "" for record in first_records)


def test_grouped_cross_validation_is_finite_and_repeatable() -> None:
    rows = round_robin_observations()

    first = rank.grouped_cross_validation(rows, folds=3)
    second = rank.grouped_cross_validation(rows, folds=3)

    assert first == second
    assert first["folds"] == 3
    assert np.isfinite(first["log_loss"])
    assert np.isfinite(first["brier"])
    assert first["even_odds_log_loss"] == pytest.approx(np.log(2.0))
    assert first["even_odds_brier"] == 0.25


def test_csv_generation_is_stable_and_formats_floats() -> None:
    records = [{"model": "A", "theta": 1.0 / 3.0}, {"model": "B", "theta": -1.25}]

    generated = rank.csv_text(records, ["model", "theta"])

    assert generated == "model,theta\nA,0.333333\nB,-1.250000\n"


def test_generated_file_write_and_check_use_only_requested_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(rank, "ROOT", tmp_path)
    destination = tmp_path / "data" / "result.csv"

    rank._write_or_check(destination, "model,theta\nA,0.000000\n", check=False)
    rank._write_or_check(destination, "model,theta\nA,0.000000\n", check=True)
    destination.write_text("stale\n", encoding="utf-8")

    with pytest.raises(SystemExit, match=r"generated file is stale: data/result\.csv"):
        rank._write_or_check(destination, "model,theta\nA,0.000000\n", check=True)
