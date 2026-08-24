# QA R006 U256 — pelokalan label Gambar 11.6

Tanggal: 2026-08-24  
Status: **dikoreksi; build ulang diwajibkan**

Audit visual pembaca U330 menemukan bahwa teks alternatif dan keterangan
Gambar 11.6 sudah berbahasa Indonesia, tetapi dua label yang dicetak oleh
overlay Xfig masih berbunyi `series converges` dan `series does not converge`.
Ini merupakan residu pembaca yang tidak terlihat oleh audit TeX utama.

Perubahan dibatasi pada aset turunan Bahasa Indonesia:

- `translation/ra/figures/radiusconvcomplex.pdf_t`: 1.176 byte,
  SHA-256
  `7ee6864434d06a45723b8e9e496a26882f6e0cbb6916e6356f2d2bad61eb7f37`;
- `translation/ra/figures/radiusconvcomplex.fig`: 1.983 byte,
  SHA-256
  `3fe8c73357a4aef584b0f0e4d735885abc7c6f669a290712b8eee8c8ee815937`;
- latar `translation/ra/figures/radiusconvcomplex.pdf` tetap identik dengan
  sumber: 2.712 byte, SHA-256
  `a356422abacb1290218f5b47f9d989b0abad314b4065d9bbfb6c43c3adaf2fd3`.

Label kiri kini `deret` / `konvergen`; label kanan kini `deret` / `tidak
konvergen`. Posisi, lingkaran, arsiran, titik pusat a, jari-jari rho, keterangan,
teks alternatif, nomor gambar, dan isi matematis tidak berubah. Aset sumber
Inggris tetap utuh di `source/ra-v6.3/figures/`.

PDF pra-koreksi U330 dinyatakan superseded dan tidak boleh diterbitkan. Gerbang
penutupnya adalah converter baru, build TeX konvergen baru, render baru halaman
174, dan pemeriksaan bahwa tidak ada label Inggris tersebut pada PDF akhir.

Identifikasi edisi: **OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi
pengguna; semua kredit sumber dan manusia dipertahankan.
