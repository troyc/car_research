# SUV Comfort Ranking from Customer Comparisons

Research project that ranks SUV comfort from **customer comments that compare two or more SUVs and state a preference**. Isolated praise ("the X5 is comfy") is not used. Only relative statements are.

## What this is

A Bradley–Terry ranking of current-generation SUVs on ride comfort, seats, cabin quiet, and long-trip fatigue, built from first-hand owner and test-drive comments on Reddit, X, and Edmunds/Cars.com consumer reviews. Collected 18 August 2026; expanded the same day for 2020–2025 / 2026 Outback (new generation), Ascent, 2020–2022 RX / RX L, and 2014–2023 GX, plus a second fit that down-weights source bias.

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

**Range Rover (full-size) is generally preferred over Range Rover Sport / Escalade / GLS / X7 / Navigator, which are generally preferred over Aviator / XC90 / GLE / Q7 / MDX / GV80, which are generally preferred over X5 / RX, which are generally preferred over Q5 / GLC / XC60 / Nautilus, which are generally preferred over Palisade ≥ Ascent (ride) / 2026 Outback (vs the old wagon), which are generally preferred over Pilot / Telluride / Highlander / Grand Highlander / CR-V ≈ 2020–25 Outback, which are generally preferred over RAV4 / CX-5 / CX-50 / 4Runner / Forester / Model Y. GX 460 beats 4Runner on comfort and splits with RX; it still loses to X5 / X7 / GLE.**
