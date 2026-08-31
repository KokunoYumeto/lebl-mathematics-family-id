# GitHub main U413 source/backend publication receipt

Status: **PASS; public bytes verified**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Transaction

- Repository: `https://github.com/KokunoYumeto/lebl-mathematics-family-id`
- Branch: `main`
- Verified base/sole parent: `c07607310682436fc9c0f01f42e436b2db547b71`
- Base tree: `32974f59ebbe54413693ddd4e87c09a6300405a0`
- New source/backend commit: `97e750330eeabae9b6d6845f5da157479a0fb832`
- New tree: `c7a162c927524e87ea3fe9bd667f535b566afd1b`
- Commit message: `Advance live Indonesian Lebl source checkpoint to U413`
- Update: non-forced; the transaction re-read `main` immediately before the
  branch update and failed closed unless it still equaled the verified base.

## Exact published scope

The transaction published exactly 41 explicit regular non-symlink paths /
19,164,915 bytes:

- current README, controls, ledgers, and production-backend README;
- the U413 translation and backend QA receipts;
- the 413-row translation manifest and live R006 target;
- the finalized local U412 GitHub-main receipt reserved for this substantive
  checkpoint;
- one complete 27-file deterministic U413-a backend tree.

The 413-unit manifest distribution is R006 328, R007 35, R008 50. The backend
has 3,939 records, 826 embedded expressions, 792 current logical terms, 265
corrections, and all 413 exact manifest bindings. Its 27-file tree totals
17,480,735 bytes and has canonical JSON inventory SHA-256
`928ed5553cb822f33ffbc55abdc9198d4ecbd710c879066712958e13d1d3063f`.

The canonical explicit-order compact UTF-8 JSON inventory of all 41 published
paths, with sorted object keys plus LF, is 6,455 bytes, SHA-256
`6c8b8a13394651876c3fce1b952cac692fb1c8278cb198bf6760012cbed67176`.

## Readback

- Authenticated immutable Git-blob readback: PASS, 41/41 files /
  19,164,915 bytes.
- Anonymous immutable raw-commit readback: PASS, 41/41 files /
  19,164,915 bytes; every payload matched the frozen local byte string.
- Authenticated `main` readback: PASS; it resolved to the new commit.
- Commit-tree and sole-parent readback: PASS.
- Recursive commit-tree readback: PASS; 1,312 entries, `truncated=false`, and
  all 41 payload paths resolved to the exact uploaded blob IDs.
- Authenticated and anonymous inventories were identical by path, byte count,
  and SHA-256.

No GitHub release, release asset, tag, Zenodo record, DOI, or public-access
state changed. The public reader remains the independently verified U397
release and Zenodo record `22105195` / DOI `10.5281/zenodo.22105195`.

A bounded follow-up commit will preserve this sanitized receipt and the current
recovery controls. Its resulting commit pointer will be recorded locally and
carried with the next substantive checkpoint, avoiding a pointer-only loop.

## Receipt and recovery-controls overlay

The bounded follow-up transaction advanced `main` non-forcibly from the U413
source/backend commit to controls commit
`d196897b114c86cd4316220ba08d63a8a8122dd0`, tree
`f5087bd4bd2cb32083083a44e6a110e1ebaa4b14`. Its sole parent is
`97e750330eeabae9b6d6845f5da157479a0fb832`.

The overlay preserved exactly six regular paths / 452,972 bytes: the public
receipt snapshot, `CURRENT_CURSOR.json`, `CURRENT_STATE.json`,
`PUBLICATION_STATE.json`, `TASK_AND_RECOVERY.md`, and `DECISION_LOG.jsonl`.
Authenticated immutable-blob and anonymous immutable-commit readback matched
all six frozen byte strings. The canonical sorted compact inventory is 826
bytes, SHA-256
`6e0342ffeaeb0b1df0338f41df308d3893524ab60d5b894af6fa77a065b564fc`.
Authenticated `main`, commit-tree, and sole-parent checks also passed.

This local receipt now records the overlay pointer. Its final-byte identity is
carried with the next substantive source/backend checkpoint rather than by a
third pointer-only commit. The U397 GitHub release, release assets, tag, Zenodo
record, DOI, and public-access state remain unchanged.
