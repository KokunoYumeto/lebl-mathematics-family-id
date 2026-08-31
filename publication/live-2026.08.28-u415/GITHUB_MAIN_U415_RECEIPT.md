# GitHub main U415 source/backend publication receipt

Status: **PASS; public bytes verified**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Transaction

- Repository: `https://github.com/KokunoYumeto/lebl-mathematics-family-id`
- Branch: `main`
- Verified base/sole parent: `d43aa8cf3252bc986f366d99677560ba6f844169`
- Base tree: `6d5fa587ec67d1ca72be9e05ae171f2dfb60d873`
- New source/backend commit: `b59fa16fddfdad15943b5fab384fcefe2ab2545b`
- New tree: `8bf2df12558c8c33c5ed314aafb9445d3655d46c`
- Commit message: `Advance live Indonesian Lebl source checkpoint to U415`
- Update: non-forced; the transaction re-read `main` immediately before the
  branch update and failed closed unless it still equaled the verified base.

## Exact published scope

The transaction published exactly 41 explicit regular non-symlink paths /
19,252,828 bytes:

- current README, controls, ledgers, and production-backend README;
- the U415 translation and backend QA receipts;
- the 415-row translation manifest and live R006 target;
- the finalized local U414 GitHub-main receipt reserved for this substantive
  checkpoint;
- one complete 27-file deterministic U415-a backend tree.

The 415-unit manifest distribution is R006 330, R007 35, R008 50. The backend
has 3,951 records, 830 embedded expressions, 795 current logical terms, 265
corrections, and all 415 exact manifest bindings. Its 27-file tree totals
17,546,055 bytes and has canonical JSON inventory SHA-256
`89eeec626092d0ec1ac92bebab9a977b3d2ee00c97866993903f145ebba5646c`.

The canonical explicit-order compact UTF-8 JSON inventory of all 41 published
paths, with sorted object keys plus LF, is 6,453 bytes, SHA-256
`03c878add4f24b7291bdba5fea79c1e020fd0befe4026283e04c31fb37fe52c9`.

## Readback

- Authenticated immutable Git-blob readback: PASS, 41/41 files /
  19,252,828 bytes.
- Anonymous immutable raw-commit readback: PASS, 41/41 files /
  19,252,828 bytes; every payload matched the frozen local byte string.
- Authenticated `main` readback: PASS; it resolved to the new commit.
- Commit-tree and sole-parent readback: PASS.
- Recursive commit-tree readback: PASS; 1,382 entries, `truncated=false`, and
  all 41 payload paths resolved to the exact uploaded blob IDs.
- Authenticated and anonymous inventories were identical by path, byte count,
  and SHA-256.

The unchanged validator's exact reference collector resolves 14,652
record-field references in U415 with zero unresolved targets. Both U415 A/B
backends independently validate and all 15 CSV projections recover all 3,951
canonical records exactly.

No GitHub release, release asset, tag, Zenodo record, DOI, or public-access
state changed. The public reader remains the independently verified U397
release and Zenodo record `22105195` / DOI `10.5281/zenodo.22105195`.

A bounded follow-up commit will preserve this sanitized receipt and the current
recovery controls. Its resulting commit pointer will be recorded locally and
carried with the next substantive checkpoint, avoiding a pointer-only loop.

## Receipt and recovery-controls overlay

The bounded follow-up transaction advanced `main` non-forcibly from the U415
source/backend commit to controls commit
`deea5e238ffef867b756c51a5bab73ffc377a027`, tree
`5f0baabf136bb2cd7c37e2807c6fa27eb945003e`. Its sole parent is
`b59fa16fddfdad15943b5fab384fcefe2ab2545b`.

The overlay preserved exactly six regular paths / 468,597 bytes: the public
receipt snapshot, `CURRENT_CURSOR.json`, `CURRENT_STATE.json`,
`PUBLICATION_STATE.json`, `TASK_AND_RECOVERY.md`, and `DECISION_LOG.jsonl`.
Authenticated immutable-blob and anonymous immutable-commit readback matched
all six frozen byte strings. The canonical sorted compact inventory is 826
bytes, SHA-256
`a643662d2919f26369016f9eaf1e698c59c65a92439abb78db239f814df63d3c`.
Authenticated `main`, commit-tree, and sole-parent checks also passed.

This local receipt now records the overlay pointer. Its final-byte identity is
carried with the next substantive source/backend checkpoint rather than by a
third pointer-only commit. The U397 GitHub release, release assets, tag, Zenodo
record, DOI, and public-access state remain unchanged.
