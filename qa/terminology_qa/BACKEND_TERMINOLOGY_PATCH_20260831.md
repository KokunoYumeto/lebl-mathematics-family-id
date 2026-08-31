# Backend QA — native-Indonesian terminology patch

Date: 31 August 2026  
Status: **PASS**

The complete 5,884-row translation manifest was regenerated after the bounded
R007/R008 terminology corrections. Stable unit identifiers, resource/edition/
rights identities, exercise/hint/solution states, and the 32 complete-file
coverage bindings were preserved.

## Manifest

- rows: 5,884;
- logical rows: 5,420 (R006 2,264; R007 1,681; R008 1,475);
- coverage rows: 32;
- exercises: 2,169; hints: 290; source solutions: 251;
- bytes: 7,233,001;
- SHA-256: `1fe580c9c25c8ba9a8e9532c609e05f1b4102a6b1e77531ffdf6b0947a642c84`;
- unit IDs: 5,884 unique / 5,884 rows.

The generated QA pointer now resolves to
`qa/terminology_qa/NATIVE_INDONESIAN_TERMINOLOGY_AUDIT_20260831.md`; the prior
hard-coded nonexistent 30-August backend report name was removed from the
manifest finalizer.

## Independent backend replays

The deterministic builder was run into two fresh directories:

- `backend/production/v0.4-complete-2026.08.31-tqa-release-a`;
- `backend/production/v0.4-complete-2026.08.31-tqa-release-b`.

Each replay contains 27 files / 122,779,068 bytes and 20,401 canonical records.
The complete relative-path/byte/SHA-256 inventories are identical. Canonical
JSON inventory SHA-256:
`4005b1bf3ee6c7b4b4e70f658eea141d188479727c31617df7b8038cdc8dcabc`.
`records.jsonl` SHA-256:
`60ea5afad065a29d5d2ffca8bc0ac0fec3998bb1c0e9fff9ac6302769171e7b9`.

Both replays pass:

- Draft 2020-12 schema validation;
- referential integrity;
- all 5,884 manifest bindings;
- 11,282 direct component checks;
- 20,401 validated records;
- 15 CSV projections and lossless round trip (20,401 recovered records);
- 804 current logical terminology rows / 827 physical term records;
- 34 O001 solution gaps with 14 source hints and no invented solution.

Runtime provenance: OpenAI Codex gpt-5.6-sol, Ultra acting on the user's request.
