# SUV Comfort Ranking from Customer Comparisons

Research project that ranks SUV comfort from **customer comments that compare two or more SUVs and state a preference**. Isolated praise ("the X5 is comfy") is not used. Only relative statements are.

## What this is

A Bradley–Terry ranking of current-generation SUVs on ride comfort, seats, cabin quiet, and long-trip fatigue, built from first-hand owner and test-drive comments on Reddit, X, and Edmunds/Cars.com consumer reviews. Collected 18 August 2026; expanded the same day through six research passes, the last aimed at remaining thin flagship (Yukon / Tahoe / Suburban / QX80 / Escalade IQ), mid-luxury (EQS SUV / Defender / R1S / Cayenne / Macan), compact (Crosstrek / Corsair / X1 / Model Y), and three-row (CX-90 / Pathfinder / Murano / Passport) nodes. A second fit down-weights source bias. A third fit keeps only owners (no same-day testers).

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

Core models with **three or more** coded appearances. Bradley–Terry θ and win–loss from the default fit (`python3 src/rank.py`). Shopping-order chain, caveats, and who-met-whom are in `reports/composite_ranking.md`. Raw θ still inflates cars that only beat same-class rivals (EQS SUV 5–1 vs iX, XT6 5–2 after one X5 Edmunds win, CX-9 5–0 vs Highlander/RAV4). Use the chain, not this numeric list, as a shopping order.

| Rank | Model | θ | W–L |
|---:|---|---:|---:|
| 1 | Mercedes EQS SUV | 5.13 | 5–1 |
| 2 | Range Rover | 4.98 | 9–1 |
| 3 | Mercedes GLS | 4.68 | 17–3 |
| 4 | Lexus LX | 3.95 | 8–2 |
| 5 | Buick Enclave | 3.42 | 4–2 |
| 6 | Lincoln Aviator | 3.38 | 15–4 |
| 7 | BMW iX | 3.16 | 10–5 |
| 8 | Audi Q8 | 3.07 | 5–3 |
| 9 | BMW X5 | 3.07 | 24–40 |
| 10 | Range Rover Sport | 2.93 | 10–3 |
| 11 | Cadillac XT6 | 2.76 | 5–2 |
| 12 | BMW X7 | 2.53 | 9–20 |
| 13 | Lincoln Nautilus | 2.53 | 13–3 |
| 14 | Lexus RX | 2.50 | 20–16 |
| 15 | Genesis GV70 | 2.22 | 13–3 |
| 16 | Cadillac Escalade | 2.21 | 16–11 |
| 17 | Genesis GV80 | 2.20 | 7–7 |
| 18 | Acura MDX | 2.01 | 9–4 |
| 19 | Lexus TX | 1.98 | 6–7 |
| 20 | Lincoln Navigator | 1.96 | 12–12 |
| 21 | Subaru Ascent | 1.73 | 22–9 |
| 22 | Jeep Grand Wagoneer | 1.46 | 7–6 |
| 23 | Infiniti QX80 | 1.35 | 2–1 |
| 24 | Mazda CX-9 | 1.34 | 5–0 |
| 25 | Mercedes GLE | 1.30 | 14–15 |
| 26 | Honda Pilot | 1.22 | 29–32 |
| 27 | GMC Yukon | 1.22 | 8–5 |
| 28 | Audi Q7 | 1.19 | 8–6 |
| 29 | Lincoln Corsair | 1.10 | 5–3 |
| 30 | Audi Q5 | 1.08 | 14–7 |
| 31 | Volkswagen Atlas | 0.71 | 11–5 |
| 32 | Volvo XC90 | 0.69 | 15–13 |
| 33 | Subaru Outback 2026 | 0.64 | 11–1 |
| 34 | Volvo XC60 | 0.42 | 17–13 |
| 35 | Toyota Sequoia | 0.16 | 2–7 |
| 36 | Mercedes GLC | 0.15 | 6–6 |
| 37 | Lexus GX | 0.10 | 24–12 |
| 38 | Lexus NX | −0.13 | 7–11 |
| 39 | Toyota Venza | −0.15 | 8–3 |
| 40 | Porsche Macan | −0.27 | 3–5 |
| 41 | Nissan Pathfinder | −0.44 | 14–8 |
| 42 | Honda CR-V | −0.50 | 20–18 |
| 43 | Land Rover Defender | −0.52 | 4–5 |
| 44 | Hyundai Palisade | −0.55 | 48–19 |
| 45 | Kia Telluride | −1.15 | 24–21 |
| 46 | Toyota Highlander | −1.22 | 8–21 |
| 47 | Tesla Model X | −1.25 | 7–10 |
| 48 | Porsche Cayenne | −1.27 | 2–8 |
| 49 | Volkswagen Tiguan | −1.40 | 6–4 |
| 50 | Toyota Grand Highlander | −1.47 | 4–14 |
| 51 | Chevrolet Tahoe | −1.69 | 1–2 |
| 52 | Subaru Outback (2020–25) | −1.72 | 23–15 |
| 53 | Rivian R1S | −1.80 | 2–9 |
| 54 | Mazda CX-90 | −1.82 | 2–11 |
| 55 | Cadillac XT5 | −2.14 | 0–7 |
| 56 | Honda Passport | −2.37 | 5–8 |
| 57 | Ford Explorer | −2.66 | 1–5 |
| 58 | Chevrolet Suburban | −2.75 | 0–5 |
| 59 | Mazda CX-5 | −2.77 | 4–5 |
| 60 | BMW X3 | −3.05 | 2–16 |
| 61 | Subaru Crosstrek | −3.21 | 2–5 |
| 62 | Lexus GX 550 | −3.33 | 9–12 |
| 63 | Toyota Land Cruiser | −3.88 | 3–4 |
| 64 | Kia Sorento | −4.04 | 0–6 |
| 65 | Mazda CX-50 | −4.12 | 1–14 |
| 66 | Toyota 4Runner | −4.21 | 2–21 |
| 67 | Jeep Grand Cherokee L | −4.25 | 0–3 |
| 68 | Toyota RAV4 | −4.28 | 1–23 |
| 69 | Subaru Forester | −4.84 | 0–9 |
| 70 | Tesla Model Y | −5.35 | 0–7 |
| 71 | BMW X1 | −5.47 | 0–5 |
