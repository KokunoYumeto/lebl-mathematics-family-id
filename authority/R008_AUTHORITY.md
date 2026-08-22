# R008 Authority Receipt — Guide to Cultivating Complex Analysis

Status: stable source bound; translation not started  
Bounded: 2026-08-20

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Repository: `https://github.com/jirilebl/ca`; sole/default branch `master`.
- Selected stable release: `v1.9`, published 2026-07-11, 304 pages.
- Lightweight tag commit: `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Tree: `7b5118614dde859638def4eace53e169dfc3643d`.
- Release: `https://github.com/jirilebl/ca/releases/tag/v1.9`.
- Commit-pinned archive: `https://codeload.github.com/jirilebl/ca/zip/a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Local archive bytes: `1114291`.
- Local archive SHA-256: `ab4f7935dbda39dcb955834af807e4107808a9d000df8dcaadf9812bd0eeb884`.
- Extracted authority: `source/ca-v1.9`.

Current `master` commit `adfaaf8b13287185c22db079f16f39183628f482`,
tree `9f341dc398ab67cc991d0dbecb76684e14e14518`, is a post-v1.9
working-source witness. Its archive SHA-256 is
`126725f705c328df2560e8f936bd4c2de551df0654a4f1b3d21662a35658accc`.

The editable PDF-reader closure is the monolithic `ca.tex`, `notations.tex`,
local bibliography/glossary/index machinery, figures, and build script. The
source contains 607 exercises and 99 explicit hints, but no answer or solution
corpus. `publish.sh` uses repeated `pdflatex`, `makeindex`, and
`makeglossaries`; compiled figures are present. There is no authored HTML or
interactive reader closure in the repository.

The source is dual CC BY-NC-SA 4.0 / CC BY-SA 4.0. The Indonesian derivative
selects CC BY-SA 4.0 with attribution, change marking, ShareAlike, no added
restrictions, prominent derivative identification, and non-endorsement. Retail
KDP cover art is separately nonfree and excluded. All 607 exercises must be
represented in the O001 solution-gap map; the 99 hints remain hints and must
not be mislabeled as solutions.
