# GitHub main U418 source/backend publication receipt

Status: **PASS; public bytes verified**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Transaction

- Repository: `https://github.com/KokunoYumeto/lebl-mathematics-family-id`
- Branch: `main`
- Verified base/sole parent: `aa7aabda7c923d54837457a8b40169ac57b4a9eb`
- Base tree: `665ec8e021d04e6c65986bd1c56df140a38f11a6`
- New source/backend commit: `6795b0deac4929a787b41e62b24d5dc7c0a66540`
- New tree: `38362acfc9482ded7e16e18337a986b97e5d1e4b`
- Commit message: `Advance live Indonesian Lebl source checkpoint to U418`
- Update: non-forced; the transaction re-read `main` immediately before the
  branch update and failed closed unless it still equaled the verified base.

## Exact published scope

The transaction published exactly 41 explicit regular non-symlink paths /
19,417,080 bytes:

- current README, controls, ledgers, and production-backend README;
- the U418 translation and backend QA receipts;
- the 418-row translation manifest and live R006 target;
- the finalized local U417 GitHub-main receipt reserved for this substantive
  checkpoint;
- one complete 27-file deterministic U418-a backend tree.

The 418-unit manifest distribution is R006 333, R007 35, R008 50. The backend
has 3,966 records, 836 embedded expressions, 796 current logical terms, 267
corrections, 23 O001 gaps, and all 418 exact manifest bindings. Its 27-file
tree totals 17,679,288 bytes and has canonical JSON inventory SHA-256
`f7520356545f2460bf8b76d7455d8d1d3c67ca3e5e5fcb9eb740e2014e90032c`.

The canonical explicit-order compact UTF-8 JSON inventory of all 41 published
paths, with sorted object keys plus LF, is 6,462 bytes, SHA-256
`055f03bb6fa0fcd534bf384676128c00c0cbdc630ede67fef3d0cb6e862f535a`.

## Readback

- Authenticated immutable Git-blob readback: PASS, 41/41 files /
  19,417,080 bytes.
- Anonymous immutable raw-commit readback: PASS, 41/41 files /
  19,417,080 bytes; every payload matched the frozen local byte string.
- Authenticated `main` readback: PASS; it resolved to the new commit.
- Commit-tree and sole-parent readback: PASS.
- Recursive commit-tree readback: PASS; 1,487 entries, `truncated=false`, and
  all 41 payload paths resolved to the exact uploaded blob IDs.
- Authenticated and anonymous inventories were identical by path, byte count,
  and SHA-256.

Both retained U418 A/B backends are byte-identical. Schema and referential
validation pass, and all 15 CSV projections recover all 3,966 canonical
records exactly. The local Fourier-convergence exercise, ADV-0267, and O001
gap LEBL-O001-R006-0023 are all bound in the public checkpoint; no new logical
term, hint, answer, or solution was introduced.

No GitHub release, release asset, tag, Zenodo record, DOI, or public-access
state changed. The public reader remains the independently verified U397
release and Zenodo record `22105195` / DOI `10.5281/zenodo.22105195`.

A bounded follow-up commit will preserve this sanitized receipt and the current
recovery controls. Its resulting commit pointer will be recorded locally and
carried with the next substantive checkpoint, avoiding a pointer-only loop.

## Receipt and recovery-controls overlay

The bounded follow-up transaction advanced `main` non-forcibly from the U418
source/backend commit to controls commit
`a1f928d708137af166d8e527147a896f41605333`, tree
`05ebc12bb711eade0da306e8374d6cb738049284`. Its sole parent is
`6795b0deac4929a787b41e62b24d5dc7c0a66540`.

The overlay preserved exactly six regular paths / 487,157 bytes: the public
receipt snapshot, `CURRENT_CURSOR.json`, `CURRENT_STATE.json`,
`PUBLICATION_STATE.json`, `TASK_AND_RECOVERY.md`, and `DECISION_LOG.jsonl`.
Authenticated immutable-blob and anonymous immutable-commit readback matched
all six frozen byte strings. The canonical sorted compact inventory is 826
bytes, SHA-256
`55df1f8bc518516d8be3543d1f480672bb2b4bde02bb3f6ed0067572cd2712b1`.
Authenticated `main`, commit-tree, and sole-parent checks also passed.

This local receipt now records the overlay pointer. Its final-byte identity is
carried with the next substantive source/backend checkpoint rather than by a
third pointer-only commit. The U397 GitHub release, release assets, tag, Zenodo
record, DOI, and public-access state remain unchanged.
