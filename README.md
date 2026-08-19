# SUV Comfort Ranking from Customer Comparisons

Research project that ranks SUV comfort from **customer comments that compare two or more SUVs and state a preference**. Isolated praise ("the X5 is comfy") is not used. Only relative statements are.

## What this is

A Bradley–Terry ranking of current-generation SUVs on ride comfort, seats, cabin quiet, and long-trip fatigue, built from first-hand owner and test-drive comments on Reddit, X, and Edmunds/Cars.com consumer reviews. Collected 18 August 2026; expanded the same day through nine research passes, then audited (19 unsupported rows removed; evidence tags, quotes, and `home_team` recoded). A second fit down-weights source bias. A third fit keeps only owners (no same-day testers). Reddit / X scores are not used in any fit.

## How to read it

Open `reports/composite_ranking.md` first. That file is the result: one composite chain plus segment rankings. `reports/bias_analysis.md` is the second reading — same quotes, less brand-sub weight. `reports/owner_analysis.md` is the third — same quotes, **no test drivers**.

- `data/comparisons.csv` — coded pairwise votes (each row has a stable 4-character `id`)
- `src/rank.py` — Bradley–Terry fit (default + bias-adjusted + owners)
- `data/ranking.csv` / `data/ranking_bias.csv` / `data/ranking_owners.csv` — machine-readable tables
- `reports/figures/` — PNGs of the graph, segment ladders, rank robustness, and top matchups
- `audit/` — verification kit (`fetch_pages.sh`, `parse_reddit.py`, `audit_rows.py`), `compiled.md` (applied full-file audit), and `old/` (per-batch working notes)
- `reports/methodology.md` — inclusion rules, weighting, generation coding, limits, and how to read Edmunds/Cars.com when the live review page is blocked

```bash
python3 src/rank.py
```

Then rebuild the figures from those CSVs (does not re-fit):

```bash
# matplotlib + numpy
python3 src/plot.py

# this machine (Nix):
nix-shell -p python3Packages.matplotlib python3Packages.numpy --run "python3 src/plot.py"
```

Writes `reports/figures/comfort_ladders.png`, `comparison_graph.png`, `rank_robustness.png`, and `top_matchups.png`.

## Who met whom

Each line is a pair with 3+ coded votes. Height is global θ; columns are shopping segments. Most comparisons stay inside a column — that is why EQS SUV / XT6 / CX-9 sit near flagships on raw θ. Amber = the lower car won the head-to-head. Full-size image and the other charts: [`reports/figures/`](reports/figures/).

![Who actually sat in whom — pairwise SUV comfort comparisons](reports/figures/comparison_graph.png)

## Composite chain

Shopping order from who actually beat whom. Later bands are generally less comfortable. `≈` is a split; `/` is “about this neighborhood.” Caveats and who-met-whom: [`reports/composite_ranking.md`](reports/composite_ranking.md).

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

Off the ladder: **GX 460** beats 4Runner and splits RX (not an X5). **GX 550** beats Land Cruiser / usually 4Runner; loses to the 460 and air Defender. **Sequoia** loses ride/NVH to LX / Yukon / Range Rover / Navigator. **Defender** loses to Range Rover; beats Cayenne / R1S / GX 550. **Escalade IQ** is 6–1 vs Model X and gas Escalade — not a Range Rover.

## Mechanical ranking

Core models with **three or more** coded appearances. Bradley–Terry θ and win–loss from the default fit (`python3 src/rank.py`). Raw θ still inflates cars that only beat same-class rivals (EQS SUV 9–1 vs iX/R1S, Escalade IQ 6–1 vs Model X, XT6 7–2, CX-9 7–0 vs Highlander/Pilot/RAV4). Use the chain above, not this numeric list, as a shopping order.

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
