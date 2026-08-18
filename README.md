# SUV Comfort Ranking from Customer Comparisons

Research project that ranks SUV comfort from **customer comments that compare two or more SUVs and state a preference**. Isolated praise ("the X5 is comfy") is not used. Only relative statements are.

## What this is

A Bradley–Terry ranking of current-generation SUVs on ride comfort, seats, cabin quiet, and long-trip fatigue, built from first-hand owner and test-drive comments on Reddit, X, and Edmunds/Cars.com consumer reviews. Collected 18 August 2026; expanded the same day through five research passes, the last aimed at remaining thin flagship / mid-luxury / compact-luxury / three-row / truck nodes. A second fit down-weights source bias. A third fit keeps only owners (no same-day testers).

## How to read it

Open `reports/composite_ranking.md` first. That file is the result: one composite chain plus segment rankings. `reports/bias_analysis.md` is the second reading — same quotes, less Reddit karma and brand-sub weight. `reports/owner_analysis.md` is the third — same quotes, **no test drivers**.

- `data/comparisons.csv` — coded pairwise votes
- `src/rank.py` — Bradley–Terry fit (default + bias-adjusted + owners)
- `data/ranking.csv` / `data/ranking_bias.csv` / `data/ranking_owners.csv` — machine-readable tables
- `reports/methodology.md` — inclusion rules, weighting, generation coding, limits, and how to read Edmunds/Cars.com when the live review page is blocked

```bash
python3 src/rank.py
```

## Mechanical ranking

Core models with **three or more** coded appearances. Bradley–Terry θ and win–loss from the default fit (`python3 src/rank.py`). Shopping-order chain, caveats, and who-met-whom are in `reports/composite_ranking.md`.

| Rank | Model | θ | W–L |
|---:|---|---:|---:|
| 1 | Range Rover | 5.28 | 9–1 |
| 2 | Mercedes GLS | 4.73 | 17–3 |
| 3 | Mercedes EQS SUV | 4.61 | 3–1 |
| 4 | Range Rover Sport | 4.14 | 9–1 |
| 5 | Lexus LX | 3.91 | 8–2 |
| 6 | Lincoln Aviator | 3.37 | 15–4 |
| 7 | Buick Enclave | 3.36 | 3–1 |
| 8 | BMW iX | 3.32 | 9–3 |
| 9 | Audi Q8 | 3.09 | 5–3 |
| 10 | BMW X5 | 2.84 | 22–39 |
| 11 | BMW X7 | 2.59 | 9–20 |
| 12 | Lexus RX | 2.39 | 19–16 |
| 13 | Cadillac Escalade | 2.30 | 13–8 |
| 14 | Lincoln Navigator | 2.30 | 10–11 |
| 15 | Lincoln Nautilus | 2.27 | 12–3 |
| 16 | Genesis GV80 | 2.24 | 7–7 |
| 17 | Jeep Grand Wagoneer | 2.00 | 5–4 |
| 18 | Acura MDX | 1.95 | 9–4 |
| 19 | Lexus TX | 1.92 | 6–7 |
| 20 | Genesis GV70 | 1.90 | 11–3 |
| 21 | Subaru Ascent | 1.68 | 22–9 |
| 22 | Mercedes GLE | 1.55 | 13–15 |
| 23 | Porsche Cayenne | 1.05 | 2–5 |
| 24 | Audi Q7 | 1.04 | 8–6 |
| 25 | Audi Q5 | 0.83 | 12–6 |
| 26 | Honda Pilot | 0.80 | 22–31 |
| 27 | Subaru Outback 2026 | 0.76 | 10–1 |
| 28 | Volkswagen Atlas | 0.51 | 10–4 |
| 29 | Toyota Venza | 0.45 | 7–2 |
| 30 | Mercedes GLC | 0.44 | 6–5 |
| 31 | Volvo XC90 | 0.42 | 14–13 |
| 32 | Volvo XC60 | 0.40 | 16–13 |
| 33 | Lexus NX | 0.10 | 7–9 |
| 34 | Lexus GX | 0.08 | 24–12 |
| 35 | Nissan Pathfinder | −0.03 | 11–6 |
| 36 | Honda CR-V | −0.33 | 20–15 |
| 37 | Tesla Model X | −0.51 | 3–8 |
| 38 | Hyundai Palisade | −0.61 | 44–18 |
| 39 | Kia Telluride | −1.09 | 23–20 |
| 40 | Toyota Grand Highlander | −1.32 | 4–13 |
| 41 | Mazda CX-90 | −1.37 | 1–6 |
| 42 | Subaru Outback (2020–25) | −1.47 | 19–15 |
| 43 | Toyota Highlander | −1.61 | 6–16 |
| 44 | Land Rover Defender | −1.66 | 2–3 |
| 45 | Honda Passport | −2.00 | 5–6 |
| 46 | Volkswagen Tiguan | −2.10 | 4–4 |
| 47 | Mazda CX-5 | −2.58 | 4–5 |
| 48 | Ford Explorer | −2.64 | 1–5 |
| 49 | BMW X3 | −3.16 | 1–16 |
| 50 | Rivian R1S | −3.26 | 0–6 |
| 51 | Lexus GX 550 | −3.43 | 9–11 |
| 52 | Kia Sorento | −3.86 | 0–5 |
| 53 | Mazda CX-50 | −3.87 | 1–14 |
| 54 | Toyota Land Cruiser | −3.95 | 3–4 |
| 55 | Toyota 4Runner | −4.26 | 2–21 |
| 56 | Toyota RAV4 | −4.39 | 1–21 |
| 57 | Subaru Forester | −4.71 | 0–8 |
| 58 | Tesla Model Y | −5.01 | 0–4 |
