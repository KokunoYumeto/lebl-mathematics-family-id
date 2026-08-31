# Durable Task and Recovery Handoff — Lebl Family id-ID

Updated: 2026-08-30
Lane: sister lane `[5]`
Status: all three release authorities frozen; R006 Volumes I-II are complete and publicly released at U429; public GitHub U430 adds one verified R007 unit through `ch-first-order-ode.tex` raw line 98 and a deterministic 4,026-record backend; publish its bounded controls overlay, then resume R007 at raw line 100; HP-LEBL-R007-001 remains owner-accepted

## Current authoritative recovery snapshot — 2026-08-30 U430

This block supersedes older local-progress and next-action statements below.
The public reader boundary remains U429; the U430 source/backend checkpoint is
public and byte-verified, with only its bounded controls overlay pending.

- Stable unit:
  `diffyqs.v6.11.first-order.integrals-as-solutions.definite-vs-indefinite-and-closed-form`.
  Source raw lines 89–98 are 601 normalized UTF-8/LF bytes, SHA-256
  `ef332a9ff33ceacb440cb57ef6275302f14ba5b2c517d67e2fc0722f6c0658e1`;
  target raw lines 89–98 are 680 bytes, SHA-256
  `f6919302a02ca3aeb96c904e2a8de6f9eb18d7dd25393e8510beaf6da2c44c84`.
  Full target: 4,158 bytes, SHA-256
  `dd10809f0a5714c8dc050e3878de7156dbaa138ca541dc35349261a245304451`.
  Receipt: `qa/R007_FIRST_ORDER_DEFINITE_VS_INDEFINITE_CLOSED_FORM_U430_20260830.md`.
- Manifest: 430 unique rows (R006 344, R007 36, R008 50), 673,396
  bytes, SHA-256
  `2dcf7104439fb9d83db6b291b00153f38807935fcb99dc90362635058978ed42`.
  `LEBL-TERM-0798` binds `closed form` → `bentuk tertutup`; the 798-row
  terminology ledger is 128,991 bytes, SHA-256
  `c281609be2e2a3c47df7c8ebffb7fe5ddf34a848a9ef7ac7916947854704b9d8`.
- Backend builds `v0.4-live-2026.08.30-u430-a` and `-b` are byte-identical:
  27 files / 18,239,374 bytes, 4,026 records, 860 expressions, 430/430
  manifest bindings, 374 direct checks, and 15 lossless CSV round trips.
  Inventory SHA-256:
  `bba7789a35d3d5b6db5c90a65a0cdbff6ed1330eba893e07018ba2adbf6c508f`.
  Receipt: `qa/BACKEND_V0_4_LIVE_U430_20260830.md`.
- Public U430 source/backend: GitHub main commit
  `69697bb19ac259da87f0803abee5cf64b1ad6a71`, tree
  `05e083ddb2d5c82e7bbf1609701d0136457edea1`, sole parent
  `4d7f767a564243cad0ada9cdde8a5a6a868482ce`. Authenticated and anonymous
  readback pass all 42 paths / 20,027,522 bytes; canonical inventory SHA-256
  is `e5f188ba407b5c6fff5e82ba74e051f7e104d0efda557fc13e584c529b71400f`.
  Receipt: `publication/live-2026.08.30-u430/GITHUB_MAIN_U430_RECEIPT.md`.
  The U429 GitHub release and Zenodo DOI `10.5281/zenodo.22172396` remain
  unchanged by U430.
- Next executable sequence: publish the bounded U430 six-path controls overlay
  from that exact source commit, anonymously read back every path, then
  translate the complete R007 example at source raw lines 100–119 into the
  target beginning at raw line 100. Preserve the R008 cursor at raw line 1648
  and do not recopy HP-LEBL-R007-001.

## Publication closure — 2026-08-30 U429

This block supersedes every older statement below that calls the U429 release
pending or identifies U397 as the current reader boundary.

- GitHub source/backend commit:
  `e55907983ca54bb2c94d90230eb949b64a6ee7ff`, tree
  `97cc963dc211728a20be1c18f9c8890f01790ae9`; independent audit passes all
  42 paths / 20,178,050 bytes. The corrected local receipt is
  `publication/live-2026.08.30-u429/GITHUB_MAIN_U429_RECEIPT.md`.
- GitHub release checkpoint:
  `0ea0e44992addc811552d6fd37689e59385272d5`, tree
  `4c88e2a011d7229643059c2924460b04242272fc`; annotated tag object
  `1a0348e4cf0a0cdeead623574d0e3ad563d98cc7`; release ID `379250341` at
  `lebl-family-id-wip.2026.08.30.u429`.
- Zenodo version: record `22172396`, DOI `10.5281/zenodo.22172396`, in the
  existing concept `10.5281/zenodo.22059779`; status published and open;
  concept-latest resolves to this record.
- Both providers expose exactly nine assets / 12,943,707 bytes, and every
  filename, byte count, and SHA-256 is cross-provider identical. The complete
  Volume II reader is 2,427,379 bytes, SHA-256
  `e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3`.
  The deterministic source/backend archive is 6,106,435 bytes, SHA-256
  `b721834dff25b7e2017d53baa228fb44b20f49fc02aa55e7fd43cfec0849da34`.
- Sanitized receipts:
  `publication/wip-2026.08.30-u429/GITHUB_PUBLICATION_RECEIPT.md`,
  `ZENODO_PUBLICATION_RECEIPT.md`, and
  `CROSS_PROVIDER_PUBLIC_READBACK_U429.md`.
- GitHub main now points to the non-forced post-publication controls commit
  `4d7f767a564243cad0ada9cdde8a5a6a868482ce`, tree
  `438366f04913fc18fe026f48b7a6bf4b8b28c222`, whose sole parent is the U429
  release checkpoint. Fresh anonymous readback passes all 9 controls/receipt
  files / 606,492 bytes; canonical inventory SHA-256 is
  `449b506ca0559d20a1974ece46a5299def0af98cd0bdd85bce58cf2ba081500f`.
  Local receipt: `publication/live-2026.08.30-u429/GITHUB_POST_PUBLICATION_CONTROLS_U429_RECEIPT.md`.
- Historical U397 remains public and unchanged. The full family remains
  partial because R007 and R008 are unfinished.
- Next executable action: translate R007
  `source/diffyqs-v6.11/ch-first-order-ode.tex` raw lines 89–98 into the target
  at raw line 89, admit stable unit
  `diffyqs.v6.11.first-order.integrals-as-solutions.definite-vs-indefinite-and-closed-form`,
  rebuild the deterministic backend, and keep the R008 cursor at raw line 1648.

## Current authoritative recovery snapshot - 2026-08-30 U429

This block supersedes every older progress count or publication pointer later
in this historical log. The machine-readable authorities are
`CURRENT_STATE.json`, `CURRENT_CURSOR.json`, and `PUBLICATION_STATE.json`.

- Local boundary: U429, manifest 429 (R006 344, R007 35, R008 50), 671,315
  bytes, SHA-256
  `b493ed47379b99c8cd5cae0d123063702082c27e654b4e64ea59d2faa6cca52e`.
  U429 is the complete final R006 exercise at source raw lines 5460-5473 /
  target raw lines 5474-5487, stable ID
  `ra.v2.fourier-series.exercises.continuous-function-arbitrarily-slow-fourier-coefficient-decay`.
  Its source block is 525 bytes, SHA-256
  `7231ef00ce5acbdf3da710ffac7de7e4af1fbacbe6669f71b2b62a7c520ae25a`;
  its Indonesian block is 581 bytes, SHA-256
  `232f2d069038044e6a9058f3fa25ccf28376e95bf29ae005f30471a6c269824d`.
  The complete target is 198,362 bytes, SHA-256
  `cfaa1339706c31f16255642adcccb33903343808bc2d1bf195d70d3f25004133`.
  The source's explanatory remark and explicit hint are preserved; no source
  solution exists, and O001 gap `LEBL-O001-R006-0034` records that exact state.
- Backend U429 A/B is byte-identical: 27 files / 18,208,054 bytes, 4,021
  records, 858 embedded expressions, 429 manifest bindings, 372 direct checks,
  and 15 lossless CSV round trips. Its 3,292-byte canonical ordinal-POSIX
  inventory has SHA-256
  `e6ab83c87774c191ba28b4efa1d0cef3ac551d74482c52b6c968816e51c76057`.
  Receipt: `qa/BACKEND_V0_4_LIVE_U429_20260830.md`, 3,134 bytes, SHA-256
  `4713c21f6827b69cced04a8530dfd5fadd0ce428795d5f5c7bfb0a71744b1183`.
- The final R006 Volume II reader is
  `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf`: 241 pages /
  2,427,379 bytes, SHA-256
  `e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3`.
  Final passes 5 and 6 are byte-identical across the PDF and seven auxiliaries;
  zero hard/reference errors, 98/98 embedded font rows, 687 valid links, 33
  valid outlines, zero replacement characters, and visual pages 1-2 and
  231-241 pass. Independent final QA proved page 232 pixel-identical after the
  convergence reruns. Unit/reader receipt:
  `qa/R006_FOURIER_ARBITRARILY_SLOW_COEFFICIENT_DECAY_EXERCISE_U429_20260830.md`,
  4,235 bytes, SHA-256
  `22312ba06b801f720278584b9f577d9414bb01017288923697788a1538c45e8e`.
- R006 Volumes I-II are complete. The full three-book family remains partial
  because R007 and R008 are unfinished.
- Verified public source boundary remains U428 commit
  `0916d113a5ce9d826d3c03fe0c869830c6e37070` plus controls commit
  `daa1c9dee22bfcec459d3b54e9f1ab575f6b25be`; do not repeat them. The public
  reader remains U397 on GitHub and Zenodo record 22105195 until the authorized
  U429 transaction completes. Preserve that historical release unchanged.
- Next executable sequence: publish U429 source/backend and the completed
  Volume II reader in the existing GitHub repository and Zenodo concept
  `10.5281/zenodo.22059779`, perform anonymous byte readback, update controls,
  then translate R007 source raw lines 89-98 into the target beginning at raw
  line 89. Preserve the R008 cursor at source raw line 1648.

Recovery rule: begin with this U429 block and the three machine-readable
controls. Do not retranslate R006, do not re-copy HP-LEBL-R007-001, do not
create a competing Zenodo concept, and do not contact an upstream author before
the full assigned three-book corpus is complete.

## Historical authoritative recovery snapshot - 2026-08-30 U428

This block supersedes every older progress count or publication pointer later
in this historical log. The machine-readable authorities are
`CURRENT_STATE.json`, `CURRENT_CURSOR.json`, and `PUBLICATION_STATE.json`.

- Local boundary: U428, manifest 428 (R006 343, R007 35, R008 50), 668,974
  bytes, SHA-256
  `5fc464cc5d3db1fd858ba28d0525cd35a7ee7792b2b6a59c0596a24206b0a844`.
  U428 is the complete two-part symmetric Fourier-partial-sum jump-midpoint
  convergence exercise at source raw lines 5428–5458 / target raw lines
  5442–5472, stable ID
  `ra.v2.fourier-series.exercises.symmetric-partial-sums-jump-one-sided-limit-average`.
  Its exact source block is 910 bytes, SHA-256
  `322b590d17072290cb02092c8b14e840523f24bb6f02560a8de4e75b5ad95c2f`;
  its exact Indonesian block is 1,007 bytes, SHA-256
  `e39ce52a989ffee0660f9ff67b7897ac5d4e384fb7155caed2920b3c7d3a47d8`.
  The complete target is 198,306 bytes, SHA-256
  `0ea422821552511f443ac628af80d41020fa1cc99d879bbd302f1bdcc75ee90e`.
  The source supplies neither hint nor solution for either part; neither is
  invented, and O001 gap `LEBL-O001-R006-0033` records that exact state.
- Backend U428 A/B is byte-identical: 27 files / 18,151,570 bytes, 4,015
  records, 856 embedded expressions, 428 manifest bindings, 370 direct checks,
  and 15 lossless CSV round trips. Its 3,292-byte canonical ordinal-POSIX
  inventory has SHA-256
  `77e1b2128513b78305740126ff974949efe6e220c720b66e65b8a09521802275`.
  Receipt: `qa/BACKEND_V0_4_LIVE_U428_20260830.md`, 2,860 bytes, SHA-256
  `f2c945eb6292e943be5587fe7e5f090b31965eddf7bb92c2ccb663a96d0949b7`.
- The U428 fixed-epoch integration build passes at 241 pages / 2,427,826
  bytes, PDF SHA-256
  `b566883b66b32b84edd186a97ae643d7371b4474c3b543b6a6ed0df7f128329f`.
  Passes 3 and 4 are byte-identical across the PDF and seven auxiliaries;
  text, 687 links, 33 outline entries, all 98 embedded font rows, and rendered
  pages 231–233 pass. Page 232 contains complete Indonesian U428 followed by
  the exact untouched English U429 boundary. Unit receipt:
  `qa/R006_FOURIER_JUMP_MIDPOINT_CONVERGENCE_EXERCISE_U428_20260830.md`,
  4,784 bytes, SHA-256
  `b92e9de3c5701590ed5b61315575375ac3c697b0816ce4054e7a9535af764a10`.
- Verified public source boundary: U428 commit
  `0916d113a5ce9d826d3c03fe0c869830c6e37070`, tree
  `3451309d24bd92242a6c0d121614cf57a9827cbc`, with verified U427 controls
  commit `b7a8341fd6f23575c269f7c24a415966227877cc` as its sole parent. The exact
  42-path / 20,107,366-byte payload passed authenticated and anonymous
  immutable-byte readback; its 6,611-byte canonical inventory has SHA-256
  `88c805be563229c26070b48d7dad2f1f8f9c04570ac7771369d96fb4c95ff4df`.
  The finalized U427 receipt was carried exactly. The bounded U428 controls
  overlay is public at commit
  `daa1c9dee22bfcec459d3b54e9f1ab575f6b25be`, tree
  `c928e03799ed2eb10d4c13b4cd589454a20f1755`, with the U428 source commit as
  sole parent. Its exact six paths / 588,985 bytes passed authenticated and
  anonymous readback; canonical inventory SHA-256 is
  `dae6178deae219c0d1779b9bd3b07548f8550d092698e376582b53bc418d27d7`.
  The public receipt snapshot is 5,032 bytes, SHA-256
  `fc0f22ea196b869f25f0f42d42b548aa460fea4633080f7c7a4a58579cee7361`;
  the finalized local receipt is 6,303 bytes, SHA-256
  `fafe5cbc3dabc838fee25e148fe921fc8338028fc5eed39d8ab8296a4e66140f`.
- The public reader remains U397 on GitHub and Zenodo record 22105195; all nine
  files / 12,439,062 bytes remain public and unchanged. U428 is a
  source/backend checkpoint and does not alter that reader release.
- Next executable action: translate the complete exercise with
  remark and explicit hint at source raw lines 5460–5473 / target raw lines
  5474–5487. Keep R007/R008 cursors unchanged.

Recovery rule: begin with this block and the three machine-readable control
files. U428 source commit `0916d113a5ce9d826d3c03fe0c869830c6e37070`
and controls commit `daa1c9dee22bfcec459d3b54e9f1ab575f6b25be`
are already public; do not repeat them. Resume U429 at the exact recorded
lines and carry the finalized U428 receipt with its next substantive
checkpoint. Do not change the U397 reader release and do not contact an
upstream author before the full assigned three-book corpus is complete.

## Historical authoritative recovery snapshot — 2026-08-29 U427

This block is retained as historical evidence and is superseded by the U428
snapshot above.

- Local boundary: U427, manifest 427 (R006 342, R007 35, R008 50), 666,844
  bytes, SHA-256
  `b405f3978aaffaebc0a2344cfdae032a02199daa70c1d54204354e99b63771f2`.
  U427 is the complete integral-representation Fourier-coefficient
  inverse-linear-decay exercise at source raw lines 5415–5426 / target raw
  lines 5429–5440, stable ID
  `ra.v2.fourier-series.exercises.integral-representation-fourier-coefficient-inverse-linear-decay`.
  Its exact target block is 464 bytes, SHA-256
  `25e7b22f29911161b05f50d2f5d6436e38ab3d683323bf08e421217b9bae3d68`;
  the complete target file is 198,209 bytes, SHA-256
  `39bf28512e7f98a00b2cbdbc4fb7824794168c7ceca041052a469d36958d407e`.
  No source hint or solution exists; neither is invented, and O001 gap
  `LEBL-O001-R006-0032` records that state.
- Backend U427 A/B is byte-identical: 27 files / 18,108,960 bytes, 4,011
  records, 854 embedded expressions, 427 manifest bindings, 368 direct checks,
  and 15 lossless CSV round trips. Its 3,292-byte canonical ordinal-POSIX
  inventory has SHA-256
  `48132a45901e66eb0216d2df08b5e2ea03d3e6897a48a865dd2446238c6386a1`.
  Receipt: `qa/BACKEND_V0_4_LIVE_U427_20260829.md`, 2,820 bytes, SHA-256
  `8dcd2deba2c64f1bbb9db6014f847c66b9b1f86242b79564338b816b6367f7d0`.
- The U427 fixed-epoch integration build passes at 241 pages / 2,427,815
  bytes, PDF SHA-256
  `3161b210f7654b1ae6abb7b9c2c8387ebdf9af2e6a4164eef9029aa0236864a2`.
  Its final two passes are byte-identical across the PDF and seven auxiliaries;
  text, links, outline, all 98 embedded font rows, and rendered pages 231–233
  pass. Page 232 contains complete Indonesian U427 followed by the exact
  untouched English U428 boundary. Unit receipt:
  `qa/R006_FOURIER_COEFFICIENT_INVERSE_LINEAR_DECAY_EXERCISE_U427_20260829.md`,
  4,553 bytes, SHA-256
  `af0c5ae5151f21aec6920170cdbdf0a6ec5182552fc75b76aed92e31d32e89db`.
- Verified public boundary: U427 source commit
  `89d415893405d413bc344112a36bfe497bf2e2bd`, tree
  `ef2186c2d65a98acf9835d7560fc5ca57be34fd2`, with verified U426 controls
  commit `b3902ea81953493873c8c5cf7ecf4617c0e2c136` as its sole parent. The exact
  42-path / 20,048,428-byte source/backend payload passed authenticated and
  anonymous immutable readback; its 6,617-byte inventory has SHA-256
  `59bb0972b85e7b3ea8bed0bba6731f535257aace66f5feec55e5240ac6e2d899`.
  The bounded U427 controls commit is
  `b7a8341fd6f23575c269f7c24a415966227877cc`, tree
  `907cfe0eeb0e68cecd35fc15e2e63b06baf51b7c`, with the source commit as sole
  parent. Its exact six-path / 577,053-byte payload has 827-byte inventory
  SHA-256
  `4f90527ec10f505ac531431d62fcc54fc5c14f67d5eb2e5ca66ab22aede9f573`.
  Authenticated and anonymous byte readback passed for both transactions. The
  public receipt snapshot is 4,063 bytes, SHA-256
  `6cdb60014632143b431039365265ff782681010dd201a252bf2db14274063659`;
  the finalized local receipt is 6,191 bytes, SHA-256
  `ade7c8ddcf7898a1237b4236aefd2d4a3eddb2b6fbeba40817f04bce5a9da09a`.
- The public reader remains U397 on GitHub and Zenodo record 22105195; all nine
  files / 12,439,062 bytes remain public and unchanged. U427 is a source/backend
  checkpoint and does not alter that reader release.
- Next executable action: continue the complete two-part R006 exercise at
  source raw lines 5428–5458 / target raw lines 5442–5472. Carry the finalized
  U427 receipt with U428 and keep R007/R008 cursors unchanged.

## Historical authoritative recovery snapshot — 2026-08-29 U426

This block is retained as historical evidence and is superseded by the U427
snapshot above.

- Local boundary: U426, manifest 426 (R006 341, R007 35, R008 50), 664,696
  bytes, SHA-256
  `e6504ab057ae73cd5dff392680cc8ca3ac7c8aca6d6b0ccc4315c6172fc55028`.
  U426 is the complete exponentially decaying sine-series smoothness exercise
  through source raw line 5413 / target raw line 5427. No source hint or
  solution exists; neither is invented, and O001 gap `LEBL-O001-R006-0031`
  records that state. The live target is 198,142 bytes, SHA-256
  `9d0626aa2c1d8cbee2c6740acef767a8e0a4726ca841239c823c6b626e17b993`.
- Backend U426 A/B is byte-identical: 27 files / 18,066,968 bytes, 4,007
  records, 850 embedded expressions, 426 manifest bindings, 366 direct checks,
  and 15 lossless CSV round trips. Its canonical ordinal-POSIX inventory is
  3,292 bytes, SHA-256
  `19a50c7e70392608126019e0d75309cd8fd46652cf3dbd7b230bce02a9d296e2`.
- The U426 fixed-epoch integration build passes at 241 pages / 2,427,800
  bytes, PDF SHA-256
  `9e7f88e73350124a50479b5e1eaea0fc1beb0f183be1417f79488abb841abc91`.
  Passes 10–11 are byte-identical across the PDF and seven auxiliaries; 687
  links, 33 outline items, 98 embedded font rows, text extraction, and rendered
  pages 230–233 pass. Page 232 contains the complete Indonesian U426 exercise
  followed by the exact untouched English boundary.
- Verified public source boundary: U426 source commit
  `e084868c37179d8cc08f4105103c7d93faae912b`, tree
  `c3b72c4478c9c3f7f652fd9164ecddfad1f5ca8b`, with the verified U425 controls
  commit `23835b0329a6397d74889aaf62fc993d02945e0e` as its sole parent. The exact
  42-path / 19,993,559-byte payload passed authenticated and anonymous readback;
  its 6,604-byte inventory has SHA-256
  `1e21ec85b89e294901bdba2dfec2d66bd5c4638beed83df4881117b50d185806`.
  The independently audited U426 receipt snapshot is 4,586 bytes, SHA-256
  `f2bfab515002f5a3ceb8478444457a50b0fbc899e906b5c4908d05db4826afca`.
- The public reader remains U397 on GitHub and Zenodo record 22105195; all nine
  files / 12,439,062 bytes remain public and unchanged. U426 is public as a
  source/backend checkpoint and does not alter that reader release.
- Next executable action: publish the bounded U426 six-path controls overlay
  from the verified U426 source head and complete anonymous readback. After
  closure, continue R006 at source raw lines
  5415–5426 / target raw lines 5429–5440 (`exercise:fsdiffmindecay`).

## Historical authoritative recovery snapshot — 2026-08-29 U425

This block is retained as historical evidence and is superseded by the U426
snapshot above. The machine-readable authorities are
`CURRENT_STATE.json`, `CURRENT_CURSOR.json`, and `PUBLICATION_STATE.json`.

- Local boundary: U425, manifest 425 (R006 340, R007 35, R008 50), 662.792
  bytes, SHA-256
  `d689bac08ef5909b8edb2730dbedfa6ea1910d5ed6b50221fe09fc1293dd2ffe`.
  U425 is the complete one-sided absolutely summable series / analytic
  closed-unit-disc extension exercise through source raw line 5405 / target raw
  line 5419. Its explicit hint is preserved, no solution is invented, and O001
  gap `LEBL-O001-R006-0030` records the source support exactly. The live target
  is 198.123 bytes, SHA-256
  `1c51b2b3490f84c2016ff0e2ac4e347f268fb4568f187773147b3c9703151157`.
- Backend U425 A/B is byte-identical: 27 files / 18.027.168 bytes, 4.003
  records, 850 embedded expressions, 425 manifest bindings, 364 direct checks,
  and 15 lossless CSV round trips. Its canonical ordinal-POSIX inventory is
  3.292 bytes, SHA-256
  `729587820f9ea940bb7f25377705ceb3ed37015e15c3b86d557d541823e3b9e2`.
- The U425 fixed-epoch integration build passes at 241 pages / 2.427.763 bytes,
  PDF SHA-256
  `2166d72eaedfb0bece00d2df99902694c39a0151eb2e8243f568e68587623ba7`.
  Passes 10–11 are byte-identical across the PDF and seven auxiliaries; links,
  outlines, embedded fonts, text extraction, and rendered pages 230–233 pass.
- Verified public boundary: U424 source commit
  `51426054b71910557f3d2a9d166248d65a987258`, tree
  `33c12752c1acb39622367e79304e8b9dbb46e4ab`, followed by controls commit
  `c7951cc776924ebad27d544e4208d749a941b5de`, tree
  `63ef7c3281509c4317b09f4a256ce5a136c2ea7b`. Both bounded transactions and
  their sole-parent chain passed authenticated, anonymous, and independent
  byte readback. The finalized U424 receipt is 5.542 bytes, SHA-256
  `722dde31b78e8134cc04006bbbf447ce1768c8cbf990f91ff651337adc639b76`,
  and must be carried in U425.
- The public reader remains U397 on GitHub and Zenodo record 22105195; all nine
  files / 12.439.062 bytes remain public and byte-identical. U425 is a source
  and backend checkpoint only and does not alter that release.
- Next executable action: continue R006 at source raw lines 5407–5413 / target
  raw lines 5421–5427,
  `ra.v2.fourier-series.exercises.exponentially-decaying-sine-series-smoothness`.
  Carry the finalized U425 receipt with the next substantive checkpoint.

## Historical authoritative recovery snapshot — U422

This block is retained as historical evidence only and is superseded by the
U425 snapshot above.

- Public boundary: U397, manifest 397 (R006 312, R007 35, R008 50),
  605.334 bytes, SHA-256
  `e69eff9f1ab797ccb1be2865bc95999631d6fd5a374d5250db3b4cfb816db347`.
  U309–U312 translate the Section 11.8 opening and complete
  `Polinom trigonometri`, including periodicity, coefficient recovery, the
  real-valued conjugate criterion, and linear independence. ADV-0257 repairs
  the source's undefined zero-frequency antiderivative quotient. The public
  U397 target is 194.506 bytes, SHA-256
  `3de28aaac5ce08b69e97060ea01fe7f1d0e7b9d1c024e2fad49e9ece3893b839`.
- Live boundary: U422, manifest 422 (R006 337, R007 35, R008 50), 657.135
  bytes, SHA-256
  `c0265e1b312b35023764de041f2b122f8b1bb57e0b4ea52099a48535754b2a3b`.
  U422 adds the complete labeled `L^2` triangle-inequality exercise through
  source raw line 5356 / target raw line 5370. Its display, 11 ordered TeX
  commands, four environment events, label, eight brace pairs, and four dollar
  delimiters are exact. No source correction or new term is needed. O001 gap
  LEBL-O001-R006-0027 records neither source hint nor solution. The full live
  target is 197.967 bytes, SHA-256
  `30a7ef6c6675cae45949b3de4e325d0934289238e6789ebcc3c99be431059f2d`.
  Fixed-epoch integration passes 20–21 are byte-identical at 241 pages /
  2.427.736 bytes, SHA-256
  `a45a0e4e7b4cf7fad3c6cc9a7c112eb486ef8a5391567cb4a7239a8bd75436ef`;
  pages 230–231 pass visual inspection.
- Backend U422 A/B is byte-identical: 27 files / 17.886.457 bytes, 3.987
  records, 844 embedded expressions, 796 current logical terms, 268
  corrections, 33 assets, 648 relations, and 27 O001 gaps. All 422 live unit
  bindings and 358 direct component checks pass, generic validation passes,
  and all 15 CSV views round-trip losslessly. The platform-neutral canonical
  inventory uses ordinal POSIX-relative-path ordering; its SHA-256 is
  `312fb8f903cb19492d2dd6194c09fc69c49e9fd265e39c18d52c9b2a3368ecbf`.
  The live builder is 78.347 bytes, SHA-256
  `77522ade28f62fc94110dc870917f91a21b0720905a9b73a51f328e0aa159bbb`,
  and now validates optional contextual source/target hint selectors and
  hashes fail closed while preserving inline-hint detection as a fallback.
- GitHub main preserves the complete U422 live source/backend checkpoint at
  immutable commit `390716d4701fa450e65e93c7ab9c7dc6c7752e6b`, tree
  `44d02db5895d5866626cc437b04c126467c4ca16`. Its sole parent is the verified
  U421 controls commit `e76a90911c7966f7fdd12987359e73cc0929526b`.
  Authenticated and anonymous immutable readback matched all 42 bounded paths /
  19.749.150 bytes; the canonical 6.599-byte inventory has SHA-256
  `4afc7f9419a2655bbf58f3156cc0b77237dccfbdc152fc310d844f7ccbe5a4b1`.
  The recursive tree is untruncated at 1.627 entries, and an independent second
  audit repeated the branch, parent, tree, blob, and raw-byte checks. Receipt:
  `publication/live-2026.08.29-u422/GITHUB_MAIN_U422_RECEIPT.md`, 3.779 bytes,
  SHA-256
  `3cfab748096faf41f9c7d04e7f29973c90550b57a8297bff2ea65abd1f1111dc`.
  The bounded follow-up controls commit is
  `219d65a5d81a07c86509421df147c8875939bb2f`, tree
  `8250513929d898d38523b2ff30a8103e980ab00c`, with the source commit as its
  sole parent. Authenticated and anonymous immutable readback matched all six
  paths / 517.185 bytes; the 827-byte canonical inventory has SHA-256
  `026a6f0b6c74f056a9627e8a49fab8694e86cdcbbbf6e016967e820c037a6754`,
  and an independent second audit passed. The finalized local receipt is 5.133
  bytes, SHA-256
  `dc111dc126653ffc60b1086aa05e02d318573efc95444f3c7618c74a3c8cfa4e`,
  and must be carried by the next substantive checkpoint. No release, tag, or
  Zenodo object changed; an independent preservation audit reconfirmed all nine
  U397 release assets / 12.439.062 bytes.
- Centered U397 reader PASS: 226 pages / 2.292.242 bytes, SHA-256
  `40b2e2cb27dd59d288ef76453ae293558fcd1ae8efb96e1e87a646f8f0b8f73d`.
  The final nine-pass build has zero TeX/reference failures and zero visible
  `??` or placeholders; 85/85 font objects are embedded, 1.227/1.227 named
  destinations and all 644 links are valid, pages 216–217 are centered within
  three pixels at 144 dpi, and an independent final-byte audit passed. Receipt:
  `qa/R006_FOURIER_TRIGONOMETRIC_POLYNOMIAL_READER_U397_20260826.md`,
  5.996 bytes, SHA-256
  `719330ff435534e81459e82ff46eac736d12ef9734871033e8d120f114338824`.
- GitHub release
  `https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.26.u397`
  and Zenodo DOI `10.5281/zenodo.22105195` expose the identical nine-file /
  12.439.062-byte U397 payload. Anonymous downloads matched every local
  filename, byte count, and SHA-256 on both providers; the Zenodo concept
  latest endpoint resolves to record 22105195. Sanitized receipts are
  `publication/wip-2026.08.26-u397/GITHUB_PUBLICATION_RECEIPT.md` and
  `publication/wip-2026.08.26-u397/ZENODO_PUBLICATION_RECEIPT.md`. Narrow
  post-publication state commit
  `007128997ddcbd448ff26cd97556b2a3f9de2035` (tree
  `7488ae6658145a5e518825064cd455a30e7b59aa`) contains those receipts and all
  seven bounded controls/receipts; anonymous readback matched all 408.484 bytes.
  Final pointer commit `57211953210933e7bcaf6165b2d04587fcd00200`
  (tree `4d845894ee625231d4c2357cc3f567ff15a87009`) also passed anonymous
  readback for all seven files / 409.835 bytes. Neither commit changed the U397
  release tag or Zenodo record.
- Resume only R006 with the complete unlabeled decaying-sine-series and
  forced-ODE exercise at source raw lines 5358–5385 / target raw lines
  5372–5399. Preserve the verified U422 source and controls checkpoints and do
  not change the U397 release.
  R007 remains at
  `ch-first-order-ode.tex` raw line 89; R008 remains at `ca.tex` raw line 1648.
  HP-LEBL-R007-001 is owner-accepted only for complete
  `ch-nonlin-systems.tex`; the live owner target, not the uncorrected helper
  copy, remains authoritative. There is no range conflict.

## Exact scope

This lane owns only:

1. R006 — Jiří Lebl, *Basic Analysis I–II*, curriculum roles C10/C20.
2. R007 — Jiří Lebl, *Notes on Diffy Qs: Differential Equations for
   Engineers*, curriculum role B70.
3. R008 — Jiří Lebl, *Guide to Cultivating Complex Analysis*, curriculum role
   C50.

It is not the curriculum-selection or global-hub coordinator. It must produce
one coherent family handoff while preserving separate edition, source, license,
unit, and artifact identities per book.

## User authority

Read the entire the user-authored file, including its preface:

- path: `%USERPROFILE%/Documents/Obsidian notes/Untitled 1693.md`
- bytes: `10476`
- SHA-256: `cf913e8cb4d487f4c6958c079b372ccbb2fb5929dd483068441e80cefd6794f2`

Later user corrections bind this thread to R006/R007/R008 only. Translation is
the focus; QA supports it and must not become the work product.

## Workspace safety

No broad or recursive Git operation is permitted. Narrow operations limited to
this Lebl-family lane are allowed when they become an ordinary release step.
Current workspace rules and the user's direct correction supersede stale
conversational confirmation gates. The user explicitly directed that the
public repositories remain maintained even while the corpus is incomplete, so
  clean, explicitly labeled, nonduplicative WIP checkpoints are published after
  their bounded gates and public-byte readback. The current Zenodo version is
  `10.5281/zenodo.22105195` in concept lineage
  `10.5281/zenodo.22059779`; the latest-version endpoint resolves record
  `22105195`. GitHub access is healthy; release commit
  `a35de2ff999291c3414d6ba319f16bb149c7d5f5` and U397 were published and
  anonymously verified. The exact authorized Figshare credential path was absent
on 2026-08-26, so no account call, mutation, or duplicate was made. Every
current or future
reader, repository description, release payload, and preservation record must
identify the runtime generically as acting on the user's instruction; it must
not publish the user's personal first name. Historical immutable releases are
evidence, not inputs to a new payload.

The local authoritative checkpoint is U416: R006 U001–U331, R007 U001–U035,
and R008 U001–U050. The public repository `main` binds the verified U416
source/backend payload and receipt/current-controls overlay. The separate
U397 reader release
binds its 397-row manifest: R006 U001–U312, R007 U001–U035, and R008 U001–U050,
and contains nine anonymously verified assets totaling 12.439.062 bytes. The
primary current reader is the centered 226-page Volume II
PDF through complete Subsection 11.8.1, `Polinom trigonometri`. GitHub and
Zenodo receipts are under `publication/wip-2026.08.26-u397/`; the last bounded
Figshare-attempt receipt remains historical evidence under
`publication/wip-2026.08.26-u393/`. Earlier versions remain public evidence.

## Production requirements

- Recover any existing Lebl captures or Indonesian work before duplication.
- Bind exact upstream repositories, commits/trees/tags or archives, releases,
  active source closure, licenses, assets, dependencies, and build baselines.
- Treat “freeze” as an immutable reproducibility receipt, not a ban on additive
  indexing, schema, or build improvements in the derivative.
- Verify the actual license route separately for all three works. Preserve any
  dual-license choice and component-specific code/media terms.
- Translate contiguously into natural `id-ID` from the mathematical source.
- Preserve source topology, formulas, identifiers, xrefs, figures, code,
  exercises, hints/answers/solutions, accessibility text, and attribution.
- Never invent missing R006/R008 solutions during ordinary translation. Map
  mastery gaps for O001. For R007, also map proof/modeling needs and public
  solution coverage.
- Log every source correction as a separate typed delta.
- Maintain a shared terminology ledger with per-book scope.

## Modular backend requirement

The lane must satisfy:

`outputs/01a01ec1-e685-70d0-b022-211396334723/curriculum_logbook/05_MODULAR_BACKEND_INTEROPERABILITY_V0.md`

The lane may improve the storage model, but must deterministically export all
required resource, edition, unit, concept, segment, term, asset, relation,
rights, correction, QA-event, and artifact entities. Semantic IDs are
locale-neutral and cannot depend solely on translated titles or page numbers.
Exports must be schema-versioned, UTF-8, deterministic, and round-trip tested.

## Publication and upstream contact

Maintain the individual Lebl-family mirror/fork and a future central-hub
handoff. The corpus remains incomplete. The verified source mirror and WIP
prerelease are public at
  <https://github.com/KokunoYumeto/lebl-mathematics-family-id>; the current
  preservation version is <https://zenodo.org/records/22105195>. The public
Figshare collection remains `10.6084/m9.figshare.c.8668413.v43`, but its
account route was not called at U393 because its exact authorized credential
  path was absent; do not create a duplicate to bypass that failure. See
  `PUBLICATION_STATE.json` and the U397 GitHub/Zenodo publication receipts. Do not contact
authors during production. Only after the
full three-book corpus is complete may at most one concise, high-confidence,
deduplicated upstream issue be sent if the tracker permits it. It must disclose
that Codex acted on the user's request and must not initiate chatbot-style
correspondence. A ready, nonduplicative release is published automatically; no
later confirmation is requested.

## Recovery order

1. Read this file.
2. Read `CURRENT_STATE.json`, `CURRENT_CURSOR.json`, and the tail of
   `DECISION_LOG.jsonl` and `ADVERSE_LEDGER.jsonl`.
3. Verify the instruction-file hash above.
4. Read `PUBLICATION_STATE.json`, `RIGHTS_COMPONENTS.csv`, and
   `TERMINOLOGY.csv`.
5. Read `backend/README.md` and the v0 envelope.
6. Read the exact per-book authority/build receipts once created.
7. Resume only the `next_action` in `CURRENT_CURSOR.json` unless new user
   instruction explicitly supersedes it.

Do not use a compaction summary as authority when these records exist.

## Historical production detail

The detailed chronology below is retained as evidence. Any older count, cursor,
or publication URL in it is superseded by the authoritative recovery snapshot
above and the three current-state JSON files.

- R006 uses release v6.3 commit `00f5a8635cfba0d908cd95da53068572f30687b1`;
  its exact 312-page source-compatible baseline is proved in
  `qa/R006_V63_BUILD_BASELINE.md`.
- R007 uses release v6.11 commit
  `066f96506d0954cc3efb900db0d68d121733b2dc`; R008 uses release v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`. Their exact archive and license
  receipts are `authority/R007_AUTHORITY.md` and `authority/R008_AUTHORITY.md`.
- R006 admitted units are enumerated—not inferred—in
  `translation/TRANSLATION_MANIFEST.jsonl`. There are currently 261 R006 rows;
  Volume I is complete.
  Volume II
  Chapters 1 and 2 are complete. Volume II Chapter 3 is admitted through the
  full Riemann-integral and Fubini sections and through Outer measure and null
  sets through all 16 exercises and the Cantor-function figure, completing that
  section, plus the complete *Oscillation and continuity* subsection, the
  Riemann--Lebesgue/Lebesgue--Vitali theorem, its four-part closure corollary,
  and all 13 exercises. The *set of Riemann integrable functions* section is
  complete. The oscillation checkpoint is bound by
  `qa/builds/ra-id-volume2-oscillation-continuity-20260822/BUILD_RECEIPT.md`.
  The theorem checkpoint is bound separately by
  `qa/builds/ra-id-volume2-riemann-lebesgue-20260822/BUILD_RECEIPT.md`.
  The corollary checkpoint, including a revalidation of the theorem's final
  Indonesian wording, is bound by
  `qa/builds/ra-id-volume2-riemann-integrable-corollary-20260822/BUILD_RECEIPT.md`.
  The complete exercise block and its readable cases reflow are bound by
  `qa/builds/ra-id-volume2-riemann-integrable-exercises-20260822/BUILD_RECEIPT.md`.
  The *Jordan measurable sets* opening, characteristic/indicator definition,
  volume, boundary criterion, set operations, and outer-measure equality are
  bound by `qa/builds/ra-id-volume2-jordan-volume-20260822/BUILD_RECEIPT.md`.
  The complete *Integration over Jordan measurable sets* subsection, including
  its repaired type-I formula and accessible figure, is bound by
  `qa/builds/ra-id-volume2-jordan-integration-20260822/BUILD_RECEIPT.md`.
  The complete *Images of Jordan measurable subsets* subsection and its
  repaired inverse-map identifier are bound by
  `qa/builds/ra-id-volume2-jordan-images-20260822/BUILD_RECEIPT.md`.
  All nine Jordan-measurability exercises and their explicit zero-extension
  repair are bound by
  `qa/builds/ra-id-volume2-jordan-exercises-20260822/BUILD_RECEIPT.md`,
  completing the section. The Green's-theorem opening, bounded-domain
  definition, componentwise orientation repair, and accessible orientation
  figure are bound by
  `qa/builds/ra-id-volume2-green-domain-orientation-20260822/BUILD_RECEIPT.md`.
  The following Jordan-measurability proposition and null-path-image proof are
  bound by
  `qa/builds/ra-id-volume2-green-jordan-measurability-20260822/BUILD_RECEIPT.md`.
  The Green theorem statement, general-to-special reduction, type-I/II/III
  domain setup, localized figure labels, and full alternative text are bound by
  `qa/builds/ra-id-volume2-green-statement-types-20260822/BUILD_RECEIPT.md`.
  That checkpoint also binds the one-time Indonesian field-usage terminology QA
  and exact `OpenAI Codex gpt-5.6-sol, Ultra` provenance in every reader driver;
  detailed evidence is in
  `authority/terminology_evidence/2026-08-22-indonesian-field-usage-qa/TERMINOLOGY_QA_REPORT.md`.
  The complete proof of Green's theorem for type-III domains is bound by
  `qa/builds/ra-id-volume2-green-type-iii-proof-20260822/BUILD_RECEIPT.md`.
  The following complete vortex-field application, punctured-rectangle
  decomposition, clockwise-circle computation, accessible figure, and
  origin-detection conclusion are bound by
  `qa/builds/ra-id-volume2-green-vortex-example-20260822/BUILD_RECEIPT.md`.
  The complete harmonic-function mean-value-property example is bound by
  `qa/builds/ra-id-volume2-green-harmonic-mean-value-20260823/BUILD_RECEIPT.md`.
  The complete seven-exercise block and Green-section completion are bound by
  `qa/builds/ra-id-volume2-green-exercises-20260823/BUILD_RECEIPT.md`.
  Both examples and the exercise block pass strict raw-math, structural,
  mathematical, terminology, converged-build, extraction, privacy, and visual
  checks. The complete change-of-variables section opening and its
  one-dimensional substitution plus volume/length/determinant motivation are
  bound by
  `qa/builds/ra-id-volume2-change-vars-opening-20260823/BUILD_RECEIPT.md`.
  That checkpoint revalidates the stored one-time arXiv/fallback terminology
  evidence, records that no additional term change is justified, and proves the
  235-page QA build plus physical page 151. Proposition 10.7.1, Theorem 10.7.2,
  and the theorem's complete proof are bound by
  `qa/builds/ra-id-volume2-change-vars-theorem-20260823/BUILD_RECEIPT.md`.
  The complete six-exercise block is bound by
  `qa/builds/ra-id-volume2-change-vars-exercises-20260823/BUILD_RECEIPT.md`;
  it completes Section 10.7 and `ch-multivar-int.tex`, applies the bounded
  correction `LEBL-ID-ADV-0221`, and records the unresolved source defect
  `LEBL-ID-ADV-0222` without a speculative rewrite. The Chapter 11 continuation
  now reaches the complete *Power series as analytic functions* subsection at
  source raw line 1554 and target raw line 1549 (R006 U265). The exact next
  cursor is `\subsection{Identity theorem for analytic functions}` at source
  raw line 1556 and target raw line 1551. U255–U265 and their eleven receipts
  under `qa/` bind the completed opening and four full subsections.
  `LEBL-ID-ADV-0226` records the
  source proof's missing uniform-tail/M-test step without silently altering it;
  `CURRENT_CURSOR.json` is authoritative.
- The exact 318-page partial Indonesian Volume I checkpoint, its build log,
  warning disposition, explicit `/Lang=id-ID`, and fifteen visual witnesses are bound by
  `qa/R006_ID_TRANSLATION_CHECKPOINT_20260820.md`. This proves the stated
  checkpoint only; it is not a whole-book completion claim.
- The shared backend v0.1 production checkpoint under `backend/production`
  validates 210 records from the retained 19-unit boundary. Backend v0.2 is a
  separately retained deterministic checkpoint built from the frozen 26-unit
  manifest: 526 records, typed converter/build QA metrics, schema and reference
  validation, 15 losslessly round-tripping CSV views, and two-run byte identity.
  Backend v0.3 is the separately frozen, schema-valid, round-trip and
  byte-deterministic 167-unit checkpoint. The authoritative additive
  mixed-resource v0.4 checkpoint is
  `backend/production/v0.4-live-2026.08.23-u319-tqa-a`; it validates 2,650
  records from all 319 live manifest units (R006 254, R007 15, R008 50), passes
  schema and referential-integrity validation, and losslessly round-trips all
  2,650 records through 15 CSV projections. Its independent replay at
  `backend/production/v0.4-live-2026.08.23-u319-tqa-b` is byte-identical across
  all 26 files and 11,227,185 bytes. Both `VALIDATION.json` files are 7,573
  bytes with SHA-256
  `e8b431ee42608c8b549d78048e29410a8e603214d208bcdc4a9b815e0a1269f5`;
  the record-stream SHA-256 is
  `062f7e040cc79ac7b8c428bfd2b7149a831262402a69d46800242ae1efc01c29`.
  The current local continuation is
  `backend/production/v0.4-live-2026.08.24-u330-figfix-a`: 2,683 records from
  330 units after binding the localized Figure 11.6 overlay, all 15 CSV views
  losslessly round-tripped, 26 files and 11,495,077 bytes. Its replay
  `-u330-figfix-b` is byte-identical, with canonical tree inventory
  SHA-256
  `8c60d50e03a80441dcc5e73ba398ab37f1b258048cb34368d44d474296ac68df`.
  The pre-figure-fix U330 pair is superseded and must not be packaged.
  U323 and U326 remain local historical witnesses; U330 is the current
  authoritative backend for the next release.
  Never
  treat example fixtures or an older backend snapshot as current corpus truth.
- The first source correction is `LEBL-ID-ADV-0002`: the inverse image of a
  singleton under a bijection is a singleton set, not itself an element. The
  complete current correction set is enumerated through `LEBL-ID-ADV-0226` in
  `ADVERSE_LEDGER.jsonl`. No author has been contacted; candidates remain
  internal until one final high-confidence deduplicated disposition after all
  three books.

## Live continuation checkpoint — 2026-08-24

The live manifest is the authoritative unit ledger and contains exactly 333
valid JSONL rows: R006 U001–U268 (268 rows), R007 U001–U015 (15 rows), and R008
U001–U050 (50 rows). It is 478,547 bytes with SHA-256
`de03bdf56a20104420dde65bbb47778189f58a97134b6867aa32f6cbd1ba0385`.
The deterministic U333 backend contains 2,692 records and 333 units; its two
independent 26-file trees contain 11,574,002 bytes each and are byte-identical
with canonical inventory SHA-256
`d0aac7d8017ba5f6540f5fa1ab344982146ab35347d7f7337d38513948823bf1`.
The **public continuation boundary remains U330**. GitHub `main` and release tag
`lebl-family-id-wip.2026.08.24.u330` bind commit
`2f375c7a5578595e7e12cbe3a5ae11a6ed01a237`; Zenodo version
`10.5281/zenodo.22074515` is the latest version in the existing concept
`10.5281/zenodo.22059779`. Both destinations expose exactly eight files / 
  12,625,918 bytes. Every file was anonymously downloaded and matched by byte
count and SHA-256. Zenodo's IIIF thumbnail selects the corrected 188-page R006
  Volume II reader through complete Subsection 11.3.4. The Identity theorem is
  not included in that public reader. Receipts are under
  `publication/wip-2026.08.24-u330/`. Local translation has since advanced to
  U332: the complete Identity-theorem subsection is bound by
  `qa/R006_IDENTITY_THEOREM_U266_20260824.md`, and the complete 11-exercise
  section is bound by `qa/R006_POWER_SERIES_EXERCISES_U267_20260824.md`.

- R006 next: resume source and target `ch-approximate.tex` at raw line 1863,
  *Trigonometric functions and \(\pi\)*, using the revalidated field choices
  `fungsi trigonometri` and `rumus Euler`. U268 completes the full
  *Complex exponential* subsection, including the exponent law, proof,
  accessible figure text, and expansion at an arbitrary center; the public
  U330 reader remains unchanged.
- R007 next: continue `source/diffyqs-v6.11/ch-first-order-ode.tex` and its
  Indonesian target at raw line 89. U015 binds the definite-integral solution
  for an initial condition and its verification.
- Helper packet `HP-LEBL-R007-001` was owner-verified and admitted only for the
  complete, disjoint `ch-nonlin-systems.tex` chapter at pinned Diffy Qs v6.11
  commit `066f96506d0954cc3efb900db0d68d121733b2dc`. All 66 packet hashes,
  dependency closure, labels, mathematics, terminology, figures, full build,
  39-page visual surface, 20 stable units, and backend integration passed.
  The active first-order cursor remains raw line 89; no R006/R008 boundary
  changed. Evidence is `qa/R007_NONLINEAR_SYSTEMS_HP001_U357_20260824.md`.
- R008 next: source `ca.tex` raw line 1648, Linear fractional transformations.
  U050 closes the Riemann-sphere section through partial infinity arithmetic.
- Terminology QA is complete and recorded in
  `authority/terminology_evidence/2026-08-22-indonesian-field-usage-qa/TERMINOLOGY_QA_REPORT.md`.
  The arXiv candidate was rejected as English. Indonesian academic fallbacks,
  including the 48-page *Analisis Real (Bahan Ajar)*, were inspected directly.
  Preferred `lingkungan` and `subbarisan` remain; attested variants and the
  general `ketaksamaan` entry are recorded without unjustified mass rewriting.
  The exact provenance string is
  `OpenAI Codex gpt-5.6-sol, Ultra`.
- No author contact has occurred. Keep all source defects in the adverse ledger
  until the one permitted post-completion upstream disposition.

## Complete to-do list

- [x] Bind lane boundary and create durable goal.
- [x] Verify the canonical instruction file.
- [x] Perform bounded explicit-path recovery for existing Lebl material.
- [x] Verify official upstream repositories/releases/licenses from primary
      authorities without Git.
- [x] Capture exact source archives and create immutable authority receipts.
- [ ] Prove clean upstream builds and enumerate active source/asset closure
      (R006 PDF baseline proved; R007/R008 authority bound and first units
      admitted, full-driver gates still pending).
- [x] Finalize backend schema v0.1 and deterministic exporters/validators.
- [ ] Populate per-book unit, rights, exercise-solution, and asset inventories.
- [x] Establish the shared id-ID terminology baseline; extend it at first use.
- [ ] Translate contiguously, updating cursor and manifests at boundaries.
      Current admitted boundary: R006 U280 through the compact-space
      countable-dense-subset proposition and proof; R007 U015 through the initial-value
      integral formula plus the complete disjoint nonlinear-systems chapter as
      20 owner-admitted units; and R008 U050 through the complete Riemann-sphere
      section. Exact next cursors are recorded in `CURRENT_CURSOR.json`.
- [x] Validate and owner-merge `HP-LEBL-R007-001` as the complete 20-unit
      nonlinear-systems chapter without disturbing the active first-order ODE
      cursor; verify all packet hashes, dependencies, mathematics, terminology,
      assets, backend records, full book build, and reader pages.
- [x] Rebuild the mixed-resource backend at the U319 boundary and prove an
      independent byte-identical replay: 2,650 records, 15 losslessly
      round-tripping CSV views, 26 files, and zero A/B differences.
- [x] Rebuild the mixed-resource backend at the corrected U330 boundary and
      prove an independent byte-identical replay: 2,683 records, 15
      losslessly round-tripping CSV views, 26 files, and zero A/B differences.
- [ ] Build and audit source/PDF; add other formats only where additive.
- [x] Build and independently audit the corrected 188-page U330 Volume II
      reader through complete Subsection 11.3.4; localize Figure 11.6 labels,
      embed all 78 fonts, and inspect pages 170–188 plus every overfull page.
- [ ] Prepare the central-hub handoff; the individual GitHub mirror is public
      and anonymously verified at the U361 boundary.
- [x] Publish and anonymously verify the clean U214 WIP checkpoint on GitHub
      and the Zenodo lineage `10.5281/zenodo.22059779`; publish and verify the
      exact-license-safe Figshare metadata/link item.
- [x] Supersede U214 with the privacy-safe U216 GitHub prerelease and Zenodo
      version `10.5281/zenodo.22062325`; verify all public bytes and update the
      same Figshare metadata/link item to public version 2.
- [x] Supersede U216 with the privacy-safe U219 section-complete GitHub
      prerelease and Zenodo version `10.5281/zenodo.22062970`; verify all public
      bytes, the reader-first Zenodo preview, and update the same zero-file
      Figshare metadata/link item to public version 3.
- [x] Admit and independently verify local U220, the Section 10.7 opening, after
      revalidating the one-time Indonesian field-usage terminology evidence and
      exact model provenance; keep the public preservation boundary at the
      coherent U219 section completion until the next substantial release.
- [x] Admit and independently verify local U227 through the complete
      change-of-variables theorem proof, correct the retained terminology
      evidence provenance, and prepare the coherent theorem-complete release.
- [x] Publish and anonymously verify the U227 GitHub prerelease and Zenodo
      version `10.5281/zenodo.22063321`; update the same zero-file Figshare
      metadata/link item to public version 4 and verify its project and
      Indonesian-collection membership.
- [x] Admit and independently verify local U228 through all six Section 10.7
      exercises; preserve the exact topology and mathematics, record
      `LEBL-ID-ADV-0221` and `LEBL-ID-ADV-0222`, and pass converter, converged
      TeX, extraction, font, privacy, and final-page visual gates.
- [x] Publish and anonymously verify the U228 GitHub prerelease at commit
      `e6542057669a8e5256d5d89890a30823ab7f635b` and Zenodo version
      `10.5281/zenodo.22070430`; set the newest Volume II reader PDF as the
      default preview and verify all eight public files byte-for-byte. Attempt the
      existing Figshare item update; leave public v4 intact after the bounded
      `InactiveAccount` response and record the exception.
- [x] Publish and anonymously verify the consolidated U310 checkpoint at GitHub
      commit `3a870747b074115af7fd4a7e767734e404e7a63a`, release tag
      `lebl-family-id-wip.2026.08.23.u310`, and Zenodo version
      `10.5281/zenodo.22071911`; verify all eight assets byte-for-byte and set
      the 176-page Volume II reader through Continuity as Zenodo's default
      preview. Preserve the existing Figshare v4 item without duplication.
- [x] Admit and independently review R006 U252, R007 U013, and R008 U048;
      propagate the glossary-consistent `metrik Euklides` correction in U048,
      rebuild the deterministic U313 backend, and repair the command-line
      validator so self-contained versioned schema bundles validate correctly.
- [x] Admit and independently review R006 U253, R007 U014, and R008 U049;
      rebuild the deterministic U316 backend with 2,641 records, and verify its
      command-line schema validation and complete 15-view CSV round-trip.
- [x] Admit and independently review R006 U254, R007 U015, and R008 U050;
      correct the two retained English cases strings found by review, close the
      R006 Swapping limits and R008 Riemann-sphere sections, and verify the
      deterministic 2,650-record U319 backend and independent replay.
- [x] Build, visually audit, and publish the corrected section-complete U319
      reader checkpoint on the existing GitHub and Zenodo lineages. The
      180-page reader SHA-256 is
      `303ec82e16d133e938247f6611e31e36cb435ff0285a7b33fbbf4f8a5eb91725`;
      all eight assets at each destination passed anonymous byte readback.
- [x] Build, visually audit, and publish the corrected U330 reader through
      complete Subsection 11.3.4 on the existing GitHub and Zenodo lineages.
      GitHub commit `2f375c7a5578595e7e12cbe3a5ae11a6ed01a237`, release tag
      `lebl-family-id-wip.2026.08.24.u330`, and Zenodo version
      `10.5281/zenodo.22074515` expose the same eight files / 12,625,918 bytes;
      all public bytes, the latest-version relation, and reader-first preview
      passed anonymous verification.
- [x] Publish and anonymously verify U333 on the same GitHub and Zenodo
      lineages. GitHub commit
      `01a822f2890bcc00f717a8c6451ff9cbc538be5a`, release tag
      `lebl-family-id-wip.2026.08.24.u333`, and Zenodo version
      `10.5281/zenodo.22076849` expose the same eight files / 14,158,094 bytes.
      The concept DOI resolves to U333, every anonymous download matches, and
      Zenodo's IIIF preview names the new 192-page Volume II reader.
- [x] Rebuild and independently replay the local U332 backend: 2,689 records,
      332 units, 15 lossless CSV views, 26 files / 11,548,659 bytes per tree,
      schema and referential-integrity PASS, and zero A/B byte differences.
- [x] Rebuild and independently replay the local U333 backend: 2,692 records,
      333 units, 15 lossless CSV views, 26 files / 11,574,002 bytes per tree,
      schema and referential-integrity PASS, and zero A/B byte differences.
- [x] Build and visually audit the 192-page local U333 Volume II reader through
      complete Subsection 11.4.1, *Eksponensial kompleks*. The converter,
      five-pass TeX convergence, index, glossary, extraction, privacy, embedded
      fonts, navigation, pages 170–192, and every overfull-page render pass;
      accepted reader SHA-256 is
      `6f1f38221af120d6459cdc217e789ca1f7a9d4f353f5720db00ff271ce637061`.
- [x] Translate and independently audit U229/U230, `ch-approximate.tex` raw
      lines 5--94; record exact slice hashes and the next cursor in
      `qa/R006_COMPLEX_PLANE_U229_U230_20260823.md`.
- [x] Translate and independently audit U231, `ch-approximate.tex` raw lines
      96--195 (target lines 96--193); record exact slice hashes, terminology
      decision, provenance, and the next cursor in
      `qa/R006_COMPLEX_PLANE_U231_20260823.md`.
- [x] Translate and independently audit U232, `ch-approximate.tex` raw lines
      197--245 (target lines 195--240); preserve the stable source label typo
      `prop:cachysercomplex`, record `LEBL-ID-ADV-0223`, and bind exact slice
      hashes/provenance in `qa/R006_COMPLEX_SERIES_U232_20260823.md`.
- [x] Translate and independently audit U233, `ch-approximate.tex` raw lines
      246--280 (target lines 242--275); bind exact slice hashes, provenance,
      and the next Exercises cursor in
      `qa/R006_COMPLEX_VALUED_FUNCTIONS_U233_20260823.md`.
- [x] Translate and independently audit U234, `ch-approximate.tex` raw lines
      283--359 (target lines 278--354); preserve the matrix-exercise prose
      defect as `LEBL-ID-ADV-0224` and bind exact slice hashes and the next
      `Swapping limits` cursor in `qa/R006_COMPLEX_EXERCISES_U234_20260823.md`.
- [x] Translate and independently audit U266, the complete Identity-theorem
      subsection at source lines 1556--1630 and target lines 1551--1629; bind
      the mathematically necessary recentering and relative-topology repair as
      `LEBL-ID-ADV-0227`.
- [x] Translate and independently audit U267, all 11 Power-series exercises at
      source lines 1632--1768 and target lines 1631--1768; bind the zero-function
      and local-domain repairs as `LEBL-ID-ADV-0228` and `LEBL-ID-ADV-0229`.
- [x] Translate and independently audit U268, the complete Complex-exponential
      subsection at source and target lines 1770--1862; preserve all 48
      mathematical expressions and clarify the source's panel-ambiguous figure
      alternative text without changing its represented mathematics.
- [x] Translate and independently audit U269, the complete Trigonometric
      functions and pi subsection at source lines 1864--2096 and target lines
      1863--2106. Preserve all 24 displays and 13 proposition items; bind the
      positive-period, first-zero supremum, minimal-period/injectivity, and
      quadrant repairs as `LEBL-ID-ADV-0230` through `LEBL-ID-ADV-0233`.
- [x] Rebuild and independently replay the local U334 backend: 2,695 records,
      334 units, 668 expressions, 15 lossless CSV views, 26 files / 11,604,713
      bytes per tree, schema and referential-integrity PASS, and zero A/B byte
      differences. The canonical inventory SHA-256 is
      `11c69cc880d3a31c6f9221601c3e39b49f654696da4128b7d92f1bed069865a5`.
- [x] Translate and independently audit U270 at frozen source lines 2097--2140
      and live target lines 2107--2150, *The unit circle and polar coordinates*.
      Preserve all four displays and bind the curve-regularity,
      parametrization-endpoint, and exponent-domain repairs as
      `LEBL-ID-ADV-0234` through `LEBL-ID-ADV-0236`.
- [x] Translate and independently audit U271 at frozen source lines 2141--2261
      and live target lines 2151--2271. Preserve all eleven unsolved exercises,
      the stable `exercise:cossinidentity` label, three displays, and exact
      environment topology; bind the tangent/inverse-derivative domain and
      convergence-scope repairs as `LEBL-ID-ADV-0237` through
      `LEBL-ID-ADV-0239`.
- [x] Build and visually audit the 198-page U336 reader through complete
      Section 11.4. The formerly visible forward reference now resolves and
      extraction contains zero literal `??`; all 80 fonts are embedded and
      fresh pages 185--193 pass. Promoted reader SHA-256 is
      `78543d4e8087e68589e8f15d0a3a969b3282247c7c9c2cdcb6f658dfa4b68e4f`.
- [x] Rebuild and independently replay the local U336 backend: 2,701 records,
      336 units, 672 expressions, 15 lossless CSV views, 26 files / 11,659,282
      bytes per tree, schema and referential-integrity PASS, and zero A/B byte
      differences. Canonical inventory SHA-256 is
      `e39eec0b1c05b39a274ffc6fa1f23408e81c8d163a76bb4d6d8339cfb4be2321`.
- [x] Publish the coherent U336 checkpoint to the individual GitHub mirror and
      the existing Zenodo concept lineage. GitHub commit
      `53a3551ed8164aab5a9a28892e8177e18bfa2951`, release
      `lebl-family-id-wip.2026.08.24.u336`, and Zenodo version DOI
      `10.5281/zenodo.22082567` each expose the same eight substantive files /
      15,665,220 bytes. Anonymous readback of the public manifest and every
      release file passed; receipts are under
      `publication/wip-2026.08.24-u336/`.
- [x] Translate and independently audit R006 U272 at frozen source lines
      2262--2341 and live target lines 2272--2351: the Maximum-principle
      section opening and complete first minimum-modulus lemma and proof.
      Preserve `sec:fundalgeb`, `lemma:polyalwaysgetssmaller`,
      `exercise:minprinciple`, all 18 inline expressions, all four displays,
      and the exact 80-line topology; evidence is bound in
      `qa/R006_MAXIMUM_PRINCIPLE_OPENING_LEMMA_U272_20260824.md`.
- [x] Rebuild and independently replay the local U337 backend: 2,704 records,
      337 units, 674 expressions, 15 lossless CSV views, 26 files /
      11,684,846 bytes per tree, schema and referential-integrity PASS, and
      zero A/B byte differences. Canonical inventory SHA-256 is
      `54928313efea8de8b2e3b416ce02de6c09984dbf87c3eb77d71d95ee128b61cf`.
- [x] Record HP-LEBL-R007-001 as a disjoint owner-QA handoff for only complete
      `ch-nonlin-systems.tex` at Diffy Qs v6.11 commit
      `066f96506d0954cc3efb900db0d68d121733b2dc`. It does not change ownership
      or the active `ch-first-order-ode.tex` cursor and excludes all R006/R008
      material. Verify the packet personally before any label/stable-ID merge.
- [x] Owner-admit HP-LEBL-R007-001 after verifying 66/66 packet hashes, exact
      v6.11 source identity, 28 figure records and two bibliography spans,
      1,591 commands, 444 environment boundaries, 735 inline and 70 display
      payloads, 31 labels, 20 dependency-aware units, a converged 472-page full
      build, and all 39 chapter pages. Produce the centered 40-page partial
      reader with an explicit cover and no English scaffolding residue.
- [x] Rebuild the U357 backend twice with zero byte differences: 3,326 records,
      357 units, 714 expressions, 700 concepts, 734 physical term records and
      exactly 712 current logical terms. Expose `supersedes_id`, preserve 22
      historical terms, and pass schema, referential, 15-CSV, and round-trip QA.
- [x] Publish the coherent U357 checkpoint to GitHub and the existing Zenodo
      concept lineage. GitHub commit
      `f2c8e2202f0af97fdf230069b250c971b455a946`, release
      `lebl-family-id-wip.2026.08.24.u357`, and Zenodo version DOI
      `10.5281/zenodo.22086636` expose the same nine files / 18,904,112 bytes.
      Fresh anonymous downloads of all nine files matched local byte counts and
      SHA-256 hashes; the concept latest-version endpoint resolves U357. Receipts
      are under `publication/wip-2026.08.24-u357/`.
- [x] Translate and independently audit R006 U273 at frozen source lines
      2343--2374 and live target lines 2353--2384: minimum-modulus explanation,
      maximum-modulus theorem, real counterexample, and local `1+az^k`
      heuristic. Preserve all 19 inline expressions, theorem label, exercise
      reference, and exact TeX topology; evidence is
      `qa/R006_MAXIMUM_MODULUS_PRINCIPLE_U273_20260824.md`.
- [x] Rebuild and independently replay the local U358 backend: 3,335 records,
      358 units, 716 expressions, 715 current logical terms, 15 lossless CSV
      views, 26 files / 13,534,440 bytes per tree, and zero A/B differences.
- [x] Translate and independently audit R006 U274--U276: the
      polynomial-growth-at-infinity lemma, the proof of the fundamental theorem
      of algebra, and all seven Section 11.5 exercises. Preserve exact source
      structure and record the punctured-neighborhood and locally-identically-
      zero clarifications as `LEBL-ID-ADV-0240` and `LEBL-ID-ADV-0241`. Map the
      seven unsolved exercises to O001, including the four source hints, without
      inventing answers or solutions.
- [x] Rebuild and independently replay the U361 backend. The authoritative
      `v0.4-live-2026.08.24-u361-e` tree and its `-u361-f` replay each contain
      27 files / 15,051,229 bytes and have zero byte differences. The dataset
      contains 3,520 records, 361 units, 722 expressions, 722 current logical
      terms, 241 correction events, and seven O001 gaps; all schemas,
      references, 15 CSV views, and lossless round trips pass. Canonical
      inventory SHA-256 is
      `a8396edb38b192a955431715b0eb44abae823bfd80370f876089c1c0f4ef96af`.
- [x] Build and visually audit the centered 200-page U361 Volume II reader
      through complete Section 11.5 and all seven exercises. Converter and
      TeX convergence checks pass, all 80 fonts are embedded, pages 1--2 and
      184--200 were rendered, and the fresh tail is readable without clipping
      or off-center content. Promoted reader SHA-256 is
      `3e03748a32b19a7fabc38be7dbc9f1c8bc845eb99f5896dd5d93877176ceab72`.
- [x] Reconfirm the HP-LEBL-R007-001 owner boundary with no range conflict:
      only complete `ch-nonlin-systems.tex` is reserved/admitted. The live
      `ch-first-order-ode.tex` cursor remains raw line 89 and all R006/R008 work
      remains excluded.
- [x] Publish U361 to GitHub and as a new version of existing Zenodo concept
      DOI `10.5281/zenodo.22059779`. GitHub commit
      `5123f592f7721f82af5c6367bc391bbc064bc988`, tag
      `lebl-family-id-wip.2026.08.25.u361`, release ID 376023034, and Zenodo
      record/DOI `10.5281/zenodo.22087498` expose the same nine files /
      20,798,759 bytes. Anonymous downloads of every asset match local byte
      counts and SHA-256; all 50 changed GitHub source files also pass public
      raw-byte readback. Receipts are in
      `publication/wip-2026.08.25-u361/`.
- [x] Translate and independently audit R006 U277 at frozen source raw lines
      2542--2617 / live target raw lines 2552--2627: Section 11.6 opening,
      pointwise/uniform boundedness definitions, and three counterexamples.
      Bind field-backed terms `LEBL-TERM-0723` through `LEBL-TERM-0725` and
      record no source correction.
- [x] Rebuild and independently replay local U362: 3.529 records, 362
      segments, 724 expressions, 725 current logical terms, 15 lossless CSV
      views, and two identical 27-file / 15.092.885-byte trees. Canonical
      inventory SHA-256 is
      `29df1983b6e89b671a716c68a5a796584fe8abc87fdda74349377cfe0182b99a`.
- [x] Translate and independently audit R006 U278 at frozen source raw lines
      2619--2659 / live target raw lines 2629--2669: the countable-domain
      pointwise-convergent subsequence proposition and complete diagonal proof.
      Preserve 32 mathematical payloads and bind `LEBL-TERM-0726`, *diagonal
      argument* → `argumen diagonal`; record no source correction.
- [x] Rebuild and independently replay local U363: 3.534 records, 363
      segments, 726 expressions, 726 current logical terms, 15 lossless CSV
      views, and two identical 27-file / 15.123.003-byte trees. Canonical
      inventory SHA-256 is
      `7ba145406f0e6dd132eaa210edc17c5ba83336e730bdac6d51f7a515d9841041`.
- [x] Translate and independently audit R006 U279 at frozen source raw lines
      2661--2738 / live target raw lines 2671--2748: the uniform-equicontinuity
      definition and complete uniform-limit criterion proof. Bind
      `LEBL-TERM-0727` and `LEBL-TERM-0728`; record no source correction.
- [x] Rebuild and independently replay local U364: 3.541 records, 364
      segments, 728 expressions, 728 current logical terms, 15 lossless CSV
      views, and two identical 27-file / 15.160.351-byte trees.
- [x] Translate and independently audit R006 U280 at frozen source raw lines
      2740--2762 / live target raw lines 2749--2771: the compact-space
      countable-dense-subset proposition and finite-cover proof. Bind
      `LEBL-TERM-0729`; record no source correction.
- [x] Rebuild and independently replay local U365: 3.546 records, 365
      segments, 730 expressions, 729 current logical terms, 15 lossless CSV
      views, and two identical 27-file / 15.190.364-byte trees. Canonical
      inventory SHA-256 is
      `a5b6859d978f6e37ffdd6ab488bf289eb68706934010a96ecb61b6f1b42e82cb`.
- [x] Translate and independently audit R006 U281 at frozen source raw lines
      2764--2872 / live target raw lines 2773--2881: the complete
      Arzelà--Ascoli theorem and proof. Bind `LEBL-TERM-0730`; preserve the
      valid reverse-triangle wording; bind the source FIXME to
      `prop:unifcauchymetric` as sole event `LEBL-ID-ADV-0242`.
- [x] Rebuild and independently replay local U366: 3.552 records, 366
      segments, 732 expressions, 730 current logical terms, 242 corrections,
      15 lossless CSV views, and two identical 27-file /
      15.230.478-byte trees. Canonical inventory SHA-256 is
      `f9c9a7609bd69d135e5393911972023cb32cca287ce50f756fec987b06290358`.
- [x] Translate and independently audit R006 U282 at frozen source raw lines
      2874--2913 / live target raw lines 2883--2923: both immediate
      Arzelà--Ascoli corollaries and the complete mean-value proof. Bind the
      undefined source domain `X` to `[a,b]` as `LEBL-ID-ADV-0243`.
- [x] Rebuild and independently replay local U367: 3.556 records, 367
      segments, 734 expressions, 730 current logical terms, 243 corrections,
      15 lossless CSV views, and two identical 27-file /
      15.264.985-byte trees. Canonical inventory SHA-256 is
      `bf0758e1c6bfa8097ab2d4ee61084cfccfc8014b3eadfb71715696e98b35a4cc`.
- [x] Translate and independently audit R006 U283 at frozen source raw lines
      2915--2945 / live target raw lines 2925--2955: the Peano-existence and
      compact-integral-operator applications. Bind field-attested
      `LEBL-TERM-0731` compact operator to `operator kompak`; no source
      correction is required.
- [x] Rebuild and independently replay local U368: 3.561 records, 368
      segments, 736 expressions, 731 current logical terms, 243 corrections,
      15 lossless CSV views, and two identical 27-file /
      15.295.246-byte trees. Canonical inventory SHA-256 is
      `77e09c45e4eb7afd71bbb7d05dd48cee9288b580be061c934917a5a930fa8502`.
- [x] Translate and independently audit R006 U284 at frozen source raw lines
      2947--3064 / live target raw lines 2957--3076: the exercise heading and
      first ten Section 11.6 exercises through Kronecker density. Bind
      `LEBL-TERM-0732`; declare only `LEBL-ID-ADV-0244` and
      `LEBL-ID-ADV-0245`.
- [x] Translate and independently audit R006 U285 at frozen source raw lines
      3066--3132 / live target raw lines 3078--3144: the complete Peano
      existence exercise and four-stage Euler argument. Bind field-attested
      `LEBL-TERM-0733`; no source correction is required. Bagian 11.6 is now
      complete.
- [x] Rebuild and independently replay local U370: 3.573 records, 370
      segments, 740 expressions, 733 current logical terms, 245 corrections,
      15 lossless CSV views, and two identical 27-file /
      15.377.121-byte trees. Canonical inventory SHA-256 is
      `f317d2add54525af1680678b181a86315340c1e06db8cf72dc9c1793f3e62e75`.
- [x] Build and visually audit the centered 208-page R006 Volume II reader
      through complete Section 11.6 and all eleven exercises. Converter output
      has zero errors; nine TeX passes converge with seven auxiliary products
      byte-identical between passes 8 and 9; all 80 fonts are embedded; all 585
      internal links and 31 outline destinations resolve; pages 1--2 and
      190--208 are centered, readable, and unclipped. Promoted PDF SHA-256 is
      `00fde02788a34292a44f38fed3146df2dbb4db8d942672e59fd54c9e362b51b7`.
- [x] Publish the nonduplicative U370 checkpoint to GitHub and the existing
      Zenodo concept. GitHub commit
      `309e37fbb2a5362e00e01e2a404d4d9fc303ce84`, release ID `376104251`, and
      Zenodo version DOI `10.5281/zenodo.22088826` expose the same nine files /
      22,589,918 bytes. Anonymous downloads of every public asset match local
      byte counts and SHA-256. The source ZIP independently passes integrity,
      rights-admission, backend, and cutoff audits. Receipts are under
      `publication/wip-2026.08.25-u370/`. Figshare was not mutated because its
      account API returned the concrete `InactiveAccount` 403 response; no
      duplicate item was created.
- [x] Translate and independently audit R006 U286 at frozen source raw lines
      3137--3390 / live target raw lines 3149--3405: the Section 11.7 opening,
      Weierstrass approximation theorem, two accessible figures, and complete
      proof. Preserve 251 controls, 34 environment events, 102 inline formulas,
      and eleven displays. Bind `LEBL-TERM-0734` through `LEBL-TERM-0738`; no
      source correction is required.
- [x] Rebuild and independently replay local U371: 3.586 records, 371
      segments, 742 expressions, 738 current logical terms, 245 corrections,
      15 lossless CSV views, and two identical 27-file /
      15.431.757-byte trees. Canonical inventory SHA-256 is
      `e3d3632976f8aa18ef1d840994b3de334fbb0d73a159c4b842674053457af2c6`.
- [x] Translate and independently audit R006 U287 at frozen source raw lines
      3392--3450 / live target raw lines 3407--3467: inherited convolution
      properties, the countable-dense-subset corollary and proof, and the
      cardinality remark. Bind `LEBL-TERM-0739` through `LEBL-TERM-0741`.
      Declare `LEBL-ID-ADV-0246`, narrowing the false arbitrary-linear-ODE
      inheritance claim to the standard homogeneous constant-coefficient case.
- [x] Rebuild and independently replay local U372: 3.596 records, 372
      segments, 744 expressions, 741 current logical terms, 246 corrections,
      15 lossless CSV views, and two identical 27-file /
      15.487.863-byte trees. Canonical inventory SHA-256 is
      `4ac6e182e14336677584c0694b75ec1816b9f416a91c0c17c23dee857f9f4774`.
- [x] Translate and independently audit R006 U288 at frozen source raw lines
      3452--3523 / live target raw lines 3469--3536: the polynomial-versus-
      analytic warning and absolute-value corollary. Bind `LEBL-TERM-0742`
      through `LEBL-TERM-0744`; repair the coefficient lower index as
      `LEBL-ID-ADV-0247`. Rebuild deterministic backend U373: 3.606 records,
      746 expressions, 744 current terms, and inventory SHA-256
      `b81fd539f8e66b039e63e0ac83ef6278b5bd815c5af4041c99bd58594be70f24`.
- [x] Translate and independently audit R006 U289 at frozen source raw lines
      3525--3626 / live target raw lines 3538--3637: the Stone--Weierstrass
      algebra, closure, point-separation, nonvanishing definitions, and three
      examples. Bind `LEBL-TERM-0745` through `LEBL-TERM-0747`; clarify the
      required nonzero constant as `LEBL-ID-ADV-0248`. Rebuild deterministic
      backend U374 with inventory SHA-256
      `21fd9d474a1892321d528551a950d6685b96487e28e37cf95f0510276f44e544`.
- [x] Translate and independently audit R006 U290 at frozen source raw lines
      3628--3670 / live target raw lines 3639--3682: the two-point
      interpolation proposition and proof. Bind `LEBL-TERM-0748`; record the
      source-only article error as `LEBL-ID-ADV-0249`. Rebuild deterministic
      backend U375 with inventory SHA-256
      `b192caf3426a10c28ee9c272a4246a1c610f896d871df72737d50a3ee0b67973`.
- [x] Translate and independently audit R006 U291 at frozen source raw lines
      3672--3710 / live target raw lines 3684--3722: the real
      Stone--Weierstrass theorem and Claim 1. Bind `LEBL-TERM-0749`; no source
      correction is required. Rebuild deterministic backend U376 with 3.627
      records and inventory SHA-256
      `ffe5bff35d0a80df6c99b33ba46d46afcae9d36fb7a3e70d8027a3e45490fb38`.
- [x] Translate and independently audit R006 U292 at frozen source raw lines
      3712--3736 / live target raw lines 3724--3748: Claim 2 on pointwise
      minima and maxima and its finite-family consequence. Bind
      `LEBL-TERM-0750` and `LEBL-TERM-0751`; no source correction is required.
      Rebuild and independently replay local U377: 3.634 records, 754
      expressions, 751 current terms, 249 corrections, 15 lossless CSV views,
      and two identical 27-file / 15.702.853-byte trees. Canonical inventory
      SHA-256 is
      `0ecbf52aee36407202c2dd910b605fd9336d04eecc030447017714155d4a5f51`.
- [x] Translate and independently audit R006 U293 at frozen source raw lines
      3738--3807 / live target raw lines 3750--3820: Claim 3, its complete
      compact-cover/finite-maximum proof, and the accessible construction
      figure. Declare `LEBL-ID-ADV-0250` and repair the invalid diagonal use of
      the distinct-point interpolation proposition with
      `h_x=f(x)q/q(x)`. Rebuild and independently replay local U378: 3.638
      records, 756 expressions, 751 current terms, 250 corrections, 15
      lossless CSV views, and two identical 27-file / 15.742.202-byte trees.
      Canonical inventory SHA-256 is
      `e3bc00e901ee0b77de3fbecf30190290f6b5e34ecd0cfe31f89d475e12a9d3ac`.
- [x] Translate and independently audit R006 U294 at frozen source raw lines
      3809--3861 / live target raw lines 3822--3874: the bridge from Claim 3,
      Claim 4, the compact-cover/finite-minimum proof, and completion of the
      real theorem. Declare `LEBL-ID-ADV-0251` for the missing universal
      quantifier and source-only grammar event `LEBL-ID-ADV-0252`; bind
      `LEBL-TERM-0752` and `LEBL-TERM-0753`. Rebuild and independently replay
      local U379: 3.647 records, 758 expressions, 753 current terms, 252
      corrections, 15 lossless CSV views, and two identical 27-file /
      15.800.879-byte trees. Canonical inventory SHA-256 is
      `623ac6f154be2fa48e9b2d3139f349c46430b2123ce27ea5d69413e0a4370a85`.
- [x] Translate and independently audit R006 U295 at frozen source raw lines
      3863--3884 / live target raw lines 3876--3897: the dense exponential-
      algebra example and definition of an algebra generated by functions.
      Bind `LEBL-TERM-0754`; declare `LEBL-ID-ADV-0253` for the source's
      misleading phrase “linear combinations of arbitrary multiples.” Rebuild
      and independently replay local U380: 3.653 records, 760 expressions,
      754 current terms, 253 corrections, 15 lossless CSV views, and two
      identical 27-file / 15.845.898-byte trees. Canonical inventory SHA-256
      is
      `0f8556ee47d8a35189c2089a8805fa54c26e05c1ea78cc0b2b1d17118ade1751`.
- [x] Translate and independently audit R006 U296 at frozen source raw lines
      3886--3908 / live target raw lines 3898--3918: the cosine-algebra
      example and Fourier-series convergence warning. Bind `LEBL-TERM-0755`;
      no source correction is required. Rebuild and independently replay local
      U381: 3.658 records, 762 expressions, 755 current terms, 253 corrections,
      15 lossless CSV views, and two identical 27-file / 15.876.749-byte
      trees. Canonical inventory SHA-256 is
      `ba9db62f1d22709b05a1476774d08f5d98770fcfc06ad1e038b8677b162e83a5`.
- [x] Translate and independently audit R006 U297 at frozen source raw lines
      3910--3966 / live target raw lines 3920--3977: the self-adjoint
      definition and complete complex Stone--Weierstrass theorem/proof. Bind
      `LEBL-TERM-0756` and `LEBL-TERM-0757`; declare `LEBL-ID-ADV-0254` and
      repair the source's missing every-`epsilon>0` quantifier. Rebuild and
      independently replay local U382: 3.666 records, 764 expressions, 757
      current terms, 254 corrections, 15 lossless CSV views, and two identical
      27-file / 15.927.185-byte trees. Canonical inventory SHA-256 is
      `c105fac61fc654072ac83731ed4fe7af78e0a83ac3102eb0c6a20f7f951de4e4`.
- [x] Translate and independently audit R006 U298 at frozen source raw lines
      3968--3988 / live target raw lines 3979--3997: the separated-variable
      approximation application. No new term or source correction is needed.
      Rebuild and independently replay local U383: 3.669 records, 766
      expressions, 757 current terms, 254 corrections, 15 lossless CSV views,
      and two identical 27-file / 15.952.435-byte trees. Canonical inventory
      SHA-256 is
      `35420a06fe9f9e2251adf5eccef0919b7fd42d1a5080c4d3731fac2afce5cade`.
- [x] Translate and independently audit R006 U299 at frozen source raw lines
      3990--4036 / live target raw lines 3999--4043: the Exercises heading and
      first five Stone--Weierstrass exercises. Preserve four source hints and
      one no-hint boundary; bind O001 gaps `-0008` through `-0012` and
      `LEBL-TERM-0758`; declare `LEBL-ID-ADV-0255` and repair the complex
      coefficient/evaluation space from `L(\R^{d+1})` to `L(\C^{d+1})`.
- [x] Rebuild and independently replay local U384: 3.688 records, 768
      expressions, 758 current terms, 255 corrections, 12 O001 exercises
      (eight hint-only, four without hints, zero solutions), 15 lossless CSV
      views, and two identical 27-file / 16.117.012-byte trees. Canonical
      inventory SHA-256 is
      `c503b7617b01254d84651a7f2b7653cefe645b6329620bf3aede71e9013c5fed`.
      The builder now binds valid inline physical-line hint markers.
- [x] Independently three-way QA and owner-accept `HP-LEBL-R007-001` against
      the frozen v6.11 source, helper handoff, and live Indonesian chapter by
      all 20 stable units. Verify 66/66 packet hashes, mathematics, language,
      structure, references, figures, full 472-page build, backend bindings,
      and four visual reader surfaces. Preserve the corrected live owner target
      SHA-256
      `adee2f44b4a570b8f89f01c529d9bb9ebc38c0999ceb949360f4c075390003a1`;
      do not recopy the helper target. Evidence is
      `qa/R007_NONLINEAR_SYSTEMS_HP001_OWNER_THREE_WAY_QA_20260825.md`.
- [x] Translate and independently audit R006 U300 at frozen source raw lines
      4038--4054 / live target raw lines 4045--4060: even real polynomials,
      algebra closure, and failure to separate points on `[-1,1]`. Add O001
      gap `LEBL-O001-R006-0013`; no source correction is needed.
- [x] Rebind seven inherited R007 introduction manifest selectors to their
      current live line ranges without changing their reproducing content
      hashes. Preserve the separately recorded Indonesian prose-refinement
      backlog for a later bounded pass; the selector repair is not evidence of
      fresh language acceptance.
- [x] Rebuild and independently replay local U385: 3.765 records, 33 assets,
      644 relations, 13 O001 exercises (eight hint-only, five without hints,
      zero solutions), 15 lossless CSV views, and two identical 27-file /
      16.318.786-byte trees. Canonical inventory SHA-256 is
      `83a6d8baa6f0e601f13744a23eabc8bbde5695a707eda9e4846cf4b0b34c9cf5`.
- [x] Translate and independently audit R006 U301 at frozen source raw lines
      4056--4081 / live target raw lines 4062--4088: Laurent and harmonic
      polynomials on the unit circle. Preserve the two-part topology, two
      displays, index hook, source hint, and no-solution state; bind
      `LEBL-TERM-0759` and O001 gap `LEBL-O001-R006-0014`. No source correction
      is needed.
- [x] Rebuild and independently replay local U386: 3.773 records, 33 assets,
      645 relations, 14 O001 exercises (nine hint-only, five without hints,
      zero solutions), 15 lossless CSV views, and two identical 27-file /
      16.375.706-byte trees. Canonical inventory SHA-256 is
      `b2cfa766aa643da8e07e54fb1a98d2424aee60a88fb079d1fb741aa1d2453aeb`.
      Independent schema, reference, projection, input, and U301-binding
      evidence is `qa/BACKEND_V0_4_LIVE_U386_INDEPENDENT_AUDIT_20260826.md`.
- [x] Translate and independently audit R006 U302 at frozen source raw lines
      4083--4091 / live target raw lines 4090--4098: uniform approximation by
      finite complex exponential sums. Preserve the endpoint condition, label,
      display, complex coefficients, and no-hint/no-solution state; bind O001
      gap `LEBL-O001-R006-0015`. No term or source correction is needed.
- [x] Translate and independently audit R006 U303 at frozen source raw lines
      4093--4120 / live target raw lines 4100--4127: the oriented unit-circle
      integral obstruction and non-self-adjoint algebra. Preserve its four
      subproblems, footnote, chapter reference, label, display, and
      no-hint/no-solution state; bind O001 gap `LEBL-O001-R006-0016`. Correct
      one target-language calque and pass the bounded recheck; no source
      correction is needed.
- [x] Rebuild local U388: 3.781 records, 33 assets, 645 relations, 16 O001
      exercises (nine hint-only, seven without hints, zero solutions), 15
      lossless CSV views, and two identical 27-file / 16.457.998-byte trees.
      Canonical inventory SHA-256 is
      `544276dc6ad9b966b238d9a58c31a038031fd1de271fe67149ef40219b8257c5`.
- [x] Translate and independently audit R006 U304 at frozen source raw lines
      4122--4131 / live target raw lines 4129--4138: the one-point-vanishing
      algebra exercise. Preserve all quantifiers, separation/nonvanishing
      hypotheses, uniform-limit conclusion, and no-hint/no-solution state;
      bind O001 gap `LEBL-O001-R006-0017`.
- [x] Translate and independently audit R006 U305 at source raw lines
      4133--4139 / target raw lines 4140--4146: density from closure under all
      distance functions. Bind O001 gap `LEBL-O001-R006-0018`; no correction
      or new term is needed.
- [x] Translate and independently audit R006 U306 at source raw lines
      4141--4161 / target raw lines 4148--4168: polynomial approximation in
      the `C^k` norm. Admit `LEBL-TERM-0760` (`norma C^k`) and O001 gap
      `LEBL-O001-R006-0019`; preserve the derivative sum and limit exactly.
- [x] Translate and independently audit R006 U307 at source raw lines
      4163--4176 / target raw lines 4170--4183: parity-preserving even/odd
      polynomial approximation. Bind O001 gap `LEBL-O001-R006-0020`; no
      correction is needed.
- [x] Translate and independently audit R006 U308 at source raw lines
      4178--4197 / target raw lines 4185--4205: finite-point polynomial
      interpolation. Declare `LEBL-ID-ADV-0256` and add the minimal
      pairwise-distinctness assumption required by the source hint after
      repeated points are discarded. Bind O001 gap `LEBL-O001-R006-0021`.
- [x] Rebuild final backend U393 as independent candidates E/F after repairing
      both the generic edition-lineage validator and ADV-0256 metadata.
      E/F contain 3,806 records and 27 files / 16,690,330 bytes each, are
      byte-identical, validate generically, and round-trip all 15 CSV views.
      Canonical inventory SHA-256 is
      `eb022c1d1388f5ef8c84574438f44d8c7ed9a3e05d070d0b2ea20395e9eb781e`.
      Independent evidence is
      `qa/BACKEND_V0_4_LIVE_U393_INDEPENDENT_AUDIT_20260826.md`.
- [x] Build and visually audit the centered 224-page R006 Jilid II reader
      through complete Section 11.7 and all fourteen exercises. Converter,
      nine-pass TeX stability, references, fonts, links, text extraction,
      pages 1--2 and 193--224, figures, exercises, index, and notation all
      pass. PDF SHA-256 is
      `5a8db6dd8f9b559c578fe31678943e093650019686e2e75cc752d1b2b49bb211`;
      receipt is
      `qa/R006_STONE_WEIERSTRASS_SECTION_COMPLETE_READER_U393_20260826.md`.
- [x] Publish U393 through the existing GitHub and Zenodo lineages with exact
      files, manifest, hashes, provenance, partial-status labeling, and
      anonymous public-byte readback. GitHub release ID `376831420`, commit
      `12b304221fcdf65a5d62a2807bcfc78601a7b6eb`, and Zenodo record `22104149`
      expose the same nine files / 12.383.839 bytes. The independent font
      recount correction is included. Continue R006 Section 11.8 at frozen
      source raw line 4201 / live target raw line 4209.
- [x] Revalidate the one-time Indonesian field-usage terminology audit against
      an actual field-specific source. The bounded arXiv search again found no
      suitable Indonesian TeX source; direct extraction and visual inspection
      of Zetriuslita's 162-page *Mudah Memahami Analisis Kompleks* confirmed
      the live R006 choices and the next-unit forms. No propagation was
      justified; evidence is bound in
      `qa/terminology_qa/ARXIV_OR_FALLBACK_TERMINOLOGY_AUDIT_20260824.md`.
- [x] Admit and independently audit R007 U001 (`ch-intro.tex` raw lines 1--45)
      and R008 U001 (`ca.tex` raw lines 556--667); retain separate resource,
      edition, rights, source, and target identities and record both next
      cursors in `CURRENT_CURSOR.json`.
- [ ] Publish future clean WIP versions and the final complete three-book release
      automatically when each bounded release gate is ready; never ask for
      redundant confirmation.
- [ ] After all three books, deduplicate and disposition at most one upstream
      issue.

## U423 recovery checkpoint (2026-08-29)

- [x] R006 contiguous unit admitted: `ra.v2.fourier-series.exercises.decaying-sine-series-forced-ode`, source raw lines 5358–5385 (774 bytes, SHA-256
      `9d34b8d673c7983231eca78947006519e71b5bdfb65a1f37672dcc5c0e602ded`),
      target raw lines 5372–5399 (873 bytes, SHA-256
      `fe3e35c58f96b3e14c29e23a820479792e524545e581e01aac11989820af2934`).
      Full target is 198066 bytes, SHA-256
      `434495045cbfd83b0d0b0ff265339d94710b7a8eea592f9f010b743108a5bab4`.
      Receipt: `qa/R006_DECAYING_SINE_FORCED_ODE_EXERCISE_U423_20260829.md`
      (5723 bytes, SHA-256
      `92765f81daa1fcbcaf09f4f93bc72024f6428951e88e98a2c7766c6f54f75da8`).
- [x] U423 backend A/B replay passed: 27 files and 17931910 bytes per tree,
      canonical ordinal-POSIX inventory 3292 bytes, SHA-256
      `1436fbd7a7b6c351d8d333713d6505310e0378330dfe7a95bf99c625c8f3c91e`,
      3993 records / 846 expressions / 797 logical terms / 423 manifest
      bindings / 360 direct checks / 15 lossless CSV round trips. Receipt:
      `qa/BACKEND_V0_4_LIVE_U423_20260829.md` (3871 bytes, SHA-256
      `099fb1ca2ca4e58c45f34301ce2a3c90da949670ca38075da8e1b07ec53790e8`).
- [x] Isolated complete-volume reader build passed at
      `tmp/r006-u423-build-20260829` with `SOURCE_DATE_EPOCH=1787961600` and
      `TZ=UTC`: converter and pdflatex/index/glossary passes 1–10 exit 0,
      241 pages / 2427666 bytes, PDF SHA-256
      `fd0830a19e94eaed0b53106adac197bec3665daf3e7a0b408a4018ac155ea504`;
      auxiliary products stable across passes 9–10 and pages 230–233 visually
      pass. This is a non-release build; public reader U397 is retained.
- [x] Publish one non-forced 42-path U423 source/backend checkpoint from public
      U422 controls commit `219d65a5d81a07c86509421df147c8875939bb2f` using
      `publication/live-2026.08.29-u423/publish_github_main_u423.py`. Public
      source commit `65b5a7950d1e6d89918603548b1663122f57cdf5`, tree
      `af701a99504cdfb04823d7343f84fb30aeb893d7`, has sole parent U422 controls.
      The exact 42-path payload totals 19810210 bytes; its 6601-byte canonical
      inventory has SHA-256
      `66c7960381bd0a16b8a78a83a877f662d695558889a24a7a611302971277cb52`.
      Authenticated immutable blobs, anonymous immutable raw bytes, branch,
      parent, tree, and untruncated 1662-entry recursive tree all pass; an
      independent audit repeated all 42 comparisons and also reverified the
      unchanged nine-file U397 GitHub release and Zenodo record 22105195.
- [x] Publish the one bounded six-path U423 receipt/recovery-controls overlay
      from source commit `65b5a7950d1e6d89918603548b1663122f57cdf5` using
      `publication/live-2026.08.29-u423/publish_github_u423_controls.py`. The
      frozen receipt snapshot is
      `publication/live-2026.08.29-u423/GITHUB_MAIN_U423_RECEIPT.md`, 3929
      bytes, SHA-256
      `6f790530f396e97128c2f2de9fd85f45557db76cb4727e153feeec372725e1db`;
      `LEBL-ID-DEC-0197` was the decision-log tail. The overlay is public at
      commit `d3cd90ffd11d1b9c193768b041b4ee947d318d0b`, tree
      `4f1815a4c11e0cc2827679c09872f085fac3fc87`, with the U423 source commit
      as sole parent. All six paths / 530792 bytes pass authenticated,
      anonymous, and independent readback; the 827-byte canonical inventory
      has SHA-256
      `78bd2c8cbaa9411a0aca85bc937563947a7c8562b1e92072def595c4c457beb6`,
      and the recursive tree has 1664 entries with `truncated=false`. The
      finalized local receipt is 5292 bytes, SHA-256
      `da71a50f4ff6a200dab24fc201b687164c99fc884b0a82a795a823430241a324`;
      carry it with the next substantive checkpoint and do not create a third
      pointer-only commit.
- [x] Set `CURRENT_CURSOR.json` next action to source raw lines 5387–5394 /
      target raw lines 5401–5408 (Parseval inverse-square-sum exercise).

Recovery rule: read this section, `CURRENT_CURSOR.json`, `CURRENT_STATE.json`,
`PUBLICATION_STATE.json`, the two U423 QA receipts, and both U423 publisher
wrappers. The U423 source and controls transactions are complete, public, and
independently verified. Resume the Parseval inverse-square-sum exercise at the
recorded source/target lines. No author contact or upstream issue is allowed
before all three assigned books are complete.

## U424 recovery checkpoint (2026-08-29)

- [x] R006 contiguous unit admitted:
      `ra.v2.fourier-series.exercises.parseval-inverse-square-sum`, source raw
      lines 5387–5394 (229 bytes, SHA-256
      `432d8ce695cfacd212eb6af3f8d81dd32a2eef7b51b1fb476f1659dd1012f314`),
      target raw lines 5401–5408 (256 bytes, SHA-256
      `2b9a298bc2c7f9c28df47872b7f7b106fb3450545af8dca5e7477b1a4eebe0c7`).
      Full target is 198093 bytes, SHA-256
      `955e4fd2b360096266939f1b6ada5a493eb6c30af6ffba894086d8d4c518c55b`.
      Independent language/mathematical/topology/O001 review passed. Receipt:
      `qa/R006_PARSEVAL_INVERSE_SQUARE_SUM_EXERCISE_U424_20260829.md` (6694
      bytes, SHA-256
      `4b6af69aea832633800cef236c7512b5aab196fbb95e3bd884e90d6548a62834`).
- [x] U424 backend A/B replay passed: 27 files / 17971333 bytes per tree,
      canonical ordinal-POSIX inventory 3292 bytes, SHA-256
      `fa1c2d90fdafed7e5042e027d95d7d1cb104e7ecf3c9d74b744ca559516de63a`,
      3997 records / 848 expressions / 797 logical terms / 424 manifest
      bindings / 362 direct checks / 15 lossless CSV round trips. Receipt:
      `qa/BACKEND_V0_4_LIVE_U424_20260829.md` (4263 bytes, SHA-256
      `580dfe415274a5cef9518377a97a01f7173f912fe9fe20f3a660029f16ecc77b`).
- [x] Isolated fixed-epoch reader build at `tmp/r006-u424-build-20260829`
      passed converter, index/glossary, `pdflatex` 1–9 plus independent pass
      10, byte stability, links, outlines, fonts, text extraction, and visual
      pages 230–233. PDF: 241 pages / 2427693 bytes, SHA-256
      `e6bb4b925793e0fc27cd3b69b01c126712ebf40d5e4e1bed64dbdd392e90fe8e`.
      Page 232 contains complete Indonesian U424 and begins the untouched next
      English exercise at the exact boundary. This is not a reader release.
- [x] Publish one non-forced 42-path U424 source/backend checkpoint from public
      U423 controls commit `d3cd90ffd11d1b9c193768b041b4ee947d318d0b`, carrying the finalized local
      U423 receipt. Public source commit
      `51426054b71910557f3d2a9d166248d65a987258`, tree
      `33c12752c1acb39622367e79304e8b9dbb46e4ab`, has exactly 42 paths /
      19866836 bytes and a canonical 6604-byte inventory SHA-256
      `2c541ead34653c2ce19e47aaba710d9932e4962ee494218ba3fe488e05b3df2f`.
      Authenticated, anonymous, and independent readback all pass; U397 GitHub
      and Zenodo inventories remain byte-identical.
- [x] Publish one bounded six-path U424 receipt/recovery-controls overlay from
      the verified U424 source commit. Public controls commit
      `c7951cc776924ebad27d544e4208d749a941b5de`, tree
      `63ef7c3281509c4317b09f4a256ce5a136c2ea7b`, has the U424 source commit as
      its sole parent. All six paths / 543054 bytes pass authenticated,
      anonymous, and independent readback; the canonical 827-byte inventory
      has SHA-256
      `cb24fcae9999f05ab3761ef0af9d63db9a885f7797f1ee5c991074d03340133b`.
      The public receipt snapshot is 3996 bytes, SHA-256
      `b28552854338498bc4eaeb732d4768935870a66d37127924f815048e85b3d759`;
      the finalized local receipt is 5542 bytes, SHA-256
      `722dde31b78e8134cc04006bbbf447ce1768c8cbf990f91ff651337adc639b76`.
      It must be carried with U425. The U397 release and Zenodo record did not
      change, and no third pointer-only commit was created.
- [x] Set the next translation boundary to source raw lines 5396–5405 / target
      raw lines 5410–5419, the one-sided absolutely summable series / analytic
      closed-unit-disc extension exercise. Preserve its explicit hint at
      source raw line 5404 and map the missing solution to O001.

Recovery rule: this U424 transaction is complete. Public preservation is U424
source commit `51426054b71910557f3d2a9d166248d65a987258` plus controls commit
`c7951cc776924ebad27d544e4208d749a941b5de`; use the U425 section below for
the current executable action. No author contact or upstream issue is allowed
before all three assigned books are complete.

## U425 recovery checkpoint (2026-08-29)

- [x] Admit
      `ra.v2.fourier-series.exercises.one-sided-series-analytic-unit-disc-extension`
      from `source/ra-v6.3/ch-approximate.tex` raw lines 5396–5405 (490 bytes,
      SHA-256
      `22c9a47d6e095ebf12acd7a5d6562712eee872d5a569093bcc676419202adeea`)
      into `translation/ra/ch-approximate.tex` raw lines 5410–5419 (520 bytes,
      SHA-256
      `7e6d0f5b214f350d6a143b38b518198944fa56cac9e7089c8d38a4e1459d3dc5`).
      The explicit `Petunjuk` is preserved; no source solution exists. The
      full target is 198123 bytes, SHA-256
      `1c51b2b3490f84c2016ff0e2ac4e347f268fb4568f187773147b3c9703151157`.
      Receipt:
      `qa/R006_ONE_SIDED_SERIES_ANALYTIC_UNIT_DISC_EXERCISE_U425_20260829.md`
      (7968 bytes, SHA-256
      `9666de83f2c9733ba6d017c907296fc2854a5547ea0448e1c3a2e47084810f34`).
- [x] U425 backend A/B replay passed: 27 files / 18027168 bytes per tree,
      canonical ordinal-POSIX inventory 3292 bytes, SHA-256
      `729587820f9ea940bb7f25377705ceb3ed37015e15c3b86d557d541823e3b9e2`,
      4003 records / 850 expressions / 425 manifest bindings / 364 direct
      checks / 15 lossless CSV round trips. Receipt:
      `qa/BACKEND_V0_4_LIVE_U425_20260829.md` (3670 bytes, SHA-256
      `592b8e75350029cd73123010c8986d3f6a70e6df2a153683aacf5b8d266f5877`).
- [x] Fixed-epoch integration build at `tmp/r006-u425-build-20260829`
      passed: 241 pages / 2427763 bytes, PDF SHA-256
      `2166d72eaedfb0bece00d2df99902694c39a0151eb2e8243f568e68587623ba7`.
      Passes 10–11 are byte-identical across the PDF and seven auxiliaries;
      pages 230–233 pass visual inspection. Page 232 contains complete
      Indonesian U425 including its hint and begins the untouched English
      U426 exercise at the exact boundary. This is not a reader release.
- [x] Publish one bounded non-forced U425 source/backend checkpoint from
      verified U424 controls commit
      `c7951cc776924ebad27d544e4208d749a941b5de`. Public source commit
      `7ffd500b2bd48c7bac13664f86e0eb04498cae97`, tree
      `640cd66666877c9ba88390e592734b207ea07c18`, has exactly 42 paths /
      19941579 bytes and canonical 6612-byte inventory SHA-256
      `eb335d7b0c964c0836b3d3f0b16aaa7f4fd96a1eb20498641eebbb62b7310f5a`.
      Authenticated, anonymous, and independent readback all pass; U397
      GitHub and Zenodo inventories remain byte-identical.
- [x] Publish one bounded six-path U425 receipt/recovery-controls overlay
      from the verified U425 source commit. Public controls commit
      `23835b0329a6397d74889aaf62fc993d02945e0e`, tree
      `f8fef281c8dee4463d31db8cb963691268c6ebad`, has U425 source as its sole
      parent. All six paths / 556942 bytes pass authenticated and anonymous
      readback; the canonical 827-byte inventory has SHA-256
      `8b70696e15f79c1e552b28dd614e218adf50bc1bda716de3e0e8595d3e5a54d0`.
      The public receipt snapshot is 4150 bytes, SHA-256
      `0d4ccaaa78ad350a6b2c0284e99fe015ae1979bdf60a8a3949dce73c24274204`;
      the finalized local receipt is 5447 bytes, SHA-256
      `5ae84b10cb2e10d33389ead81951c1a8d64448f08b19f637c023cfde1532b792`.
      An independent closure audit is required before the next publication
      and no third pointer-only commit is created. Keep the U397 reader
      release and Zenodo record 22105195 unchanged.
- [ ] Continue R006 at source raw lines 5407–5413 / target raw lines
      5421–5427:
      `ra.v2.fourier-series.exercises.exponentially-decaying-sine-series-smoothness`.
      Do not alter the R007/R008 cursors or recopy HP-LEBL-R007-001.

Recovery rule: read this U425 section, `CURRENT_CURSOR.json`,
`CURRENT_STATE.json`, `PUBLICATION_STATE.json`, the two U425 QA receipts, and
`publication/live-2026.08.29-u425/GITHUB_MAIN_U425_RECEIPT.md` plus its two
publisher wrappers. Current public preservation is verified U425 source commit
`7ffd500b2bd48c7bac13664f86e0eb04498cae97` followed by controls commit
`23835b0329a6397d74889aaf62fc993d02945e0e`; the finalized receipt is carried
with U426. The next executable action is the R006 source raw 5407–5413
exercise. The public reader remains U397. No author contact or upstream issue
is allowed before all three assigned books are complete.
