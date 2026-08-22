# R006 Authority Receipt — Basic Analysis I–II

Status: translation baseline bound  
Bounded: 2026-08-20  
Resource: Jiří Lebl, *Basic Analysis: Introduction to Real Analysis*, Volumes I–II

## Selected edition

- Upstream repository: `https://github.com/jirilebl/ra`
- Selected stable release: `v6.3` (Edition 6 update 3), published 2026-05-15.
- Commit: `00f5a8635cfba0d908cd95da53068572f30687b1`
- Git tree: `6e7d5c2c3116ff305ff27a5ac2923f26836b6bb7`
- Release: `https://github.com/jirilebl/ra/releases/tag/v6.3`
- Commit-pinned archive: `https://codeload.github.com/jirilebl/ra/zip/00f5a8635cfba0d908cd95da53068572f30687b1`
- Local archive: `authority/archives/ra-00f5a8635cfba0d908cd95da53068572f30687b1.zip`
- Archive bytes: `2136615`
- Archive SHA-256: `b1ff9f7ea84ca85836dd64408ab118413241c913190a41b4b9ec10c33ee6af7d`
- Immutable extracted authority: `source/ra-v6.3`
- Working derivative: `translation/ra`

The current `master` snapshot is retained only as a later-errata witness:
commit `e21ec524ca7d54f800c693b948020c188d21d01f`, tree
`9aa15308d3f0188828bb112d0a9822f0115c4368`, archive SHA-256
`bf4faff966c916a8edf6a61da7e5d5f5a54a0fa44add950127840cb9bdfd3217`.
It is post-release work in progress and is not the translation baseline.

## Reader baseline and closure

- Volume I: `realanal.tex`; official v6.3 PDF, 312 pages, 539 exercises,
  77 figures.
- Volume II: `realanal2.tex`; official v6.3 PDF, 217 pages, 276 exercises,
  55 figures. It uses the Volume-I auxiliary file, so Volume I builds first.
- Combined HTML conversion driver: `realanal12.tex`.
- Reader text: the active `ch-*.tex` and `frag-vol2-intro.tex` inputs,
  notation registry, bibliography, figures, and local style files.
- `slides/` is incomplete and `wip/` is explicitly unfinished; neither is an
  admitted textbook reader unit.
- PDF build scripts `publish.sh` and `publish2.sh` use repeated `pdflatex`,
  `makeindex`, and `makeglossaries` passes. Existing compiled figures permit an
  ordinary build; regenerating editable ePiX/Xfig figures needs extra tools.
- HTML is generated from annotated LaTeX through a custom near-PreTeXt
  conversion, not from a separate canonical PreTeXt source body.

## Rights route

The exact source is dual licensed CC BY-NC-SA 4.0 / CC BY-SA 4.0. This
derivative selects **CC BY-SA 4.0** so the Indonesian edition may be reused
commercially as well as noncommercially. It must credit Jiří Lebl, link source
and license, identify the translation and other changes prominently, preserve
ShareAlike, impose no additional restrictions, and imply no endorsement.

The retail print-cover photographs are explicitly all-rights-reserved and are
not reusable under the book license. `cover*.png` and `cover*.xcf` are excluded
from derivative publication unless separately cleared or replaced. The normal
free-reader PDFs do not require those retail covers.

## Exercise/solution boundary

The official source contains 815 textbook exercises and intentionally provides
no solutions manual. The separate 107-problem WeBWorK collection is companion
practice with sparse Volume-II coverage, not a solution corpus or a one-to-one
exercise mapping. Backend records must therefore mark all textbook exercises as
lacking an official solution and expose the gap to O001 without inventing
solutions during translation.
