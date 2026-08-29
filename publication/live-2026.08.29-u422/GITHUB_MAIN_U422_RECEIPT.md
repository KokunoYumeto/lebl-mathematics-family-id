# GitHub main U422 source/backend publication receipt

Status: **PASS; public bytes verified**  
Date: 2026-08-29  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Transaction

- Repository: `https://github.com/KokunoYumeto/lebl-mathematics-family-id`
- Branch: `main`
- Verified base and sole parent:
  `e76a90911c7966f7fdd12987359e73cc0929526b`
- Base tree: `36305f5028b9622460352313d5f85835ad80e887`
- New source/backend commit:
  `390716d4701fa450e65e93c7ab9c7dc6c7752e6b`
- New tree: `44d02db5895d5866626cc437b04c126467c4ca16`
- Commit message: `Advance live Indonesian Lebl source checkpoint to U422`
- Update: non-forced; the transaction re-read `main` immediately before the
  branch update and failed closed unless it still equaled the verified base.

## Exact published scope

The transaction published exactly 42 explicit regular non-symlink paths /
19,749,150 bytes:

- current README, controls, ledgers, and production-backend README;
- the U422 translation and backend QA receipts;
- the 422-row translation manifest and live R006 target;
- the finalized local U421 GitHub-main receipt reserved for this substantive
  checkpoint;
- the exact live deterministic-backend builder; and
- one complete 27-file deterministic U422-a backend tree.

The 422-unit manifest distribution is R006 337, R007 35, R008 50. The backend
has 3,987 records, 844 embedded expressions, 796 current logical terms, 268
corrections, 27 O001 gaps, and all 422 exact manifest bindings. Its 27-file
tree totals 17,886,457 bytes. The platform-neutral compact JSON inventory,
ordered by ordinal POSIX relative path, is 3,292 bytes, SHA-256
`312fb8f903cb19492d2dd6194c09fc69c49e9fd265e39c18d52c9b2a3368ecbf`.
The builder is 78,347 bytes, SHA-256
`77522ade28f62fc94110dc870917f91a21b0720905a9b73a51f328e0aa159bbb`.

The canonical explicit-order compact UTF-8 JSON inventory of all 42 published
paths, with sorted object keys plus LF, is 6,599 bytes, SHA-256
`4afc7f9419a2655bbf58f3156cc0b77237dccfbdc152fc310d844f7ccbe5a4b1`.

## Readback

- Authenticated immutable Git-blob readback: PASS, 42/42 files /
  19,749,150 bytes.
- Anonymous immutable raw-commit readback: PASS, 42/42 files /
  19,749,150 bytes; every payload matched the frozen local byte string.
- Authenticated and anonymous `main` readback: PASS; it resolves to the new
  commit.
- Commit-tree and sole-parent readback: PASS.
- Recursive commit-tree readback: PASS; 1,627 entries, `truncated=false`, and
  all 42 payload paths resolve to the exact uploaded blob IDs.
- Authenticated, anonymous, and local inventories are identical by path, byte
  count, and SHA-256. An independent second read-only audit repeated the
  branch, commit, parent, tree, blob, and anonymous raw-byte checks and passed
  all 42 paths.

Both retained U422 A/B backends are byte-identical. Schema and referential
validation pass, and all 15 CSV projections recover all 3,987 canonical
records exactly. The labeled L2 triangle-inequality exercise and O001 gap
`LEBL-O001-R006-0027` are bound in the public checkpoint. The source supplies
neither a hint nor a solution, and none was inferred or invented.

No GitHub release, release asset, tag, Zenodo record, DOI, or public-access
state changed. A separate independent preservation check confirmed that the
public U397 release remains non-draft and non-prerelease with all nine assets /
12,439,062 bytes anonymously matching their recorded SHA-256 identities. The
public reader remains U397 on GitHub and Zenodo record `22105195`, DOI
`10.5281/zenodo.22105195`.

A bounded follow-up commit will preserve this sanitized receipt and the current
recovery controls. Its resulting commit pointer will be recorded locally and
carried with the next substantive checkpoint, avoiding a pointer-only loop.
