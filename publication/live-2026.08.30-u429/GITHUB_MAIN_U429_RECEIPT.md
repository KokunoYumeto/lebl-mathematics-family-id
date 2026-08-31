# GitHub main publication receipt - U429 source/backend checkpoint

Status: **PASS - PUBLIC AND BYTE-VERIFIED**  
Date: 2026-08-30  
Repository: <https://github.com/KokunoYumeto/lebl-mathematics-family-id>  
Branch: `main`

## Transaction

- Verified base controls commit:
  `daa1c9dee22bfcec459d3b54e9f1ab575f6b25be`.
- Verified base tree: `c928e03799ed2eb10d4c13b4cd589454a20f1755`.
- New source/backend commit:
  `e55907983ca54bb2c94d90230eb949b64a6ee7ff`.
- New tree: `97cc963dc211728a20be1c18f9c8890f01790ae9`.
- Sole parent: `daa1c9dee22bfcec459d3b54e9f1ab575f6b25be`.
- Update mode: non-forced, exact expected-head compare-and-swap.

The transaction published exactly 42 bounded regular paths totaling
20,178,050 bytes. The 6,620-byte canonical inventory preserves the publisher's
explicit 15-path prefix order, followed by the 27 backend files ordered by
ordinal POSIX relative path; each row contains path, byte count, and SHA-256.
The inventory has SHA-256
`d9fdbc0921be59836e5c1447720711fd040d682574eac148acf2c723d7402118`.

## Bound checkpoint

- Manifest: 429 unique units (R006 344, R007 35, R008 50), 671,315 bytes,
  SHA-256
  `b493ed47379b99c8cd5cae0d123063702082c27e654b4e64ea59d2faa6cca52e`.
- Final R006 unit: complete arbitrarily slow Fourier-coefficient-decay
  exercise with its explanatory remark and explicit source hint.
- R006 target: 198,362 bytes, SHA-256
  `cfaa1339706c31f16255642adcccb33903343808bc2d1bf195d70d3f25004133`.
- Backend: 4,021 records, 429 manifest bindings, 372 direct component checks,
  and 15 lossless CSV round trips. The published 27-file backend tree totals
  18,208,054 bytes and has canonical inventory SHA-256
  `e6ab83c87774c191ba28b4efa1d0cef3ac551d74482c52b6c968816e51c76057`.
- U429 unit and backend receipts are included, as is the finalized U428 public
  receipt carried at the next substantive boundary.

## Readback

The publisher proved all of the following after the branch update:

- authenticated `main` resolves to the new commit;
- commit tree and sole-parent identities match;
- authenticated immutable-blob readback passes for all 42 paths and
  20,178,050 bytes;
- anonymous immutable-commit raw readback passes for all 42 paths and the
  exact canonical inventory;
- recursive tree readback is untruncated (1,872 entries) and binds all 42
  payload blobs;
- no release or Zenodo state was changed by this source transaction.

An independent anonymous audit repeated the ref, tree, parent, raw-byte, and
Git-blob checks for all 42 paths with zero mismatches. It also reproduced the
6,620-byte canonical inventory and its SHA-256 using the publisher's exact
ordering. Global ordinal sorting of all 42 paths is intentionally not the
canonicalization used by the publisher.

The completed Volume II PDF is not part of this 42-path source transaction. It
is released separately in the existing GitHub release and Zenodo concept
lineages, with historical U397 preserved.
