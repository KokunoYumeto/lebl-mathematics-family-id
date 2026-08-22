# R006 Volume II Green theorem statement and type-domain checkpoint — 2026-08-22

## Scope

- Lane: R006, *Basic Analysis II* / *Analisis Dasar II*.
- Completed unit: `ra.v2.green-theorem.statement-and-type-domains`.
- Frozen source slice: `source/ra-v6.3/ch-multivar-int.tex`, raw lines
  3213–3271 inclusive, the Green theorem statement through the complete
  type-I/II/III setup and pre-proof handoff.
- Live target slice: `translation/ra/ch-multivar-int.tex`, raw lines
  3230–3284 inclusive, the complete localized unit.
- Isolated build directory:
  `qa/builds/ra-id-volume2-green-statement-types-20260822`.

The isolated build contains the exact live target chapter: 146,477 bytes,
SHA-256 `eb718a8e48aef9d21297a4e4d1472ccdb2c5e01899424ce6ff1b429c964570db`.
The converter, both Volume I and Volume II indexes/glossaries, and all final
TeX passes exited zero. Final passes 4 and 5 for each volume have byte-identical
console logs and prove convergence. This is one contiguous Green-section unit,
not the complete section, Chapter 10, Volume II, R006, or three-book lane.

## Unit binding and topology

- Source slice: 59 lines, 2,380 bytes; SHA-256
  `e08f88792820c752a5af7e559cdec05759b563a7a25a7a1209640e4d3452008b`.
- Target slice: 55 lines, 2,542 bytes; SHA-256
  `5e03ead8145654c259cc26557e51eb462c93161fbc50b81eafd666db57449fe5`.
- Exact ordered topology is preserved: one `thm`, three `equation*` displays,
  and one `myfigureht`; all five begins and ends balance in source order.
- Four index hooks are preserved and localized (`teorema Green`, `domain tipe
  I`, `domain tipe II`, `domain tipe III`). The sole xref and label remain
  `figureref{fig:greenstypes}` and `label{fig:greenstypes}`. The theorem is
  intentionally unlabeled in both source and target.
- Both slices contain 33 opening and 33 closing braces, 28 dollar delimiters,
  and 14 identical inline-math payloads. The three display skeletons are exact;
  only the two mathematical prose fragments `text{and}`→`text{dan}` are
  localized.
- The localized `greenstypes.xp` differs from source only in the three visible
  labels `type I/II/III`→`tipe I/II/III`; every drawing command and coordinate
  is unchanged. The generated PDF retains 290×110 pt geometry, and the SVG a
  290×110 viewBox. All labels are visible and unclipped.
- Complete Indonesian alternative text describes the three panels and their
  vertical/horizontal connected-interval behavior. The converter binds it as
  `raimage/shortdescription`, and `alttexts.txt` carries the same description.
- Mathematical/formula, topology, terminology, accessibility, and render
  replay passed. No source correction was needed in this unit. Reader-facing
  English residue and U+0133/U+FFFD inside the admitted boundary are zero.

## One-time Indonesian field-usage QA and provenance

Before admission, a bounded arXiv search found no relevant manuscript with
both Indonesian main text and downloadable TeX. The TeX source of
arXiv:2008.00182 was downloaded and inspected but rejected as terminology
evidence because its actual text is English. The honest fallback was Prof. Dr.
Supama's 60-page Universitas Terbuka MATA4217 *Analisis I*, Modul 1,
`universitas-terbuka-MATA421702-M1.pdf`, 1,384,321 bytes, SHA-256
`6d55ddc986abb1a6df5513d6d5db88ff86f6709fe8358e14d8a7ae2850485412`.
The PDF was text-inspected page by page and visually inspected on PDF pages 1,
2, 6, 10, and 42.

The QA standardized `Cartesian product` to `hasil kali Kartesius` and
`countably infinite` to the directly attested `terhitung tak hingga`; all 15
old live occurrences were propagated. Domain/codomain/cardinality choices were
retained while attested explanatory variants were added. The exact evidence,
rejected arXiv near-hit, comparisons, and rationale are recorded in
`authority/terminology_evidence/2026-08-22-indonesian-field-usage-qa/TERMINOLOGY_QA_REPORT.md`,
6,016 bytes, SHA-256
`d230066a027a57a6b5a92399cb0a2e213a2dab7139b14dbd34f8de45a334e300`.
`00_control/TERMINOLOGY.csv` remains 611 data rows, 82,901 bytes, SHA-256
`9e77124b340e62662e1a6f074c22fca1cfdcf946f653f6e3ca90d342fc3d5e64`.

Every R006 reader driver and the lane README now identify the translating and
editing runtime exactly as `OpenAI Codex gpt-5.6-sol, Ultra`. Jiří Lebl's source
authorship, copyright, licenses, institutional credits, grant acknowledgments,
and every human credit remain unchanged. The provenance string is present in
both rebuilt PDFs and the combined PreTeXt XML.

## Converter, TeX, and visual gates

- Converter final status: `Done! (number of errors 0)`.
- `realanal-out.xml` parses with root `pretext`; declared locale is `id-ID`;
  672 IDs are all unique; 952 references have zero unresolved targets.
- Volume I final TeX passes 4–5 exited zero and have identical 36,233-byte
  logs, SHA-256
  `462a4f7ac0834f53f89306f8376432a5a577988f9f7c4b35946aa5c41a3426d7`.
- Volume II final TeX passes 4–5 exited zero and have identical 33,083-byte
  logs, SHA-256
  `669d9fee8d50b2ac509f5f3be2a3258cc1b5dc0490fd1746d160c573ffa31892`.
- Volume I index: 465 accepted, zero rejected/warnings; glossary: 91 accepted,
  zero rejected/warnings. Volume II index: 253 accepted, zero
  rejected/warnings; glossary: 59 accepted, zero rejected/warnings.
- Both logs contain zero undefined control sequences, emergency stops, fatal
  errors, missing-character diagnostics, undefined references,
  multiply-defined labels, rerun warnings, and overfull vboxes. Inherited
  underfull boxes remain harmless. Volume I has 17 inherited overfull hboxes,
  maximum 19.30838 pt; Volume II has 12, maximum 18.71684 pt. No changed unit or
  terminology/provenance page has clipping or overlap.
- Volume I PDF: 334 letter-size pages, unencrypted, `/Lang(id-ID)`, 142 font
  rows all embedded, 47 with ToUnicode. Volume II PDF: 233 letter-size pages,
  unencrypted, `/Lang(id-ID)`, 98 font rows all embedded, 27 with ToUnicode.
  Full extraction from both has zero U+0133 and U+FFFD.
- Physical Volume I pages 2, 16, and 25 and Volume II pages 2, 145, and 146
  were rendered at 144 dpi after final convergence and inspected at original
  detail. Provenance, terminology, theorem, displays, type definitions, figure,
  localized labels, caption, xref, running heads, and page numbers are readable,
  centered, unclipped, and nonoverlapping. The English proof beginning on
  Volume II page 146 is strictly beyond this unit's cursor.

## Artifact hashes

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `ch-multivar-int.tex` | 146,477 | `eb718a8e48aef9d21297a4e4d1472ccdb2c5e01899424ce6ff1b429c964570db` |
| `ch-vol1-intro.tex` | 57,887 | `ef0075e766143e147dd6fc382ff9e4a5b33ebff004c6d4ead3e69b3140bca8b2` |
| `ch-real-nums.tex` | 89,211 | `fff61366f94bfb74229b921dce8d21b95fcbea3e24fc3b1bc92f293006fb732b` |
| `notations.tex` | 15,808 | `dfbf2c9a903847bd74ef91c95835d30833e9a2266a0a64f5049072bafe612d04` |
| `realanal.tex` | 20,050 | `a88f807c10dbf00674f6dabf01bcc53bcb406c941cab411be7aab285defd59d4` |
| `realanal2.tex` | 20,443 | `ee3e1282711af6cf5803327a2bba0e05933a37fb3d5c64b18299abcee8345d1f` |
| `realanal12.tex` | 26,892 | `b816d73c075b58eaced97b865b621d5a8ed284675c9bf627c74a9d9cc717193d` |
| `converter.console.log` | 1,504,640 | `4bf7d4607aa5c55a9437e9f73fb701a5ff1bbdcd4160ed8b9b2e8e76636099cb` |
| `realanal-out.xml` | 1,696,423 | `7064d2ffaadd2c0ea1bbfba91bc67428467955533327e09ace8d11b65714123b` |
| `realanal.aux` | 359,397 | `f7d44a16a503d8100180e3f5bcd4502a6770fe2eb40994ba4319a01ffc8dffda` |
| `realanal.log` | 111,771 | `fb0c58faa31bf3c70a2f84c5d797856a726b6fefe0004f263afde549b30f2549` |
| `realanal.pdf` | 2,870,910 | `bf1ec8277530c134bfa06ac9952709c41d91e4427f865a1c19043ef5c3b5ffbf` |
| `realanal2.log` | 101,636 | `0726b7bf6b6df30fa88fc441804ef0d6bb2c0050f1fb2edbe767280be770cc63` |
| `realanal2.pdf` | 2,407,322 | `28cd6eec8d3c359adcc2d457f63332d6a8ad852dc24d0aa4412f1a622f344924` |
| `realanal.idx` | 21,370 | `1d411d2390b9ee4781862949ca06f3be81f2acc6742bdc55a7dbc9b6fa85d563` |
| `realanal.ind` | 18,827 | `32911ae266ef449e91cb98e8dbb0a3a8e391643eeda1707cc56f1366033c5ffa` |
| `realanal.glo` | 8,640 | `f295085e149fad7adfadc4c67532f0346b282a32d718ace11209a066a25daef8` |
| `realanal.gls` | 9,564 | `3d04f3401d40290ede0de2640d3c67bf557faf0578007798368c9ce8b5f9eef2` |
| `realanal2.idx` | 11,863 | `7426e54830e8b489ba1adafe8631f962d5189c3de8d12ea583570fc3091433f8` |
| `realanal2.ind` | 11,255 | `4eb66ef9add8f238130a68f3e9e181b37b258028e73c5d2b18bb08ccd2302e92` |
| `realanal2.glo` | 5,596 | `c9e69c64131559eea532e31e7071571739736c22b341385ddeaf585990265eb0` |
| `realanal2.gls` | 6,287 | `258cd827db811d211ca573e3b6e5a3e95e2bcfada77b78a54e8d656afb28c7bd` |
| `figures/greenstypes.xp` | 2,061 | `75ffeb0ed99366016bb1510b7509eee8fb72b7898c7c93e047dd2440f2b07aa1` |
| `figures/greenstypes.pdf` | 232,006 | `5d1d3fd38fcf9d263cc922950fbf1b27982df97d694531e90832e990a86fbf69` |
| `figures/greenstypes-mbx.svg` | 20,389 | `2bad5efb73845696add3a2f2e68e0461e817b981f661e549b5e417be59044296` |
| `alttexts.txt` | 66,220 | `c93c9ccdc6740c818b5c1116742962ca5ce5e0af67b975234dafe81c1a4866f7` |
