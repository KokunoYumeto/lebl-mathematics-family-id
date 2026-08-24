# Keluarga Matematika Lebl — cuplikan kerja U319 — 2026-08-24

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.2_Latihan.pdf`:
  cuplikan R006 Jilid II, 180 halaman. Berkas berakhir tepat setelah seluruh
  sepuluh latihan yang menutup Bagian 11.2, `Pertukaran limit`; Bagian 11.3
  dan ekor berikutnya tidak dimuat.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I yang
  lengkap, 334 halaman.
- `lebl-mathematics-family-id-source-backend-wip-u319-20260824.zip`: sumber
  LaTeX, manifes terjemahan, terminologi, ledger koreksi, bukti otoritas/QA,
  overlay pembaca U319, dan backend modular netral-lokal.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku sengaja
dikecualikan. Pembaca Jilid II dibuat melalui cutoff sumber, bukan pemotongan
PDF; daftar isi, bibliografi, indeks, dan daftar notasi dibangun secara normal.

## Cakupan terjemahan

Manifes memuat 319 unit yang diterima:

- R006: 254 unit; Jilid I lengkap dan Jilid II sampai seluruh Latihan Bagian
  11.2;
- R007: 15 unit; pendahuluan lengkap dan Bab 1 sampai rumus integral tentu
  untuk kondisi awal;
- R008: 50 unit; sampai akhir bagian bola Riemann.

Manifes adalah 452.035 byte dengan SHA-256
`0718642d139d80c505605d6cd47d5f836ba15dd0bde7a7f02e344922fee4d703`.
Tidak ada ID unit duplikat dan seluruh hash komponen valid.

## Backend modular v0.4

Checkpoint `v0.4-live-2026.08.23-u319-tqa-a` memuat 2.650 rekaman netral-lokal
dan lima belas proyeksi CSV. Dua build independen masing-masing menghasilkan
26 berkas, 11.227.185 byte, dan tidak mempunyai satu pun perbedaan path,
ukuran, atau hash. Hash aliran rekaman kanonik adalah
`062f7e040cc79ac7b8c428bfd2b7149a831262402a69d46800242ae1efc01c29`.
Validasi skema JSON, integritas referensial, dialek CSV, dan putar-balik tepat
2.650 rekaman semuanya lulus. Build replay tidak disertakan agar byte tidak
digandakan.

## QA istilah, matematika, dan layout

Paket TeX arXiv kandidat diperiksa tetapi berbahasa Inggris dan tidak dipakai
sebagai bukti istilah Indonesia. Sumber akademik Indonesia pada analisis real
diperiksa sebagai fallback. Bentuk pilihan konsisten `lingkungan` dan
`subbarisan` dipertahankan; variasi lapangan dicatat dalam ledger tanpa
memaksakan penggantian teks yang tidak diperlukan.

Audit visual terakhir menemukan lima residu Inggris dalam daftar jalur mata
kuliah pada pendahuluan. Semuanya dilokalkan menjadi `Bab`, `dan`, dan
`mungkin` tanpa mengubah rujukan atau isi matematika, lalu pembaca penuh
dibangun ulang. Build integrasi membuktikan 672 ID unik dan 952 referensi
internal tanpa target hilang. Build cutoff mempunyai 627 ID unik; hanya dua
target setelah batas yang sengaja dibekukan. Lima pass TeX stabil, semua 76
font tertanam, dan ekstraksi tidak memuat U+FFFD atau referensi `??`.

PDF akhir 180 halaman adalah 1.909.146 byte dengan SHA-256
`303ec82e16d133e938247f6611e31e36cb435ff0285a7b33fbbf4f8a5eb91725`.
Halaman 1-6, 167-180, dan seluruh lokasi overfull dirender dan diperiksa:
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

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U319 adalah
`10.5281/zenodo.22073827`. Repositori publik berada di
<https://github.com/KokunoYumeto/lebl-mathematics-family-id> dan rilis GitHub
U319 mencerminkan delapan aset substantif yang sama.
