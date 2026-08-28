# GitHub main U412 source/backend publication receipt

Status: **PASS; public bytes verified**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Transaction

- Repository: `https://github.com/KokunoYumeto/lebl-mathematics-family-id`
- Branch: `main`
- Verified base/sole parent: `46dff7ff4a18ea8d0e4b6c43e0e38328af4880c7`
- Base tree: `68514b675135b680e1741c8d6f0917f08db76edd`
- New source/backend commit: `3e759645f4b24d2e08adf116a859351aebf6db7e`
- New tree: `e572647f44f2145bb4ec8f813db7a7d1218ccd62`
- Commit message: `Advance live Indonesian Lebl source checkpoint to U412`
- Update: non-forced; the transaction re-read `main` immediately before the
  branch update and failed closed unless it still equaled the verified base.

The first bounded attempt stopped during blob upload on a transient TLS
handshake timeout. It had not created a tree, commit, or branch update. A
read-only check proved `main` still equaled the expected base. The retry added
bounded transient-network retries and completed against that same base.

## Exact published scope

The transaction published exactly 41 explicit regular non-symlink paths /
19,083,153 bytes:

- current README, controls, ledgers, and production-backend README;
- U410–U412 translation and backend QA receipts;
- the 412-row translation manifest and live R006 target;
- the finalized local U409 GitHub-main receipt that had been reserved for the
  next substantive checkpoint;
- one complete 27-file deterministic U412-a backend tree.

The 412-unit manifest distribution is R006 327, R007 35, R008 50. The backend
has 3,931 records, 824 embedded expressions, 791 current logical terms, 262
corrections, and all 412 exact manifest bindings. Its 27-file tree totals
17,413,205 bytes and has canonical JSON inventory SHA-256
`92a73394f6ad19b80c64f777f60abb500cf1976fa1eee01aac057298cd490b01`.

The canonical explicit-order compact UTF-8 JSON inventory of all 41 published
paths, with sorted object keys plus LF, is 6,451 bytes, SHA-256
`1e3cdd934032469bde2db682a7811ba485112f70ec0213f747e988191c6d5e05`.

## Readback

- Authenticated immutable Git-blob readback: PASS, 41/41 files /
  19,083,153 bytes.
- Anonymous immutable raw-commit readback: PASS, 41/41 files /
  19,083,153 bytes; every payload matched the frozen local byte string.
- Authenticated `main` readback: PASS; it resolved to the new commit.
- Recursive commit-tree readback: PASS; 1,277 entries, `truncated=false`, and
  all 41 payload paths resolved to the exact uploaded blob IDs.
- Authenticated and anonymous inventories were identical by path, byte count,
  and SHA-256.

No GitHub release, release asset, tag, Zenodo record, DOI, or public-access
state changed. The public reader remains the independently verified U397
release and Zenodo record `22105195` / DOI `10.5281/zenodo.22105195`.

A bounded follow-up commit will preserve this sanitized receipt and the current
recovery controls. Its resulting commit pointer will be recorded locally and
carried with the next substantive checkpoint, avoiding a pointer-only loop.
