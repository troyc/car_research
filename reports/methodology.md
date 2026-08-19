# Methodology

## Question and estimand

Among the collected online statements in which someone compared at least two SUVs from first-hand experience and chose a comfort winner, what ordering is implied?

The result describes **this collected corpus**. It is not a random sample of owners or shoppers, and its resampling intervals must not be read as population confidence intervals. Statements with no preference or a tie were not collected, so every estimate is conditional on an expressed preference.

Comfort is coded as ride isolation, seats, cabin noise/vibration/harshness (NVH), explicit long-trip fatigue, or an overall comfort judgment. Handling, styling, reliability, and prestige do not count unless the author explicitly connects them to comfort.

## Primary inclusion rules

A primary observation must:

1. Name a winner and loser that are SUVs/crossovers in the coded generation.
2. State or directly imply a preference on a supported comfort axis.
3. Come from first-hand exposure: owned/lived with, rented or borrowed, test-drove, rode in, or regularly used a family vehicle.
4. Be recoverable from one source statement or its necessary reply-chain context.

The primary analysis excludes `opinion`, `opinion_plus_drive`, `journalist`, `exclude`, the two non-SUV context rows, and the two `interior` rows. Those records remain in `data/comparisons.csv` for provenance. Reddit/X scores and the legacy `weight_base` field are not used.

## Observation unit and dependence

The raw CSV is not a file of independent people. A single post can rank several cars, discuss several axes, and create several pairwise rows. The audit backfill therefore adds:

- `statement_id` — source post, comment, or review unit;
- `respondent_id` — deterministic, privacy-preserving author cluster;
- `thread_id` — conversation/source-page cluster;
- `community_affinity` — whether a brand community favors the winner, loser, another model, or neither;
- `collection_batch` — the historical collection pass.

Within a statement, exact duplicate pair-axis judgments are removed. Each retained statement receives total mass 1, divided equally over its distinct pair-axis judgments. Repeated same-direction judgments by one respondent about the same pair and axis collapse to the earliest coded statement. If the same respondent expresses both directions for the same pair and axis, neither direction enters the primary composite.

This prevents a six-car comparison from automatically counting like many independent people. Different statements by the same respondent may still contain new comparisons, so uncertainty is resampled by respondent rather than row.

## Bradley–Terry model

For model scores \(\theta_i\) and \(\theta_j\),

\[
P(i \succ j) = \frac{e^{\theta_i}}{e^{\theta_i}+e^{\theta_j}}.
\]

The analysis minimizes the weighted negative log likelihood plus a weak independent normal prior,

\[
\theta_i \sim N(0, 2.5^2).
\]

This is a regularized maximum-a-posteriori estimate, not unpenalized maximum likelihood. Regularization keeps undefeated and weakly connected models finite. Prior standard deviations 1.5 and 5.0 are reported as sensitivity fits.

`scipy.optimize.minimize` fits the model with an analytic gradient. L-BFGS is followed by a positive-definite Newton refinement when necessary. Every published fit must have finite scores and maximum absolute gradient below `1e-6`; otherwise generation fails.

The readable score is

\[
P(\text{model beats average}) = \operatorname{logit}^{-1}(\theta_i),
\]

where the average model has \(\theta=0\) in that fit. This probability is model-based and corpus-specific.

## Global and segment fits

The global fit uses all primary comparisons. It answers the project-wide question, but its cross-class ordering depends on the comparisons that connect shopping segments.

Four separate segment fits use only comparisons with both models in the same segment:

- compact / small-mid;
- midsize luxury;
- three-row family;
- flagship / large.

Each segment is centered independently. A 70% score in one segment is **not** directly comparable with 70% in another segment.

For each scope, the comparison graph is checked before ranking. A model receives an ordinal rank only if it:

- belongs to the scope's largest connected component;
- has at least five respondent clusters; and
- has at least three distinct opponents.

Other models remain in machine outputs with `disconnected`, `insufficient_respondents`, or `insufficient_opponents` status.

## Stability intervals

The primary global and segment tables use 2,000 respondent-cluster bootstrap refits with seed `20260819`. Each replicate samples respondents with replacement and keeps all of that respondent's statements together. Tables report the 5th–95th percentile score and rank ranges; rank endpoints are rounded outward.

An additional 1,000 refits resample whole threads. These measure sensitivity to correlated discussion and influential source pages. They do not repair purposive sampling or justify population inference.

## Sensitivity analyses

`data/ranking_sensitivity.csv` contains:

- owners only and lived-with-both only;
- neutral/non-brand communities only;
- `home_team=1` observations excluded (same-team wins);
- Reddit only and consumer-review sites only;
- the former evidence/home-team weights, labeled `legacy_weights`;
- prior scales 1.5 and 5.0;
- ride, seats, NVH, long-trip, and overall axes separately;
- leave-one-collection-batch-out fits; and
- thread-cluster stability intervals.

The old “bias-adjusted” label is retired. The old multipliers were subjective reliability choices, not a statistical correction for selection bias. Source restrictions are now presented as scenarios.

## Diagnostics

The generated diagnostic report includes:

- connected components, unique opponents, graph bridges, and cross-segment comparison mass;
- five-fold respondent-grouped predictive log loss and Brier score against an even-odds baseline;
- leave-one-thread-out rank influence; and
- supported direct pairs that disagree most with the one-dimensional global scale.

Large pair residuals are expected when “comfort” means different things to different people. The direct-matchup figure therefore separates ride, seats, NVH, long-trip, and overall mass.

## Important limitations

- Collection was purposive and expanded around thin models; inclusion probabilities are unknown.
- Reddit dominates the corpus, and brand communities influence which comparisons are discussed.
- Owner switchers can justify a purchase; short test drives can overemphasize first impressions.
- Wheel size, tires, air suspension, trim, model year, roads, and body shape can matter as much as a nameplate average.
- A single latent comfort score cannot fully represent people who prefer one car's ride and another car's seats.
- Review-site fallbacks do not always expose a stable author identifier; unresolved authors are conservatively treated as separate respondent clusters.
- Rank intervals express corpus stability, not a probability that a vehicle holds a population rank.

## Reproduce

```bash
# numpy + scipy
python3 src/rank.py

# matplotlib + numpy; consumes only generated analysis outputs
python3 src/plot.py

# fast statistical tests
pytest -q
```

On Nix:

```bash
nix-shell -p python3Packages.numpy python3Packages.scipy --run "python3 src/rank.py"
nix-shell -p python3Packages.matplotlib python3Packages.numpy --run "python3 src/plot.py"
```

The first command generates the global, segment, sensitivity, primary-observation, summary, ranking-report, and diagnostic files. Use `python3 src/rank.py --check` to verify that tracked statistical outputs match the current data and fixed seed. Collection history and the retired hand-authored chain are preserved in [`collection_history.md`](collection_history.md).
