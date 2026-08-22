# Exercise and Solution Coverage — R006/R007/R008

Date: 2026-08-20

This receipt records source coverage; it does not invent answers and does not
claim that a pedagogical companion has already been authored.

## R006 — *Basic Analysis I–II* v6.3

The active LaTeX input closure was resolved from the three release drivers.
Counts use literal active environment/macro occurrences in the resolved files.

| Reader | Active files | Exercises | Examples | Local solutions/answers/hints |
|---|---:|---:|---:|---:|
| `realanal.tex` (Volume I) | 10 | 539 | 137 | 0 |
| `realanal2.tex` (Volume II) | 7 | 276 | 57 | 0 |
| `realanal12.tex` (combined) | 15 | 815 | 194 | 0 |

The combined total is not the sum of three separate books: it is the union of
the two volumes. No `\exsol{}` call or `solution`, `answer`, or `hint`
environment occurs in the active combined closure. O001 therefore has a real
815-exercise coverage gap for this resource. Any future solution companion must
be independently authored and keyed to stable exercise units; ordinary
translation must not fabricate solutions.

## R007 — *Notes on Diffy Qs* v6.11

The exact release source contains 747 exercise environments and 251
`\exsol{}` solution entries. Coverage is therefore substantial but incomplete:
496 exercises have no corresponding source solution under this coarse count.
O001 mapping must retain the existing solutions and distinguish the unmatched
exercises rather than treating the book as wholly unsolved.

## R008 — *Guide to Cultivating Complex Analysis* v1.9

The exact release source contains 607 exercise environments and 99 explicit
`Hint:` occurrences, but no solution or answer corpus. Hints are not solutions
and must remain separately typed. O001 has a 607-exercise solution gap, with 99
hint-bearing locations available as pedagogical evidence.

## Backend rule

Exercise, hint, answer, and solution are separate entity/relationship types.
Summary counts may guide planning, but completion status can be asserted only
after every active exercise has a stable unit ID and its exact relation to any
hint/answer/solution has been enumerated.
