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
        curl -s -L -A "$UA_GENERIC" -H "Accept: text/html" "$url" -o "$RAW_DIR/$file" \
            || { echo "FAILED $url (try the fetch tool if the site blocks curl)"; rm -f "$RAW_DIR/$file"; }
    fi
    sleep 1
done
echo "done. verify a reddit page with: python3 audit/parse_reddit.py $RAW_DIR/<id>.html"
echo "non-reddit pages use the generic text fallback until a source extractor exists"
