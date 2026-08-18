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

A third fit is **owners only** (`data/ranking_owners.csv`). It keeps `owned_both`, `owned_one_td_other`, `owned_one_family`, `owned_one_loaner`, and `owned_one_rode_other`, and drops `test_drove_both` plus passenger / opinion / journalist. Default weights otherwise. See [`owner_analysis.md`](owner_analysis.md). The script also still prints a lived-with-both-only robustness column (`owned_both`, no karma boost).

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

Three-row family crossovers (Palisade, Telluride, Highlander, Grand Highlander, Pilot, CX-90, Ascent, Santa Fe) sit between the last two and are reported separately when they appear. Full-size Expedition is scored with flagship / large SUVs, but its new sample is still a family-truck split. Lexus TX is scored with midsize luxury because that is who it is cross-shopped against, even though it shares a platform with Grand Highlander. Lexus GX 460 and Toyota 4Runner sit with midsize luxury for the same reason (that is who they meet); they are body-on-frame trucks, not X5s.

## Generations we split

Most nameplates stay one node. Two changes this pass:

- **Subaru Outback 2026** is a new generation (wagon → more upright crossover). It is coded separately from **Subaru Outback** (2020–2025, 6th gen). A same-garage 2026 vs 2020/2019 note is a vote, not a same-nameplate exclude.
- **Lexus RX** still includes 2020–2022 AL20 (RX 350 / 350L / 450h / 450hL) and 2023+ AL30. Year is kept in the quote when the author named it. Splitting RX would orphan the older mixed-year rows.
- **Lexus GX** here is the 2014–2023 GX 460 (J150). **Lexus GX 550** is a separate node. First-hand 460-vs-550 notes are votes, not same-nameplate excludes.
- **Cadillac Escalade IQ** is a separate node from the ICE Escalade.
- **Toyota Land Cruiser** here is the 2024+ 250-series (not the old 200 / LX twin).
- **Chevrolet Tahoe** is a separate node from Suburban when the author named Tahoe.

## Bias we did not remove

- Reddit `r/whatcarshouldIbuy` over-represents US buyers who post long comparison threads. X added almost no usable pairwise SUV-comfort comments; most hits were unrelated. Edmunds/Cars.com added a few clean family-class pairs and almost no luxury pairs.
- Brand subreddits (`r/BMWX5`, `r/RangeRover`, `r/Lexus`) tilt toward the home team. We down-weight thin home-team comments; we do not delete them, because many owners there have also owned the rival.
- "Comfort" is not one thing. Volvo wins seats; Lincoln / Range Rover win softness; BMW often wins "I wasn't tired" via support rather than plushness. The model averages those meanings.
- Wheel size and air suspension flip results inside a nameplate. An XC60 on 21s loses to a Q5 on air; the same XC60 on 19s often wins. We code the specific spec when the commenter named it, otherwise the typical retail car.
- Sample grew from ~99 to 214, then to 297 after the Outback / Ascent / RX / GX pass, then to 453 after a fourth pass on thin luxury / missing three-row / trucks, then to 554 after a fifth pass on remaining thin flagship / mid-luxury / compact / three-row / truck nodes, then to 633 after a sixth pass on Yukon / Tahoe / Suburban / QX80 / Escalade IQ, EQS SUV / Defender / R1S / Cayenne / Macan, Crosstrek / Corsair / X1 / Model Y, and CX-90 / Pathfinder / Murano / Passport, then to 725 after a seventh pass on Yukon / R1S / Sequoia / QX80 / Tahoe, Defender / Cayenne / Grand Cherokee, Crosstrek / Corsair / X1 / Murano / Model Y, and CX-90 / Explorer / Enclave / GCL, then to 792 after an eighth pass on Escalade IQ / EQS SUV / LX / Yukon / Land Cruiser, Defender / Grand Cherokee / Cayenne / R1S / Model Y, Venza / Tiguan / Corsair / X1 / Crosstrek, and leftover GCL / XT5 / Enclave owner-review lines, and finally to **805 weighted votes (809 coded rows)** after a ninth pass on Expedition / Suburban / Tahoe / Escalade / Navigator, 2026 Santa Fe / Palisade, and fresh RR / GLS / Q7 / X5 / GV80 links. Treat ranks as a reading of this corpus, not a census of owners. One 241-upvote test-drive write-up is down-weighted by `log(1+upvotes)` so it boosts Q8/MDX/Q7 but does not own the scale. The bias-adjusted fit removes that karma term entirely.

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

Fifth-pass threads (remaining thin flagship / mid-luxury / compact / three-row / truck):

- [GLS vs X7 (r/mercedes_benz)](https://old.reddit.com/r/mercedes_benz/comments/1tb4gtd/)
- [X7 vs GLS / Escalade](https://old.reddit.com/r/bmwx7/comments/1vdka3x/)
- [Escalade vs rental X7](https://old.reddit.com/r/bmwx7/comments/1q2bau6/)
- [EQS SUV vs iX owned both](https://old.reddit.com/r/BMWiX/comments/1n7z1m4/)
- [Q8 vs X5](https://old.reddit.com/r/BMWX5/comments/1qoeyi1/)
- [R1S vs XC90 / MDX / GV80](https://old.reddit.com/r/Rivian/comments/1d717bt/)
- [Defender vs GX 550](https://old.reddit.com/r/LexusGX550/comments/1qsxj0w/)
- [GV70 vs Nautilus](https://old.reddit.com/r/GenesisGV70/comments/1fpluz2/)
- [GV70 vs NX](https://old.reddit.com/r/LexusNX/comments/1oyu0kp/)
- [Tiguan vs RAV4 / CR-V](https://old.reddit.com/r/Tiguan/comments/1izzwia/)
- [Enclave vs Palisade](https://old.reddit.com/r/HyundaiPalisade/comments/1i2w104/)
- [Atlas vs Telluride](https://old.reddit.com/r/VWatlas/comments/1rpc4fb/)
- [Passport vs 4Runner](https://old.reddit.com/r/hondapassport/comments/1p7rfj1/)
- [GX 550 vs Land Cruiser](https://old.reddit.com/r/LexusGX/comments/1htwbzj/)
- [LX / Sequoia / TX](https://old.reddit.com/r/Lexus/comments/1s68u5o/)

Sixth-pass threads (thin flagship trucks, mid-luxury / EV, compact, remaining three-row):

- [Yukon Denali Ultimate vs AT4 / Escalade](https://old.reddit.com/r/gmc/comments/1qff0ms/)
- [Grand Wagoneer vs Escalade vs Navigator](https://old.reddit.com/r/Cadillac/comments/1d2hnnw/)
- [Wagoneer vs Tahoe / Yukon](https://old.reddit.com/r/whatcarshouldIbuy/comments/1c7ig0f/)
- [Tahoe to GX 550](https://old.reddit.com/r/LexusGX/comments/1ighcjb/)
- [Escalade IQ AMA](https://old.reddit.com/r/Cadillac/comments/1iczh1s/)
- [Tahoe / Yukon / Sequoia](https://old.reddit.com/r/gmc/comments/1ilm79y/)
- [QX80 vs Escalade](https://old.reddit.com/r/whatcarshouldIbuy/comments/1r92flo/)
- [EQS SUV vs iX](https://old.reddit.com/r/BMWiX/comments/1dbdtul/)
- [Macan vs GV70](https://old.reddit.com/r/GenesisGV70/comments/1jqm8fq/)
- [Model X vs R1S](https://old.reddit.com/r/Rivian/comments/1cttrwt/)
- [Defender seat comfort](https://old.reddit.com/r/NewDefender/comments/1oycglg/)
- [RRS vs Defender](https://old.reddit.com/r/LandRover/comments/1n7bd1f/)
- [Pilot vs CX-90](https://old.reddit.com/r/hondapilot/comments/1k9kymr/)
- [2026 Murano vs Pathfinder](https://old.reddit.com/r/Nissan/comments/1vczalz/)
- [Pathfinder vs Highlander](https://old.reddit.com/r/nissanpathfinder/comments/1se7lew/)
- [Outback vs Crosstrek](https://old.reddit.com/r/subaru/comments/1n2i0bi/)
- [Model X vs Y](https://old.reddit.com/r/TeslaModelX/comments/1f79pdw/)
- [2025 Tiguan vs CR-V](https://old.reddit.com/r/Tiguan/comments/1l73h71/)

Seventh-pass threads (Yukon / R1S / Sequoia, Defender / Cayenne / Grand Cherokee, remaining compact and three-row):

- [Yukon Denali to R1S](https://old.reddit.com/r/Rivian/comments/1o5m69h/considering_switch_from_yukon_denali_to_r1sanyone/)
- [R1S driving comfort vs others](https://old.reddit.com/r/Rivian/comments/12y9lsg/how_does_driving_comfort_compare_with_other/)
- [Lexus to GMC Yukon](https://old.reddit.com/r/gmc/comments/147e881/lexus_to_gmc/)
- [Model X to R1S](https://old.reddit.com/r/Rivian/comments/1l0h94p/switched_from_tesla_x_to_r1s_detailed_comparison/)
- [RR vs Defender](https://old.reddit.com/r/RangeRover/comments/1lbjadj/strugglingrr_vs_defender/)
- [Cayenne or X5](https://old.reddit.com/r/PorscheCayenne/comments/1nl126k/cayenne_or_x5/)
- [X5 vs GLE owner feedback](https://old.reddit.com/r/BMWX5/comments/1d5xb30/bmw_x5_vs_mercedesbenz_gle_owner_feedback_needed/)
- [Grand Cherokee vs X5 / GLE](https://old.reddit.com/r/GrandCherokee/comments/h7s402/officially_joined_the_jeep_club_its_a_2018_grand/)
- [X1 vs X3](https://old.reddit.com/r/BMW/comments/1oaw3u6/am_i_crazy_for_preferring_the_x1_over_the_x3/)
- [Murano vs Pathfinder](https://old.reddit.com/r/nissanpathfinder/comments/1nfzc56/)
- [Corsair vs XC60](https://old.reddit.com/r/lincolnmotorco/comments/1evcups/)
- [Outback vs Crosstrek seats](https://old.reddit.com/r/subaru/comments/1i4q03v/)
- [CX-90 vs Pilot seats](https://old.reddit.com/r/MazdaCX90/comments/1sfskcv/)
- [Explorer vs 4Runner](https://old.reddit.com/r/FordExplorer/comments/1gkxc16/)

Eighth-pass threads (Escalade IQ / EQS SUV / LX / Yukon / LC, Defender / Grand Cherokee / Cayenne / R1S / Model Y, Venza / Tiguan / Corsair / X1, leftover reviews):

- [MX HW3 vs Escalade IQ](https://old.reddit.com/r/TeslaFSD/comments/1qp9m1z/mx_hw3_fsd_vs_escalade_iq_blue_cruise/)
- [Cadillac EV regrets](https://old.reddit.com/r/Cadillac/comments/1uk1si1/any_regrets_buying_cadillac_ev_lyric_or_vistiq_or/)
- [IQ vs gas Escalade](https://old.reddit.com/r/Cadillac/comments/1q4ycd0/help_me_choose_should_i_make_the_change/)
- [iX vs EQS](https://old.reddit.com/r/BMWiX/comments/1mmpydw/ix_vs_eqs/)
- [R1S vs EQS](https://old.reddit.com/r/Rivian/comments/16eteh0/r1s_vs_eqs/)
- [2021 GLE 53 after X5s](https://old.reddit.com/r/AMG/comments/q1gbok/thoughts_on_21_amg_gle_53_after_2k_miles/)
- [Sequoia vs LX](https://old.reddit.com/r/LandCruisers/comments/1qmwkdb/lexus_bias_aside_sequoia_vs_lx_570_for_longterm/)
- [2025 LC impressions](https://old.reddit.com/r/LexusGX/comments/1ldxrlw/2025_land_cruiser_driving_impressions/)
- [Yukon over Suburban/Tahoe](https://old.reddit.com/r/gmc/comments/1qvx1jp/2526_yukon_over_suburbantahoe/)
- [Talk me out of trading for a Range Rover](https://old.reddit.com/r/NewDefender/comments/1sxe4iu/talk_me_out_of_trading_for_a_range_rover/)
- [GX550 v Defender](https://old.reddit.com/r/NewDefender/comments/1qsxes3/gx550_v_defender/)
- [R1S test drive after Defender](https://old.reddit.com/r/Rivian/comments/1k2wct8/took_a_test_drive_of_an_r1s_at_rivian_3_days_ago/)
- [R1S coming from X5](https://old.reddit.com/r/Rivian/comments/15jtz7v/very_conflicted_after_test_driving_the_r1s_coming/)
- [Venza vs RAV4](https://old.reddit.com/r/Toyotavenza/comments/10nmo6u/venza_vs_rav_4/)
- [Tiguan vs RAV4](https://old.reddit.com/r/Tiguan/comments/1qh9gy8/tiguan_vs_rav4_similar_sizes_different_priorities/)
- [Corsair or Nautilus](https://old.reddit.com/r/lincolnmotorco/comments/1gq264h/corsair_or_nautilus/)

Ninth-pass comparison threads:

- [Expedition owner comparison with Suburban / Yukon](https://old.reddit.com/r/fordexpedition/comments/1rl3wmy/)
- [Tahoe / Suburban vs 2025 Expedition](https://old.reddit.com/r/ChevyTahoe/comments/1kob8dv/)
- [Expedition vs Escalade](https://old.reddit.com/r/fordexpedition/comments/1i3q2b9/)
- [Tahoe / Suburban vs 2026 Expedition](https://old.reddit.com/r/fordexpedition/comments/1meko7j/)
- [2026 Palisade vs Santa Fe](https://old.reddit.com/r/HyundaiPalisade/comments/1onsp6r/)
- [Santa Fe vs Palisade, both owned](https://old.reddit.com/r/HyundaiPalisade/comments/1ux87px/)
- [2026 Palisade / Santa Fe decision](https://old.reddit.com/r/HyundaiPalisade/comments/1o1qoue/)
- [Palisade loaner vs Santa Fe Hybrid](https://old.reddit.com/r/HyundaiPalisade/comments/1u1qfhh/)
- [Range Rover vs GLS](https://old.reddit.com/r/whatcarshouldIbuy/comments/1kemw8r/)
- [Q7 vs X5 / RX / XC90](https://old.reddit.com/r/whatcarshouldIbuy/comments/1vd150j/)
- [X5 vs GV80 vs Q7](https://old.reddit.com/r/whatcarshouldIbuy/comments/1j6z1bc/)

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
