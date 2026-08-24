# Backend v0.4 live U319 + terminology-QA revalidation

Status: **PASS**  
Dataset generation date: 2026-08-23  
Independent revalidation date: 2026-08-24  
Lane: `R006+R007+R008`  
Dataset ID: `urn:uuid:d4942c0c-1b83-541d-ac61-d7c7964e1473`  
Schema version: `0.3.0`  
Authority status: `authoritative`

## Scope

This receipt revalidates the two pre-existing deterministic builds:

- `backend/production/v0.4-live-2026.08.23-u319-tqa-a`
- `backend/production/v0.4-live-2026.08.23-u319-tqa-b`

No translation, repository, or publication file was changed by this check. The only retained output from the revalidation is this receipt. Temporary regenerated CSV projections were removed after their hashes had been compared.

## Validator identity and checks run

Validator: `backend/tools/backend_tool.py`  
Bytes: `41,874`  
SHA-256: `cb6596ad61c50b8072660cdd9246692ba0c6caac405ed84f3527386973a9591c`

For each of builds A and B, the validator was run against `dataset.json` with:

1. `validate`, including schema identity, canonicalization, UUIDv5 identities, record-stream byte count/hash/count, global sort order, per-record validation, referential integrity, projection-manifest integrity, and solution-coverage consistency;
2. `roundtrip` against the checked-in `csv` directory, which recomputed every deterministic projection byte-for-byte and reconstructed all record projections;
3. `project` to a fresh temporary directory, followed by byte-and-hash comparison of generated A against generated B and generated A against A's checked-in projections.

The illustrative fixture at `backend/fixtures/non_authoritative` was separately validated, projected to a fresh temporary directory, and round-tripped. Its `illustrative_only` authority label and fixture notice were enforced by the validator.

## Authoritative dataset result

Both A and B returned the same successful validation summary:

- records: `2,650`
- expressions: `638`
- schemas checked: `3`
- units: `319`
- segments: `319`
- concepts: `432`
- terms: `440`
- relations: `594`
- QA events: `421`
- corrections: `94`
- artifacts: `15`
- editions: `7`
- resources: `3`
- rights records: `4`
- assets: `2`
- fixture flag: `false`

Each checked-in CSV set passed deterministic byte comparison across `15` files and reconstructed all `2,650` records without a missing, extra, changed, or duplicate record. Each fresh projection contained `15` files and `6,803,946` bytes. Fresh A and fresh B had `0` mismatches; fresh A and checked-in A had `0` mismatches.

## Byte identities

Each complete build tree contains `26` files and `11,227,185` bytes. A and B have the same relative paths, byte counts, and SHA-256 hashes with `0` mismatches.

Canonical comparison inventory format: one UTF-8 line per file, sorted by forward-slash relative path, as `<sha256>\t<bytes>\t<relative-path>\n`.

- A inventory SHA-256: `65e4d277b5ec2579ad22cc1eee4ff70a01ef7237390fd2e94b9355729b7f594f`
- B inventory SHA-256: `65e4d277b5ec2579ad22cc1eee4ff70a01ef7237390fd2e94b9355729b7f594f`
- `records.jsonl`: `3,599,333` bytes; SHA-256 `062f7e040cc79ac7b8c428bfd2b7149a831262402a69d46800242ae1efc01c29`; `2,650` lines
- `dataset.json`: `1,793` bytes; SHA-256 `7131513f60cfeacda899f6fa3169da9c0483f58e815136d2c2ae992edf2f85b8`
- `projection_manifest.json`: `28,966` bytes; SHA-256 `34f7cb8d24b13e264029538033450eb1c31f2f166ceacc04980f39b5d7d9bac5`
- `VALIDATION.json`: `7,573` bytes; SHA-256 `e8b431ee42608c8b549d78048e29410a8e603214d208bcdc4a9b815e0a1269f5`

Bound input identities embedded identically in both builds:

- `inputs/TRANSLATION_MANIFEST.jsonl`: `452,035` bytes; SHA-256 `0718642d139d80c505605d6cd47d5f836ba15dd0bde7a7f02e344922fee4d703`
- `inputs/TERMINOLOGY.csv`: `86,076` bytes; SHA-256 `2e844ec82fa781b2fb3eb67deed21e55ab8c2dc25fcb2e609d46603f3a32e6aa`
- `inputs/ADVERSE_LEDGER.jsonl`: `198,171` bytes; SHA-256 `cb972c4fa07ebf4c0706bb2eda7c80300448748919c30153d1b04ebb5cd5de5e`

## Fixture result

The non-authoritative fixture passed validation with `24` records, `2` expressions, and one exercise declared with full-solution coverage. Fresh projection generated `15` files; round-trip checked all `15` and recovered all `24` records. Fixture identities:

- `dataset.json`: `1,233` bytes; SHA-256 `5da98407e72dc8b44727868ff99b09070225d9d59032916891c267ec6fd93531`
- `records.jsonl`: `20,147` bytes; SHA-256 `3becbbd217cb8206c01c79f8c34cf1dfe7393ddabd644e688ae8883c91d0685e`

## Conclusion

The U319 terminology-QA backend is internally valid, referentially intact, round-trip lossless, and deterministic across two independently materialized trees. Builds A and B are byte-identical; one copy, conventionally build A, is sufficient for a non-duplicative release payload, while build B serves as reproducibility evidence.
