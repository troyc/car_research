#!/usr/bin/env python3
"""Parse old.reddit HTML into structured comments.

Handles the quirks found during the audit:
- comments by deleted accounts have NO `data-author` attribute -> author falls
  back to the tagline ("[deleted]") instead of dropping the comment
- the post body is parsed separately (some quotes come from the OP write-up,
  e.g. audit row 33)
- deleted-comment placeholders are counted so the auditor knows coverage
- scores are the "unvoted" (true) value; old.reddit shows three fuzzed spans

Usage:  python3 parse_reddit.py thread.html [--json]
"""
import html as htmlmod
import json
import re
import sys
from collections import OrderedDict


def unescape(s):
    return htmlmod.unescape(s).replace("\r", "")


def extract_text(md_html):
    """Text of a <div class="md">...</div> body, paragraphs as newlines."""
    md_html = re.sub(r'<div class="md">|</div>', "", md_html)
    md_html = re.sub(r"<(?:p|li|br|blockquote)[^>]*>", "\n", md_html)
    md_html = re.sub(r"</(?:p|li|blockquote|ul|ol)>", "\n", md_html)
    md_html = re.sub(r"<[^>]+>", "", md_html)
    lines = [ln.strip() for ln in unescape(md_html).split("\n")]
    return "\n".join(ln for ln in lines if ln)


def _first_block(doc, marker, close):
    i = doc.find(marker)
    if i < 0:
        return None
    j = doc.find(close, i)
    if j < 0:
        return None
    return doc[i:j]


def parse_thread(fn):
    """Return dict with title, post info, comments, deleted_count."""
    with open(fn, encoding="utf-8", errors="replace") as f:
        doc = f.read()

    m = re.search(r"<title>(.*?)</title>", doc, re.S)
    title = unescape(m.group(1)) if m else "?"

    # ---- post body (row 33's quote came from here) ----
    post = {"author": None, "body": "", "score": None}
    m = re.search(r"data-author=\"([^\"]*)\"[^>]*data-comments-count", doc)
    if m:
        post["author"] = m.group(1)
    m = re.search(r"data-score=\"(\d+)\"", doc)
    if m:
        post["score"] = int(m.group(1))
    m = re.search(r'id="form-t3_[a-z0-9]+"[^>]*>.*?<div class="md">(.*?)</div>\s*</div>\s*</form>', doc, re.S)
    if m:
        post["body"] = extract_text(m.group(1))

    # ---- comments ----
    # Each comment starts with <div class=" thing id-t1_XXXX ...". Slicing
    # between starts keeps nested children inside their parent's slice.
    starts = [m.start() for m in re.finditer(r'<div class=" thing id-t1_([a-z0-9]+)[^"]*"', doc)]
    comments = OrderedDict()
    deleted_count = 0
    for k, s in enumerate(starts):
        cid = re.match(r'<div class=" thing id-t1_([a-z0-9]+)[^"]*"', doc[s:]).group(1)
        e = starts[k + 1] if k + 1 < len(starts) else len(doc)
        seg = doc[s:e]

        # author: data-author attr; deleted accounts lack it
        author = None
        m = re.search(r'data-author="([^"]*)"', seg)
        if m:
            author = m.group(1)
        else:
            m = re.search(r'class="author[^>]*>\s*([^<]+?)\s*</a>', seg)
            if m:
                author = m.group(1)
            elif "deleted" in seg[:3000]:
                author = "[deleted]"

        # true score = the middle (unvoted) of the three fuzzed spans
        score = None
        m = re.search(r'<span class="score unvoted" title="(\d+)">', seg)
        if m:
            score = int(m.group(1))

        # body; deleted bodies live in a grayed div without the trailing </form>
        body = None
        m = re.search(r'<div class="md">(.*?)</div>\s*</div>\s*</form>', seg, re.S)
        if not m:
            m = re.search(r'<div class="usertext grayed">.*?<div class="md">(.*?)</div>', seg, re.S)
        if m:
            body = extract_text(m.group(1)).strip()

        if body is None or body == "[deleted]":
            deleted_count += 1
            continue
        comments[cid] = {"author": author, "score": score, "body": body,
                         "parent": None, "children": []}

    # ---- parent/child structure ----
    for m in re.finditer(r'<div class="child"><div id="siteTable_t1_([a-z0-9]+)"', doc):
        parent = m.group(1)
        if parent not in comments:
            continue
        seg = doc[m.end():m.end() + 6000]
        for cm in re.finditer(r'<div class=" thing id-t1_([a-z0-9]+)[^"]*"', seg):
            cid = cm.group(1)
            if cid in comments and cid != parent:
                comments[cid]["parent"] = parent
                comments[parent]["children"].append(cid)

    return {"title": title, "post": post, "comments": comments,
            "deleted_count": deleted_count}


if __name__ == "__main__":
    t = parse_thread(sys.argv[1])
    print(f"# {t['title']}")
    if t["post"]["body"]:
        print(f"\n[POST u/{t['post']['author']} score={t['post']['score']}]\n{t['post']['body']}")
    print(f"\n{len(t['comments'])} comments parsed; {t['deleted_count']} deleted placeholders skipped")
    for cid, c in t["comments"].items():
        print(f"\n--- {cid} | u/{c['author']} | {c['score']} pts | parent={c['parent']} | kids={c['children']}")
        print(c["body"])
