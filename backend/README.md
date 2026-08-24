# Backend Modular Lebl — envelope v0.1, checkpoint produksi v0.4 U319

Status: implementasi untuk keluarga R006/R007/R008 Lebl; belum menjadi backend
kanonik lintas-korpus. Envelope/skema arsitektur tetap versi v0.1. Checkpoint
hidup yang diterbitkan berada di
`production/v0.4-live-2026.08.23-u319-tqa-a/` dan memuat semua 319 unit manifes
yang diterima pada batas ini.

Backend mempertahankan `ra`, `diffyqs`, dan `ca` sebagai sumber/edisi terpisah
sambil mengizinkan konsep dan istilah bersama yang dibenarkan. Terjemahan yang
dibaca manusia tetap berada di pohon `translation/`; backend mengindeksnya
tanpa menulis ulang matematika sumber.

## Bagian normatif

- `schemas/record.schema.json`: rekaman entitas dan kendala per jenis;
- `schemas/dataset.schema.json`: manifes dataset JSONL yang terikat hash;
- `schemas/projection-manifest.schema.json`: tata bahasa proyeksi deterministik;
- `projection_manifest.json`: daftar view CSV;
- `specs/IDENTIFIERS.md`: identitas persisten dan netral-lokal;
- `specs/SERIALIZATION_AND_PROJECTIONS.md`: kontrak byte JSONL/CSV;
- `tools/backend_tool.py`: validasi, proyeksi CSV, dan putar-balik;
- `production/build_live_v04.py`: builder aditif checkpoint hidup;
- `tools/make_partial_tex.py`: cutoff TeX deterministik untuk pembaca parsial.

## Checkpoint produksi U319

`production/v0.4-live-2026.08.23-u319-tqa-a/` adalah keluaran kanonik:

- 2.650 rekaman JSONL yang lulus skema dan integritas referensial;
- 319 unit: R006 254, R007 15, R008 50;
- 638 ekspresi, 319 segmen, 432 konsep, 440 istilah, 594 relasi, dan 421
  peristiwa QA;
- 15 proyeksi CSV yang pulang-pergi menjadi tepat 2.650 rekaman;
- 26 berkas dan 11.227.185 byte;
- hash aliran rekaman
  `062f7e040cc79ac7b8c428bfd2b7149a831262402a69d46800242ae1efc01c29`.

Build replay independen menghasilkan nol perbedaan path, ukuran, atau SHA-256.
Replay B tidak disertakan dalam paket publik. Bukti lengkap berada di
`qa/BACKEND_V0_4_LIVE_U319_TQA_20260823.md`; hasil mesin berada di
`production/v0.4-live-2026.08.23-u319-tqa-a/VALIDATION.json`.

## Hubungan dengan v0.3

`production/v0.3/` dipertahankan sebagai basis terikat hash yang memuat 167
unit dan 2.193 rekaman. Builder v0.4 menambah manifes, istilah, koreksi, dan QA
hidup tanpa mengganti identitas lama. Jangan mengubah konstanta versi saja:
perubahan envelope, skema, atau dialek proyeksi harus menaikkan versi,
membangun replay independen, dan mengulangi validasi skema, referensi, serta
putar-balik CSV.
