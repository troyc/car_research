# Composite SUV comfort ranking from customer comparisons

**Collected 18 August 2026; expanded twice the same day** — first Edmunds/Cars.com and three-row family SUVs, then a pass aimed at **2020–2025 / 2026 Subaru Outback** (2026 is a new generation), **Subaru Ascent**, **2020–2022 Lexus RX / RX L**, and **2014–2023 Lexus GX 460**. A second Bradley–Terry fit down-weights Reddit karma and brand-sub home cooking: [`bias_analysis.md`](bias_analysis.md).

Only comments that name two or more SUVs and pick a winner on comfort (ride, seats, quiet, long-trip fatigue). Isolated praise is not used.

**297 weighted pairwise votes** from Reddit owner/test-drive threads, two X posts, plus Edmunds and Cars.com consumer reviews. Combined with a Bradley–Terry model. Method: [`methodology.md`](methodology.md). Raw votes: [`../data/comparisons.csv`](../data/comparisons.csv).

---

## The composite chain

People almost never rank ten SUVs at once. They say “A over B.” Stack those statements and this is the order that falls out:

**Range Rover (full-size) > Range Rover Sport ≈ Escalade / GLS / X7 ≈ Navigator > Lincoln Aviator / Volvo XC90 / Mercedes GLE / Audi Q7 / Acura MDX / Genesis GV80 > BMW X5 ≈ Lexus RX > Audi Q5 / Mercedes GLC / Volvo XC60 / Lincoln Nautilus / Genesis GV70 > Hyundai Palisade ≥ Subaru Ascent (ride) ≥ 2026 Outback (vs the old wagon) > Honda Pilot / Kia Telluride / Toyota Highlander / Toyota Grand Highlander / Mazda CX-90 > Honda CR-V ≈ 2020–25 Subaru Outback > Toyota RAV4 / Mazda CX-5 / Mazda CX-50 / Tesla Model Y / Toyota 4Runner / Subaru Forester**

**GX 460** sits off that ladder on purpose: it beats **4Runner** on ride/NVH/seats, splits with **RX**, and still loses to **X5 / X7 / GLE**. It is a comfortable 4Runner, not a soft-roader X5.

Read that as “generally preferred,” not “always preferred.” Spec matters: air suspension and 19-inch wheels move a nameplate a full tier; 22-inch wheels and sport packs drop it a tier.

### Why this is not a single numeric list

The mechanical Bradley–Terry fit still inflates cars that only played (and beat) weaker or same-class rivals. **GV70** is 2–0 and sits near the raw global top because it only beat Q5 / XC60. **GLS** and **LX** jump because GLS went 5–1 against X7 / Navigator and LX once beat GLS — that is not evidence they beat a full-size Range Rover. **Ascent** is 22–9 and **2026 Outback** is 10–1 for the same reason: they beat Palisade / Telluride / old Outback / Forester / 4Runner, not a Range Rover. **Palisade** is 38–16 because it crushed Pilot / Telluride / Highlander / Grand Highlander, plus one Cars.com owner who preferred it to a previous Nautilus and Aviator. That last pair is a single owner, not a class result. The chain above respects who actually met whom.

---

## Tier picture

| Tier | What customers meant | Models |
|---|---|---|
| 1. Magic carpet | Isolated, quiet, not tired after 5+ hours | **Range Rover**; then Range Rover Sport, Escalade, GLS, X7 air |
| 2. Comfort-first luxury | Soft or ergonomic, still a daily SUV | **Aviator**, **XC90**, **GLE** (road-trip vote), **Q7** (quiet), GV80 |
| 3. Dual-purpose luxury | Comfortable enough; some road feel on purpose | **X5**, **RX**, Q8, Cayenne *with air*, Model X (ride) |
| 4. Compact luxury / near-luxury | Big step up from RAV4; not a Range Rover | **Q5 (air)**, **GLC**, **XC60** (19s), **Nautilus**, **GV70**, Venza |
| 5. Mainstream three-row / comfortable | Fine all-day if you pick the right one | **Palisade**, Ascent (ride pick), **2026 Outback** (quieter than 2020–25), Highlander, Pilot, CR-V, **2020–25 Outback** |
| 6. Firm / fatiguing | Repeatedly lose long-drive comparisons | **Telluride** (ride vs Palisade), **Grand Highlander** (stiffer than Palisade in owned-both), **RAV4**, **CX-5**, **CX-50**, **Model Y**, NX, **4Runner**, Forester, XT5. **GX 460** is the comfortable truck in this neighborhood — it beats 4Runner and is not an X5. |

---

## What this expansion changed

The first pass had almost no Palisade–Highlander–Pilot matches and left Aviator / GLS / Escalade / Nautilus / Q7 on two or three votes. The second pass filled those holes. The ceiling did not move. The middle of the family class, and a few luxury pairs, did.

1. **Palisade is the comfort default in the $40–55k three-row set**, not an undefeated one. It still beats Pilot / Telluride / Highlander / CX-90 more often than not. Counters exist: one shopper’s sciatica liked Pilot seats, tall drivers (6'3"+) sometimes fit GH or CX-90 better, and a few same-day loops gave **Ascent** a slight ride edge while still calling Palisade quietest.
2. **Grand Highlander is usually the stiffer Toyota.** A household that owns both a Palisade Limited and a GH Hybrid Limited: “The Palisade is a great ride… The GHHL is a stiffer ride.” GH still wins some tall-driver front seats and one high-effort “ride quality / noise-reducing glass” shopper.
3. **Aviator is no longer undefeated** (9–3). Same-garage Aviator vs X5 still favors the Lincoln as the people-hauler; a week in a rental X5 went the other way on NVH. A 2020 back-to-back also put Aviator over XC90 on seats and silence.
4. **Escalade vs Navigator is ride vs chairs.** Multiple first-hand notes: Escalade air is “king” over bumps; Navigator massage seats win; one 2025 Navigator owner called his own ride “horrendous” next to his wife’s 2024 Escalade. GLS still beats Navigator on smoothness.
5. **Q7 beats X5 on plushness when both have air.** Two owned-both households: “The Audi is smoother by design and quieter”; another switched X5←Q7 and wanted the Audi back for long-drive seats. Q7 still loses seats to XC90 and lost one high-upvote test-drive to Q8.
6. **Cayenne with air can win.** First coded Cayenne victory: air + PASM vs an air X5 the tester called “stiff as a board.” Base Cayenne still loses.
7. **Q5 is no longer 4–0.** GV70 beat it on seats (and one tester ranked GV70 over XC60 too). GLC picked up two more X3 wins, including an owned-both “way more smoothly and quietly.”
8. **Edmunds owner reviews added compact-class texture.** An RX 350 owner who traded a 2018 XC60 called the Lexus “quieter, smoother, and much more comfortable.” A Palisade Hybrid household did the same 2.5-hour trip in a CR-V Touring and came back “refreshed rather than stiff.” A 2026 CX-5 owner is the first coded Mazda win: “much better ride and quieter than my 2024 RAV4.” CX-50 finally won one (seats vs CX-5) and still lost another. An NX 450h+ owner said it drove smoother and quieter than their 2021 RX 350 — the first NX-over-RX ride vote.

---

## What the Outback / Ascent / RX / GX pass changed

This pass added first-hand votes (297 weighted rows, up from 214) and split **2026 Outback** off the 2020–2025 wagon. Same inclusion rules. Same-author restatements of the same pair were not added twice; different authors on one thread who named the same pair were kept. Four research subagents pulled extra Outback / Ascent / RX / GX threads; those were de-duped against the existing file before coding.

### 2020–2025 Outback is the comfortable compact wagon; it is not quiet luxury

Outback went from **4–2** to **19–15**. The new wins are almost all vs **RAV4** and **Forester**:

- Owned both (2019 RAV4 Limited → 2025 Outback): “The Outback is a more comfortable ride… The RAV handles like a small truck, louder and more stiff.”
- Same-day 2020 Outback vs 2019 RAV4 LE: “the outback felt substantially better… it drove smoother.”
- RAV4-hybrid owner who has driven current Outbacks: “The Outback's cabin is quieter than the RAV4 hybrid at highway speeds.”
- Owned both Forester and Outback: “Smoother ride, quieter”; another: “SO much quieter”; a third loves the Outback on long trips.

CR-V vs Outback is a real split, not a one-off. A household with a **2025 Outback Onyx** and a **2026 CR-V Hybrid Touring** called the Honda “smoother, quicker, quieter.” Other owned-both notes go the other way: 2024 Outback quieter than a 2020 CR-V; 2025 Touring XT seats and NVH over a 2024 CR-V Hybrid; a 2024 same-day loop split the cars (CR-V smoother ride, Outback better seats). One r/CX5 same-day test called a 2024 CX-5 “MUCH quieter” than a 2024 Outback. Raw θ stays low because Outback plays in the compact graph.

### 2026 Outback is a different car — coded separately

**Subaru Outback 2026** is **10–1**. 2026 is a new generation (more upright crossover, not the 6th-gen wagon). Owners who had both:

- 2020 Premium → 2026 Limited: “definitely quieter and smoother.”
- 2019 Limited → 2026 Touring: “much quieter.”

A 6'3" Forester lessee who test-drove a 2026 agreed on ride/NVH (“quieter cabin, smoother ride”) and still kept the Forester for visibility. Extra 2026 notes: seats better than a 2025 Limited; quieter than a 2023 Touring XT and than a household Ascent; a multi-car shop gave **CR-V the smoother ride** and **2026 Outback the lounge seat**. **10–1 is not Nautilus/Q5.** It is “quieter than the wagon it replaced.”

### Ascent is a real three-row ride pick — and still not a flagship

Ascent went from **4–1** to **22–9**. New same-day / owned-both notes:

- After Palisade, Telluride, and Highlander: “The driving felt smoother and quieter to me than the 3 others.”
- Another loop: Telluride “drove like absolute garbage”; Palisade CPO “drove just like the telluride”; Pilot “felt more like a body on frame SUV.”
- vs Outback and Forester at 70 mph: Ascent “roughly 5dB quieter”; “suspension is softest.”
- Owned both Outback then Ascent: “sooo smooth and comfortable.”
- Contra (Ascent-sub shopper who drove the set): “The Telluride is so very nice, much quieter than the Ascent.”
- Owned both Palisade and Ascent: Palisade “more comfortable for longer road trips”; another household preferred Ascent seats (tall driver, back injury).
- Owned both Pilot Elite and Ascent: “her Pilot is more comfortable to drive and the seats feel better.”
- Outback vs Ascent is split: two owned-both notes say the Outback rides better; two say the Ascent is the long-trip / smoother car.

Raw θ still parks Ascent near MDX. That is the same graph artifact as before — Ascent beat Palisade / Telluride / Pilot / Outback / Forester, not a GLS. The composite chain keeps it in the family class. The [bias fit](bias_analysis.md) **does** demote Ascent once home-team and karma are stripped (22–9 stays; global rank falls). Palisade rises in that fit. `no_home` is the check that Ascent’s sample is still brand-sub heavy.

### 2020–2022 RX / RX L: Highlander step-up; GX is a split

New first-hand 2020–22 notes, not mixed into 2023+ on purpose in the quote:

- 2018 Highlander → 2020 RX: “smoother to drive.”
- 2023 Highlander XLE turbo-4 → CPO 2022 RX350: “such a smoother ride. Quieter cabin… so comfortable.”

**RX vs GX 460** is no longer empty. Same-garage and family notes split the way body-on-frame vs unibody should:

- RX 450hL + GX household: “The unibody RX is much much smoother… The GX rides like a truck.”
- Sibling RX350 vs own GX: “The rx is a much smoother drive.”
- 2021 RX 350 → 2023 GX 460: “I enjoy the ride of the GX 460 better… smoother… more comfortable” on long trips.
- Owned both: GX “more comfortable for day to day use due to road noise.”

RX is now **18–14** (32 appearances). Still dual-purpose luxury. Extra 2020–22 notes: owned-both 2021 RX quieter and less fatiguing than a 2021 RAV4 on long trips; Edmunds 2021 RX 350 quieter/smoother than a 2016 Q5; one same-day loop called a base RX “easily the most jarring ride” next to an air XC90. Not XC90 chairs, not Range Rover isolation.

### GX 460 is no longer 0–3 — it beat the 4Runner, not the Germans

GX went from **0–3** (GLE / X5 / X7) to **15–11**. The new wins are almost all vs **4Runner**, including people who own both:

- “Softer ride, quieter ride, smoother ride.”
- 2023 GX + 2023 4Runner TRD Pro in the same garage: “The GX is quieter.”
- 17 TRD Pro → 23 GX: “rides so quiet and smooth.”
- Three Limited 4Runners → 21 GX460: “ride, comfort, noise level… leaps ahead.”
- Edmunds owner: “smoother and quiet overall” vs the 4Runner.

**Read that carefully.** GX beating 4Runner is not GX beating X5. The old losses (GLE, X5, X7) are still in the file. New texture: GX quieter than a TX 350 (TX wins seats); **LX 570** still beats GX on ride; two first-hand notes say **GX 460 rides smoother and quieter than GX 550**. The bias fit keeps the same story and shaves a little off GX because so many of those 4Runner notes live on `r/LexusGX`.

---

## Evidence that actually moves the ranking

### Range Rover is still the ceiling

Full-size Range Rover remains **6–0**. Nothing in the new batch put another nameplate next to it and won.

### Flagship is a three-way, not Escalade by default

New first-hand votes:

| Winner | Loser | Axis | Typical language |
|---|---|---|---|
| GLS | X7 | ride / seats | “smoother and more refined”; “Seat comfort: GLS”; “X7 feels a bit connected to the road” |
| X7 | Escalade | ride / 2nd-row | household that left a 2021 Escalade: “ride smoother than the Caddy… kids more comfortable in the second row” |
| Escalade | X7 | isolation | “a cloud by comparison. More isolation, less feel” |
| Escalade | Model X | seats / space | “way more comfortable and roomy”; “seats… more comfortable for longer road trips” |
| Model X | Escalade | ride | “The Tesla is a smoother ride” |
| Escalade | Navigator | ride | “air suspension is king”; “leagues above in ride quality”; one 2025 Nav owner vs wife’s Escalade |
| Navigator | Escalade | seats | “massage function… more comfortable than the latest Escalade seats”; one same-day “Navigator was the most comfortable” |
| GLS | Navigator | ride | shopper who bought a Navigator still said GLS was smoother |

Escalade still wins the American-cloud brief, especially vs Navigator on bumps. Navigator wins some seat comparisons. X7 wins when the same family wants less boat. GLS wins the Mercedes version of isolation. Range Rover still sits above all of them in the older owned-both notes.

### Aviator vs the Germans is now a real sample

Aviator went from **3–0** to **7–2**.

- Owned / regularly driven both: “The aviator is just flat out comfortable… much more passenger hauler friendly than the x5.” Another household with a 2025 X5 and 2026 Aviator: “The Aviator is smoother while the X5 is sportier.”
- Contra: Aviator PHEV owner after a week in a rental X5 — “coil spring suspension on X5 rides better than Aviator air ride… a lot quieter.”
- vs X7: one tester “X7 ride was a hair smoother”; another household “couldn’t get comfortable in the X7’s we tried” and also found Lexus TX seat comfort “poor” without even driving it.

So Aviator stays in the comfort-first luxury tier. It is no longer an undefeated artifact. One 2020 tester who wanted an XC90 bought the Aviator instead: “more comfortable than any of the other cars we tested… smoothest ride of them all.”

### Q7 is the quiet midsize; XC90 is still the chair

New owned-both / switcher notes put **Q7 over XC90 on NVH** (“much quieter,” “more squeaks in the XC90”) and **XC90 over Q7 on third-row seats**. Two households that ran **Q7 and X5 with air** picked the Audi as smoother and better on long-drive seats. That is the same split the first pass found between XC90 and X7: Volvo wins furniture, the other Germans win silence — except Q7 now has a real X5 ride win.

**MDX Type S** showed up as a comfort alternative to X5 (massage / adjustable suspension) and a smoother ride than an older XC90. One six-SUV test still put X5 over MDX on bump absorption.

**Cayenne** is no longer 0–fer. Air + PASM beat an air X5 one tester called “stiff as a board.” Without air it is still “too sporty / you feel the road.”

### Compact luxury: Nautilus vs XC60 is split, like Q5 vs XC60

- Testers who wanted a *crisp* ride: “Volvo was superior in comfort, ride… Nautilus felt floaty.”
- Testers who wanted *seat theater*: “nautilus has a better and more comfortable seat… massage and heat/cool is far more intense.”
- One back-to-back of Nautilus and RX: Lincoln “more comfortable and quiet inside,” with the usual reliability caveat attached.

Nautilus is now 4–1, not 2–0. It belongs with Q5 / GLC / XC60, not with Aviator.

### Three-row family is no longer a footnote

This was the thin spot. It is not thin anymore.

**Within-class (pairs only):** Palisade is still the volume winner (30–9 in-segment). Ascent is 4–1 on *ride* in a few same-day loops. Then Telluride / Pilot / Grand Highlander / Highlander cluster below.

What the comments actually said:

| Winner | Loser | Why |
|---|---|---|
| Palisade | Pilot | “plywood with leather covering”; owned-both “drives much smoother and is very quite”; 4-day rental “smoother ride”; Cars.com “rides better than our Honda Pilot” |
| Pilot | Palisade | sciatica “twanging” in Palisade, not Pilot — a real long-trip seat counter |
| Palisade | Telluride | ride again, plus seats “too firm”; Cars.com “far superior and drove much smoother” |
| Palisade | Highlander | owned both Platinum trims (2020 Palisade / 2023 Highlander): “Palisade ride is alot smoother”; testers: Highlander “bumpy” / “noisy… a chore on the highway” |
| Highlander | Palisade (2021) | Pilot + Highlander owner who test-drove a 2021 Palisade: “Loud… uncomfortable seating position” |
| Palisade | Grand Highlander | owned both: “GHHL is a stiffer ride”; third row “comfy” vs GH “uncomfortable”; bump absorption |
| Grand Highlander | Palisade | 6'3"+ front-seat fit; one shopper’s “ride quality, noise-reducing glass” |
| Palisade | CX-90 | owner of both: “takes bumps like dogshit”; other testers: Palisade more comfortable for family trips |
| CX-90 | Palisade | 6'3" driver: Calligraphy seat “super high on the lowest setting” |
| Ascent | Palisade / Telluride / GH | “liked the ride on that the best”; another loop “slight edge to Ascent” on ride, Palisade still “quietest” |
| Palisade | Ascent | “didn’t find the Ascent as comfortable” |
| Palisade | Atlas | bought Palisade “because how smooth the ride is” |
| Telluride | Highlander / Explorer | “not as comfortable as the Telluride”; 4-hour trip “ride was smoother” |
| Pilot | Highlander (2025 vs 2021) | newer Pilot “quieter… less wind noise” |
| Highlander | Pilot (older pair) | owned both: “Highlander is smoother” |
| Highlander | RAV4 | owned both: Highlander “quieter than the Rav 4” |
| CR-V Hybrid | RAV4 Hybrid | traded 2021 RAV4 Hybrid: CR-V “very quiet” |

**Read that carefully.** Palisade winning this class is not Palisade beating an X5. Cross-class votes still have RX / Navigator / Escalade / Range Rover above it. One Cars.com Palisade Hybrid owner called a 2023 Nautilus Black Label “rough and noisy.” That is a single owner, not a reason to shop Palisade as compact luxury.

Regular **Highlander** loses more ride/NVH comparisons than the first pass showed, but it still beats RAV4 and some older Palisades/Pilots. **Grand Highlander** is the stiff/cargo Toyota: better for tall front-seat fit and luggage, worse for plushness. **Ascent** is the ride specialist a few shoppers left the Korean set for. **CX-90** is still the sporty one families stop using for trips, unless the driver is tall and hated the Palisade seat height.

### Compact mainstream: RAV4 is now 0–8; CX-5 finally won one

XC60 over RAV4 is still the strongest repeated switch. New owned-both notes add **CR-V Hybrid quieter than RAV4 Hybrid**, **Highlander quieter than RAV4**, and **CX-5 quieter/smoother than a 2024 RAV4** — Mazda’s first coded win, and it is still only vs RAV4. CR-V vs Outback is still split (Edmunds added another Outback-over-CR-V ride note). CX-50 is 1–6: one owner prefers its front seats to a CX-5, another calls CX-50 seats a “total miss from the cx5” on any trip over an hour. **Venza vs Highlander is split** (one owner traded a stiff Venza for a smoother Highlander Hybrid; another found the current Highlander “extremely noisy” and bought a Venza). GLC is 4–0 after two more X3 losses. Q5’s first loss is to GV70 seats, not to a mainstream compact. An **RX owner who came from XC60** called the Lexus quieter and smoother — that sits next to the older thin “Volvo is another spectrum” opinion and is the stronger evidence.

---

## Mechanical ranking (for the record)

Core models with **three or more** coded appearances, Bradley–Terry θ, and win–loss (default fit):

| Rank | Model | θ | W–L |
|---:|---|---:|---:|
| 1 | Range Rover | 6.08 | 6–0 |
| 2 | Lexus LX | 4.85 | 4–1 |
| 3 | Mercedes GLS | 4.69 | 5–1 |
| 4 | Range Rover Sport | 4.00 | 8–1 |
| 5 | Lincoln Aviator | 2.57 | 10–3 |
| 6 | Genesis GV80 | 2.54 | 4–2 |
| 7 | BMW X7 | 2.51 | 5–7 |
| 8 | Mercedes GLC | 2.50 | 4–0 |
| 9 | Cadillac Escalade | 2.35 | 9–5 |
| 10 | BMW X5 | 2.15 | 15–21 |
| 11 | Lincoln Navigator | 2.03 | 4–6 |
| 12 | Acura MDX | 1.42 | 4–1 |
| 13 | Subaru Ascent | 1.34 | 22–9 |
| 14 | Audi Q5 | 1.31 | 4–2 |
| 15 | Lincoln Nautilus | 0.99 | 5–2 |
| 16 | Mercedes GLE | 0.63 | 7–12 |
| 17 | Subaru Outback 2026 | 0.47 | 10–1 |
| 18 | Lexus GX | 0.44 | 15–11 |
| 19 | Audi Q7 | 0.42 | 6–5 |
| 20 | Volvo XC90 | 0.11 | 11–10 |
| 21 | Lexus RX | 0.02 | 18–14 |
| 22 | Volvo XC60 | −0.36 | 9–11 |
| 23 | Honda CR-V | −0.56 | 10–12 |
| 24 | Toyota Grand Highlander | −0.76 | 4–8 |
| 25 | Hyundai Palisade | −0.98 | 38–16 |
| 26 | Honda Pilot | −1.04 | 7–13 |
| 27 | Kia Telluride | −1.33 | 5–12 |
| 28 | Toyota Highlander | −1.69 | 5–14 |
| 29 | Subaru Outback (2020–25) | −1.93 | 19–15 |
| 30 | BMW X3 | −2.95 | 0–5 |
| 31 | Mazda CX-5 | −2.96 | 3–4 |
| 32 | Mazda CX-50 | −3.34 | 1–6 |
| 33 | Toyota 4Runner | −3.63 | 0–9 |
| 34 | Subaru Forester | −5.07 | 0–8 |
| 35 | Toyota RAV4 | −5.17 | 0–15 |

GLS’s 5–1 is almost all vs X7 / Navigator on *plushness*. That is a real within-flagship result. It is not a global claim over Range Rover.

Palisade’s 36–15 still looks huge until you see the losers. The new Ascent and Outback rows did not move Palisade into luxury.

Ascent’s **22–9** and raw θ near MDX is still a **ride** cluster against Palisade / Telluride / Pilot / Outback / Forester. Do not shop Ascent as a flagship.

**2026 Outback** at 0.47 / 10–1 is the same kind of artifact as GV70: it mostly beat the old Outback, Forester, CX-50, a 4Runner, and one Ascent.

**GX** at 0.44 / 15–11 is the first time the truck has a real sample. Those wins are 4Runner, a TX NVH note, and a split with RX. The Germans and LX still beat it. GX 550 is 0–2 vs the 460.

The [bias-adjusted table](bias_analysis.md) shrinks luxury θ and **does** pull Ascent down once home-team / karma are stripped. Palisade rises. RX and 2020–25 Outback stay in the same neighborhood. That is the point of the second fit.

---

## Within-class order (safer for shopping)

**Compact / small-mid**  
Audi Q5 (air) ≈ Mercedes GLC ≈ Lincoln Nautilus ≈ Genesis GV70 (seats) ≈ Toyota Venza > Volvo XC60 (seats; ride depends on wheels; beat Nautilus for some testers) > **2026 Outback** (quieter/smoother than 2020–25 per owners who had both) > Honda CR-V ≈ **2020–25 Outback** ≈ VW Tiguan > Mazda CX-5 > Toyota RAV4 ≈ Mazda CX-50 ≈ Forester. CR-V vs 2020–25 Outback is split; one same-garage 2026 CR-V Hybrid beat a 2025 Outback on smoothness and quiet.

**Midsize luxury**  
Range Rover Sport ≈ Lincoln Aviator > Volvo XC90 ≈ Mercedes GLE (plush) ≈ Audi Q7 (quiet / long-trip vs X5 air) ≈ Genesis GV80 ≈ Acura MDX Type S (seats) > BMW X5 ≈ Lexus RX (2020–22 beats Highlander; splits with GX 460) > Audi Q8 ≈ Porsche Cayenne *with air* > Cayenne without air > **GX 460** (comfortable 4Runner; loses to X5 / X7 / GLE) > **4Runner**

**Flagship / large**  
Range Rover > Escalade (ride vs Navigator) ≈ GLS ≈ X7 air ≈ Navigator (seats vs Escalade) > Lexus LX (truckier than Escalade)

**Three-row family**  
Palisade ≥ Ascent (ride loops; seats and quiet often go the other way) ≥ Highlander > Pilot ≈ Telluride > Grand Highlander ≈ CX-90. Palisade is the comfort default. Ascent is the ride specialist a few shoppers picked after driving the Koreans — and after an Outback. Owned-both counters now exist (Pilot seats, Palisade long-trip, Outback ride). Highlander is the Toyota-faithful counter and still quieter than RAV4; it loses ride to a 2020–22 RX. Grand Highlander wins cargo and some tall front seats, not plushness. CX-90 is the sporty one people stop using for family trips unless they hated Palisade seat height.

---

## What “comfort” split on

Customers were not talking about one thing:

1. **Isolation / magic carpet** — Range Rover, GLE, GLS, Escalade, Navigator, X7 air, Model X air. Soft, quiet, disconnected.
2. **Seats as furniture** — Volvo (ergonomic, firm, all-day), Lincoln (plush, many-way, stronger massage than Volvo), Mercedes massage. Palisade beats Pilot/GH/CX-90 here in the family class. Toyota/RAV4/Pilot rear seats called hard or “plywood.”
3. **Not tired after 400 miles** — sometimes the firmer, more supportive chair (X5 multi-contour, Volvo) beats the softer one that lets you slouch.
4. **Wheel and tire** — still the most repeated piece of advice that is *not* a nameplate effect.

If you only care about (1), buy air suspension and the smallest legal wheels. If you only care about (2), sit in a Volvo and a Lincoln before you sit in anything else — and if the budget is family-three-row, sit in a Palisade before a Pilot or Grand Highlander.

---

## Limits

- Reddit still carries most of the signal. This pass added Outback / Ascent / RX / GX threads plus one Edmunds GX-vs-4Runner owner line. Direct fetches of Edmunds/Cars.com review hubs are still often blocked; those votes are taken from indexed owner-review text. How to do that next time: [`methodology.md`](methodology.md#getting-around-blocked-review-sites).
- Brand subs still tilt GLE vs X5, Palisade vs Pilot, Ascent vs the Koreans, and GX vs 4Runner. Owned-both comments were kept at full weight; thin home-team comments stay down-weighted. The [bias-adjusted fit](bias_analysis.md) tightens that further and drops karma.
- 2020–25 Outback (19–15), 2026 Outback (10–1, still small vs luxury), Ascent (22–9), RX (18–14), and GX 460 (15–11) are no longer sparse. 2026 Outback and Ascent raw θ are still “beat weaker or same-class rivals” artifacts.
- One 241-upvote six-SUV test-drive write-up still moves Q8 / MDX / Q7 / Cayenne more than any other single source. The bias fit ignores its upvote count.
- Palisade > Nautilus and Palisade > Aviator are single Cars.com owners. They are coded. They do not move Palisade into the luxury shopping list.
- 2026 Outback vs 2020–25 Outback is two owners. Direction is consistent (quieter/smoother). Sample is tiny.
- No China / Europe-only nameplates. No GX 550 sample.
- Comfort is not reliability. Range Rover, Palisade, and Ascent all win comfort arguments in threads that immediately warn you about service.

Re-run: `python3 src/rank.py`. Default table: `data/ranking.csv`. Bias table: `data/ranking_bias.csv`.
