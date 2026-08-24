# Overlay pembaca R006 Jilid II — U361 / batas R006-U276

Overlay ini membangun pembaca Bahasa Indonesia *Analisis Dasar II* sampai
akhir Bagian 11.5, termasuk seluruh tujuh latihan tentang prinsip maksimum,
teorema dasar aljabar, fungsi rasional, dan singularitas terisolasi.

## Batas yang dibekukan

- Sumber hidup `translation/ra/ch-approximate.tex`: 188.535 byte, SHA-256
  `004bb76d7a48fcf842073d49649303d7ab96a65c0782d374094a381eaffbf974`.
- Prefiks target yang diterima: raw line 1–2551 inclusive, 92.210 byte,
  SHA-256
  `36009a672867a5fd811217696e546e3d1daaf61a58953f4a7a4efd9c8cdcfd69`.
- Cutoff overlay menambahkan satu komentar deterministik nonpembaca: 92.306
  byte, SHA-256
  `ec1579da1191ec1d9a083fe16642fafd081b33af5aa5e797e04c36d0d006223a`.
- Unit terakhir: `R006-U276`, seluruh latihan Bagian 11.5.
- Unit berikutnya dimulai pada source raw line 2542 dan target raw line 2552,
  *Equicontinuity and the Arzela--Ascoli theorem*; materi itu tidak ada dalam
  pembaca ini.

## Cara memakai

Salin seluruh pohon `translation/ra/` ke direktori build baru. Ganti
`realanal2.tex` dan `ch-approximate.tex` pada salinan dengan kedua berkas di
direktori overlay ini. Salin pula ketiga aset `figures/radiusconvcomplex.*`
yang dilokalkan. Bangun Jilid I terlebih dahulu agar `realanal.aux` tersedia,
lalu jalankan converter, `makeindex`, `makeglossaries`, dan lima pass
`pdflatex` untuk Jilid II.

Hasil terverifikasi: 200 halaman, 2.112.324 byte, SHA-256
`3e03748a32b19a7fabc38be7dbc9f1c8bc845eb99f5896dd5d93877176ceab72`.
Seluruh 80 font tertanam. Halaman 1–2 dan 184–200 telah dirender; halaman baru
terpusat, mengisi blok halaman secara wajar, terbaca, dan tidak terpotong.
Receipt lengkap berada di
`qa/R006_MAXIMUM_PRINCIPLE_SECTION_READER_U361_20260824.md`.

Penerjemahan, penataan, QA istilah, dan integrasi backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna. Semua kredit
sumber dan kontributor manusia tetap dipertahankan. Lisensi turunan:
CC BY-SA 4.0.
