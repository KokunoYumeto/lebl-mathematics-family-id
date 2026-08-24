# R007 owner-admission receipt — nonlinear systems chapter (HP-LEBL-R007-001 / U357)

Date: 2026-08-24  
Resource: R007, *Notes on Diffy Qs*, upstream v6.11  
Assigned object: complete `ch-nonlin-systems.tex` chapter  
Result: **PASS — owner-verified and admissible as 20 structurally verified units**

## Authority and handoff identity

- Registry: `outputs/01a01ec1-e685-70d0-b022-211396334723/curriculum_logbook/63_HELPER_PACKET_REGISTRY_V1_20260824.json`; 47,732 bytes; SHA-256 `95b3c046bc504e42b535c766cd43fb8855a57b4defe7af2dfa355c6eddb0fdd8`.
- Packet: `outputs/01a01ec1-e685-70d0-b022-211396334723/curriculum_logbook/helper_packets/HP-LEBL-R007-001`.
- Handoff: 24,607 bytes; SHA-256 `5f51bda4f2a64c6e0777dbcb51435a0f403bec7ff585878106f471103523cba4`.
- Packet checksums: 6,852 bytes; SHA-256 `7bc509b0a277d5323a72b910e45a06d8620bf628cd16f5cb9ce3c399b937ab47`.
- Owner replay: all 66 listed packet files exist and match their SHA-256; no missing, unlisted, or mismatched packet files.
- The registry excludes the active `ch-first-order-ode.tex` cursor and all R006/R008 work. No excluded file was merged or changed through this admission.

## Exact source and admitted target

- Source: `source/diffyqs-v6.11/ch-nonlin-systems.tex`; 108,130 bytes; 2,629 LF lines; SHA-256 `9af714bde1b6d84f45c7812829e1d5ad099a0866bd0f7d6588f5d2277edc7d22`.
- Packet target before owner corrections: 113,661 bytes; 2,553 lines; SHA-256 `e371977c70ffac5bb5b0939e2361451a41779fa613a13741165e6d3af3167226`.
- Admitted target: `translation/diffyqs/ch-nonlin-systems.tex`; 112,655 bytes; 2,553 LF lines; SHA-256 `08420ee211ac98641c3a6e535c6587ff6890e1515326e627e361c5ed5ea6ee61`.
- Localized figure overlay: `translation/diffyqs/figures/nlin-pend.pdf_t`; 939 bytes; SHA-256 `01bc3cdb0d660cc9f4b53eccc5eb714c2f479bd773caf059c51370f739a789ad`.
- Reusable reader-label overlay: `translation/diffyqs/id-localization.tex`; 3,461 bytes; SHA-256 `1f02f6678c1d2ebeb44f8b881e2206ed70d4345283eb188f8f579815ee3b062b`.

## Owner corrections and terminology decisions

The owner reviewed the complete packet target rather than admitting it mechanically. Eight definite fluency defects and two smaller continuity defects were corrected without changing mathematical content. The changes include grammatical repair of a directional-region sentence, removal of an `adalah bahwa apakah` construction, lowercasing the index key `siklus limit`, idiomatic bounded-region wording, `diferensiabel secara kontinu`, an explicit positive-or-negative formulation for “takes both signs,” `barisan titik`, `suatu titik acak`, `sepanjang suatu lingkaran hampiran`, and smoother positive-population wording.

R007 terminology is now fixed as follows: `initial condition` → `kondisi awal`; `source/sink` → `sumber/serapan`; `spiral source/sink` → `sumber spiral/serapan spiral`; `limit cycle` → `siklus limit`; `Poincaré section` → `penampang Poincaré`; technical noun `chaos` remains `chaos`, while the adjective is `kaotik`. These choices agree with the already admitted R007 first-order chapter and the lane's Indonesian field-usage evidence. The 24 new R007 core terms are recorded separately in `00_control/TERMINOLOGY.csv`; existing cross-resource concepts are extended rather than duplicated.

## Structural and mathematical replay

`qa/R007_NONLINEAR_SYSTEMS_STRUCTURAL_OWNER_20260824.json` is the machine-readable owner replay: 7,424 bytes; SHA-256 `2b5cee22a3fc8c408b69fe60a836f9f4f45bcd820c90c57c2f15665ab1c254b3`; PASS with no failures.

The admitted target preserves, in order:

- 1,591/1,591 named commands;
- 444/444 environment boundaries;
- 66/66 key macros;
- 26/26 figure calls;
- 735/735 inline-math payloads;
- 70/70 display-math payloads;
- 31 unique labels, all retained;
- 1,235 opening and 1,235 closing braces, balanced at final depth zero.

Required content counts also agree: one chapter, five sections, fifteen subsections, eleven examples, two theorems, forty-three exercises, sixteen selected solutions, ten citations, one table, eighteen captions, ten footnotes, four `inputpdft` calls, twenty-two `diffyincludegraphics` calls, and four `sectionnewpage` controls. Independent mathematical review found no semantic or formula defect. All stable and external label dependencies are intentional; bibliography dependencies `BD` and `EP` and the 26 occurrence-aware figure calls are present. The localized `nlin-pend.pdf_t` remains a locale-specific overlay over the unchanged upstream PDF asset.

## Integrated build and reader-facing QA

The owner built the exact v6.11 book in the bounded stage `tmp/r007-hp-lebl-r007-001-owner-build-20260824`, replacing only this chapter and its localized overlay. The official CTAN `tasks.sty` was vendored into the stage because the local MiKTeX package manager was unavailable; it is not part of the pinned source or admitted translation.

Final deterministic sequence: `pdflatex` PASS, `makeindex` PASS (585 accepted entries, zero rejected), then convergent `pdflatex` passes. The final 472-page integrated proof is 5,083,112 bytes, SHA-256 `27352ff1ca53f89f370c329bfa176bbcc3d2e313419ea14170b4dd08fe46ccb3`; it has zero TeX errors, zero undefined references or citations, and zero rerun request. It is a QA proof containing untranslated upstream chapters and therefore is **not** a reader release.

All 39 physical pages of the translated chapter (351–389) were rendered at 100 dpi. Representative pages 351, 359, 376, 387, and 389 were inspected at original render resolution after localization. The chapter, tables, figures, captions, headings, references, footnotes, and exercises are centered, unclipped, and readable. An extracted-text scan of pages 351–389 finds no remaining English scaffold labels (`Chapter`, `Note`, `Example`, `Figure`, `Exercise`, `Theorem`, `Proof`, `Table`, or English varioref page phrases). The overlay produces `Bab`, `Catatan`, `Contoh`, `Gambar`, `Tabel`, `Latihan`, `Teorema`, `Bukti`, and Indonesian page-reference phrases.

## Stable unit map

Every source and target line is owned exactly once. Section-opening units begin at the preceding `sectionnewpage`, so page-break controls are not attached to the wrong unit.

| # | Stable unit suffix after `diffyqs.v6.11.nonlinear-systems.` | Source lines | Target lines |
|---:|---|---:|---:|
| 1 | `linearization-critical-points-equilibria.opening` | 1–69 | 1–69 |
| 2 | `linearization-critical-points-equilibria.autonomous-systems-phase-plane` | 70–200 | 70–200 |
| 3 | `linearization-critical-points-equilibria.linearization` | 201–334 | 201–334 |
| 4 | `linearization-critical-points-equilibria.exercises` | 335–540 | 335–540 |
| 5 | `stability-classification.opening` | 541–549 | 541–549 |
| 6 | `stability-classification.isolated-critical-points-almost-linear` | 550–596 | 550–596 |
| 7 | `stability-classification.stability-classification` | 597–766 | 597–766 |
| 8 | `stability-classification.centers` | 767–844 | 767–843 |
| 9 | `stability-classification.conservative-equations` | 845–940 | 844–939 |
| 10 | `stability-classification.exercises` | 941–1064 | 940–1064 |
| 11 | `applications.opening` | 1065–1081 | 1065–1081 |
| 12 | `applications.pendulum` | 1082–1326 | 1082–1313 |
| 13 | `applications.predator-prey-lotka-volterra` | 1327–1569 | 1314–1553 |
| 14 | `applications.exercises` | 1570–1765 | 1554–1750 |
| 15 | `limit-cycles.exposition` | 1766–2097 | 1751–2058 |
| 16 | `limit-cycles.exercises` | 2098–2194 | 2059–2153 |
| 17 | `chaos.opening` | 2195–2265 | 2154–2220 |
| 18 | `chaos.duffing-strange-attractors` | 2266–2467 | 2221–2405 |
| 19 | `chaos.lorenz-system` | 2468–2554 | 2406–2478 |
| 20 | `chaos.exercises` | 2555–2629 | 2479–2553 |

## Provenance and boundary

Translation, owner integration, and QA were performed with **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the user's instruction. Upstream author and source credit, license, and human-contributor credit remain controlling. This admission does not make R007 complete: the canonical contiguous cursor remains in `ch-first-order-ode.tex`, and untranslated R007 chapters remain. No author was contacted and no upstream issue was opened.
