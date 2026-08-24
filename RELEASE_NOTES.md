# Keluarga Matematika Lebl — cuplikan kerja U357 — 2026-08-24

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`:
  pembaca R007 baru, 40 halaman. Berkas memuat sampul status/lisensi dan
  terjemahan lengkap Bab 8, *Sistem nonlinear*. Tidak ada bab hulu berbahasa
  Inggris yang dicampurkan.
- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.4_Latihan.pdf`:
  pembaca R006 Jilid II U336, 198 halaman, dipertahankan tanpa perubahan.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I lengkap,
  334 halaman, dipertahankan tanpa perubahan.
- `lebl-mathematics-family-id-source-backend-wip-u357-20260824.zip`: sumber
  LaTeX, manifes, terminologi, ledger koreksi, bukti otoritas/QA, overlay
  pembaca U357, dan backend modular netral-lokal.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku tetap
dikecualikan. Proof 472 halaman yang dipakai untuk QA R007 berisi bab hulu yang
belum diterjemahkan dan tidak dipublikasikan sebagai pembaca.

## Cakupan terjemahan

Manifes memuat 357 unit yang diterima:

- R006: 272 unit; Jilid I lengkap dan Jilid II lokal satu unit melewati pembaca
  U336, sampai lema modulus minimum pertama;
- R007: 35 unit; pendahuluan lengkap, Bab 1 kontigu sampai rumus integral tentu
  untuk kondisi awal, dan Bab 8 lengkap sebagai 20 unit disjoint;
- R008: 50 unit; sampai akhir bagian bola Riemann.

Manifes adalah 520.108 byte dengan SHA-256
`783aff8d2d58a6ae8d152816cd7d8799c95c0eda27c04c61b719b5b4d56d47ba`.
Tidak ada ID unit duplikat dan seluruh 40 hash irisan sumber/sasaran Bab 8
cocok. Bab 8 mempertahankan 1.591 perintah, 444 batas lingkungan, 735 payload
matematika inline, 70 payload display, 31 label, dan semua dependensi gambar
serta bibliografi.

## Backend modular v0.4

Checkpoint `v0.4-live-2026.08.24-u357-a` memuat 3.326 rekaman, 357 unit,
714 ekspresi, dan lima belas proyeksi CSV. Ia memuat 700 konsep dan 734
rekaman istilah fisik. Dua puluh dua rekaman lama dipertahankan secara historis
dan ditunjuk oleh `supersedes_id`; tampilan kini memuat tepat 712 istilah logis
yang sama dengan ledger hidup.

Dua build independen masing-masing menghasilkan 26 berkas dan 13.493.718 byte,
dengan nol perbedaan path, ukuran, atau hash. Hash inventaris kanonik adalah
`cf2c08405a3c7926d2f5b1e54d1d7b94733636156256a609b84648791f27976e`.
Validasi skema, integritas referensial UUID, lima belas CSV, dan putar-balik
tepat 3.326 rekaman semuanya lulus.

## QA matematika, istilah, dan layout

Paket helper HP-LEBL-R007-001 tidak diterima secara mekanis. Pemilik lane
memverifikasi 66/66 hash paket, sumber v6.11, 28 rekaman dependensi gambar,
dua span bibliografi, formula, label, referensi, terminologi, serta seluruh
permukaan visual. Sepuluh perbaikan kefasihan diterapkan tanpa mengubah
matematika. Konvensi R007 mencakup `kondisi awal`, `sumber/serapan`, `siklus
limit`, `chaos/kaotik`, dan `penampang Poincaré`.

Build campuran akhir mempunyai 472 halaman, nol error, nol referensi/sitasi tak
terdefinisi, dan nol permintaan rerun. Semua 39 halaman bab dirender; sampul
baru dan halaman representatif diperiksa pada resolusi asli. Pembaca akhir
40 halaman adalah 1.524.418 byte dengan SHA-256
`8d392ef36104027fd680d1bfd73a153ea3e69ead1d4c6867143ab9d2f8f6c3ad`.
Ekstraksi halaman bab tidak memuat label scaffold Inggris seperti `Chapter`,
`Example`, `Figure`, `Exercise`, atau frasa varioref Inggris. Gambar dan teks
memakai blok halaman yang terpusat dan tidak terpotong.

## Otoritas, provenance, dan lisensi

Karya sumber matematika, masing-masing oleh Jiří Lebl, tetap mempunyai
identitas dan jalur hak terpisah: R006 *Basic Analysis* v6.3, R007 *Notes on
Diffy Qs* v6.11, dan R008 *Guide to Cultivating Complex Analysis* v1.9.
Edisi turunan memilih jalur **CC BY-SA 4.0** secara terpisah untuk ketiga
sumber. Ini bukan edisi resmi dan tidak menyiratkan dukungan penulis atau
institusi mana pun.

Penerjemahan, penyuntingan, QA istilah, metadata aksesibilitas, dan integrasi
backend dilakukan oleh **OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi
pengguna. Seluruh kredit sumber dan kontributor manusia dipertahankan. Tidak
ada penulis yang dihubungi dan tidak ada isu upstream yang dibuka.

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U357 adalah
`10.5281/zenodo.22086636`. Tag GitHub adalah
`lebl-family-id-wip.2026.08.24.u357`.
