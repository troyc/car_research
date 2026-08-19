#!/usr/bin/env python3
"""Generate the publication figures from ``rank.py`` outputs.

The figures deliberately do not read ``comparisons.csv``: ranking results come
from the generated ranking tables, while all matchup and coverage counts are
recomputed from the exact primary sample in ``analysis_observations.csv``.

Typical use::

    python3 src/plot.py
    python3 src/plot.py --only global segment --dpi 160

On Nix (when matplotlib is not installed system-wide)::

    nix-shell -p python3Packages.matplotlib python3Packages.numpy \
      --run "python3 src/plot.py"

Outputs (under ``reports/figures`` by default):

* ``global_rank_stability.png`` — all globally ranked models and 90% intervals
* ``segment_rankings.png`` — four within-segment rankings
* ``sensitivity.png`` — probability changes, never cross-fit rank changes
* ``direct_matchups.png`` — best-supported direct pairs, split by comfort axis
* ``coverage_graph.png`` — diagnostic comparison network
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DEFAULT_OUT = ROOT / "reports" / "figures"

# A muted, colorblind-safe palette (Okabe-Ito plus neutral ink).
BG = "#F5F2EB"
PANEL = "#FFFCF7"
INK = "#24201D"
MUTED = "#706A65"
FAINT = "#D8D2CA"
REFERENCE = "#9A948D"

SEG_ORDER = ["flagship", "mid_luxury", "family_3row", "compact"]
SEG_TITLE = {
    "flagship": "Flagship / large",
    "mid_luxury": "Midsize luxury",
    "family_3row": "Three-row family",
    "compact": "Compact / small-mid",
}
SEG_COLOR = {
    "flagship": "#0072B2",
    "mid_luxury": "#CC79A7",
    "family_3row": "#D55E00",
    "compact": "#009E73",
}

AXIS_ORDER = ["ride", "seats", "nvh", "long_trip", "overall"]
AXIS_TITLE = {
    "ride": "Ride",
    "seats": "Seats",
    "nvh": "Quiet / NVH",
    "long_trip": "Long-trip",
    "overall": "Overall",
}
AXIS_COLOR = {
    "ride": "#0072B2",
    "seats": "#E69F00",
    "nvh": "#009E73",
    "long_trip": "#CC79A7",
    "overall": "#8C8C8C",
}

SCENARIO_TITLE = {
    "primary": "Primary",
    "owners_only": "Owners only",
    "neutral_forums": "Neutral forums",
}
SCENARIO_COLOR = {
    "primary": "#0072B2",
    "owners_only": "#D55E00",
    "neutral_forums": "#009E73",
}
SCENARIO_MARKER = {"primary": "o", "owners_only": "s", "neutral_forums": "^"}

# Short labels keep dense, complete charts legible.
DISPLAY = {
    "Mercedes EQS SUV": "EQS SUV",
    "Mercedes GLS": "GLS",
    "Mercedes GLE": "GLE",
    "Mercedes GLE AMG": "GLE AMG",
    "Mercedes GLC": "GLC",
    "Range Rover Sport": "RR Sport",
    "Land Rover Defender": "Defender",
    "Lincoln Aviator": "Aviator",
    "Lincoln Nautilus": "Nautilus",
    "Lincoln Navigator": "Navigator",
    "Lincoln Corsair": "Corsair",
    "Cadillac Escalade": "Escalade",
    "Cadillac Escalade IQ": "Escalade IQ",
    "Cadillac XT6": "XT6",
    "Cadillac XT5": "XT5",
    "BMW X5": "X5",
    "BMW X7": "X7",
    "BMW X3": "X3",
    "BMW X1": "X1",
    "BMW iX": "iX",
    "Audi Q8": "Q8",
    "Audi Q7": "Q7",
    "Audi Q5": "Q5",
    "Lexus LX": "LX",
    "Lexus GX": "GX 460",
    "Lexus GX 550": "GX 550",
    "Lexus RX": "RX",
    "Lexus NX": "NX",
    "Lexus TX": "TX",
    "Genesis GV80": "GV80",
    "Genesis GV70": "GV70",
    "Acura MDX": "MDX",
    "Volvo XC90": "XC90",
    "Volvo XC60": "XC60",
    "Porsche Cayenne": "Cayenne",
    "Porsche Macan": "Macan",
    "Jeep Grand Cherokee": "Grand Cherokee",
    "Jeep Grand Cherokee L": "Grand Cherokee L",
    "Jeep Grand Wagoneer": "Grand Wagoneer",
    "GMC Yukon": "Yukon",
    "Chevrolet Tahoe": "Tahoe",
    "Chevrolet Suburban": "Suburban",
    "Infiniti QX80": "QX80",
    "Toyota Sequoia": "Sequoia",
    "Toyota Highlander": "Highlander",
    "Toyota Grand Highlander": "Grand Highlander",
    "Toyota Venza": "Venza",
    "Toyota RAV4": "RAV4",
    "Toyota 4Runner": "4Runner",
    "Toyota Land Cruiser": "Land Cruiser",
    "Honda Pilot": "Pilot",
    "Honda CR-V": "CR-V",
    "Honda Passport": "Passport",
    "Hyundai Palisade": "Palisade",
    "Hyundai Santa Fe": "Santa Fe",
    "Kia Telluride": "Telluride",
    "Kia Sorento": "Sorento",
    "Subaru Ascent": "Ascent",
    "Subaru Outback": "Outback '20–25",
    "Subaru Outback 2026": "Outback 2026",
    "Subaru Crosstrek": "Crosstrek",
    "Subaru Forester": "Forester",
    "Nissan Pathfinder": "Pathfinder",
    "Nissan Murano": "Murano",
    "Volkswagen Atlas": "Atlas",
    "Volkswagen Tiguan": "Tiguan",
    "Mazda CX-9": "CX-9",
    "Mazda CX-5": "CX-5",
    "Mazda CX-50": "CX-50",
    "Mazda CX-90": "CX-90",
    "Buick Enclave": "Enclave",
    "Ford Explorer": "Explorer",
    "Ford Expedition": "Expedition",
    "Rivian R1S": "R1S",
    "Tesla Model X": "Model X",
    "Tesla Model Y": "Model Y",
}


def display_name(name: str) -> str:
    return DISPLAY.get(name, name)


def as_float(value: str | None) -> float | None:
    if value is None or not value.strip():
        return None
    try:
        number = float(value)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def as_int(value: str | None) -> int:
    number = as_float(value)
    return int(number) if number is not None else 0


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_summary(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def require_columns(rows: list[dict[str, str]], path: Path, columns: Iterable[str]) -> None:
    if not rows:
        raise ValueError(f"{path} has no data rows")
    missing = set(columns) - set(rows[0])
    if missing:
        raise ValueError(f"{path} is missing columns: {', '.join(sorted(missing))}")


def style_axis(ax) -> None:
    ax.set_facecolor(PANEL)
    ax.tick_params(colors=INK, labelsize=8)
    for spine in ax.spines.values():
        spine.set_color(FAINT)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def add_header(fig, title: str, subtitle: str, left: float = 0.04) -> None:
    fig.text(left, 0.975, title, ha="left", va="top", fontsize=18, weight="semibold", color=INK)
    fig.text(left, 0.944, subtitle, ha="left", va="top", fontsize=9.2, color=MUTED)


def add_footer(fig, text: str, left: float = 0.04) -> None:
    fig.text(left, 0.012, text, ha="left", va="bottom", fontsize=7.4, color=MUTED)


def save(fig, path: Path, dpi: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.patch.set_facecolor(BG)
    fig.savefig(path, dpi=dpi, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"wrote {path}")


def bootstrap_note(summary: dict, rows: list[dict[str, str]]) -> str:
    reps = summary.get("bootstrap_reps")
    has_intervals = any(as_float(row.get("p_lo")) is not None for row in rows)
    if not has_intervals:
        return "intervals unavailable (--no-bootstrap run)"
    if reps:
        return f"90% respondent-cluster bootstrap interval ({reps:,} resamples)"
    return "90% respondent-cluster bootstrap interval"


def draw_probability_forest(ax, rows: list[dict[str, str]], *, coverage: bool = True) -> None:
    """Draw ordered p-versus-average rows on one axis."""
    ys = list(range(len(rows)))[::-1]
    for y, row in zip(ys, rows):
        p = as_float(row.get("p_vs_average"))
        if p is None:
            continue
        lo, hi = as_float(row.get("p_lo")), as_float(row.get("p_hi"))
        color = SEG_COLOR.get(row.get("segment", ""), INK)
        if lo is not None and hi is not None:
            ax.hlines(y, lo, hi, color=color, lw=1.25, alpha=0.72, zorder=2)
        ax.scatter(p, y, s=23, color=color, edgecolor=PANEL, linewidth=0.45, zorder=3)

    labels = []
    for row in rows:
        rank = row.get("rank", "").strip()
        labels.append(f"{rank:>2}  {display_name(row['model'])}")
    ax.set_yticks(ys)
    ax.set_yticklabels(labels, fontsize=7.25)
    ax.tick_params(axis="y", length=0, pad=4)
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.axvline(0.5, color=REFERENCE, lw=0.9, ls="--", zorder=0)
    ax.grid(axis="x", color=FAINT, lw=0.55, zorder=0)
    ax.set_ylim(-1, len(rows))
    ax.set_xlabel("modeled chance of beating an average model", fontsize=8.2, color=MUTED)
    style_axis(ax)

    if coverage:
        for y, row in zip(ys, rows):
            respondents = as_int(row.get("n_respondents"))
            opponents = as_int(row.get("n_opponents"))
            ax.text(
                1.012,
                y,
                f"{respondents}r · {opponents}o",
                transform=ax.get_yaxis_transform(),
                ha="left",
                va="center",
                fontsize=6.4,
                color=MUTED,
                clip_on=False,
            )


def plot_global_rank_stability(
    ranking: list[dict[str, str]], summary: dict, destination: Path, dpi: int
) -> None:
    ranked = [row for row in ranking if row.get("status") == "ranked" and row.get("rank", "").strip()]
    ranked.sort(key=lambda row: as_int(row["rank"]))
    split = math.ceil(len(ranked) / 2)
    pages = [ranked[:split], ranked[split:]]
    fig, axes = plt.subplots(1, 2, figsize=(16.0, 15.7))
    fig.subplots_adjust(left=0.13, right=0.93, top=0.895, bottom=0.057, wspace=0.33)

    for index, (ax, rows) in enumerate(zip(axes, pages)):
        draw_probability_forest(ax, rows)
        ax.set_title(
            f"Ranks {rows[0]['rank']}–{rows[-1]['rank']}   ·   respondents / opponents →",
            fontsize=9.2,
            color=INK,
            loc="left",
            pad=8,
        )
        if index == 1:
            ax.set_ylabel("")

    excluded = len(ranking) - len(ranked)
    primary = summary.get("primary", {})
    add_header(
        fig,
        "Global comfort ranking: estimate and stability",
        "Every coverage-qualified model is shown. Farther right means more often preferred in this collected online corpus.",
        left=0.035,
    )
    fig.text(
        0.035,
        0.918,
        f"Dots are regularized Bradley–Terry estimates; lines are the {bootstrap_note(summary, ranking)}. "
        f"{excluded} model{'s' if excluded != 1 else ''} without minimum coverage {'are' if excluded != 1 else 'is'} not ranked.",
        ha="left",
        va="top",
        fontsize=8.4,
        color=MUTED,
    )
    add_footer(
        fig,
        f"Primary sample: {primary.get('statements', '—')} statements from "
        f"{primary.get('respondents', '—')} respondents · r = respondents · o = distinct opponents · "
        "Intervals describe resampling stability, not population sampling error.",
        left=0.035,
    )
    save(fig, destination, dpi)


def plot_segment_rankings(
    ranking: list[dict[str, str]], summary: dict, destination: Path, dpi: int
) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(16.0, 17.0))
    fig.subplots_adjust(left=0.14, right=0.93, top=0.89, bottom=0.055, wspace=0.34, hspace=0.17)

    for ax, scope in zip(axes.flat, SEG_ORDER):
        rows = [row for row in ranking if row.get("scope") == scope]
        rows.sort(key=lambda row: (-(as_float(row.get("p_vs_average")) or 0.0), row["model"]))
        ys = list(range(len(rows)))[::-1]
        for y, row in zip(ys, rows):
            p = as_float(row.get("p_vs_average"))
            if p is None:
                continue
            qualified = row.get("status") == "ranked"
            color = SEG_COLOR[scope] if qualified else REFERENCE
            lo, hi = as_float(row.get("p_lo")), as_float(row.get("p_hi"))
            if lo is not None and hi is not None:
                ax.hlines(y, lo, hi, color=color, lw=1.2, alpha=0.72, zorder=2)
            ax.scatter(
                p,
                y,
                s=25,
                facecolor=color if qualified else PANEL,
                edgecolor=color,
                linewidth=1.0,
                zorder=3,
            )

        labels = []
        for row in rows:
            marker = "" if row.get("status") == "ranked" else "†"
            labels.append(f"{marker}{display_name(row['model'])}")
        ax.set_yticks(ys)
        ax.set_yticklabels(labels, fontsize=7.25)
        ax.tick_params(axis="y", length=0, pad=4)
        ax.set_xlim(0, 1)
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
        ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
        ax.axvline(0.5, color=REFERENCE, lw=0.85, ls="--", zorder=0)
        ax.grid(axis="x", color=FAINT, lw=0.55, zorder=0)
        ax.set_ylim(-1, len(rows))
        ax.set_xlabel("chance vs this segment's average", fontsize=8.1, color=MUTED)
        style_axis(ax)

        for y, row in zip(ys, rows):
            ax.text(
                1.012,
                y,
                f"{as_int(row.get('n_respondents'))}r · {as_int(row.get('n_opponents'))}o",
                transform=ax.get_yaxis_transform(),
                ha="left",
                va="center",
                fontsize=6.35,
                color=MUTED,
                clip_on=False,
            )
        qualified_count = sum(row.get("status") == "ranked" for row in rows)
        ax.set_title(
            f"{SEG_TITLE[scope]}   ·   {qualified_count}/{len(rows)} coverage-qualified",
            loc="left",
            fontsize=10.2,
            color=SEG_COLOR[scope],
            weight="semibold",
            pad=8,
        )

    add_header(
        fig,
        "Comfort rankings within each shopping segment",
        "Each panel is a separate Bradley–Terry fit. Probabilities—and ranks—should only be compared within the same panel.",
        left=0.035,
    )
    fig.text(
        0.035,
        0.915,
        f"Lines show the {bootstrap_note(summary, ranking)}. † Open markers miss the minimum respondent or opponent coverage and are not assigned a rank.",
        ha="left",
        va="top",
        fontsize=8.4,
        color=MUTED,
    )
    add_footer(
        fig,
        "r = respondents · o = distinct opponents · 50% is the average model in that segment · "
        "Interval width reveals instability from sparse or influential comparison paths.",
        left=0.035,
    )
    save(fig, destination, dpi)


def plot_sensitivity(
    global_ranking: list[dict[str, str]],
    sensitivity: list[dict[str, str]],
    destination: Path,
    dpi: int,
) -> None:
    scenarios = ["primary", "owners_only", "neutral_forums"]
    maps: dict[str, dict[str, dict[str, str]]] = {
        "primary": {row["model"]: row for row in global_ranking if row.get("status") == "ranked"}
    }
    for scenario in scenarios[1:]:
        maps[scenario] = {
            row["model"]: row
            for row in sensitivity
            if row.get("scenario") == scenario and row.get("status") == "ranked"
        }
    models = set.intersection(*(set(maps[scenario]) for scenario in scenarios))
    ordered = sorted(
        models,
        key=lambda model: -(as_float(maps["primary"][model].get("p_vs_average")) or 0.0),
    )

    height = max(8.5, 0.43 * len(ordered) + 2.5)
    fig, ax = plt.subplots(figsize=(13.8, height))
    fig.subplots_adjust(left=0.22, right=0.965, top=0.85, bottom=0.095)
    ys = list(range(len(ordered)))[::-1]
    for y, model in zip(ys, ordered):
        ps = [as_float(maps[scenario][model].get("p_vs_average")) for scenario in scenarios]
        values = [p for p in ps if p is not None]
        if values:
            ax.hlines(y, min(values), max(values), color=FAINT, lw=1.4, zorder=1)
        for scenario, p in zip(scenarios, ps):
            if p is None:
                continue
            ax.scatter(
                p,
                y,
                s=35,
                color=SCENARIO_COLOR[scenario],
                marker=SCENARIO_MARKER[scenario],
                edgecolor=PANEL,
                linewidth=0.45,
                zorder=3,
            )

    ax.set_yticks(ys)
    ax.set_yticklabels([display_name(model) for model in ordered], fontsize=8.1)
    ax.tick_params(axis="y", length=0, pad=5)
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.axvline(0.5, color=REFERENCE, lw=0.85, ls="--", zorder=0)
    ax.grid(axis="x", color=FAINT, lw=0.55, zorder=0)
    ax.set_ylim(-1, len(ordered))
    ax.set_xlabel("modeled chance of beating the average model in that fit", fontsize=8.5, color=MUTED)
    style_axis(ax)

    handles = [
        Line2D(
            [0],
            [0],
            marker=SCENARIO_MARKER[scenario],
            color="none",
            markerfacecolor=SCENARIO_COLOR[scenario],
            markeredgecolor=PANEL,
            markersize=7,
            label=SCENARIO_TITLE[scenario],
        )
        for scenario in scenarios
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False, ncol=3, fontsize=8.4)
    add_header(
        fig,
        "Source sensitivity: how modeled probabilities move",
        "The chart compares probabilities—not ranks—because each scenario contains a different set and amount of evidence.",
        left=0.045,
    )
    fig.text(
        0.045,
        0.898,
        f"Shown: all {len(ordered)} models that meet coverage rules in the primary, owners-only, and neutral-forum fits. "
        "Shorter horizontal spans indicate less sensitivity to those source restrictions.",
        ha="left",
        va="top",
        fontsize=8.4,
        color=MUTED,
    )
    add_footer(
        fig,
        "Each 50% reference is the average model within that scenario. Movement can reflect both evidence removal and a changed fit baseline; it is not a bias correction.",
        left=0.045,
    )
    save(fig, destination, dpi)


def aggregate_pairs(observations: list[dict[str, str]]) -> list[dict]:
    pairs: dict[tuple[str, str], dict] = {}
    for row in observations:
        winner, loser = row["winner"].strip(), row["loser"].strip()
        if not winner or not loser or winner == loser:
            continue
        a, b = sorted((winner, loser))
        record = pairs.setdefault(
            (a, b),
            {
                "a": a,
                "b": b,
                "directions": {a: defaultdict(float), b: defaultdict(float)},
                "statements": set(),
                "respondents": set(),
                "mass": 0.0,
            },
        )
        weight = as_float(row.get("analysis_weight")) or 0.0
        axis = row.get("comfort_axis", "overall") or "overall"
        record["directions"][winner][axis] += weight
        record["mass"] += weight
        if row.get("statement_id"):
            record["statements"].add(row["statement_id"])
        if row.get("respondent_id"):
            record["respondents"].add(row["respondent_id"])
    return list(pairs.values())


def axis_order(records: list[dict]) -> list[str]:
    present = {
        axis
        for record in records
        for direction in record["directions"].values()
        for axis in direction
    }
    return [axis for axis in AXIS_ORDER if axis in present] + sorted(present - set(AXIS_ORDER))


def plot_direct_matchups(
    observations: list[dict[str, str]], summary: dict, destination: Path, dpi: int
) -> None:
    pairs = aggregate_pairs(observations)
    top = sorted(pairs, key=lambda record: (-record["mass"], record["a"], record["b"]))[:18]
    top.reverse()
    axes_present = axis_order(top)
    max_side = max(
        (
            sum(direction.values())
            for record in top
            for direction in record["directions"].values()
        ),
        default=1.0,
    )

    fig, ax = plt.subplots(figsize=(15.4, 11.5))
    fig.subplots_adjust(left=0.30, right=0.88, top=0.855, bottom=0.10)
    pair_labels = []
    for y, record in enumerate(top):
        a, b = record["a"], record["b"]
        a_mass = sum(record["directions"][a].values())
        b_mass = sum(record["directions"][b].values())
        preferred, other = (a, b) if a_mass >= b_mass else (b, a)
        preferred_mass, other_mass = max(a_mass, b_mass), min(a_mass, b_mass)

        right = 0.0
        left = 0.0
        for axis_name in axes_present:
            value = record["directions"][preferred].get(axis_name, 0.0)
            if value:
                ax.barh(y, value, left=right, height=0.68, color=AXIS_COLOR.get(axis_name, MUTED), zorder=3)
                right += value
            value = record["directions"][other].get(axis_name, 0.0)
            if value:
                ax.barh(y, -value, left=-left, height=0.68, color=AXIS_COLOR.get(axis_name, MUTED), alpha=0.72, zorder=3)
                left += value

        pair_labels.append(f"{display_name(other)}  ←  |  →  {display_name(preferred)}")

        def compact(value: float) -> str:
            return f"{value:.1f}".rstrip("0").rstrip(".")

        ax.text(
            1.01,
            y,
            f"{compact(preferred_mass)}–{compact(other_mass)} · {len(record['respondents'])}r",
            transform=ax.get_yaxis_transform(),
            ha="left",
            va="center",
            fontsize=7.2,
            color=MUTED,
            clip_on=False,
        )

    bound = max_side * 1.08
    ax.set_xlim(-bound, bound)
    ax.set_ylim(-1, len(top))
    ax.set_yticks(range(len(top)))
    ax.set_yticklabels(pair_labels, fontsize=7.7)
    ax.tick_params(axis="y", length=0, pad=7)
    ax.axvline(0, color=INK, lw=0.75, zorder=4)
    ax.grid(axis="x", color=FAINT, lw=0.55, zorder=0)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _position: f"{abs(value):g}"))
    ax.set_xlabel("weighted statement mass favoring each model", fontsize=8.5, color=MUTED)
    style_axis(ax)
    handles = [
        Patch(facecolor=AXIS_COLOR.get(axis_name, MUTED), label=AXIS_TITLE.get(axis_name, axis_name.replace("_", " ").title()))
        for axis_name in axes_present
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False, ncol=min(5, len(handles)), fontsize=8.2)

    primary = summary.get("primary", {})
    add_header(
        fig,
        "Best-supported direct comfort matchups",
        "The 18 pairs with the most primary-sample evidence. The majority-preferred model is on the right; color shows the comfort axis.",
        left=0.045,
    )
    fig.text(
        0.045,
        0.900,
        "Split statements contribute fractional mass, so totals need not be whole numbers. These are direct observations—not model-implied matchups.",
        ha="left",
        va="top",
        fontsize=8.4,
        color=MUTED,
    )
    add_footer(
        fig,
        f"Computed only from analysis_observations.csv: {primary.get('observations', len(observations))} coded observations · "
        f"{primary.get('statements', '—')} statements · r = distinct respondents for that pair.",
        left=0.045,
    )
    save(fig, destination, dpi)


def plot_coverage_graph(
    ranking: list[dict[str, str]],
    observations: list[dict[str, str]],
    summary: dict,
    destination: Path,
    dpi: int,
) -> None:
    by_model = {row["model"]: row for row in ranking}
    pairs = aggregate_pairs(observations)
    # A two-statement-mass cutoff keeps the network diagnostic legible. Counts
    # in the subtitle make the filtering explicit.
    threshold = 2.0
    shown_pairs = [record for record in pairs if record["mass"] >= threshold]

    node_respondents: dict[str, set[str]] = defaultdict(set)
    node_mass: dict[str, float] = defaultdict(float)
    for row in observations:
        weight = as_float(row.get("analysis_weight")) or 0.0
        for model in (row["winner"], row["loser"]):
            node_mass[model] += weight
            if row.get("respondent_id"):
                node_respondents[model].add(row["respondent_id"])

    x_base = {segment: index for index, segment in enumerate(SEG_ORDER)}
    positions: dict[str, tuple[float, float]] = {}
    for segment in SEG_ORDER:
        rows = [row for row in ranking if row.get("segment") == segment]
        rows.sort(key=lambda row: (-(as_float(row.get("p_vs_average")) or 0.0), row["model"]))
        offsets = [0.0, -0.14, 0.14, -0.27, 0.27]
        for index, row in enumerate(rows):
            p = as_float(row.get("p_vs_average"))
            if p is not None:
                positions[row["model"]] = (x_base[segment] + offsets[index % len(offsets)], p)

    fig, ax = plt.subplots(figsize=(16.0, 13.5))
    fig.subplots_adjust(left=0.075, right=0.975, top=0.87, bottom=0.09)
    within_count = 0
    cross_count = 0
    for record in shown_pairs:
        a, b = record["a"], record["b"]
        if a not in positions or b not in positions:
            continue
        segment_a = by_model[a].get("segment", "")
        segment_b = by_model[b].get("segment", "")
        same_segment = segment_a == segment_b
        if same_segment:
            within_count += 1
            color, alpha = SEG_COLOR.get(segment_a, MUTED), 0.17
        else:
            cross_count += 1
            color, alpha = "#E69F00", 0.34
        ax.plot(
            [positions[a][0], positions[b][0]],
            [positions[a][1], positions[b][1]],
            color=color,
            alpha=alpha,
            lw=0.45 + 0.42 * math.sqrt(record["mass"]),
            zorder=1,
        )

    for model, (x, y) in positions.items():
        row = by_model[model]
        qualified = row.get("status") == "ranked"
        color = SEG_COLOR.get(row.get("segment", ""), MUTED)
        size = 16 + 10 * math.sqrt(max(1, len(node_respondents.get(model, set()))))
        ax.scatter(
            x,
            y,
            s=size,
            facecolor=color if qualified else PANEL,
            edgecolor=color,
            linewidth=0.9,
            alpha=0.94,
            zorder=3,
        )

    # Label the best-covered nodes and endpoints of the strongest cross-segment
    # bridges. This gives readers landmarks without turning the graph into text.
    label_models: set[str] = set()
    for segment in SEG_ORDER:
        candidates = [model for model in positions if by_model[model].get("segment") == segment]
        candidates.sort(key=lambda model: (-len(node_respondents.get(model, set())), model))
        label_models.update(candidates[:5])
    bridges = [
        record
        for record in shown_pairs
        if by_model.get(record["a"], {}).get("segment") != by_model.get(record["b"], {}).get("segment")
    ]
    for record in sorted(bridges, key=lambda item: -item["mass"])[:8]:
        label_models.update((record["a"], record["b"]))

    for model in sorted(label_models):
        if model not in positions:
            continue
        x, y = positions[model]
        ax.annotate(
            display_name(model),
            (x, y),
            xytext=(4, 3),
            textcoords="offset points",
            fontsize=6.7,
            color=INK,
            zorder=4,
        )

    ax.set_xlim(-0.48, 3.48)
    ax.set_ylim(-0.03, 1.03)
    ax.set_xticks(range(4))
    ax.set_xticklabels([SEG_TITLE[segment] for segment in SEG_ORDER], fontsize=9.5)
    ax.tick_params(axis="x", length=0, pad=8)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.set_ylabel("global p vs average (layout only)", fontsize=8.3, color=MUTED)
    ax.axhline(0.5, color=REFERENCE, lw=0.8, ls="--", zorder=0)
    ax.grid(axis="y", color=FAINT, lw=0.55, zorder=0)
    style_axis(ax)

    legend = [
        Line2D([0], [0], color=MUTED, alpha=0.4, lw=2, label="Within segment"),
        Line2D([0], [0], color="#E69F00", alpha=0.7, lw=2, label="Cross-segment bridge"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=MUTED, markersize=7, label="More respondents = larger node"),
    ]
    ax.legend(handles=legend, loc="lower left", frameon=False, fontsize=8.0)
    primary = summary.get("primary", {})
    add_header(
        fig,
        "Coverage diagnostic: which models were compared directly?",
        "Lines are observed pairings, not inferred wins. Amber cross-segment bridges are especially important to the global fit.",
        left=0.04,
    )
    fig.text(
        0.04,
        0.906,
        f"Shown: {len(shown_pairs)} pairs with at least {threshold:g} weighted statement mass "
        f"({within_count} within-segment; {cross_count} cross-segment). Node height uses global probability only to spread the network.",
        ha="left",
        va="top",
        fontsize=8.4,
        color=MUTED,
    )
    add_footer(
        fig,
        f"Computed only from analysis_observations.csv: {primary.get('observations', len(observations))} observations · "
        "unshown one-off edges still contribute to the fitted model · open node = insufficient rank coverage.",
        left=0.04,
    )
    save(fig, destination, dpi)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate publication PNGs from rank.py outputs.",
        epilog=(
            "Examples:\n"
            "  python3 src/plot.py\n"
            "  python3 src/plot.py --only global segment --dpi 160\n\n"
            "All matchup and coverage counts come from analysis_observations.csv."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--only",
        nargs="+",
        choices=["global", "segment", "sensitivity", "matchups", "coverage"],
        help="render only the selected figure groups (default: all five)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUT,
        help=f"figure destination (default: {DEFAULT_OUT.relative_to(ROOT)})",
    )
    parser.add_argument("--dpi", type=int, default=180, help="PNG resolution (default: 180)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.dpi < 72:
        raise SystemExit("--dpi must be at least 72")
    requested = set(args.only or ["global", "segment", "sensitivity", "matchups", "coverage"])

    ranking_path = DATA / "ranking.csv"
    segment_path = DATA / "ranking_segments.csv"
    sensitivity_path = DATA / "ranking_sensitivity.csv"
    observation_path = DATA / "analysis_observations.csv"
    ranking = load_csv(ranking_path)
    segments = load_csv(segment_path)
    sensitivity = load_csv(sensitivity_path)
    observations = load_csv(observation_path)
    summary = load_summary(DATA / "analysis_summary.json")

    require_columns(
        ranking,
        ranking_path,
        ["rank", "model", "p_vs_average", "p_lo", "p_hi", "n_respondents", "n_opponents", "status", "segment"],
    )
    require_columns(
        segments,
        segment_path,
        ["scope", "model", "p_vs_average", "p_lo", "p_hi", "n_respondents", "n_opponents", "status"],
    )
    require_columns(
        sensitivity,
        sensitivity_path,
        ["scenario", "model", "p_vs_average", "status"],
    )
    require_columns(
        observations,
        observation_path,
        ["winner", "loser", "analysis_weight", "comfort_axis", "statement_id", "respondent_id"],
    )

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "text.color": INK,
            "axes.edgecolor": FAINT,
            "axes.labelcolor": MUTED,
            "figure.dpi": 110,
            "savefig.bbox": None,
            "savefig.pad_inches": 0,
        }
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if "global" in requested:
        plot_global_rank_stability(ranking, summary, args.output_dir / "global_rank_stability.png", args.dpi)
    if "segment" in requested:
        plot_segment_rankings(segments, summary, args.output_dir / "segment_rankings.png", args.dpi)
    if "sensitivity" in requested:
        plot_sensitivity(ranking, sensitivity, args.output_dir / "sensitivity.png", args.dpi)
    if "matchups" in requested:
        plot_direct_matchups(observations, summary, args.output_dir / "direct_matchups.png", args.dpi)
    if "coverage" in requested:
        plot_coverage_graph(ranking, observations, summary, args.output_dir / "coverage_graph.png", args.dpi)


if __name__ == "__main__":
    main()
