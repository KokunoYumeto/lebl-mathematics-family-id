# Keluarga Matematika Lebl - cuplikan kerja U228 / kelanjutan main U230 - 2026-08-23

## Kelanjutan pohon `main` setelah U228

Setelah rilis publik U228, pohon `main` meneruskan terjemahan R006 secara
kontigu ke dua unit Chapter 11 pada `ch-approximate.tex` (raw lines 5--94).
Manifes kini memuat 230 unit (227 unit isi dan tiga driver); audit slice yang
terikat hash ada di `qa/R006_COMPLEX_PLANE_U229_U230_20260823.md`. Perubahan
ini belum mengubah artefak pembaca 155 halaman yang dibekukan pada rilis U228.

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi Bahasa Indonesia R006
  Jilid I yang lengkap, 334 halaman, telah melewati build penuh dan pemeriksaan
  visual seluruh halaman.
- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_Akhir_Bagian_10.7.pdf`:
  cuplikan kerja R006 Jilid II, 155 halaman. Berkas berakhir setelah keenam
  latihan Bagian 10.7; Bab 11 dan seterusnya tidak dimuat. Semua tautan latihan
  yang berada di dalam batas tetap hidup. Tidak ada ekor berbahasa Inggris.
- `lebl-mathematics-family-id-source-backend-wip-u228-20260823.zip`: sumber LaTeX,
  manifes terjemahan, terminologi, catatan koreksi, bukti otoritas, bukti QA,
  serta backend modular netral-lokal. Foto sampul ritel yang haknya tidak
  termasuk dalam lisensi buku sengaja dikecualikan.

Pada batas ini terdapat 228 unit R006 yang diterima: 225 unit isi dan tiga unit
driver pembaca. R007 (*Notes on Diffy Qs*) dan R008 (*Guide to Cultivating
Complex Analysis*) belum diterjemahkan; paket hanya memuat bukti otoritas dan
pemetaan cakupannya untuk kelanjutan yang dapat direproduksi.

Backend produksi v0.3 adalah checkpoint beku yang telah divalidasi untuk 167
unit. Enam puluh unit R006 yang lebih baru tetap dilestarikan dalam
`translation/TRANSLATION_MANIFEST.jsonl`, `control/TERMINOLOGY.csv`, dan
`control/ADVERSE_LEDGER.jsonl`; proyeksi backend berikutnya belum diklaim
selesai.

## Otoritas dan lisensi

Sumber matematika adalah Jiří Lebl, *Basic Analysis: Introduction to Real
Analysis*, rilis `v6.3`, commit
`00f5a8635cfba0d908cd95da53068572f30687b1`, tree
`6e7d5c2c3116ff305ff27a5ac2923f26836b6bb7`.

Edisi turunan ini memilih jalur **CC BY-SA 4.0** dari lisensi ganda sumber.
Jiří Lebl dikreditkan sebagai penulis. Penerjemahan, penataan, dan integrasi
backend dilakukan oleh OpenAI Codex gpt-5.6-sol, Ultra atas instruksi pengguna.
Ini bukan edisi
resmi dan tidak menyiratkan dukungan penulis atau institusi mana pun.

## Status repositori

Zenodo menjadi salinan pelestarian yang berdiri sendiri pada concept DOI
`10.5281/zenodo.22059779`; cuplikan U228 berada pada DOI versi berikutnya dalam
rantai yang sama dan tidak membuat concept yang bersaing. Repositori
GitHub publik berada di
<https://github.com/KokunoYumeto/lebl-mathematics-family-id>; rilis GitHub U228
mencerminkan tiga artefak substantif yang sama dan menambahkan manifes,
lisensi, serta checksum khusus rilis.
