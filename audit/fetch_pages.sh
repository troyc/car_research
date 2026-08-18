#!/usr/bin/env bash
# Fetch the pages cited in comparisons.csv into audit/raw/.
#
# Filenames:
#   reddit  -> raw/<thread id>.html            (stable, readable)
#   others  -> raw/<sha1(url)[:10]>.html       (any source, any URL shape)
#
# Fetching notes per source:
#   reddit  -> old.reddit.com with a browser User-Agent. The .json endpoints and
#              www.reddit.com returned HTML/"Blocked" at audit time; old.reddit
#              served the full comment tree (bodies, scores, authors, parents).
#   other sources (edmunds, cars.com, x) -> plain curl with a generic browser UA.
#              Review sites often block bots; if a page comes back empty or as a
#              captcha, fetch it with the fetch tool (or a browser) instead and
#              save it under the same filename, then re-run the audit.
#
# Usage:
#   ./audit/fetch_pages.sh                  # all URLs in data/comparisons.csv
#   CSV=data/comparisons.csv ./audit/fetch_pages.sh
#   ./audit/fetch_pages.sh 1gi84ub 1opp4z4  # just specific reddit threads
set -euo pipefail
RAW_DIR="${RAW_DIR:-audit/raw}"
CSV="${CSV:-data/comparisons.csv}"
UA_REDDIT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
UA_GENERIC="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
mkdir -p "$RAW_DIR"

# Looks like a block/empty page? (Cloudflare challenge, 403, wayback 404 page)
suspicious() {
    [ ! -s "$1" ] && return 0
    [ "$(wc -c < "$1")" -lt 5000 ] && return 0
    grep -qE "Just a moment|Attention Required|Access Denied|<title>Wayback Machine" "$1" && return 0
    return 1
}

# Fallback chain for curl-blocked sites: archive.org snapshot -> r.jina.ai
# reader (renders JS, passes most bot checks). Both save under the SAME target
# filename; the audit does not care how the HTML got there.
fetch_fallback() { # $1 = url, $2 = out file
    echo "  curl blocked/empty; trying web.archive.org..."
    if curl -s -L -A "$UA_GENERIC" "https://web.archive.org/web/2024id_/$1" -o "$2"; then
        sleep 2
        if ! suspicious "$2"; then
            echo "  saved from web.archive.org ($(wc -c < "$2") bytes)"
            return 0
        fi
    fi
    echo "  wayback miss; trying r.jina.ai reader proxy..."
    ok=""
    for try in 1 2 3; do
        if curl -s -L -A "$UA_GENERIC" "https://r.jina.ai/$1" -o "$2"; then
            sleep 2
            if ! suspicious "$2" && grep -qE "Title:|URL Source:" "$2"; then
                ok=1
                break
            fi
        fi
        echo "  (jina attempt $try blocked; retrying)"
        sleep 5
    done
    if [ -n "$ok" ]; then
        echo "  saved from r.jina.ai ($(wc -c < "$2") bytes)"
        return 0
    fi
    echo "  all fetchers blocked; save the page from a browser under: $2"
    rm -f "$2"
    return 1
}

if [ "$#" -gt 0 ]; then
    for id in "$@"; do
        url="https://old.reddit.com/comments/$id/"
        out="$RAW_DIR/$id.html"
        if [ -s "$out" ]; then
            echo "exists: $out"
            continue
        fi
        echo "fetching reddit $id -> $out"
        curl -s -L -A "$UA_REDDIT" "$url" -o "$out" || { echo "FAILED $id"; rm -f "$out"; }
        sleep 1
    done
    exit 0
fi

# url<TAB>filename<TAB>source — resolved by the same logic audit_rows.py uses
python3 - "$CSV" <<'PY' | while IFS=$'\t' read -r url file src; do
import csv, hashlib, re, sys
seen = {}
for row in csv.DictReader(open(sys.argv[1])):
    url = row["url"].strip().rstrip("/")
    src = row["source"].strip()
    m = re.search(r"(?:old\.|www\.)?reddit\.com/.*?/comments/([a-z0-9]+)", url)
    if src == "reddit" and m:
        file = m.group(1) + ".html"
    else:
        file = hashlib.sha1(url.encode()).hexdigest()[:10] + ".html"
    if url not in seen:
        seen[url] = True
        print(f"{url}\t{file}\t{src}")
PY
    if [ -s "$RAW_DIR/$file" ]; then
        echo "exists: $RAW_DIR/$file"
        continue
    fi
    echo "fetching [$src] $url -> $RAW_DIR/$file"
    if [ "$src" = "reddit" ]; then
        curl -s -L -A "$UA_REDDIT" "$url" -o "$RAW_DIR/$file" \
            || { echo "FAILED $url"; rm -f "$RAW_DIR/$file"; }
    else
        if ! curl -s -L -A "$UA_GENERIC" -H "Accept: text/html" "$url" -o "$RAW_DIR/$file" \
            || suspicious "$RAW_DIR/$file"; then
            rm -f "$RAW_DIR/$file"
            fetch_fallback "$url" "$RAW_DIR/$file" || true
        fi
    fi
    sleep 1
done
echo "done. verify a reddit page with: python3 audit/parse_reddit.py $RAW_DIR/<id>.html"
echo "non-reddit pages use the generic text fallback until a source extractor exists"
