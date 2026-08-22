# R007 Authority Receipt — Notes on Diffy Qs

Status: stable source bound; translation not started  
Bounded: 2026-08-20

- Work: Jiří Lebl, *Notes on Diffy Qs: Differential Equations for Engineers*.
- Repository: `https://github.com/jirilebl/diffyqs`; default branch `master`.
- Selected stable release: `v6.11`, published 2026-05-18, 466 pages.
- Lightweight tag commit: `066f96506d0954cc3efb900db0d68d121733b2dc`.
- Tree: `f577007352167bf3e86586cca2bdc6c5c223ebfa`.
- Release: `https://github.com/jirilebl/diffyqs/releases/tag/v6.11`.
- Commit-pinned archive: `https://codeload.github.com/jirilebl/diffyqs/zip/066f96506d0954cc3efb900db0d68d121733b2dc`.
- Local archive bytes: `3679820`.
- Local archive SHA-256: `19c2cbf085fdd65b9c8629fa82eb5aacf7efdd3c6d0541b10ad2dd867e5e54ce`.
- Extracted authority: `source/diffyqs-v6.11`.

Current `master` commit `658bcae9fb710f3fae2c9da4ca4524ce157453af`,
tree `4335d8c10a87caaf94d329c931cc59d3006b54e3`, is a post-v6.11
working-source witness, not the stable translation baseline. Its local archive
SHA-256 is `ea1366591281b85a31e0621b3bd8838c6725843caa15bb355ed88c7e4e39052b`.

The editable reader closure is the `diffyqs.tex` driver, nine `ch-*.tex`
modules, two `ap-*.tex` appendices, local styles, bibliography, and compiled
figures. It contains 747 exercises and 251 explicit solutions. `runpdf.sh`
uses repeated `pdflatex` and `makeindex` passes. The HTML path is a custom
LaTeX-to-near-PreTeXt conversion and depends on an unpinned local PreTeXt asset
tree; official Sage demos are external to the repository. These are recorded
as non-hermetic companion surfaces, not missing textbook prose.

The source is dual CC BY-NC-SA 4.0 / CC BY-SA 4.0. The Indonesian derivative
selects CC BY-SA 4.0 with attribution, change marking, ShareAlike, no added
restrictions, prominent derivative identification, and non-endorsement. Retail
KDP cover art is separately nonfree and excluded. Backend coverage must map the
496 exercises without an explicit source solution and distinguish official
solutions from any later O001 companion material.
