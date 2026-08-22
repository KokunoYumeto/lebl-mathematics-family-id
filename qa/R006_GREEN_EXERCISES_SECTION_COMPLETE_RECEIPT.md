# R006 Volume II Green exercise-section checkpoint — 2026-08-23

## Scope

- Completed unit: `ra.v2.green-theorem.exercises`.
- Source: `source/ra-v6.3/ch-multivar-int.tex`, raw lines 3545–3620
  inclusive, the complete seven-exercise Green theorem block.
- Target: `translation/ra/ch-multivar-int.tex`, raw lines 3560–3635
  inclusive, the complete localized exercise block.
- Isolated build: `qa/builds/ra-id-volume2-green-exercises-20260823`.

This unit completes the Green theorem section. It does not complete Chapter 10,
Volume II, R006, or the three-book lane. The change-of-variables section begins
strictly after the admitted boundary.

## Binding, topology, and problem QA

- Source slice: 76 lines, 2,313 UTF-8 bytes, SHA-256
  `f424d4083e37d82d33cd29eb518da5d7e5b248b239ae4332100105d75b772e7f`.
- Target slice: 76 lines, 2,523 UTF-8 bytes, SHA-256
  `8aaa85a86ac5948970ad3a2716951be16c3f3f78b0281ca9c83718a40744d366`.
  Both hashes include a terminating LF.
- All 30 inline-math payloads are raw-byte identical and identically ordered;
  their sequence SHA-256 is
  `1cefa35729feafe9cfa35837353397dec938c3f7643476b72df58d505eed9a6f`.
- Topology is exact: seven `exercise` environments, one `samepage`, two
  `enumerate[a)]` blocks, seven ordered items, and the single
  `label{green:balltype3orient}`. Both slices have 45 opening/45 closing braces
  and 60 dollar delimiters.
- Independent mathematics, final natural formal id-ID, and strict
  topology/raw-math audits passed. The disk/type-III orientation exercise,
  convex-domain result, exact-differential boundary integral, three oriented
  disk integrals, triangle-area formula, harmonic maximum principle, and
  logarithmic singularity/mean-value questions preserve every hypothesis,
  orientation, sign, factor, formula, and requested conclusion.
- The translated index key is `prinsip maksimum!fungsi harmonik`, and
  `LEBL-TERM-0616` admits `maximum principle` as `prinsip maksimum`. The live
  glossary now has 616 rows. English prose residue and mojibake are zero.
- No high-confidence mathematical or typographical source issue was found, so
  no adverse-ledger event was added.

## Build and reader gates

- Converter exited zero and ended `Done! (number of errors 0)`.
  `realanal-out.xml` parses as `pretext` with locale `id-ID`, 672 unique IDs,
  952 references, and zero unresolved references. Exact runtime provenance
  occurs once and the personal-name privacy scan has zero matches.
- Converter stderr contains only the known Windows Perl locale fallback and 67
  optional-`svgo-ll` notices. All requested SVG outputs exist, are nonempty,
  and XML-parse; the TeX/PDF build does not depend on that optimizer.
- Both volumes converge with final passes 4–5 byte-identical. Final logs contain
  zero fatal errors, undefined controls/references, multiply-defined labels,
  rerun warnings, missing characters, or overfull vboxes. Inherited warnings
  remain bounded: Volume I has 17 overfull hboxes (maximum 19.30838 pt), and
  Volume II has 12 (maximum 18.71684 pt).
- Index/glossary gates accept 465/91 entries for Volume I and 253/59 for Volume
  II, with zero rejected entries and warnings.
- Volume II PDF: 235 letter-size pages, unencrypted, `/Lang(id-ID)`, 98 font
  rows all embedded, 27 with ToUnicode. Full extraction has zero U+0133,
  U+FFFD, and personal-name matches; exact runtime provenance and generic user
  attribution each occur once.
- Physical pages 149–150 were rendered at 144 dpi and inspected at original
  detail. All seven exercises, enumerated parts, formulas, running heads, page
  numbers, and section title are centered, readable, unclipped, and
  nonoverlapping. The sparse lower half of page 150 is intentional because the
  following section begins on a new page. The full-tail PDF is QA-only, not a
  public partial reader.

## Artifact hashes

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `ch-multivar-int.tex` | 147,404 | `0836cc282746881971854301c93f35728d8e8e5d0c0f6b0fa55cadb2e3fb3e1c` |
| `TERMINOLOGY.csv` | 83,598 | `a84ad9adec94d3b5e375f5c05bed77e208ece8712db65866fbcf11263c25794c` |
| `converter.console.log` | 1,508,241 | `b1e61af00c1e0ddd504e77ae170cfa95228cb62bdc70712899986174b5924151` |
| `converter.stderr.log` | 6,959 | `45114193e37e1ea25259ecc671dfb5dd2252cda8bcd417294c228206402dc746` |
| `realanal-out.xml` | 1,697,390 | `1bd97e01f7bdb4fb2ba470b3beb44ef0ddf475c924b4724165013fab8d3c5abf` |
| `realanal.tex` | 20,051 | `69744e482f9484a2779ea5fb5a389912d867049983f94b6d5d7065075ed4283f` |
| `realanal2.tex` | 20,444 | `99670a3938d6cd54b7e37158c88185d3baaf9116f2927ff73e57fee5ac1ed03f` |
| `realanal12.tex` | 26,894 | `02a99404add602283fd1b9638b79c4866000e5211674b5f1d876d01462b83678` |
| `realanal.aux` | 359,397 | `f7d44a16a503d8100180e3f5bcd4502a6770fe2eb40994ba4319a01ffc8dffda` |
| `realanal.log` | 111,771 | `521112d05a30031d473afdaa611ddb46df553d3d9289ff943e90732f3fdbef7b` |
| `realanal.pdf` | 2,870,909 | `3a74a74768bd2eb6f454c94107e89abeb430ab42b5a846b6cb1f5c3512d73a21` |
| `realanal2.log` | 101,721 | `a9b4e4b2a922e016afb78e6fc2fdafb45ababe815d51a73baef3c224b36e420f` |
| `realanal2.pdf` | 2,410,208 | `dc405f3b12d813f9924479e7ec0095568ab2ac9c4b06b40fe3c40c57d2b7c990` |
| `realanal.idx` | 21,370 | `1d411d2390b9ee4781862949ca06f3be81f2acc6742bdc55a7dbc9b6fa85d563` |
| `realanal.ind` | 18,827 | `32911ae266ef449e91cb98e8dbb0a3a8e391643eeda1707cc56f1366033c5ffa` |
| `realanal.glo` | 8,640 | `f295085e149fad7adfadc4c67532f0346b282a32d718ace11209a066a25daef8` |
| `realanal.gls` | 9,564 | `3d04f3401d40290ede0de2640d3c67bf557faf0578007798368c9ce8b5f9eef2` |
| `realanal2.idx` | 11,863 | `5191bed9eaf52c443be214499a08b7bb2466547c3e183c6c11f4ec0f90561d76` |
| `realanal2.ind` | 11,260 | `a2ea285b8f4db8a5cba51fa64837d303599de77bcec63649a115a6553e59a794` |
| `realanal2.glo` | 5,596 | `1033afc3382e773b337abfd580f9b23d5ca00794949b9f6a8f44e407a11374e1` |
| `realanal2.gls` | 6,287 | `e24d2ad06d5717ef09aba67942e65e21e7ca71a67ab500b984e0af9ef75c0fac` |
