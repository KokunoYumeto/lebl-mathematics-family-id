# R006 Volume II change-of-variables theorem checkpoint — 2026-08-23

## Scope and exact boundary

This checkpoint completes Proposition 10.7.1, the statement of the
multivariable change-of-variables theorem, and its full proof. It admits seven
contiguous content units after `ra.v2.change-of-variables.opening`:

| Unit | Source lines | Target lines | Source SHA-256 | Target SHA-256 |
|---|---:|---:|---|---|
| `ra.v2.change-of-variables.linear-volume-scaling` | 3659–3668 | 3673–3682 | `708c8960c20bfb1c918d9fd27077c95f619167a40917623f12939c9e4c26cd1a` | `2cf95e5ca2a317322afb7da2144d11992f91df587288b562af92b3c1f878a4b3` |
| `ra.v2.change-of-variables.theorem-statement` | 3670–3697 | 3684–3711 | `a4f1f087289305a571089874c2508a69d2a87e3ed102a6f04fe13f54680a1392` | `b0f67b97b0daccb17830c64f1e547ed1fad3673ad1716db0df75871bea90bbc8` |
| `ra.v2.change-of-variables.proof-rectangle-reduction` | 3699–3717 | 3713–3731 | `d596f87327d369c2d0159d6d2426637fa7bd05daea46fd7eaf641a20026f46eb` | `88801c09ca4a5f650c9fd4ddfa704eb1349816b1d78e0474efbdeb7686335be8` |
| `ra.v2.change-of-variables.proof-uniform-derivative-control` | 3719–3735 | 3733–3749 | `f0f5e9ebbf11f19f3c0891de16903c90471899511ede9fd4b7629ffea5c275cb` | `915ac2ee7beaf23d3847d53be862ac42d8e1f13f9ff342d334a5ab228b5c008b` |
| `ra.v2.change-of-variables.proof-normalized-volume-claim` | 3737–3838 | 3751–3852 | `599a8c97c226f96b0d164657dcc83b347351a8706bc9eec282a2792038acf878` | `d1a0cc10c79011e6f48a3b48e37e9ad8776eccf781ab005b7322ad8370d70558` |
| `ra.v2.change-of-variables.proof-general-linearization` | 3840–3880 | 3854–3894 | `624ddc8ab1e334a51af48635816e2101d9a2920e47303640d890d50a360a0aec` | `a9a18ad5559cbfb236136e3592dd73b9634ed1e6a5567f5b852f862d38bdf8db` |
| `ra.v2.change-of-variables.proof-integral-equality` | 3882–3944 | 3896–3958 | `dfae6ce5fe98fb5ce2b156ca4a59e971450753797a0f45a55ed3397952372941` | `8fe934423c247ddcd12d8d5a4ce26a4929cbb966809aaf5a304a6b1cfe5744c0` |

Every slice hash covers raw UTF-8 bytes through the LF terminating its final
line. The exercise subsection begins at source line 3946 / target line 3960
and is strictly outside this checkpoint. The isolated build directory is
`qa/builds/ra-id-volume2-change-vars-theorem-20260823`.

## Translation, mathematics, and topology QA

- Independent audits passed for every unit. All inline and displayed
  mathematics is byte-identical and identically ordered within each paired
  slice. Proposition, theorem, proof, equation, split, figure, label, and xref
  topology is preserved exactly.
- Proposition 10.7.1 retains Jordan measurability and the exact
  `|det(A)| V(R)` volume factor. Its reduction to elementary matrices is
  unchanged.
- The theorem retains openness of `U`, compact Jordan measurability of `S`,
  injectivity and continuous differentiability of `g`, nonvanishing Jacobian,
  Riemann integrability, and the exact integral identity.
- The proof preserves the finite closed-rectangle cover with disjoint
  interiors, zero extension, inverse-derivative norm bound, Lebesgue covering
  lemma, `epsilon/M` derivative control, partition refinement, minimizing
  points, normalized FTC estimate, enclosing-rectangle bound, general linear
  factor, positive/negative decomposition, every inequality direction, the
  `epsilon -> 0` limit, Jacobian chain identity, inverse-map reverse inequality,
  and final QED topology.
- `Translation` in the geometric argument is rendered as `Translasi`, not as
  linguistic translation. Terminology is consistent with the admitted ledger:
  `persegi panjang`, `terukur Jordan`, `matriks elementer`, `determinan
  Jacobian`, `diferensiabel secara kontinu`, `terintegralkan secara Riemann`,
  `selimut terbuka`, `lema selimut Lebesgue`, and `penghalusan`.
- No English reader prose remains inside the admitted boundary. Proper names,
  mathematical identifiers, and TeX control words are not residue.

## Terminology-evidence correction and provenance

The one-time Indonesian field-usage audit was rechecked rather than trusted by
assertion. The downloaded arXiv:2008.00182 TeX is English and remains correctly
rejected. The 60-page Universitas Terbuka *Analisis I* PDF directly supports
the recorded analysis/set-theory terms, but an independent audit found that an
earlier report version had falsely attributed `sedemikian sehingga` to it; a
full extraction found zero occurrences and the report now says so.

The separate preference `hasil kali Kartesius` is now bound to Soffi
Widyanesti Priwantoro, *Dasar-dasar Matematika Diskrit dan Graf*, UAD Press,
2020, Definisi 3.D.1, printed page 30 / PDF page 39. The official-repository PDF
has 95 pages, 1,719,957 bytes, and SHA-256
`5761dce0e6d055b9bb60ee32afedcc39818071de99f168e510f34554f9583063`;
the cited page was checked by extraction and visual render. The corrected
report has 7,495 bytes and SHA-256
`8c0d8a44e1391cda486cb491053d07a564c23239483a42511c6099c0c8f8c3ee`.
No additional translation change is justified.

Every R006 reader driver retains the exact identification `OpenAI Codex
gpt-5.6-sol, Ultra` with generic user-instruction attribution. Jiří Lebl remains
the source author; the original copyright, source URLs, dual-license notice,
bibliography, acknowledgments, and human credits remain intact.

## Source corrections in localized accessibility text

- Source alternate text at line 3795 calls the gray and dashed objects
  “square,” although the surrounding description, theorem, variables
  `s_1,s_2`, and rendered figure all establish arbitrary rectangles. The
  Indonesian alternative text consistently uses `persegi panjang`.
- Source caption line 3802 contains the malformed phrase “within with a
  radius.” The localized caption states the intended distance/radius relation
  grammatically without changing the estimate.

Both are high-confidence minor source/editorial defects. They are recorded for
the one final deduplicated upstream disposition; no author was contacted.

## Build and reader gates

- Converter exited zero and ended `Done! (number of errors 0)`.
  `realanal-out.xml` parses as `pretext` with locale `id-ID`, 672 unique IDs,
  952 references, zero duplicate IDs, and zero unresolved references.
- Converter stderr contains only the known Windows Perl locale fallback. The
  `changeofvarssq` FIG/PDF/PDF_T assets exist,
  are nonempty, and retain their source geometry.
- Volume II TeX passes 4 and 5 have byte-identical 32,356-byte console logs,
  SHA-256
  `6b727b0a18d16954b7733a8e324fdc76c9b81ac0284116b75612ffc7bcf5da78`.
  The final log has zero LaTeX errors, undefined controls/references, rerun
  warnings, or missing characters. It retains 12 bounded inherited overfull
  hboxes, maximum 18.71684 pt.
- Index generation accepted 253 entries and glossary generation accepted 59;
  both rejected zero entries and emitted zero warnings.
- QA-only full-tail Volume II PDF: 235 letter-size pages, unencrypted, 2,410,207
  bytes, SHA-256
  `f58c20a0381ebf09cbad279c95cf60e01f954b7d36e7252b4da307bf9fef677c`.
  All 98 font rows are embedded and 27 have ToUnicode. Full extraction has zero
  U+FFFD and U+0133 characters; exact model provenance and generic user
  attribution each occur once.
- Physical pages 151–155 were rendered at 144 dpi and inspected at original
  detail. Pages 151–154 contain the complete localized opening, proposition,
  theorem, proof, figure, caption, and QED with no clipping, overlap, broken
  glyphs, or margin defect. The figure on page 153 is centered and readable.
  Untranslated exercises begin cleanly on page 155 and are outside the boundary.
  A public reader may therefore end after physical page 154, but must use a
  source-level cutoff rather than direct PDF-page truncation: the full-tail PDF
  intentionally retains later links and outline entries. The separately proved
  U227 release cut removes those destinations and renders the three references
  to omitted exercises as plain, explicitly out-of-scope text; see
  `qa/builds/ra-id-volume2-wip-release-u227-20260823/BUILD_RECEIPT.md`.
- The converter XML's optional `*-mbxpdft.svg` derivatives are not generated in
  this TeX/PDF checkpoint. All source figures needed by the PDF build resolve
  through their retained FIG/PDF/PDF_T or SVG assets; no HTML edition is
  claimed by this receipt.

## Principal artifact hashes

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `ch-multivar-int.tex` | 148,272 | `a464e6a0adabb4f4b99b87cb2cc1f7aae0565d511b27c57f595dc5c0e6c7375a` |
| `TERMINOLOGY.csv` | 83,675 | `f3f65667da2726a7d2a83d4563ae86688f2bfca226e2dfdc942b57cfcf2d67a9` |
| `converter.console.log` | 1,506,010 | `ebc10dbce4daff43b9332384b35547f9c587a523bf4109a859415cf7383df880` |
| `converter.stderr.log` | 393 | `57183f2646e20faf44dfd55c212cfffb98328b1d5d3de478116a3bede3a033be` |
| `realanal-out.xml` | 1,698,263 | `26f67df7ef01c08ba280b853a2f01c34d5bfd5c3d3a2dc7483ae1d1ee386dd29` |
| `realanal2.log` | 101,721 | `363e664239d36184e05bf4ce58b44ea9a382965451133e3679c08edec4211c7a` |
| `realanal2.pdf` | 2,410,207 | `f58c20a0381ebf09cbad279c95cf60e01f954b7d36e7252b4da307bf9fef677c` |
| `figures/changeofvarssq.fig` | 3,244 | `dc98ced2d6f5323e34bc9ff7ae4ba8b75f5fd5dc5cd4c5c2684f732471865c36` |
| `figures/changeofvarssq.pdf` | 6,869 | `57178a5dc2cc8dcaf62f5486bca33d8287245ff4bc9037d1b98b0d1beab9c0b2` |
| `figures/changeofvarssq.pdf_t` | 2,041 | `9529caa0d4712d51cf7c43ff4b524241f750e39350b88f08b1048d94ba141aed` |
