# SUV Comfort Ranking from Customer Comparisons

This repository ranks SUV comfort from first-hand online comments that name two or more vehicles and pick a winner on ride, seats, cabin quietness, long-trip fatigue, or overall comfort, by coding those pairwise judgments and fitting a regularized Bradley–Terry model.

## Rankings within shopping segments

Each panel is a separate fit using only comparisons inside that segment. Scores and ranks must not be compared across panels. Open `†` entries lack five respondents or three opponents and do not receive an ordinal rank.

![Four within-segment SUV comfort rankings with 90% stability intervals](reports/figures/segment_rankings.png)

| Segment | Point-estimate leaders | Main caution |
|---|---|---|
| Flagship / large | Yukon, Grand Wagoneer, Navigator, Escalade, GLS, Range Rover | Only 72 within-segment statements; most intervals span several ranks. |
| Midsize luxury | Aviator, Q7, MDX, iX, Range Rover Sport, GLE, GV80 | Comfort remains multidimensional; direct X5–RX and X5–GV80 residuals are large. |
| Three-row family | Atlas, Palisade, Enclave, Pathfinder, Ascent, Pilot, Telluride | Palisade has far more support than the other point leaders. |
| Compact / small-mid | Nautilus, 2026 Outback, Q5, Macan, Venza, XC60, Corsair | CX-9 lacks enough within-segment coverage despite its global point rank. |

The [full segment tables](reports/rankings.md#within-segment-rankings) include probability, rank ranges, support, and withheld models.

## What people compared directly

The chart below uses only the filtered primary observations—never model-implied wins. Each statement has total mass one, split across its coded judgments, so totals can be fractional.

![Best-supported direct SUV comfort matchups split into ride, seat, NVH, long-trip, and overall judgments](reports/figures/direct_matchups.png)

Among the best-supported pairs, GLS is 11–0 in normalized statement mass against X7, Venza is 9–0 against RAV4, GX 460 is 8–0 against 4Runner, and Palisade is 7.2–1 against Pilot. The axis breakdown matters—Escalade versus Navigator, for example, splits ride from seats.

## Global ranking

Dots are regularized Bradley–Terry point estimates. Lines are 90% respondent-cluster resampling intervals. The right annotation is `respondents · opponents`; four models below the minimum coverage rule are not assigned a rank.

![Global SUV comfort point rankings with wide 90% stability intervals](reports/figures/global_rank_stability.png)

The first ten point ranks show why the interval belongs next to the number. Range Rover and GLS sit at the top, but their 90% rank ranges still run into the mid-teens. CX-9 is the clearest warning against reading point rank as a podium: six respondent clusters compared it with five mostly mainstream opponents, and its stability range is 2–21.

| Rank | Model | Modeled P vs average | 90% rank range | Respondents | Opponents |
|---:|---|---:|---:|---:|---:|
| 1 | Range Rover | 92% | 1–16 | 16 | 8 |
| 2 | Mercedes GLS | 92% | 1–15 | 19 | 9 |
| 3 | Mercedes EQS SUV | 91% | 1–26 | 8 | 3 |
| 4 | Mazda CX-9 | 91% | 2–21 | 6 | 5 |
| 5 | Cadillac Escalade IQ | 90% | 1–27 | 6 | 4 |
| 6 | GMC Yukon | 88% | 2–24 | 24 | 11 |
| 7 | Lincoln Nautilus | 87% | 1–24 | 16 | 9 |
| 8 | Buick Enclave | 86% | 2–31 | 8 | 5 |
| 9 | Cadillac XT6 | 86% | 2–33 | 9 | 6 |
| 10 | Volkswagen Atlas | 85% | 2–29 | 15 | 5 |

`P vs average` is the model's estimate of how often this vehicle would be preferred to an average vehicle **in this corpus**. See the [complete generated global table](reports/rankings.md#global-ranking), including the four models whose coverage was withheld.

## What this can and cannot answer

The estimand is the ordering implied by the collected statements in which someone compared at least two SUVs from first-hand experience and chose a comfort winner. It is not a representative survey of SUV owners. Statements with no preference or a tie were not collected, so every estimate is conditional on an expressed preference. Stability intervals describe this corpus under respondent resampling, not uncertainty for all owners.

| Primary analysis | Count |
|---|---:|
| Coded source rows | 790 |
| Retained pair-axis judgments | 731 |
| Source statements | 651 |
| Respondent clusters | 628 |
| Models in the connected global graph | 77 |
| Respondent bootstrap refits | 2,000 |

Reddit supplies 653 of the 731 retained observations; Edmunds and Cars.com consumer reviews supply most of the rest. Ride is the most common axis (343), then seats (141), NVH (136), overall (95), and explicit long-trip fatigue (16).

## How the analysis works

1. Keep first-hand owner, family-car, rental/loaner, passenger, and test-drive comparisons; exclude thin opinion, journalist, non-SUV, and unsupported-axis rows.
2. Match rows back to source statements and privacy-preserving respondent clusters. A multi-car comment receives total mass one rather than counting like several independent people.
3. Fit regularized global and within-segment Bradley–Terry models with a weak `Normal(0, 2.5²)` score prior and a converged SciPy optimizer.
4. Resample respondents 2,000 times for the displayed 90% stability intervals, and resample threads 1,000 times as a discussion-clustering sensitivity check.
5. Withhold ordinal rank unless a model has five respondent clusters, three opponents, and membership in the scope's main connected component.

The primary fit gives statements equal influence. Former evidence-quality and home-team multipliers are retained only as a `legacy_weights` sensitivity scenario; they are not described as a bias correction.

[Source sensitivity](reports/figures/sensitivity.png) compares probabilities under the primary, owners-only, and neutral-forum samples. The [coverage graph](reports/figures/coverage_graph.png) shows which direct pairings hold the global scale together.

Read the [methodology](reports/methodology.md), [model diagnostics](reports/model_diagnostics.md), and [machine-readable sensitivity table](data/ranking_sensitivity.csv) for the full specification.

## Reproduce it

```bash
# numpy + scipy; writes rankings, intervals, diagnostics, and generated reports
python3 src/rank.py

# matplotlib + numpy; reads only the generated analysis outputs
python3 src/plot.py

# fast statistical tests
pytest -q
```

On Nix:

```bash
nix-shell -p python3Packages.numpy python3Packages.scipy --run "python3 src/rank.py"
nix-shell -p python3Packages.matplotlib python3Packages.numpy --run "python3 src/plot.py"
```

Useful options:

```bash
python3 src/rank.py --bootstrap-reps 2000 --seed 20260819
python3 src/rank.py --check
python3 src/plot.py --only segment_rankings direct_matchups
```

## Repository map

- [`data/comparisons.csv`](data/comparisons.csv) — audited coded rows with statement/respondent/thread/batch metadata
- [`data/analysis_observations.csv`](data/analysis_observations.csv) — generated primary observations and normalized analysis weights
- [`data/ranking.csv`](data/ranking.csv) / [`data/ranking_segments.csv`](data/ranking_segments.csv) — global and within-segment results
- [`src/rank.py`](src/rank.py) / [`src/plot.py`](src/plot.py) — analysis and visualization pipeline
- [`audit/`](audit/) — source snapshots, verification, and metadata backfill tools
- [`reports/collection_history.md`](reports/collection_history.md) — archived nine-pass narrative and retired hand-authored chain

## Limits worth keeping in view

- This was purposive collection, expanded around thin models; sampling probabilities are unknown.
- Reddit supplies most observations, and brand communities shape what gets discussed.
- Statements without a winner are absent. The model estimates preferences conditional on someone expressing one.
- Wheel size, tires, air suspension, trim, generation, road, and body shape can flip a nameplate comparison.
- “Comfort” combines ride, seats, NVH, fatigue, and overall judgments; one latent score cannot capture every tradeoff.
- Stability intervals describe this corpus under respondent resampling, not uncertainty for all SUV owners.
