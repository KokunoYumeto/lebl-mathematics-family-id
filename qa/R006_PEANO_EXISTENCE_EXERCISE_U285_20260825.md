# R006 U285 — latihan eksistensi Peano

Status: **PASS; diterima sebagai unit terjemahan kontigu**  
Tanggal: 2026-08-25  
Provenance runtime: `OpenAI Codex gpt-5.6-sol, Ultra`

## Batas dan identitas

- ID stabil:
  `ra.v2.equicontinuity-arzela-ascoli.exercises.peano-existence`.
- Sumber beku: `source/ra-v6.3/ch-approximate.tex`, raw lines 3066–3132
  inclusive; 67 LF lines; 2.438 byte; SHA-256
  `89bed4245e493fef36b6874e03a0a61cb5f10c58e31789e76eb71addc4696fb0`.
- Sasaran: `translation/ra/ch-approximate.tex`, raw lines 3078–3144
  inclusive; 67 LF lines; 2.638 byte; SHA-256
  `17429965c3b6f969cd2b915c2d9568f9dd46a5184fecfcc3780f460d2cf0b66b`.
- Unit ini menutup Bagian 11.6 secara lengkap. Batas berikutnya ialah source
  raw line 3137 / target raw line 3149, pembukaan Bagian 11.7, teorema
  Stone--Weierstrass.

## Cakupan dan istilah

Unit mempertahankan pernyataan teorema eksistensi Peano dan keempat tahap
latihannya: konstruksi poligonal metode Euler, ekuikontinuitas dan keterbatasan
seragam, pemilihan subbarisan Arzelà--Ascoli, lintasan ke limit integral beserta
teorema dasar kalkulus, dan perluasan solusi ke sebelah kiri titik awal.

`LEBL-TERM-0733` mengikat *Euler's method* ke `metode Euler` untuk R006 dan
R007. Istilah itu mengikuti penggunaan bidang Indonesia, termasuk kurikulum
persamaan diferensial numerik MA3232 Institut Teknologi Bandung. Istilah
`teorema eksistensi Peano` telah terikat sebelumnya oleh `LEBL-TERM-0316`.

## QA independen

- Struktur: PASS. Aliran 108 kontrol TeX aktif identik. Aliran lingkungan
  identik: 12 peristiwa / enam pasangan seimbang (`exercise` satu,
  `equation*` tiga, `enumerate` satu, dan `split` satu), dengan empat butir
  enumerasi dan penyarangan terjaga.
- Tiga puluh payload matematika inline identik byte demi byte dan berurutan.
  Ketiga display mempertahankan struktur dan formula; dua perbedaan tunggal
  ialah lokalisasi `\text{and}` menjadi `\text{dan}` dan
  `\text{converges to}` menjadi `\text{konvergen menuju}`.
- Label `exercise:peanoexistence`, payload indeks, tanda kurung kurawal aktif,
  dan delimiter matematika terjaga. Tidak ada komentar atau perubahan struktur
  yang tak dideklarasikan.
- Audit matematis: PASS. Seluruh hipotesis interval, titik awal, domain solusi,
  persamaan diferensial, rekursi $f_n$/$s_n$, konstanta Lipschitz bersama,
  subbarisan, limit integral, dua petunjuk, dan perluasan kiri setara dengan
  sumber tanpa penguatan atau pelemahan.
- Bahasa Indonesia: PASS. Prosa formal alami dan lengkap; istilah konsisten
  dengan ledger; tidak ada residu prosa Inggris selain eponim dan pengenal TeX.

Tidak ada koreksi sumber baru. Ledger koreksi tetap memuat 245 peristiwa unik,
220.783 byte, SHA-256
`9559996396d2b90c34e446e9c90de9268f7433c39c810135322cd7ca0c354f3f`.
Ledger istilah sesudah U285 memuat 733 istilah unik, 106.182 byte, SHA-256
`580653f43e23e73ff95b9dea299f9e1e636c9db65b1dac4a9508d4531e5c0148`.
Sasaran hidup lengkap sesudah U285 adalah 190.655 byte, SHA-256
`8207bf35bf21bdcb65ac1947c92c51951b65e4faad5c348ac40796663bd36ac2`.
Tidak ada penulis yang dihubungi.
