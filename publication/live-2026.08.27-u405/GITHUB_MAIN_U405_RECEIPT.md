# GitHub `main` U405 source/backend publication receipt

Status: **PASS; public immutable bytes verified anonymously**  
Date: 2026-08-27  
Repository: `KokunoYumeto/lebl-mathematics-family-id`  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Bounded non-force transaction

- Verified starting `main` commit:
  `ce796a7e3efe43f42f4011a6cc4b59bb50d8a932`.
- Verified starting tree:
  `1925afe2ed4d86ffb063a04b996c1cce97b0c1cf`.
- Created source/backend commit:
  `49f35c4d2a9d3ebe5269eb37a456b2424d2a74fb`.
- Created tree:
  `e265383cb3ecb4cecc8d5629f01ca78804bdb163`.
- The update was non-force and race-checked immediately before changing
  `refs/heads/main`.
- The resulting tree contains 1,105 regular file blobs. No release, tag, or
  Zenodo object was created, edited, or republished.

## Exact payload

The transaction changed or refreshed exactly 40 explicit paths totaling
18,564,601 bytes. They comprise:

- the reader-facing repository README;
- six current controls/ledgers plus the terminology ledger;
- the current production-backend README;
- the U320 translation receipt and U405 backend receipt;
- the 405-row translation manifest and live R006 target;
- the final local U404 receipt carried forward;
- one complete U405-a backend tree of 27 files.

The canonical explicit-order compact UTF-8 JSON inventory with sorted object
keys plus LF is 6,309 bytes, SHA-256
`2d1008ce5ccb6a08cea371440cf12c5f34e7113f719f906b406cecc666412596`.
The payload includes the 405-unit manifest SHA-256
`bc8fbaea7e0abd3792f24217e3e9680976efc6fd969dfeada94e84e608b5c979`,
the live R006 target SHA-256
`f878c2862a574a3544ed740cafbdbd30faa1cd76cdd459b4984f4ba387a5bd67`,
and U405 `records.jsonl` SHA-256
`8abde22c1473cb8901121aba609dad7c91390c66f63b409438d0192e884a4bed`.

## Anonymous readback

Every one of the 40 paths was downloaded anonymously from the immutable
commit URL. All 40 payloads matched the pre-transaction in-memory snapshot by
filename, byte count, and SHA-256: 40/40 PASS, 18,564,601/18,564,601 bytes.
An authenticated read immediately after the transaction also resolved
`main` to commit `49f35c4d2a9d3ebe5269eb37a456b2424d2a74fb`.

This checkpoint advances only the live source/backend lineage from U404 to
U405 at a complete orthonormal-systems subsection boundary. The public reader
remains the verified U397 GitHub release and Zenodo record 22105195 / DOI
`10.5281/zenodo.22105195`. A bounded follow-up commit preserves this sanitized
receipt and current controls; it does not change release or Zenodo bytes.

## Receipt/control preservation

The bounded follow-up completed at commit
`87b172deca6284600d28f82c5937458c61519cc0`, tree
`77edf16cef6ddb9165dd7f4ed3f46996a8e8a11e`, with source commit
`49f35c4d2a9d3ebe5269eb37a456b2424d2a74fb` as its sole parent. It changed
exactly this receipt and five current controls: six files / 431,921 bytes.
Anonymous immutable-commit readback matched all six paths, byte counts, and
SHA-256 values. The public receipt snapshot in that commit is 2,538 bytes,
SHA-256
`1f1d60c254a6118249a3807fdb63c8c7b2b2ac3b7d9fa51a39f663803420e79c`.

This local post-transaction section records the commit that contains its prior
snapshot. It is intentionally carried with the next substantive checkpoint
rather than creating an infinite chain of self-referential pointer-only
commits. The GitHub release, tag, and Zenodo record remain unchanged.
