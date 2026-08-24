# QA R006 U266 — teorema identitas untuk fungsi analitik

Tanggal: 2026-08-24  
Status: **lulus**

## Batas dan identitas

- Sumber: `source/ra-v6.3/ch-approximate.tex` baris mentah 1556–1630
  inklusif, 75 baris / 2.910 byte UTF-8 LF, SHA-256
  `f6da25de01b123897795a68c727b3d92432c2218c9194cfab8093e1f4c6629c4`.
- Target: `translation/ra/ch-approximate.tex` baris mentah 1551–1629
  inklusif, 79 baris / 3.492 byte UTF-8 LF, SHA-256
  `78dbbb3f180df6ac29f4cdade1c8f7ac4f9a929b0ae156377bfbd4f99dc4eed9`.
- Berkas target hidup sesudah unit: 184.192 byte, SHA-256
  `56de8847cc792e6654c026fd40017f030e10efa5b1eede9b129b67935650d235`.
- Unit: `ra.v2.functions-as-limits.power-series-analytic.identity-theorem`.
- Batas berikutnya: sumber baris 1632 / target baris 1631,
  `\subsection{Exercises}`.

## QA struktur dan matematika

- Satu subbagian, satu lema, satu teorema, dua bukti, tiga lingkungan
  `equation*`, satu label, dan satu kait indeks dipertahankan.
- Urutan 14 token lingkungan persis sama dan semuanya seimbang.
- Label `thm:identityanalytic` dipertahankan persis; kait indeks dilokalkan
  menjadi `\index{teorema identitas}`.
- Ketiga blok matematika tampil identik setelah hanya teks `and`/`dan` dan
  spasi tak semantis dinormalisasi.
- Sumber/target memuat 67/68 perintah TeX, 69/78 rentang matematika sebaris,
  80/80 tanda kurung kurawal, dan 138/156 pembatas dolar. Seluruh selisih
  sebaris ditentukan oleh penyederhanaan frasa sumber yang berulang dan
  klarifikasi terdeklarasi `LEBL-ID-ADV-0227`: $p \in U$, $w=z-p$, $p=0$,
  kekonvergenan $z_n$ ke $0$, keberlakuan untuk semua $n$, serta keterbukaan
  dan ketertutupan relatif terhadap $U$.
- Audit matematika independen menurunkan ulang faktorisasi $f(z)=z^m g(z)$,
  aplikasi lema pada $f-g$, argumen translasi koordinat, dan langkah
  terbuka-tertutup. Recheck terakhir sesudah hipotesis barisan dibuat eksplisit:
  **PASS**.
- Tidak ada residu Inggris yang tampak bagi pembaca, karakter pengganti,
  mojibake, perubahan hipotesis teorema, perubahan rumus tampil, atau kerusakan
  struktur.

## Terminologi dan koreksi sumber

`LEBL-TERM-0644`–`LEBL-TERM-0646` menerima *identity theorem* → *teorema
identitas*, nama alternatif *limit point* → *titik limit* untuk konsep utama
*titik akumulasi*, dan *closed relative to* → *tertutup relatif terhadap*.

`LEBL-ID-ADV-0227` mencatat tiga langkah pembuktian yang benar tetapi implisit
dalam sumber: mengganti himpunan kesamaan awal dengan himpunan nol penuh,
mentranslasikan titik akumulasi umum ke nol dan memilih barisan nol tak nol yang
benar-benar konvergen ke nol, serta membaca keterbukaan/ketertutupan relatif
terhadap $U$. Target menyatakannya secara eksplisit tanpa mengubah teorema,
rumus tampil, atau kesimpulan. Tidak ada kontak dengan penulis.

Identifikasi edisi: **OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi
pengguna; semua kredit sumber dan manusia dipertahankan.
