# Audit kit for `data/comparisons.csv`

Each comparison has a stable 4-character `id` in `data/comparisons.csv`. Audit
verdicts (and `audit_compiled.md` / `audit_deletions.md`) refer to that id, not
the CSV line number — deleting rows does not invalidate earlier comments.

Verification kit used for `audit1-50.md` (the first 50 coded rows). It fetches the
cited pages, re-locates every stored quote in the raw page, prints the full source
text with context, and flags quotes that cannot be recovered.

The CSV mixes sources — reddit (c2sv rows), edmunds (51), cars.com (32), x (3) — and
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
"Adding a source"). If a site blocks curl, `fetch_pages.sh` now falls back
automatically to (1) a **web.archive.org** snapshot (`web/2024id_/<url>`) and
then (2) the **r.jina.ai** reader proxy (renders JS, passes most bot checks);
either can also be run by hand, or the page can be saved from a browser under the
same filename — the audit doesn't care how the HTML got there. The wayback leg
failed on exactly the URLs with no archive snapshot (query-string pages,
brand-new model pages), and jina is rate-flaky (retries built in); when both
miss, the script prints the exact filename to save from a browser. Note that
archived snapshots can **predate** content the coder saw (row dh9m's review was
only in the live page, row wu48/pq3c's quote in neither) — a clean match on an old
snapshot verifies the quote, but a miss should be checked against the live page
before concluding.

## The standards being enforced

Each coded row is judged on five things:

1. **Quote verbatim-ness.** The `quote` cell must be recoverable text from the cited
   page — a comment, a review, a post body. `…` compression inside one passage is
   fine; editorial text is not. Two violations seen in rows 1–50:
   - row b5p5's quote contained a coder parenthetical — "(vs XC60 harsher; XT5 called
     lazy)" — and spliced two different commenters' statements into one row;
   - row ex4q's quote is a fragment of a comment that never names the coded winner.
   A quote that can't be matched verbatim is a red flag, not a style choice.

2. **Pair support.** The `winner > loser` pair must be statable from a single passage
   (one comment, one review, one post body — row v8ax). If the passage names only one
   model, the reply chain must supply the other *and* the row should say so (rows qur7,
   w4g9, ec3t, ft57). If no single passage supports the pair, the row is deleted (rows w6cq, r9vk,
   b5p5, ex4q, uh8k, t4w2, s787). Deleting is preferred over stitching two strangers'
   statements together.

3. **Axis.** `comfort_axis` (ride / seats / nvh / overall) must be stated or directly
   implied. Row w4g9 coded `seats` from a comment that never mentions seats.

4. **Evidence tag = weight.** `rank.py` derives weight from the evidence tag:
   `owned_both` 3.0, `test_drove_both` 2.0, `owned_one_*` / `opinion_plus_drive`
   1.2–1.5, `opinion` 0.7. The tag must match first-person claims in the passage:
   "I own/had both", "test drove both", "own one, drove the other", or plain opinion.
   Nine of the first 50 rows had unsupported tags (qur7, z4c2, yd7s, kz3s, ft57, m3cu, y452, b98s,
   bfa4) — row bfa4 even says "We had a MB GLE350 for 3 years and we traded it for the
   X5" yet is tagged `test_drove_both`, which the owners-only fit drops.

5. **Upvotes (legacy).** Upvotes are planned to be **removed from all data and
   calculations** — the `upvotes` column and the `log(1+upvotes)` karma multiplier
   will go away, so drift is not a concern and nothing needs re-capturing. Until the
   removal lands, treat the column as informational: ±1 vs the current score is
   Reddit fuzzing, larger deltas are old snapshots (rows ex4q, v4ar, ec3t, ww3m, bfa4; row bfa4
   was stored 21, actual 10). Do not spend effort fixing them.

## The problem spots the tools are built for

| Spot | Example row(s) | How the kit handles it |
|---|---|---|
| Brand-level statement coded to a specific model ("Audi" → Q7, "Mercedes" → GLE) | fg67, cg84, zt5h–b3qj (51–100) | `audit_rows.py` prints `MODEL CHECK` when a coded winner/loser is never named in the matched passage — brand-only mentions are flagged separately from total absences, and reply chains are pointed to |
| `home_team` flag disagrees with the subreddit's home badge | rc5y, bbb7, zhy4 (51–100); h8an (1–50) | `HOME_TEAM CHECK`: the winner is compared against the sub's badge model(s); a mismatch is printed so the row can be fixed (rank.py penalizes home wins in all fits) |
| Comments by deleted accounts lack `data-author` | x453 | `parse_reddit.py` falls back to the tagline (`u/[deleted]`), keeps the comment |
| Quotes from the OP's post body, not a comment | v8ax | post body is parsed and searched; a post-row upvote convention is flagged |
| Coder-editorial / spliced quotes | b5p5, ex4q, edp9 | `audit_rows.py` prints `NO CLEAN MATCH` with the fragment candidates spread across comments |
| Ellipsis-compressed but legitimate quotes | dsu7, zd4y, cv8b, h8an… | fragment-coverage check: all distinctive fragments in one place ⇒ `COMPRESSED MATCH` |
| Tiny / ambiguous comments | s787 | the *entire* comment is printed; nothing is hidden behind a fragment |
| `…` hiding a different model | uh8k ("Volvo wagon") | the full comment is always printed, so the hidden word is visible |
| Upvote drift | ex4q, v4ar, ec3t, ww3m, bfa4 | printed for information only — upvotes are planned to be removed from all data and calculations, so no re-capture is needed |
| One comment backing several rows | b2mz/cfj8, m25u/j6ae, vhc5–bg6j, mwu2/nn8d, y3yk/b6zb | same-comment summary at the end — quotes across those rows should be consistent |
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
badge — flags rows rc5y/bbb7/zhy4-type miscodes) and `MODEL CHECK` (a coded winner/loser
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
- **QUOTE FIX** — quote is misleading as stored (e.g. row cv8b quotes a clause that
  contradicts the coded winner and omits the decisive one; row cfj8 duplicates row b2mz
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
  (rows mh6d–jf27) — no fetch-tool workaround was needed. The generic whole-page
  fallback verifies quotes (the text is in the page's OG/tweet markup). Note the
  visible engagement metrics (replies / reposts / likes / views) do **not** map to
  the stored `upvotes` column; treat them as informational like reddit karma
  drift. If x.com starts serving a login wall again, use the fetch tool / a
  browser and save under the same sha1 filename.
- **Browser fallback on NixOS (this machine):** chromium is installed
  system-wide (`/run/current-system/sw/bin/chromium`) and omp is configured to
  use it — the headless daemon prefers a detected system Chromium on Linux, so a
  cold daemon start (fresh broker) launches system chromium with no extra work.
  **Caveat:** a broker that was already running when chromium was installed keeps
  the cached Chrome-for-Testing binary in `~/.omp/puppeteer/chrome/<ver>/` —
  that binary needs the one-time RPATH fix below (already applied on this
  machine, harmless if system chromium later takes over). If a daemon shows
  `exit=127` on launch, apply:
  `nix-shell -p "nss.out" "nspr.out" "gtk3.out" ...` (explicit `.out` outputs —
  plain `nss` resolves to the `-dev` output and ships no libs) and patch the
  binary's RPATH:
  `patchelf --set-rpath "$(find /nix/store -maxdepth 1 -type d -iname '*-nspr-*' -o -iname '*-nss-*' … | tr '\n' ':')" ~/.omp/puppeteer/chrome/<ver>/chrome-linux64/chrome`.
  Note store dirs are `<hash>-<name>`, so globs must be `*<name>*`; after the
  patch, `ldd` should report zero "not found". The browser then passes
  Cloudflare (cars.com) where curl/jina fail (edmunds 403s the machine's IP
  after a few hits — treat as a per-IP block, not a browser problem).
- **Filename normalization:** non-reddit raws are `<sha1(url)[:10]>.html` of the
  URL **with the trailing slash stripped** (`url.strip().rstrip("/")`) — the same
  normalization `audit_rows.py` uses. Hashing the URL as-cited (with slash)
  produces a different filename; compute hashes the same way the tool does.
- `MODEL CHECK` now accepts plural model forms ("Palisades", "Escalades") and
  space-inserted codes ("XC 90" for XC90, "GLE Coupe" for GLE) after the
  101–150 pass produced false flags on both (rows xe8m, wwj2). Genuine
  misspellings in the source ("Nautilis" for Nautilus, row ebe6) still flag —
  by design, the row should quote the source verbatim anyway.
- `MODEL CHECK` needs the `HOME_MODELS` mapping to cover new brand subs before it
  can sanity-check their `home_team`; unknown subs are skipped silently. Add the
  sub and its badge model(s) when a new brand sub shows up in the CSV.
