# Production Backend Checkpoints

This directory contains two append-only production checkpoints for the bounded
R006/R007/R008 Lebl-family lane.

## Retained v0.1 history

The top-level `dataset.json`, `records.jsonl`, `csv/`,
`frozen_translation_manifest_through_notation.jsonl`,
`frozen_translation_manifest_through_real_numbers.jsonl`, and
`frozen_adverse_ledger_through_0005.jsonl` are the retained 19-manifest-unit
v0.1 checkpoint. They remain unchanged historical evidence. The v0.1 stream
contains 210 records and has SHA-256
`bbd5fb1e24a875c1fcc0b7f7311c9e811426cd3c76c14f3cf638338447488a8e`.

## Current v0.2 checkpoint

`v0.2/` is bound to these exact frozen inputs:

- 26-row translation manifest: 29,512 bytes,
  `0e6ab45a456935dd7a5a5c294aa4b47e34fa5ecc90b1f66127d3f3fd9f9e62b1`.
- terminology through `LEBL-TERM-0129`: 16,312 bytes,
  `09c2000bc1133b3065a713e3b532b20000ab6905bb5ae4f5f3d7d47ec80e2b58`.
- adverse ledger through `LEBL-ID-ADV-0009`: 7,194 bytes,
  `361666e2dbf419282428e07a5ca3b8520d25aecc1d12a8a78a1583b919c9d148`.
- exact checkpoint receipt: 6,353 bytes,
  `a1269c6a592ccc4eb28b338ce9f8cc8fef0497eb1c3bf6c7d8e4cf99f6d63d80`.

The v0.2 canonical stream contains 526 records in 1,116,969 bytes and has
SHA-256 `c0e97748bda5d50be56e0799362dd47e08861c68334c9b4a39d1d301871db06c`.
It includes exactly one unit record for each frozen manifest row, six retained
dense child units, every admitted terminology-ledger row, all nine correction
events, two localized figure assets, and typed QA metrics for the converter
(0 errors, 672 unique IDs, 952 resolving xrefs) and the 318-page PDF
checkpoint.

`v0.2/VALIDATION.json` records JSON Schema validation, referential integrity,
15 deterministic CSV projections, and lossless 526-record CSV round-trip
recovery. `V02_IDEMPOTENCE_RECEIPT.md` records the independent two-build byte
comparison. The QA CSV exposes typed metric columns as well as the lossless
`record_json` field.

Rebuild with the bounded generator:

```powershell
python .\build_production_v02.py --out .\v0.2
```

The generator reads the frozen v0.2 inputs, retained v0.1 record stream, named
R006 selectors, and local backend schemas/tools only. It does not use Git,
network access, or build the books.

