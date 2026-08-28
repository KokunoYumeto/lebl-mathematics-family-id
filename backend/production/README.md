# Production backend checkpoints

## Current production checkpoint U417

`v0.4-live-2026.08.28-u417-a/` is the authoritative production checkpoint. It
binds the 417-row translation manifest, 796-row live terminology ledger,
266-event adverse ledger, and 22-entry O001 solution-gap ledger.

- 3,961 canonical records, 417 manifest segments, 449 units, 784 concepts,
  834 embedded expressions, and exactly 796 current logical terms;
- 22 O001 exercise gaps, ten source hints, twelve no-hint states, and no
  invented answers or solutions;
- 15 deterministic CSV projections;
- 27 files / 17,628,427 bytes;
- `records.jsonl` SHA-256
  `59a5537b6a96a2d6485e5d12331ae1b53a63477cee911d0125925ceed78fd88f`;
- canonical inventory SHA-256
  `fe0edd56faa1e4183c010002903a0af14f17a5ce3afe56a47b0d561300485424`.

All schemas, referential checks, all 417 live manifest bindings, 15 CSV views,
and lossless round trips pass. Independent replay `-u417-b` produced the
identical path/byte/hash inventory. Relative to U416, U417 adds one manifest
unit, one segment, one QA event, one concept, one term, one declared source
correction, and one O001 exercise unit, while removing nothing. It admits the
first Fourier-series exercise and its Weierstrass figure binding. It has not
replaced the U397 reader release.

## Preserved production checkpoint U416

`v0.4-live-2026.08.28-u416-a/` is the authoritative production checkpoint. It
binds the 416-row translation manifest, 795-row live terminology ledger,
265-event adverse ledger, and 21-entry O001 solution-gap ledger.

- 3,954 canonical records, 416 manifest segments, 447 units, 783 concepts,
  832 embedded expressions, and exactly 795 current logical terms;
- 21 O001 exercise gaps, ten source hints, eleven no-hint states, and no
  invented answers or solutions;
- 15 deterministic CSV projections;
- 27 files / 17,569,205 bytes;
- `records.jsonl` SHA-256
  `b0c459a4aca91381a5bbc0cdb4a42e3009264c4e5b32f3987fe599cf0b24f897`;
- canonical inventory SHA-256
  `c4ab72e0c178748410c3d77c5af94b987c4853b2bae86c8bd54a0534f9538bc4`.

All schemas, referential checks, all 416 live manifest bindings, 15 CSV views,
and lossless round trips pass. Independent replay `-u416-b` and two fresh
task-local admission replays produced the identical path/byte/hash inventory.
Relative to U415, U416 adds exactly one unit, one segment, and one QA event and
removes nothing. It admits the complete proof of Parseval's theorem. It has
not replaced the U397 reader release.

## Preserved production checkpoint U415

`v0.4-live-2026.08.28-u415-a/` is the authoritative production checkpoint. It
binds the 415-row translation manifest, 795-row live terminology ledger,
265-event adverse ledger, and 21-entry O001 solution-gap ledger.

- 3,951 canonical records, 415 manifest segments, 446 units, 783 concepts,
  830 embedded expressions, and exactly 795 current logical terms;
- 21 O001 exercise gaps, ten source hints, eleven no-hint states, and no
  invented answers or solutions;
- 15 deterministic CSV projections;
- 27 files / 17,546,055 bytes;
- `records.jsonl` SHA-256
  `dea4bef0c68b6bf7bb3a35c4c422a2f3ef1fb71eb5f8b1d005199cfc347b557b`;
- canonical inventory SHA-256
  `89eeec626092d0ec1ac92bebab9a977b3d2ee00c97866993903f145ebba5646c`.

All schemas, referential checks, all 415 live manifest bindings, 15 CSV views,
and lossless round trips pass. Independent replay `-u415-b` produced the
identical path/byte/hash inventory. Relative to U414, U415 adds exactly one
unit, one segment, one QA event, two concepts, and two terms and removes
nothing. It admits the Parseval opening and complete theorem statement,
including convergence in the `L^2` sense. It has not replaced the U397 reader
release.

## Preserved production checkpoint U414

`v0.4-live-2026.08.28-u414-a/` is the authoritative production checkpoint. It
binds the 414-row translation manifest, 793-row live terminology ledger,
265-event adverse ledger, and 21-entry O001 solution-gap ledger.

- 3,944 canonical records, 414 manifest segments, 445 units, 781 concepts,
  828 embedded expressions, and exactly 793 current logical terms;
- 21 O001 exercise gaps, ten source hints, eleven no-hint states, and no
  invented answers or solutions;
- 15 deterministic CSV projections;
- 27 files / 17,511,006 bytes;
- `records.jsonl` SHA-256
  `452cb24ec28b4c5f60aef8c39985027419de018844428eba605a02a3f1415694`;
- canonical inventory SHA-256
  `c3c2de27a4afba87315cb6cf9a5fb7a0f18202f06336dea0e531da00ce4e549a`.

All schemas, referential checks, all 414 live manifest bindings, 15 CSV views,
and lossless round trips pass. Independent replay `-u414-b` produced the
identical path/byte/hash inventory. Relative to U413, U414 adds exactly one
unit, segment, QA event, concept, and term and removes nothing. It admits the
locality consequence, corollary, convergence-rate remark, and
Stone--Weierstrass comparison. It has not replaced the U397 reader release.

## Preserved production checkpoint U413

`v0.4-live-2026.08.28-u413-a/` preserves the byte-verified predecessor with
3,939 records and 413 admitted units. Its 27-file tree totals 17,480,735 bytes
and has canonical inventory SHA-256
`928ed5553cb822f33ffbc55abdc9198d4ecbd710c879066712958e13d1d3063f`.

## Preserved production checkpoint U412

`v0.4-live-2026.08.28-u412-a/` preserves the byte-verified predecessor with
3,931 records and 412 admitted units. Its 27-file tree totals 17,413,205 bytes
and has canonical inventory SHA-256
`92a73394f6ad19b80c64f777f60abb500cf1976fa1eee01aac057298cd490b01`.

## Current public checkpoint U397

`v0.4-live-2026.08.26-u397-a/` is the public checkpoint represented by GitHub
release `lebl-family-id-wip.2026.08.26.u397` and Zenodo record `22105195`. It
binds 397 admitted units and 3,831 canonical records. Its 27-file backend tree
totals 16,839,490 bytes and has canonical inventory
SHA-256
`0b5720512a26fb12282971daf04d45c5db55d8678afe1a35e5cc44de0675302b`.

The release contains one canonical backend replay. All nine GitHub assets and
all nine Zenodo assets, totaling 12,439,062 bytes per provider, plus the
bounded repository overlays were anonymously read back and verified.

## Preserved public checkpoint U393

`v0.4-live-2026.08.26-u393-final-e/` remains historical evidence for GitHub
release `lebl-family-id-wip.2026.08.26.u393` and Zenodo record `22104149`.
It binds 393 admitted units and 3,806 canonical records. Its 27-file backend
tree totals 16,690,330 bytes and has canonical inventory SHA-256
`eb022c1d1388f5ef8c84574438f44d8c7ed9a3e05d070d0b2ea20395e9eb781e`.

## Preserved public checkpoint U370

`v0.4-live-2026.08.25-u370-a/` is the authoritative checkpoint for release
U370. It binds the 370-row translation manifest, 733-row live terminology
ledger, 245-event adverse ledger, and seven-entry O001 solution-gap ledger.

- 3,573 canonical records, 370 manifest segments, 381 units, 721 concepts,
  740 expressions, and exactly 733 current logical terms;
- seven O001 exercise gaps, four source hints, and no invented answers or
  solutions;
- 15 deterministic CSV projections;
- 27 files / 15,377,121 bytes;
- `records.jsonl` SHA-256
  `bc1fdf4050d123cc7df2ddba2e60463fd55b72723e2e8cba240708a3bb147d03`;
- canonical inventory SHA-256
  `f317d2add54525af1680678b181a86315340c1e06db8cf72dc9c1793f3e62e75`.

All schemas, referential checks, 15 CSV views, and lossless round trips pass.
Independent replay `-u370-b` produced the identical path/byte/hash inventory
and is intentionally omitted from the public package.

## Preserved public checkpoint U361

`v0.4-live-2026.08.24-u361-e/` is the authoritative checkpoint for release
U361. It binds the 361-row translation manifest, 722-row live terminology
ledger, 241-event adverse ledger, and seven-entry O001 solution-gap ledger.

- 3,520 canonical records, 361 manifest segments, 372 units, 710 concepts,
  722 expressions, and exactly 722 current logical terms;
- seven O001 exercise gaps, four source hints, and no invented answers or
  solutions;
- 15 deterministic CSV projections;
- 27 files / 15,051,229 bytes;
- `records.jsonl` SHA-256
  `1f9c3bfe0513cdda8aa496fce0d8d5870e73bbd3211481708f3a75bed1c0fa2d`;
- canonical inventory SHA-256
  `a8396edb38b192a955431715b0eb44abae823bfd80370f876089c1c0f4ef96af`.

All schemas, referential checks, 15 CSV views, and lossless round trips pass.
Independent replay `-u361-f` produced the identical path/byte/hash inventory
and is intentionally omitted from the public package.

## Public checkpoint U333

`v0.4-live-2026.08.24-u333-a/` is the authoritative checkpoint for release
U333. It binds the 333-row translation manifest, the 658-row terminology
ledger, and the unchanged 229-event adverse ledger.

- 2,692 canonical records and 666 expression records;
- 15 deterministic CSV projections;
- 26 files / 11,574,002 bytes;
- `records.jsonl` SHA-256
  `134204de247ad797a2e0c97799eebfdc657a21e0e2c0deedc388f5ef9093c502`;
- input manifest SHA-256
  `de03bdf56a20104420dde65bbb47778189f58a97134b6867aa32f6cbd1ba0385`;
- input terminology SHA-256
  `0a89033d92b46dd34278b9ba6cac27821266367a450e1ccf96d31fbb70254004`.

The dataset passes all three schemas, UUID referential checks, and all 15
lossless CSV round trips. An independent replay produced the same 26-file
inventory SHA-256
`d0aac7d8017ba5f6540f5fa1ab344982146ab35347d7f7337d38513948823bf1`.
That duplicate replay is intentionally omitted from the public repository and
source package.

## Preserved public checkpoint U330

`v0.4-live-2026.08.24-u330-figfix-a/` is the authoritative checkpoint for
release U330. It binds the 330-row translation manifest, the 643-row
terminology ledger, and the localized Figure 11.6 derivative assets.

- 2,683 canonical records;
- 15 deterministic CSV projections;
- 26 files / 11,495,077 bytes;
- `records.jsonl` SHA-256
  `a072ad3b76864de53bd1a5802dd9aaee5f9067f2e63b192eafdc308bc9fff9bf`;
- input manifest SHA-256
  `c45f42524e598f724e5845c1a7e3c38b9c43de241dcae63b48870b2683d1b34b`;
- input terminology SHA-256
  `9192208da259eb7f0b7ab8dd9ceb7569ed0af8f1d90c27a349fd0e84c36ac463`.

The dataset passes schema and referential validation. Every CSV projection
round-trips to the exact canonical record set. An independent replay produced
the identical 26-file inventory SHA-256
`8c60d50e03a80441dcc5e73ba398ab37f1b258048cb34368d44d474296ac68df`;
that duplicate replay is intentionally omitted from the public repository and
source package.

## Preserved public checkpoint U319

`v0.4-live-2026.08.23-u319-tqa-a/` is the preserved checkpoint for release
U319. It binds the 319-row translation manifest and the 626-row
terminology ledger used after the field-terminology revalidation.

- 2,650 canonical records;
- 15 deterministic CSV projections;
- 26 files / 11,227,185 bytes;
- `records.jsonl` SHA-256
  `062f7e040cc79ac7b8c428bfd2b7149a831262402a69d46800242ae1efc01c29`;
- input manifest SHA-256
  `0718642d139d80c505605d6cd47d5f836ba15dd0bde7a7f02e344922fee4d703`;
- input terminology SHA-256
  `2e844ec82fa781b2fb3eb67deed21e55ab8c2dc25fcb2e609d46603f3a32e6aa`.

Its validation and replay evidence remain intact as release history.

## Baseline and builders

`v0.3/` is the retained hash-bound baseline: 167 units and 2,193 records.
`build_live_v04.py` extends that baseline with live manifest, terminology,
correction, and QA inputs. `build_production_v03.py` is retained as an
implementation reference for the earlier snapshot.

Do not treat an older checkpoint as current coverage and do not change only a
version constant. Any schema, envelope, or CSV-dialect change requires a new
version, a fresh independent replay, and complete validation/round-trip proof.
