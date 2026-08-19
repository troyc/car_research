# Round 04 X audit

Collection date: 2026-08-19. Scope was public first-person SUV comfort comparisons on X, found through official X search and thread interfaces. No HTML crawling, login, member/profile, or unofficial API endpoints were used. Raw usernames are not stored; `respondent_id` is `resp_` plus the first 16 lowercase hex characters of SHA-256(`x:{username}`).

## Access, robots, and terms checks

- `https://x.com/robots.txt` (fetched 2026-08-19): `User-agent: *` disallows `/` and sets crawl-delay 1. Collection therefore did not crawl status HTML. Discovery used the published X search and thread tools.
- [X Terms of Service](https://x.com/tos) (effective 2026-04-10) require using currently available published interfaces and expressly prohibit scraping. Short excerpts were stored only as evidence for a later merge; no bulk archive of posts was written.

The three existing parent `source=x` rows were treated as already collected: `mh6d` (owned-both Model X over Model Y ride) remains the only first-hand parent X observation; `jf27` is opinion and `pa49` is journalist.

## Discovery and inclusion

Targeted keyword and semantic searches covered first-person ride language (`owned both`, `test drove`, `smoother ride`, `ride quality`) plus withheld/sparse models (Palisade, Grand Highlander, Pathfinder, Santa Fe, Sorento, QX80, Grand Cherokee, X5–RX, GX 550, CX-90, Enclave). Candidate posts were opened with thread context so parent tweets could supply the second model name.

Twelve comparison rows from nine statements were retained:

| ID | Winner > loser | Axis | Evidence |
|---|---|---|---|
| 9df4 | Honda Pilot > Toyota RAV4 | ride | owned_both |
| kzc1 | Audi Q7 > BMW X5 | ride | owned_one_td_other |
| 4nib | Lexus GX 550 > Chevrolet Tahoe | ride | owned_both |
| 5uz6 | BMW X5 > Tesla Model X | ride | owned_both (both air) |
| f8fz / wqva | BMW X5 > Tesla Model Y | ride / NVH | owned_both |
| zs6t / ecke | Kia Telluride and Subaru Outback 2026 > Tesla Model Y | ride | test_drove_both |
| 0nxs | BMW X7 air > Tesla Model Y | ride | owned_one_td_other |
| 8e8z | Tesla Model Y > Tesla Model X | NVH | owned_one_td_other |
| 0wdh / ea5q | Lexus RX > Highlander and Grand Highlander | ride | owned_one_td_other |

The Outback row uses `Subaru Outback 2026` because the author called it a “new Outback” during a July 2026 test drive. The X5–Model Y owned-both reply names “Tesla” in-post; the parent tweet is specifically X5 versus Model Y, so the loser is coded as Model Y. The Juniper Y versus Model X Plaid post described suspension as almost as good, so only the quieter-cabin NVH winner was kept.

Quotes are the smallest verbatim excerpts that name both SUVs and the directional comfort judgment. `upvotes` is the visible like count, matching the existing parent X rows. Community affinity is `neutral` because X is a general source.

## Rejections

Fifteen reviewed posts are in `rejections.csv`. Typical misses were journalist/dealer copy, unnamed “competitors,” sedans (Model 3, Model S, Jetta), unspecified Jeep, same-nameplate Model Y refreshes, Palisade praise whose explicit comparison was powertrain smoothness, and owners who named two SUVs without a comfort winner.

No qualified first-person X posts were found for the withheld models (QX80, Grand Cherokee, Santa Fe, Sorento) or for the sparse pairs Defender–XC90, Palisade–Pathfinder, Palisade–CX-90, Enclave–Palisade, Corsair–Nautilus, NX–Corsair, Pilot–Pathfinder, or TX–Aviator.

## Coverage and stopping

Two search batches after the included set returned mostly repeats, professional reviews, India-market shopping posts, and Tesla-versus-sedan notes. Returns fell below five qualified statements per batch, so the round stops. No parent dataset or generated ranking output was changed.

## Reproducibility

Included URLs are ordinary `x.com/{user}/status/{id}` pages. `source_record_id` and `statement_id` are `x:{status_id}`; `thread_id` is `x:{conversation_id}`. Context records keep model-year, trim, suspension, ownership, and road qualifiers where the post stated them. No raw snapshots were saved; `snapshot_path` is blank.
