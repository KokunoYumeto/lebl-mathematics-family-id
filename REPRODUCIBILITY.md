# Reproduksi cuplikan kerja U357

Paket ini mempertahankan pekerjaan publik pada 24 Agustus 2026. Statusnya
parsial sampai seluruh korpus tiga buku selesai.

Identitas checkpoint: tag GitHub `lebl-family-id-wip.2026.08.24.u357`, DOI
versi Zenodo `10.5281/zenodo.22086636`, dan concept DOI
`10.5281/zenodo.22059779`.

## Batas isi

- `translation/ra/`: R006 Jilid I lengkap; Jilid II hidup sampai lema modulus
  minimum pertama. Pembaca publik R006 yang dipertahankan tetap berhenti di
  akhir Bagian 11.4 dan seluruh sebelas latihan.
- `translation/diffyqs/`: R007 kontigu sampai rumus integral tentu untuk kondisi
  awal pada raw line 87 `ch-first-order-ode.tex`, ditambah Bab 8
  `ch-nonlin-systems.tex` yang lengkap dan terverifikasi.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann pada
  raw line 1644 sumber `ca.tex`.
- `translation/TRANSLATION_MANIFEST.jsonl`: 357 unit (R006 272, R007 35,
  R008 50), 520.108 byte, SHA-256
  `783aff8d2d58a6ae8d152816cd7d8799c95c0eda27c04c61b719b5b4d56d47ba`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

## Membangun pembaca R007 Bab 8

Overlay reproduksi ada di `release/u357/`.

1. Ambil sumber `jirilebl/diffyqs` tag v6.11, commit
   `066f96506d0954cc3efb900db0d68d121733b2dc`, ke direktori build baru.
2. Ganti hanya `ch-nonlin-systems.tex` dan salin
   `figures/nlin-pend.pdf_t` dari overlay U357.
3. Muat `id-localization.tex` tepat sebelum input Bab 8. Ini melokalkan label
   pembaca tanpa mengubah source mathematics, counter, label, atau rujukan.
4. Jalankan `pdflatex`, `makeindex`, lalu `pdflatex` sampai log stabil tanpa
   error, referensi tak terdefinisi, atau permintaan rerun.
5. Ekstrak halaman fisik 351--389 dari proof 472 halaman. Bangun sampul dari
   `nonlinear-systems-reader-cover-id.tex`, lalu gabungkan sampul sebagai
   halaman pertama.
6. Hasil acuan harus 40 halaman, 1.524.418 byte, SHA-256
   `8d392ef36104027fd680d1bfd73a153ea3e69ead1d4c6867143ab9d2f8f6c3ad`.

Proof penuh campuran hanya bukti QA karena bab lain belum seluruhnya
diterjemahkan. Jangan menerbitkannya sebagai pembaca Indonesia.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.24-u357-a/`. Ia memuat 3.326 rekaman,
357 unit, 714 ekspresi, lima belas proyeksi CSV, 26 berkas, dan 13.493.718
byte. Hash inventaris kanoniknya adalah
`cf2c08405a3c7926d2f5b1e54d1d7b94733636156256a609b84648791f27976e`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik dari snapshot v0.3 ditambah manifes, terminologi, dan ledger
koreksi hidup. Validasi harus menegakkan:

- dataset dan seluruh rekaman lulus JSON Schema;
- ID rekaman unik dan relasi referensial utuh;
- lima belas CSV mengikuti spesifikasi serialisasi;
- `record_json` dari CSV mengembalikan tepat 3.326 rekaman kanonik;
- `terms.csv` memuat 734 rekaman fisik, 22 superseder, dan tepat 712 istilah
  logis kini setelah ID yang disupersesi dikeluarkan;
- build ulang mempunyai inventaris path, ukuran, dan SHA-256 identik.

Receipt ada di `qa/BACKEND_V0_4_LIVE_U357_20260824.md`. Replay B telah
dibuktikan identik tetapi tidak disertakan untuk menghindari duplikasi byte.

## Istilah, hak, dan pengecualian

`control/TERMINOLOGY.csv` memuat 712 baris admitted dan SHA-256
`9e942a8c48c208c1b08688e711056fb06470d9ccd59082e0072c2e812fcf2a8e`.
`supersedes_id` mempertahankan sejarah tanpa membuat tampilan istilah kini
ambigu. Hak ketiga karya tetap terpisah; lisensi turunan yang dipilih adalah
CC BY-SA 4.0.

Paket mengecualikan cache, render sementara, proof campuran, replay backend B,
raw provenance dumps, arsip otoritas mentah, dan gambar sampul ritel yang
haknya tidak termasuk dalam lisensi buku.

Penerjemahan, penataan, QA istilah, dan backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna, dengan seluruh
kredit sumber dan kontributor manusia dipertahankan.
