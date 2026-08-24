# Reproduksi cuplikan kerja U319

Paket ini mempertahankan pekerjaan publik pada 24 Agustus 2026.

## Batas isi

- `translation/ra/`: R006 Jilid I lengkap; Jilid II diterima berurutan sampai
  seluruh latihan yang menutup Bagian 11.2, `Pertukaran limit`.
- `translation/diffyqs/`: R007 sampai rumus integral tentu untuk kondisi awal
  pada raw line 87 `ch-first-order-ode.tex`.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann pada
  raw line 1644 sumber `ca.tex`.
- `translation/TRANSLATION_MANIFEST.jsonl`: 319 unit (R006 254, R007 15,
  R008 50), 452.035 byte, SHA-256
  `0718642d139d80c505605d6cd47d5f836ba15dd0bde7a7f02e344922fee4d703`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

## Membangun pembaca Jilid II

1. Salin pohon `translation/ra/` ke direktori build baru.
2. Ganti `realanal2.tex` dan `ch-approximate.tex` pada salinan dengan berkas
   dari `release/u319/`. Jangan menimpa pohon terjemahan hidup.
3. Jalankan converter sumber proyek dan wajibkan pesan akhir nol error.
4. Jalankan `makeindex` untuk indeks dan glosarium, kemudian lima pass
   `pdflatex` sampai log dan referensi stabil.
5. Verifikasi hasil terhadap
   `qa/R006_VOLUME2_SWAPPING_LIMITS_SECTION_READER_U254_BUILD_RECEIPT.md`.

Cutoff berakhir pada target raw line 1030 dari `ch-approximate.tex`, tepat pada
penutup latihan kesepuluh Bagian 11.2. Overlay `ch-approximate.tex` adalah
35.780 byte, SHA-256
`63edb3e4c91c3f015f84d641fbf67947f0434b870930d42c4700ce67d4c4b7a4`.
Ia dibuat oleh `backend/tools/make_partial_tex.py`, bukan dengan memangkas PDF.
Nomor untuk dua referensi yang targetnya berada setelah cutoff dibekukan dari
build penuh v6.3; target tidak dibuat seolah-olah hadir atau dapat diklik.

PDF acuan U319 adalah 180 halaman, 1.909.146 byte, SHA-256
`303ec82e16d133e938247f6611e31e36cb435ff0285a7b33fbbf4f8a5eb91725`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.23-u319-tqa-a/`. Ia memuat 2.650
rekaman, lima belas proyeksi CSV, 26 berkas, dan 11.227.185 byte. Hash
`records.jsonl` adalah
`062f7e040cc79ac7b8c428bfd2b7149a831262402a69d46800242ae1efc01c29`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik dari snapshot v0.3 ditambah manifes, terminologi, koreksi, dan QA
hidup. Validasi harus menegakkan:

- dataset dan seluruh rekaman lulus JSON Schema;
- ID rekaman unik dan relasi referensial utuh;
- lima belas CSV memakai dialek LF + quote-all yang ditetapkan;
- `record_json` dari CSV mengembalikan tepat 2.650 rekaman kanonik;
- build ulang mempunyai inventaris path, ukuran, dan SHA-256 identik.

Receipt ada di `qa/BACKEND_V0_4_LIVE_U319_TQA_20260823.md`. Replay B telah
dibuktikan identik tetapi tidak disertakan dalam paket publik.

## Istilah, hak, dan pengecualian

`control/` memuat terminologi, komponen hak, dan kandidat koreksi sumber.
`authority/terminology_evidence/` memuat laporan audit istilah lapangan.
Kandidat TeX arXiv terbukti berbahasa Inggris; fallback akademik Indonesia dan
keputusan istilah dicatat secara eksplisit.

Lisensi turunan adalah CC BY-SA 4.0. Lihat `LICENSE.md`,
`translation/ra/LICENSE.md`, dan `authority/R006_AUTHORITY.md`. Foto sampul
ritel `cover*.png`, `cover*.xcf`, dan thumbnail terkait tidak disertakan karena
haknya tidak termasuk dalam lisensi buku. Paket juga mengecualikan cache,
render sementara, build penuh dengan ekor belum diterjemahkan, raw provenance
dumps, backend replay B, dan arsip otoritas mentah.

Penerjemahan, penataan, QA istilah, dan backend dilakukan oleh **OpenAI Codex gpt-5.6-sol, Ultra**
atas instruksi pengguna, dengan seluruh kredit sumber dan kontributor manusia
dipertahankan.
