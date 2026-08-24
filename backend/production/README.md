# Production backend checkpoints

## Public checkpoint U319

`v0.4-live-2026.08.23-u319-tqa-a/` is the authoritative live checkpoint for
release U319. It binds the 319-row translation manifest and the 626-row
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

The dataset passes schema and referential validation. Every CSV projection
round-trips to the exact canonical record set. An independent replay produced
an identical 26-file inventory; that duplicate replay is intentionally omitted
from the public repository and source package.

## Baseline and builders

`v0.3/` is the retained hash-bound baseline: 167 units and 2,193 records.
`build_live_v04.py` extends that baseline with live manifest, terminology,
correction, and QA inputs. `build_production_v03.py` is retained as an
implementation reference for the earlier snapshot.

Do not treat an older checkpoint as current coverage and do not change only a
version constant. Any schema, envelope, or CSV-dialect change requires a new
version, a fresh independent replay, and complete validation/round-trip proof.
