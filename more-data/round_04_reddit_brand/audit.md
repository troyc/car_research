# Round 04 Reddit brand-community audit

Collection date: 2026-08-19. Scope was a small set of ordinary public HTML threads in vehicle-brand subreddits surfaced through targeted web search. No Reddit API, JSON, RSS, search endpoint, user/profile page, deep comment permalink, authentication, or bulk crawl was used. Raw usernames are not stored. `respondent_id` is `resp_` plus the first 16 hex characters of SHA-256 over `reddit|username`; where the browser page did not expose a comment ID without entering a disallowed deep permalink, `statement_id` is a deterministic digest of the source, thread, and author identity.

## Access and policy checks

Reddit's current `robots.txt` allows ordinary page HTML under `User-agent: *` while disallowing JSON, API, search, user-pagination, and deep comment paths. The current User Agreement conditionally permits crawling within `robots.txt` and prohibits scraping without prior written consent. Collection was therefore limited to manually targeted browser-readable pages and short excerpts, with no direct scraping or prohibited endpoint access.

## Inclusion and deduplication

Nine rows from seven first-person statements were retained. They add three respondents comparing Santa Fe and Sorento, including a useful split: Santa Fe wins third-row comfort and NVH, while one same-day shopper preferred the Sorento's 19-inch-wheel ride. Two new X5-X7 owners disagree on ride direction. The round also adds direct GX 550-Land Cruiser ride evidence and another GV80-X5 overall-comfort judgment.

Every candidate thread was checked against the 790-row parent file and all earlier staged rounds. Strong Defender-XC90, Corsair-Nautilus, TX-Aviator, GV70-Macan, and Pilot-Pathfinder passages were rejected as existing parent statements rather than counted again. A week-long rental of both GX and Land Cruiser was not forced into the `test_drove_both` category because the current evidence taxonomy has no rental-both value. A Gulf-market Santa Fe-Sorento passage was excluded to avoid regional powertrain/generation drift.

## Coverage and limits

The round increases evidence for two withheld models (Santa Fe and Sorento) and three named priority pairs (GX 550-Land Cruiser, X5-X7, and X5-GV80). Exact dates or model years remain blank where the public page exposed only a relative timestamp; the context file records every stated trim, wheel, and generation qualifier. No parent data or generated ranking output was changed.
