# SUV Comfort Ranking from Customer Comparisons

Research project that ranks SUV comfort from **customer comments that compare two or more SUVs and state a preference**. Isolated praise ("the X5 is comfy") is not used. Only relative statements are.

## What this is

A Bradley–Terry ranking of current-generation SUVs on ride comfort, seats, cabin quiet, and long-trip fatigue, built from first-hand owner and test-drive comments on Reddit, X, and Edmunds/Cars.com consumer reviews. Collected 18 August 2026; expanded the same day through seven research passes, the last aimed at remaining thin flagship trucks (Yukon / Tahoe / Suburban / QX80 / Sequoia), mid-luxury (Defender / R1S / Cayenne / Grand Cherokee), compact (Crosstrek / Corsair / X1 / Model Y / Murano), and three-row (CX-90 / Explorer / Enclave / GCL) nodes. A second fit down-weights source bias. A third fit keeps only owners (no same-day testers).

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

Core models with **three or more** coded appearances. Bradley–Terry θ and win–loss from the default fit (`python3 src/rank.py`). Shopping-order chain, caveats, and who-met-whom are in `reports/composite_ranking.md`. Raw θ still inflates cars that only beat same-class rivals (EQS SUV 5–1 vs iX, XT6 7–2, CX-9 8–0 vs Highlander/Pilot/RAV4). Use the chain, not this numeric list, as a shopping order.

| Rank | Model | θ | W–L |
|---:|---|---:|---:|
| 1 | Mercedes GLS | 5.02 | 17–3 |
| 2 | Mercedes EQS SUV | 4.99 | 5–1 |
| 3 | Range Rover | 4.98 | 14–2 |
| 4 | Range Rover Sport | 3.72 | 12–3 |
| 5 | Lexus LX | 3.70 | 8–2 |
| 6 | Buick Enclave | 3.69 | 6–3 |
| 7 | Lincoln Aviator | 3.66 | 15–4 |
| 8 | Audi Q8 | 3.10 | 5–3 |
| 9 | Cadillac XT6 | 3.06 | 7–2 |
| 10 | BMW iX | 3.00 | 10–5 |
| 11 | Lincoln Nautilus | 2.93 | 13–3 |
| 12 | BMW X5 | 2.90 | 28–47 |
| 13 | Cadillac Escalade | 2.86 | 17–13 |
| 14 | Mazda CX-9 | 2.69 | 8–0 |
| 15 | Genesis GV80 | 2.53 | 7–7 |
| 16 | BMW X7 | 2.45 | 10–20 |
| 17 | Genesis GV70 | 2.32 | 13–4 |
| 18 | Jeep Grand Wagoneer | 2.23 | 7–6 |
| 19 | Lincoln Navigator | 2.21 | 12–12 |
| 20 | GMC Yukon | 2.17 | 19–5 |
| 21 | Lexus GX | 2.16 | 24–14 |
| 22 | Acura MDX | 2.10 | 9–4 |
| 23 | Mercedes GLE | 1.93 | 21–16 |
| 24 | Infiniti QX80 | 1.68 | 4–1 |
| 25 | Subaru Ascent | 1.65 | 22–9 |
| 26 | Honda Pilot | 1.63 | 33–37 |
| 27 | Lexus TX | 1.46 | 6–7 |
| 28 | Lincoln Corsair | 1.42 | 6–3 |
| 29 | Audi Q7 | 1.41 | 8–6 |
| 30 | Audi Q5 | 1.30 | 15–7 |
| 31 | Nissan Murano | 0.83 | 3–2 |
| 32 | Volkswagen Atlas | 0.77 | 11–5 |
| 33 | Volvo XC90 | 0.74 | 16–13 |
| 34 | Subaru Outback 2026 | 0.71 | 11–1 |
| 35 | Jeep Grand Cherokee | 0.68 | 1–2 |
| 36 | Lexus RX | 0.60 | 21–16 |
| 37 | Volvo XC60 | 0.53 | 17–14 |
| 38 | Mercedes GLC | 0.24 | 6–6 |
| 39 | Lexus NX | 0.08 | 8–11 |
| 40 | Toyota Sequoia | 0.08 | 3–11 |
| 41 | Toyota Venza | −0.18 | 8–3 |
| 42 | Porsche Macan | −0.24 | 3–5 |
| 43 | Honda CR-V | −0.51 | 21–18 |
| 44 | Nissan Pathfinder | −0.60 | 15–11 |
| 45 | Land Rover Defender | −0.74 | 4–11 |
| 46 | Hyundai Palisade | −0.78 | 53–22 |
| 47 | Kia Telluride | −1.02 | 28–25 |
| 48 | Chevrolet Tahoe | −1.17 | 2–5 |
| 49 | Volkswagen Tiguan | −1.18 | 7–4 |
| 50 | Rivian R1S | −1.33 | 5–14 |
| 51 | Toyota Highlander | −1.39 | 9–23 |
| 52 | Toyota Grand Highlander | −1.41 | 5–14 |
| 53 | Subaru Outback (2020–25) | −1.65 | 29–15 |
| 54 | Ford Explorer | −1.96 | 4–6 |
| 55 | Tesla Model X | −1.99 | 11–12 |
| 56 | Cadillac XT5 | −2.18 | 0–9 |
| 57 | Honda Passport | −2.50 | 6–8 |
| 58 | Mazda CX-5 | −2.77 | 5–7 |
| 59 | Chevrolet Suburban | −3.27 | 0–6 |
| 60 | Porsche Cayenne | −3.35 | 4–13 |
| 61 | BMW X3 | −3.43 | 2–17 |
| 62 | Mazda CX-90 | −3.63 | 3–15 |
| 63 | Subaru Forester | −3.73 | 2–11 |
| 64 | Lexus GX 550 | −3.74 | 9–13 |
| 65 | Kia Sorento | −4.00 | 0–6 |
| 66 | Mazda CX-50 | −4.09 | 1–14 |
| 67 | Toyota Land Cruiser | −4.27 | 3–4 |
| 68 | Subaru Crosstrek | −4.38 | 2–12 |
| 69 | Toyota RAV4 | −4.50 | 1–25 |
| 70 | Toyota 4Runner | −4.65 | 2–23 |
| 71 | BMW X1 | −4.68 | 1–5 |
| 72 | Jeep Grand Cherokee L | −5.24 | 0–4 |
| 73 | Tesla Model Y | −6.25 | 0–12 |
