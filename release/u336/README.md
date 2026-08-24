# Overlay pembaca R006 Jilid II — U336 / batas R006-U271

Overlay ini membangun pembaca Bahasa Indonesia *Analisis Dasar II* sampai
akhir Bagian 11.4, `Eksponensial kompleks dan fungsi trigonometri`, termasuk
seluruh sebelas latihan.

## Batas

- Komponen hidup: `translation/ra/ch-approximate.tex`, 187.510 byte,
  SHA-256
  `7efdde57494518efc8f3ac61b868783459245939c77ec41cb66120a3aac999d6`.
- Prefiks target yang diterima: raw line 1–2271 inclusive, 81.734 byte,
  SHA-256
  `30dcec5183dbb5f092d7be4c351509a3c5dc0e8f929748d6cc8f969f19331b57`.
- Cutoff overlay menambahkan satu komentar deterministik nonpembaca: 81.802
  byte, SHA-256
  `362969b9ce085c1e454cd3c8d7eeaa6ce2ab185c3fbc98a624c21f8c06814920`.
- Unit terakhir: `R006-U271`, blok latihan Bagian 11.4 lengkap.
- Unit berikutnya dimulai pada source raw line 2262 / heading line 2263 dan
  target raw line 2272 / heading line 2273, `Maximum principle and the
  fundamental theorem of algebra`; materi itu tidak ada dalam pembaca.

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
`figures/` build. Jangan menerapkan cutoff ke pohon terjemahan hidup. Jalankan
converter, generator indeks/glosarium, lalu lima pass `pdflatex`.

Driver membekukan nomor hanya untuk dua target yang sengaja berada setelah
cutoff, Bagian 11.6 dan 11.7. Nomornya dibuktikan oleh build penuh sumber v6.3;
target tidak disertakan dan tidak dibuat seolah-olah dapat diklik.

Hasil terverifikasi: 198 halaman, 2.091.363 byte, SHA-256
`78543d4e8087e68589e8f15d0a3a969b3282247c7c9c2cdcb6f658dfa4b68e4f`.
Label latihan yang dahulu berada setelah cutoff kini disertakan dan
referensinya terselesaikan; ekstraksi memuat nol `??`. Receipt lengkap berada
di `qa/R006_COMPLEX_TRIG_SECTION_READER_U336_20260824.md`.

Penerjemahan, penataan, QA istilah, dan integrasi backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna. Semua kredit
sumber dan kontributor manusia tetap dipertahankan. Lisensi turunan:
CC BY-SA 4.0.
