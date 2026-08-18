#!/usr/bin/env python3
"""Audit coded comparison rows against fetched page HTML — any source.

For each row of data/comparisons.csv this prints:
  - where the stored quote actually lives and how it relates to the source text:
        VERBATIM                exact normalized match
        COMPRESSED              all distinctive fragments in ONE place
                                (legitimate "…" compression, e.g. rows 4, 20)
        !! NO CLEAN MATCH       fragments split across several places or
                                missing -> coder-spliced / editorial text
                                (rows 16, 19, 34), wrong URL, or a comment
                                that is no longer on the page.
  - the full source comment (never just the fragment) plus up to 3 levels of
    parent context, so pair / axis / evidence tags can be judged by a human
  - the current (frozen) score vs the stored upvotes, flagging drift > 1
  - per-thread deleted-comment coverage, and a same-comment summary (one
    comment backing several rows, e.g. 5/6, 7/8, 13-15)

Sources:
  - reddit rows are resolved to raw/<thread id>.html and parsed with the
    structured extractor (parse_reddit.py).
  - every other source (edmunds, cars.com, x, ...) is resolved to
    raw/<sha1(url)[:10]>.html and checked with a generic whole-page text
    fallback: the quote still gets a verbatim/compressed verdict and a
    context window is printed, but there is no comment tree yet. For
    structured context (reviewer, score, reply chain) write a small
    per-source extractor — see audit/README.md, "Adding a source".

Usage:
  python3 audit_rows.py 1 50               # rows 1..50
  python3 audit_rows.py --all
  python3 audit_rows.py 1 50 --raw audit/raw --csv data/comparisons.csv
"""
import argparse
import csv
import hashlib
import html as htmlmod
import re
import sys
from collections import defaultdict
from pathlib import Path

from parse_reddit import parse_thread

REDDIT_ID_RE = re.compile(r"(?:old\.|www\.)?reddit\.com/.*?/comments/([a-z0-9]+)")


def norm(s):
    s = htmlmod.unescape(s).lower()
    s = re.sub(r"[\s\u2019'\"`.,!?;:()\-…—/\\*]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def frag_ok(hits, total):
    """Threshold for a clean compressed match: small quotes need every
    distinctive fragment in one place; large quotes allow ~2/3 (so a stray
    missed word doesn't flag a legitimate '…' compression). Splits across
    comments (rows 16/19) and editorial text (row 34) fall below it."""
    if total <= 4:
        return hits >= total
    return hits >= max(total - 1, int(total * 2 / 3) + 1)


def frag_coverage(qn, body_norm):
    """(hits, total) of the quote's distinctive fragments in a body."""
    frags = [f for f in qn.split(" ") if len(f) >= 5]
    if not frags:
        return 0, 0
    return sum(1 for f in frags if f in body_norm), len(frags)


def extract_generic(fn, url):
    """Whole-page text fallback for sources without a structured extractor.

    Strips scripts/styles/tags and returns the page text as the only "body".
    Verbatim/compressed checks work; author/score/parent context does not
    exist yet — write a per-source extractor when you need it."""
    raw = open(fn, encoding="utf-8", errors="replace").read()
    m = re.search(r"<title>(.*?)</title>", raw, re.S)
    title = htmlmod.unescape(m.group(1)) if m else url
    doc = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    doc = re.sub(r"(?is)<[^>]+>", "\n", doc)
    body = "\n".join(l.strip() for l in htmlmod.unescape(doc).split("\n") if l.strip())
    return {"title": title,
            "post": {"author": None, "score": None, "body": body},
            "comments": {}, "deleted_count": None,
            "note": f"generic whole-page text (no structured extractor for source yet)"}


def show(cid, c, comments, label):
    print(f"--- {label} {cid} | u/{c['author']} | {c['score']} pts | "
          f"parent={c['parent']} | kids={c['children']}")
    print(c["body"])
    p = c["parent"]
    for _ in range(3):
        if not p or p not in comments:
            break
        par = comments[p]
        print(f"  [parent {p} u/{par['author']} {par['score']}pts]: "
              f"{par['body'][:500]}")
        p = par["parent"]
    print()


def show_window(body, qn, width=700):
    """Context window around the first distinctive fragment (generic pages)."""
    frags = [f for f in qn.split(" ") if len(f) >= 8]
    if frags:
        i = body.lower().find(frags[0])
    else:
        i = body.lower().find(qn.split(" ")[0])
    if i < 0:
        print(body[:width * 2])
        return
    print(f"...{body[max(0, i - width):i + width]}...")


def resolve_page(raw: Path, url: str, src: str):
    """(filename, page|None, error|None) for a row's URL."""
    if src == "reddit":
        m = REDDIT_ID_RE.search(url)
        if m:
            return f"{m.group(1)}.html", None, None
        return None, None, f"reddit URL without a /comments/<id>: {url}"
    h = hashlib.sha1(url.encode()).hexdigest()[:10]
    return f"{h}.html", None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rows", nargs="*", help="'start end' or '--all'")
    ap.add_argument("--csv", default="data/comparisons.csv")
    ap.add_argument("--raw", default="audit/raw")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.csv)))
    if args.rows and args.rows[0] == "--all":
        start, end = 1, len(rows)
    elif len(args.rows) == 2:
        start, end = int(args.rows[0]), int(args.rows[1])
    else:
        ap.error("pass 'start end' or '--all'")

    raw = Path(args.raw)
    pages = {}
    row_comment = defaultdict(list)   # comment id -> [row ids]

    for row in rows[start - 1:end]:
        url = row["url"].strip().rstrip("/")
        src = row["source"].strip()
        rid = row["id"]

        print("=" * 100)
        print(f"ROW {rid}: {row['winner']} > {row['loser']} | "
              f"axis={row['comfort_axis']} | evidence={row['evidence']} | "
              f"wt={row['weight_base']} up={row['upvotes']} | source={src} | {url}")
        print(f"CSV QUOTE: {row['quote']}")

        fname, _, err = resolve_page(raw, url, src)
        if err:
            print(f"!! {err}\n")
            continue
        fn = raw / fname
        if not fn.exists():
            print(f"!! missing {fn} — fetch it first:\n"
                  f"      ./audit/fetch_pages.sh      (curl; may be blocked)\n"
                  f"   or use the fetch tool / a browser and save the page under "
                  f"that name, then re-run.\n")
            continue

        key = f"{src}:{fname}"
        if key not in pages:
            if src == "reddit":
                page = parse_thread(fn)
                print(f"### page {fname} [reddit] | {page['title']} | "
                      f"{len(page['comments'])} comments parsed, "
                      f"{page['deleted_count']} deleted placeholders | "
                      f"post u/{page['post']['author']} score={page['post']['score']}")
            else:
                page = extract_generic(fn, url)
                print(f"### page {fname} [{src}] | {page['title']}")
                print(f"    {page['note']} — quote checks work, structured "
                      f"context needs an extractor (see audit/README.md)")
            pages[key] = page
            if page["post"]["body"]:
                print(f"    body: {page['post']['body'][:160]}...")
            print()

        page = pages[key]
        comments = page["comments"]
        pb = norm(page["post"]["body"])
        quote = row["quote"]
        qn = norm(quote)

        locs = {}  # location -> (hits, total, body, kind)
        if qn and pb and qn in pb:
            locs["POST"] = (10**9, 0, page["post"]["body"], "verbatim")
        elif pb:
            h, tot = frag_coverage(qn, pb)
            if h:
                locs["POST"] = (h, tot, page["post"]["body"], "frags")
        for cid, c in comments.items():
            bn = norm(c["body"])
            if qn and qn in bn:
                locs[cid] = (10**9, 0, c["body"], "verbatim")
            else:
                h, tot = frag_coverage(qn, bn)
                if h:
                    locs[cid] = (h, tot, c["body"], "frags")

        best = max(locs.items(), key=lambda kv: kv[1][0]) if locs else None

        if best and best[1][0] == 10**9:
            loc = best[0]
            if loc == "POST":
                print(f">> VERBATIM MATCH in PAGE BODY (source {src})")
                if comments:
                    print(f"   [post u/{page['post']['author']} "
                          f"score={page['post']['score']}]")
                    print(page["post"]["body"][:800])
                else:
                    show_window(page["post"]["body"], qn)
                if page["post"]["score"] is not None:
                    print(f"   NOTE: stored upvotes {row['upvotes']} vs post score "
                          f"{page['post']['score']} — decide the post-row convention.")
            else:
                print(f">> VERBATIM MATCH in comment {loc}")
                show(loc, comments[loc], comments, "exact")
                row_comment[loc].append(rid)
        elif best and frag_ok(best[1][0], best[1][1]):
            hits, tot, body, _ = best[1]
            loc = best[0]
            if loc == "POST":
                print(f">> COMPRESSED MATCH in PAGE BODY ({hits}/{tot} distinctive "
                      f"fragments) — '…' compression")
                if comments:
                    print(f"   [post u/{page['post']['author']} "
                          f"score={page['post']['score']}]")
                show_window(body, qn)
                if page["post"]["score"] is not None:
                    print(f"   NOTE: stored upvotes {row['upvotes']} vs post score "
                          f"{page['post']['score']} — decide the post-row convention.")
            else:
                print(f">> COMPRESSED MATCH in comment ({hits}/{tot} distinctive "
                      f"fragments) — '…' compression; verify the ellipsis does not "
                      f"hide a different model or reverse the direction")
                show(loc, comments[loc], comments, "compressed")
                row_comment[loc].append(rid)
        else:
            cands = sorted(locs.items(), key=lambda kv: -kv[1][0])[:4]
            print("!! NO CLEAN MATCH — the quote as stored is NOT recoverable as a")
            print("   single passage. Check for: (a) coder editorial text or quotes")
            print("   spliced from several places (rows 16/19), (b) wrong URL,")
            print("   (c) removed/deleted content, (d) paraphrase.")
            if cands:
                print(f"   best fragment coverage: {cands[0][1][0]}/{cands[0][1][1]}")
                for loc, (hits, tot, body, _) in cands:
                    if loc == "POST":
                        print(f"   [PAGE BODY frags {hits}/{tot}]")
                        show_window(body, qn, width=400)
                    else:
                        show(loc, comments[loc], comments,
                             f"fragment-candidate({hits}/{tot})")
                        row_comment[loc].append(rid)
            else:
                print("   (no fragment candidates in this page either)")

        # ---- upvote drift on the matched comment ----
        if best and best[0] != "POST" and frag_ok(best[1][0], best[1][1]):
            c = comments[best[0]]
            stored = int(row["upvotes"] or 0)
            if c["score"] is not None and abs(c["score"] - stored) > 1:
                print(f">> UPVOTE DRIFT: stored {stored}, current frozen score "
                      f"{c['score']} — informational only; upvotes are planned for "
                      f"removal from all data and calculations, nothing to fix.")
        print()

    print("#" * 100)
    print("Same-comment rows (one comment backing several coded rows — fine, but")
    print("quotes should be consistent across them):")
    for cid, rids in sorted(row_comment.items(), key=lambda kv: min(kv[1])):
        if len(rids) > 1:
            print(f"  comment {cid} -> rows {rids}")


if __name__ == "__main__":
    main()
