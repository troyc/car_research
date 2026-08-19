# Staged comparison collection

This directory contains new, independently auditable comparison rows that have
not yet been merged into `data/comparisons.csv`. Collection here must not change
the parent dataset or generated ranking outputs.

## Inclusion standard

Keep only a first-person owner, family-car, loaner/rental, passenger, or
test-drive passage that identifies at least two SUVs and expresses a winner on
one of the existing axes: `ride`, `seats`, `nvh`, `long_trip`, or `overall`.
The winner, loser, axis, and evidence must be supported by one post or by its
direct reply context. Do not include professional reviews, aggregate scores,
unsupported opinions, ties, or ambiguous generations.

Use the smallest verbatim excerpt that proves the judgment. Never store forum
usernames: `respondent_id` is a deterministic truncated SHA-256 digest of the
lower-cased source name and username. Raw page snapshots belong under
`more-data/raw/`, which is gitignored.

## Round layout

Each `round_*` directory contains:

- `comparisons.csv` — the exact 16-column parent schema, ready for a later merge.
- `context.csv` — generation, trim, suspension, source-record, and extraction
  details keyed by comparison ID.
- `rejections.csv` — reviewed passages that were rejected, preventing repeated
  work in later rounds.
- `audit.md` — queries, access checks, inclusion decisions, coverage gains, and
  unresolved targets.

The required `comparisons.csv` header is:

```text
id,winner,loser,weight_base,upvotes,source,evidence,home_team,comfort_axis,quote,url,statement_id,respondent_id,thread_id,community_affinity,collection_batch
```

The required `context.csv` header is:

```text
id,source_record_id,published_at,winner_model_year,loser_model_year,winner_trim,loser_trim,generation_notes,wheel_tire_suspension,ownership_context,road_context,extraction_method,snapshot_path,audit_status
```

The required `rejections.csv` header is:

```text
source,url,source_record_id,reason,notes
```

Row IDs are deterministic four-character lowercase alphanumeric strings and
must not collide with the parent dataset or an earlier round. `statement_id`
uses the source/thread/post identity, `thread_id` uses the source/thread
identity, and repeated posts by the same person reuse the same
`respondent_id`. Multi-pair statements may produce several rows with the same
statement and respondent IDs.

Use the existing evidence-to-weight mapping even though the primary analysis
normalizes statement mass:

| Evidence | Weight |
|---|---:|
| `owned_both` | 3.0 |
| `test_drove_both` | 2.0 |
| `owned_one_td_other` | 1.5 |
| `owned_one_family` | 1.5 |
| `owned_one_loaner` | 1.5 |
| `owned_one_rode_other` | 1.5 |
| `passenger` | 1.0 |

Brand forums use `community_affinity=winner`, `loser`, or `other` according to
which side matches the forum badge. General forums use `neutral`.

## Collection procedure

1. Read `source_registry.csv` and re-check the source's current robots file and
   terms before collecting. Never bypass authentication, CAPTCHAs, proof-of-work
   challenges, or disallowed endpoints.
2. Discover targeted public threads through ordinary web search. Do not crawl
   search, member, login, profile, or API endpoints.
3. Review candidates in batches of 25 threads. Retire a source after two
   consecutive batches each yield fewer than five qualified statements.
4. Deduplicate against the parent CSV and all earlier rounds by source post,
   then by respondent, unordered pair, and axis.
5. Run `python3 more-data/validate.py` before handing off a round.

## Priority gaps

Prioritize withheld models (`Infiniti QX80`, `Jeep Grand Cherokee`, `Hyundai
Santa Fe`, and `Kia Sorento`), long-trip evidence, cross-segment statements,
and the sparse/high-residual pairs X5–RX, Defender–XC90, X5–GV80,
Palisade–Pathfinder, GV70–Macan, GX 550–Land Cruiser, Palisade–CX-90,
Palisade–Grand Highlander, Enclave–Palisade, Highlander–Venza,
Corsair–Nautilus, X5–X7, NX–Corsair, Pilot–Pathfinder, and TX–Aviator.

## Validation

```bash
python3 more-data/validate.py
python3 more-data/report.py
```

If NumPy/SciPy are not installed in the active Python environment:

```bash
nix-shell -p python3Packages.numpy python3Packages.scipy \
  --run "python3 more-data/validate.py && python3 more-data/report.py"
```

The validator checks schemas, IDs, model names, evidence weights, metadata,
context coverage, cross-round duplication, and in-memory compatibility with the
existing observation builder. It never writes the combined dataset.
`report.py` prints retained-observation, long-trip, cross-segment, withheld-model,
and priority-pair gains from the same in-memory combination.
