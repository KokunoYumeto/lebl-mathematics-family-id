# GitHub main U416 source/backend publication receipt

Status: **PASS; public bytes verified**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Transaction

- Repository: `https://github.com/KokunoYumeto/lebl-mathematics-family-id`
- Branch: `main`
- Verified base/sole parent: `deea5e238ffef867b756c51a5bab73ffc377a027`
- Base tree: `5f0baabf136bb2cd7c37e2807c6fa27eb945003e`
- New source/backend commit: `264a8ad907a73ce05c663cb508dac59972b2794b`
- New tree: `21bba7ec7c5f9aa47d33280c3122322346b3308d`
- Commit message: `Advance live Indonesian Lebl source checkpoint to U416`
- Update: non-forced; the transaction re-read `main` immediately before the
  branch update and failed closed unless it still equaled the verified base.

## Exact published scope

The transaction published exactly 41 explicit regular non-symlink paths /
19,285,093 bytes:

- current README, controls, ledgers, and production-backend README;
- the U416 translation and backend QA receipts;
- the 416-row translation manifest and live R006 target;
- the finalized local U415 GitHub-main receipt reserved for this substantive
  checkpoint;
- one complete 27-file deterministic U416-a backend tree.

The 416-unit manifest distribution is R006 331, R007 35, R008 50. The backend
has 3,954 records, 832 embedded expressions, 795 current logical terms, 265
corrections, and all 416 exact manifest bindings. Its 27-file tree totals
17,569,205 bytes and has canonical JSON inventory SHA-256
`c4ab72e0c178748410c3d77c5af94b987c4853b2bae86c8bd54a0534f9538bc4`.

The canonical explicit-order compact UTF-8 JSON inventory of all 41 published
paths, with sorted object keys plus LF, is 6,450 bytes, SHA-256
`57fe8a41a44d41ed8c6d49a889b8695a4fc2cd7fcddd33ef399064bb9aacc236`.

## Readback

- Authenticated immutable Git-blob readback: PASS, 41/41 files /
  19,285,093 bytes.
- Anonymous immutable raw-commit readback: PASS, 41/41 files /
  19,285,093 bytes; every payload matched the frozen local byte string.
- Authenticated `main` readback: PASS; it resolved to the new commit.
- Commit-tree and sole-parent readback: PASS.
- Recursive commit-tree readback: PASS; 1,417 entries, `truncated=false`, and
  all 41 payload paths resolved to the exact uploaded blob IDs.
- Authenticated and anonymous inventories were identical by path, byte count,
  and SHA-256.

Both retained U416 A/B backends and two fresh bounded admission replays are
byte-identical. Schema and referential validation pass, and all 15 CSV
projections recover all 3,954 canonical records exactly.

No GitHub release, release asset, tag, Zenodo record, DOI, or public-access
state changed. The public reader remains the independently verified U397
release and Zenodo record `22105195` / DOI `10.5281/zenodo.22105195`.

A bounded follow-up commit will preserve this sanitized receipt and the current
recovery controls. Its resulting commit pointer will be recorded locally and
carried with the next substantive checkpoint, avoiding a pointer-only loop.
