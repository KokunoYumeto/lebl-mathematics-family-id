# R006 Volume II Green theorem type-III proof checkpoint — 2026-08-22

## Scope

- Lane: R006, *Basic Analysis II* / *Analisis Dasar II*.
- Completed unit: `ra.v2.green-theorem.type-iii-proof`.
- Frozen source slice: `source/ra-v6.3/ch-multivar-int.tex`, raw lines
  3273–3354 inclusive, the complete proof of Green's theorem for a type-III
  domain.
- Live target slice: `translation/ra/ch-multivar-int.tex`, raw lines
  3286–3366 inclusive, the complete localized proof.
- Isolated build directory:
  `qa/builds/ra-id-volume2-green-type-iii-proof-20260822`.

This is one contiguous proof unit, not the complete Green section, Chapter 10,
Volume II, R006, or three-book lane. The next source sentence at raw line 3356
and the following example remain outside the admitted boundary.

## Source/target binding and proof topology

- Source slice: 82 lines, 2,041 bytes, SHA-256
  `4622798e4e5807b2a2b5c64bfc4075ed766b681f9f3abc8cf20ae77effd7d1e7`.
- Target slice: 81 lines, 2,136 bytes, SHA-256
  `610c0fc54e6c06553dadf2219d300faa13242d38ab030e32eea21c96a792f207`.
- The ordered environment sequence is exact in both slices: one `proof`, four
  `equation*` environments, and one nested `split`; every begin/end balances.
- All four display environments are byte-identical between source and target.
  All 12 inline-math payloads are byte-identical in sequence. Both slices have
  24 dollar delimiters and 40 opening/40 closing braces.
- The single cross-reference remains
  `propref{prop:intovertypeIset}`.
- The type-I iterated integral, two boundary decompositions, the type-II
  iterated integral, all bounds, signs, partial derivatives, orientations, and
  the final Green identity are unchanged.
- Two independent final audits passed after prose polish: mathematical/source
  equivalence and natural formal id-ID/terminology. No high-confidence source
  mathematical issue was found, so no adverse-ledger event was added.
- Reader-facing English residue, U+0133, U+FFFD, and mojibake inside the exact
  admitted proof are zero.

## Attribution privacy and provenance gate

The active repository README and all three R006 reader drivers retain the exact
runtime identification `OpenAI Codex gpt-5.6-sol, Ultra` while attributing the
work generically as performed at the user's instruction. The user's personal
name is absent from the rebuilt Volume I PDF, Volume II PDF, and combined
PreTeXt XML. Jiří Lebl's source authorship, copyright, dual-license notice,
institutional and grant acknowledgments, and all human/source credits remain
unchanged.

## Converter, TeX, index, font, extraction, and visual gates

- Converter final status: `Done! (number of errors 0)`.
- `realanal-out.xml` parses with root `pretext`; locale is `id-ID`; all 672 IDs
  are unique; all 952 references resolve; the exact runtime provenance occurs
  once and the personal-name privacy scan has zero matches.
- Volume I final TeX passes 4–5 exited zero and have identical 36,233-byte
  console logs, SHA-256
  `d37fc577254dce6a9d63c1161f8e2e6bbcb8d7c233c7a077a55a7ac77730df6a`.
- Volume II final TeX passes 4–5 exited zero and have identical 33,083-byte
  console logs, SHA-256
  `afe1eb5a181636e2d851fa8b951de5af43a17aed77a5c66e74c02d949a10818b`.
- Volume I index: 465 accepted, zero rejected/warnings; glossary: 91 accepted,
  zero rejected/warnings. Volume II index: 253 accepted, zero
  rejected/warnings; glossary: 59 accepted, zero rejected/warnings.
- Both final logs contain zero undefined control sequences, emergency stops,
  fatal errors, missing-character diagnostics, undefined references,
  multiply-defined labels, rerun warnings, and overfull vboxes. Inherited
  underfull boxes remain harmless. Volume I has 17 inherited overfull hboxes,
  maximum 19.30838 pt; Volume II has 12, maximum 18.71684 pt. None belongs to
  the new proof or attribution page.
- Volume I PDF: 334 letter-size pages, unencrypted, `/Lang(id-ID)`, 142 font
  rows all embedded, 47 with ToUnicode. Volume II PDF: 233 letter-size pages,
  unencrypted, `/Lang(id-ID)`, 98 font rows all embedded, 27 with ToUnicode.
  Full extraction from both has zero U+0133/U+FFFD and zero personal-name
  matches; each contains the exact runtime provenance once.
- Volume I page 2 and Volume II pages 2, 146, and 147 were rendered at 144 dpi
  after final convergence and inspected at original detail. The generic
  attribution, proof title and prose, all displays, figure handoff, running
  heads, and page numbers are readable, centered, unclipped, and
  nonoverlapping. The final proof identity begins Volume II page 147; the
  following English paragraph and example on that page begin strictly after
  this unit's source cursor.

## Artifact hashes

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `ch-multivar-int.tex` | 146,572 | `33e578858fdb64f2df8271b772852536d4a6305798c611a34477f862d8346a9a` |
| `realanal.tex` | 20,051 | `69744e482f9484a2779ea5fb5a389912d867049983f94b6d5d7065075ed4283f` |
| `realanal2.tex` | 20,444 | `99670a3938d6cd54b7e37158c88185d3baaf9116f2927ff73e57fee5ac1ed03f` |
| `realanal12.tex` | 26,894 | `02a99404add602283fd1b9638b79c4866000e5211674b5f1d876d01462b83678` |
| `converter.console.log` | 1,504,735 | `5c33ccfe02fac6ff7235fa81b0e9ecf2b6d8ce0b37af354b7a370e568bbd72e7` |
| `realanal-out.xml` | 1,696,518 | `844fb160c04e3a8b770c60fd7e875e755caa349118e9d0d77894fbc552e054d8` |
| `realanal.aux` | 359,397 | `f7d44a16a503d8100180e3f5bcd4502a6770fe2eb40994ba4319a01ffc8dffda` |
| `realanal.log` | 111,771 | `2dd3e7fc930bcef515e8cb4a753e0c257fa0aef7c8c38de0b47fd4ee050a2416` |
| `realanal.pdf` | 2,870,909 | `38743ea0e7ce52bdadf5233fc9d6e79e00717f9ba55a393f2bf46ea21c65ef56` |
| `realanal2.log` | 101,636 | `c4d2820bde1596712e700c7d0d66fa28d9bdd18a89df85920ff5990a7ba86fe1` |
| `realanal2.pdf` | 2,407,533 | `00589c2aefaaff5b9ee81d855e3e31dfddb9f1adeea70b9f44d4898c9f72ff60` |
| `realanal.idx` | 21,370 | `1d411d2390b9ee4781862949ca06f3be81f2acc6742bdc55a7dbc9b6fa85d563` |
| `realanal.ind` | 18,827 | `32911ae266ef449e91cb98e8dbb0a3a8e391643eeda1707cc56f1366033c5ffa` |
| `realanal.glo` | 8,640 | `f295085e149fad7adfadc4c67532f0346b282a32d718ace11209a066a25daef8` |
| `realanal.gls` | 9,564 | `3d04f3401d40290ede0de2640d3c67bf557faf0578007798368c9ce8b5f9eef2` |
| `realanal2.idx` | 11,863 | `7426e54830e8b489ba1adafe8631f962d5189c3de8d12ea583570fc3091433f8` |
| `realanal2.ind` | 11,255 | `4eb66ef9add8f238130a68f3e9e181b37b258028e73c5d2b18bb08ccd2302e92` |
| `realanal2.glo` | 5,596 | `c9e69c64131559eea532e31e7071571739736c22b341385ddeaf585990265eb0` |
| `realanal2.gls` | 6,287 | `258cd827db811d211ca573e3b6e5a3e95e2bcfada77b78a54e8d656afb28c7bd` |
