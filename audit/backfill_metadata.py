#!/usr/bin/env python3
"""Backfill provenance metadata columns in ``data/comparisons.csv``.

The Reddit statement is resolved against the saved HTML snapshot using the
same normalized exact/fragment matching used by :mod:`audit_rows`.  A matched
post uses ``post`` as its statement id; a matched comment uses its Reddit
comment id.  Missing/deleted/unfetched pages and non-Reddit sources receive a
deterministic row fallback.  Respondent identifiers are one-way SHA-256
digests (never raw usernames). ``collection_batch`` matches each comparison
against the growing historical CSV snapshots to recover passes 1--9.

Run from the repository root::

    python3 audit/backfill_metadata.py

The rewrite preserves all existing cells and appends/replaces only the five
metadata columns: ``statement_id``, ``respondent_id``, ``thread_id``,
``community_affinity``, and ``collection_batch``.
"""
from __future__ import annotations

import csv
import hashlib
import re
import subprocess
from pathlib import Path

try:  # script execution (``python audit/backfill_metadata.py``)
    from audit_rows import (REDDIT_ID_RE, REDDIT_SUB_RE, HOME_MODELS,
                            frag_coverage, frag_ok, norm, parse_thread)
except ModuleNotFoundError:  # package import (``import audit.backfill_metadata``)
    from .audit_rows import (REDDIT_ID_RE, REDDIT_SUB_RE, HOME_MODELS,
                             frag_coverage, frag_ok, norm, parse_thread)


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "comparisons.csv"
RAW_PATH = ROOT / "audit" / "raw"
META_COLUMNS = [
    "statement_id",
    "respondent_id",
    "thread_id",
    "community_affinity",
    "collection_batch",
]


def digest(prefix: str, value: str, n: int = 16) -> str:
    """Stable, privacy-preserving identifier for a value."""
    return f"{prefix}_{hashlib.sha256(value.encode('utf-8')).hexdigest()[:n]}"


def thread_for(row: dict) -> str:
    url = row.get("url", "").strip().rstrip("/")
    if row.get("source", "").strip().lower() == "reddit":
        m = REDDIT_ID_RE.search(url)
        if m:
            return f"reddit_{m.group(1)}"
    # Non-Reddit and malformed Reddit URLs still need a stable non-empty id.
    return digest("thread", f"{row.get('source', '').strip().lower()}|{url}", 16)


def _match_statement(row: dict, page: dict):
    """Return (statement key, author) for the best quote match, or None."""
    qn = norm(row.get("quote", ""))
    if not qn:
        return None
    candidates = []
    post_body = page.get("post", {}).get("body", "") or ""
    post_norm = norm(post_body)
    if qn in post_norm:
        candidates.append((10**9, 0, "post", page["post"].get("author"), post_body))
    elif post_norm:
        hits, total = frag_coverage(qn, post_norm)
        if hits:
            candidates.append((hits, total, "post", page["post"].get("author"), post_body))
    for cid, comment in page.get("comments", {}).items():
        body = comment.get("body", "") or ""
        body_norm = norm(body)
        if qn in body_norm:
            candidates.append((10**9, 0, cid, comment.get("author"), body))
        elif body_norm:
            hits, total = frag_coverage(qn, body_norm)
            if hits:
                candidates.append((hits, total, cid, comment.get("author"), body))
    if not candidates:
        return None
    # Exact matches always win.  For compressed matches, prefer coverage ratio,
    # then hit count, while retaining deterministic insertion order as a tie
    # breaker (post precedes comments, comments are parser order).
    exact = [c for c in candidates if c[0] == 10**9]
    if exact:
        best = exact[0]
    else:
        best = max(candidates, key=lambda c: (c[0] / c[1] if c[1] else 0, c[0]))
    # Do not assign a statement to a one-fragment accidental hit.  The audit
    # still reports those candidates, but metadata falls back to the row id.
    if best[0] != 10**9 and not frag_ok(best[0], best[1]):
        return None
    return best[2], best[3]


def _home_match(model: str, homes: list[str]) -> bool:
    text = norm(model)
    # HOME_MODELS values are normalized phrases; substring matching is
    # intentional because coded names include model years and trim suffixes.
    return any(norm(home) in text for home in homes)


def community_affinity(row: dict) -> str:
    """Classify a row relative to a subreddit brand/community home badge."""
    if row.get("source", "").strip().lower() != "reddit":
        return "neutral"
    m = REDDIT_SUB_RE.search(row.get("url", ""))
    if not m:
        return "neutral"
    homes = HOME_MODELS.get(m.group(1))
    if not homes:
        # Known general-purpose communities have an explicit empty home list;
        # unknown subreddits are treated as neutral rather than guessed.
        return "neutral"
    winner = _home_match(row.get("winner", ""), homes)
    loser = _home_match(row.get("loser", ""), homes)
    if winner and not loser:
        return "winner"
    if loser and not winner:
        return "loser"
    return "other"


def _git_batches(rows: list[dict]) -> dict[str, str]:
    """Recover the collection pass in which each comparison first appeared.

    Stable row ids were added only after all nine passes, so ``git log -S`` on
    the id labels every row with the same commit.  Instead, inspect the growing
    historical CSV snapshots and match the original comparison content.  The
    repository's first snapshot already contains passes 1--3; each subsequent
    size increase corresponds to passes 4--9.
    """
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=ROOT,
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (OSError, subprocess.CalledProcessError):
        return {}
    try:
        history = subprocess.run(
            ["git", "log", "--reverse", "--format=%H", "--", "data/comparisons.csv"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError):
        return {}

    snapshots = []
    largest = -1
    for commit in history:
        try:
            text = subprocess.run(
                ["git", "show", f"{commit}:data/comparisons.csv"],
                cwd=ROOT, check=True, capture_output=True, text=True,
            ).stdout
            old_rows = list(csv.DictReader(text.splitlines()))
        except (OSError, subprocess.CalledProcessError, csv.Error):
            continue
        # Audit commits shrink or merely recode the file; they are not a new
        # collection pass.
        if len(old_rows) <= largest:
            continue
        largest = len(old_rows)
        snapshots.append((commit, old_rows))

    labels = ["pass_1_to_3"] + [f"pass_{number}" for number in range(4, 10)]
    out = {}
    remaining = {row.get("id", ""): row for row in rows if row.get("id")}
    for snapshot_index, (_, old_rows) in enumerate(snapshots[: len(labels)]):
        exact = {
            (r.get("winner", "").strip(), r.get("loser", "").strip(),
             norm(r.get("quote", "")), r.get("url", "").strip().rstrip("/"))
            for r in old_rows
        }
        pair_url = {
            (r.get("winner", "").strip(), r.get("loser", "").strip(),
             r.get("url", "").strip().rstrip("/"))
            for r in old_rows
        }
        for rid, row in list(remaining.items()):
            key = (row.get("winner", "").strip(), row.get("loser", "").strip(),
                   norm(row.get("quote", "")), row.get("url", "").strip().rstrip("/"))
            loose = (key[0], key[1], key[3])
            if key in exact or loose in pair_url:
                out[rid] = labels[snapshot_index]
                del remaining[rid]
    for rid in remaining:
        out[rid] = "audit_or_unresolved"
    return out


def backfill(csv_path: Path = CSV_PATH, raw_path: Path = RAW_PATH) -> int:
    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fieldnames = list(rows[0].keys()) if rows else []
    for col in META_COLUMNS:
        if col not in fieldnames:
            fieldnames.append(col)

    pages = {}
    batches = _git_batches(rows)
    stats = {"matched": 0, "fallback": 0, "reddit": 0}
    for row in rows:
        src = row.get("source", "").strip().lower()
        url = row.get("url", "").strip().rstrip("/")
        thread_id = thread_for(row)
        row["thread_id"] = thread_id
        match = None
        if src == "reddit":
            stats["reddit"] += 1
            m = REDDIT_ID_RE.search(url)
            if m:
                fn = raw_path / f"{m.group(1)}.html"
                if fn.exists():
                    key = str(fn)
                    if key not in pages:
                        try:
                            pages[key] = parse_thread(fn)
                        except (OSError, ValueError, re.error):
                            pages[key] = None
                    if pages[key]:
                        match = _match_statement(row, pages[key])
        if match:
            statement_key, author = match
            row["statement_id"] = f"{thread_id}_{statement_key}"
            if author and author != "[deleted]":
                row["respondent_id"] = digest("resp", f"reddit|{author}")
            else:
                row["respondent_id"] = digest("resp", f"anonymous|{row['statement_id']}")
            stats["matched"] += 1
        else:
            # Generic review pages do not expose structured author blocks yet,
            # but repeated rows with the same source passage must still cluster
            # as one statement rather than masquerade as independent people.
            fallback_key = f"{src}|{url}|{norm(row.get('quote', ''))}"
            row["statement_id"] = digest("stmt", fallback_key)
            row["respondent_id"] = digest("resp", fallback_key)
            stats["fallback"] += 1
        row["community_affinity"] = community_affinity(row)
        row["collection_batch"] = batches.get(
            row.get("id", ""), digest("batch", f"{src}|{url}", 12)
        )

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"backfilled {len(rows)} rows: {stats['matched']} quote-matched, {stats['fallback']} fallbacks; {stats['reddit']} reddit")
    return len(rows)


if __name__ == "__main__":
    backfill()
