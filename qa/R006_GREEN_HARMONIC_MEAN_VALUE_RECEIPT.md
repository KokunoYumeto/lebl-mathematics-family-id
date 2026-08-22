# R006 Volume II harmonic mean-value example checkpoint — 2026-08-23

## Scope

- Completed unit: `ra.v2.green-theorem.harmonic-mean-value-example`.
- Source: `source/ra-v6.3/ch-multivar-int.tex`, raw lines 3456–3543
  inclusive, the complete harmonic-function example and mean-value-property
  derivation.
- Target: `translation/ra/ch-multivar-int.tex`, raw lines 3471–3558
  inclusive, the complete localized example.
- Isolated build: `qa/builds/ra-id-volume2-green-harmonic-mean-value-20260823`.

This is one contiguous example, not the complete Green section, Chapter 10,
Volume II, R006, or the three-book lane. The exercise subsection beginning
immediately afterward remains outside this unit.

## Binding, topology, and mathematical QA

- Source slice: 88 lines, 2,398 UTF-8 bytes, SHA-256
  `a7f1c01ae08381cdbab13b55fd14e8a23d7d2fa0f2b200b812324abac6ad4858`.
- Target slice: 88 lines, 2,525 UTF-8 bytes, SHA-256
  `3f6e0f2d2c2fca3454277001f3a241d2beec45d962195f9d86f3669431c85dfb`.
  Both hashes include a terminating LF.
- All 20 inline-math payloads and all three `equation*` payloads are
  raw-byte identical and identically ordered; the NUL-joined inline sequence
  has SHA-256
  `c30849f824d04ed114d8cb9a78e3a2d74d1fe2cacfb40348a428c502b4004f3b`.
- Environment topology is exact: one outer `example`, three `equation*`
  environments, and one `split`; all nesting balances. Both slices have 59
  opening/59 closing braces and 40 dollar delimiters. The single
  `exerciseref{green:balltype3orient}` is preserved.
- Independent mathematical, natural formal id-ID/terminology, and strict
  topology/formula audits passed. With `P=-f_y` and `Q=f_x`, Green's theorem
  yields the Laplacian integral; the positive circle parametrization gives the
  displayed radial derivative; `g'=0` and continuity at zero yield the center
  value; and `ds=r dt` gives the factor `1/(2 pi r)`. All signs, radius factors,
  hypotheses, closure condition, and conclusions are preserved.
- `C(p,r)` is defined elsewhere in the pinned edition as the closed ball, so
  the source identity `overline{D_r}=C(p,r)` is consistent. No source issue was
  found and no adverse-ledger event was added.
- Terminology rows `LEBL-TERM-0613` through `LEBL-TERM-0615` admit `fungsi
  harmonik`, `persamaan Laplace`, and `sifat nilai rata-rata`. The live glossary
  now has 615 rows. English prose residue and mojibake within the unit are zero.

## Build and reader gates

- Converter exited zero and ended `Done! (number of errors 0)`.
  `realanal-out.xml` parses as `pretext` with locale `id-ID`, 672 unique IDs,
  952 references, and zero unresolved references. Runtime provenance occurs
  once and the personal-name privacy scan has zero matches.
- Converter stderr contains only one Windows Perl locale fallback and 67
  notices that optional `svgo-ll` is unavailable. All 67 requested SVGs exist,
  are nonempty, and parse as XML; these notices do not affect the TeX/PDF build.
- Both volumes converged with final passes 4–5 byte-identical. Final logs have
  zero fatal errors, undefined controls/references, multiply-defined labels,
  rerun warnings, missing characters, or overfull vboxes. Inherited warnings
  remain bounded: Volume I has 17 overfull hboxes (maximum 19.30838 pt), and
  Volume II has 12 (maximum 18.71684 pt).
- Index/glossary gates: Volume I accepts 465/91 entries; Volume II accepts
  253/59; all reject and warning counts are zero.
- Volume II PDF: 235 letter-size pages, unencrypted, `/Lang(id-ID)`, 98 font
  rows all embedded, 27 with ToUnicode. Full extraction has zero U+0133,
  U+FFFD, and personal-name matches; exact runtime provenance and generic user
  attribution each occur once.
- Physical pages 148–149 were rendered at 144 dpi and inspected at original
  detail. Prose, all three displays, running heads, links, and page numbers are
  centered, readable, unclipped, and nonoverlapping. The following untranslated
  exercise block starts strictly after the admitted example. The full-tail PDF
  is QA-only, not a public partial reader.

## Artifact hashes

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `ch-multivar-int.tex` | 147,194 | `b5852dfcc186649e33459ce88a46e492965d33eac33ae33c58fecb89fe961404` |
| `TERMINOLOGY.csv` | 83,455 | `053ba1367bf1340c7f29cd1153e9d51da4cab41c674abee115ea33739b92590f` |
| `converter.console.log` | 1,508,018 | `aec61c8fc1db85d7f87b6bb7ec10fbbcc5a692002829e5ed2f8cca502eb8519b` |
| `converter.stderr.log` | 6,959 | `45114193e37e1ea25259ecc671dfb5dd2252cda8bcd417294c228206402dc746` |
| `realanal-out.xml` | 1,697,152 | `6a76f82ba42f8c71dbb8d6fad1c6de44874976865810d519543fcc4fab1ccf04` |
| `realanal.tex` | 20,051 | `69744e482f9484a2779ea5fb5a389912d867049983f94b6d5d7065075ed4283f` |
| `realanal2.tex` | 20,444 | `99670a3938d6cd54b7e37158c88185d3baaf9116f2927ff73e57fee5ac1ed03f` |
| `realanal12.tex` | 26,894 | `02a99404add602283fd1b9638b79c4866000e5211674b5f1d876d01462b83678` |
| `realanal.aux` | 359,397 | `f7d44a16a503d8100180e3f5bcd4502a6770fe2eb40994ba4319a01ffc8dffda` |
| `realanal.log` | 111,771 | `0a1099818c8d6af1d0633844dff14978bee868f3185c43e3085a9e136548bc64` |
| `realanal.pdf` | 2,870,909 | `e955764f92a5c84153a69e625fc8a0ab6c9343f03d89cfc3073f8b96d4ee905b` |
| `realanal2.log` | 101,721 | `73197c7336a4e2262637be4a9bb8dd159f370f8d6356a78c15da3a7154285d96` |
| `realanal2.pdf` | 2,410,073 | `3a853b356a37205f71fa1141d4ce8b091d4ae9d2525fb20221c3f41f47d6f1e9` |
| `realanal.idx` | 21,370 | `1d411d2390b9ee4781862949ca06f3be81f2acc6742bdc55a7dbc9b6fa85d563` |
| `realanal.ind` | 18,827 | `32911ae266ef449e91cb98e8dbb0a3a8e391643eeda1707cc56f1366033c5ffa` |
| `realanal.glo` | 8,640 | `f295085e149fad7adfadc4c67532f0346b282a32d718ace11209a066a25daef8` |
| `realanal.gls` | 9,564 | `3d04f3401d40290ede0de2640d3c67bf557faf0578007798368c9ce8b5f9eef2` |
| `realanal2.idx` | 11,867 | `d4e45a212df9ab0b47839dce45eab18d0b6c69b7d815cb7bba7069658e57605a` |
| `realanal2.ind` | 11,238 | `bca8c34d2f2c704dc79babbfbba0130d50d875f76426e6e87ea65bf2151d4618` |
| `realanal2.glo` | 5,596 | `1033afc3382e773b337abfd580f9b23d5ca00794949b9f6a8f44e407a11374e1` |
| `realanal2.gls` | 6,287 | `e24d2ad06d5717ef09aba67942e65e21e7ca71a67ab500b984e0af9ef75c0fac` |
