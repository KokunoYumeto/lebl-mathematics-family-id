# Serialization and Projection Contract v0.1

## Canonical JSON and JSONL

Canonical JSON uses UTF-8 without BOM, Unicode NFC, lexicographically sorted
object keys, compact `,`/`:` separators, lowercase JSON literals, and decimal
integers. Fractional floating-point values are forbidden in canonical records;
use a string when exact decimal notation matters. Array order is semantic and
is preserved.

A JSONL stream contains one canonical record per line, is sorted by
`(record_type, id)`, ends every record including the last with LF (`0A`), and
contains no blank lines. Dataset manifests bind each stream by path, byte count,
record count, and SHA-256. Hashes inside records use `sha256:<64 lowercase hex>`.

## CSV projections

CSV is a deterministic exchange/query projection, not the authority. Every file
uses UTF-8 without BOM, LF line endings, the manifest's exact header order,
RFC-4180 double-quote escaping, and quotes every field. Rows use the manifest's
sort keys. Identifiers remain text. Booleans are `true`/`false`; integers are
base-10; indexed null/absent values are empty. Arrays and objects use canonical
JSON in a field.

Each ordinary projection contains `record_json`, the exact canonical source
record. Consequently, empty versus absent indexed values remain lossless, and
the complete set of ordinary projections must reconstruct the JSONL stream
byte-for-byte after canonical sorting. `exercise_support.csv` is a derived view
and is excluded from record reconstruction.

The projection set covers every envelope entity plus a derived exercise-support
view. The latter emits one row for every exercise, even where no hint, answer,
or solution exists. `solution_status` therefore records `full_solution`,
`answer_only`, `hint_only`, `mixed_partial`, `none`, `unknown`, or
`not_applicable`; absence is not silently treated as an error. `hints`,
`answers`, and `solves` relations point from the supporting unit to the exercise.

## Round-trip and change discipline

Validation must check schema shape, UUID derivation, unique IDs/keys, reference
closure, unit-parent acyclicity, edition/resource/rights consistency, segment
source/translation provenance, exercise-support consistency, canonical byte
form, stream hashes, and projection grammar. Corrections are separate records;
they never mutate a frozen source witness invisibly.

Changing a schema or projection column requires a new semantic version and a
documented migration. Reordering keys, columns, or rows without a version change
is prohibited because it changes artifact hashes without adding meaning.
