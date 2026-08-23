# Overlay pembaca R006 Jilid II — U310 / batas R006-U251

Overlay ini membangun pembaca Bahasa Indonesia *Analisis Dasar II* sampai
akhir Subbagian 11.2.1, `Kekontinuan`.

## Batas

- Komponen hidup: `translation/ra/ch-approximate.tex`, 181.628 byte, SHA-256
  `f73a48bd4e06f72bb54d9fdaafc20511c7856cbaa350f7ad99465e8fb7149acb`.
- Cutoff overlay: target raw line 719 inclusive, 26.183 byte, SHA-256
  `d4a31d1396da0ed90d7f7f534ff89f542eec1b4166c04e07cacd3f3bf7b9cc7f`.
- Unit terakhir: `R006-U251`.
- Unit berikutnya dimulai pada source raw line 726,
  `\subsection{Integration}`; materi itu tidak ada dalam pembaca ini.

## Cara memakai

Salin seluruh pohon `translation/ra/` ke direktori build baru. Ganti
`realanal2.tex` dan `ch-approximate.tex` pada salinan itu dengan kedua berkas
di direktori overlay ini. Jangan menerapkan cutoff ke pohon terjemahan hidup.
Jalankan converter, generator indeks/glosarium, lalu lima pass `pdflatex`.

Driver pembaca membekukan tiga nomor referensi yang targetnya sengaja berada
setelah cutoff. Nomor 11.2.3, 11.6, dan 11.7 berasal dari build penuh sumber
v6.3; target tidak disertakan dan tidak dibuat seolah-olah dapat diklik.

Hasil terverifikasi: 176 halaman, 1.865.175 byte, SHA-256
`1545aba2084913afeafa6fc54bb4f21523f93dbfd229b96bcc3a90d4bc6fe262`.
Receipt lengkap berada di
`qa/R006_VOLUME2_CONTINUITY_READER_U251_BUILD_RECEIPT.md`.

Penerjemahan, penataan, dan integrasi backend dilakukan oleh **OpenAI Codex
gpt-5.6-sol, Ultra** atas instruksi pengguna. Semua kredit sumber dan
kontributor manusia tetap dipertahankan. Lisensi turunan: CC BY-SA 4.0.
