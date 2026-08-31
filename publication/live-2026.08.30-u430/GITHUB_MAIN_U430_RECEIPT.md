# GitHub Main Publication Receipt — U430 Source/Backend Checkpoint

Status: **PASS — PUBLIC AND BYTE-VERIFIED**  
Date: 2026-08-30  
Repository: <https://github.com/KokunoYumeto/lebl-mathematics-family-id>  
Branch: `main`

## Transaction

- Verified base/post-publication-controls commit: `4d7f767a564243cad0ada9cdde8a5a6a868482ce`.
- Verified base tree: `438366f04913fc18fe026f48b7a6bf4b8b28c222`.
- New source/backend commit: `69697bb19ac259da87f0803abee5cf64b1ad6a71`.
- New tree: `05e083ddb2d5c82e7bbf1609701d0136457edea1`.
- Sole parent: `4d7f767a564243cad0ada9cdde8a5a6a868482ce`.
- Update mode: non-forced, exact expected-head compare-and-swap.

The transaction published exactly 42 bounded regular paths totaling 20,027,522 bytes. The 6,644-byte canonical inventory preserves the publisher’s explicit 15-path prefix order followed by the 27 backend files in ordinal POSIX-relative-path order; each row binds path, byte count, and SHA-256. Its SHA-256 is `e5f188ba407b5c6fff5e82ba74e051f7e104d0efda557fc13e584c529b71400f`.

## Bound checkpoint

- Manifest: 430 unique units (R006 344, R007 36, R008 50), 673,396 bytes, SHA-256 `2dcf7104439fb9d83db6b291b00153f38807935fcb99dc90362635058978ed42`.
- U430 unit: R007 definite-versus-indefinite-integral and closed-form discussion, source and target raw lines 89–98. The target is 4,158 bytes, SHA-256 `dd10809f0a5714c8dc050e3878de7156dbaa138ca541dc35349261a245304451`.
- Terminology: 798 current logical rows; `LEBL-TERM-0798` binds `closed form` → `bentuk tertutup`.
- Backend: 4,026 records, 860 expressions, 430 manifest bindings, 374 direct component checks, and 15 lossless CSV round trips. The published 27-file tree totals 18,239,374 bytes and has canonical inventory SHA-256 `bba7789a35d3d5b6db5c90a65a0cdbff6ed1330eba893e07018ba2adbf6c508f`.
- The U430 unit and backend receipts, current controls, live builder, active R007 target, and finalized U429 post-publication-controls receipt are included.

## Readback

The bounded publisher proved all of the following after the branch update:

- authenticated `main` resolves to the new commit;
- the commit tree and sole-parent identities match;
- authenticated immutable-blob readback passes all 42 paths / 20,027,522 bytes;
- anonymous immutable-commit raw readback passes all 42 paths with the exact canonical inventory;
- recursive tree readback is untruncated (1,917 entries) and binds all 42 payload blobs;
- no GitHub release or Zenodo state changed.

The U429 release remains the current reader boundary, including the complete R006 Volume II PDF and Zenodo DOI `10.5281/zenodo.22172396`. U430 is a source/backend checkpoint only. This receipt contains no credential material.
