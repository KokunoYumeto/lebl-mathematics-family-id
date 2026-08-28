# GitHub main U417 source/backend publication receipt

Status: **PASS; public bytes verified**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Transaction

- Repository: `https://github.com/KokunoYumeto/lebl-mathematics-family-id`
- Branch: `main`
- Verified base/sole parent: `9296ab4e6b75266881cd5ea857ca83ecfa933118`
- Base tree: `5d0e3516b6a6b299ce75f28014944a93b3916860`
- New source/backend commit: `8a87e4c6dfc9b1576e684bd909ac6570834726af`
- New tree: `96a1dc4c1afaf32863a365722a02c51fbdf9c9ef`
- Commit message: `Advance live Indonesian Lebl source checkpoint to U417`
- Update: non-forced; the transaction re-read `main` immediately before the
  branch update and failed closed unless it still equaled the verified base.

## Exact published scope

The transaction published exactly 41 explicit regular non-symlink paths /
19,357,500 bytes:

- current README, controls, ledgers, and production-backend README;
- the U417 translation and backend QA receipts;
- the 417-row translation manifest and live R006 target;
- the finalized local U416 GitHub-main receipt reserved for this substantive
  checkpoint;
- one complete 27-file deterministic U417-a backend tree.

The 417-unit manifest distribution is R006 332, R007 35, R008 50. The backend
has 3,961 records, 834 embedded expressions, 796 current logical terms, 266
corrections, 22 O001 gaps, and all 417 exact manifest bindings. Its 27-file
tree totals 17,628,427 bytes and has canonical JSON inventory SHA-256
`fe0edd56faa1e4183c010002903a0af14f17a5ce3afe56a47b0d561300485424`.

The canonical explicit-order compact UTF-8 JSON inventory of all 41 published
paths, with sorted object keys plus LF, is 6,456 bytes, SHA-256
`6d04ccf3fe30eefd1ea1880ba6bfd56b7cc9b0da8562ada233742009e3977d29`.

## Readback

- Authenticated immutable Git-blob readback: PASS, 41/41 files /
  19,357,500 bytes.
- Anonymous immutable raw-commit readback: PASS, 41/41 files /
  19,357,500 bytes; every payload matched the frozen local byte string.
- Authenticated `main` readback: PASS; it resolved to the new commit.
- Commit-tree and sole-parent readback: PASS.
- Recursive commit-tree readback: PASS; 1,452 entries, `truncated=false`, and
  all 41 payload paths resolved to the exact uploaded blob IDs.
- Authenticated and anonymous inventories were identical by path, byte count,
  and SHA-256.

Both retained U417 A/B backends are byte-identical. Schema and referential
validation pass, and all 15 CSV projections recover all 3,961 canonical
records exactly. The first Fourier-series exercise, TERM-0796, ADV-0266, and
O001 gap LEBL-O001-R006-0022 are all bound in the public checkpoint.

No GitHub release, release asset, tag, Zenodo record, DOI, or public-access
state changed. The public reader remains the independently verified U397
release and Zenodo record `22105195` / DOI `10.5281/zenodo.22105195`.

A bounded follow-up commit will preserve this sanitized receipt and the current
recovery controls. Its resulting commit pointer will be recorded locally and
carried with the next substantive checkpoint, avoiding a pointer-only loop.
