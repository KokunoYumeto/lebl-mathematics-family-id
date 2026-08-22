# R006 Volume II Green vortex-field example checkpoint — 2026-08-23

## Scope

- Lane: R006, *Basic Analysis II* / *Analisis Dasar II*.
- Completed unit: `ra.v2.green-theorem.vortex-field-example`.
- Frozen source slice: `source/ra-v6.3/ch-multivar-int.tex`, raw lines
  3356–3454 inclusive, the complete vortex vector-field application of
  Green's theorem, including its figure, caption, alternative text, and final
  origin-detection remark.
- Live target slice: `translation/ra/ch-multivar-int.tex`, raw lines
  3368–3469 inclusive, the complete localized example.
- Isolated build directory:
  `qa/builds/ra-id-volume2-green-vortex-example-20260822`.

This is one contiguous example, not the complete Green section, Chapter 10,
Volume II, R006, or the three-book lane. The harmonic-function example that
starts at source raw line 3456 and target raw line 3471 remains outside this
admitted boundary.

## Source/target binding and mathematical topology

- Source slice: 99 lines, 3,868 UTF-8 bytes, SHA-256
  `ab0de28ba77d66318b2b6a0456dbe8c4b20665c30576c84e086fff76150a7dc0`.
- Target slice: 102 lines, 4,363 UTF-8 bytes, SHA-256
  `010fe5356b60b44448a1c434ac50c5f6180eddc82665486b80f62635ceb9490f`.
  Both slice hashes include a terminating LF.
- All 37 inline-math payloads are raw-byte identical and ordered identically;
  the NUL-joined payload sequence has SHA-256
  `010bebaabf7519f61a31489220111f1e8969c761248ac7905fd65994cffe7a3f`.
- All five display payloads are raw-byte identical and occur in the same order:
  `equation*`, `multline*`, `equation*`, `equation*`, `equation*`.
- The complete environment topology is identical: one outer `example`, the
  five displays, and one `myfigureht`, all correctly nested and closed. Each
  slice has 59 opening and 59 closing braces and 74 dollar delimiters.
- The single `figureref{fig:vortexbox}`, `label{fig:vortexbox}`, and
  `myincludepdft{vortexbox}` are preserved. The editable and TeX-overlay figure
  assets are source-identical: `vortexbox.fig` is 2,343 bytes with SHA-256
  `fc5b815a760011b3692623c1816f20eeaddff85ab8785b698ce749dd8107bc25`;
  `vortexbox.pdf_t` is 1,429 bytes with SHA-256
  `76cc159beb6c6920aa676915414fa4a734bd2321146582d85055a74b292929cf`.
- Independent mathematics, strict topology/formula, and final natural-id-ID /
  accessibility audits passed. The rectangle and circle orientations, the
  four type-III subdomains, cancellation on the cuts, zero curl away from the
  origin, and the signs `integral_C = -2 pi` and `integral_gamma = 2 pi` are
  correct. No high-confidence source issue was found.
- Reader-facing English residue and mojibake inside the exact admitted slice
  are zero. Terminology row `LEBL-TERM-0612` admits `vortex vector field` as
  `medan vektor pusaran`; the live glossary now contains 612 rows.

## Provenance, converter, TeX, and reader gates

- The reader drivers retain the exact runtime identification
  `OpenAI Codex gpt-5.6-sol, Ultra`, with generic user-instruction attribution;
  all source-author, copyright, license, institutional, grant, and human
  contributor credits remain intact.
- Converter status: `Done! (number of errors 0)`. The locale warning in the
  separate stderr transcript is the Windows Perl fallback to the system
  locale; conversion exited zero.
- `realanal-out.xml` parses with root `pretext` and locale `id-ID`; all 672 IDs
  are unique and all 952 references resolve. Runtime provenance occurs once
  and the personal-name privacy check has zero matches.
- Volume I and Volume II final TeX passes 4–5 are byte-identical within each
  volume. The final logs contain zero undefined control sequences, emergency
  stops, fatal errors, missing-character diagnostics, undefined references,
  multiply-defined labels, rerun warnings, and overfull vboxes.
- Inherited layout warnings remain bounded: Volume I has 17 overfull hboxes,
  maximum 19.30838 pt; Volume II has 12, maximum 18.71684 pt. Neither affected
  vortex page is clipped or overlapped.
- Volume I index/glossary: 465/91 entries accepted, zero rejected and zero
  warnings. Volume II index/glossary: 253/59 entries accepted, zero rejected
  and zero warnings.
- Volume II PDF: 235 letter-size pages, unencrypted, `/Lang(id-ID)`, 98 font
  rows all embedded, 27 with ToUnicode. Full extraction has zero U+0133,
  U+FFFD, and personal-name matches; runtime provenance and generic
  attribution each occur once.
- Physical pages 147–148 were rendered at 144 dpi and inspected at original
  detail. The complete example, formulas, figure, caption, running heads, and
  page numbers are centered, readable, unclipped, and nonoverlapping. The next
  English harmonic-function unit begins strictly after the admitted boundary
  on page 148. This full-tail PDF is a QA artifact, not a public partial reader.

## Artifact hashes

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `ch-multivar-int.tex` | 147,067 | `0da1a77158a1296fe77bf48afd09dd9a409a7d43ba340a63ceb00e22b475a4c3` |
| `TERMINOLOGY.csv` | 83,042 | `426d6724d153d21095be187c44281baca4fd87ece49c0ff7541cceb269bc164c` |
| `converter.console.log` | 1,504,804 | `9d276518c489d86855f842ca10cb57e7048ccc1d4c88b40c16309c1bab4814db` |
| `converter.stderr.log` | 393 | `57183f2646e20faf44dfd55c212cfffb98328b1d5d3de478116a3bede3a033be` |
| `realanal-out.xml` | 1,697,022 | `7859c5b9df212e17761391e1315397460f0f65ceead7513b7dc3fb18e5bce577` |
| `realanal.tex` | 20,051 | `69744e482f9484a2779ea5fb5a389912d867049983f94b6d5d7065075ed4283f` |
| `realanal2.tex` | 20,444 | `99670a3938d6cd54b7e37158c88185d3baaf9116f2927ff73e57fee5ac1ed03f` |
| `realanal12.tex` | 26,894 | `02a99404add602283fd1b9638b79c4866000e5211674b5f1d876d01462b83678` |
| `realanal.aux` | 359,397 | `f7d44a16a503d8100180e3f5bcd4502a6770fe2eb40994ba4319a01ffc8dffda` |
| `realanal.log` | 111,771 | `e8d6fcef81ee2c719473d46ce60b00cf728b7f8853672a3796059bf32de3f03f` |
| `realanal.pdf` | 2,870,909 | `0f559e3fff40aaf3fe6cc4caa5ff93e21aee04cbd0548243dae71f6ddeee9e4e` |
| `realanal2.log` | 101,722 | `741aa6d16f62b3dabaadb09959a771d8219b4e2253da64802cb2f01b9f5bd225` |
| `realanal2.pdf` | 2,410,126 | `03f721dc31db6e0ae40a8e98ba6bbfb80f4575a3919ea9c7b7e219d7e1c448f3` |
| `realanal.idx` | 21,370 | `1d411d2390b9ee4781862949ca06f3be81f2acc6742bdc55a7dbc9b6fa85d563` |
| `realanal.ind` | 18,827 | `32911ae266ef449e91cb98e8dbb0a3a8e391643eeda1707cc56f1366033c5ffa` |
| `realanal.glo` | 8,640 | `f295085e149fad7adfadc4c67532f0346b282a32d718ace11209a066a25daef8` |
| `realanal.gls` | 9,564 | `3d04f3401d40290ede0de2640d3c67bf557faf0578007798368c9ce8b5f9eef2` |
| `realanal2.idx` | 11,864 | `a355a98cfea3a30afc189341a413ec3a90e75ca343c13edd842e7f75cec70100` |
| `realanal2.ind` | 11,235 | `8b0a85cf7bf0dc2386677a3391204ebc9532e6ae2e60a03601de191d67aa0ce7` |
| `realanal2.glo` | 5,596 | `1033afc3382e773b337abfd580f9b23d5ca00794949b9f6a8f44e407a11374e1` |
| `realanal2.gls` | 6,287 | `e24d2ad06d5717ef09aba67942e65e21e7ca71a67ab500b984e0af9ef75c0fac` |
