# GitHub `main` U404 source/backend publication receipt

Status: **PASS; public immutable bytes verified anonymously**  
Date: 2026-08-27  
Repository: `KokunoYumeto/lebl-mathematics-family-id`  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Bounded non-force transaction

- Verified starting `main` commit:
  `5876d70f0374a964df80d7ea627f525c92dbf227`.
- Verified starting tree:
  `25dd659e66bdb1f2fa42f88e2762ff1cc83a91fa`.
- Created source/backend commit:
  `396fa49d0ac6f0d30fc2fc5c22ed12b9f6f070ff`.
- Created tree:
  `587ad5002c175e75072e63545996f55edb7c9de7`.
- The update was non-force and race-checked immediately before changing
  `refs/heads/main`.
- The resulting tree contains 1,075 regular file blobs. No release, tag, or
  Zenodo object was created, edited, or republished.

## Exact payload

The transaction changed or refreshed exactly 42 explicit paths totaling
18,766,173 bytes. They comprise:

- the reader-facing repository README;
- seven current controls/ledgers;
- the current production-backend README;
- U318/U319 translation receipts and U403/U404 backend receipts;
- the 404-row translation manifest and live R006 `ch-approximate.tex` target;
- one complete U404-a backend tree of 27 files.

The canonical explicit-order compact UTF-8 JSON inventory with sorted object
keys plus LF is 6,577 bytes, SHA-256
`ed93aab6eb9fc2e6ceb57732b53591da9280a1e09bb8f9a9211c09cecb3a2457`.
The payload includes the 404-unit manifest SHA-256
`c1c7d3a8eae8b91a60b0e5448ca4b54fc44cc8b5880a6c2ae3a9681f64ee2517`,
the live R006 target SHA-256
`fee5eec4f67c6f2bd9ff434afb7165cbae05f98c5d27d1fd55b4ac9d5f052491`,
and U404 `records.jsonl` SHA-256
`2145f4254ef7ae42c4e46e753be63948d739a207b38b3b1a611c8c81769492a9`.

## Anonymous readback

Every one of the 42 paths was downloaded anonymously from the immutable
commit URL. All 42 payloads matched the pre-transaction in-memory snapshot by
filename, byte count, and SHA-256: 42/42 PASS, 18,766,173/18,766,173 bytes.
An authenticated read immediately after the transaction also resolved
`main` to commit `396fa49d0ac6f0d30fc2fc5c22ed12b9f6f070ff`.

This checkpoint advances only the live source/backend lineage from U402 to
U404. The public reader remains the already verified U397 GitHub release and
Zenodo record 22105195 / DOI `10.5281/zenodo.22105195`. A bounded follow-up
commit preserves this sanitized receipt and current controls; it does not
change release or Zenodo bytes.
