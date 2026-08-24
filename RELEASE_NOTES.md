# Keluarga Matematika Lebl — cuplikan kerja U336 — 2026-08-24

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.4_Latihan.pdf`:
  cuplikan R006 Jilid II, 198 halaman. Berkas berakhir tepat setelah seluruh
  Bagian 11.4, `Eksponensial kompleks dan fungsi trigonometri`, termasuk
  sebelas latihan; `Prinsip maksimum dan teorema dasar aljabar` dan ekor
  berikutnya tidak dimuat.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I yang
  lengkap, 334 halaman.
- `lebl-mathematics-family-id-source-backend-wip-u336-20260824.zip`: sumber
  LaTeX, manifes terjemahan, terminologi, ledger koreksi, bukti otoritas/QA,
  overlay pembaca U336, dan backend modular netral-lokal.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku sengaja
dikecualikan. Pembaca Jilid II dibuat melalui cutoff sumber, bukan pemotongan
PDF; daftar isi, bibliografi, indeks, dan daftar notasi dibangun secara normal.

## Cakupan terjemahan

Manifes memuat 336 unit yang diterima:

- R006: 271 unit; Jilid I lengkap dan Jilid II sampai akhir Bagian 11.4;
- R007: 15 unit; pendahuluan lengkap dan Bab 1 sampai rumus integral tentu
  untuk kondisi awal;
- R008: 50 unit; sampai akhir bagian bola Riemann.

Manifes adalah 484.083 byte dengan SHA-256
`05e5e333ae2e9ee427887c96d91848d9e99b95e4c3391f77a209ede8677a002c`.
Tidak ada ID unit duplikat dan seluruh hash komponen valid. Unit baru menutup
subbagian fungsi trigonometri dan pi, subbagian lingkaran satuan dan koordinat
polar, serta seluruh sebelas latihan Bagian 11.4 tanpa mengubah identitas
struktur sumber.

## Backend modular v0.4

Checkpoint `v0.4-live-2026.08.24-u336-a` memuat 2.701 rekaman netral-lokal,
672 rekaman ekspresi, dan lima belas proyeksi CSV. Dua build independen
masing-masing menghasilkan 26 berkas, 11.659.282 byte, dan tidak mempunyai
satu pun perbedaan path, ukuran, atau hash. Hash inventaris kanonik adalah
`e39eec0b1c05b39a274ffc6fa1f23408e81c8d163a76bb4d6d8339cfb4be2321`.
Validasi tiga skema JSON, integritas referensial UUID, dialek CSV, dan
putar-balik tepat 2.701 rekaman semuanya lulus. Build replay tidak disertakan
agar byte tidak digandakan.

## QA istilah, matematika, dan layout

Pencarian arXiv terbatas tidak menemukan sumber matematika berbahasa Indonesia
dengan sumber TeX yang dapat diunduh. Sebagai fallback yang dinyatakan secara
jujur, buku analisis kompleks Indonesia karya Zetriuslita diperiksa melalui
ekstraksi dan render halaman. Audit itu menguatkan istilah hidup, termasuk
`fungsi analitik`, `lingkungan`, `deret pangkat`, `jari-jari konvergensi`,
`bagian real`, `bagian imajiner`, `fungsi trigonometri`, dan `rumus Euler`.
Materi bukti berhak cipta tidak disertakan; hanya laporan keputusan tersanitasi
yang dipublikasikan.

Build cutoff mempunyai 639 ID unik dan 909 referensi silang; hanya dua target setelah batas yang
sengaja dibekukan. Converter berakhir dengan nol error, lima pass TeX stabil,
semua 80 baris font tertanam, dan ekstraksi tidak memuat U+FFFD atau referensi
`??`. PDF tidak terenkripsi, tidak memuat JavaScript atau AcroForm, dan
mempertahankan 29 tujuan outline. PDF belum bertag dan 54 dari 80 baris objek
font—terutama font matematika lama—tidak mempunyai ToUnicode eksplisit;
keterbatasan aksesibilitas nonblocking ini dinyatakan, bukan disembunyikan.

PDF akhir 198 halaman adalah 2.091.363 byte dengan SHA-256
`78543d4e8087e68589e8f15d0a3a969b3282247c7c9c2cdcb6f658dfa4b68e4f`.
Halaman 185–193 dan seluruh lokasi overfull dirender dan diperiksa, termasuk
subbagian koordinat polar dan sebelas latihan penutup: tidak ada clipping,
overlap, glyph rusak, formula tidak terbaca, atau blok teks yang tidak
terpusat. Halaman kosong 190 dan 192 disengaja oleh pemisah bagian.

## Otoritas, provenance, dan lisensi

Karya sumber matematika, masing-masing oleh Jiří Lebl, dipertahankan sebagai
identitas dan jalur hak terpisah: R006 *Basic Analysis* v6.3 commit
`00f5a8635cfba0d908cd95da53068572f30687b1`; R007 *Notes on Diffy Qs*
v6.11 commit `066f96506d0954cc3efb900db0d68d121733b2dc`; dan R008 *Guide to
Cultivating Complex Analysis* v1.9 commit
`a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.

Edisi turunan memilih jalur **CC BY-SA 4.0** secara terpisah untuk ketiga
sumber. Jiří Lebl dikreditkan sebagai penulis. Penerjemahan, penyuntingan, QA
istilah, metadata aksesibilitas, dan integrasi backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna. Ini bukan edisi
resmi dan tidak menyiratkan dukungan penulis atau institusi mana pun.

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U336 adalah
`10.5281/zenodo.22082567`. Repositori publik berada di
<https://github.com/KokunoYumeto/lebl-mathematics-family-id> dan rilis GitHub
`lebl-family-id-wip.2026.08.24.u336` mencerminkan aset substantif yang sama.
