# SUV Comfort Ranking from Customer Comparisons

Research project that ranks SUV comfort from **customer comments that compare two or more SUVs and state a preference**. Isolated praise ("the X5 is comfy") is not used. Only relative statements are.

## What this is

A Bradley–Terry ranking of current-generation SUVs on ride comfort, seats, cabin quiet, and long-trip fatigue, built from first-hand owner and test-drive comments on Reddit, X, and Edmunds/Cars.com consumer reviews. Collected 18 August 2026; expanded the same day for 2020–2025 / 2026 Outback, Ascent, 2020–2022 RX / RX L, and 2014–2023 GX, then again for thin compact-luxury / midsize / flagship nameplates, missing three-row models (Pathfinder, Sorento, Passport, Atlas), and more Edmunds/Cars.com owner pairs. A second fit down-weights source bias.

## How to read it

Open `reports/composite_ranking.md` first. That file is the result: one composite chain plus segment rankings. `reports/bias_analysis.md` is the second reading — same quotes, less Reddit karma and brand-sub weight.

- `data/comparisons.csv` — coded pairwise votes
- `src/rank.py` — Bradley–Terry fit (default + bias-adjusted)
- `data/ranking.csv` / `data/ranking_bias.csv` — machine-readable tables
- `reports/methodology.md` — inclusion rules, weighting, generation coding, limits, and how to read Edmunds/Cars.com when the live review page is blocked

```bash
python3 src/rank.py
```

## One-line result

**Range Rover (full-size) / GLS / LX sit at the top; Range Rover now has a first X7 NVH counter. Then Range Rover Sport / Escalade / Navigator / Grand Wagoneer / X7 / iX / Aviator. Then GLE / Q7 / MDX / GV80 / X5 / RX. Then Q5 / Nautilus / GLC / XC60 / GV70 (compact luxury — GV70 is 9–0 here, not a flagship). Then Palisade ≥ Ascent (ride) / Pathfinder (seats vs Pilot) / Telluride (now a real split, not 5–12) / Pilot / 2026 Outback. Then CR-V ≈ 2020–25 Outback / Highlander / Grand Highlander. Then RAV4 / CX-50 / X3 / 4Runner / Forester / Model Y. GX 460 still beats 4Runner and splits RX; GX 550 now beats 4Runner too and still loses to the 460.**
