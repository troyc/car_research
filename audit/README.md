# Audit kit for `data/comparisons.csv`

Verification kit used for `audit1-50.md` (the first 50 coded rows). It fetches the
cited Reddit threads, re-locates every stored quote in the raw page, prints the full
source comment with its reply chain, and flags quotes that cannot be recovered.

## The standards being enforced

Each coded row is judged on five things:

1. **Quote verbatim-ness.** The `quote` cell must be recoverable text from the cited
   page — a comment body or the post body. `…` compression inside one comment is fine;
   editorial text is not. Two violations seen in rows 1–50:
   - row 16's quote contained a coder parenthetical — "(vs XC60 harsher; XT5 called
     lazy)" — and spliced two different commenters' statements into one row;
   - row 19's quote is a fragment of a comment that never names the coded winner.
   A quote that can't be matched verbatim is a red flag, not a style choice.

2. **Pair support.** The `winner > loser` pair must be statable from a single comment
   (or the post body, row 33). If the comment names only one model, the parent chain
   must supply the other *and* the row should say so (rows 2, 9, 32, 36). If no single
   comment supports the pair, the row is deleted (rows 1, 10, 16, 19, 28, 31, 45).
   Deleting is preferred over keeping a pair that requires stitching two strangers'
   comments together.

3. **Axis.** `comfort_axis` (ride / seats / nvh / overall) must be stated or directly
   implied. Row 9 coded `seats` from a comment that never mentions seats.

4. **Evidence tag = weight.** `rank.py` derives weight from the evidence tag:
   `owned_both` 3.0, `test_drove_both` 2.0, `owned_one_*` / `opinion_plus_drive`
   1.2–1.5, `opinion` 0.7. The tag must match first-person claims in the comment:
   "I own/had both", "test drove both", "own one, drove the other", or plain opinion.
   Nine of the first 50 rows had unsupported tags (2, 18, 25, 29, 36, 37, 38, 47, 50) —
   row 50 even says "We had a MB GLE350 for 3 years and we traded it for the X5" yet is
   tagged `test_drove_both`, which the owners-only fit drops.

5. **Upvotes.** For archived threads the score is frozen — re-capture the current value
   when it disagrees with the stored `upvotes` (rows 19, 22, 32, 35, 50; row 50 was
   stored 21, actual 10). ±1 is Reddit fuzzing; more than ±1 is a data error.

## The problem spots the tools are built for

| Spot | Example row(s) | How the kit handles it |
|---|---|---|
| Comments by deleted accounts lack `data-author` | 21 | `parse_reddit.py` falls back to the tagline (`u/[deleted]`), keeps the comment |
| Quotes from the OP's post body, not a comment | 33 | post body is parsed and searched; a post-row upvote convention is flagged |
| Coder-editorial / spliced quotes | 16, 19, 34 | `audit_rows.py` prints `NO CLEAN MATCH` with the fragment candidates spread across comments |
| Ellipsis-compressed but legitimate quotes | 4, 20, 24, 41… | fragment-coverage check: all distinctive fragments in one comment ⇒ `COMPRESSED MATCH` |
| Tiny / ambiguous comments | 45 | the *entire* comment is printed; nothing is hidden behind a fragment |
| `…` hiding a different model | 28 ("Volvo wagon") | the full comment is always printed, so the hidden word is visible |
| Upvote drift | 19, 22, 32, 35, 50 | current frozen score printed next to stored upvotes |
| One comment backing several rows | 5/6, 7/8, 13–15, 26/27, 48/49 | same-comment summary at the end — quotes across those rows should be consistent |
| Deleted comments in a thread | — | per-thread deleted-placeholder count printed (coverage warning) |

## Workflow

```bash
# 1. fetch the threads cited in the CSV (needs a browser User-Agent; the .json
#    endpoints and www.reddit.com were blocked at audit time, old.reddit.com worked)
RAW_DIR=audit/raw ./audit/fetch_threads.sh

# 2. audit a range of rows
python3 audit/audit_rows.py 1 50
python3 audit/audit_rows.py --all

# 3. inspect one thread by hand if needed
python3 audit/parse_reddit.py audit/raw/1khcp25.html
```

Reading `audit_rows.py` output: every row prints the stored quote, the match class
(`VERBATIM`, `COMPRESSED`, or `NO CLEAN MATCH`), the full source comment, and up to
three levels of parent context. Judge the pair, axis, and evidence tag from that full
text — never from the fragment alone. Then fix the CSV row, or delete it.

## Verdict taxonomy (used in `audit1-50.md`)

- **OK** — quote verified verbatim; a fuller quote is often still suggested.
- **QUOTE FIX** — quote is misleading as stored (e.g. row 24 quotes a clause that
  contradicts the coded winner and omits the decisive one; row 6 duplicates row 5 with
  a truncated quote).
- **RECODE** — pair is right but the evidence tag / axis / weight is wrong.
- **DELETE** — no single comment supports the pair; the comment is not a relative
  statement; or the text is ambiguous.

## Layout

```
audit/
├── README.md          ← this file
├── audit1-50.md       ← findings for rows 1–50, with per-row verdicts
├── fetch_threads.sh   ← downloads thread HTML (browser UA, old.reddit.com)
├── parse_reddit.py    ← HTML → comments (deleted authors, post body, scores, tree)
├── audit_rows.py      ← CSV rows ↔ page verification (verbatim/compressed/splice)
└── raw/               ← fetched HTML, gitignored; re-create with fetch_threads.sh
```

Notes for future audits:

- `raw/` is a snapshot of archived threads (scores frozen, but pages can move) —
  keep it locally, re-fetch with `fetch_threads.sh` if missing.
- New threads need their HTML fetched before `audit_rows.py` can see them; the script
  says so when a file is missing.
- `weight_base` in the CSV is informational; `rank.py` recomputes weights from the
  `evidence` tag, so fixing tags is what changes the rankings.
