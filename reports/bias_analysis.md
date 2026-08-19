# Source-bias analysis

A second Bradley–Terry fit of the same **786-vote / 790-row** pairwise file, re-weighted to take source bias seriously. Default ranking: [`composite_ranking.md`](composite_ranking.md). Method: [`methodology.md`](methodology.md).

Default `src/rank.py` already down-weights brand-subreddit home-team comments (`×0.6`) and uses `log(1+upvotes)` so a 241-upvote write-up cannot own the scale. That is not the same as asking whether **the sources themselves** are biased.

## What the second fit changes

| Knob | Default | Bias-adjusted |
|---|---|---|
| Reddit / X karma | `weight × log(1+upvotes)` | none — popularity is not independence |
| Thin talk (`opinion`, `opinion_plus_drive`) | kept at 0.7 / 1.2 | dropped |
| Coded home-team | `×0.6` | `×0.4` |
| Home-team **and** a model fan-sub | already in home-team | extra `×0.75` |
| Edmunds / Cars.com owner reviews | same as Reddit | `×1.25` |
| X | same as Reddit | `×0.8` |

Two extra robustness runs are printed by the script and are **not** the headline of *this* file:

- **no_home** — drop every `home_team=1` row
- **owned_both** — lived-with-both only, no karma boost

Owners vs testers is a separate cut: [`owner_analysis.md`](owner_analysis.md) (`data/ranking_owners.csv`). Same default weights; `test_drove_both` dropped.

Re-run: `python3 src/rank.py` writes `data/ranking.csv` (default) and `data/ranking_bias.csv`.

## Why these knobs

The corpus is not a random sample of owners.

1. **Reddit karma rewards entertainment and tribal certainty.** A funny X5-vs-GLE roast at +21 is not 21 independent sit-comparisons. The log boost already limits this; removing it asks what the *statements* say without the crowd.
2. **Brand subs are not a census.** `r/LexusGX`, `r/SubaruAscent`, `r/Subaru_Outback`, `r/HyundaiPalisade` are full of people who already bought the home badge. Many of those comments are still first-hand and specific. They stay in the file. They do not keep default weight.
3. **Edmunds / Cars.com consumer reviews are slower and less tribal.** They are also the pages most likely to 403 an automated fetch, so the sample is smaller. The lift is modest (`×1.25`), not a replacement for Reddit.
4. **“I heard Volvos have great seats” and “just get an Outback”** are already tagged thin. The bias fit drops them instead of leaving a 0.7 drip in the likelihood.

This is still not a causal model of reviewer psychology. It does not fix switcher regret (people who sold A for B tend to say B > A). It does not split wheel size. It is a second reading of the same quotes.

## What moves

Core models, default 3+ appearances. Ranks below are **global rank among every model that appears in that fit** (sparse 1-appearance cars sit in the file, so a “rank 17 Ascent” is not “17th among shoppers”).

| Model | Default θ | Default W–L | Bias θ | Default rank | Bias rank | no_home rank | owned_both rank |
|---|---:|---:|---:|---:|---:|---:|---:|
| Range Rover | 4.51 | 15–2 | 2.87 | 3 | 6 | 11 | 2 |
| Mercedes GLS | 4.55 | 17–4 | 2.38 | 2 | 7 | 8 | 4 |
| Subaru Ascent | 1.54 | 22–9 | 0.72 | 29 | 30 | 51 | 33 |
| Subaru Outback 2026 | 0.31 | 12–1 | 0.80 | 40 | 28 | 53 | 8 |
| Lexus RX | 1.60 | 19–14 | 0.56 | 26 | 31 | 24 | 26 |
| Lexus GX | 1.54 | 25–14 | 0.73 | 28 | 29 | 26 | 32 |
| Hyundai Palisade | −0.33 | 54–22 | 1.92 | 46 | 13 | 19 | 7 |
| BMW X5 | 2.98 | 35–50 | 0.22 | 11 | 36 | 39 | 35 |
| Honda CR-V | −0.07 | 21–18 | −0.16 | 42 | 46 | 29 | 55 |
| Subaru Outback (2020–25) | −1.84 | 31–16 | −0.03 | 58 | 45 | 40 | 44 |
| Nissan Pathfinder | −0.30 | 15–11 | 0.35 | 45 | 33 | 60 | 24 |
| Genesis GV70 | 2.31 | 14–4 | 0.83 | 18 | 27 | 21 | 61 |
| BMW iX | 3.29 | 11–7 | 0.86 | 6 | 26 | 43 | 10 |
| Kia Telluride | −0.89 | 28–26 | 0.28 | 52 | 34 | 42 | 21 |
| Toyota 4Runner | −3.91 | 3–24 | −3.17 | 72 | 73 | 65 | 73 |
| Toyota RAV4 | −4.53 | 1–31 | −3.62 | 76 | 74 | 70 | 76 |

### The ceiling shrinks; the family class rises

Range Rover is 3 on the default numeric list (EQS SUV / GLS own raw #1–2) and 6 on the bias list. Its θ falls from 4.51 to 2.87. **GLS** is 17–4 vs X7 and still does not jump Range Rover in the shopping chain.

**Palisade** is still a big mover (default rank 46 → bias 13). Default θ is depressed because the model plays inside the three-row set. Take karma off and 54–22 against Pilot / Telluride / Highlander / Grand Highlander / Pathfinder / CX-90 looks like the class default. It is still not an X5.

**Yukon** is still the robustness check: 21–5 in the default fit and 10th on the bias list. Most of those wins are owned-both vs R1S / Sequoia / GX / Tahoe, so stripping karma does not erase them. That is “comfortable full-size GM,” not Yukon-over-Range Rover.

**Ascent** is still pulled down (1.54 → 0.72; rank 29 → 30). **no_home** pulls it to 51. The sample is still brand-sub heavy.

**Pathfinder** is no longer a bias-fit rocket (−0.30 → 0.35; rank 45 → 33). Palisade and Telluride still beat it on ride.

**GV70** is 14–4. The bias fit parks it mid-pack (rank 27) once the X3/Q5/Macan tester pile is de-weighted. **iX** shrinks (3.29 → 0.86) because several notes live on `r/BMWiX` and more owned-both EQS SUV losses are now in the file.

**X5** still falls (2.98 → 0.22) once GLE/X5 brand-sub karma is stripped.

**Telluride** still looks better in the bias fit (−0.89 → 0.28) once the Sorento / Explorer / CX-90 / Pilot-split notes are not drowned by Palisade-sub volume.

**EQS SUV**, **Escalade IQ**, and **XT6** stay high in both fits for the same graph reason as before: they mostly beat the cars they actually met (iX / R1S; Model X / gas Escalade; X5/Highlander/Yukon). The shopping chain still refuses to promote them.

### The four nameplates from the previous pass (still true)

**2020–2025 Outback** is stable. 31–16, still a compact. It beats RAV4 and Forester in owned-both notes; it splits CR-V. Every robustness column leaves it in the compact cluster, not next to RX.

**2026 Outback** is 12–1. Default rank stays mid-pack; the bias fit *raises* it because the 12–1 record does not depend on karma. Its victims are still the old Outback, Forester, CX-50, a 4Runner, and one Ascent. Do not read 12–1 as “Nautilus class.”

**2020–2022 RX** (and RX L, coded as RX) is among the more stable luxury nameplates. Default 19–14. vs GX 460 the unibody RX usually wins ride; some GX households prefer isolation.

**2014–2023 GX 460** is 25–14. Almost every win is still vs 4Runner. vs RX it splits. vs X5 / X7 / GLE / LX it usually loses; one tester preferred the 460 to GLS / X5 / QX80 / MDX. GX 550 is now 9–15 (beats Land Cruiser / usually 4Runner; still loses to the 460). The *direction* survives: GX is a comfortable 4Runner, not a soft-roader X5.

## How to read this next to the composite chain

The composite chain in [`composite_ranking.md`](composite_ranking.md) is still the shopping document. It already refuses to promote Palisade or Ascent into flagship because of who they actually met.

Use this file for one question: **if we distrust Reddit’s applause and brand-sub home cooking, does the story change?**

- Flagship order: no.
- RX vs the Germans: no — RX stays dual-purpose luxury.
- GX vs 4Runner: no — GX still wins comfort.
- 2020–25 Outback vs RAV4 / Forester: no.
- 2026 Outback vs the old wagon: yes, owners who had both say quieter/smoother; the sample is small.
- Palisade / Ascent vs luxury θ: yes, the *numeric* global list was flattering luxury-thread engagement. The chain already said that. The bias fit agrees with the chain more than with the raw θ list.
- Pathfinder vs Pilot: no — Pathfinder still wins seats.
- GV70 vs X3 / Q5: no — GV70 still wins that compact-luxury loop; it now has Nautilus / NX / RX counters.
- iX vs Model X: no — iX still wins quiet. vs EQS SUV, owners who had both pick the Mercedes.
- Telluride vs Palisade: no — Palisade still wins ride more often; Telluride is no longer 5–12.
