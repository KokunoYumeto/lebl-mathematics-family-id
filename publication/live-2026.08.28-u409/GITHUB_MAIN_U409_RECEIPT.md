# GitHub `main` U409 source/backend publication receipt

Status: **PASS; public immutable bytes verified anonymously**  
Date: 2026-08-28  
Repository: `KokunoYumeto/lebl-mathematics-family-id`  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Bounded non-force transaction

- Verified starting `main` commit:
  `87b172deca6284600d28f82c5937458c61519cc0`.
- Verified starting tree:
  `77edf16cef6ddb9165dd7f4ed3f46996a8e8a11e`.
- Created source/backend commit:
  `d3421380ca7161c2bbc9de51cc20a1384f14cbc0`.
- Created tree:
  `2ba52e5aec58a29931778722000f641e2a6bdf31`.
- The source commit has the verified starting commit as its sole parent. The
  update was non-force and race-checked immediately before changing
  `refs/heads/main`; an authenticated post-update read resolved `main` to the
  new commit.
- The resulting recursive tree inventory is not truncated and contains 1,135
  regular file blobs. No release, tag, or Zenodo object was created, edited, or
  republished.

## Exact payload

The transaction changed or refreshed exactly 41 explicit paths totaling
18,966,796 bytes. They comprise:

- the reader-facing repository README;
- seven current controls/ledgers, including terminology and adverse events;
- the current production-backend README;
- the combined U321–U324 translation receipt and U409 backend receipt;
- the 409-row translation manifest and live R006 target;
- the finalized local U405 receipt carried forward;
- one complete U409-a backend tree of 27 files.

The canonical explicit-order compact UTF-8 JSON inventory with sorted object
keys plus LF is 6,447 bytes, SHA-256
`dfc8c19ffc1d79836f749f3a71824daa5ef1052f8e217cd6d686b741d70279b3`.
The payload includes the 409-unit manifest SHA-256
`ac416d4f845ce410aec13a9da3293eed1e4465129fe99cd56643284351d90fc6`,
the live R006 target SHA-256
`5cfac7475255872ad5b08b9fedbe8d8387289d60f1777d5b2f4c8ed2e65d4807`,
and U409 `records.jsonl` SHA-256
`18a8f43c5f92c5622ca127ce94e8ea80ce0e442ed209398c14c01a15ca355c2d`.

## Anonymous readback

Every one of the 41 paths was downloaded anonymously from the immutable
commit URL. All 41 payloads matched the pre-transaction in-memory snapshot by
filename, byte count, and SHA-256: 41/41 PASS,
18,966,796/18,966,796 bytes. The authenticated post-transaction main readback,
commit-parent check, and recursive-tree readback also passed.

This checkpoint advances only the live source/backend lineage from U405 to
U409 at the complete Dirichlet-kernel and approximate-delta-functions
subsection boundary. The public reader remains the verified U397 GitHub
release and Zenodo record 22105195 / DOI `10.5281/zenodo.22105195`. A bounded
follow-up commit preserves this sanitized receipt and current controls; it does
not change release or Zenodo bytes.

## Receipt/control preservation

The bounded follow-up completed at commit
`46dff7ff4a18ea8d0e4b6c43e0e38328af4880c7`, tree
`68514b675135b680e1741c8d6f0917f08db76edd`, with source commit
`d3421380ca7161c2bbc9de51cc20a1384f14cbc0` as its sole parent. It changed
exactly this receipt and five current controls: six files / 439,951 bytes.
Anonymous immutable-commit readback matched all six paths, byte counts, and
SHA-256 values. Their canonical explicit-order inventory is 826 bytes,
SHA-256
`d1faf751abe621443fc3059c0b194485890e44d2270368ed049f6afa85ef00aa`.
The public receipt snapshot in that commit is 2,773 bytes, SHA-256
`9a6b0212eb59e481c25958e6fbea89247bc880ac3bddfcfeb7d17acc9904c45e`.

An authenticated post-transaction read resolved `main` to the controls commit,
and the direct U397 release remained public with nine assets, `draft=false`,
and `prerelease=false`. This local post-transaction section records the commit
that contains its prior snapshot. It is intentionally carried with the next
substantive checkpoint rather than creating an infinite chain of
self-referential pointer-only commits. The GitHub release, tag, and Zenodo
record remain unchanged.
