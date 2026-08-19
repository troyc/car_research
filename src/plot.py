#!/usr/bin/env python3
"""Static PNG figures for the SUV comfort ranking.

Reads the CSVs written by rank.py. Does not re-fit.

    python3 src/plot.py

On Nix (no system matplotlib):

    nix-shell -p python3Packages.matplotlib python3Packages.numpy --run "python3 src/plot.py"

Writes reports/figures/{comfort_ladders,comparison_graph,rank_robustness,top_matchups}.png
"""

from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.gridspec import GridSpec

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "reports" / "figures"

MIN_APPS = 3
MIN_PAIR = 3

# Warm paper, stone ink. Segment colors stay distinct in grayscale-ish print.
BG = "#F4F0E8"
PANEL = "#FBF8F2"
INK = "#1C1917"
MUTED = "#78716C"
FAINT = "#D6D3CD"
ZERO = "#A8A29E"

SEG_COLOR = {
    "flagship": "#1D4E89",
    "mid_luxury": "#6D28D9",
    "family_3row": "#C2410C",
    "compact": "#0F766E",
}
SEG_ORDER = ["flagship", "mid_luxury", "family_3row", "compact"]
SEG_TITLE = {
    "flagship": "Flagship / large",
    "mid_luxury": "Midsize luxury",
    "family_3row": "Three-row family",
    "compact": "Compact / small-mid",
}

# Short labels so 20-row columns stay readable.
DISPLAY = {
    "Mercedes EQS SUV": "EQS SUV",
    "Mercedes GLS": "GLS",
    "Mercedes GLE": "GLE",
    "Mercedes GLE AMG": "GLE AMG",
    "Mercedes GLC": "GLC",
    "Range Rover": "Range Rover",
    "Range Rover Sport": "RR Sport",
    "Land Rover Defender": "Defender",
    "Land Rover": "Land Rover",
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

# Models the reports actually argue about.
ROBUST_FOCUS = [
    "Range Rover",
    "Mercedes GLS",
    "Mercedes EQS SUV",
    "Lexus LX",
    "Cadillac Escalade",
    "Lincoln Navigator",
    "BMW X7",
    "GMC Yukon",
    "Lincoln Aviator",
    "BMW X5",
    "Mercedes GLE",
    "BMW iX",
    "Lexus RX",
    "Lexus GX",
    "Hyundai Palisade",
    "Subaru Ascent",
    "Honda Pilot",
    "Kia Telluride",
    "Nissan Pathfinder",
    "Honda CR-V",
    "Subaru Outback",
    "Subaru Outback 2026",
    "Lincoln Nautilus",
    "Volvo XC60",
    "Toyota RAV4",
    "Rivian R1S",
    "Tesla Model Y",
    "Lexus GX 550",
    "Toyota 4Runner",
]


def label_of(name: str) -> str:
    return DISPLAY.get(name, name)


def load_ranking(path: Path) -> list[dict]:
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        for raw in csv.DictReader(f):
            rows.append(
                {
                    "rank": int(raw["rank"]),
                    "model": raw["model"],
                    "theta": float(raw["theta"]),
                    "wins": int(raw["wins"]),
                    "losses": int(raw["losses"]),
                    "appearances": int(raw["appearances"]),
                    "segment": raw["segment"] or "compact",
                }
            )
    return rows


def load_pairs() -> list[dict]:
    tally: dict[tuple[str, str], list] = {}
    with (DATA / "comparisons.csv").open(newline="", encoding="utf-8") as f:
        n = 0
        for raw in csv.DictReader(f):
            a, b = raw["winner"].strip(), raw["loser"].strip()
            if a == b:
                continue
            n += 1
            key = tuple(sorted((a, b)))
            rec = tally.setdefault(key, [0, 0, 0.0])  # wins of key[0], key[1], count
            rec[2] += 1
            rec[0 if a == key[0] else 1] += 1
    pairs = []
    for (a, b), (w0, w1, c) in tally.items():
        pairs.append({"a": a, "b": b, "w_a": w0, "w_b": w1, "n": int(c)})
    return pairs, n


def style_fig(fig) -> None:
    fig.patch.set_facecolor(BG)
    for ax in fig.axes:
        ax.set_facecolor(PANEL)
        ax.tick_params(colors=INK, labelsize=8)
        for spine in ax.spines.values():
            spine.set_color(FAINT)
        ax.xaxis.label.set_color(MUTED)
        ax.yaxis.label.set_color(MUTED)


def footer(fig, text: str) -> None:
    fig.text(0.02, 0.012, text, fontsize=7.2, color=MUTED, ha="left", va="bottom")


def marker_size(apps: int) -> float:
    return 22 + 11 * math.sqrt(apps)


# ---------------------------------------------------------------------------
# 1. Segment ladders
# ---------------------------------------------------------------------------

def plot_ladders(ranking: list[dict], n_votes: int, dest: Path) -> None:
    core = [r for r in ranking if r["appearances"] >= MIN_APPS]
    fig = plt.figure(figsize=(15.6, 16.8))
    gs = GridSpec(
        2, 2, figure=fig, left=0.18, right=0.975, top=0.88, bottom=0.045,
        wspace=0.55, hspace=0.16,
    )
    axes = [
        fig.add_subplot(gs[0, 0]),
        fig.add_subplot(gs[0, 1]),
        fig.add_subplot(gs[1, 0]),
        fig.add_subplot(gs[1, 1]),
    ]
    xmax = max(r["theta"] for r in core) + 0.35
    xmin = min(r["theta"] for r in core) - 0.25

    for ax, seg in zip(axes, SEG_ORDER):
        items = sorted(
            [r for r in core if r["segment"] == seg],
            key=lambda r: r["theta"],
        )
        color = SEG_COLOR[seg]
        ys = list(range(len(items)))
        for y, r in zip(ys, items):
            thin = r["appearances"] < 10
            ax.hlines(y, 0, r["theta"], color=color, lw=1.2, alpha=0.5)
            ax.plot(
                [r["theta"]],
                [y],
                "o",
                ms=math.sqrt(marker_size(r["appearances"])),
                color=PANEL if thin else color,
                markeredgecolor=color,
                markeredgewidth=1.35,
                zorder=3,
            )
        ax.axvline(0, color=ZERO, lw=0.8, ls="--", zorder=0)
        ax.set_yticks(ys)
        ax.set_yticklabels(
            [f"{label_of(r['model'])}   {r['wins']}–{r['losses']}" for r in items],
            fontsize=8.0,
        )
        ax.set_ylim(-0.9, len(items) - 0.3)
        ax.set_xlim(xmin, xmax)
        ax.tick_params(axis="y", length=0, pad=4)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.set_title(
            f"{SEG_TITLE[seg]}   ·   {len(items)} models",
            fontsize=11,
            color=color,
            pad=8,
            fontweight="semibold",
            loc="left",
        )
        ax.set_xlabel("comfort θ  →", fontsize=8.4, color=MUTED)

    fig.text(
        0.02, 0.965,
        "SUV comfort ladders by segment",
        fontsize=17, fontweight="semibold", color=INK, ha="left", va="top",
    )
    fig.text(
        0.02, 0.932,
        "Core models (3+ coded appearances). Higher θ = more often preferred on ride, seats, quiet, or long-trip fatigue.",
        fontsize=9.0, color=MUTED, ha="left", va="top",
    )
    fig.text(
        0.02, 0.908,
        "Read each panel as its own shopping list. Palisade beating Pilot is not Palisade beating an X5.  "
        "Open circle = fewer than 10 appearances — treat those θ values as thin.",
        fontsize=9.0, color=MUTED, ha="left", va="top",
    )
    style_fig(fig)
    footer(
        fig,
        f"Bradley–Terry θ from {n_votes} first-hand pairwise votes  ·  "
        f"dot size = number of comparisons  ·  raw θ inflates cars that only beat same-class rivals",
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(dest, dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"wrote {dest}")


# ---------------------------------------------------------------------------
# 2. Who-met-whom graph on the global θ scale
# ---------------------------------------------------------------------------

def plot_graph(ranking: list[dict], pairs: list[dict], n_votes: int, dest: Path) -> None:
    core = {r["model"]: r for r in ranking if r["appearances"] >= MIN_APPS}
    nodes = [r for r in ranking if r["appearances"] >= MIN_APPS]
    col_x = {seg: i * 2.45 for i, seg in enumerate(SEG_ORDER)}
    placed: dict[str, tuple[float, float]] = {}
    for seg in SEG_ORDER:
        group = sorted(
            [r for r in nodes if r["segment"] == seg],
            key=lambda r: -r["theta"],
        )
        last_y = None
        side = 1
        for r in group:
            x = float(col_x[seg])
            if last_y is not None and abs(last_y - r["theta"]) < 0.32:
                x += side * 0.22
                side *= -1
            placed[r["model"]] = (x, r["theta"])
            last_y = r["theta"]

    fig, ax = plt.subplots(figsize=(17.2, 18.4))
    fig.subplots_adjust(left=0.07, right=0.98, top=0.90, bottom=0.048)
    ax.set_facecolor(PANEL)

    segs, colors, widths = [], [], []
    for p in pairs:
        if p["n"] < MIN_PAIR:
            continue
        if p["a"] not in placed or p["b"] not in placed:
            continue
        x0, y0 = placed[p["a"]]
        x1, y1 = placed[p["b"]]
        winner = p["a"] if p["w_a"] > p["w_b"] else p["b"]
        upset = core[winner]["theta"] < min(y0, y1) + 1e-9 and abs(y0 - y1) > 0.25
        same = core[p["a"]]["segment"] == core[p["b"]]["segment"]
        if upset:
            c, a = "#B45309", 0.50
        elif same:
            c, a = SEG_COLOR[core[p["a"]]["segment"]], 0.22
        else:
            c, a = "#57534E", 0.16
        segs.append([(x0, y0), (x1, y1)])
        colors.append((*_hex_rgb(c), a))
        widths.append(0.65 + 0.16 * p["n"])
    if segs:
        ax.add_collection(LineCollection(segs, colors=colors, linewidths=widths, zorder=1))

    for r in nodes:
        x, y = placed[r["model"]]
        color = SEG_COLOR[r["segment"]]
        thin = r["appearances"] < 10
        ax.scatter(
            [x], [y],
            s=marker_size(r["appearances"]) * 2.0,
            c=PANEL if thin else color,
            edgecolors=color,
            linewidths=1.35,
            zorder=3,
        )

    # Directory of every name is the ladder figure. Here, only the models
    # the reports argue about — so labels stay next to their dots.
    label_names = {
        "Mercedes EQS SUV", "Mercedes GLS", "Range Rover", "Lexus LX",
        "Cadillac Escalade", "Cadillac Escalade IQ", "BMW X7",
        "Lincoln Navigator", "GMC Yukon", "Chevrolet Suburban",
        "Range Rover Sport", "Lincoln Aviator", "BMW X5", "BMW iX",
        "Mercedes GLE", "Lexus GX", "Lexus RX", "Land Rover Defender",
        "Porsche Cayenne", "Lexus GX 550", "Toyota 4Runner",
        "Rivian R1S", "Tesla Model X", "Tesla Model Y",
        "Buick Enclave", "Cadillac XT6", "Honda Pilot", "Subaru Ascent",
        "Hyundai Palisade", "Kia Telluride", "Toyota Highlander",
        "Mazda CX-90", "Nissan Pathfinder",
        "Lincoln Nautilus", "Mazda CX-9", "Audi Q5", "Honda CR-V",
        "Subaru Outback", "Subaru Outback 2026", "Toyota RAV4", "BMW X3",
        "Volvo XC60", "Toyota Venza",
    }
    label_side = {
        "flagship": ("right", -0.16),
        "mid_luxury": ("right", -0.16),
        "family_3row": ("left", 0.16),
        "compact": ("left", 0.16),
    }
    taken: dict[str, list[float]] = {s: [] for s in SEG_ORDER}
    labeled = [r for r in nodes if r["model"] in label_names]
    labeled.sort(key=lambda r: -r["appearances"])
    gap = 0.22
    for r in labeled:
        x, y = placed[r["model"]]
        ly = y
        for k in range(0, 6):
            cand = y - k * gap
            if all(abs(cand - t) >= gap - 1e-9 for t in taken[r["segment"]]):
                ly = cand
                break
        taken[r["segment"]].append(ly)
        ha, dx = label_side[r["segment"]]
        ax.text(
            x + dx, ly, label_of(r["model"]),
            fontsize=7.2, color=INK, ha=ha, va="center", zorder=4,
        )

    ax.set_xlim(-0.95, col_x["compact"] + 1.15)
    ys = [r["theta"] for r in nodes]
    ax.set_ylim(min(ys) - 0.7, max(ys) + 0.55)
    ax.set_xticks([col_x[s] for s in SEG_ORDER])
    ax.set_xticklabels([SEG_TITLE[s] for s in SEG_ORDER], fontsize=10.5, color=INK)
    ax.set_ylabel("global comfort θ", fontsize=9)
    ax.axhline(0, color=ZERO, lw=0.7, ls="--", zorder=0)
    ax.tick_params(axis="x", length=0, pad=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", color=FAINT, lw=0.6)

    fig.text(
        0.07, 0.965,
        "Who actually sat in whom",
        fontsize=17, fontweight="semibold", color=INK, ha="left", va="top",
    )
    fig.text(
        0.07, 0.932,
        "Each line is a pair with 3+ coded votes. Height is global θ. Most comparisons stay inside a segment —",
        fontsize=9.0, color=MUTED, ha="left", va="top",
    )
    fig.text(
        0.07, 0.910,
        "that is why EQS SUV, XT6, and CX-9 sit near flagships on raw θ. Amber = the lower car won the head-to-head.",
        fontsize=9.0, color=MUTED, ha="left", va="top",
    )

    legend = [
        Line2D([0], [0], color=SEG_COLOR[s], lw=2.2, label=SEG_TITLE[s])
        for s in SEG_ORDER
    ]
    legend.append(Line2D([0], [0], color="#B45309", lw=2.2, label="Upset (lower θ won)"))
    ax.legend(
        handles=legend, loc="lower left", frameon=False,
        fontsize=8, labelcolor=INK, bbox_to_anchor=(0.0, 0.08),
    )

    style_fig(fig)
    footer(
        fig,
        f"Bradley–Terry θ from {n_votes} first-hand pairwise votes  ·  "
        f"edges: pairs with {MIN_PAIR}+ votes  ·  open circle = fewer than 10 appearances",
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(dest, dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"wrote {dest}")


def _hex_rgb(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))


# ---------------------------------------------------------------------------
# 3. Default vs bias vs owners
# ---------------------------------------------------------------------------

def _spread(values: list[float], gap: float = 1.4) -> list[float]:
    """Push labels apart on a downward rank axis without reordering them."""
    out = [float(v) for v in values]
    order = sorted(range(len(out)), key=lambda i: out[i])
    for k in range(1, len(order)):
        i, j = order[k - 1], order[k]
        if out[j] < out[i] + gap:
            out[j] = out[i] + gap
    return out


def plot_robustness(
    default: list[dict],
    bias: list[dict],
    owners: list[dict],
    n_votes: int,
    dest: Path,
) -> None:
    maps = {r["model"]: r for r in default}

    def core_rank(rows: list[dict]) -> dict[str, int]:
        ranked = [r for r in rows if r["appearances"] >= MIN_APPS]
        ranked = sorted(ranked, key=lambda r: -r["theta"])
        return {r["model"]: i + 1 for i, r in enumerate(ranked)}

    ranks = {
        "default": core_rank(default),
        "bias": core_rank(bias),
        "owners": core_rank(owners),
    }

    models = [
        m
        for m in ROBUST_FOCUS
        if m in ranks["default"] and m in ranks["bias"] and m in ranks["owners"]
    ]
    models.sort(key=lambda m: ranks["default"][m])

    fig, ax = plt.subplots(figsize=(11.8, 14.2))
    fig.subplots_adjust(left=0.24, right=0.86, top=0.88, bottom=0.05)
    xs = [0, 1, 2]
    left_y = _spread([ranks["default"][m] for m in models])
    right_y = _spread([ranks["owners"][m] for m in models])

    for m, ly, ry in zip(models, left_y, right_y):
        ys = [ranks["default"][m], ranks["bias"][m], ranks["owners"][m]]
        color = SEG_COLOR[maps[m]["segment"]]
        ax.plot(xs, ys, color=color, lw=1.4, alpha=0.88, zorder=2)
        ax.scatter(xs, ys, s=32, color=color, zorder=3)
        ax.text(-0.07, ly, f"{label_of(m)}   {ys[0]}", fontsize=8.1, color=INK, ha="right", va="center")
        ax.text(2.07, ry, str(ys[2]), fontsize=8.1, color=MUTED, ha="left", va="center")

    n_core = len(ranks["default"])
    ax.set_xlim(-0.12, 2.22)
    ax.set_ylim(max(n_core, max(left_y), max(right_y)) + 2.2, 0.3)
    ax.set_xticks(xs)
    ax.set_xticklabels(["Default", "Bias-adjusted", "Owners only"], fontsize=10.5, color=INK)
    ax.set_yticks([])
    ax.grid(axis="y", color=FAINT, lw=0.55)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    fig.text(
        0.24, 0.965,
        "Does the order survive a less trusting read?",
        fontsize=16.5, fontweight="semibold", color=INK, ha="left", va="top",
    )
    fig.text(
        0.24, 0.932,
        "Same quotes, three weights. Bias-adjusted drops thin opinions, tightens brand-sub penalties,",
        fontsize=8.7, color=MUTED, ha="left", va="top",
    )
    fig.text(
        0.24, 0.910,
        "lifts Edmunds/Cars.com. Owners only drops same-day testers. X5 falls without testers. EQS stays high — it still only beat iX.",
        fontsize=8.7, color=MUTED, ha="left", va="top",
    )

    handles = [
        Line2D([0], [0], color=SEG_COLOR[s], lw=2.4, label=SEG_TITLE[s])
        for s in SEG_ORDER
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=8)

    style_fig(fig)
    footer(
        fig,
        f"{n_votes} pairwise votes  ·  rank among models with 3+ appearances in that fit  ·  1 = most preferred",
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(dest, dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"wrote {dest}")


# ---------------------------------------------------------------------------
# 4. Head-to-heads people actually ran
# ---------------------------------------------------------------------------

def plot_matchups(ranking: list[dict], pairs: list[dict], n_votes: int, dest: Path) -> None:
    by_name = {r["model"]: r for r in ranking}
    top = sorted(pairs, key=lambda p: -p["n"])[:22]
    top = list(reversed(top))

    fig, ax = plt.subplots(figsize=(12.2, 11.8))
    fig.subplots_adjust(left=0.30, right=0.96, top=0.88, bottom=0.06)

    ys = list(range(len(top)))
    for y, p in zip(ys, top):
        if p["w_a"] >= p["w_b"]:
            left, right, lw, rw = p["a"], p["b"], p["w_a"], p["w_b"]
        else:
            left, right, lw, rw = p["b"], p["a"], p["w_b"], p["w_a"]
        lc = SEG_COLOR.get(by_name.get(left, {}).get("segment", ""), INK)
        rc = SEG_COLOR.get(by_name.get(right, {}).get("segment", ""), MUTED)
        ax.barh(y, lw, color=lc, height=0.68, zorder=2)
        ax.barh(y, rw, left=lw, color=rc, height=0.68, alpha=0.38, zorder=2)
        ax.text(
            -0.28, y,
            f"{label_of(left)}  {lw}–{rw}  {label_of(right)}",
            fontsize=8.3, color=INK, ha="right", va="center",
        )

    ax.set_yticks([])
    ax.set_xlabel("coded votes for this pair", fontsize=9)
    ax.set_xlim(0, max(p["n"] for p in top) + 1.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", color=FAINT, lw=0.6)

    fig.text(
        0.30, 0.965,
        "The comparisons that actually exist",
        fontsize=16.5, fontweight="semibold", color=INK, ha="left", va="top",
    )
    fig.text(
        0.30, 0.930,
        "Twenty-two most-coded pairs. Solid bar = majority winner. X5 vs GLE and Palisade vs Pilot are the dense cores.",
        fontsize=8.8, color=MUTED, ha="left", va="top",
    )
    fig.text(
        0.30, 0.908,
        "Range Rover barely appears here — its record is spread across fewer, stronger notes.",
        fontsize=8.8, color=MUTED, ha="left", va="top",
    )

    style_fig(fig)
    footer(fig, f"{n_votes} pairwise votes  ·  split bars are split decisions, not ties unless the scores say so")
    dest.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(dest, dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"wrote {dest}")


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "text.color": INK,
            "axes.edgecolor": FAINT,
            "figure.dpi": 120,
            "savefig.bbox": None,
            "savefig.pad_inches": 0,
        }
    )
    default = load_ranking(DATA / "ranking.csv")
    bias = load_ranking(DATA / "ranking_bias.csv")
    owners = load_ranking(DATA / "ranking_owners.csv")
    pairs, n_votes = load_pairs()

    OUT.mkdir(parents=True, exist_ok=True)
    plot_ladders(default, n_votes, OUT / "comfort_ladders.png")
    plot_graph(default, pairs, n_votes, OUT / "comparison_graph.png")
    plot_robustness(default, bias, owners, n_votes, OUT / "rank_robustness.png")
    plot_matchups(default, pairs, n_votes, OUT / "top_matchups.png")


if __name__ == "__main__":
    main()
