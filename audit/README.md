# Audit kit for `data/comparisons.csv`

Each comparison has a stable 4-character `id`. Verdicts in `compiled.md` refer
to that id, not the CSV line number — deleting rows does not invalidate them.
The first full-file audit is recorded in `compiled.md` and has been applied.

The CSV mixes sources (reddit, edmunds, cars.com, x) and new ones may appear.
The pipeline is source-agnostic:

```
fetch page  ->  extract structured text  ->  match quote  ->  judge pair/axis/evidence
fetch_pages.sh   per-source extractor        audit_rows.py      human (or agent) reads
                 (reddit: parse_reddit.py)                       the full context
```

Reddit is the worked example: a full extractor with comment trees, scores,
deleted-account handling, and reply chains. Other sources use a generic
whole-page text fallback that still verifies quotes verbatim; write a
per-source extractor when structured context is needed (see "Adding a source").

If a site blocks curl, `fetch_pages.sh` falls back to a web.archive.org snapshot
and then the r.jina.ai reader proxy. Either can be run by hand, or the page can
be saved from a browser under the same filename. Archived snapshots can predate
the content the coder saw — a clean match verifies the quote, but a miss should
be checked against the live page before concluding.

## Standards

1. **Quote verbatim-ness.** The `quote` cell must be recoverable text from the
   cited page. `…` compression inside one passage is fine; editorial text is not.
2. **Pair support.** `winner > loser` must be statable from a single passage
   (one comment, review, or post body). If the passage names only one model, the
   reply chain must supply the other *and* the row should say so. If no single
   passage supports the pair, delete the row — do not stitch two strangers'
   statements together.
3. **Axis.** `comfort_axis` (ride / seats / nvh / overall) must be stated or
   directly implied.
4. **Evidence tag = weight.** `rank.py` derives weight from the evidence tag:
   `owned_both` 3.0, `test_drove_both` 2.0, `owned_one_*` / `opinion_plus_drive`
   1.2–1.5, `opinion` 0.7. The tag must match first-person claims in the passage.
   `weight_base` in the CSV is informational.
5. **Upvotes (legacy).** Planned for removal from all data and calculations.
   Treat the column as informational; do not spend effort fixing drift.

## Verdicts

- **OK** — quote verified; pair, axis, and evidence stand.
- **QUOTE_FIX** — quote is misleading as stored (wrong clause, missing parent
  context, truncated sibling of another row).
- **RECODE** — pair is right but evidence / axis / `home_team` / weight is wrong.
- **DELETE** — no single passage supports the pair; not a relative statement;
  or the text is ambiguous.
- **UNVERIFIED** — re-audit when the page is fetchable.

## Workflow

```bash
# 1. fetch every page cited in the CSV
./audit/fetch_pages.sh

# 2. audit a range of rows (any mix of sources)
python3 audit/audit_rows.py 1 50
python3 audit/audit_rows.py --all

# 3. inspect one reddit thread by hand if needed
python3 audit/parse_reddit.py audit/raw/1khcp25.html
```

`audit_rows.py` prints the stored quote, the match class (`VERBATIM`,
`COMPRESSED`, or `NO CLEAN MATCH`), the full source passage, and up to three
levels of reply-chain context (reddit). Judge pair, axis, and evidence from
that full text — never from the fragment alone.

Two advisory checks run per row:

- **HOME_TEAM CHECK** — winner vs the subreddit's home badge. `rank.py`
  penalizes home wins. Unknown brand subs are skipped; add them to
  `HOME_MODELS` when a new one shows up.
- **MODEL CHECK** — a coded winner/loser never named in the matched passage.
  Brand-only mentions are printed softer than a total absence. Plurals
  ("Palisades") and spaced codes ("XC 90") count as named; source misspellings
  still flag. Reply chains and thread titles can legitimately supply the name,
  but the row should then say so.

For non-reddit rows the same verdicts run against the whole page text, with a
context window instead of a comment tree. A verbatim hit verifies the quote; it
does not by itself verify first-person claims — that needs a structured extractor.

Sites that block curl (edmunds, cars.com often): save the page from a browser
under the filename `audit_rows.py` prints, then re-run.

## Adding a source

`audit_rows.py` dispatches on the row's `source` column. A structured extractor
returns the same shape as `parse_reddit.py`:

```python
{"title": str,
 "post": {"author": str|None, "score": int|None, "body": str},
 "comments": {cid: {"author": str|None, "score": int|None,
                    "body": str, "parent": cid|None, "children": [cid...]}},
 "deleted_count": int|None,
 "note": str|None}
```

For a review site, a minimal extractor is usually one regex over the repeated
review blocks. Register it in `audit_rows.py` (one `if src == "edmunds":`
branch) — matching, drift, and same-comment logic carry over unchanged.

## Layout

```
audit/
├── README.md          ← this file
├── compiled.md        ← one-line verdicts from the first full-file audit
├── fetch_pages.sh     ← downloads every cited page
├── parse_reddit.py    ← reddit extractor (HTML → comment tree)
├── audit_rows.py      ← source-agnostic CSV-row ↔ page verification
├── old/               ← per-batch working notes that compiled.md summarizes
└── raw/               ← fetched HTML, gitignored; re-create with fetch_pages.sh
                         reddit: <thread id>.html
                         others: <sha1(url.strip().rstrip("/"))[:10]>.html
```

`raw/` is a local snapshot. Re-fetch with `fetch_pages.sh` if missing; the
script prints the exact filename it expects. Hash non-reddit URLs the same way
the tool does (trailing slash stripped) or the filename will not match.
