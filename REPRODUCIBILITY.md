# Reproduksi cuplikan kerja U361

Paket ini mempertahankan pekerjaan publik pada 25 Agustus 2026. Statusnya
parsial sampai seluruh korpus tiga buku selesai.

Identitas checkpoint: tag GitHub `lebl-family-id-wip.2026.08.25.u361`, DOI
versi Zenodo `10.5281/zenodo.22087498`, dan concept DOI
`10.5281/zenodo.22059779`.

## Batas isi

- `translation/ra/`: R006 Jilid I lengkap; Jilid II hidup sampai seluruh
  latihan Bagian 11.5. Cursor berikutnya adalah source raw line 2542 / target
  raw line 2552, *Equicontinuity and the Arzela--Ascoli theorem*.
- `translation/diffyqs/`: R007 kontigu sampai raw line 87
  `ch-first-order-ode.tex`, ditambah Bab 8 `ch-nonlin-systems.tex` lengkap.
  Cursor aktif tetap raw line 89; paket helper Bab 8 tidak mengubahnya.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann pada
  raw line 1644 sumber `ca.tex`.
- `translation/TRANSLATION_MANIFEST.jsonl`: 361 unit (R006 276, R007 35,
  R008 50), 527.420 byte, SHA-256
  `3bba4abf924cff036d02b8f7e39e5442afa1117b20d107832cc38cee1ce77ac4`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

## Membangun pembaca R006 Jilid II U361

Overlay reproduksi ada di `release/u361/`.

1. Salin pohon `translation/ra/` ke direktori build baru.
2. Ganti `realanal2.tex` dan `ch-approximate.tex` dengan berkas overlay.
3. Salin `release/u361/figures/radiusconvcomplex.*` ke subdirektori gambar.
4. Bangun Jilid I agar `realanal.aux` tersedia.
5. Jalankan converter, `makeindex`, `makeglossaries`, dan lima pass
   `pdflatex` untuk Jilid II.

Overlay membekukan prefiks target line 1–2551. Hasil acuan harus 200 halaman,
2.112.324 byte, SHA-256
`3e03748a32b19a7fabc38be7dbc9f1c8bc845eb99f5896dd5d93877176ceab72`.
Receipt: `qa/R006_MAXIMUM_PRINCIPLE_SECTION_READER_U361_20260824.md`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.24-u361-e/`. Ia memuat 3.520 rekaman,
361 segmen manifes, 722 ekspresi, 15 proyeksi CSV, 27 berkas, dan 15.051.229
byte. Hash inventaris kanonik:
`a8396edb38b192a955431715b0eb44abae823bfd80370f876089c1c0f4ef96af`.

`backend/production/build_live_v04.py`, 60.541 byte, SHA-256
`df4660f64e7707084f252a1fda61b0f9f349417fcd9e56bccf993e68a08f8290`,
membangun checkpoint secara deterministik. Validasi harus menegakkan skema,
ID unik, referensi utuh, binding ledger O001 tanpa alias jalur, 15 proyeksi
CSV, dan putar-balik tepat 3.520 rekaman. Replay `-u361-f` telah terbukti
identik tetapi dikecualikan dari paket untuk menghindari duplikasi byte.

## Istilah, koreksi, dan pengecualian

`control/TERMINOLOGY.csv` memuat 722 istilah kini dan SHA-256
`dfd2ac7e8c5b572d224238164dd7c6414d95a2f1ea703706ed655d371072c511`.
`control/ADVERSE_LEDGER.jsonl` memuat 241 peristiwa dan SHA-256
`724d21f2dce15ce3b4cd49498e1dce1ad4bb9445833d94e952b0362b531bf04f`.
`control/O001_SOLUTION_GAP_LEDGER.jsonl` memuat tujuh kekosongan latihan dan
SHA-256
`06d3cb8a5616f3f2009c36336e19a05f429e9336257f451ea33adb117166da4e`.

Paket mengecualikan cache, render sementara, proof campuran, replay backend,
raw provenance dump, arsip otoritas mentah, dan gambar sampul ritel yang
haknya tidak termasuk dalam lisensi buku.

Penerjemahan, penataan, QA istilah, dan backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna, dengan seluruh
kredit sumber dan kontributor manusia dipertahankan.
