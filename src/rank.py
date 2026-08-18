#!/usr/bin/env python3
"""Bradley-Terry ranking of SUV comfort from pairwise customer comparisons."""

from __future__ import annotations

import csv
import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "comparisons.csv"

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
    "journalist": 0.0,
    "exclude": 0.0,
}

# Sedans / non-SUVs coded only as context; drop from the ranking.
NOT_SUV = {"Lexus ES", "Audi A7"}

SEGMENTS = {
    "compact": {
        "Honda CR-V",
        "Subaru Outback",
        "Subaru Outback 2026",
        "Subaru Crosstrek",
        "Mazda CX-5",
        "Mazda CX-50",
        "Mazda CX-9",
        "Toyota RAV4",
        "Toyota Venza",
        "Volvo XC60",
        "Audi Q5",
        "Mercedes GLC",
        "Volkswagen Tiguan",
        "Lincoln Nautilus",
        "Lexus NX",
        "Porsche Macan",
        "BMW X3",
        "BMW X1",
        "Subaru Forester",
        "Cadillac XT5",
        "Lincoln Corsair",
    },
    "mid_luxury": {
        "BMW X5",
        "Mercedes GLE",
        "Mercedes GLE AMG",
        "Lexus RX",
        "Volvo XC90",
        "Audi Q8",
        "Audi Q7",
        "Porsche Cayenne",
        "Genesis GV80",
        "Genesis GV70",
        "Jeep Grand Wagoneer",
        "Lincoln Aviator",
        "Acura MDX",
        "Range Rover Sport",
        "Land Rover Defender",
        "Lexus GX",
        "Lexus GX 550",
        "Toyota 4Runner",
        "Lexus TX",
        "Rivian R1S",
        "Tesla Model X",
        "Tesla Model Y",
        "BMW iX",
    },
    "family_3row": {
        "Hyundai Palisade",
        "Kia Telluride",
        "Toyota Highlander",
        "Toyota Grand Highlander",
        "Honda Pilot",
        "Honda Passport",
        "Mazda CX-90",
        "Subaru Ascent",
        "Volkswagen Atlas",
        "Ford Explorer",
        "Kia Sorento",
        "Nissan Pathfinder",
    },
    "flagship": {
        "Range Rover",
        "Mercedes GLS",
        "Mercedes EQS SUV",
        "Cadillac Escalade",
        "Lincoln Navigator",
        "BMW X7",
        "Lexus LX",
        "Land Rover",
        "Chevrolet Suburban",
    },
}

SEGMENT_OF = {m: seg for seg, models in SEGMENTS.items() for m in models}

# Consumer-review sites are less tribal than brand subs; X is sparse and performative.
SOURCE_RELIABILITY = {
    "edmunds": 1.25,
    "cars.com": 1.25,
    "reddit": 1.0,
    "x": 0.8,
}

# Model fan-subs tilt toward the home badge even after the coded home_team flag.
BRAND_SUB_RE = re.compile(
    r"reddit\.com/r/("
    r"Subaru_Outback|SubaruAscent|SubaruForester|HyundaiPalisade|"
    r"KiaTelluride|LexusGX|LexusRX350|BMWX5|BMWX3|bmwx7|RangeRover|"
    r"VolvoXC90|VolvoXC60|AudiQ7|ToyotaHighlander|ToyotaGrandHighlander|"
    r"hondapilot|lincolnmotorco|PorscheCayenne|GenesisMotors|TeslaModelX|"
    r"rav4club|CX5|MazdaCX90"
    r")",
    re.I,
)

# Thin first-person-adjacent talk; dropped in the bias-adjusted fit.
THIN_EVIDENCE = {"opinion", "opinion_plus_drive"}


def row_weight(raw: dict, mode: str) -> float | None:
    """Return a positive weight, or None if the row is dropped for this mode."""
    evidence = raw["evidence"].strip()
    base = EVIDENCE_WEIGHT.get(evidence, 0)
    if base <= 0:
        return None
    upvotes = int(raw["upvotes"] or 0)
    home = int(raw["home_team"] or 0)
    source = raw["source"].strip()
    url = raw.get("url") or ""

    if mode == "default":
        w = base * math.log1p(max(upvotes, 0) + 1)
        if home:
            w *= 0.6
        return w

    if mode == "bias":
        # Source-bias fit:
        # 1. drop thin opinion rows (hearsay-adjacent)
        # 2. do not boost by Reddit karma (popularity ≠ independence)
        # 3. heavier home-team and brand-sub penalties
        # 4. slight lift for Edmunds/Cars.com owner reviews
        if evidence in THIN_EVIDENCE:
            return None
        w = base
        if home:
            w *= 0.4
        w *= SOURCE_RELIABILITY.get(source, 1.0)
        if home and BRAND_SUB_RE.search(url):
            w *= 0.75
        return w

    if mode == "no_home":
        if home:
            return None
        return base * math.log1p(max(upvotes, 0) + 1)

    if mode == "owned_both":
        if evidence != "owned_both":
            return None
        return base  # no karma boost; lived-with-both only

    raise ValueError(f"unknown weight mode {mode!r}")


def load_comparisons(mode: str = "default") -> list[dict]:
    rows = []
    with DATA.open(newline="", encoding="utf-8") as f:
        for raw in csv.DictReader(f):
            winner = raw["winner"].strip()
            loser = raw["loser"].strip()
            if winner == loser:
                continue
            if winner in NOT_SUV or loser in NOT_SUV:
                continue
            w = row_weight(raw, mode)
            if w is None or w <= 0:
                continue
            rows.append(
                {
                    "winner": winner,
                    "loser": loser,
                    "weight": w,
                    "axis": raw["comfort_axis"],
                    "source": raw["source"],
                    "url": raw["url"],
                    "quote": raw["quote"],
                    "home_team": int(raw["home_team"] or 0),
                    "evidence": raw["evidence"].strip(),
                }
            )
    return rows


def fit_bradley_terry(
    rows: list[dict],
    models: list[str] | None = None,
    iters: int = 400,
    l2: float = 0.15,
) -> dict[str, float]:
    if models is None:
        names = sorted({r["winner"] for r in rows} | {r["loser"] for r in rows})
    else:
        names = list(models)
        rows = [r for r in rows if r["winner"] in names and r["loser"] in names]
    if len(names) < 2 or not rows:
        return {}

    idx = {n: i for i, n in enumerate(names)}
    theta = [0.0] * len(names)

    for _ in range(iters):
        grad = [0.0] * len(names)
        for r in rows:
            i, j = idx[r["winner"]], idx[r["loser"]]
            # P(i beats j)
            m = max(theta[i], theta[j])
            ei = math.exp(theta[i] - m)
            ej = math.exp(theta[j] - m)
            p_i = ei / (ei + ej)
            w = r["weight"]
            grad[i] += w * (1.0 - p_i)
            grad[j] += w * (0.0 - (1.0 - p_i))
        for k in range(len(names)):
            grad[k] -= l2 * theta[k]
            theta[k] += 0.08 * grad[k]
        mean = sum(theta) / len(theta)
        for k in range(len(names)):
            theta[k] -= mean
    return {n: theta[idx[n]] for n in names}


def counts(rows: list[dict]) -> tuple[dict[str, int], dict[str, int], dict[str, float]]:
    wins = defaultdict(int)
    losses = defaultdict(int)
    wsum = defaultdict(float)
    for r in rows:
        wins[r["winner"]] += 1
        losses[r["loser"]] += 1
        wsum[r["winner"]] += r["weight"]
        wsum[r["loser"]] += r["weight"]
    return wins, losses, wsum


def print_table(title: str, scores: dict[str, float], rows: list[dict], min_apps: int = 2) -> list[str]:
    wins, losses, _ = counts(rows)
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])
    ranked = [(m, s) for m, s in ranked if wins[m] + losses[m] >= min_apps]
    print()
    print(title)
    print("-" * len(title))
    print(f"{'#':>3}  {'model':<22} {'theta':>7}  {'W-L':>7}  {'win%':>6}")
    out_lines = [title]
    for i, (m, s) in enumerate(ranked, 1):
        w, l = wins[m], losses[m]
        pct = 100.0 * w / (w + l) if (w + l) else 0.0
        line = f"{i:3d}  {m:<22} {s:7.2f}  {w:>2d}-{l:<2d}   {pct:5.0f}%"
        print(line)
        out_lines.append(line)
    return [m for m, _ in ranked]


def write_ranking(path: Path, scores: dict[str, float], rows: list[dict]) -> None:
    wins, losses, _ = counts(rows)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank", "model", "theta", "wins", "losses", "appearances", "segment"])
        ranked = sorted(scores.items(), key=lambda kv: -kv[1])
        rank_i = 0
        for m, s in ranked:
            apps = wins[m] + losses[m]
            if apps < 1:
                continue
            rank_i += 1
            w.writerow([rank_i, m, f"{s:.4f}", wins[m], losses[m], apps, SEGMENT_OF.get(m, "")])
    print(f"\nWrote {path}")


def rank_map(scores: dict[str, float], rows: list[dict], min_apps: int = 3) -> dict[str, tuple[int, float, int, int]]:
    wins, losses, _ = counts(rows)
    ranked = [(m, s) for m, s in sorted(scores.items(), key=lambda kv: -kv[1]) if wins[m] + losses[m] >= min_apps]
    out = {}
    for i, (m, s) in enumerate(ranked, 1):
        out[m] = (i, s, wins[m], losses[m])
    return out


def print_bias_comparison(default_rows: list[dict], default_scores: dict[str, float]) -> None:
    variants = {
        "default": (default_rows, default_scores),
        "bias": None,
        "no_home": None,
        "owned_both": None,
    }
    for name in ("bias", "no_home", "owned_both"):
        rows = load_comparisons(name)
        scores = fit_bradley_terry(rows)
        variants[name] = (rows, scores)

    focus = [
        "Subaru Outback",
        "Subaru Outback 2026",
        "Subaru Ascent",
        "Lexus RX",
        "Lexus GX",
        "Toyota 4Runner",
        "Honda CR-V",
        "Toyota RAV4",
        "Subaru Forester",
        "Hyundai Palisade",
        "Toyota Highlander",
        "Honda Pilot",
        "Kia Telluride",
        "BMW X5",
        "Lincoln Aviator",
        "Range Rover",
    ]

    print()
    print("Source-bias robustness (core 3+ appearances in the default fit)")
    print("-" * 72)
    header = f"{'model':<22} {'def':>5} {'bias':>5} {'noHm':>5} {'own2':>5}  default W-L"
    print(header)
    maps = {name: rank_map(sc, rs, min_apps=1) for name, (rs, sc) in variants.items()}
    def_map = rank_map(default_scores, default_rows, min_apps=3)
    for m in focus:
        if m not in maps["default"]:
            continue
        cells = []
        for name in ("default", "bias", "no_home", "owned_both"):
            if m in maps[name]:
                cells.append(f"{maps[name][m][0]:>5d}")
            else:
                cells.append(f"{'—':>5}")
        wl = ""
        if m in def_map:
            _, _, w, l = def_map[m]
            wl = f"{w}-{l}"
        elif m in maps["default"]:
            _, _, w, l = maps["default"][m]
            wl = f"{w}-{l}"
        print(f"{m:<22} {cells[0]} {cells[1]} {cells[2]} {cells[3]}  {wl}")

    bias_rows, bias_scores = variants["bias"]
    print_table(
        "Bias-adjusted ranking (no karma boost; drop opinion; stronger home-team / brand-sub penalty; Edmunds/Cars.com lift)",
        bias_scores,
        bias_rows,
        min_apps=3,
    )
    write_ranking(ROOT / "data" / "ranking_bias.csv", bias_scores, bias_rows)


def main() -> None:
    rows = load_comparisons("default")
    print(f"Loaded {len(rows)} weighted pairwise comparisons from {DATA}")

    scores = fit_bradley_terry(rows)
    print_table("Global comfort ranking (Bradley-Terry, 2+ appearances)", scores, rows, min_apps=2)
    order = print_table(
        "Core ranking (3+ appearances — fewer sparse-graph artifacts)",
        scores,
        rows,
        min_apps=3,
    )

    print()
    print("Composite chain (core, 3+ appearances):")
    print("  " + "  >  ".join(order))

    for seg, models in SEGMENTS.items():
        sub = [r for r in rows if r["winner"] in models and r["loser"] in models]
        if len(sub) < 2:
            # still rank any model in the segment that appears in the global fit
            seg_scores = {m: scores[m] for m in models if m in scores}
            if len(seg_scores) >= 2:
                print_table(
                    f"{seg} ranking (projected from global theta)",
                    seg_scores,
                    [r for r in rows if r["winner"] in models or r["loser"] in models],
                    min_apps=1,
                )
            continue
        seg_scores = fit_bradley_terry(sub)
        print_table(f"{seg} ranking (within-segment pairs only)", seg_scores, sub, min_apps=1)

    write_ranking(ROOT / "data" / "ranking.csv", scores, rows)
    print_bias_comparison(rows, scores)


if __name__ == "__main__":
    main()
