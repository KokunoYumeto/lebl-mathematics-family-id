# Backend Modular Lebl — envelope arsitektur v0.1, checkpoint produksi v0.3

Status: implementasi eksperimental untuk lane Lebl; belum menjadi backend
kanonik lintas-korpus. Angka v0.1 menamai envelope/skema arsitektur. Direktori
`production/v0.3/` adalah checkpoint data produksi terbeku terbaru dalam rilis
U219 dan memuat 167 unit yang telah divalidasi. Manifes terjemahan hidup telah
maju ke 219 unit; selisih 52 unit itu belum diklaim sebagai checkpoint v0.4.

This directory implements the shared interoperability envelope for only the
R006/R007/R008 Lebl family. It keeps `ra`, `diffyqs`, and `ca` as distinct
resources and editions while allowing justified shared concepts and terms.
Reader-facing translation remains in the translation tree; this backend indexes
it without silently rewriting source mathematics.

## Normative pieces

- `schemas/record.schema.json`: entity records and type-specific constraints.
- `schemas/dataset.schema.json`: a hash-bound JSONL dataset manifest.
- `schemas/projection-manifest.schema.json`: deterministic projection grammar.
- `projection_manifest.json`: the required queryable CSV views.
- `specs/IDENTIFIERS.md`: persistent locale-neutral identity policy.
- `specs/SERIALIZATION_AND_PROJECTIONS.md`: byte-level JSONL/CSV contract.
- `tools/backend_tool.py`: dependency-free validation, CSV projection, and
  lossless round-trip checks.
- `fixtures/non_authoritative/`: tiny synthetic data used only to exercise the
  contract. It is not a source, edition, translation, or rights claim.

The common envelope remains at
`outputs/01a01ec1-e685-70d0-b022-211396334723/curriculum_logbook/05_MODULAR_BACKEND_INTEROPERABILITY_V0.md`.

## Validasi

`tools/backend_tool.py` dipertahankan sebagai implementasi kontrak arsitektur
v0.1. Paket publik ringkas ini tidak menyertakan fixture sintetis
non-authoritative. Jangan menjalankan alat v0.1 terhadap dataset v0.3 dan lalu
menafsirkan ketidakcocokan versi skema sebagai kegagalan data.

Checkpoint produksi yang diterbitkan berada di `production/v0.3/`. Bukti
validasinya adalah [`production/v0.3/VALIDATION.json`](production/v0.3/VALIDATION.json):
2.193 record, 167 unit manifes, validasi skema dan referensi lulus, 15 proyeksi
CSV pulang-pergi tanpa kehilangan, dan dua replay byte-identik. `dataset.json`
serta `records.jsonl` mengikat setiap stream dengan jumlah byte dan SHA-256.

Paket publik ringkas tidak menyertakan seluruh riwayat seed v0.1/v0.2. Oleh
karena itu, v0.3 harus diperlakukan sebagai snapshot tervalidasi dan terikat
hash, bukan sebagai klaim bahwa generator dapat dijalankan ulang hanya dari
berkas paket ini. `build_production_v03.py` dipertahankan sebagai referensi
implementasi dan memerlukan seed v0.2 yang berada di luar paket ringkas.

Alat/proyektor untuk checkpoint backend berikutnya harus dinaikkan versinya
bersama skema dan diuji ulang; jangan hanya mengganti konstanta versi pada alat
v0.1.
