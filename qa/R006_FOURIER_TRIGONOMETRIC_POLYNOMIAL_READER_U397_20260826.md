# R006 Section 11.8.1 trigonometric-polynomial reader — U397

Status: **PASS; 226-page centered reader promoted**  
Date: 2026-08-26  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact boundary and artifact

- Live target: `translation/ra/ch-approximate.tex`, 194,506 bytes / 5,481 LF lines, SHA-256 `3de28aaac5ce08b69e97060ea01fe7f1d0e7b9d1c024e2fad49e9ece3893b839`.
- Deterministic cutoff: target lines 1–4,370, immediately after the complete Section 11.8.1 proof and before `\subsection{Fourier series}` at line 4,371.
- Admitted prefix: 159,829 bytes, SHA-256 `623b0fa87ea96a68f32de75dd2d806627650cbfcd394c64a6ed1fa96cf802b5c`.
- Installed partial: 159,915 bytes, SHA-256 `cda236d10652b42e89784cc584e45efd5553092c16a15a8d96e9ac6579fc168b`.
- Promoted reader: `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.8.1_Polinom_Trigonometrik.pdf`, 2,292,242 bytes, 226 pages, SHA-256 `40b2e2cb27dd59d288ef76453ae293558fcd1ae8efb96e1e87a646f8f0b8f73d`.

## Reproducible build

- Build directory: `qa/builds/ra-id-volume2-fourier-trigonometric-polynomial-reader-u397-20260826`.
- Build script: 4,971 bytes, SHA-256 `d4cf590c9be45ec7d0dc9a17a3a688fa5fc5fd452ec84c7b7e90c91aeb872da4`.
- Partial-reader driver: 20,444 bytes, SHA-256 `99670a3938d6cd54b7e37158c88185d3baaf9116f2927ff73e57fee5ac1ed03f`.
- The complete Indonesian Volume I auxiliary label set was deterministically regenerated in draft mode and bound into the Volume II build: `realanal.aux`, 354,013 bytes, SHA-256 `8696b0f4e80ddfe0093da26955f868304892bf081eb01c04d21feedd1815d5c2`.
- The first attempted build failed closed before TeX because one inherited assertion still expected the English section title. The assertion was corrected to the admitted Indonesian title `Deret Fourier`.
- A subsequent provisional build exposed the absence of `realanal.aux`: 24 undefined cross-volume reference warnings and visible `??` markers. No provisional bytes were promoted. After regenerating the exact Volume I labels, the final nine-pass build completed with zero undefined references, multiply defined labels, undefined control sequences, LaTeX/package errors, fatal errors, emergency stops, rerun warnings, or missing labels.
- Converter output ended with `Done! (number of errors 0)`. `realanal-out.xml` is 1,675,326 bytes, SHA-256 `8d37de31ad6cd569ee6597a2e52bfb26243e155f125b366dda8f41788318e2ee`; it parses as `pretext`, language `id-ID`, with 32,487 elements, 660 unique IDs, zero duplicate IDs, 934 references, and zero unresolved references.
- The final TeX log is 101,797 bytes, SHA-256 `25c1b010b7b0300e3f9f9afdf0b6c28f26f907de94dd4dd1f6539b40fd1b3495`. Seven controlled auxiliary products were byte-stable between passes 8 and 9.

## Mathematical and language QA

- Independent no-edit comparison passed U309–U312: source lines 4,201–4,361 correspond to target lines 4,209–4,369.
- All ten displayed equation blocks match after localizing only prose inside cases; all 32 environment delimiters retain their order; `\label{sec:fourier}` is preserved.
- The only added inline formulas are the documented correctness clarification `$n \neq 0$` and the `$n=0$` case. They repair the source's unconditional use of $e^{inx}/(in)$ without changing the integral or coefficient-recovery result.
- The opening, Laurent-polynomial interpretation, eigenfunction motivation, periodicity, coefficient recovery, real-valued criterion, and linear-independence proof are faithful and natural in Indonesian. No reader-facing English residue was found.

## Structural, text, and font QA

- Strict `pypdf` reopen: 226 pages; unencrypted; 870 annotations; 644 valid links (622 internal and 22 URI); 1,227/1,227 valid named destinations; 33/33 valid outline items; zero malformed annotations or link targets; no JavaScript or AcroForm field tree.
- The 226 inherited 3×3-point `/Widget` annotations are the established Acrobat-reader workaround also present in the predecessor build; they are not content fields and have no AcroForm tree.
- `pdfinfo` confirms uniform US-letter pages (612 × 792 pt), zero rotation, no encryption, and no JavaScript. All 85 rows reported by `pdffonts` are embedded.
- Full-document layout-preserving extraction is 765,100 bytes, SHA-256 `895b837f8bb90d4b2cb9e9d08fe44f8b43eacdb93bc624829839a3afd84ca4f4`; it contains zero literal `??`, TODO, TBD, placeholder, untranslated marker, or similar scaffold.
- The log has 15 inherited overfull horizontal boxes, all below 20 pt and all before the new Section 11.8.1 source lines. It has zero overfull vertical boxes and zero missing-character warnings.

## Visual and reflow QA

- Rendered physical pages 1–2 and 212–226 at 144 dpi. The 17-page render set totals 3,522,985 bytes; its canonical logical inventory is 1,442 bytes with SHA-256 `9b529bf46c0c6f81e3da9fece5d5a3ada40536fa22dbf46fa0664eaf7ed44850`.
- Contact-sheet review covered every rendered page. Physical pages 216–218 were additionally inspected at original render resolution; pages 216–217 contain the new Section 11.8/11.8.1 material, and page 218 is the intentional recto/verso blank before the bibliography.
- On pages 216–217, thresholded ink begins at x=143 and ends at x=1082/1083 on a 1,224-pixel-wide render: left/right margins differ by at most three pixels, content uses approximately 77% of page width, and no ink touches the outer ten-pixel boundary.
- Result: sharp, centered, readable text and mathematics with zero clipping, overlap, black boxes, broken glyphs, or header/footer/page-number defects.

An independent final-byte audit repeated the log, text, destination, outline, link, font, annotation, and representative visual checks and returned PASS with no concrete defect. It also proved that the remaining 15 overfull and five underfull box warnings match the predecessor U393 warning multiset and were not introduced by U397.

The promoted output is byte-identical to the visually verified build PDF. No upstream author contact occurred.
