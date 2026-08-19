# Round 01 vBulletin audit

## Scope and access checks

Sources were limited to ordinary public thread HTML on MBWorld and ClubLexus. On 2026-08-19, `https://mbworld.org/robots.txt` and `https://www.clublexus.com/robots.txt` both returned HTTP 200. Their `User-agent: *` rules allow ordinary forum pages and disallow search, member/profile, login, sendmessage, subscription, printthread, post_thanks, and tags endpoints; both specify a one-second crawl delay for Bingbot. I used no disallowed endpoints, authentication, CAPTCHA/proof-of-work bypass, member/profile lookups, or forum search crawling. The guessed `/terms/` paths returned 404, so no terms page was treated as authoritative; collection followed the public-site rules and registry's targeted-only policy.

## Discovery and extraction

Targeted ordinary web searches covered X5–RX, Q7/X5/RX, GLS–X7, LX/QX80, dealership QX/LX comparisons, and cross-segment GLC–GLE ownership comparisons. Candidate pages were fetched directly with a normal browser-like User-Agent and inspected for visible post text, post IDs, dates, and author metadata. Usernames were not written to outputs; `respondent_id` is `resp_` plus the first 16 hex characters of SHA-256 over lower-cased `source:username`.

## Inclusion decisions

Eleven rows were included from eight first-person posts. They cover X5–RX ride; Q7–X5 overall/ride; QX80–LX seats/ride; GLS–X7 NVH/long-trip plus X7–GLS ride; and three cross-segment GLE–GLC judgments. One owner of a 2021 GLE 450 and 2017 GLC 300 called the GLE quieter and its seats more comfortable; a separate owner of a 2020 GLE 350 and 2020 GLC 43 preferred the GLC seats. The other strong contexts are the owner of both a 2020 GLS and 2021 X7, the owner of a 2010 LX and week-long 2019 QX80 loaner, the 2018 Q7 buyer's direct shopping drive, and the Infiniti dealership employee's direct QX/LX driving. Quotes are kept to the smallest visible excerpts supporting a directional axis judgment.

The GX550 Overtrail/Luxury+ page was rejected because it compares trims of one canonical model (and would fail the distinct-model contract). A ClubLexus GX/Land Cruiser article was rejected as professional editorial content. An ML/X5 owned-both passage was rejected because Mercedes ML is not in the current canonical model map. A recent GX ride question was rejected because the author had not driven the vehicle.

## Coverage and stopping

The search produced a small set of auditable, first-person statements on the requested sparse pairs and added three compact-to-mid-luxury observations. Additional snippets were either professional/editorial, same-model trim comparisons, unsupported generalizations, or noncanonical generations. After targeted passes across both domains, returns diminished; this round stops without quota-filling.

## Reproducibility

All included source URLs are ordinary thread URLs with visible post fragments. `source_record_id` is the domain/post identity, `statement_id` and `thread_id` preserve post/thread identity, and context records retain model-year, trim, suspension, ownership, and road-use qualifiers where stated. No raw snapshots were saved because the public HTML was directly auditable at collection time; `snapshot_path` is therefore blank.
