# Backend Modular Lebl — envelope v0.1, checkpoint produksi v0.4 U310

Status: implementasi untuk lane Lebl; belum menjadi backend kanonik
lintas-korpus. Envelope/skema arsitektur tetap memakai versi v0.1. Checkpoint
produksi hidup yang diterbitkan berada di
`production/v0.4-live-2026.08.23-u310-a/` dan memuat semua 310 unit manifes
R006/R007/R008 yang diterima pada batas ini.

This directory implements the shared interoperability envelope for only the
R006/R007/R008 Lebl family. It keeps `ra`, `diffyqs`, and `ca` as distinct
resources and editions while allowing justified shared concepts and terms.
Reader-facing translation remains in the translation tree; this backend indexes
it without silently rewriting source mathematics.

## Bagian normatif

- `schemas/record.schema.json`: rekaman entitas dan kendala per jenis;
- `schemas/dataset.schema.json`: manifes dataset JSONL yang terikat hash;
- `schemas/projection-manifest.schema.json`: tata bahasa proyeksi deterministik;
- `projection_manifest.json`: daftar view CSV yang dapat ditanyakan;
- `specs/IDENTIFIERS.md`: kebijakan identitas persisten dan netral-lokal;
- `specs/SERIALIZATION_AND_PROJECTIONS.md`: kontrak byte JSONL/CSV;
- `tools/backend_tool.py`: validasi, proyeksi CSV, dan pemeriksaan putar-balik;
- `production/build_live_v04.py`: builder aditif untuk checkpoint hidup U310;
- `tools/make_partial_tex.py`: cutoff komponen TeX deterministik untuk pembaca
  parsial.

Envelope bersama dijelaskan di
`outputs/01a01ec1-e685-70d0-b022-211396334723/curriculum_logbook/05_MODULAR_BACKEND_INTEROPERABILITY_V0.md`.

## Checkpoint produksi U310

`production/v0.4-live-2026.08.23-u310-a/` adalah keluaran kanonik. Ia memuat:

- 2.623 rekaman JSONL yang lulus skema;
- 310 unit: R006 251, R007 12, R008 47;
- 15 proyeksi CSV yang pulang-pergi menjadi tepat 2.623 rekaman;
- 26 berkas dan 11.027.539 byte;
- hash aliran rekaman
  `027a1a2007a10343cbcef904387450dacb40d4f3ddbedd7c5327c50b507b265d`.

Build replay independen dibandingkan dengan keluaran kanonik dan menghasilkan
nol perbedaan path, ukuran, maupun SHA-256. Replay itu sendiri tidak disertakan
dalam paket publik untuk menghindari duplikasi byte. Bukti lengkap berada di
`qa/BACKEND_V0_4_LIVE_U310_20260823.md`; hasil mesin ada di
`production/v0.4-live-2026.08.23-u310-a/VALIDATION.json`.

## Hubungan dengan v0.3

`production/v0.3/` tetap dipertahankan sebagai basis terikat hash yang memuat
167 unit dan 2.193 rekaman. Builder v0.4 menambah manifest, istilah, koreksi,
dan QA hidup tanpa mengganti identitas lama. Paket ringkas tidak menyertakan
seluruh seed historis v0.1/v0.2, sehingga v0.3 diperlakukan sebagai snapshot
tervalidasi, bukan sebagai keluaran yang berdiri sendiri tanpa seed.

Jangan mengubah konstanta versi saja. Perubahan envelope, skema, atau dialek
proyeksi harus menaikkan versi, membangun replay independen, dan mengulangi
validasi skema, referensi, serta putar-balik CSV.
