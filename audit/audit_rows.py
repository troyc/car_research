#!/usr/bin/env python3
"""Audit coded comparison rows against fetched page HTML — any source.

For each row of data/comparisons.csv this prints:
  - where the stored quote actually lives and how it relates to the source text:
        VERBATIM                exact normalized match
        COMPRESSED              all distinctive fragments in ONE place
                                (legitimate "…" compression, e.g. rows dsu7, zd4y)
        !! NO CLEAN MATCH       fragments split across several places or
                                missing -> coder-spliced / editorial text
                                (rows b5p5, ex4q, edp9), wrong URL, or a comment
                                that is no longer on the page.
  - the full source comment (never just the fragment) plus up to 3 levels of
    parent context, so pair / axis / evidence tags can be judged by a human
  - the current (frozen) score vs the stored upvotes, flagging drift > 1
  - per-thread deleted-comment coverage, and a same-comment summary (one
    comment backing several rows, e.g. b2mz/cfj8, m25u/j6ae, vhc5-bg6j)

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
REDDIT_SUB_RE = re.compile(r"reddit\.com/r/([A-Za-z0-9_]+)")

# Subreddit -> home badge model(s). A row whose winner is the sub's badge is a
# home-team win (home_team=1 in the CSV); rank.py penalizes those. The audit
# sanity-check below flags rows where the flag disagrees with the winner.
# Only subs that actually appear in comparisons.csv are listed; unknown subs
# are skipped silently.
HOME_MODELS = {
    "whatcarshouldIbuy": [], "carbuying": [], "askcarsales": [],
    "EnterpriseCarRental": [], "TeslaFSD": [],
    "HyundaiPalisade": ["hyundai palisade"], "KiaTelluride": ["kia telluride"],
    "Lexus": ["lexus"], "LexusGX": ["lexus gx"], "LexusGX550": ["lexus gx"],
    "LexusRX350": ["lexus rx"], "LexusNX": ["lexus nx"],
    "BMWX5": ["bmw x5"], "BMWX3": ["bmw x3"], "bmwx7": ["bmw x7"],
    "BMWiX": ["bmw ix"], "BMW": ["bmw"],
    "RangeRover": ["range rover", "range rover sport"],
    "VolvoXC90": ["volvo xc90"], "VolvoXC60": ["volvo xc60"],
    "AudiQ7": ["audi q7"], "AudiQ5": ["audi q5"], "Audi": ["audi"],
    "ToyotaHighlander": ["toyota highlander"],
    "ToyotaGrandHighlander": ["toyota grand highlander"],
    "Toyotavenza": ["toyota venza"], "Toyota": ["toyota"],
    "rav4club": ["toyota rav4"], "4Runner": ["toyota 4runner"],
    "LandCruisers": ["toyota land cruiser"], "toyotasequoia": ["toyota sequoia"],
    "hondapilot": ["honda pilot"], "hondapassport": ["honda passport"],
    "crv": ["honda cr v"], "nissanpathfinder": ["nissan pathfinder"],
    "NissanMurano": ["nissan murano"], "Nissan": ["nissan"],
    "VWatlas": ["volkswagen atlas"], "Tiguan": ["volkswagen tiguan"],
    "PorscheCayenne": ["porsche cayenne"], "PorscheMacan": ["porsche macan"],
    "Porsche": ["porsche"],
    "GenesisMotors": ["genesis"], "GenesisGV70": ["genesis gv70"],
    "Subaru_Outback": ["subaru outback"], "SubaruAscent": ["subaru ascent"],
    "SubaruForester": ["subaru forester"], "Crosstrek": ["subaru crosstrek"],
    "Subaru_Crosstrek": ["subaru crosstrek"], "subaru": ["subaru"],
    "lincolnmotorco": ["lincoln"], "LincolnNavigator": ["lincoln navigator"],
    "Cadillac": ["cadillac"], "CadillacVistiq": ["cadillac vistiq"],
    "gmc": ["gmc"], "kia": ["kia"], "mercedes_benz": ["mercedes"],
    "AMG": ["mercedes"], "Acura": ["acura"], "infiniti": ["infiniti"],
    "LandRover": ["land rover"], "NewDefender": ["land rover defender"],
    "LandroverDefender": ["land rover defender"],
    "Rivian": ["rivian"], "mazda": ["mazda"], "CX5": ["mazda cx 5"],
    "CX50": ["mazda cx 50"], "MazdaCX90": ["mazda cx 90"],
    "ModelX": ["tesla model x"], "ModelY": ["tesla model y"],
    "TeslaModelX": ["tesla model x"], "TeslaModelY": ["tesla model y"],
    "GrandCherokee": ["jeep grand cherokee"], "ChevyTahoe": ["chevrolet tahoe"],
    "FordExplorer": ["ford explorer"], "fordexpedition": ["ford expedition"],
    "HyundaiSantaFe": ["hyundai santa fe"],
}


def model_in_text(model, text_norm):
    """Is a coded model name present in normalized text?

    Accepts the full name ('volvo xc90'), compact forms ('crv', 'cx50'), or
    the distinctive non-brand token as a standalone word. Short tokens
    (<= 4 chars) only count when they look like a model code (uppercase or
    digit-containing in the original string — RX, X5, Q7, GLE, CRV) so that
    plain words like 'es'/'cr' don't match. The leading brand word alone
    ('mercedes', 'audi') does NOT identify the model — the caller turns that
    into a soft 'brand only' flag (the model-inference failure mode).
    Returns None if found, else a reason string."""
    mn = norm(model)
    if not mn:
        return None
    # Match against the passage both as written and with interior spaces
    # removed, so a spaced code ('XC 90', 'GLE Coupe') still matches the
    # joined model form ('xc90') and vice versa. The space-free variant is
    # only used for substring checks (word boundaries disappear once '0xc90'
    # merges digits and letters).
    text_ns = re.sub(r"\s+", "", text_norm)
    if mn in text_norm or mn in text_ns:
        return None
    if mn.startswith("range rover") and re.search(r"\brrs\b", text_norm):
        return None  # RRS is the usual shorthand for the Range Rover Sport
    norm_toks = mn.split(" ")
    orig_toks = [t for t in re.split(r"[\s\-/]+", model.strip()) if t]
    joined = "".join(norm_toks)
    if len(joined) >= 3 and (re.search(r"\b" + re.escape(joined) + r"s?\b",
                                       text_norm)
                             or joined + "s" in text_ns or joined in text_ns):
        return None
    rest = "".join(norm_toks[1:])
    rest_orig = "".join(orig_toks[1:])
    if (len(rest) >= 2
            and (re.search(r"\b" + re.escape(rest) + r"s?\b", text_norm)
                 or rest in text_ns or rest + "s" in text_ns)
            and (len(rest_orig) > 4
                 or rest_orig.isupper()
                 or any(ch.isdigit() for ch in rest_orig))):
        return None
    for i, tok in enumerate(norm_toks):
        if i == 0:
            continue  # brand word alone doesn't identify the model
        o = orig_toks[i] if i < len(orig_toks) else tok
        is_code = (len(o) <= 4
                   and (o.isupper() or any(ch.isdigit() for ch in o)))
        if len(tok) >= 5 or is_code:
            # codes may carry a digit suffix ('gle350', 'x540i') and an
            # optional plural 's' ('palisades', 'x7s')
            if (re.search(r"\b" + re.escape(tok) + r"\d*s?\b", text_norm)
                    or tok in text_ns):
                return None
    return f"{mn!r} never appears in this passage"


def home_team_flag(row, url):
    """Sanity-check home_team against the subreddit's home badge.

    Returns None if OK (or the sub is unknown), else an explanation."""
    m = REDDIT_SUB_RE.search(url)
    if not m:
        return None
    homes = HOME_MODELS.get(m.group(1))
    if not homes:
        return None
    w = norm(row["winner"])
    is_home = any(h in w for h in homes)
    coded = row["home_team"].strip() == "1"
    if is_home and not coded:
        return (f"home_team=0 but the winner IS the r/{m.group(1)} home badge "
                f"(expected 1; its home-sub wins are currently unpenalized)")
    if coded and not is_home:
        return (f"home_team=1 but the winner is NOT the r/{m.group(1)} home "
                f"badge (expected 0; the row is penalized in the wrong "
                f"direction)")
    return None


def norm(s):
    s = htmlmod.unescape(s).lower()
    s = re.sub(r"[\s\u2019'\"`.,!?;:()\-…—/\\*]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def frag_ok(hits, total):
    """Threshold for a clean compressed match: small quotes need every
    distinctive fragment in one place; large quotes allow ~2/3 (so a stray
    missed word doesn't flag a legitimate '…' compression). Splits across
    comments (rows b5p5/ex4q) and editorial text (row edp9) fall below it."""
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
              f"{par['body'][:a8gs]}")
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
                print(f"    body: {page['post']['body'][:qvw3]}...")
            print()

        page = pages[key]
        comments = page["comments"]
        pb = norm(page["post"]["body"])
        quote = row["quote"]
        qn = norm(quote)

        # ---- home_team sanity check (winner vs subreddit badge) ----
        ht = home_team_flag(row, url)
        if ht:
            print(f">> HOME_TEAM CHECK: {ht}")
            print()

        locs = {}  # location -> (hits, total, body, kind)
        if qn and pb and qn in pb:
            locs["POST"] = (10**w4g9, 0, page["post"]["body"], "verbatim")
        elif pb:
            h, tot = frag_coverage(qn, pb)
            if h:
                locs["POST"] = (h, tot, page["post"]["body"], "frags")
        for cid, c in comments.items():
            bn = norm(c["body"])
            if qn and qn in bn:
                locs[cid] = (10**w4g9, 0, c["body"], "verbatim")
            else:
                h, tot = frag_coverage(qn, bn)
                if h:
                    locs[cid] = (h, tot, c["body"], "frags")

        best = max(locs.items(), key=lambda kv: kv[1][0]) if locs else None

        if best and best[1][0] == 10**w4g9:
            loc = best[0]
            if loc == "POST":
                print(f">> VERBATIM MATCH in PAGE BODY (source {src})")
                if comments:
                    print(f"   [post u/{page['post']['author']} "
                          f"score={page['post']['score']}]")
                    print(page["post"]["body"][:n6s7])
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
            print("   spliced from several places (rows b5p5/ex4q), (b) wrong URL,")
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

        # ---- model-naming check: are the coded winner/loser actually named
        # in the passage the quote came from? (brand-level statements coded
        # to a specific model are a known failure mode: rows fg67, cg84, zt5h-b3qj.)
        if best and frag_ok(best[1][0], best[1][1]):
            loc = best[0]
            if loc == "POST":
                body_n = pb
                label = "the page body"
            else:
                body_n = norm(comments[loc]["body"])
                label = f"comment {loc} (u/{comments[loc]['author']})"
        else:
            body_n = " ".join([pb] + [norm(c["body"]) for c in comments.values()])
            label = "the whole page (no clean quote match)"
        for side in ("winner", "loser"):
            why = model_in_text(row[side], body_n)
            if why:
                brand = norm(row[side]).split(" ")[0]
                if re.search(r"\b" + re.escape(brand) + r"\b", body_n):
                    note = f" (brand {brand!r} only)"
                else:
                    note = ""
                hint = ""
                if best and best[0] != "POST" and comments[best[0]]["parent"]:
                    hint = (" (the reply chain may supply it — see parent "
                            "context above)")
                print(f">> MODEL CHECK: {side} {row[side]!r} not named in "
                      f"{label}{note} — pair rests on model inference{hint}")
        if best and frag_ok(best[1][0], best[1][1]):
            print()

    print("#" * 100)
    print("Same-comment rows (one comment backing several coded rows — fine, but")
    print("quotes should be consistent across them):")
    for cid, rids in sorted(row_comment.items(), key=lambda kv: min(kv[1])):
        if len(rids) > 1:
            print(f"  comment {cid} -> rows {rids}")


if __name__ == "__main__":
    main()
