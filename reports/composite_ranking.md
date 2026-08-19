# Composite SUV comfort ranking from customer comparisons

**Collected 18 August 2026; expanded nine times the same day** — Edmunds/Cars.com and three-row family SUVs; then **2020–2025 / 2026 Subaru Outback**, **Ascent**, **2020–2022 RX / RX L**, and **2014–2023 GX 460**; then thin luxury / missing three-row / trucks; then remaining thin flagship, mid-luxury, compact-luxury, three-row, and truck nodes; then Yukon / Tahoe / Suburban / QX80 / Escalade IQ, EQS SUV / Defender / R1S / Cayenne / Macan, Crosstrek / Corsair / X1 / Model Y, and CX-90 / Pathfinder / Murano / Passport; then a seventh pass on Yukon / R1S / Sequoia / QX80 / Tahoe, Defender / Cayenne / Grand Cherokee, Crosstrek / Corsair / X1 / Murano / Model Y, and CX-90 / Explorer / Enclave / GCL; then an **eighth pass** on Escalade IQ / EQS SUV / LX / Yukon / Land Cruiser, Defender / Grand Cherokee / Cayenne / R1S / Model Y, Venza / Tiguan / Corsair / X1 / Crosstrek, and leftover GCL / XT5 / Enclave owner-review lines; then a **ninth pass** on Expedition / Suburban / Tahoe / Escalade / Navigator, 2026 Santa Fe / Palisade, and fresh RR / GLS / Q7 / X5 / GV80 links. Then a full-file **audit** removed 19 unsupported rows and recoded evidence / quotes / `home_team`. A second Bradley–Terry fit down-weights brand-sub home cooking: [`bias_analysis.md`](bias_analysis.md).

Only comments that name two or more SUVs and pick a winner on comfort (ride, seats, quiet, long-trip fatigue). Isolated praise is not used.

**786 weighted pairwise votes** (790 coded rows) from Reddit owner/test-drive threads, three X posts, plus Edmunds and Cars.com consumer reviews. Combined with a Bradley–Terry model. Method: [`methodology.md`](methodology.md). Raw votes: [`../data/comparisons.csv`](../data/comparisons.csv). Owners only, testers dropped: [`owner_analysis.md`](owner_analysis.md). Audit record: [`../audit/compiled.md`](../audit/compiled.md).

---

## The composite chain

People almost never rank ten SUVs at once. They say “A over B.” Stack those statements and this is the order that falls out. Later bands are generally less comfortable. `≈` is a split; `/` is “about this neighborhood.”

| | Band | Models |
|---:|---|---|
| 1 | Magic carpet | **Range Rover** ≈ **GLS** ≈ **LX** |
| 2 | Flagship / comfort-first luxury | Range Rover Sport ≈ Escalade / Escalade IQ / Navigator / Grand Wagoneer / Yukon / X7 / BMW iX / Lincoln Aviator / EQS SUV |
| 3 | Dual-purpose luxury | Mercedes GLE / Audi Q7 / Acura MDX / Genesis GV80 / **BMW X5** ≈ **Lexus RX** / Audi Q8 |
| 4 | Compact luxury | Audi Q5 / Lincoln Nautilus / Mercedes GLC / Volvo XC60 / Genesis GV70 / Lincoln Corsair |
| 5 | Comfortable three-row / near-luxury compact | **Palisade** ≥ Ascent (ride) ≥ Pathfinder (seats vs Pilot) ≥ Telluride ≥ Atlas ≥ Expedition (split) ≥ 2026 Outback / Murano / Venza / Santa Fe |
| 6 | Mainstream three-row | Honda Pilot / Toyota Highlander / Toyota Grand Highlander / Mazda CX-90 |
| 7 | Comfortable compact | Honda CR-V ≈ 2020–25 Subaru Outback |
| 8 | Firm / fatiguing | RAV4 / CX-5 / CX-50 / BMW X3 / Crosstrek / Model Y / 4Runner / Forester / R1S / BMW X1 |

Off the main ladder (they mostly met trucks, not the band above them):

- **GX 460** beats **4Runner**, splits with **RX**, and usually loses to the Germans. One tester did prefer the 460’s ride to GLS / X5 / QX80 / MDX.
- **GX 550** usually beats **Land Cruiser** and **4Runner**; still loses to the 460 and to air **Defender**.
- **Sequoia** loses ride/NVH to **LX**, **Yukon**, **Range Rover**, and **Navigator**.
- **Tahoe** beats GX 550 on air-ride, splits Sequoia, and loses to Escalade / QX80 / Grand Wagoneer / Yukon NVH.
- **Defender** loses ride/NVH to Range Rover; beats **Cayenne**, **R1S**, and **GX 550** on ride.
- **Yukon air** repeatedly beats **R1S** in same-garage notes.
- **Escalade IQ** is 6–1 vs Model X and gas Escalade — quiet EV truck, not a Range Rover.

Read that as “generally preferred,” not “always preferred.” Spec matters: air suspension and 19-inch wheels move a nameplate a full tier; 22-inch wheels and sport packs drop it a tier.

### Why this is not a single numeric list

The mechanical Bradley–Terry fit still inflates cars that only played (and beat) weaker or same-class rivals. **EQS SUV** is 9–1 vs iX / R1S and now sits #1 on raw θ — still not a Range Rover. **Escalade IQ** is 6–1 vs Model X / gas Escalade. **XT6** is 7–2 after one Edmunds shopper preferred it to an X5; do not shop XT6 as mid-luxury furniture. **CX-9** is 7–0 vs Highlander / Pilot / RAV4. **Enclave** is 7–3 vs Palisade/Telluride/TX/X5. **Yukon** is 21–5 mostly vs R1S / Sequoia / GX / Tahoe — that is a real truck sample, not Yukon-over-GLS. **GV70** is 14–4 and still has not met a Range Rover. **GLS** is 17–4 almost entirely vs X7. **iX** is 11–7 vs Model X / X5 / EQS SUV / Model Y / R1S. **Ascent** is 22–9 and **2026 Outback** is 12–1 for the same reason as before. **Palisade** is 54–22 because it crushed Pilot / Telluride / Highlander / Grand Highlander / Pathfinder / CX-90. The chain above respects who actually met whom.

---

## Tier picture

| Tier | What customers meant | Models |
|---|---|---|
| 1. Magic carpet | Isolated, quiet, not tired after 5+ hours | **Range Rover**; then Range Rover Sport, Escalade, GLS, X7 air |
| 2. Comfort-first luxury | Soft or ergonomic, still a daily SUV | **Aviator**, **XC90**, **GLE** (road-trip vote), **Q7** (quiet), GV80 |
| 3. Dual-purpose luxury | Comfortable enough; some road feel on purpose | **X5**, **RX**, Q8, Cayenne *with air*, **iX** (quiet vs Model X / X5), Model X (ride) |
| 4. Compact luxury / near-luxury | Big step up from RAV4; not a Range Rover | **GV70**, **Q5 (air)**, **Nautilus**, **GLC**, **XC60** (19s), Venza, NX |
| 5. Mainstream three-row / comfortable | Fine all-day if you pick the right one | **Palisade**, Ascent (ride), **Pathfinder** (seats vs Pilot), **Telluride** (now a split), **2026 Outback**, Pilot, Atlas, CR-V, **2020–25 Outback** |
| 6. Firm / fatiguing | Repeatedly lose long-drive comparisons | **Grand Highlander** (stiffer than Palisade), **X3** (0–15), **RAV4**, **CX-5**, **CX-50**, **Model Y**, **4Runner**, Forester, XT5, Explorer, Sorento. **GX 460** is the comfortable truck in this neighborhood — it beats 4Runner and is not an X5. **GX 550** is the same story with more road feel. |

---

## What this expansion changed

The first pass had almost no Palisade–Highlander–Pilot matches and left Aviator / GLS / Escalade / Nautilus / Q7 on two or three votes. The second pass filled those holes. The ceiling did not move. The middle of the family class, and a few luxury pairs, did.

1. **Palisade is the comfort default in the $40–55k three-row set**, not an undefeated one. It still beats Pilot / Telluride / Highlander / CX-90 more often than not. Counters exist: one shopper’s sciatica liked Pilot seats, tall drivers (6'3"+) sometimes fit GH or CX-90 better, and a few same-day loops gave **Ascent** a slight ride edge while still calling Palisade quietest.
2. **Grand Highlander is usually the stiffer Toyota.** A household that owns both a Palisade Limited and a GH Hybrid Limited: “The Palisade is a great ride… The GHHL is a stiffer ride.” GH still wins some tall-driver front seats and one high-effort “ride quality / noise-reducing glass” shopper.
3. **Aviator is no longer undefeated** (9–3). Same-garage Aviator vs X5 still favors the Lincoln as the people-hauler; a week in a rental X5 went the other way on NVH. A 2020 back-to-back also put Aviator over XC90 on seats and silence.
4. **Escalade vs Navigator is ride vs chairs.** Multiple first-hand notes: Escalade air is “king” over bumps; Navigator massage seats win; one 2025 Navigator owner called his own ride “horrendous” next to his wife’s 2024 Escalade. GLS still beats Navigator on smoothness.
5. **Q7 beats X5 on plushness when both have air.** Two owned-both households: “The Audi is smoother by design and quieter”; another switched X5←Q7 and wanted the Audi back for long-drive seats. Q7 still loses seats to XC90 and lost one test-drive to Q8.
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

Raw θ still parks Ascent near MDX. That is the same graph artifact as before — Ascent beat Palisade / Telluride / Pilot / Outback / Forester, not a GLS. The composite chain keeps it in the family class. The [bias fit](bias_analysis.md) leaves Ascent at the same global rank (22–9 stays). `no_home` is the check that Ascent’s sample is still brand-sub heavy.

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

## What the thin-nameplate / family / review-site pass changed

Five research subagents pulled unused threads (compact luxury, midsize luxury, three-row holes, flagship/trucks, Edmunds/Cars.com snippets). Coded **156** new first-hand rows after dropping India/Gulf market notes, a pre-2018 Bluetec-as-GLE, “looked at” rather than drove, and Lincoln MKX. Same inclusion rules. Same-author restatements of the same pair were not added twice.

### Compact luxury is no longer a Q5/GLC shutout

- **GV70** went from 2–0 to **9–0**. Same-day loops put it over Macan and SQ5 on ride (“more luxurious and comfortable than both”) and called X3 M40 “harsh… worst of the bunch.” That is compact-luxury furniture, not a midsize-luxury result.
- **Nautilus** is **10–2**. New wins vs X3 seats, RX quiet, and XT5 ride. Still not Aviator.
- **GLC** is no longer 4–0. NX owners preferred NX seats/quiet; a Q5 owner who rented a 2022 GLC preferred Audi seats/suspension; an Edmunds XC60 shopper ranked XC60 over GLC.
- **NX vs XC60** is a split: XC60 wins seats/ride for people who hated NX run-flats; NX wins cabin quiet for one tester.
- **CR-V vs CX-50** piled on (seats, potholes, rental). CX-50 is now **1–12**. **X3** is **0–15**.

### Midsize: GLE finally met XC90/Q7; iX is a real quiet EV

- Owned-both **GLE air > XC90** ride (“Night and day”) and **GLE air > Q7**. A Q7 tester still called the Audi quieter than GLE/X5 with air.
- **Aviator** beat GV80 on two same-day loops (“cloud”; “smoother/less bumpy”).
- **MDX** picked up X5-seat and GV80-ride notes and still lost one owned-both to X5.
- **BMW iX** is **8–1**: owned-both quieter than Model X; smoother/quieter than an X5 rental; one tester kept X5 50e for multi-contour seats. Do not read 8–1 as Range Rover class — the victims are Model X / X5 / EQS SUV.
- **X5** beat Model X and Model Y on comfort for long trips.

### Three-row: Pathfinder is in; Telluride is no longer a punching bag

This was the hole. **Nissan Pathfinder** arrives at **10–5**. Almost every new win is vs **Pilot** on seats (owned-both and same-day). Palisade still beats Pathfinder 4–0 on ride/luxury feel. Telluride crushed one Pathfinder owned-both.

**Telluride** went from **5–12** to **17–16**. New wins: Sorento (owned-both, smoother), Explorer (owned-both), CX-90 seats, Grand Cherokee L ride, and a split with Pilot (Telluride quieter/car-like; Pilot smoother/seats). That is “not Palisade, not plywood,” not a luxury result.

**Atlas** is quieter than Pilot in several same-day notes and splits Telluride (Telluride ride; Atlas NVH). **Passport vs Pilot** is seats vs highway ride. **Pilot vs Grand Highlander** added four ride/NVH wins for Pilot.

### Flagship / trucks: Range Rover’s first loss; Wagoneer is real; GX 550 vs 4Runner

- Full-size **Range Rover** is **8–1**. Two new X7 testers preferred RR ride/seats. An X7 owner who drove several RRs said they were **not quieter** — maybe more window noise. That is the first coded RR loss.
- **GLS** picked up more X7 ride/3rd-row notes (9–1). Still not evidence GLS beats Range Rover.
- **Grand Wagoneer** vs Navigator is the Escalade split again: Wagoneer ride/composure; Navigator massage seats. Rental-fleet notes put Wagoneer over Suburban and are split vs Yukon.
- **GX 550** is **6–4**. Owned-both vs 4Runner usually prefers GX comfort/seats; one 4Runner owner called Premium 550 “atrocious” vs the 4Runner. Another 460-vs-550 note: 460 still smoother. **Land Cruiser** 250 beats 4Runner on ride/NVH and loses cabin quiet to GX 550.

### Edmunds / Cars.com (no bot-wall bypass)

Owner sentences visible in search snippets added Q5-over-X3, XC60-over-GLC, GLE-over-X5, RRS-over-GLE AMG, Navigator-over-Escalade seats, Pathfinder-over-Pilot on a dirt road, Nautilus-over-Grand Cherokee quiet. Dropped anything that only said “looked at.”

---

## What the fifth pass changed

Five research subagents pulled unused threads (flagship, midsize luxury, compact luxury, three-row holes, trucks plus owner-review snippets). Coded **101** new first-hand rows after dropping a 1sk09pg/1sjoqi7 crosspost already in the file, an Aviator/GV80 crosspost, a 2014/2017 pair, a styling-only GX 550 note, RX praise with no loser, and a Palisade-is-squishy stability comment. Same inclusion rules. Different authors on one thread who named the same pair were kept.

### Flagship: GLS sample grew; EQS SUV is real; Escalade still splits

- **GLS** went from 9–1 to **17–3**. New owned-both / test-drive notes still pick it over X7 on plushness (“spastic gorilla”; “effortless at 70”). First coded losses: an Escalade tester called the Cadillac **quieter**; a GX 460 shopper preferred the Lexus ride to GLS / X5 / QX80 / MDX.
- **EQS SUV** is **3–1**. Two owned-both households picked it over **iX** on seats/smoothness (“comfort wise eqs wins”; “even smoother ride”). That is why raw θ parks EQS near Range Rover — do not shop it as a magic-carpet winner. The victims are iX / XC90, not GLS.
- **Escalade** is **13–8**. A 2022 Platinum owner who rented an X7 called the Cadillac smoother. Navigator vs Escalade is still ride vs seats.
- **LX** is **8–2**. Owned-both vs a 2023 Sequoia Hybrid: the Toyota “rode extremely rough… battery sitting on the back axle.” Sequoia still wins some passenger-seat notes vs an older LX 570 and beats Tahoe on long trips.

### Midsize: iX is no longer 8–1; R1S is 0–6; Q8 splits X5

- **iX** is **9–3**. The new losses are the EQS SUV garage notes above. It still beats X5 on seats/quiet for people who drove both.
- **Rivian R1S** is **0–6**. XC90 (owned-both, no air) “noticeably smoother”; a three-car loop put MDX Type S / GV80 / XC90 over R1S on bumps; a totaled R1S household preferred Model X for quiet and long-trip seats.
- **Defender** is **2–3**: air Defender beat GX 550; a 2023 Defender owner who bought a GX 550 still said the Rover rode better; XC90 seats won a Defender switcher.
- **Q8 vs X5** is now a real split: two owned-both notes give Q8-with-air the smoother/quieter ride; one of those same households missed X5 seats.
- **Cayenne** picked up another air + PASM win vs an X5 PHEV the tester called “rickety.”
- **TX** vs GX / Aviator: TX rides nicer than GX 550 as a loaner; Aviator still wins “couch” vs TX.

### Compact luxury: GV70 is no longer undefeated

- **GV70** went from 9–0 to **11–3**. First losses: an owned-both Nautilus household preferred Lincoln seats/ride; a tester who drove GV70 and NX picked NX for comfort; an RX household said the wife found the Lexus smoother.
- **Nautilus** is **12–3** and now has a first-hand GV70 split plus a Tiguan trade-in (“next level comfort”).
- **Corsair** beat NX on a same-day loop (NX “noisy and rode very stiff”).
- **Tiguan** is **4–4**: owned-both quieter than RAV4; seats split vs CR-V and a long-commute RAV4.
- **X3** is **1–16** (Macan ride win). **X1** is 0–3. **CX-9** is 3–0, all vs CX-50.

### Three-row: Atlas and Enclave are no longer footnotes

- **Atlas** is **10–4**. Three same-day testers on `r/VWatlas` picked it over Telluride on ride/quiet. An Atlas owner preferred its seats to Palisade.
- **Enclave** is **3–1**. Owned-both vs Palisade: Enclave smoother ride, Palisade better seats. A dB-meter shopper picked Enclave over TX.
- **Telluride** is **23–20**. More CX-90 / Sorento / 4Runner wins; Pilot still splits.
- **Passport** is **5–6**. Two owned-both notes crush a 2025 4Runner and a TRD Pro on quiet/seats.

### Trucks: GX 550 vs Land Cruiser is now a pile

- **GX 550** is **9–11**. Back-to-back and owned-both notes prefer it to 2024+ Land Cruiser on wind noise (“LC wind noise was comparable to my gladiator”). Overtrail still loses isolation to GLS. One 4Runner owner called 550 ride worse than the Toyota.
- **GX 460** is **24–12**. Another owned-both 460 > 550 ride note; Edmunds owner: 2023 GX 460 KDSS “much smoother” than a 2025 Land Cruiser.

---

## What the sixth pass changed

Five research subagents pulled unused threads (flagship trucks, mid-luxury / EV, family three-row holes, compact / compact-luxury, Edmunds/Cars.com snippets). Coded **79** new first-hand rows after dropping a 2019 Explorer (prior generation), one shopper’s “we shopped X5/Q7/GLE/XC90/MDX” exploded into four extra XT6 wins, and a Pilot-vs-GH note that was handling/body-roll. Same inclusion rules. Same-author restatements of the same pair were not added twice.

### Flagship trucks are finally in the graph

- **GMC Yukon** is **8–5**. Escalade vs Yukon is a real split: Escalade usually quieter; one Denali Ultimate tester preferred Yukon ride; an owned-both garage said Escalade road noise is better. Yukon beat similarly spec’d Suburban (MagneRide) on ride and seats. Sequoia Capstone lost NVH to Yukon and ride to Navigator.
- **Grand Wagoneer** is **7–6**. A same-day loop of all three full-sizers put Navigator most comfortable and Wagoneer last; a household that rented a gas Yukon for a week was glad to return to the Jeep; a car-show tester said Wagoneer “shat on the Tahoe” for ride.
- **Tahoe** is **1–2**: air Tahoe beats GX 550; loses to Wagoneer. **Suburban** is **0–5**.
- **Escalade IQ** picked up its first win: an owner coming from a 2018 Navigator called the IQ “miles above… in terms of feel.” Still 1–1.
- **QX80** is **2–1**. A shopper who test-drove Escalade bought QX80 because Cadillac seats felt “very grandma.”
- **XT6** is **5–2**. Keep this off the shopping chain. One Edmunds owner preferred XT6 ride to the X5 they almost bought; another called Highlander a “tin can.” That is not XT6-over-GLE.

### Mid-luxury / EV: EQS SUV piled on; R1S finally won; Defender is a split

- **EQS SUV** is **5–1**. Two more first-hand notes pick it over iX (owned-both seats “vastly more comfortable”; 2024 EQS 450 tester “more comfortable, smooth”). Victims are still iX / XC90. Raw θ now parks it #1. Do not shop it as the magic-carpet winner.
- **iX** is **10–5**. New owned-both vs Model Y: the Tesla (even on aftermarket coils) was “sitting on a skateboard.”
- **R1S** is **2–9**. First coded wins: owned-both Soft mode “eats up bumps much better than X”; Adventure seats “WAY more comfortable” than a 2024 Model X. Counters: Model X loaner quieter/smoother; another owned-both “model x is much quieter and smoother”; XC60 seats 10/10 vs Rivian 7.5–8.
- **Defender** is **4–5**. Owned-both long-trip comfort over a prior Cayenne; ride split vs Range Rover Sport (2025 RRS loaner won; SVR→Defender 110 went the other way). XC90 seats still beat a 2020 Defender HSE.
- **Cayenne** is **2–8**. Two more X5 testers preferred multi-contour seats and smoothness. **Macan** is **3–5**: GV70 quieter/softer; SQ5 more comfortable on long trips.
- **GLE** picked up a same-day ride win vs Range Rover Sport (GLE580 “MUCH smoother”).

### Three-row: CX-90 is a firm Mazda; Pathfinder vs Highlander is in; Murano is quiet

- **CX-90** is **2–11**. Pilot testers called it “too stiff of a ride for a 3 row suv” / “best ride” went to Pilot. Same-garage Palisade vs CX-90: Palisade ride/luxury, CX-90 firmer over bumps. One CX-90 PHEV tester did prefer Mazda smoothness to a 2026 Palisade.
- **Pathfinder vs Highlander** is new and mostly Pathfinder: seats and cabin quiet. One tester flipped it — Highlander “more refined… smooth,” Pathfinder “like a truck.”
- **Murano** (2026) is quieter and smoother than a 2025 Pathfinder the same owner put 23k miles on. Still 1–1 overall.
- **Pilot vs Passport**: 2025/2026 back-to-back — Pilot quieter on the highway; Passport seat shorter.
- **Palisade vs Enclave**: Palisade Hybrid won 3rd-row comfort; new Enclave turbo “loud… at high rpm.” Enclave is **4–2**, not undefeated.
- **Telluride** is **24–21**. Another owned-both road-trip note vs Sorento (6'2" twins called the Sorento “child abuse”). **Atlas** picked up Palisade comfort (Palisade) and an owned-both seat win vs Pilot.

### Compact: Crosstrek is a small-car ride; Corsair is real; Tiguan vs CR-V flipped

- **Crosstrek** is **2–5**. Four first-hand Outback notes: quieter, “silky smooth,” PA–FL trip fatigue. Consumer-review counters: smoother than an X1; quieter than one CR-V.
- **Corsair** is **5–3**. Beats NX on quiet/ride (two testers). Loses to Q5 on a long-distance ranking and to Nautilus in an owned-both upgrade (“comfortable, quiet ride”).
- **Tiguan** is **6–4**. Two new CR-V notes on `r/Tiguan` (owned-both ’23 CR-V → ’25 Tiguan “much less road/wind noise”; same-day CR-V “felt every bump”).
- **CX-9** is **5–0** (Highlander 3rd-row seats; RAV4 highway quiet). Last-gen Mazda, not a current three-row pick.
- **X1** is **0–5**. **Model Y** is **0–7**. **Model X** is **7–10** after two more Y losses and the R1S split.

### Edmunds / Cars.com (no bot-wall bypass)

Wayback / search snippets added XT6-over-X5 ride, XT6-over-Highlander NVH, XT6-over-Yukon (prior 2019), XT6-over-XT5, Yukon XL seats over a 2025 Escalade, Venza-over-RAV4, Highlander-over-Venza, Crosstrek-over-X1 / CR-V, CX-9-over-RAV4. Dropped a 2019 Explorer vs Highlander (wrong Explorer generation) and four extra luxury losses from one “we shopped” sentence.

---

## What the seventh pass changed

Five research subagents pulled unused threads (flagship trucks, mid-luxury / EV / sport, compact holes, three-row holes, Edmunds/Cars.com snippets). Coded **92** new first-hand rows after dropping a same-author EQS SUV vs iX restatement, 2015–2016 CX-9 / Murano / RX rows, an implicit Corsair-over-X5, and a “more refined” Telluride-over-Pilot with no comfort axis. Same inclusion rules. Same-author restatements of the same pair were not added twice.

### Yukon is now a real flagship node; R1S loses the air-ride comparison

- **GMC Yukon** is **19–5**. Five same-garage notes on one R1S thread pick Yukon air over Rivian ride/seats (“managed the bumps better”; “not nearly as smooth”; “better road trip ride”). Yukon also beat Sequoia (2018 and new) and a 2021 GX 460. One Yukon owner said three previous full-size Range Rovers were not as good on ride — years unspecified, so that is a vote, not a reason to shop Yukon over a current L460. Escalade vs Yukon is still a split.
- **R1S** is **5–14**. New wins: owned-both quieter than a Model X, Adventure seats over a 2023 X, ride over a loaded Suburban. The Yukon pile is the new ceiling. Do not read 5–14 as “always harsh” — it loses to GM air and still splits Tesla.
- **Sequoia** is **3–11**. One 3rd-gen tester preferred it to Tahoe on comfort; it still loses NVH to Tahoe/Yukon and seats to Range Rover.
- **Tahoe** is **2–5** (Escalade trade-in crushed it on seats/ride/quiet; QX80 seats beat it). **QX80** is **4–1** — recliner seats vs Escalade and Tahoe, still a thin sample. **Suburban** is **0–6**.

### Defender lost the Range Rover comparison; Grand Cherokee is on the board

- **Defender** is **4–11**. Six first-hand notes on one RR thread pick full-size Range Rover or Range Rover Sport for ride/NVH/ergonomics. That is the class split, not a new Defender collapse vs XC90.
- **Cayenne** is **4–13**. Owned-both still splits X5; GLE and X7 picked up ride wins. First GLE AMG loss (Cayenne tester: GLE 53 “not quite as comfortable”).
- **Jeep Grand Cherokee** is **1–2**: one tester ranked GLE > Grand Cherokee > X5 on ride. **GLE** is **21–16** after more owned-both road-trip notes vs X5.

### Compact: Murano is quiet vs Pathfinder; X1 finally won seats; Crosstrek piled on

- **Murano** is **3–2**. Two 2020 Murano households called Pathfinder louder/stiffer; one tester preferred new Murano less than Pathfinder ride. That is NVH vs a three-row, not Murano-over-Nautilus.
- **Crosstrek** is **2–12**. More Outback seat/ride notes plus Forester lumbar/loaner seats. Still beats X1 and one CR-V in older consumer reviews.
- **X1** is **1–5**. First coded win: same-day 2023 X1 vs X3, tester preferred X1 seats (“hugging”). Ride comparisons still go the other way.
- **Corsair** is **6–3** after a same-day quiet/comfort win vs XC60. **Model Y** is **0–12** (XC90 ride; more Model X owned-both). **CX-9** is **8–0** (Pilot/Highlander/Pathfinder shop). Last-gen Mazda.

### Three-row: CX-90 still firm; Explorer beat trucks, not Palisade

- **CX-90** is **3–15**. Owned-both seats still lose to Pilot and Telluride. One CX-90 PHEV owner did prefer its NVH to a prior Telluride. A CX-5 loaner on 17s was more composed over bumps than a CX-90.
- **Explorer** is **4–6**. Owned-both smoother than a 4Runner; quieter than a RAV4; splits 2020 Highlander. Still not a Palisade rival.
- **Enclave** is **6–3**. Another Palisade NVH win (new turbo “loud”); Edmunds shopper preferred Enclave ride to Telluride and Palisade. **GCL** is **0–4** (Pilot quieter). **Passport** picked up a family “Pilot felt like a bus” ride note.

### Edmunds / Cars.com (no bot-wall bypass)

Snippets added Escalade-over-2023 Tahoe Premier, Yukon-over-2019 Escalade ride, Yukon-over-GX 460, Range Rover seats over Sequoia, Explorer/Highlander split, Enclave-over-Telluride/Palisade, CX-9-over-Pilot/Highlander/Pathfinder. Dropped 2012 RX, 2015–16 CX-9, and an implicit Corsair-over-X5.

---

## What the eighth pass changed

Five research subagents pulled unused threads (flagship / EV trucks, mid-luxury / sport / EV, compact holes, leftover Edmunds/Cars.com snippets; a fifth family-three-row agent was still running when this pass was coded). Coded **67** new first-hand rows after dropping EQS-sedan-vs-GLS ambiguity, a 2014 LX 570, a 2016 CR-V, QX80 “luxury feel” with no ride/seat/NVH axis, and same-author restatements. Same inclusion rules. Different authors on one thread who named the same pair were kept.

### Escalade IQ and EQS SUV finally met more than iX

- **Cadillac Escalade IQ** is **6–1**. Owned-both / test-drive notes pick it over **Model X** (“spartan Toyota”; “pile of noisy junk”; “way more comfortable”) and over gas **Escalade** (“quieter”; “feels like floating”). That is why raw θ parks it near Nautilus / iX. Do not shop IQ as a Range Rover. The victims are Tesla and the ICE truck it replaced.
- **EQS SUV** is **9–1**. Two more owned-both households pick it over **iX** (massage seats; more isolated even vs iX air). Two first-hand notes pick it over **R1S** (sound deadening; quieter/smoother). Victims are still iX / R1S, not GLS / Range Rover. Raw θ is now #1. The shopping chain still refuses.
- **LX** is **10–2**. A 2025 household with both an LX 700 and a Sequoia: “Significantly quieter and smoother riding.” An LC250 owner who sat in an LX 600 called the Toyota “a geo metro.”
- **Yukon** is **21–5**. Another owned-both Sequoia bounce-back, plus a 2023 Tahoe Premier → 2026 Yukon XL NVH note (“road noise is quieter in the Yukon”).

### Defender beat the sport-luxury set; Grand Cherokee is real

- **Defender** is **10–13**. New wins: owned-both / test-drive vs **Cayenne** (including Cayenne air “jolty” vs Defender), owned-both / same-road vs **R1S**, and two testers vs **GX 550** air. Range Rover still wins ride/NVH when both are named.
- **Grand Cherokee** is **3–2**. Air / massage WL beat an X5 the owner called “sporty and rough”; an owned-both Grand Cherokee vs Model Y went to the Jeep on ride and seats. **GLE AMG** picked up its first win (owned-both 53 vs X5 firmness) and still loses seats to a family GLS.
- **Cayenne** is **4–17**. More base / air losses to GLE, Defender, and Range Rover.
- **R1S** is **5–21**. New losses to Defender, X5, iX, and EQS SUV. **Model Y** is **0–16**.

### Compact: Venza piled on RAV4; Tiguan is quieter; Corsair lost to Nautilus

- **Venza** is **14–3**. Five more first-hand notes vs **RAV4** (owned-both quiet; household smoother; Limited-vs-Limited test). Still a RAV4-class step-up, not Nautilus.
- **Tiguan** is **11–4**. Owned-both quieter than a 2025 RAV4 (explicitly not smoother); two owned-both CX-5 notes (quieter / smoother).
- **Corsair** is **6–5** after an owned-both 2021 Corsair → 2024 Nautilus ride upgrade and a same-day “much smoother.” **X1** is **1–7**. **XT5** finally won one (long-drive seats vs X3). **Crosstrek** is **4–14** (CR-V quieter; one Wilderness quieter than a Forester Hybrid; seats still split vs Outback).
- **Murano** is **4–2** after a 2016 Murano vs 2016 Model X owned-both (ride / seats / NVH). Last-gen Murano, not a Nautilus result.

### Three-row leftovers: GCL finally won NVH; Enclave met an X5

- **Grand Cherokee L** is **2–4**. First coded wins: a 2021 Edmunds shopper called it quieter than Palisade and Telluride on 18s. Still loses ride to Pilot / Telluride testers.
- **Enclave** is **7–3**. An Edmunds 2020 owner preferred Enclave ride/quiet to a company X5 on 500-mile trips. That is Enclave-over-X5, not Enclave-over-GLE. Keep it in the family class.

### Edmunds / Cars.com (no bot-wall bypass)

Snippets / listing reprints added Enclave-over-X5, GCL-over-Palisade/Telluride NVH, XT5-over-X3 long-drive seats. Dropped a pre-2018 Sequoia, an incomplete Tahoe-vs-Grand Cherokee snippet, and Explorer “driving dynamics” with no comfort axis.

---

## What the ninth pass changed

The ninth pass added **13 first-hand rows** and one previously missing full-size SUV. After the later audit (below) the fit loads **786 usable comparisons / 790 coded rows** after the sedan and exclusion drops.

### Expedition fills the full-size truck gap

**Ford Expedition** enters at **3–3**: it beats Suburban twice on stability / interior comfort, beats Tahoe on seats and body control, and loses ride comparisons to Suburban, Escalade, and Navigator. The practical read is a split: Expedition seats and body control are strong, while GM air / magnetic-ride setups can be softer. It is not evidence that Expedition belongs beside Navigator or Escalade in the comfort chain.

### 2026 Santa Fe is a Palisade counterpoint, not a luxury benchmark

The new **Hyundai Santa Fe** has four direct comparisons, all against 2026 Palisade, and loses all four on ride / quiet. Owners describe it as sportier and still smooth; the Palisade is quieter, smoother, and more settled over bumps. Because Santa Fe has not met CR-V, Tiguan, RAV4, or another compact rival in this file, its **0–4** is a within-Hyundai result, not a general compact ranking.

### A few luxury bridges got stronger

One owner who had both preferred the full-size Range Rover to the GLS on comfort. A new Q7 test drive favored the Audi’s softer / quieter feel over X5, while a three-way test drive called the GV80 cushier than the chosen X5. These reinforce the existing split—comfort-first Audi / Genesis versus sportier BMW—without changing the ceiling or making GV80 an air-suspension flagship.

## What the audit changed

The compiled audit ([`../audit/compiled.md`](../audit/compiled.md)) was applied to `data/comparisons.csv`. It did not add new comparisons. It cleaned the ones already coded.

- **19 rows deleted** — no single passage supported the pair (isolated praise, spliced quotes, brand-level statements coded to a specific rival). Range Rover lost three unsupported wins (GLE / X5 / Palisade). GLS lost a Navigator row. Aviator lost an RX recommendation. Palisade lost three thin three-row rows. GLE/X5 each lost a weak head-to-head.
- **Evidence recodes** — 181 tags moved, mostly `test_drove_both` → `owned_one_td_other` (owns one, sat in the other) or down to `opinion` / `opinion_plus_drive`. `rank.py` reads the tag, so those rows now sit in the owner fit instead of the tester pile, or drop out of the bias fit.
- **Quote / axis / `home_team` / loser** — misleading fragments replaced; six axis fixes; ~97 home-badge flags flipped; one GLE row recoded to GLE AMG.

The shopping chain above did not move. Raw θ at the top is EQS SUV 3.87, Range Rover 2.98, then sparse-graph CX-9 / Enclave. Palisade is 54–22 and now sits near Aviator / Escalade on default θ (who they met is still the chain). Ascent is still 22–9. The owner cut is the bigger remaining shift: testers fell from about 40% of the file to 176 / 786, because many “test-drove both” tags were really owner-plus-sit.

## Evidence that actually moves the ranking

### Range Rover is still the ceiling

Full-size Range Rover remains **15–2**. The losses are still not a flagship rival winning isolation — they are the older X7 window-noise note, plus a Yukon owner comparing unspecified-year Range Rovers. Three brand-only RR wins were deleted in the audit. Defender notes go the other way.

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
| 1 | Mercedes EQS SUV | 3.87 | 9–1 |
| 2 | Range Rover | 2.98 | 15–2 |
| 3 | Mazda CX-9 | 2.93 | 7–0 |
| 4 | Buick Enclave | 2.89 | 7–3 |
| 5 | Cadillac Escalade IQ | 2.71 | 6–1 |
| 6 | Mercedes GLS | 2.46 | 17–4 |
| 7 | Cadillac XT6 | 2.44 | 7–2 |
| 8 | Lexus LX | 2.35 | 10–2 |
| 9 | GMC Yukon | 2.17 | 21–5 |
| 10 | Lincoln Nautilus | 2.09 | 14–3 |
| 11 | Audi Q8 | 1.70 | 5–3 |
| 12 | Jeep Grand Wagoneer | 1.66 | 7–6 |
| 13 | Hyundai Palisade | 1.61 | 54–22 |
| 14 | Lincoln Aviator | 1.59 | 14–4 |
| 15 | Cadillac Escalade | 1.58 | 18–15 |
| 16 | Range Rover Sport | 1.57 | 12–3 |
| 17 | Lincoln Navigator | 1.55 | 13–11 |
| 18 | Volkswagen Atlas | 1.47 | 11–5 |
| 19 | Infiniti QX80 | 1.42 | 4–1 |
| 20 | Nissan Murano | 1.38 | 4–2 |
| 21 | BMW iX | 1.37 | 11–7 |
| 22 | Subaru Outback 2026 | 1.30 | 12–1 |
| 23 | Audi Q7 | 1.23 | 9–5 |
| 24 | Acura MDX | 1.17 | 8–4 |
| 25 | Genesis GV70 | 1.12 | 14–4 |
| 26 | Mercedes GLE | 1.06 | 21–14 |
| 27 | BMW X5 | 0.96 | 35–50 |
| 28 | BMW X7 | 0.89 | 10–20 |
| 29 | Subaru Ascent | 0.88 | 22–9 |
| 30 | Genesis GV80 | 0.87 | 8–7 |
| 31 | Lexus GX | 0.78 | 25–14 |
| 32 | Lexus RX | 0.73 | 19–14 |
| 33 | Lexus TX | 0.70 | 6–6 |
| 34 | Nissan Pathfinder | 0.57 | 15–11 |
| 35 | Jeep Grand Cherokee | 0.52 | 3–2 |
| 36 | Lincoln Corsair | 0.42 | 6–5 |
| 37 | Audi Q5 | 0.31 | 15–9 |
| 38 | Volvo XC60 | 0.28 | 17–12 |
| 39 | Kia Telluride | 0.23 | 28–26 |
| 40 | Volvo XC90 | 0.22 | 15–13 |
| 41 | Honda Pilot | 0.17 | 33–37 |
| 42 | Toyota Grand Highlander | 0.00 | 5–12 |
| 43 | Volkswagen Tiguan | −0.03 | 11–4 |
| 44 | Subaru Outback (2020–25) | −0.12 | 31–16 |
| 45 | Toyota Venza | −0.12 | 14–3 |
| 46 | Porsche Macan | −0.22 | 5–6 |
| 47 | Toyota Highlander | −0.22 | 8–23 |
| 48 | Land Rover Defender | −0.27 | 10–13 |
| 49 | Lexus NX | −0.40 | 8–11 |
| 50 | Honda CR-V | −0.43 | 21–18 |
| 51 | Jeep Grand Cherokee L | −0.49 | 2–4 |
| 52 | Honda Passport | −0.62 | 6–8 |
| 53 | Mercedes GLE AMG | −0.66 | 1–4 |
| 54 | Toyota Sequoia | −0.79 | 3–13 |
| 55 | Ford Explorer | −0.84 | 4–6 |
| 56 | Ford Expedition | −1.10 | 3–3 |
| 57 | Mercedes GLC | −1.25 | 6–6 |
| 58 | Hyundai Santa Fe | −1.42 | 0–4 |
| 59 | Mazda CX-90 | −1.43 | 3–15 |
| 60 | Chevrolet Tahoe | −1.65 | 2–7 |
| 61 | Cadillac XT5 | −1.71 | 1–8 |
| 62 | Porsche Cayenne | −1.85 | 4–17 |
| 63 | Tesla Model X | −1.97 | 11–16 |
| 64 | Mazda CX-5 | −2.03 | 5–8 |
| 65 | Subaru Crosstrek | −2.11 | 4–14 |
| 66 | Lexus GX 550 | −2.27 | 9–15 |
| 67 | Rivian R1S | −2.30 | 5–21 |
| 68 | Chevrolet Suburban | −2.30 | 1–8 |
| 69 | Mazda CX-50 | −2.36 | 1–13 |
| 70 | Subaru Forester | −2.41 | 2–14 |
| 71 | Kia Sorento | −2.77 | 0–6 |
| 72 | Toyota Land Cruiser | −3.15 | 4–7 |
| 73 | Toyota 4Runner | −3.59 | 3–24 |
| 74 | Toyota RAV4 | −3.63 | 1–31 |
| 75 | BMW X3 | −3.84 | 3–20 |
| 76 | BMW X1 | −4.46 | 1–7 |
| 77 | Tesla Model Y | −5.00 | 0–16 |

**EQS SUV** at 3.87 / 9–1, **CX-9** at 2.93 / 7–0, **Escalade IQ** at 2.71 / 6–1, and **XT6** at 2.44 / 7–2 are this pass’s sparse-graph inflations. EQS beat iX / R1S. CX-9 beat Highlander/Pilot/RAV4. IQ beat Model X / gas Escalade. XT6 beat X5/Highlander/XT5. None of them met a Range Rover.

**GLS** 17–4 is still almost all vs X7 on plushness. Raw θ next to Range Rover is the same artifact as before. Range Rover is **15–2** after the audit dropped three unsupported wins.

**Yukon** 21–5 is the flagship-truck sample, not a magic-carpet result — the victims are R1S / Sequoia / GX / Tahoe. **R1S** is 5–21. **Defender** is 10–13.

The [bias-adjusted table](bias_analysis.md) still shrinks X5 / iX θ and slightly raises Telluride. Palisade is already high on default θ. Yukon stays high (21–5 is mostly owned-both). That agrees with the chain more than with this raw θ list.

---

## Within-class order (safer for shopping)

**Compact / small-mid**  
Genesis GV70 (14–4) ≈ Audi Q5 (air) ≈ Lincoln Nautilus (14–3) ≈ Mercedes GLC ≈ **Toyota Venza** (14–3 vs RAV4) > Volvo XC60 (seats; ride depends on wheels; splits NX) > **2026 Outback** > Honda CR-V ≈ **2020–25 Outback** > Volkswagen Tiguan (11–4 vs RAV4/CX-5) > Mazda CX-5 ≈ Toyota RAV4 ≈ Mazda CX-50 ≈ Forester ≈ **BMW X3** (3–20). CR-V vs 2020–25 Outback is still split. CR-V vs CX-50 is not.

**Midsize luxury**  
Range Rover Sport ≈ Lincoln Aviator > BMW iX (quiet EV vs Model X / X5 / R1S; loses comfort to EQS SUV) ≈ Mercedes GLE ≈ Audi Q7 (quiet / air) ≈ Acura MDX Type S (seats) ≈ Genesis GV80 > BMW X5 ≈ Lexus RX > Audi Q8 (air ride vs X5 seats) ≈ Porsche Cayenne *with air* > **GX 460** > **Defender** (loses to RR; beats Cayenne / R1S / GX 550) > **GX 550** (beats Land Cruiser / usually 4Runner; loses to 460 / Defender air) > **Land Cruiser** 250 > **Rivian R1S** (5–21; loses Yukon air / Defender / X5 / EQS) > **4Runner** / **Model Y** (0–16)

**Flagship / large**  
Range Rover (15–2; Defender pile plus the older X7 NVH counter) ≈ GLS (still beats X7) ≈ LX > Escalade (ride vs Navigator) ≈ **Escalade IQ** (6–1 vs Model X / gas Escalade) ≈ Navigator (seats) ≈ Grand Wagoneer ≈ **Yukon** (21–5 vs R1S / Sequoia / GX / Tahoe) ≈ X7 air > QX80 (seats vs Escalade/Tahoe; thin) > Tahoe / Sequoia / Suburban

**Three-row family**  
Palisade ≥ Ascent (ride) ≥ **Pathfinder** (seats vs Pilot; loses ride to Palisade/Telluride; loses NVH to 2020 Murano) ≥ Telluride (28–26: beats Sorento/Explorer/4Runner, splits Pilot) ≥ Pilot ≥ Atlas (quiet vs Pilot) > Highlander > Grand Highlander ≈ CX-90 (3–15, still firm) > Passport (driver-seat counter) > Explorer (4–6 vs trucks, not Palisade) / Sorento / **GCL** (2–4; first NVH wins vs Palisade/Telluride). Palisade is still the comfort default. Pathfinder is the Pilot-seat alternative. Telluride is no longer just “loses to Palisade.”

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

- Reddit still carries most of the signal (710 of 796 rows). The eighth pass added Escalade IQ / EQS SUV / LX / Yukon / LC, Defender / Grand Cherokee / Cayenne / R1S / Model Y, Venza / Tiguan / Corsair / X1, and leftover GCL / XT5 / Enclave owner lines. Direct fetches of review hubs are still often blocked; those votes are taken from indexed owner-review text. How to do that next time: [`methodology.md`](methodology.md#getting-around-blocked-review-sites).
- Brand subs still tilt GLE vs X5, Palisade vs Pilot, Pathfinder vs Pilot, Ascent vs the Koreans, GX vs 4Runner, Yukon vs Sequoia, iX vs Model X, and Venza vs RAV4. Owned-both comments were kept at full weight; thin home-team comments stay down-weighted. The [bias-adjusted fit](bias_analysis.md) tightens that further.
- Escalade IQ (6–1), EQS SUV (9–1), Yukon (21–5), Defender (10–13), R1S (5–21), Venza (14–3), and Grand Cherokee (3–2) are no longer empty. EQS SUV / Escalade IQ / XT6 / CX-9 / 2026 Outback / Ascent raw θ are still “beat weaker or same-class rivals” artifacts.
- One six-SUV test-drive write-up still moves Q8 / MDX / Q7 / Cayenne more than any other single source. Its Reddit score is ignored; it is one `test_drove_both` vote.
- Palisade > Nautilus and Palisade > Aviator are single Cars.com owners. They are coded. They do not move Palisade into the luxury shopping list.
- Range Rover’s first loss is one X7 owner on window noise. Direction of the other RR notes is still isolation/seats over X7.
- No China / Europe-only nameplates. India/Gulf X7–GLS threads were not coded.
- Comfort is not reliability. Range Rover, Palisade, Ascent, and Pathfinder all win comfort arguments in threads that immediately warn you about service.

Re-run: `python3 src/rank.py`. Default table: `data/ranking.csv`. Bias table: `data/ranking_bias.csv`.
