# SUV Comfort Ranking from Customer Comparisons

Research project that ranks SUV comfort from **customer comments that compare two or more SUVs and state a preference**. Isolated praise ("the X5 is comfy") is not used. Only relative statements are.

## What this is

A Bradley–Terry ranking of current-generation SUVs on ride comfort, seats, cabin quiet, and long-trip fatigue, built from first-hand owner and test-drive comments on Reddit, X, and Edmunds/Cars.com consumer reviews. Collected 18 August 2026; expanded the same day through nine research passes, with the latest adding Expedition / Suburban / Tahoe / Escalade / Navigator, 2026 Santa Fe / Palisade, and fresh RR / GLS / Q7 / X5 / GV80 comparisons. A second fit down-weights source bias. A third fit keeps only owners (no same-day testers). Upvotes are planned to be removed from all data and calculations — the `upvotes` column and the karma boost in the default fit are legacy.

## How to read it

Open `reports/composite_ranking.md` first. That file is the result: one composite chain plus segment rankings. `reports/bias_analysis.md` is the second reading — same quotes, less Reddit karma and brand-sub weight. `reports/owner_analysis.md` is the third — same quotes, **no test drivers**.

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

Core models with **three or more** coded appearances. Bradley–Terry θ and win–loss from the default fit (`python3 src/rank.py`). Raw θ still inflates cars that only beat same-class rivals (EQS SUV 9–1 vs iX/R1S, Escalade IQ 6–1 vs Model X, XT6 7–2, CX-9 8–0 vs Highlander/Pilot/RAV4). Use the chain above, not this numeric list, as a shopping order.

| Rank | Model | θ | W–L |
|---:|---|---:|---:|
| 1 | Mercedes EQS SUV | 5.43 | 9–1 |
| 2 | Mercedes GLS | 5.10 | 18–3 |
| 3 | Range Rover | 5.08 | 17–2 |
| 4 | Range Rover Sport | 3.97 | 12–3 |
| 5 | Lexus LX | 3.76 | 10–2 |
| 6 | Lincoln Aviator | 3.70 | 15–4 |
| 7 | Buick Enclave | 3.70 | 7–3 |
| 8 | Audi Q8 | 3.22 | 5–3 |
| 9 | Lincoln Nautilus | 3.21 | 15–3 |
| 10 | Cadillac Escalade IQ | 3.17 | 6–1 |
| 11 | BMW X5 | 3.13 | 36–50 |
| 12 | BMW iX | 3.12 | 11–7 |
| 13 | Cadillac XT6 | 3.12 | 7–2 |
| 14 | Cadillac Escalade | 2.70 | 17–15 |
| 15 | Mazda CX-9 | 2.66 | 8–0 |
| 16 | Genesis GV80 | 2.60 | 7–7 |
| 17 | Jeep Grand Cherokee | 2.53 | 3–2 |
| 18 | BMW X7 | 2.52 | 10–20 |
| 19 | Genesis GV70 | 2.32 | 14–4 |
| 20 | Lincoln Navigator | 2.21 | 12–12 |
| 21 | Lexus GX | 2.20 | 25–14 |
| 22 | Acura MDX | 2.20 | 9–4 |
| 23 | GMC Yukon | 2.19 | 21–5 |
| 24 | Jeep Grand Wagoneer | 2.19 | 7–6 |
| 25 | Mercedes GLE | 2.02 | 22–17 |
| 26 | Honda Pilot | 1.70 | 33–37 |
| 27 | Infiniti QX80 | 1.62 | 4–1 |
| 28 | Audi Q7 | 1.51 | 8–6 |
| 29 | Subaru Ascent | 1.48 | 22–9 |
| 30 | Lexus TX | 1.45 | 6–7 |
| 31 | Mercedes GLE AMG | 1.28 | 1–3 |
| 32 | Lincoln Corsair | 1.00 | 6–5 |
| 33 | Audi Q5 | 0.91 | 15–9 |
| 34 | Volvo XC90 | 0.85 | 16–13 |
| 35 | Lexus RX | 0.69 | 21–16 |
| 36 | Nissan Murano | 0.67 | 4–2 |
| 37 | Volkswagen Atlas | 0.65 | 11–5 |
| 38 | Subaru Outback 2026 | 0.55 | 12–1 |
| 39 | Volvo XC60 | 0.31 | 17–14 |
| 40 | Porsche Macan | 0.21 | 5–6 |
| 41 | Mercedes GLC | −0.06 | 7–6 |
| 42 | Toyota Sequoia | −0.09 | 3–13 |
| 43 | Lexus NX | −0.17 | 8–11 |
| 44 | Toyota Venza | −0.29 | 14–3 |
| 45 | Land Rover Defender | −0.29 | 10–13 |
| 46 | Honda CR-V | −0.58 | 22–19 |
| 47 | Nissan Pathfinder | −0.78 | 15–11 |
| 48 | Jeep Grand Cherokee L | −0.81 | 2–4 |
| 49 | Volkswagen Tiguan | −0.95 | 11–4 |
| 50 | Hyundai Palisade | −1.18 | 53–23 |
| 51 | Chevrolet Tahoe | −1.31 | 2–6 |
| 52 | Kia Telluride | −1.32 | 28–26 |
| 53 | Toyota Highlander | −1.60 | 9–23 |
| 54 | Toyota Grand Highlander | −1.66 | 5–14 |
| 55 | Cadillac XT5 | −1.96 | 1–9 |
| 56 | Subaru Outback (2020–25) | −2.02 | 31–16 |
| 57 | Ford Explorer | −2.11 | 4–6 |
| 58 | Honda Passport | −2.52 | 6–8 |
| 59 | Mazda CX-5 | −3.20 | 5–9 |
| 60 | Porsche Cayenne | −3.39 | 4–17 |
| 61 | Lexus GX 550 | −3.46 | 9–15 |
| 62 | Mazda CX-90 | −3.88 | 3–15 |
| 63 | Subaru Crosstrek | −3.95 | 4–14 |
| 64 | Tesla Model X | −4.06 | 11–16 |
| 65 | BMW X3 | −4.17 | 3–20 |
| 66 | Kia Sorento | −4.21 | 0–6 |
| 67 | Subaru Forester | −4.22 | 2–14 |
| 68 | Toyota Land Cruiser | −4.27 | 4–7 |
| 69 | Toyota 4Runner | −4.36 | 3–24 |
| 70 | Mazda CX-50 | −4.41 | 1–14 |
| 71 | Rivian R1S | −4.55 | 5–21 |
| 72 | Chevrolet Suburban | −4.89 | 0–6 |
| 73 | Toyota RAV4 | −5.04 | 1–32 |
| 74 | BMW X1 | −5.59 | 1–7 |
| 75 | Tesla Model Y | −8.01 | 0–16 |
