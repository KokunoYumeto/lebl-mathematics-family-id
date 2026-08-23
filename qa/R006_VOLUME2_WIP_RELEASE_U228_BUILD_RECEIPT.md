# R006 Volume II WIP release U228 — 2026-08-23

## Exact reader boundary

This is the public-reader build for the contiguous R006 checkpoint through the
end of Section 10.7, Change of variables. The source-level overlay places one
`\end{document}` immediately after Exercise 10.7.6. Chapter 11 and all later
upstream material are outside the reader and are not claimed as translated.

- Release ID: `r006-v6.3-id-wip.2026.08.23.u228`
- Source overlay: `release/u228/`
- Volume I remains the previously verified complete 334-page reader.
- Volume II reader: 155 letter-size pages; final page contains all six Section
  10.7 exercises.

## Overlay and source identity

| Overlay file | Bytes | SHA-256 |
|---|---:|---|
| `ch-multivar-int.tex` | 148,582 | `678af7cd67a6fc75ab949ffcd12b4cfb98d22d45520397cd48352e06cadecdab` |
| `frag-vol2-intro.tex` | 3,702 | `c94fef51d856c913cb7b717a88945510cb4a6fbeadcc8ae8cda64f8f17f7295e` |
| `realanal2.tex` | 20,681 | `bf561da5e7f5de1c84d6fff01bfeac088e43e2146f07bb7509d546c1c9211fba` |

The live translated `ch-multivar-int.tex` contains 148,566 bytes and SHA-256
`65c8bdb840c9ac573b94b9cc9f971c63fe40d1f07b0ac1f2d595a85b9ca07dd2`; the
16-byte difference is the source-cut `\end{document}` and final newline in the
release overlay.

## Reader and link gates

- Direct `perl convert-to-mbx.pl` exited zero and ended `Done! (number of
  errors 0)`.
- Five `pdflatex` passes completed after explicit index and glossary generation;
  passes 4 and 5 converge byte-for-byte. The final log contains zero LaTeX
  errors, undefined controls or references, rerun warnings, and missing
  characters.
- `realanal-out.xml` is 1,492,179 bytes with SHA-256
  `cc899eb949e02898b9c062cf1a2c2fc3e760718db71dd004cf56a3f3c30ab86e` and
  parses as `pretext`, locale `id-ID`, with 672 unique IDs, 952 references,
  zero duplicate IDs, and zero unresolved references.
- The release PDF is 1,694,008 bytes with SHA-256
  `44907b1bc7b4d11ba0b8c15ddbb76adcf737eb7858107bc8b8a9b99e89eb7294`.
- The PDF has 225 internal links and 21 outline destinations; every one
  resolves within the 155-page reader. No Chapter 11 page or English tail is
  included.
- All 98 font rows are embedded; extraction is clean with zero replacement
  characters and zero workspace-path residue. The exact provenance string
  `OpenAI Codex gpt-5.6-sol, Ultra` occurs once.
- Rendered at 144 dpi and inspected at original detail: front pages 1–2 and
  boundary pages 153–155 show no clipping, overlap, broken glyph, or margin
  defect. Page 155 contains all six exercises in a readable centered layout.

## Source-defect truth

Exercise 10.7.5 carries the bounded zero-extension correction recorded as
`LEBL-ID-ADV-0221`. Exercise 10.7.6 is preserved as printed despite the
high-confidence unbounded-integrand counterexample recorded as
`LEBL-ID-ADV-0222`; no speculative mathematical repair was inserted.

The source author remains Jiří Lebl. The dual-license notice, bibliography,
acknowledgments, and human credits are preserved. This independent Indonesian
derivative selects CC BY-SA 4.0 and identifies the runtime as OpenAI Codex
gpt-5.6-sol, Ultra acting on the user's instruction. No author or maintainer
was contacted.

## Principal hashes

| File | Bytes | SHA-256 |
|---|---:|---|
| `realanal2.pdf` | 1,694,008 | `44907b1bc7b4d11ba0b8c15ddbb76adcf737eb7858107bc8b8a9b99e89eb7294` |
| `realanal-out.xml` | 1,492,179 | `cc899eb949e02898b9c062cf1a2c2fc3e760718db71dd004cf56a3f3c30ab86e` |
| `realanal2.log` | 94,631 | `3e606aa2b6fe590ca08ecffbdd411d9db39dbfd538fe051ce30a4eac215405eb` |
| `realanal2.extracted.txt` | 535,274 | `3bcd092ba1b399216c8afde3429840ac010935f3039e6f26578b4f6527e9bf14` |
