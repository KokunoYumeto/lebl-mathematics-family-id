# Keluarga Matematika Lebl — cuplikan kerja U310 — 2026-08-23

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi Bahasa Indonesia R006
  Jilid I yang lengkap, 334 halaman.
- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.2.1_Kekontinuan.pdf`:
  cuplikan kerja R006 Jilid II, 176 halaman. Berkas berakhir tepat setelah
  Subbagian 11.2.1, `Kekontinuan`; `Integration` dan seluruh ekor berikutnya
  tidak dimuat.
- `lebl-mathematics-family-id-source-backend-wip-u310-20260823.zip`: sumber
  LaTeX, manifes terjemahan, terminologi, ledger koreksi, bukti otoritas dan
  QA, overlay pembaca U310, serta backend modular netral-lokal.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku sengaja
dikecualikan. Pembaca Jilid II dibuat melalui cutoff sumber, bukan pemotongan
halaman PDF; daftar isi, bibliografi, indeks, dan daftar notasi tetap dibangun
secara normal.

## Cakupan terjemahan

Manifes hidup memuat 310 unit yang diterima:

- R006: 251 unit; Jilid I lengkap dan Jilid II sampai akhir Subbagian 11.2.1;
- R007: 12 unit; bab pendahuluan lengkap, berikutnya persamaan diferensial orde
  satu;
- R008: 47 unit; sampai pemetaan eksponensial atas garis dan pita, berikutnya
  bola Riemann.

Manifes adalah 437.400 byte dengan SHA-256
`00f16705241a2ff94a80c5971cbefd7ade17fbc5529e46f71738436bd09a88ec`.
Tidak ada ID unit duplikat, dan semua hash komponen berbentuk SHA-256 lowercase
yang valid.

## Backend modular v0.4

Checkpoint produksi U310 memuat 2.623 rekaman netral-lokal dan lima belas
proyeksi CSV. Dua build independen masing-masing menghasilkan 26 berkas,
11.027.539 byte, dan tidak mempunyai satu pun perbedaan path, ukuran, atau
hash. Hash aliran rekaman kanonik adalah
`027a1a2007a10343cbcef904387450dacb40d4f3ddbedd7c5327c50b507b265d`.
Validasi skema JSON, integritas referensial, dialek CSV, dan putar-balik tepat
2.623 rekaman semuanya lulus.

## QA istilah, matematika, dan layout

Pemeriksaan istilah satu kali mencari sumber Indonesia pada bidang yang sama.
Paket TeX arXiv kandidat diperiksa tetapi ternyata berbahasa Inggris dan tidak
dipakai sebagai bukti. Dua sumber akademik Indonesia diperiksa sebagai
fallback; hanya `hasil kali Kartesius` dan `terhitung tak hingga` yang perlu
disempurnakan dan dipropagasikan.

Build penuh dengan ekor sumber membuktikan 672 ID unik dan 952 referensi tanpa
target yang hilang. Build pembaca cutoff lulus converter tanpa error. Tiga
referensi ke materi yang sengaja berada setelah cutoff mempertahankan nomor
sumbernya tanpa menyertakan atau memalsukan target. Lima pass TeX menghasilkan
PDF 176 halaman tanpa error, undefined control sequence, unresolved-reference
warning, missing character, atau U+FFFD. Halaman pembuka, seluruh batas baru,
gambar, dan back matter dirender dan diperiksa: blok teks terpusat dan memenuhi
halaman, rumus terbaca, dan tidak ada clipping atau overlap.

## Otoritas, provenance, dan lisensi

Sumber matematika adalah Jiří Lebl, *Basic Analysis: Introduction to Real
Analysis*, rilis `v6.3`, commit
`00f5a8635cfba0d908cd95da53068572f30687b1`, tree
`6e7d5c2c3116ff305ff27a5ac2923f26836b6bb7`.

Edisi turunan ini memilih jalur **CC BY-SA 4.0** dari lisensi ganda sumber.
Jiří Lebl dikreditkan sebagai penulis. Penerjemahan, penyuntingan, QA istilah,
metadata aksesibilitas, dan integrasi backend dilakukan oleh **OpenAI Codex
gpt-5.6-sol, Ultra** atas instruksi pengguna. Ini bukan edisi resmi dan tidak
menyiratkan dukungan penulis atau institusi mana pun.

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U310 adalah
`10.5281/zenodo.22071911`. Repositori publik berada di
<https://github.com/KokunoYumeto/lebl-mathematics-family-id> dan rilis GitHub
U310 mencerminkan payload substantif yang sama.
