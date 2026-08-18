# Owner-only comfort ranking

Same pairwise file as [`composite_ranking.md`](composite_ranking.md), but **test drivers are out**. A same-day loop is not a year in the car. This fit keeps only people who owned, leased, or lived with at least one of the two SUVs.

Default ranking (owners + testers): [`composite_ranking.md`](composite_ranking.md). Source-bias fit: [`bias_analysis.md`](bias_analysis.md). Method: [`methodology.md`](methodology.md). Machine table: [`../data/ranking_owners.csv`](../data/ranking_owners.csv).

`python3 src/rank.py` writes this table. Weights match the default fit (`log(1+upvotes)`, home-team `×0.6`). The only change is who is allowed to vote.

## Who is in

| Evidence | Kept? | Rows in file |
|---|---|---:|
| `owned_both` | yes | 214 |
| `owned_one_td_other` | yes — they own one | 60 |
| `owned_one_family` | yes | 17 |
| `owned_one_loaner` | yes | 8 |
| `owned_one_rode_other` | yes | 6 |
| `test_drove_both` | **no** | 238 |
| `opinion` / `opinion_plus_drive` / `passenger` / journalist | no | 14 |

**303 weighted votes** after the usual sedan drop (Lexus ES / Audi A7). **212** of those are lived-with-both. Testers are still about 43% of the coded file; they are not a rounding error.

`owned_one_td_other` stays because the author is an owner comparing to a car they sat in. If you want the stricter garage-vs-garage cut, the script also prints **owned_both only** (no karma boost). That sample is 212 votes and is thinner at the flagship end.

## The owner chain

Ignore raw global θ. GLS is 8–0 almost entirely vs X7. EQS SUV is 3–0 vs iX. 2026 Outback is 7–0 vs the wagon it replaced. Same graph rule as the composite: who met whom.

**Range Rover ≈ GLS > Range Rover Sport / iX / EQS SUV / Escalade / X7 / Aviator / GLE / Q7 / MDX > X5 / XC90 / RX / GX 460 > XC60 / Nautilus / GLC / Venza > Palisade ≥ Telluride ≥ Pathfinder (seats vs Pilot) > Pilot / Highlander / Ascent / 2020–25 Outback / CR-V > CX-5 / GX 550 > CX-50 / X3 / RAV4 / Forester / 4Runner**

That is close to the full-sample shopping chain. The middle is not.

## What testers were doing that owners do not

| Pair | Owners | Testers | What changed |
|---|---|---|---|
| GLE vs X5 | **GLE 5–0** | X5 6–2 | Testers picked the sport-luxury daily. Households that ran both pick GLE for road trips. |
| Ascent record | **6–6** | 16–3 | Ascent’s default 22–9 is a same-day pile, mostly `r/SubaruAscent`. |
| Pilot vs Ascent | **Pilot 2–0** | Ascent 3–0 | Flip. Owners who share a garage prefer Pilot seats/ride. |
| Q5 vs XC60 | XC60 1–0 | **Q5 4–0** | Compact-luxury testers liked Q5 air. Owners keep Volvo chairs. |
| XC60 overall | **9–2** | 5–9 | Same story at the nameplate. |
| Q5 overall | 4–4 | **8–2** | Most Q5 wins were 20-minute loops. |
| Telluride | **9–3** | 8–13 | Testers compared it to Palisade and lost. Owners compared it to Explorer / Sorento / Pathfinder and won. |
| Palisade | 17–5 | 25–11 | Still the three-row default. Sample just shrinks. |
| GV70 | 3–2 | **8–1** | The old 9–0 headline was testers vs Macan / SQ5 / X3. Owners now include a Nautilus and RX counter. |
| GV80 | 0–2 | 4–5 | No owner pile. Do not rank it from this cut. |
| Grand Highlander | 0–2 | 4–11 | Almost no owner-vs-owner GH notes. |
| CR-V vs Outback | Outback 4–3 | CR-V 2–1 | Still a split. Owners lean Subaru; testers lean Honda. |
| Escalade vs Navigator | Escalade 4–2 | Navigator 2–1 | Ride vs seats. Owners lean Escalade air. |
| Venza vs CR-V | **Venza 3–0** | CR-V 1–0 | Owners who had both call Venza quieter / better seats. |
| iX vs X5 | **iX 3–0** | X5 1–0 | Owners who lived with iX keep it for quiet. |

### GLE vs X5 is the headline flip

Every owner who named both and picked a comfort winner picked the Mercedes:

- “The GLE is a dramatically smoother ride and is my choice for a road trip.”
- “Mercedes is larger and more comfortable on longer trips.”
- “The X5 is more fun to drive… the Benz has… plusher and smoother drive for road trips.”
- “GLE is better for road-trips ngl and the x5 better to daily.”
- “I do miss the merc seats… Felt the Benz seats were buttery and plush.”

The default fit still parks X5 near Aviator because testers on `r/whatcarshouldIbuy` and `r/BMWX5` keep handing it same-day wins. Owners who actually swapped or ran both do not. **If the question is “which one after 10,000 miles,” use this file, not the composite θ for X5.**

Two owned-both Q7 households said the same thing vs X5: Audi smoother and quieter with air; one switcher wanted the Q7 seats back.

### Ascent was a test-drive nameplate

Default Ascent is 22–9, global rank 24, θ next to GLE. Owners: **6–6**, rank 44, and **1–3 inside the three-row set**.

What owners actually said:

- Pilot vs Ascent: “her Pilot is more comfortable to drive and the seats feel better.” Another household: FIL’s Pilot “feels nicer, is smoother.”
- Outback vs Ascent is still split (3–2 Ascent among owners). Two households said the Outback rides better; two use the Ascent for long trips.

The 16–3 tester pile is “I drove Palisade / Telluride / Highlander / Ascent today.” That is a real first-hand vote. It is not ownership. Drop it and Ascent is a mid-pack three-row, not a comfort pick.

### Palisade and Telluride both look better without testers

Palisade is **18–7** among owners. Still beats Pilot on ride (“drives much smoother and is very quite”; Cars.com “Rides better than our Honda Pilot”). Split with Ascent 1–1. An Enclave household gave Palisade the seats and the Buick the smoother ride.

Telluride is **9–3**. That is not “beat Palisade.” It is beat Explorer (several owned-both), Sorento, Pathfinder, and split Pilot. Testers left it 8–13 because they kept matching it to Palisade. Owners who bought a Telluride after an Explorer are not the same population.

Pathfinder vs Pilot is **4–0 owned-both**. “pathfinders seats are super comfortable especially compared to the Honda Pilot.” Palisade still beats Pathfinder 2–0 on ride.

### Compact luxury: XC60 stays; Q5 and GV70 shrink

Owner compact-luxury order (within-segment pairs): **Venza / 2026 Outback / XC60 / GLC / Nautilus > CR-V ≈ 2020–25 Outback > Q5 > CX-5 > CX-50 / X3 / Forester / RAV4**.

- **XC60 is 9–2.** One owned-both vs Q5: “I found the seats of the xc60 way nicer than the q5. I don’t think they compare at all.”
- **Q5 is 4–4.** Testers were 8–2, including a 4–0 vs XC60 on air. Those loops are gone.
- **GV70 is 2–0** (Macan / Q5, same shopper). Do not read the default 9–0 as an owner result.
- **Nautilus 4–1** and **GLC 4–2** survive.
- **Venza 4–1**, including three CR-V losses for Honda: “seats and road noise are a world of difference”; “The seat comfort is PHENOMENAL.”

### Compact wagons and trucks do not flip

These owner records are the same story as the composite, just cleaner:

- **2026 Outback 7–0.** “'26 Limited is definitely quieter and smoother” than a ’20 Premium; 2019 Limited → 2026 Touring “much quieter.”
- **2020–25 Outback 14–11.** Beats RAV4 3–0 and Forester 4–0. Splits CR-V 4–3.
- **RAV4 0–12. Forester 0–6. CX-50 1–7. X3 0–7.**
- **GX 460 vs 4Runner 7–0** owned-both: “softer / quieter / smoother”; same-garage 2023 GX + 2023 TRD Pro; three Limited 4Runners → GX460. **4Runner is 0–15 among owners.**
- **GX 550 vs 4Runner 4–0** owners (testers were 1–1).
- **GX vs RX is still a split (4–5).** Unibody RX is usually smoother; some GX households prefer isolation / less road noise. Not an X5.

### Flagship is thinner, not different

- **Range Rover 6–1.** Still the ceiling vs RX / GLE / X5 / Q8 / RRS. The one loss is an X7 owner who drove several RRs and did not hear less noise.
- **GLS 3–0** (two vs X7, one vs X5). Same Mercedes-plush note as testers, fewer votes.
- **Escalade 8–4.** Ride over Navigator in same-garage notes (“Escalade was leagues above in ride quality”; 2025 Navigator owner vs wife’s 2024 Escalade). Navigator still wins some seats.
- **iX 5–0.** Quieter / smoother than X5 for people who owned or loaned both.
- **Aviator 6–2.** Still comfort-first vs X5. Not undefeated.

Yukon 3–0 and Enclave 1–0 are too thin to put above Range Rover.

## Ranks that move (core nameplates)

Global rank among every model that appears in that fit. Sparse 1-appearance cars sit in the file, so “rank 25 Palisade” is not “25th among shoppers.”

| Model | Default W–L | Owner W–L | Both W–L | Def rank | Owner rank | owned_both rank |
|---|---:|---:|---:|---:|---:|---:|
| Range Rover | 8–1 | 6–1 | 2–0 | 3 | 2 | 1 |
| Mercedes GLS | 9–1 | 3–0 | 2–0 | 1 | 1 | 4 |
| Mercedes GLE | 12–14 | **10–4** | 10–2 | 22 | **9** | 5 |
| BMW X5 | 21–29 | 11–18 | 6–14 | 9 | 17 | 26 |
| BMW iX | 8–1 | 5–0 | 4–0 | 6 | 3 | 6 |
| Audi Q7 | 8–6 | 4–2 | 4–2 | 25 | 13 | 14 |
| Lincoln Aviator | 13–3 | 6–2 | 3–1 | 8 | 14 | 12 |
| Lexus RX | 18–16 | 16–11 | 11–6 | 39 | 34 | 20 |
| Genesis GV70 | 9–0 | 2–0 | — | 4 | 18 | — |
| Subaru Ascent | 22–9 | **6–6** | 6–4 | 20 | **44** | 28 |
| Hyundai Palisade | 42–16 | 17–5 | 13–2 | 47 | 25 | 8 |
| Kia Telluride | 17–16 | **9–3** | 7–1 | 49 | **24** | 11 |
| Honda Pilot | 19–29 | 8–11 | 5–9 | 40 | 41 | 31 |
| Nissan Pathfinder | 10–5 | 5–3 | 5–3 | 41 | 36 | 16 |
| Volvo XC60 | 15–13 | **9–2** | 6–2 | 32 | 26 | 21 |
| Audi Q5 | 12–6 | 4–4 | 1–3 | 24 | 47 | 48 |
| Subaru Outback 2026 | 10–1 | 7–0 | 3–0 | 27 | 15 | 7 |
| Subaru Outback | 19–15 | 14–11 | 11–9 | 53 | 46 | 33 |
| Honda CR-V | 20–14 | 10–10 | 6–5 | 42 | 48 | 38 |
| Lexus GX | 16–11 | 14–10 | 11–6 | 29 | 31 | 24 |
| Toyota 4Runner | 1–17 | 0–15 | 0–13 | 73 | 72 | 67 |
| Toyota RAV4 | 0–16 | 0–12 | 0–7 | 75 | 70 | 66 |

Palisade’s owner θ is less depressed than the default (−0.76 → +0.72) because it is no longer drowning in a huge tester graph of other three-rows. It still did not meet a Range Rover.

## Bias this cut does not fix

Owners are not a cleaner census. They are a different bias.

1. **Switcher justification.** People who sold an X5 for a GLE, or a Pilot for a Palisade, tend to say the new one is more comfortable. Testers do not have that sunk cost. The GLE 5–0 and Palisade 17–5 should be read with that in mind. Lived-with-both is the best evidence in the file. It is also the most post-hoc.
2. **Home-team rate is about the same.** 97 / 249 owner rows are `home_team=1` (39%). Testers are 81 / 194 (42%). Dropping testers does not drop brand-sub cooking. Ascent’s tester pile was the extreme case; GX-vs-4Runner owner notes still live on `r/LexusGX`.
3. **Edmunds / Cars.com are more owner than tester** (39 vs 16). That is why Palisade / Pathfinder / Venza look a little cleaner here. Luxury pairs are still mostly Reddit.
4. **Luxury testers filled holes owners do not.** GV70, GV80, Grand Highlander, Cayenne, Q8, and most X7–GLS volume are tester-heavy. This cut is stronger on family / compact / GX and weaker on compact-luxury shootouts.

## How to use this next to the composite

The composite chain is still the shopping document if you want every first-hand sit. Use this file for one question: **do people who lived with the cars agree with the people who drove them on Saturday?**

- Flagship ceiling: yes — Range Rover / GLS.
- GLE vs X5: **no** — owners pick GLE; testers pick X5.
- Ascent as a comfort default: **no** — that was testers.
- Palisade in the three-row set: yes.
- Telluride as plywood: **no** — testers vs Palisade said that; owners vs Explorer / Sorento did not.
- Pathfinder seats vs Pilot: yes, and it is owned-both.
- XC60 seats vs Q5 air: **owners keep XC60**; testers kept Q5.
- GV70 9–0: not an owner result.
- 2026 Outback quieter than 2020–25: yes, same-garage.
- GX 460 over 4Runner: yes, almost all owned-both.
- RX vs GX: still a split.
- RAV4 / Forester / X3 / 4Runner at the bottom: yes.

Lived-with-both only (170 votes) agrees with the owner cut on GLE, Palisade, Telluride, Pathfinder, GX, 2026 Outback, and the compact losers. It is too thin to rank GLS vs Range Rover or to keep GV70 in the table.
