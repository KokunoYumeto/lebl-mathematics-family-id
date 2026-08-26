# R006 Section 11.7 complete reader — U393

Status: **PASS; 224-page centered reader promoted**  
Date: 2026-08-26  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact boundary and artifact

- Live target: `translation/ra/ch-approximate.tex`, 194,239 bytes / 5,481 LF lines, SHA-256 `f78bb158c48d33deb40424c18855a369ded1122929cdbc532de9d389c28e0fdc`.
- Deterministic cutoff: target lines 1–4208, after the complete Section 11.7 exercise suite and before `\sectionnewpage` / Section 11.8.
- Prefix: 155,064 bytes, SHA-256 `fcaf7baefb0a3356be1c1bc1625b90f90e899c8334ba11337f320c71a1b8fa21`.
- Installed partial: 155,141 bytes, SHA-256 `1bc05e5e8b0b31e21fe89cabbbedafbc0e95f9b013106dac32f2483a60df786b`.
- Reader: `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.7_Latihan.pdf`, 2,281,400 bytes, 224 pages, SHA-256 `5a8db6dd8f9b559c578fe31678943e093650019686e2e75cc752d1b2b49bb211`.

## Reproducible build

- Build directory: `qa/builds/ra-id-volume2-stone-weierstrass-section-complete-reader-u393-20260826`.
- Build script: 4,665 bytes, SHA-256 `1a15bf20d093b0eeb594fae8859dc39cdd3b9e952e58c3c2b542000a37a6ff48`.
- Partial-reader driver: 20,805 bytes, SHA-256 `222b5676017bd33af5492eb36148f46b82c483677b5d562accdb68578cd09f67`.
- The omitted Section 11.8 reference is pinned as nonclickable printed number 11.8; the obsolete Section 11.6/11.7 stubs were removed because both targets are present.
- Converter completed with zero errors. Four index/glossary cycles and nine `pdflatex` passes completed; all seven controlled auxiliary products were byte-stable from pass 8 to pass 9.
- Final log scan found zero undefined references, multiply defined labels, undefined control sequences, LaTeX/package errors, fatal errors, or emergency stops.

## Structural and font QA

- Strict `pypdf` reopen passed: 224 pages, not encrypted, metadata title exact, 862 annotations, 638 link annotations, and 13 top-level outline entries.
- `pdfinfo` reports uniform US-letter pages (612 × 792 pt), zero rotation, and no suspect objects, forms, JavaScript, or encryption.
- An independent `pdffonts` recount of the final packaged PDF enumerated 85 font-object rows; every row is embedded. The expected mathematical Type 1 subsets and the localized DejaVu Serif object are present.
- Full-document text extraction contains no literal `??`, undefined marker, TODO, or placeholder. Tail pages 193–224 contain no English theorem/exercise/figure scaffolding.

## Visual and reflow QA

- Rendered pages 1–2 and every page 193–224 at 120 dpi. Contact-sheet review covered the whole set; pages 201, 202, 207, 208, 210, 211, 213, 214, 215, 217, 219, and 224 were also inspected at full rendered resolution.
- Section 11.7 occupies physical pages 201–215. Its three figures, captions, theorem/proof blocks, formulas, fourteen exercises, correction sentence, bibliography transition, index, and notation list are sharp and readable with no clipping, overlap, black boxes, or broken glyphs.
- On substantive pages 193–215, thresholded content has left/right margins normally 116–121 / 117–120 pixels on a 1,020-pixel page. This proves the text and figures are centered to within five pixels while using about 76.5% of page width. Sparse pages 200 and 215 are intentional section-boundary tails; pages 216 and 218 are intentional recto/verso blanks.
- The promoted output is byte-identical to the visually verified build PDF.

No Git operation, publication transaction, or upstream contact occurred during this build gate.
