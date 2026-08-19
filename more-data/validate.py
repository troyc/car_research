#!/usr/bin/env python3
"""Validate staged comparison rounds without modifying the parent dataset."""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "more-data"
PARENT = ROOT / "data" / "comparisons.csv"

COMPARISON_FIELDS = [
    "id", "winner", "loser", "weight_base", "upvotes", "source",
    "evidence", "home_team", "comfort_axis", "quote", "url",
    "statement_id", "respondent_id", "thread_id", "community_affinity",
    "collection_batch",
]
CONTEXT_FIELDS = [
    "id", "source_record_id", "published_at", "winner_model_year",
    "loser_model_year", "winner_trim", "loser_trim", "generation_notes",
    "wheel_tire_suspension", "ownership_context", "road_context",
    "extraction_method", "snapshot_path", "audit_status",
]
REJECTION_FIELDS = ["source", "url", "source_record_id", "reason", "notes"]
WEIGHTS = {
    "owned_both": 3.0,
    "test_drove_both": 2.0,
    "owned_one_td_other": 1.5,
    "owned_one_family": 1.5,
    "owned_one_loaner": 1.5,
    "owned_one_rode_other": 1.5,
    "passenger": 1.0,
}
AXES = {"ride", "seats", "nvh", "overall", "long_trip"}
AFFINITIES = {"winner", "loser", "other", "neutral"}
ID_RE = re.compile(r"^[a-z0-9]{4}$")


def read_csv(path: Path, expected: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        raw_rows = list(csv.reader(handle))
        if not raw_rows:
            raise ValueError(f"{path.relative_to(ROOT)}: empty CSV")
        bad_widths = [index for index, row in enumerate(raw_rows[1:], 2) if len(row) != len(expected)]
        if bad_widths:
            raise ValueError(
                f"{path.relative_to(ROOT)}: rows with wrong field count: {bad_widths}"
            )
        if raw_rows[0] != expected:
            raise ValueError(
                f"{path.relative_to(ROOT)}: header {raw_rows[0]!r} != {expected!r}"
            )
        return [dict(zip(expected, row, strict=True)) for row in raw_rows[1:]]


def load_rank_module():
    spec = importlib.util.spec_from_file_location("car_rank", ROOT / "src" / "rank.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load src/rank.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    rank = load_rank_module()
    parent = read_csv(PARENT, COMPARISON_FIELDS)
    parent_ids = {row["id"] for row in parent}
    parent_posts = {(row["source"], row["statement_id"]) for row in parent}
    registry = read_csv(
        STAGING / "source_registry.csv",
        [
            "source", "domain", "round", "community_type", "engine",
            "access_method", "automation_status", "min_delay_seconds",
            "last_checked", "notes",
        ],
    )
    registry_by_source = {row["source"]: row for row in registry}

    staged: list[dict[str, str]] = []
    staged_ids: set[str] = set()
    staged_posts: set[tuple[str, str]] = set()
    staged_person_judgments: set[tuple[str, tuple[str, str], str]] = set()
    parent_person_judgments = {
        (
            row["respondent_id"],
            tuple(sorted((row["winner"], row["loser"]))),
            row["comfort_axis"],
        )
        for row in parent
    }
    statement_metadata: dict[tuple[str, str], tuple[str, str, str]] = {}
    round_dirs = sorted(path for path in STAGING.glob("round_*") if path.is_dir())
    if not round_dirs:
        fail(errors, "no round_* directories found")

    for round_dir in round_dirs:
        try:
            comparisons = read_csv(round_dir / "comparisons.csv", COMPARISON_FIELDS)
            contexts = read_csv(round_dir / "context.csv", CONTEXT_FIELDS)
            read_csv(round_dir / "rejections.csv", REJECTION_FIELDS)
        except ValueError as exc:
            fail(errors, str(exc))
            continue
        if not (round_dir / "audit.md").exists():
            fail(errors, f"missing {(round_dir / 'audit.md').relative_to(ROOT)}")

        context_ids = [row["id"] for row in contexts]
        if len(context_ids) != len(set(context_ids)):
            fail(errors, f"{round_dir.name}: duplicate context IDs")
        if set(context_ids) != {row["id"] for row in comparisons}:
            fail(errors, f"{round_dir.name}: context IDs do not exactly match comparisons")
        for context in contexts:
            if context["audit_status"] != "included":
                fail(errors, f"{round_dir.name}/{context['id']}: audit_status must be included")
            if not context["source_record_id"] or not context["extraction_method"]:
                fail(errors, f"{round_dir.name}/{context['id']}: missing source record or extraction method")
            if not context["generation_notes"]:
                fail(errors, f"{round_dir.name}/{context['id']}: generation_notes is required")

        for row in comparisons:
            rid = row["id"]
            label = f"{round_dir.name}/{rid}"
            if not ID_RE.fullmatch(rid):
                fail(errors, f"{label}: ID must be four lowercase alphanumeric characters")
            if rid in parent_ids or rid in staged_ids:
                fail(errors, f"{label}: ID collision")
            staged_ids.add(rid)
            if row["collection_batch"] != round_dir.name:
                fail(errors, f"{label}: collection_batch must equal {round_dir.name}")
            if row["source"] not in registry_by_source:
                fail(errors, f"{label}: source missing from source_registry.csv")
            elif registry_by_source[row["source"]]["round"] != round_dir.name:
                fail(errors, f"{label}: source is assigned to another round")
            else:
                source_info = registry_by_source[row["source"]]
                host = (urlparse(row["url"]).hostname or "").lower()
                domain = source_info["domain"].lower()
                if host != domain and not host.endswith(f".{domain}"):
                    fail(errors, f"{label}: URL host {host!r} does not match {domain!r}")
                community_type = source_info["community_type"]
                if community_type == "general":
                    if row["community_affinity"] != "neutral" or row["home_team"] != "0":
                        fail(errors, f"{label}: general forums must be neutral with home_team=0")
                elif row["community_affinity"] == "neutral":
                    fail(errors, f"{label}: brand forums must use winner/loser/other affinity")
            if row["evidence"] not in WEIGHTS:
                fail(errors, f"{label}: non-first-hand evidence {row['evidence']!r}")
            else:
                try:
                    weight = float(row["weight_base"])
                except ValueError:
                    fail(errors, f"{label}: invalid weight_base")
                else:
                    if weight != WEIGHTS[row["evidence"]]:
                        fail(errors, f"{label}: weight does not match evidence")
            if row["comfort_axis"] not in AXES:
                fail(errors, f"{label}: invalid comfort axis")
            if row["winner"] not in rank.SEGMENT_OF or row["loser"] not in rank.SEGMENT_OF:
                fail(errors, f"{label}: model is not in the canonical segment map")
            if row["winner"] == row["loser"]:
                fail(errors, f"{label}: self-comparison")
            if row["home_team"] not in {"0", "1"}:
                fail(errors, f"{label}: home_team must be 0 or 1")
            if row["community_affinity"] not in AFFINITIES:
                fail(errors, f"{label}: invalid community_affinity")
            if row["home_team"] == "1" and row["community_affinity"] != "winner":
                fail(errors, f"{label}: home_team=1 requires winner affinity")
            if row["community_affinity"] == "winner" and row["home_team"] != "1":
                fail(errors, f"{label}: winner affinity requires home_team=1")
            for field in ("quote", "url", "statement_id", "respondent_id", "thread_id"):
                if not row[field].strip():
                    fail(errors, f"{label}: missing {field}")
            try:
                if int(row["upvotes"]) < 0:
                    raise ValueError
            except ValueError:
                fail(errors, f"{label}: upvotes must be a non-negative integer")

            post_key = (row["source"], row["statement_id"])
            if post_key in parent_posts:
                fail(errors, f"{label}: source statement already exists in parent data")
            staged_posts.add(post_key)
            metadata = (row["respondent_id"], row["thread_id"], row["url"])
            previous_metadata = statement_metadata.setdefault(post_key, metadata)
            if metadata != previous_metadata:
                fail(errors, f"{label}: inconsistent respondent/thread/URL for statement")

            person_judgment = (
                row["respondent_id"],
                tuple(sorted((row["winner"], row["loser"]))),
                row["comfort_axis"],
            )
            if person_judgment in parent_person_judgments:
                fail(errors, f"{label}: respondent/pair/axis already exists in parent data")
            if person_judgment in staged_person_judgments:
                fail(errors, f"{label}: duplicate respondent/pair/axis across staged rows")
            staged_person_judgments.add(person_judgment)
            staged.append(row)

    ids = [row["id"] for row in staged]
    duplicate_ids = [key for key, count in Counter(ids).items() if count > 1]
    if duplicate_ids:
        fail(errors, f"duplicate staged IDs: {duplicate_ids}")

    combined = parent + staged
    try:
        rank.validate_raw_rows(combined)
        observations = rank.build_observations(combined)
    except Exception as exc:  # noqa: BLE001 - surface parent-pipeline incompatibility
        fail(errors, f"combined observation compatibility failed: {exc}")
        observations = []

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(staged)} staged row(s) across {len(round_dirs)} round(s).")
    print(f"Temporary combined input: {len(combined)} rows; {len(observations)} observations.")
    print("No parent data or generated outputs were written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
