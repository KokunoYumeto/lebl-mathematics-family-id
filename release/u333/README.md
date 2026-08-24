# Overlay pembaca R006 Jilid II — U333 / batas R006-U268

Overlay ini membangun pembaca Bahasa Indonesia *Analisis Dasar II* sampai
akhir Subbagian 11.4.1, `Eksponensial kompleks`.

## Batas

- Komponen hidup: `translation/ra/ch-approximate.tex`, 184.745 byte, SHA-256
  `ea35f4bbbc3bb4a00b780339e59b45b57eca2a539da93ccc386f010c5c99cbfa`.
- Prefiks target yang diterima: raw line 1–1862 inclusive, 66.475 byte,
  SHA-256
  `c44b27e4a29305d492c66e2c22a21a45346b40a070c197a3f113a6c71149439f`.
- Cutoff overlay menambahkan satu komentar deterministik nonpembaca: 66.543
  byte, SHA-256
  `468729fb18049785586a0638872cd049ffc61762de4149013685c354cb4daaf0`.
- Unit terakhir: `R006-U268`, Subbagian Eksponensial kompleks lengkap.
- Unit berikutnya dimulai pada source dan target raw line 1863,
  `Trigonometric functions and pi`; materi itu tidak ada dalam pembaca.

## Aset gambar yang dibekukan

Overlay mempertahankan tiga aset Figure 11.6 yang telah dilokalkan di
`figures/`:

- `radiusconvcomplex.pdf_t`, 1.176 byte, SHA-256
  `7ee6864434d06a45723b8e9e496a26882f6e0cbb6916e6356f2d2bad61eb7f37`;
- `radiusconvcomplex.fig`, 1.983 byte, SHA-256
  `3fe8c73357a4aef584b0f0e4d735885abc7c6f669a290712b8eee8c8ee815937`;
- `radiusconvcomplex.pdf`, 2.712 byte, SHA-256
  `a356422abacb1290218f5b47f9d989b0abad314b4065d9bbfb6c43c3adaf2fd3`.

Figure 11.7 memakai aset sumber bebas yang sudah ada di
`translation/ra/figures/`; alternatif teks Indonesia dan keterangan lengkap
berada di cutoff `ch-approximate.tex`.

## Cara memakai

Salin seluruh pohon `translation/ra/` ke direktori build baru. Ganti
`realanal2.tex` dan `ch-approximate.tex` pada salinan dengan kedua berkas di
direktori overlay ini, lalu salin ketiga aset di `figures/` ke subdirektori
`figures/` build. Jangan menerapkan cutoff ke pohon terjemahan hidup.
Jalankan converter, generator indeks/glosarium, lalu lima pass `pdflatex`.

Driver membekukan nomor hanya untuk dua target yang sengaja berada setelah
cutoff, Bagian 11.6 dan 11.7. Nomornya dibuktikan oleh build penuh sumber v6.3;
target tidak disertakan dan tidak dibuat seolah-olah dapat diklik.

Hasil terverifikasi: 192 halaman, 2.058.059 byte, SHA-256
`6f1f38221af120d6459cdc217e789ca1f7a9d4f353f5720db00ff271ce637061`.
Receipt lengkap berada di
`qa/R006_VOLUME2_COMPLEX_EXPONENTIAL_READER_U333_BUILD_RECEIPT.md`.

Penerjemahan, penataan, QA istilah, dan integrasi backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna. Semua kredit
sumber dan kontributor manusia tetap dipertahankan. Lisensi turunan:
CC BY-SA 4.0.
