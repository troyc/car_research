# Source-bias analysis

A second Bradley–Terry fit of the same pairwise file, re-weighted to take source bias seriously. Default ranking: [`composite_ranking.md`](composite_ranking.md). Method: [`methodology.md`](methodology.md).

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

Two extra robustness runs are printed by the script and are **not** the headline:

- **no_home** — drop every `home_team=1` row
- **owned_both** — lived-with-both only, no karma boost

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
| Range Rover | 6.08 | 6–0 | 3.93 | 1 | 2 | 4 | 1 |
| Subaru Ascent | 1.34 | 22–9 | 0.32 | 20 | 28 | 35 | 19 |
| Subaru Outback 2026 | 0.47 | 10–1 | 1.40 | 25 | 13 | 21 | 6 |
| Lexus RX | 0.02 | 18–14 | 0.41 | 34 | 25 | 37 | 14 |
| Lexus GX | 0.44 | 15–11 | 0.02 | 26 | 31 | 32 | 17 |
| Hyundai Palisade | −0.98 | 38–16 | 1.38 | 40 | 14 | 19 | 11 |
| BMW X5 | 2.15 | 15–21 | 0.34 | 12 | 27 | 23 | 22 |
| Honda CR-V | −0.56 | 10–12 | −0.35 | 37 | 38 | 29 | 27 |
| Subaru Outback (2020–25) | −1.93 | 19–15 | −0.37 | 44 | 39 | 31 | 24 |
| Toyota 4Runner | −3.63 | 0–9 | −3.02 | 59 | 58 | 49 | 48 |
| Toyota RAV4 | −5.17 | 0–15 | −4.75 | 61 | 61 | 56 | 50 |

### The ceiling shrinks; the family class rises

Range Rover stays first (or second to LX once karma is gone). Its θ falls from 6.08 to 3.93 because several of those 6–0 notes lived in high-upvote / brand-sub threads. The **order** at the top does not flip.

**Palisade** is the biggest mover. Default θ is depressed because the model plays almost entirely inside the three-row set while luxury cars collect high-engagement wins against each other. Take karma off and Palisade’s 38–16 against Pilot / Telluride / Highlander / Grand Highlander looks like what it is: the volume comfort default in that class. It is still not an X5.

**Ascent** is a ride specialist (22–9). After the extra owned-both counters (Pilot seats, Palisade long-trip, Outback ride split), the bias fit **does** pull it down (θ 1.34 → 0.32; rank 20 → 28). **no_home** pulls it further (35). A lot of the Ascent sample still lives on `r/SubaruAscent`. Treat 22–9 as “won more ride loops than it lost,” not “quieter than a Palisade Calligraphy.” One Ascent-sub shopper who actually drove both said the Telluride was “much quieter.”

**X5** falls (2.15 → 0.34) once GLE/X5 brand-sub karma is stripped. That matches the older write-up: X5 is a dual-purpose luxury SUV with a losing record on plushness, and Reddit likes to argue about it.

### The four nameplates this pass was about

**2020–2025 Outback** is stable. 19–15, still a compact. It beats RAV4 and Forester in owned-both notes; it splits CR-V. Every robustness column leaves it in the compact cluster, not next to RX.

**2026 Outback** is 10–1. Default rank stays mid-pack; the bias fit *raises* it because the 10–1 record does not depend on karma. Its victims are still the old Outback, Forester, CX-50, a 4Runner, and one Ascent. Do not read 10–1 as “Nautilus class.”

**2020–2022 RX** (and RX L, coded as RX) is among the more stable luxury nameplates. Default 18–14; bias 18–12 after thin opinion rows drop, and rank *improves* (34 → 25) because RX’s new Highlander / RAV4 / Q5 notes are owned-both, not brand-sub applause. vs GX 460 the unibody RX usually wins ride; some GX households prefer isolation.

**2014–2023 GX 460** is no longer 0–3. It is 15–11. Almost every new win is vs 4Runner (owned-both: quieter, smoother, seats that survive a long trip). vs RX it splits. vs X5 / X7 / GLE / LX it still loses. Two first-hand notes say the **460 rides smoother than the GX 550**. **no_home** and the extra fan-sub penalty both nudge GX down a couple of ranks — `r/LexusGX` is where the 4Runner pile-on lives. The *direction* survives: GX is a comfortable 4Runner, not a soft-roader X5.

## How to read this next to the composite chain

The composite chain in [`composite_ranking.md`](composite_ranking.md) is still the shopping document. It already refuses to promote Palisade or Ascent into flagship because of who they actually met.

Use this file for one question: **if we distrust Reddit’s applause and brand-sub home cooking, does the story change?**

- Flagship order: no.
- RX vs the Germans: no — RX stays dual-purpose luxury.
- GX vs 4Runner: no — GX still wins comfort.
- 2020–25 Outback vs RAV4 / Forester: no.
- 2026 Outback vs the old wagon: yes, owners who had both say quieter/smoother; the sample is small.
- Palisade / Ascent vs luxury θ: yes, the *numeric* global list was flattering luxury-thread engagement. The chain already said that. The bias fit agrees with the chain more than with the raw θ list.
