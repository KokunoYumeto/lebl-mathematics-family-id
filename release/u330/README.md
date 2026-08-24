# Overlay pembaca R006 Jilid II — U330 / batas R006-U265

Overlay ini membangun pembaca Bahasa Indonesia *Analisis Dasar II* sampai
akhir Subbagian 11.3.4, `Fungsi analitik`.

## Batas

- Komponen hidup: `translation/ra/ch-approximate.tex`, 183.610 byte, SHA-256
  `aa51a8032b1babc9a530e0b68ebdaa1087932d66bf60162f42b775576a5fdedb`.
- Cutoff overlay: target raw line 1549 inclusive, 54.933 byte, SHA-256
  `f466efb755040b41da42989f3ff9a95321f528769ba8fcb540e2c8094ae77073`.
- Unit terakhir: `R006-U265`, catatan penutup Subbagian 11.3.4.
- Unit berikutnya dimulai pada source raw line 1556 / target raw line 1551,
  `Identity theorem`; materi itu tidak ada dalam pembaca.

## Aset gambar yang dilokalkan

Overlay menyertakan tiga aset Figure 11.6 di `figures/`:

- `radiusconvcomplex.pdf_t`, 1.176 byte, SHA-256
  `7ee6864434d06a45723b8e9e496a26882f6e0cbb6916e6356f2d2bad61eb7f37`;
- `radiusconvcomplex.fig`, 1.983 byte, SHA-256
  `3fe8c73357a4aef584b0f0e4d735885abc7c6f669a290712b8eee8c8ee815937`;
- `radiusconvcomplex.pdf`, 2.712 byte, SHA-256
  `a356422abacb1290218f5b47f9d989b0abad314b4065d9bbfb6c43c3adaf2fd3`.

Label gambar kini berbunyi `deret konvergen` dan `deret tidak konvergen`.

## Cara memakai

Salin seluruh pohon `translation/ra/` ke direktori build baru. Ganti
`realanal2.tex` dan `ch-approximate.tex` pada salinan dengan kedua berkas di
direktori overlay ini, lalu salin ketiga aset di `figures/` ke subdirektori
`figures/` build. Jangan menerapkan cutoff ke pohon terjemahan hidup.
Jalankan converter, generator indeks/glosarium, lalu lima pass `pdflatex`.

Driver membekukan nomor hanya untuk dua target yang sengaja berada setelah
cutoff, Bagian 11.6 dan 11.7. Nomornya dibuktikan oleh build penuh sumber v6.3;
target tidak disertakan dan tidak dibuat seolah-olah dapat diklik.

Hasil terverifikasi: 188 halaman, 1.991.475 byte, SHA-256
`28c0844666712d94bed82789e014faf8dbbba32c2384b77cd745423c4f845aa1`.
Receipt lengkap berada di
`qa/R006_VOLUME2_POWER_SERIES_ANALYTIC_READER_U330_BUILD_RECEIPT.md`.

Penerjemahan, penataan, QA istilah, dan integrasi backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna. Semua kredit
sumber dan kontributor manusia tetap dipertahankan. Lisensi turunan:
CC BY-SA 4.0.
