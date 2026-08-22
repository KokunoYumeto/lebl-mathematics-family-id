# Identifier Policy v0.1

## Namespace and algorithm

The fixed Lebl-family UUID namespace is
`ccdf8f89-242c-5c81-863d-54d9fb08f872`, derived once as UUIDv5 from the URL
namespace and `urn:interlanguage:lebl-mathematics-family`.

Every top-level record has both:

- `semantic_key`: an immutable, readable key beginning with `lebl.ra.`,
  `lebl.diffyqs.`, `lebl.ca.`, or `lebl.shared.`; and
- `id`: `urn:uuid:` plus UUIDv5(namespace,
  `record_type + ":" + semantic_key`).

Nested segment expressions use UUIDv5(namespace,
`"expression:" + expression_key`). Dataset IDs use UUIDv5(namespace,
`"dataset:" + dataset_key`). The validator recomputes these values.

The key is assigned once and then persisted. It must not contain a translated
title or rendered page number. Prefer a stable upstream identifier where one
exists; otherwise assign a durable registry token before translation. A later
source rename, renumbering, or title correction updates locators and aliases,
not identity. A genuine semantic split receives new IDs plus explicit
`supersedes`/`contains`/`corrects` relations.

`source_local_id`, labels, paths, titles, and page references are locators or
aliases only. They never replace the stable ID. Locale is carried by segment
expressions, terms, editions, and per-locale unit states; it is never baked into
the semantic unit or segment identity.

## Structural keys

Suggested forms (not title slugs):

```text
lebl.ra.resource.primary
lebl.ra.edition.upstream.<frozen-revision-token>
lebl.ra.unit.<durable-source-token>
lebl.ra.segment.<durable-source-token>.<ordinal>
lebl.shared.concept.<curated-token>
```

Cross-book concepts use `lebl.shared` only after an editor has established
semantic equivalence. Similar wording alone is insufficient. R006/R007/R008
rights, edition authority, and source topology remain separate.
