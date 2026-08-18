# Audit kit for `data/comparisons.csv`

Verification kit used for `audit1-50.md` (the first 50 coded rows). It fetches the
cited pages, re-locates every stored quote in the raw page, prints the full source
text with context, and flags quotes that cannot be recovered.

The CSV mixes sources — reddit (723 rows), edmunds (51), cars.com (32), x (3) — and
new ones may appear. The pipeline is deliberately source-agnostic:

```
fetch page  ->  extract structured text  ->  match quote  ->  judge pair/axis/evidence
fetch_pages.sh   per-source extractor        audit_rows.py      human (or agent) reads
                 (reddit: parse_reddit.py)                       the full context
```

Reddit is the **worked example**: a full extractor with comment trees, scores,
deleted-account handling, and reply chains. Other sources currently use a **generic
whole-page text fallback** that still verifies quotes verbatim but has no structured
context yet; per-source extractors are small and are written as needed (see
"Adding a source"). If a site blocks curl, fetch the page with the fetch tool or a
browser and save it under the same filename — the audit doesn't care how the HTML
got there.

## The standards being enforced

Each coded row is judged on five things:

1. **Quote verbatim-ness.** The `quote` cell must be recoverable text from the cited
   page — a comment, a review, a post body. `…` compression inside one passage is
   fine; editorial text is not. Two violations seen in rows 1–50:
   - row 16's quote contained a coder parenthetical — "(vs XC60 harsher; XT5 called
     lazy)" — and spliced two different commenters' statements into one row;
   - row 19's quote is a fragment of a comment that never names the coded winner.
   A quote that can't be matched verbatim is a red flag, not a style choice.

2. **Pair support.** The `winner > loser` pair must be statable from a single passage
   (one comment, one review, one post body — row 33). If the passage names only one
   model, the reply chain must supply the other *and* the row should say so (rows 2,
   9, 32, 36). If no single passage supports the pair, the row is deleted (rows 1, 10,
   16, 19, 28, 31, 45). Deleting is preferred over stitching two strangers'
   statements together.

3. **Axis.** `comfort_axis` (ride / seats / nvh / overall) must be stated or directly
   implied. Row 9 coded `seats` from a comment that never mentions seats.

4. **Evidence tag = weight.** `rank.py` derives weight from the evidence tag:
   `owned_both` 3.0, `test_drove_both` 2.0, `owned_one_*` / `opinion_plus_drive`
   1.2–1.5, `opinion` 0.7. The tag must match first-person claims in the passage:
   "I own/had both", "test drove both", "own one, drove the other", or plain opinion.
   Nine of the first 50 rows had unsupported tags (2, 18, 25, 29, 36, 37, 38, 47,
   50) — row 50 even says "We had a MB GLE350 for 3 years and we traded it for the
   X5" yet is tagged `test_drove_both`, which the owners-only fit drops.

5. **Upvotes (legacy).** Upvotes are planned to be **removed from all data and
   calculations** — the `upvotes` column and the `log(1+upvotes)` karma multiplier
   will go away, so drift is not a concern and nothing needs re-capturing. Until the
   removal lands, treat the column as informational: ±1 vs the current score is
   Reddit fuzzing, larger deltas are old snapshots (rows 19, 22, 32, 35, 50; row 50
   was stored 21, actual 10). Do not spend effort fixing them.

## The problem spots the tools are built for

| Spot | Example row(s) | How the kit handles it |
|---|---|---|
| Brand-level statement coded to a specific model ("Audi" → Q7, "Mercedes" → GLE) | 60, 62, 69–71 (51–100) | `audit_rows.py` prints `MODEL CHECK` when a coded winner/loser is never named in the matched passage — brand-only mentions are flagged separately from total absences, and reply chains are pointed to |
| `home_team` flag disagrees with the subreddit's home badge | 67, 89, 90 (51–100); 41 (1–50) | `HOME_TEAM CHECK`: the winner is compared against the sub's badge model(s); a mismatch is printed so the row can be fixed (rank.py penalizes home wins in all fits) |
| Comments by deleted accounts lack `data-author` | 21 | `parse_reddit.py` falls back to the tagline (`u/[deleted]`), keeps the comment |
| Quotes from the OP's post body, not a comment | 33 | post body is parsed and searched; a post-row upvote convention is flagged |
| Coder-editorial / spliced quotes | 16, 19, 34 | `audit_rows.py` prints `NO CLEAN MATCH` with the fragment candidates spread across comments |
| Ellipsis-compressed but legitimate quotes | 4, 20, 24, 41… | fragment-coverage check: all distinctive fragments in one place ⇒ `COMPRESSED MATCH` |
| Tiny / ambiguous comments | 45 | the *entire* comment is printed; nothing is hidden behind a fragment |
| `…` hiding a different model | 28 ("Volvo wagon") | the full comment is always printed, so the hidden word is visible |
| Upvote drift | 19, 22, 32, 35, 50 | printed for information only — upvotes are planned to be removed from all data and calculations, so no re-capture is needed |
| One comment backing several rows | 5/6, 7/8, 13–15, 26/27, 48/49 | same-comment summary at the end — quotes across those rows should be consistent |
| Deleted comments in a thread | — | per-thread deleted-placeholder count printed (coverage warning) |
| Non-reddit sources (edmunds, cars.com, x) | — | generic whole-page text fallback verifies quotes; structured context needs a per-source extractor (below) |
| Sites that block curl | edmunds/cars.com often | fetch with the fetch tool / a browser, save under the same filename, re-run |

## Workflow

```bash
# 1. fetch every page cited in the CSV (reddit via old.reddit + browser UA — the
#    .json endpoints and www.reddit.com were blocked at audit time; other sources
#    with a generic UA, and curl-blocked sites can be saved from the fetch tool)
./audit/fetch_pages.sh

# 2. audit a range of rows (any mix of sources)
python3 audit/audit_rows.py 1 50
python3 audit/audit_rows.py --all

# 3. inspect one reddit thread by hand if needed
python3 audit/parse_reddit.py audit/raw/1khcp25.html
```

Reading `audit_rows.py` output: every row prints the stored quote, the match class
(`VERBATIM`, `COMPRESSED`, or `NO CLEAN MATCH`), the full source passage, and up to
three levels of reply-chain context (reddit). Judge the pair, axis, and evidence tag
from that full text — never from the fragment alone. Two advisory checks run per
row on top of the quote match: `HOME_TEAM CHECK` (winner vs the subreddit's home
badge — flags rows 67/89/90-type miscodes) and `MODEL CHECK` (a coded winner/loser
that is never named in the matched passage — flags brand-level statements coded to
specific models, e.g. "Audi" → Q7; a brand-only mention is printed softer than a
total absence, and reply-chain rows get a hint). `MODEL CHECK` is advisory:
reply chains and thread context can legitimately supply the name, but the row
should then *say so*. Then fix the CSV row, or delete it.

For non-reddit rows the same verdicts are produced against the whole page text, with
a context window instead of a comment tree. A verbatim hit on a review page verifies
the quote; it does not by itself verify the reviewer's first-person claims — that
needs the structured extractor.

## Adding a source

`audit_rows.py` dispatches on the row's `source` column. To give a source structured
context (reviewer, score, reply chain), write a small extractor that returns the
same shape as `parse_reddit.py`:

```python
{"title": str,
 "post": {"author": str|None, "score": int|None, "body": str},
 "comments": {cid: {"author": str|None, "score": int|None,
                    "body": str, "parent": cid|None, "children": [cid...]}},
 "deleted_count": int|None,
 "note": str|None}
```

For a review site, a minimal extractor is usually one regex over the repeated review
blocks:

```python
def extract_edmunds(fn, url):
    doc = open(fn, encoding="utf-8", errors="replace").read()
    comments = {}
    for i, m in enumerate(re.finditer(r'<div class="review">(.*?)</div>', doc, re.S)):
        seg = m.group(1)
        author = re.search(r'class="reviewer">([^<]+)', seg)
        body = re.sub(r"<[^>]+>", " ", seg)
        comments[f"r{i}"] = {"author": author.group(1) if author else None,
                             "score": None, "body": " ".join(body.split()),
                             "parent": None, "children": []}
    return {"title": ..., "post": {"author": None, "score": None, "body": ""},
            "comments": comments, "deleted_count": None,
            "note": "edmunds review blocks"}
```

Then register it in `audit_rows.py` (one `if src == "edmunds":` branch) — the
matching, drift, and same-comment logic all carry over unchanged. When in doubt, an
agent can build the extractor as it goes from the saved `raw/<hash>.html` file; the
page is already on disk.

## Verdict taxonomy (used in `audit1-50.md`)

- **OK** — quote verified verbatim; a fuller quote is often still suggested.
- **QUOTE FIX** — quote is misleading as stored (e.g. row 24 quotes a clause that
  contradicts the coded winner and omits the decisive one; row 6 duplicates row 5
  with a truncated quote).
- **RECODE** — pair is right but the evidence tag / axis / weight is wrong.
- **DELETE** — no single passage supports the pair; the passage is not a relative
  statement; or the text is ambiguous.

## Layout

```
audit/
├── README.md          ← this file
├── audit1-50.md       ← findings for rows 1–50, with per-row verdicts
├── fetch_pages.sh     ← downloads every cited page (reddit via old.reddit + UA,
│                         others via generic UA; curl-blocked sites: fetch tool)
├── parse_reddit.py    ← reddit-specific extractor (HTML → comment tree)
├── audit_rows.py      ← source-agnostic CSV-row ↔ page verification
└── raw/               ← fetched HTML, gitignored; re-create with fetch_pages.sh
                       (reddit: <thread id>.html; others: <sha1(url)[:10]>.html)
```

Notes for future audits:

- `raw/` is a snapshot (scores frozen on archived threads, but pages can move) —
  keep it locally, re-fetch with `fetch_pages.sh` if missing.
- New pages need their HTML fetched before `audit_rows.py` can see them; the script
  prints the exact filename it expects when a file is missing.
- `weight_base` in the CSV is informational; `rank.py` recomputes weights from the
  `evidence` tag, so fixing tags is what changes the rankings.
- Upvotes are planned to be removed from all data and calculations (the `upvotes`
  column and the karma multiplier); the drift checks in `audit_rows.py` are
  informational until that lands.
- x.com status pages fetched fine with plain curl + a browser UA at audit time
  (rows 87–88) — no fetch-tool workaround was needed. The generic whole-page
  fallback verifies quotes (the text is in the page's OG/tweet markup). Note the
  visible engagement metrics (replies / reposts / likes / views) do **not** map to
  the stored `upvotes` column; treat them as informational like reddit karma
  drift. If x.com starts serving a login wall again, use the fetch tool / a
  browser and save under the same sha1 filename.
- `MODEL CHECK` needs the `HOME_MODELS` mapping to cover new brand subs before it
  can sanity-check their `home_team`; unknown subs are skipped silently. Add the
  sub and its badge model(s) when a new brand sub shows up in the CSV.
