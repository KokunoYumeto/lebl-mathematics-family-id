# Reproduksi cuplikan kerja U310

Paket ini mempertahankan pekerjaan publik pada 23 Agustus 2026.

## Batas isi

- `translation/ra/` adalah pohon kerja LaTeX R006. Jilid I lengkap; Jilid II
  diterima berurutan sampai akhir Subbagian 11.2.1, `Kekontinuan`.
- `translation/diffyqs/ch-intro.tex` menyelesaikan bab pendahuluan R007.
- `translation/complex-analysis/` diterima berurutan sampai pemetaan
  eksponensial atas garis dan pita pada R008.
- `translation/TRANSLATION_MANIFEST.jsonl` mengikat 310 unit: R006 251,
  R007 12, dan R008 47. Berkas berukuran 437.400 byte dan mempunyai SHA-256
  `00f16705241a2ff94a80c5971cbefd7ade17fbc5529e46f71738436bd09a88ec`.

Setiap baris manifes adalah JSON yang sah dan mengikat identitas unit, irisan
sumber/sasaran, serta hash komponennya. Tidak ada ID unit duplikat.

## Membangun pembaca Jilid II

1. Gunakan pohon `translation/ra/` sebagai sumber dasar.
2. Salin overlay dari `release/u310/` ke sebuah direktori build terpisah.
   Overlay mengganti `realanal2.tex` dan `ch-approximate.tex` dengan driver dan
   cutoff pembaca U310; jangan menimpa pohon terjemahan hidup.
3. Jalankan converter sumber proyek dan pastikan pesan akhir menyatakan nol
   error.
4. Jalankan `makeindex` untuk indeks dan glosarium, kemudian lima pass
   `pdflatex` sampai log dan referensi stabil.
5. Verifikasi hasil terhadap receipt
   `qa/R006_VOLUME2_CONTINUITY_READER_U251_BUILD_RECEIPT.md`.

Cutoff berakhir pada target raw line 719 dari `ch-approximate.tex`. Ia dibuat
oleh `backend/tools/make_partial_tex.py`, bukan dengan memangkas halaman PDF.
Tiga nomor referensi ke materi setelah cutoff dibekukan dari build penuh v6.3;
target yang tidak dimuat tidak dibuat seolah-olah hadir atau dapat diklik.

PDF acuan U310 adalah 176 halaman, 1.865.175 byte, SHA-256
`1545aba2084913afeafa6fc54bb4f21523f93dbfd229b96bcc3a90d4bc6fe262`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.23-u310-a/`. Ia memuat 2.623 rekaman,
lima belas proyeksi CSV, 26 berkas, dan 11.027.539 byte. Hash aliran
`records.jsonl` adalah
`027a1a2007a10343cbcef904387450dacb40d4f3ddbedd7c5327c50b507b265d`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik dari snapshot v0.3 ditambah manifes/ledger hidup. Validasi harus
menegakkan:

- dataset dan seluruh rekaman lulus JSON Schema;
- ID rekaman unik dan relasi referensial utuh;
- kelima belas CSV memakai dialek LF + quote-all yang ditetapkan;
- `record_json` dari CSV mengembalikan tepat 2.623 rekaman kanonik tanpa
  rekaman hilang atau tambahan;
- build ulang mempunyai inventaris path, ukuran, dan SHA-256 yang identik.

Receipt validasi ada di `qa/BACKEND_V0_4_LIVE_U310_20260823.md`.

## Istilah, hak, dan pengecualian

`control/` memuat terminologi, komponen hak, dan kandidat koreksi sumber.
`authority/terminology_evidence/` memuat laporan QA istilah lapangan. Paket
TeX arXiv kandidat diperiksa tetapi berbahasa Inggris; fallback Indonesia dan
keputusan istilah dicatat secara eksplisit.

Lisensi turunan adalah CC BY-SA 4.0. Lihat `LICENSE.md`,
`translation/ra/LICENSE.md`, dan `authority/R006_AUTHORITY.md`.
Foto sampul ritel `cover*.png`, `cover*.xcf`, dan thumbnail terkait tidak ada
dalam paket karena haknya tidak termasuk dalam lisensi buku. Backend replay,
cache, render sementara, build penuh yang memuat ekor belum diterjemahkan, dan
arsip otoritas mentah juga tidak termasuk dalam payload publik ringkas.

Penerjemahan, penataan, QA istilah, dan backend dilakukan oleh **OpenAI Codex
gpt-5.6-sol, Ultra** atas instruksi pengguna, dengan semua kredit sumber dan
kontributor manusia dipertahankan.
