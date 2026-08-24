# Keluarga Matematika Lebl — cuplikan kerja U330 — 2026-08-24

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.3.4_Deret_Pangkat_Analitik.pdf`:
  cuplikan R006 Jilid II, 188 halaman. Berkas berakhir tepat setelah seluruh
  Subbagian 11.3.4, `Fungsi analitik`; `Identity theorem` dan ekor berikutnya
  tidak dimuat.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I yang
  lengkap, 334 halaman.
- `lebl-mathematics-family-id-source-backend-wip-u330-20260824.zip`: sumber
  LaTeX, manifes terjemahan, terminologi, ledger koreksi, bukti otoritas/QA,
  overlay pembaca U330, dan backend modular netral-lokal.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku sengaja
dikecualikan. Pembaca Jilid II dibuat melalui cutoff sumber, bukan pemotongan
PDF; daftar isi, bibliografi, indeks, dan daftar notasi dibangun secara normal.

## Cakupan terjemahan

Manifes memuat 330 unit yang diterima:

- R006: 265 unit; Jilid I lengkap dan Jilid II sampai akhir Subbagian 11.3.4;
- R007: 15 unit; pendahuluan lengkap dan Bab 1 sampai rumus integral tentu
  untuk kondisi awal;
- R008: 50 unit; sampai akhir bagian bola Riemann.

Manifes adalah 472.659 byte dengan SHA-256
`c45f42524e598f724e5845c1a7e3c38b9c43de241dcae63b48870b2683d1b34b`.
Tidak ada ID unit duplikat dan seluruh hash komponen valid.

## Backend modular v0.4

Checkpoint `v0.4-live-2026.08.24-u330-figfix-a` memuat 2.683 rekaman
netral-lokal dan lima belas proyeksi CSV. Dua build independen masing-masing
menghasilkan 26 berkas, 11.495.077 byte, dan tidak mempunyai satu pun
perbedaan path, ukuran, atau hash. Hash inventaris kanonik adalah
`8c60d50e03a80441dcc5e73ba398ab37f1b258048cb34368d44d474296ac68df`.
Validasi skema JSON, integritas referensial, dialek CSV, dan putar-balik tepat
2.683 rekaman semuanya lulus. Build replay tidak disertakan agar byte tidak
digandakan.

## QA istilah, matematika, dan layout

Paket TeX arXiv kandidat diperiksa tetapi berbahasa Inggris dan tidak dipakai
sebagai bukti istilah Indonesia. Sumber akademik Indonesia pada analisis real
diperiksa sebagai fallback. Bentuk pilihan konsisten `lingkungan` dan
`subbarisan` dipertahankan; variasi lapangan dicatat dalam ledger tanpa
memaksakan penggantian teks yang tidak diperlukan.

Audit visual terakhir melokalkan label Inggris pada Figure 11.6 menjadi
`deret konvergen` dan `deret tidak konvergen` tanpa mengubah isi matematika.
Build cutoff mempunyai 635 ID unik; hanya dua target setelah batas yang
sengaja dibekukan. Lima pass TeX stabil, semua 78 font tertanam, dan ekstraksi
tidak memuat U+FFFD, referensi `??`, atau materi `Identity theorem`.

PDF akhir 188 halaman adalah 1.991.475 byte dengan SHA-256
`28c0844666712d94bed82789e014faf8dbbba32c2384b77cd745423c4f845aa1`.
Halaman 170-188 dan seluruh lokasi overfull dirender dan diperiksa:
tidak ada clipping, overlap, glyph rusak, atau formula tidak terbaca.

## Otoritas, provenance, dan lisensi

Sumber matematika R006 adalah Jiří Lebl, *Basic Analysis: Introduction to Real
Analysis*, rilis `v6.3`, commit
`00f5a8635cfba0d908cd95da53068572f30687b1`, tree
`6e7d5c2c3116ff305ff27a5ac2923f26836b6bb7`.

Edisi turunan memilih jalur **CC BY-SA 4.0**. Jiří Lebl dikreditkan sebagai
penulis. Penerjemahan, penyuntingan, QA istilah, metadata aksesibilitas, dan
integrasi backend dilakukan oleh **OpenAI Codex gpt-5.6-sol, Ultra** atas
instruksi pengguna. Ini bukan edisi resmi dan tidak menyiratkan dukungan
penulis atau institusi mana pun.

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U330 adalah
`10.5281/zenodo.22074515`. Repositori publik berada di
<https://github.com/KokunoYumeto/lebl-mathematics-family-id> dan rilis GitHub
`lebl-family-id-wip.2026.08.24.u330` mencerminkan aset substantif yang sama.
