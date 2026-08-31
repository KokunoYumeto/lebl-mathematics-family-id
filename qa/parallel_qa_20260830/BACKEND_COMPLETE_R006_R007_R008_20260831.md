# Complete Lebl-family modular backend — R006/R007/R008

Status: PASS

Date: 2026-08-31  
Scope: canonical Bahasa Indonesia TeX readers and build-support TeX for Basic
Analysis I–II (R006), Notes on Diffy Qs (R007), and Guide to Cultivating
Complex Analysis (R008). The three resources retain separate resource,
edition, rights, provenance, and source/target identities.

## Frozen manifest

- Path: `translation/TRANSLATION_MANIFEST.jsonl`
- Rows: 5,884
- Bytes: 7,243,891
- SHA-256: `5e7b4805fa96115b60e52c5f602633985d3464ce2faed9b0eadf2edfcc98f7be`
- Canonical whole-file closure: 32 target TeX files — R006 17, R007 13,
  R008 2 — each paired with a directly resolvable source/target full-file
  selector and exact SHA-256.
- Dense logical index: 5,420 units — R006 2,264, R007 1,681, R008 1,475.
- Logical kinds: 37 chapters, 171 sections, 516 subsections, 181 definitions,
  184 theorems, 44 lemmas, 317 propositions, 68 corollaries, 415 proofs,
  404 examples, 2,169 exercises, 290 hint/note units, 251 R007 solution
  blocks, 329 figures, 7 tables, and 37 remarks.
- Every generated logical unit uses a persisted locale-neutral token, exact
  source/target raw-line locators and hashes, typed parent linkage, and a
  resource-specific rights identifier. Exercise records include explicit
  response/answer/solution-state metadata rather than invented answers.
- Two obsolete state values (`structurally_verified_checkpoint_build` and
  `structurally_verified_build_pending`) were normalized to
  `structurally_verified`; no state contains `pending`, `checkpoint`, `draft`,
  or `partial`.
- Rights remain separate: `rights.ra.book.cc-by-sa-4.0`,
  `rights.diffyqs.book.cc-by-sa-4.0`, and
  `rights.ca.book.cc-by-sa-4.0`.

The semantic event alignment admits only documented structural adaptations:
the R007 introduction's centered `myfig` replaces the source wrapping figure
without changing its typed `figure` identity; R006's target-only ADV-0169 hint
and ADV-0259 corrective remark remain represented by correction records and
complete-file hashes rather than being falsely paired as source translations.

The retained historical fine-unit rows contain 509 legacy semantic locators
that cannot be replayed as raw-line selectors. They are preserved for stable
identity/history and are not used to prove closure. The final builder directly
verified 11,282 resolvable components, including every source and target in
the exhaustive 32-file closure and every newly generated logical unit.

## Production checkpoint

- Primary: `backend/production/v0.4-complete-2026.08.31-a`
- Independent replay: `backend/production/v0.4-complete-2026.08.31-b`
- Files per build: 27
- Bytes per build: 122,843,339
- Canonical inventory SHA-256 per build:
  `6f38b34d44835f0a3493578e005052217dd7a81949d66ab1cb17f8c98e03a7fe`
- Full path/byte/SHA-256 inventories: byte-identical.
- Dataset ID: `urn:uuid:f8badc2c-4e01-513b-a831-579c51bb9393`
- Dataset key: `lebl.shared.dataset.production-v0.4-complete-2026-08-31`
- Records: 20,396
- `records.jsonl` SHA-256:
  `e1f978beb7097875511b769abdd619c83260ac190a038d9e6915ba19d4c8bb3c`
- `dataset.json` SHA-256:
  `97e0e95330b9c32f0e0178c54c99e2bcca66c43d1cfcc665a59d146ebf8b5da6`
- `projection_manifest.json` SHA-256:
  `92242ee65f6f18bf702b0a1b4fce888c03fdb78492ff30a8f8cc97dca9f320c7`
- `VALIDATION.json` SHA-256:
  `ed53daa036ca8bb60138884a0b13c84f3494492cbfa08d53da1ffdec88ec2e41`

## Deterministic gates

Both builds passed:

1. manifest field, identity, rights, parent, and exhaustive-canonical-file
   closure checks;
2. all 5,884 exact manifest bindings;
3. all 11,282 directly resolvable component hashes;
4. JSON Schema Draft 2020-12 validation for all 20,396 records and the dataset;
5. UUID/reference and typed-parent referential integrity;
6. 15 deterministic CSV projections;
7. lossless CSV-to-record round trip, recovering exactly 20,396 records;
8. exact A/B path, byte-count, and SHA-256 inventory equality.

Validation command:

```text
python backend/production/validate_complete_backend.py --dataset backend/production/v0.4-complete-2026.08.31-a/dataset.json --csv-dir backend/production/v0.4-complete-2026.08.31-a/csv
```

The validation wrapper raises Python's CSV field limit only because the
lossless manifest-artifact record contains the complete produced-from UUID
closure; it does not relax any schema, reference, hash, or round-trip gate.

Runtime provenance: OpenAI Codex gpt-5.6-sol, Ultra, acting on the user's
request. Original authorship and edition attribution remain in the source and
edition records.
