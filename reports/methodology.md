# Methodology

## Question

Among people who have sat in more than one SUV and then said which one was more comfortable, what is the implied order?

Comfort here means ride isolation, seat support on long drives, cabin quiet, and how tired the person felt after a trip. Handling, styling, reliability, and brand prestige are ignored unless the commenter tied them to comfort.

## What counts as a vote

A comment is coded if all of these are true:

1. The author names at least two SUV models.
2. They state a preference on comfort (ride, seats, NVH, long-trip fatigue), not just "I bought the X5."
3. The comparison is first-hand: they owned, leased, rented, test-drove, or rode in the vehicles. "I heard Volvos have great seats" is excluded.
4. The vehicles are recent enough to be relevant (roughly 2018–2026 generations). Classic boats (1994 LS 400, 1970s Cadillacs) are recorded in notes but not scored.

Journalists and brand accounts are tagged `journalist` and excluded from the default ranking. Brand-subreddit posts are kept but down-weighted when the preference matches the home brand with no specific comfort detail.

## What is not a vote

- Single-model praise with no loser
- "Just get a Lexus" advice with no comparison
- Handling-only preferences ("X5 is more fun")
- Reliability-only preferences
- Sedan-vs-SUV unless both vehicles are SUVs / crossovers

## Weight

Each row gets a base weight from how the person knows the cars:

| Evidence | Weight |
|---|---|
| Owned or lived with both | 3.0 |
| Test-drove or rented both back-to-back | 2.0 |
| Owned one, test-drove the other | 1.5 |
| Passenger / short sit | 1.0 |

Then:

- `weight *= log(1 + upvotes)` if the comment has a Reddit score, floored at 1.0. Popular comments get a modest boost; they do not dominate.
- Brand-subreddit home-team comments with thin comfort language are multiplied by 0.6.
- If the same author states the same pair more than once, only the strongest statement is kept. Different authors on the same thread who name the same pair are separate votes.

`python3 src/rank.py` also writes a **bias-adjusted** fit (`data/ranking_bias.csv`). That run drops `opinion` / `opinion_plus_drive`, removes the karma multiplier, tightens the home-team penalty to 0.4 (and 0.75 more if the URL is a model fan-sub), and lifts Edmunds/Cars.com owner reviews by 1.25. Same inclusion rules; different trust in the sources. See [`bias_analysis.md`](bias_analysis.md).

## Combining votes

`src/rank.py` fits a Bradley–Terry model: each model \(i\) has a strength \(\theta_i\), and

\[
P(i \succ j) = \frac{e^{\theta_i}}{e^{\theta_i} + e^{\theta_j}}
\]

The \(\theta\) values are estimated by weighted maximum likelihood. Models with fewer than two comparisons are dropped from the printed table but remain in the raw file.

This is the right tool for the data we have. People almost never give numeric scores. They say "A over B." Bradley–Terry turns a pile of those statements into one scale.

## Segments

A global ranking mixes a $30k compact with a $130k Range Rover. That is useful as a single story and misleading as a shopping list. The script also ranks three segments that people actually cross-shop:

- Compact / small-mid crossover (RAV4 class)
- Midsize luxury (X5 / GLE / RX / XC90 / Q8 class)
- Large / flagship (Range Rover, GLS, Navigator, Escalade, X7)

Three-row family crossovers (Palisade, Telluride, Highlander, Grand Highlander, Pilot, CX-90, Ascent) sit between the last two and are reported separately when they appear. Lexus TX is scored with midsize luxury because that is who it is cross-shopped against, even though it shares a platform with Grand Highlander. Lexus GX 460 and Toyota 4Runner sit with midsize luxury for the same reason (that is who they meet); they are body-on-frame trucks, not X5s.

## Generations we split

Most nameplates stay one node. Two changes this pass:

- **Subaru Outback 2026** is a new generation (wagon → more upright crossover). It is coded separately from **Subaru Outback** (2020–2025, 6th gen). A same-garage 2026 vs 2020/2019 note is a vote, not a same-nameplate exclude.
- **Lexus RX** still includes 2020–2022 AL20 (RX 350 / 350L / 450h / 450hL) and 2023+ AL30. Year is kept in the quote when the author named it. Splitting RX would orphan the older mixed-year rows.
- **Lexus GX** here is the 2014–2023 GX 460 (J150). **Lexus GX 550** is a separate node. First-hand 460-vs-550 notes are votes, not same-nameplate excludes.
- **Cadillac Escalade IQ** is a separate node from the ICE Escalade.
- **Toyota Land Cruiser** here is the 2024+ 250-series (not the old 200 / LX twin).

## Bias we did not remove

- Reddit `r/whatcarshouldIbuy` over-represents US buyers who post long comparison threads. X added almost no usable pairwise SUV-comfort comments; most hits were unrelated. Edmunds/Cars.com added a few clean family-class pairs and almost no luxury pairs.
- Brand subreddits (`r/BMWX5`, `r/RangeRover`, `r/Lexus`) tilt toward the home team. We down-weight thin home-team comments; we do not delete them, because many owners there have also owned the rival.
- "Comfort" is not one thing. Volvo wins seats; Lincoln / Range Rover win softness; BMW often wins "I wasn't tired" via support rather than plushness. The model averages those meanings.
- Wheel size and air suspension flip results inside a nameplate. An XC60 on 21s loses to a Q5 on air; the same XC60 on 19s often wins. We code the specific spec when the commenter named it, otherwise the typical retail car.
- Sample grew from ~99 to 214, then to 297 after the Outback / Ascent / RX / GX pass, then to **453** weighted votes after a fourth pass aimed at thin compact-luxury / midsize / flagship nameplates, missing three-row models (Pathfinder, Sorento, Passport, Atlas, Grand Wagoneer), GX 550 / Land Cruiser / 4Runner, and more Edmunds/Cars.com owner pairs. Treat ranks as a reading of this corpus, not a census of owners. One 241-upvote test-drive write-up is down-weighted by `log(1+upvotes)` so it boosts Q8/MDX/Q7 but does not own the scale. The bias-adjusted fit removes that karma term entirely.

## Date and sources

Collected 18 August 2026 from public Reddit threads and X search, then expanded the same day with Edmunds and Cars.com **consumer** reviews (journalist road tests still tagged `journalist` and dropped) plus a second Reddit pass on three-row family SUVs and thin luxury nameplates. Primary threads:

- [Most comfortable SUV under $55k](https://old.reddit.com/r/whatcarshouldIbuy/comments/1gi84ub/)
- [Most comfortable small/mid SUV for a retiree](https://old.reddit.com/r/whatcarshouldIbuy/comments/1kipn8g/)
- [CR-V vs Outback vs CX-50 for long drives](https://old.reddit.com/r/whatcarshouldIbuy/comments/1opp4z4/)
- [Most comfortable crossover — is XC60 the answer?](https://old.reddit.com/r/whatcarshouldIbuy/comments/1nejfj3/)
- [Most comfortable luxury SUV?](https://old.reddit.com/r/whatcarshouldIbuy/comments/1fxpil5/)
- [Most comfortable SUV or sedan you have driven](https://old.reddit.com/r/whatcarshouldIbuy/comments/1mbg5ci/)
- [GLE vs X5](https://old.reddit.com/r/BMWX5/comments/1khcp25/)
- [XC90 vs other luxury brands](https://old.reddit.com/r/VolvoXC90/comments/1k10oqw/)
- [Lexus ride quality](https://old.reddit.com/r/Lexus/comments/1mbotxx/)
- [Why Range Rover over the alternatives](https://old.reddit.com/r/RangeRover/comments/1tvpsc8/)

Second-pass threads (family three-row and sparse luxury):

- [Palisade Calligraphy vs CX-90 vs Grand Highlander](https://old.reddit.com/r/HyundaiPalisade/comments/18yshg3/)
- [Highlander vs Palisade vs Pilot](https://old.reddit.com/r/whatcarshouldIbuy/comments/1imxwt9/)
- [Grand Highlander Hybrid vs Palisade](https://old.reddit.com/r/ToyotaGrandHighlander/comments/1ni1ytb/)
- [Pilot vs Grand Highlander](https://old.reddit.com/r/hondapilot/comments/1q04x8z/)
- [Palisade vs Pilot](https://old.reddit.com/r/HyundaiPalisade/comments/1u88tgf/)
- [Aviator vs X5](https://old.reddit.com/r/carbuying/comments/1oyqp8t/)
- [Aviator vs X7](https://old.reddit.com/r/lincolnmotorco/comments/1oxqycn/)
- [X7 vs GLS](https://old.reddit.com/r/bmwx7/comments/1nzv4yx/)
- [X7 vs Escalade](https://old.reddit.com/r/whatcarshouldIbuy/comments/1hplh9w/)
- [Escalade to X7](https://old.reddit.com/r/BMW/comments/14x5517/)
- [Model X vs Escalade](https://old.reddit.com/r/TeslaModelX/comments/1gfaxi9/)
- [Nautilus vs RX](https://old.reddit.com/r/whatcarshouldIbuy/comments/1nii2zi/)
- [XC60 vs Nautilus](https://old.reddit.com/r/VolvoXC60/comments/1sthyuw/)
- [XC90 to Q7](https://old.reddit.com/r/AudiQ7/comments/1qj0cv1/)
- [Palisade vs Highlander comfort](https://old.reddit.com/r/ToyotaHighlander/comments/15vt1b4/)
- [Palisade ride vs others](https://old.reddit.com/r/HyundaiPalisade/comments/shirxh/)
- [Palisade vs Grand Highlander](https://old.reddit.com/r/HyundaiPalisade/comments/1sm5dk5/)
- [Ascent vs Palisade / Pilot / Highlander](https://old.reddit.com/r/SubaruAscent/comments/1ma59pu/)
- [Escalade ESV vs Navigator L](https://old.reddit.com/r/whatcarshouldIbuy/comments/1o6ue2b/)
- [2025 Navigator L AMA](https://old.reddit.com/r/lincolnmotorco/comments/1mxp6lh/)
- [I test drove a bunch of midsize luxury SUVs](https://old.reddit.com/r/whatcarshouldIbuy/comments/1bexbx9/)
- [X5 or Q7](https://old.reddit.com/r/AudiQ7/comments/1jg90iw/)
- [GLC vs X3](https://old.reddit.com/r/BMWX3/comments/1kugnjo/)

Third-pass threads (Outback generations, Ascent, 2020–22 RX, GX 460):

- [RAV4 or Outback](https://old.reddit.com/r/Subaru_Outback/comments/1rryw3t/)
- [Outback or RAV4 (r/rav4club)](https://old.reddit.com/r/rav4club/comments/vgj6rw/)
- [Forester vs Outback](https://old.reddit.com/r/subaru/comments/1864k3l/)
- [2025 Outback vs 2026 CR-V Hybrid](https://old.reddit.com/r/Subaru_Outback/comments/1nzgqor/)
- [2026 Outback Limited quieter?](https://old.reddit.com/r/Subaru_Outback/comments/1sci3jp/)
- [Thought I was switching to a 2026 Outback](https://old.reddit.com/r/SubaruForester/comments/1siky1s/)
- [Ascent vs competition](https://old.reddit.com/r/SubaruAscent/comments/1g5ynww/)
- [2021/22 Ascent after Palisade / Telluride / Highlander](https://old.reddit.com/r/SubaruAscent/comments/qd4b5z/)
- [Ascent or Forester](https://old.reddit.com/r/SubaruAscent/comments/1jwr14g/)
- [RX 350 vs GX 460](https://old.reddit.com/r/Lexus/comments/18r9z6m/)
- [2022 RX350 or 2023 Highlander](https://old.reddit.com/r/Lexus/comments/1hue8eu/)
- [CPO GX460 vs 4Runner Limited](https://old.reddit.com/r/LexusGX/comments/177g7u9/)
- [GX460 over 4Runner for a family](https://old.reddit.com/r/LexusGX/comments/1u23qmr/)

Fourth-pass threads (thin luxury, missing three-row, trucks):

- [GV70 vs SQ5 vs Macan](https://old.reddit.com/r/GenesisGV70/comments/1d1bpec/)
- [NX vs GLC](https://old.reddit.com/r/LexusNX/comments/1tyb8s9/)
- [NX vs XC60](https://old.reddit.com/r/LexusNX/comments/1mttqev/)
- [CR-V vs CX-50](https://old.reddit.com/r/crv/comments/1ig8mju/)
- [Venza vs CR-V](https://old.reddit.com/r/Toyotavenza/comments/19amr95/)
- [Nautilus vs XT5](https://old.reddit.com/r/lincolnmotorco/comments/15bxna5/)
- [GLE vs XC90](https://old.reddit.com/r/mercedes_benz/comments/t63dlp/)
- [Q7 vs X5 / GLE](https://old.reddit.com/r/AudiQ7/comments/17xx4yw/)
- [Aviator vs GV80](https://old.reddit.com/r/GenesisMotors/comments/1hleau4/)
- [iX vs Model X](https://old.reddit.com/r/ModelX/comments/1emwzix/)
- [iX vs X5](https://old.reddit.com/r/BMWiX/comments/1g2dc3f/)
- [Pathfinder vs Pilot](https://old.reddit.com/r/nissanpathfinder/comments/1uyw9q3/)
- [Palisade vs Pathfinder](https://old.reddit.com/r/HyundaiPalisade/comments/1kk9vjf/)
- [Telluride vs Sorento](https://old.reddit.com/r/KiaTelluride/comments/1gq26u3/)
- [Atlas vs Pilot](https://old.reddit.com/r/VWatlas/comments/1ftqorz/)
- [Pilot vs Grand Highlander](https://old.reddit.com/r/hondapilot/comments/1bx1rm6/)
- [Passport vs Pilot](https://old.reddit.com/r/hondapilot/comments/1nn8r97/)
- [X7 vs Range Rover](https://old.reddit.com/r/RangeRover/comments/1p44h0d/)
- [Navigator vs Grand Wagoneer](https://old.reddit.com/r/lincolnmotorco/comments/1eqta1w/)
- [GX 550 vs 4Runner](https://old.reddit.com/r/LexusGX550/comments/1ikvbg1/)
- [Land Cruiser vs 4Runner](https://old.reddit.com/r/LandCruisers/comments/1lluxml/)

Owner-review pages used when the text named two SUVs and picked a comfort winner:

- [2022 Palisade consumer reviews (Cars.com)](https://www.cars.com/research/hyundai-palisade-2022/consumer-reviews/)
- [2024 / 2026 Palisade consumer reviews (Edmunds)](https://www.edmunds.com/hyundai/palisade/2026/consumer-reviews/)

Edmunds and Cars.com review hubs often returned 403 / bot-challenge pages to automated fetches. See **Getting around blocked review sites** below. Votes from those sites were coded only when the owner-review sentence itself was visible in search snippets, listing excerpts, or an archive (same inclusion rules as Reddit).

Plus scattered Palisade/Telluride threads and a handful of X posts (Model X vs Y, Palisade vs Model Y).

## Getting around blocked review sites

Edmunds and Cars.com consumer-review hubs block many automated fetches (Edmunds `403 Access Denied`; Cars.com Cloudflare challenge). The owner text is still public. Do **not** try to defeat the bot wall with spoofed clients, IP rotation, or CAPTCHA farms. Use an already-public copy of the same review.

What worked in this project, in order:

1. **Search-index snippets.** Query the review page, not the homepage:
   - `site:edmunds.com palisade consumer reviews "quieter than" OR "smoother than" OR "traded"`
   - `site:cars.com "test drove both" palisade telluride`
   Google/Bing often quote the full owner paragraph in the snippet. Code from that paragraph only if it still names two SUVs and a comfort winner.
2. **Listing and model pages that reprint reviews.** Cars.com inventory pages and Edmunds model hubs sometimes echo the same consumer blurb that the `/consumer-reviews/` URL refuses. Same inclusion rules; record the URL you actually read.
3. **Internet Archive.** If the live page is a challenge screen, try  
   `https://web.archive.org/web/https://www.edmunds.com/.../consumer-reviews/`  
   (or the Cars.com equivalent). Prefer a snapshot that shows the owner name + body, not a homepage capture.
4. **Search-engine cache.** Google/Bing “cached” copies of the consumer-review URL, when they exist, are another public reprint.
5. **A real browser session.** Opening the page as a logged-out human usually works. Copy the quote by hand. Do not automate that session.

Reddit-specific: fetch **`old.reddit.com`** thread URLs, not `www.reddit.com`. The old site is plain HTML and does not need the new-reddit app shell.

Still required after any of the above:

- The quote must be first-hand and name a loser. A snippet that only says “quieter, rides much smoother” with no other model is not a vote.
- Prefer the canonical review URL in `comparisons.csv` even if you found the text via a snippet or archive. Note the access path in the quote or a comment if the live page is still blocked.
- Journalist Edmunds/Cars.com road tests stay `journalist` and drop out of the default fit.
