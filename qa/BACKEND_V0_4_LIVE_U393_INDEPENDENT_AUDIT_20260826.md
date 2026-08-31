# Backend v0.4 live U393 — independent E/F audit

Status: **PASS; final candidates E/F independently certified**  
Date: 2026-08-26  
Auditor write scope: none

## Determinism and generic validation

- Final trees: `backend/production/v0.4-live-2026.08.26-u393-final-e` and `-f`.
- Both contain 27 files / 16,690,330 bytes and are byte-identical at every relative path.
- Canonical inventory (sorted `{path,bytes,sha256}` array, compact JSON, UTF-8 plus LF): 3,290 bytes, SHA-256 `eb022c1d1388f5ef8c84574438f44d8c7ed9a3e05d070d0b2ea20395e9eb781e`.
- Standalone generic validation exits zero for both: three schemas, 3,806 records, 786 expressions.
- All 15 CSV views round-trip losslessly to 3,806 records in both trees.

## Negative mutation gate

The independent replay rejects cross-resource derivative edges, unrelated same-resource source bindings, self-cycles, and the formerly fail-open target↔source two-cycle. The two-cycle now fails with `cycle in edition derivative chain`; the unmodified baseline passes. This proves that localized derivative assets may bind only through an acyclic same-resource edition ancestry.

## U308 correction binding

Current correction `urn:uuid:d4d74fe0-3fcc-5103-8669-3c974021d9d1` for `LEBL-ID-ADV-0256` now:

- exactly affects and matches U308 unit `urn:uuid:b93e938d-9e01-504c-b130-a4945e453175`;
- uses `scope=unit`, `method=exact_path_line`;
- carries the completed independent-PASS QA status and receipt SHA-256 `ffc05ef5aaf51fda17c16b0217348b265d0602483d4a786d7555852ab7b19dc4`;
- binds source lines 4187–4195 at SHA-256 `82255b6f81b8687b90ddf562bc884137b741141e2cfd4552355a8004f46de056`;
- carries compact ledger evidence SHA-256 `93030c2c5edf2ec385063ff93c294b6d96dbff4643af0426d80d5b8a46bf5a28`;
- has a recomputed, valid proposed-delta hash.

## Frozen inputs and R007 closure

- Manifest: 596,621 bytes, SHA-256 `500d6c59b57825cbfb53a8767a889c2aef6a25f375fe0a6aa3bdb6cb051a17cb`; 393 units = R006 308 / R007 35 / R008 50.
- Terminology: 115,790 bytes, SHA-256 `f9e5f6fa14972e139fed5c0d4afbd6a1d2ee20c3f16d0131e1617d26621e31c1`; 760 current terms.
- Adverse ledger: 234,608 bytes, SHA-256 `1492febaacbbbb9b4d2fed128d73748641cfc0411196b6659332460e8a3f6e35`; 256 events.
- O001: 14,892 bytes, SHA-256 `3ca713f97246a5008a82e05df49441667e7a379979a89634913b4f41d27637a8`; 21 exercises = 10 hint-only / 11 without hints / zero solutions.
- R007 nonlinear-system closure passes independently: 26 figure calls / 25 bases; 28 exact source figures; 31 assets including one localized overlay and two bibliography spans; 42 relations = 31 illustrates / 10 depends-on / 1 adapts; ten citations; all hashes and dependencies resolve.

Earlier U393 candidates A–D are superseded. Only E/F are accepted.
