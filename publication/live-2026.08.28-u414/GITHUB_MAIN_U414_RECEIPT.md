# GitHub main U414 source/backend publication receipt

Status: **PASS; public bytes verified**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Transaction

- Repository: `https://github.com/KokunoYumeto/lebl-mathematics-family-id`
- Branch: `main`
- Verified base/sole parent: `d196897b114c86cd4316220ba08d63a8a8122dd0`
- Base tree: `f5087bd4bd2cb32083083a44e6a110e1ebaa4b14`
- New source/backend commit: `6469a47e1944b2dc7eaeda308659400c6d417219`
- New tree: `92eedaaaedc261b4d51b827c8cee363da7dcd8f0`
- Commit message: `Advance live Indonesian Lebl source checkpoint to U414`
- Update: non-forced; the transaction re-read `main` immediately before the
  branch update and failed closed unless it still equaled the verified base.

## Exact published scope

The transaction published exactly 41 explicit regular non-symlink paths /
19,206,583 bytes:

- current README, controls, ledgers, and production-backend README;
- the U414 translation and backend QA receipts;
- the 414-row translation manifest and live R006 target;
- the finalized local U413 GitHub-main receipt reserved for this substantive
  checkpoint;
- one complete 27-file deterministic U414-a backend tree.

The 414-unit manifest distribution is R006 329, R007 35, R008 50. The backend
has 3,944 records, 828 embedded expressions, 793 current logical terms, 265
corrections, and all 414 exact manifest bindings. Its 27-file tree totals
17,511,006 bytes and has canonical JSON inventory SHA-256
`c3c2de27a4afba87315cb6cf9a5fb7a0f18202f06336dea0e531da00ce4e549a`.

The canonical explicit-order compact UTF-8 JSON inventory of all 41 published
paths, with sorted object keys plus LF, is 6,453 bytes, SHA-256
`050938230ebfe143ccfdb4d30b8f6c709d1ec792d782e4fe358d652ad723791a`.

## Readback

- Authenticated immutable Git-blob readback: PASS, 41/41 files /
  19,206,583 bytes.
- Anonymous immutable raw-commit readback: PASS, 41/41 files /
  19,206,583 bytes; every payload matched the frozen local byte string.
- Authenticated `main` readback: PASS; it resolved to the new commit.
- Commit-tree and sole-parent readback: PASS.
- Recursive commit-tree readback: PASS; 1,347 entries, `truncated=false`, and
  all 41 payload paths resolved to the exact uploaded blob IDs.
- Authenticated and anonymous inventories were identical by path, byte count,
  and SHA-256.

The unchanged validator's exact reference collector was replayed on both
canonical datasets before publication: U413 has 14,608 resolved record-field
references and U414 has 14,628. `LEBL-ID-DEC-0169` explicitly supersedes only
the earlier erroneous U413 metric; no dataset byte or validation result changed.

No GitHub release, release asset, tag, Zenodo record, DOI, or public-access
state changed. The public reader remains the independently verified U397
release and Zenodo record `22105195` / DOI `10.5281/zenodo.22105195`.

A bounded follow-up commit will preserve this sanitized receipt and the current
recovery controls. Its resulting commit pointer will be recorded locally and
carried with the next substantive checkpoint, avoiding a pointer-only loop.
