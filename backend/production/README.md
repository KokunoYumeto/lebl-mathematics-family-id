# Production backend checkpoints

## Public checkpoint U330

`v0.4-live-2026.08.24-u330-figfix-a/` is the authoritative checkpoint for
release U330. It binds the 330-row translation manifest, the 643-row
terminology ledger, and the localized Figure 11.6 derivative assets.

- 2,683 canonical records;
- 15 deterministic CSV projections;
- 26 files / 11,495,077 bytes;
- `records.jsonl` SHA-256
  `a072ad3b76864de53bd1a5802dd9aaee5f9067f2e63b192eafdc308bc9fff9bf`;
- input manifest SHA-256
  `c45f42524e598f724e5845c1a7e3c38b9c43de241dcae63b48870b2683d1b34b`;
- input terminology SHA-256
  `9192208da259eb7f0b7ab8dd9ceb7569ed0af8f1d90c27a349fd0e84c36ac463`.

The dataset passes schema and referential validation. Every CSV projection
round-trips to the exact canonical record set. An independent replay produced
the identical 26-file inventory SHA-256
`8c60d50e03a80441dcc5e73ba398ab37f1b258048cb34368d44d474296ac68df`;
that duplicate replay is intentionally omitted from the public repository and
source package.

## Preserved public checkpoint U319

`v0.4-live-2026.08.23-u319-tqa-a/` is the preserved checkpoint for release
U319. It binds the 319-row translation manifest and the 626-row
terminology ledger used after the field-terminology revalidation.

- 2,650 canonical records;
- 15 deterministic CSV projections;
- 26 files / 11,227,185 bytes;
- `records.jsonl` SHA-256
  `062f7e040cc79ac7b8c428bfd2b7149a831262402a69d46800242ae1efc01c29`;
- input manifest SHA-256
  `0718642d139d80c505605d6cd47d5f836ba15dd0bde7a7f02e344922fee4d703`;
- input terminology SHA-256
  `2e844ec82fa781b2fb3eb67deed21e55ab8c2dc25fcb2e609d46603f3a32e6aa`.

Its validation and replay evidence remain intact as release history.

## Baseline and builders

`v0.3/` is the retained hash-bound baseline: 167 units and 2,193 records.
`build_live_v04.py` extends that baseline with live manifest, terminology,
correction, and QA inputs. `build_production_v03.py` is retained as an
implementation reference for the earlier snapshot.

Do not treat an older checkpoint as current coverage and do not change only a
version constant. Any schema, envelope, or CSV-dialect change requires a new
version, a fresh independent replay, and complete validation/round-trip proof.
