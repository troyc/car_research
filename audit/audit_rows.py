#!/usr/bin/env python3
"""Audit coded comparison rows against fetched old.reddit thread HTML.

For each row of data/comparisons.csv this prints:
  - where the stored quote actually lives (comment or post body) and how it
    relates to the source text:
        VERBATIM                exact normalized match
        COMPRESSED              all distinctive fragments in ONE comment/post
                                (legitimate "…" compression, e.g. rows 4, 20)
        !! NO CLEAN MATCH       fragments split across several comments or
                                missing -> coder-spliced / editorial text
                                (rows 16, 19, 34), wrong URL, or deleted
                                comment. Candidates are listed.
  - the full source comment (never just the fragment) plus up to 3 levels of
    parent context, so pair / axis / evidence tags can be judged by a human
  - the current (frozen) score vs the stored upvotes, flagging drift > 1
  - per-thread deleted-comment coverage, and a same-comment summary (one
    comment backing several rows, e.g. 5/6, 7/8, 13-15)

Usage:
  python3 audit_rows.py 1 50               # rows 1..50
  python3 audit_rows.py --all
  python3 audit_rows.py 1 50 --raw audit/raw --csv data/comparisons.csv
"""
import argparse
import csv
import html as htmlmod
import re
import sys
from collections import defaultdict
from pathlib import Path

from parse_reddit import parse_thread

THREAD_ID_RE = re.compile(r"/comments/([a-z0-9]+)/?$")


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


def frag_coverage(qn, body_norm):
    """(hits, total, covered_frags) of the quote's distinctive fragments."""
    frags = [f for f in qn.split(" ") if len(f) >= 5]
    if not frags:
        return 0, 0, 0
    hits = sum(1 for f in frags if f in body_norm)
    return hits, len(frags), hits


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
    threads = {}
    row_comment = defaultdict(list)   # comment id -> [row ids]

    for row in rows[start - 1:end]:
        url = row["url"].strip().rstrip("/")
        m = THREAD_ID_RE.search(url)
        if not m:
            print(f"ROW {row['id']}: bad URL {url}\n")
            continue
        tid = m.group(1)
        fn = raw / f"{tid}.html"
        if not fn.exists():
            print(f"ROW {row['id']}: missing {fn} — run fetch_threads.sh first\n")
            continue
        if tid not in threads:
            threads[tid] = parse_thread(fn)
            t = threads[tid]
            post = t["post"]
            print(f"### thread {tid}: {t['title']} | {len(t['comments'])} comments "
                  f"parsed, {t['deleted_count']} deleted placeholders | "
                  f"post u/{post['author']} score={post['score']}")
            if post["body"]:
                print(f"    post body: {post['body'][:160]}...")
            print()

        t = threads[tid]
        comments = t["comments"]
        quote = row["quote"]
        qn = norm(quote)
        rid = row["id"]

        print("=" * 100)
        print(f"ROW {rid}: {row['winner']} > {row['loser']} | "
              f"axis={row['comfort_axis']} | evidence={row['evidence']} | "
              f"wt={row['weight_base']} up={row['upvotes']} | {url}")
        print(f"CSV QUOTE: {quote}")

        pb = norm(t["post"]["body"])
        locs = {}  # location key -> (hits, total, body_text, kind)
        if qn and pb and qn in pb:
            locs["POST"] = (10**9, 0, t["post"]["body"], "verbatim")
        elif pb:
            h, tot, _ = frag_coverage(qn, pb)
            if h:
                locs["POST"] = (h, tot, t["post"]["body"], "frags")
        for cid, c in comments.items():
            bn = norm(c["body"])
            if qn and qn in bn:
                locs[cid] = (10**9, 0, c["body"], "verbatim")
            else:
                h, tot, _ = frag_coverage(qn, bn)
                if h:
                    locs[cid] = (h, tot, c["body"], "frags")

        best = max(locs.items(), key=lambda kv: kv[1][0]) if locs else None

        if best and best[1][0] == 10**9:
            loc = best[0]
            kind = "POST BODY" if loc == "POST" else "comment"
            print(f">> VERBATIM MATCH in {kind} {loc}")
            if best[0] == "POST":
                print(f"   [post u/{t['post']['author']} score={t['post']['score']}]")
                print(best[1][2][:800])
                print(f"   NOTE: stored upvotes {row['upvotes']} vs post score "
                      f"{t['post']['score']} — decide the post-row convention.")
            else:
                show(best[0], comments[best[0]], comments, "exact")
                row_comment[best[0]].append(rid)
        elif best and frag_ok(best[1][0], best[1][1]):
            hits, tot, body, _ = best[1]
            loc = best[0]
            if loc == "POST":
                print(f">> COMPRESSED MATCH in POST BODY ({hits}/{tot} distinctive "
                      f"fragments) — '…' compression of the OP writeup")
                print(body[:800])
                print(f"   NOTE: stored upvotes {row['upvotes']} vs post score "
                      f"{t['post']['score']} — decide the post-row convention.")
            else:
                print(f">> COMPRESSED MATCH in comment ({hits}/{tot} distinctive "
                      f"fragments) — '…' compression; verify the ellipsis does not "
                      f"hide a different model or reverse the direction")
                show(loc, comments[loc], comments, "compressed")
                row_comment[loc].append(rid)
        else:
            # top fragment candidates, ranked
            cands = sorted(locs.items(), key=lambda kv: -kv[1][0])[:4]
            print("!! NO CLEAN MATCH — the quote as stored is NOT recoverable as a")
            print("   single passage. Check for: (a) coder editorial text or quotes")
            print("   spliced from several comments (rows 16/19), (b) wrong URL,")
            print("   (c) deleted comment, (d) paraphrase.")
            if cands:
                print(f"   best fragment coverage: {cands[0][1][0]}/{cands[0][1][1]}")
                for loc, (hits, tot, body, _) in cands:
                    if loc == "POST":
                        print(f"   [POST frags {hits}/{tot}] {body[:300]}")
                    else:
                        show(loc, comments[loc], comments, f"fragment-candidate({hits}/{tot})")
                        row_comment[loc].append(rid)
            else:
                print("   (no fragment candidates in this thread either)")

        # ---- upvote drift on the matched comment ----
        if best and best[0] != "POST" and frag_ok(best[1][0], best[1][1]):
            c = comments[best[0]]
            stored = int(row["upvotes"] or 0)
            if c["score"] is not None and abs(c["score"] - stored) > 1:
                print(f">> UPVOTE DRIFT: stored {stored}, current frozen score "
                      f"{c['score']} (thread archived) — re-capture.")
        print()

    print("#" * 100)
    print("Same-comment rows (one comment backing several coded rows — fine, but")
    print("quotes should be consistent across them):")
    for cid, rids in sorted(row_comment.items(), key=lambda kv: min(kv[1])):
        if len(rids) > 1:
            print(f"  comment {cid} -> rows {rids}")


if __name__ == "__main__":
    main()
