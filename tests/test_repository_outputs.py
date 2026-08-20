from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_readme_summary_counts_match_generated_analysis() -> None:
    summary = json.loads((ROOT / "data" / "analysis_summary.json").read_text())
    primary = summary["primary"]
    readme = (ROOT / "README.md").read_text()

    expected_rows = {
        "Coded source rows": primary["raw_rows"],
        "Retained pair-axis judgments": primary["observations"],
        "Source statements": primary["statements"],
        "Respondent clusters": primary["respondents"],
        "Respondent bootstrap refits": summary["bootstrap_reps"],
    }
    for label, count in expected_rows.items():
        assert f"| {label} | {count:,} |" in readme


def test_readme_top_ten_match_generated_global_ranking() -> None:
    with (ROOT / "data" / "ranking.csv").open(newline="") as handle:
        ranked = [row for row in csv.DictReader(handle) if row["rank"]]
    readme = (ROOT / "README.md").read_text()

    for row in ranked[:10]:
        expected = (
            f'| {row["rank"]} | {row["model"]} | '
            f'{float(row["p_vs_average"]):.0%} | '
            f'{row["rank_lo"]}–{row["rank_hi"]} | '
            f'{row["n_respondents"]} | {row["n_opponents"]} |'
        )
        assert expected in readme


def test_readme_links_to_comparisons_markdown() -> None:
    readme = (ROOT / "README.md").read_text()
    assert "reports/comparisons.md" in readme
    assert "[`reports/comparisons.md`](reports/comparisons.md)" in readme


def test_comparisons_catalog_contains_all_models_and_observations() -> None:
    catalog_path = ROOT / "reports" / "comparisons.md"
    assert catalog_path.exists(), "reports/comparisons.md should exist"
    catalog = catalog_path.read_text(encoding="utf-8")

    with (ROOT / "data" / "ranking.csv").open(newline="") as handle:
        models = [row["model"] for row in csv.DictReader(handle)]

    with (ROOT / "data" / "analysis_observations.csv").open(newline="") as handle:
        obs_rows = list(csv.DictReader(handle))

    for model in models:
        assert f"## {model}" in catalog

    for obs in obs_rows:
        assert obs["id"] in catalog

