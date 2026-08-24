# Backend v0.4 live U330 Figure 11.6 correction checkpoint

Status: **PASS**  
Validation date: 2026-08-24  
Lane: `R006+R007+R008`  
Dataset ID: `urn:uuid:d4942c0c-1b83-541d-ac61-d7c7964e1473`  
Authority status: `authoritative`

## Bound inputs and correction

The bounded builder `backend/production/build_live_v04.py` was run in two separate Python processes against the corrected live controls. The manifest remains at `330` units: `R006 265`, `R007 15`, and `R008 50`.

- `translation/TRANSLATION_MANIFEST.jsonl`: `472,659` bytes; SHA-256 `c45f42524e598f724e5845c1a7e3c38b9c43de241dcae63b48870b2683d1b34b`; `330` JSONL records.
- `00_control/TERMINOLOGY.csv`: `88,790` bytes; SHA-256 `9192208da259eb7f0b7ab8dd9ceb7569ed0af8f1d90c27a349fd0e84c36ac463`; `643` terminology rows plus the header, ending with `LEBL-TERM-0643`.
- `00_control/ADVERSE_LEDGER.jsonl`: `199,445` bytes; SHA-256 `e9d68bddc4c5b54c25a81132e0e8968569d4bcb882cabf149a94414d0a3b048a`; `226` records, ending with `LEBL-ID-ADV-0226`.

The existing U256 unit now binds the Figure 11.6 source overlay, editable Xfig file, and PDF background and their localized target counterparts. The localized target overlay SHA-256 is `7ee6864434d06a45723b8e9e496a26882f6e0cbb6916e6356f2d2bad61eb7f37`; the localized editable Xfig source SHA-256 is `3fe8c73357a4aef584b0f0e4d735885abc7c6f669a290712b8eee8c8ee815937`; and the unchanged text-free PDF background SHA-256 is `a356422abacb1290218f5b47f9d989b0abad314b4065d9bbfb6c43c3adaf2fd3`. The correction is bound to `qa/R006_RADIUS_CONVERGENCE_FIGURE_LOCALIZATION_U256_20260824.md`, SHA-256 `e314ee8b845e1d4ab52de276d0ce883e606babc4aadccb3bb599f90b9f943dae`.

Both output snapshots contain byte-identical copies of the three live control inputs.

## Output paths and identities

- Authoritative A: `backend/production/v0.4-live-2026.08.24-u330-figfix-a`
- Independent replay B: `backend/production/v0.4-live-2026.08.24-u330-figfix-b`

Each complete tree contains `26` files and `11,495,077` bytes. A and B have identical relative paths, byte counts, and SHA-256 hashes, with `0` missing, extra, or changed files.

Canonical inventory format: one UTF-8 line per file, sorted by forward-slash relative path, as `<sha256>\t<bytes>\t<relative-path>\n`.

- A inventory SHA-256: `8c60d50e03a80441dcc5e73ba398ab37f1b258048cb34368d44d474296ac68df`
- B inventory SHA-256: `8c60d50e03a80441dcc5e73ba398ab37f1b258048cb34368d44d474296ac68df`

Key files in both trees:

- `records.jsonl`: `3,679,429` bytes; SHA-256 `a072ad3b76864de53bd1a5802dd9aaee5f9067f2e63b192eafdc308bc9fff9bf`; `2,683` records.
- `dataset.json`: `1,793` bytes; SHA-256 `29afbbec56012bd158114010cc894e6a6c56555619418aa2e4361fbee7bbbe2c`.
- `projection_manifest.json`: `28,966` bytes; SHA-256 `34f7cb8d24b13e264029538033450eb1c31f2f166ceacc04980f39b5d7d9bac5`.
- `VALIDATION.json`: `7,573` bytes; SHA-256 `4f17e167ae9f801a4f216a99f85140362c3bd79382cbe50ae75708e2b6e26343`.

## Validation and lossless projections

Before installing either tree, the builder performed record-schema validation, dataset-schema validation, UUID-reference resolution, deterministic CSV projection, and a projection round trip. Both retained `VALIDATION.json` files report `schema_validation: pass`, `referential_integrity: pass`, `330` live units, `163` units added beyond retained v0.3, and `2,683` records.

After materialization, `backend/tools/backend_tool.py validate` was independently run against A and B. Both returned the same valid authoritative dataset with `3` schema documents, `660` expressions, and these entity counts: artifacts `15`, assets `2`, concepts `432`, corrections `94`, editions `7`, QA events `432`, relations `594`, resources `3`, rights `4`, segments `330`, terms `440`, and units `330`.

`backend/tools/backend_tool.py roundtrip` was then independently run against each checked-in CSV directory. Both runs checked all `15` projection files and recovered all `2,683` records with `roundtrip: pass`. Each CSV set contains `15` files and `6,967,130` bytes. Its canonical inventory SHA-256 is `191c74e5d79f8a1a6e1d6cf40b514f1c697fb05f2d9afdba992dda1cab76b974`; A and B are byte-identical.

## Supersession and provenance

The prior `backend/production/v0.4-live-2026.08.24-u330-a` and `backend/production/v0.4-live-2026.08.24-u330-b` trees remain present and unmodified as superseded local witnesses. The Figure 11.6 correction snapshots above are the authoritative U330 backend boundary.

The exact translation/runtime provenance recorded in both corrected datasets is `OpenAI Codex gpt-5.6-sol, Ultra`. The corrected U330 backend is schema-valid, referentially intact, losslessly projected through every required CSV view, and reproducible across two independent materializations. Build A is the authoritative checkpoint; build B is the byte-identity replay witness.
