#!/usr/bin/env python3
"""Print the incremental coverage supplied by staged rounds."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

from validate import COMPARISON_FIELDS, PARENT, STAGING, load_rank_module, read_csv


PRIORITY_MODELS = [
    "Infiniti QX80",
    "Jeep Grand Cherokee",
    "Hyundai Santa Fe",
    "Kia Sorento",
]
PRIORITY_PAIRS = [
    ("BMW X5", "Lexus RX"),
    ("Land Rover Defender", "Volvo XC90"),
    ("BMW X5", "Genesis GV80"),
    ("Hyundai Palisade", "Nissan Pathfinder"),
    ("Genesis GV70", "Porsche Macan"),
    ("Lexus GX 550", "Toyota Land Cruiser"),
    ("Hyundai Palisade", "Mazda CX-90"),
    ("Hyundai Palisade", "Toyota Grand Highlander"),
    ("Buick Enclave", "Hyundai Palisade"),
    ("Toyota Highlander", "Toyota Venza"),
    ("Lincoln Corsair", "Lincoln Nautilus"),
    ("BMW X5", "BMW X7"),
    ("Lexus NX", "Lincoln Corsair"),
    ("Honda Pilot", "Nissan Pathfinder"),
    ("Lexus TX", "Lincoln Aviator"),
]


def staged_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(STAGING.glob("round_*/comparisons.csv")):
        rows.extend(read_csv(path, COMPARISON_FIELDS))
    return rows


def support(observations):
    respondents = defaultdict(set)
    opponents = defaultdict(set)
    for item in observations:
        respondents[item.winner].add(item.respondent_id)
        respondents[item.loser].add(item.respondent_id)
        opponents[item.winner].add(item.loser)
        opponents[item.loser].add(item.winner)
    return respondents, opponents


def pair_counts(observations):
    counts = defaultdict(set)
    for item in observations:
        counts[tuple(sorted((item.winner, item.loser)))].add(item.respondent_id)
    return counts


def main() -> int:
    rank = load_rank_module()
    parent = read_csv(PARENT, COMPARISON_FIELDS)
    staged = staged_rows()
    base_obs = rank.build_observations(parent)
    combined_obs = rank.build_observations(parent + staged)
    base_resp, base_opp = support(base_obs)
    new_resp, new_opp = support(combined_obs)
    base_pairs = pair_counts(base_obs)
    new_pairs = pair_counts(combined_obs)

    print("# Staged collection coverage")
    print()
    print(f"- Staged coded rows: {len(staged)}")
    print(f"- Retained observations: {len(base_obs)} -> {len(combined_obs)}")
    print(
        "- Long-trip observations: "
        f"{sum(o.axis == 'long_trip' for o in base_obs)} -> "
        f"{sum(o.axis == 'long_trip' for o in combined_obs)}"
    )
    print(
        "- Cross-segment observations: "
        f"{sum(rank.SEGMENT_OF.get(o.winner) != rank.SEGMENT_OF.get(o.loser) for o in base_obs)} -> "
        f"{sum(rank.SEGMENT_OF.get(o.winner) != rank.SEGMENT_OF.get(o.loser) for o in combined_obs)}"
    )
    print()
    print("## Staged sources")
    print()
    for source, count in sorted(Counter(row["source"] for row in staged).items()):
        print(f"- {source}: {count}")
    print()
    print("## Previously withheld models")
    print()
    print("| Model | Respondents | Opponents | Meets 5/3 rule |")
    print("|---|---:|---:|:---:|")
    for model in PRIORITY_MODELS:
        after_resp = len(new_resp[model])
        after_opp = len(new_opp[model])
        qualified = "yes" if after_resp >= 5 and after_opp >= 3 else "no"
        print(
            f"| {model} | {len(base_resp[model])} -> {after_resp} | "
            f"{len(base_opp[model])} -> {after_opp} | {qualified} |"
        )
    print()
    print("## Priority-pair respondent coverage")
    print()
    print("| Pair | Respondents |")
    print("|---|---:|")
    for first, second in PRIORITY_PAIRS:
        key = tuple(sorted((first, second)))
        print(f"| {first} / {second} | {len(base_pairs[key])} -> {len(new_pairs[key])} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
