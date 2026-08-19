# Round 02 owner-forum audit

Collection date: 2026-08-19. Scope was ordinary public thread HTML on Genesis Owners, Rivian Forums, Audizine, and The Subaru Forums. No login, member/profile, search, API, print, post, CAPTCHA, or challenge endpoints were used. Usernames were not stored; respondent IDs are `resp_` plus the first 16 lowercase hex characters of SHA-256(`source:username`).

## Access and policy checks

Current robots and terms were fetched before collection (HTTP 200 for each terms URL):

- `genesisowners.com/robots.txt` permits unnamed agents at ordinary paths, blocks `/find-new/`, `/account/`, `/login/`, `/conversations/`, and explicitly disallows GPTBot; its content signal allows reference use and disallows AI training. Genesis terms: `genesisowners.com/genesis-forum/help/terms/`.
- `rivianforums.com/robots.txt` sets `Crawl-delay: 5` for `User-agent: *`; only a handful of manually targeted ordinary threads were read. Terms: `rivianforums.com/forum/help/terms/`.
- `audizine.com/robots.txt` allows ordinary pages but disallows `/search/`, `/members/`, `/posts/`, `/login/`, `/account/`, `/find-new/`, and admin paths. Terms: `audizine.com/help/terms/`.
- `thesubaruforums.com/robots.txt` sets one-second crawl delay and disallows `/search/`, `/members/`, `/login/`, `/register/`, `/account/`, `/conversations/`, and other functional paths; GPTBot and ChatGPT-User are disallowed. Terms: `thesubaruforums.com/help/terms/`.

## Discovery and inclusion

Targeted ordinary-thread searches were reviewed in one small batch per source (well below 25 threads); additional searching quickly produced repeats, professional material, hypothetical shopping, unmapped XC70, or no explicit axis winner. Ten comparison rows from seven qualifying statements were retained: five Genesis rows and five Rivian rows (the shared-post multi-axis rows are intentional). Genesis rows cover GV80-X5 seats/ride/overall and GV70-Macan ride. Rivian rows cover XC90-R1S seats and 400-mile/day long-trip fatigue, plus two cross-segment Tahoe-R1S judgments from a household owner who found the air-suspended Tahoe more comfortable overall and better-riding after two days in the new R1S. The same Tahoe statement called the vehicles equally quiet, so no NVH row was coded. A further XC90-R1S seat post was rejected because the author ultimately called it a draw. The Subaru Forester-Outback candidate was rejected for generation drift (1996 Outback versus the current 2020-2025 canonical Outback node). Audizine yielded no qualifying canonical pair after review; representative rejections are recorded.

Quotes are the smallest first-person excerpts that establish both SUVs and a directional comfort judgment. `upvotes` is zero where forum reaction counts were not exposed as post votes. IDs were generated deterministically from source-record keys and checked against all 790 parent IDs plus the visible round_01 and round_03 staged IDs; no collision was found.

## Open gaps

No auditable owner comparison was found for Defender-XC90, Q7/Q8-X5 with an explicit comfort winner, or Outback-Ascent. Withheld Infiniti QX80, Grand Cherokee, Santa Fe, and Sorento did not appear in qualified public posts on these four brand forums. Further collection should move to the neutral-forum round rather than probe prohibited search/member endpoints.
