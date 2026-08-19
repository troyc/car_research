# Owner-only comfort ranking

Same pairwise file as [`composite_ranking.md`](composite_ranking.md), but **test drivers are out**. A same-day loop is not a year in the car. This fit keeps only people who owned, leased, or lived with at least one of the two SUVs.

Default ranking (owners + testers): [`composite_ranking.md`](composite_ranking.md). Source-bias fit: [`bias_analysis.md`](bias_analysis.md). Method: [`methodology.md`](methodology.md). Machine table: [`../data/ranking_owners.csv`](../data/ranking_owners.csv).

`python3 src/rank.py` writes this table. Weights match the default fit (`log(1+upvotes)`, home-team `×0.6`). The only change is who is allowed to vote.

## Who is in

| Evidence | Kept? | Rows in file |
|---|---|---:|
| `owned_both` | yes | 318 |
| `owned_one_td_other` | yes — they own one | 196 |
| `owned_one_family` | yes | 23 |
| `owned_one_loaner` | yes | 18 |
| `owned_one_rode_other` | yes | 9 |
| `test_drove_both` | **no** | 177 |
| `opinion` / `opinion_plus_drive` / `passenger` / journalist | no | 48 |

**563 weighted votes** after the usual sedan drop (Lexus ES / Audi A7). **317** of those are lived-with-both. Testers are **176 / 786** of the default file (~22%). The audit recoded a large pile of `test_drove_both` to `owned_one_td_other` (owns one, sat in the other), so those rows now vote here instead of in the tester pile.

`owned_one_td_other` stays because the author is an owner comparing to a car they sat in. If you want the stricter garage-vs-garage cut, the script also prints **owned_both only** (no karma boost). That sample is 317 votes and is thinner at the flagship end.

## The owner chain

Ignore raw global θ. GLS is 8–0 almost entirely vs X7. EQS SUV is 4–0 vs iX. 2026 Outback is 7–0 vs the wagon it replaced. Same graph rule as the composite: who met whom.

**Range Rover ≈ GLS > Range Rover Sport / iX / EQS SUV / Escalade IQ / Escalade / X7 / Yukon / Aviator / GLE / Q7 / MDX > XC90 / RX / GX 460 > XC60 / Nautilus / Palisade ≥ Pathfinder (seats vs Pilot) ≥ Telluride > Pilot / Ascent / Highlander / 2020–25 Outback / CR-V > X5 / Crosstrek / CX-5 / GX 550 > CX-50 / X3 / RAV4 / Forester / 4Runner / Model Y / X1**

Owner-only Yukon is **17–3**. Same-garage air Yukon over R1S is still the owner-only truck result. Escalade IQ is **6–1** among owners. EQS SUV is **9–1** vs iX / R1S. QX80 is 4–0 on seats in a tiny sample. The Expedition owner rows split Suburban / Tahoe / Escalade / Navigator rather than lifting it into the luxury chain. Santa Fe has only Palisade owner comparisons and loses those four. Defender still loses to Range Rover among people who lived with both and now beats R1S / Cayenne in that cut. X5’s owner rank collapses (default 11 → owner 54) once same-day loops are out.

That is close to the full-sample shopping chain. The middle is not.

## What testers were doing that owners do not

| Pair | Owners | Testers | What changed |
|---|---|---|---|
| GLE vs X5 | **GLE** still wins owner notes | X5 still wins some testers | Testers picked the sport-luxury daily. Households that ran both pick GLE for road trips. GLE is 15–9 among owners; X5 is 28–34. |
| Ascent record | **15–6** | still brand-sub heavy | Default 22–9. Many Ascent “testers” were recoded to `owned_one_td_other` (own Ascent, sat in the others), so they stay in this cut. `no_home` still dumps Ascent. |
| Q5 vs XC60 | XC60 still wins owner chairs | testers liked Q5 air | Compact-luxury testers liked Q5 air. Owners keep Volvo chairs. |
| XC60 overall | **12–4** | thinner tester leftover | Same story at the nameplate. |
| Q5 overall | 7–7 | testers still win some loops | Most Q5 wins were 20-minute loops. |
| Telluride | **18–14** | still loses to Palisade | Testers compared it to Palisade and lost. Owners compared it to Explorer / Sorento / Pathfinder and won more often. |
| Palisade | **31–11** | leftover testers | Still the three-row default. |
| GV70 | 8–4 | testers vs Macan / SQ5 / X3 | The old 9–0 headline was testers. Owners now include a Nautilus and RX counter. |
| GV80 | 2–5 | tester-heavy | Thin owner pile. Do not rank it from this cut. |
| Grand Highlander | 1–8 | leftover testers | Almost no owner-vs-owner GH notes. |
| Escalade vs Navigator | Escalade ride | Navigator seats | Ride vs seats. Owners lean Escalade air. |
| Venza vs CR-V | **Venza** | testers split | Owners who had both call Venza quieter / better seats. |
| iX vs X5 | **iX** keeps quiet | some testers keep X5 seats | Owners who lived with iX keep it for quiet. |

### GLE vs X5 is the headline flip

Every owner who named both and picked a comfort winner picked the Mercedes:

- “The GLE is a dramatically smoother ride and is my choice for a road trip.”
- “Mercedes is larger and more comfortable on longer trips.”
- “The X5 is more fun to drive… the Benz has… plusher and smoother drive for road trips.”
- “GLE is better for road-trips ngl and the x5 better to daily.”
- “I do miss the merc seats… Felt the Benz seats were buttery and plush.”

The default fit still parks X5 near Escalade / Aviator (θ 2.98, rank 11) because testers on `r/whatcarshouldIbuy` and `r/BMWX5` keep handing it same-day wins. Owners who actually swapped or ran both do not — X5 is 28–34 here and global owner rank 54. **If the question is “which one after 10,000 miles,” use this file, not the composite θ for X5.**

Two owned-both Q7 households said the same thing vs X5: Audi smoother and quieter with air; one switcher wanted the Q7 seats back.

### Ascent was a test-drive nameplate

Default Ascent is 22–9, global rank 29, θ next to GX. Owners: **15–6**, rank 34. The audit moved most of the old same-day Ascent pile into `owned_one_td_other`, so those `r/SubaruAscent` shoppers who already own the car now vote here.

What owners actually said:

- Pilot vs Ascent: “her Pilot is more comfortable to drive and the seats feel better.” Another household: FIL’s Pilot “feels nicer, is smoother.”
- Outback vs Ascent is still split. Two households said the Outback rides better; two use the Ascent for long trips.

The leftover tester rows are still “I drove Palisade / Telluride / Highlander / Ascent today.” That is a real first-hand vote. It is not a year in the car. `no_home` (bias file) is the check that Ascent’s sample is still brand-sub heavy. Ascent is a mid-pack three-row, not a comfort pick over Palisade.

### Palisade and Telluride both look better without testers

Palisade is **31–11** among owners. Still beats Pilot on ride (“drives much smoother and is very quite”; Cars.com “Rides better than our Honda Pilot”). An Enclave household gave Palisade the seats and the Buick the smoother ride. Same-garage Palisade vs CX-90: Palisade ride/luxury, CX-90 firmer.

Telluride is **18–14**. That is not “beat Palisade.” It is beat Explorer (several owned-both), Sorento, Pathfinder, and split Pilot. Testers kept matching it to Palisade. Owners who bought a Telluride after an Explorer are not the same population.

Pathfinder vs Pilot is still an owned-both seat win. “pathfinders seats are super comfortable especially compared to the Honda Pilot.” Palisade still beats Pathfinder on ride.

### Compact luxury: XC60 stays; Q5 and GV70 shrink

Owner compact-luxury order (within-segment pairs): **Nautilus / 2026 Outback / Venza / XC60 > CR-V ≈ 2020–25 Outback / Q5 > CX-5 > CX-50 / X3 / Forester / RAV4**.

- **XC60 is 12–4.** One owned-both vs Q5: “I found the seats of the xc60 way nicer than the q5. I don’t think they compare at all.”
- **Q5 is 7–7.** Testers still hold some air-suspension loops vs XC60. Those same-day wins are gone from this cut.
- **GV70 is 8–4.** Do not read the default 14–4 as an owner-only compact-luxury result — several of those are testers vs Macan / SQ5 / X3.
- **Nautilus 10–2** and **GLC 4–4** survive.
- **Venza 13–3**, including CR-V losses for Honda: “seats and road noise are a world of difference”; “The seat comfort is PHENOMENAL.”

### Compact wagons and trucks do not flip

These owner records are the same story as the composite, just cleaner:

- **2026 Outback 10–0.** “'26 Limited is definitely quieter and smoother” than a ’20 Premium; 2019 Limited → 2026 Touring “much quieter.”
- **2020–25 Outback 21–13.** Beats RAV4 and Forester in owned-both notes. Splits CR-V.
- **RAV4 1–28. Forester 2–10. CX-50 1–10. X3 3–10.**
- **GX 460 vs 4Runner** is still almost all owned-both: “softer / quieter / smoother”; same-garage 2023 GX + 2023 TRD Pro; three Limited 4Runners → GX460. **4Runner is 3–21 among owners.**
- **GX 550 vs 4Runner** still favors the Lexus among owners.
- **GX vs RX is still a split.** Unibody RX is usually smoother; some GX households prefer isolation / less road noise. Not an X5.

### Flagship is thinner, not different

- **Range Rover 14–2.** Still the ceiling vs RX / GLE / X5 / Q8 / RRS. The losses are still not a current flagship rival winning isolation.
- **GLS 11–1.** Same Mercedes-plush note as testers, mostly vs X7.
- **Escalade 12–11.** Ride over Navigator in same-garage notes (“Escalade was leagues above in ride quality”; 2025 Navigator owner vs wife’s 2024 Escalade). Navigator still wins some seats.
- **iX 9–7.** Quieter / smoother than X5 for people who owned or loaned both; EQS SUV still wins that garage.
- **Aviator 7–2.** Still comfort-first vs X5. Not undefeated.

Yukon 17–3 is a real owner truck sample (mostly vs R1S / Sequoia). It is not Yukon-over-Range Rover.

## Ranks that move (core nameplates)

Global rank among every model that appears in that fit. Sparse 1-appearance cars sit in the file, so “rank 25 Palisade” is not “25th among shoppers.”

| Model | Default W–L | Owner W–L | Both W–L | Def rank | Owner rank | owned_both rank |
|---|---:|---:|---:|---:|---:|---:|
| Range Rover | 15–2 | 14–2 | 8–1 | 3 | 3 | 2 |
| Mercedes GLS | 17–4 | 11–1 | 6–1 | 2 | 2 | 4 |
| Mercedes GLE | 21–14 | **15–9** | 12–4 | 27 | **6** | 22 |
| BMW X5 | 35–50 | 28–34 | 14–20 | 11 | **54** | 35 |
| BMW iX | 11–7 | 9–7 | 7–5 | 6 | 4 | 10 |
| Audi Q7 | 9–5 | 6–1 | 4–1 | 32 | 10 | 19 |
| Lincoln Aviator | 14–4 | 7–2 | 3–1 | 13 | 17 | 13 |
| Lexus RX | 19–14 | 14–9 | 12–6 | 26 | 30 | 26 |
| Genesis GV70 | 14–4 | 8–4 | 0–2 | 18 | 36 | 61 |
| Subaru Ascent | 22–9 | 15–6 | 6–4 | 29 | 34 | 33 |
| Hyundai Palisade | 54–22 | 31–11 | 16–3 | 46 | 29 | 7 |
| Kia Telluride | 28–26 | 18–14 | 12–1 | 52 | 44 | 21 |
| Honda Pilot | 33–37 | 25–26 | 6–11 | 31 | 43 | 34 |
| Nissan Pathfinder | 15–11 | 12–10 | 5–6 | 45 | 40 | 24 |
| Volvo XC60 | 17–12 | **12–4** | 8–1 | 37 | 27 | 20 |
| Audi Q5 | 15–9 | 7–7 | 1–3 | 33 | 51 | 56 |
| Subaru Outback 2026 | 12–1 | 10–0 | 3–0 | 40 | 9 | 8 |
| Subaru Outback | 31–16 | 21–13 | 17–9 | 58 | 46 | 44 |
| Honda CR-V | 21–18 | 16–14 | 7–8 | 42 | 47 | 55 |
| Lexus GX | 25–14 | 20–13 | 14–7 | 28 | 37 | 32 |
| Toyota 4Runner | 3–24 | 3–21 | 2–18 | 72 | 72 | 73 |
| Toyota RAV4 | 1–31 | 1–28 | 0–18 | 76 | 75 | 76 |

Palisade’s owner θ is less depressed than the default (−0.33 → +0.86) because it is no longer drowning in a huge tester graph of other three-rows. It still did not meet a Range Rover.

## Bias this cut does not fix

Owners are not a cleaner census. They are a different bias.

1. **Switcher justification.** People who sold an X5 for a GLE, or a Pilot for a Palisade, tend to say the new one is more comfortable. Testers do not have that sunk cost. The GLE 15–9 and Palisade 31–11 should be read with that in mind. Lived-with-both is the best evidence in the file. It is also the most post-hoc.
2. **Home-team rate is higher among owners now.** 314 / 563 owner rows are `home_team=1` (56%). Testers are 70 / 176 (40%). The audit flipped many home-badge flags and recoded brand-sub shoppers into `owned_one_td_other`. Dropping testers does not drop brand-sub cooking. GX-vs-4Runner owner notes still live on `r/LexusGX`.
3. **Edmunds / Cars.com are more owner than tester** (72 vs 5). That is why Palisade / Pathfinder / Venza look a little cleaner here. Luxury pairs are still mostly Reddit.
4. **Luxury testers filled holes owners do not.** GV80, Grand Highlander, Cayenne, Q8, and some X7–GLS volume are still tester-heavier. This cut is stronger on family / compact / GX and weaker on compact-luxury shootouts.

## How to use this next to the composite

The composite chain is still the shopping document if you want every first-hand sit. Use this file for one question: **do people who lived with the cars agree with the people who drove them on Saturday?**

- Flagship ceiling: yes — Range Rover / GLS.
- GLE vs X5: **no** — owners pick GLE; testers pick X5.
- Ascent as a comfort default: **no** — still brand-sub heavy; `no_home` dumps it.
- Palisade in the three-row set: yes.
- Telluride as plywood: **no** — testers vs Palisade said that; owners vs Explorer / Sorento did not.
- Pathfinder seats vs Pilot: yes, and it is owned-both.
- XC60 seats vs Q5 air: **owners keep XC60**; testers kept Q5.
- GV70 14–4: not an owner-only compact-luxury result.
- 2026 Outback quieter than 2020–25: yes, same-garage.
- GX 460 over 4Runner: yes, almost all owned-both.
- RX vs GX: still a split.
- RAV4 / Forester / X3 / 4Runner at the bottom: yes.

Lived-with-both only (317 votes) agrees with the owner cut on GLE, Palisade, Telluride, Pathfinder, GX, 2026 Outback, and the compact losers. It is still thinner at the flagship end.
