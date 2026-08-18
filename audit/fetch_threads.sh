#!/usr/bin/env bash
# Fetch the Reddit threads cited in comparisons.csv into audit/raw/.
#
# Why this works and the alternative doesn't:
#   - www.reddit.com and the .json endpoints returned "Blocked"/HTML at audit
#     time; old.reddit.com served the full page with a browser User-Agent.
#   - The old.reddit HTML embeds the complete comment tree (bodies, scores,
#     authors incl. "[deleted]", parent/child structure), which is all the
#     audit tools need.
#
# Usage:
#   RAW_DIR=audit/raw CSV=data/comparisons.csv ./fetch_threads.sh
#   ./fetch_threads.sh 1gi84ub 1opp4z4        # just specific thread ids
set -euo pipefail
RAW_DIR="${RAW_DIR:-audit/raw}"
CSV="${CSV:-data/comparisons.csv}"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
mkdir -p "$RAW_DIR"

if [ "$#" -gt 0 ]; then
    IDS="$*"
else
    IDS=$(python3 - "$CSV" <<'PY'
import csv, re, sys
ids = set()
for row in csv.DictReader(open(sys.argv[1])):
    m = re.search(r"/comments/([a-z0-9]+)/?$", row["url"].strip().rstrip("/"))
    if m:
        ids.add(m.group(1))
print("\n".join(sorted(ids)))
PY
)
fi

for id in $IDS; do
    out="$RAW_DIR/$id.html"
    if [ -s "$out" ]; then
        echo "exists: $out"
        continue
    fi
    echo "fetching $id -> $out"
    # /comments/<id> without the subreddit redirects to the right place.
    curl -s -L -A "$UA" "https://old.reddit.com/comments/$id/" -o "$out" \
        || { echo "FAILED $id"; rm -f "$out"; }
    sleep 1
done
echo "done. verify with: python3 audit/parse_reddit.py $RAW_DIR/<id>.html"
