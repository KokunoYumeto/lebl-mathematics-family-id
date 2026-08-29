# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Repositori ini memuat edisi turunan Bahasa Indonesia untuk tiga buku terbuka
karya Jiří Lebl:

- *Basic Analysis: Introduction to Real Analysis, Volumes I–II* (R006),
- *Notes on Diffy Qs: Differential Equations for Engineers* (R007), dan
- *Guide to Cultivating Complex Analysis: Working the Complex Field* (R008).

Tujuannya adalah pembaca yang nyaman digunakan, sumber LaTeX yang dapat
dibangun ulang, serta backend modular netral-bahasa. Setiap buku tetap memiliki
identitas edisi, otoritas, dan lisensi tersendiri. Edisi turunan ini memilih
jalur CC BY-SA 4.0 yang tersedia pada masing-masing sumber.

Terjemahan, penyuntingan, QA istilah, dan integrasi backend dilakukan oleh
OpenAI Codex gpt-5.6-sol, Ultra atas instruksi pengguna. Jiří Lebl tetap
merupakan penulis karya sumber; semua kredit sumber dan kontributor manusia
dipertahankan. Edisi ini independen dan tidak menyiratkan dukungan penulis.

## Checkpoint lokal U427 dan batas publik U426

Checkpoint lokal terbaru memuat 427 unit (R006 342, R007 35, R008 50) sampai
latihan representasi integral dan peluruhan koefisien Fourier dengan laju
$1/|n|$. Dua build backend U427 identik pada 27 berkas / 18.108.960 byte,
dengan 4.011 rekaman, 854 ekspresi, 797 istilah logis, dan 32 pemetaan O001;
inventaris POSIX SHA-256-nya
`48132a45901e66eb0216d2df08b5e2ea03d3e6897a48a865dd2446238c6386a1`.
Build pembaca integrasi epoch-tetap menghasilkan 241 halaman / 2.427.815
byte, SHA-256
`3161b210f7654b1ae6abb7b9c2c8387ebdf9af2e6a4164eef9029aa0236864a2`;
halaman 231–233 lulus inspeksi visual, dan halaman 232 memuat U427 lengkap
sebelum batas Inggris U428 yang masih utuh.

Batas publik saat ini adalah U426: commit sumber
`e084868c37179d8cc08f4105103c7d93faae912b` dan overlay kontrol
`b3902ea81953493873c8c5cf7ecf4617c0e2c136`, keduanya telah dibaca kembali
byte demi byte secara anonim dan diaudit ulang secara independen. U427 siap
untuk transaksi sumber/backend terbatas berikutnya. Rilis pembaca dan DOI
Zenodo U397 tetap tidak berubah.

## Status historis pembaca publik U397 dan sumber publik U422

Ini masih *work in progress*, bukan klaim bahwa ketiga buku sudah selesai.

- R006: Jilid I lengkap (334 halaman). Jilid II memiliki pembaca 226 halaman
  yang berakhir bersih setelah Subbagian 11.8.1, *Polinom trigonometri*,
  termasuk pembukaan deret Fourier, representasi Laurent, motivasi fungsi
  eigen, periodisitas, pemulihan koefisien, kriteria bernilai real, dan
  kebebasan linear.
- R007: pendahuluan lengkap; Bab 1 berlanjut sampai solusi integral tentu untuk
  kondisi awal; Bab 8, *Sistem nonlinear*, lengkap sebagai 20 unit dan pembaca
  mandiri 40 halaman.
- R008: terjemahan berurutan mencapai akhir bagian bola Riemann.

Manifes rilis U397 memuat 397 unit unik: R006 312, R007 35, dan R008 50. Backend
v0.4-live U397 memuat 3.831 rekaman, termasuk 397 segmen manifes, 428 unit,
754 konsep, 794 ekspresi, tepat 766 istilah logis kini, seluruh 257 koreksi
sumber yang tercatat, serta 21 pemetaan kekosongan solusi O001. Lima belas
proyeksi CSV berputar balik tepat ke seluruh rekaman, dan dua build independen
identik pada path, ukuran, dan SHA-256.

Checkpoint sumber/backend publik U422 memuat 422 unit (R006 337, R007 35,
R008 50) dan
menambahkan latihan ketaksamaan segitiga norma $L^2$. Label, tampilan rumus,
11 perintah TeX berurutan, dan seluruh struktur dipertahankan tepat; sumber
tidak memerlukan koreksi. Kekosongan solusi O001 mencatat secara eksplisit
bahwa sumber tidak menyediakan petunjuk ataupun solusi, tanpa menciptakan
jawaban, bukti, atau dukungan. Backend U422 memuat 3.987 rekaman dan 844
ekspresi tertanam; dua build 27 berkas identik byte demi byte dan seluruh 15
proyeksi CSV lulus putar balik. Commit sumber U422 sudah dibaca kembali byte
demi byte secara anonim dan independen untuk seluruh 42 berkas; overlay enam
berkas yang menyimpan tanda terima dan kontrol pemulihan juga sudah dipublikasi
dan diverifikasi secara independen. PDF pembaca publik tetap U397; rilis maupun
DOI U397 tidak diubah oleh checkpoint sumber ini.

## Pembaca utama

- `output/pdf/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`
- `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.8.1_Polinom_Trigonometrik.pdf`
- `output/pdf/Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`

Pembaca Jilid II terbaru menggunakan blok halaman penuh dan terpusat, memiliki
semua font tertanam, serta lulus sembilan pass TeX, pemeriksaan referensi,
ekstraksi teks, dan inspeksi visual halaman baru.

## Publikasi

- Repositori: <https://github.com/KokunoYumeto/lebl-mathematics-family-id>
- Rilis U397: <https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.26.u397>
- DOI versi U397: <https://doi.org/10.5281/zenodo.22105195>
- Konsep Zenodo stabil: <https://doi.org/10.5281/zenodo.22059779>
- Koleksi Figshare Bahasa Indonesia: <https://doi.org/10.6084/m9.figshare.c.8668413>

Setiap checkpoint publik diberi label parsial dengan cakupan dan pengecualian
yang eksplisit. Tidak ada penulis yang dihubungi selama produksi dan tidak ada
isu upstream baru yang dibuka.

Untuk batas isi, reproduksi build, dan hash checkpoint publik, lihat
[`RELEASE_NOTES.md`](RELEASE_NOTES.md) dan
[`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

## Checkpoint sumber/backend publik U423

Unit berikutnya yang sudah selesai adalah latihan tanpa label tentang deret
sinus dengan koefisien meluruh dan persamaan diferensial paksa (sumber raw
5358–5385; target raw 5372–5399). Terjemahan Bahasa Indonesia, struktur TeX,
matematika, dan pemetaan O001 `LEBL-O001-R006-0028` (tanpa petunjuk maupun
solusi sumber) telah diaudit. Manifes lokal memiliki 423 unit (R006 338,
R007 35, R008 50). Backend v0.4-live U423 berisi 3.993 rekaman dalam dua
build 27-berkas yang identik (17.931.910 byte; inventaris POSIX SHA-256
`1436fbd7a7b6c351d8d333713d6505310e0378330dfe7a95bf99c625c8f3c91e`), dan
lima belas tampilan CSV lulus putar balik. Build pembaca lengkap lokal pada
epoch tetap 1787961600 menghasilkan 241 halaman / 2.427.666 byte dengan SHA-256
`fd0830a19e94eaed0b53106adac197bec3665daf3e7a0b408a4018ac155ea504`; halaman
230–233 terpusat dan terbaca. Checkpoint sumber/backend U423 sudah publik pada
commit `65b5a7950d1e6d89918603548b1663122f57cdf5`; seluruh 42 berkas /
19.810.210 byte dibaca kembali secara anonim dan diaudit ulang secara
independen. Overlay enam berkas untuk tanda terima dan kontrol pemulihan juga
sudah publik pada commit `d3cd90ffd11d1b9c193768b041b4ee947d318d0b` dan
diverifikasi ulang secara independen. Rilis pembaca U397 dan Zenodo DOI tetap
tidak berubah.

## Checkpoint sumber/backend publik U424

Latihan Parseval berikutnya sudah diterjemahkan lengkap sampai sumber raw
5394 / target raw 5408. Manifes lokal kini memiliki 424 unit (R006 339,
R007 35, R008 50), dan O001 mencatat latihan ini tanpa petunjuk terpisah
ataupun solusi sumber. Dua build backend U424 identik pada seluruh 27 berkas /
17.971.333 byte, dengan 3.997 rekaman dan inventaris POSIX SHA-256
`fa1c2d90fdafed7e5042e027d95d7d1cb104e7ecf3c9d74b744ca559516de63a`.
Build pembaca integrasi epoch-tetap menghasilkan 241 halaman / 2.427.693 byte,
SHA-256
`e6bb4b925793e0fc27cd3b69b01c126712ebf40d5e4e1bed64dbdd392e90fe8e`;
halaman 232 memuat Latihan 11.8.8 dalam Bahasa Indonesia dan langsung
menunjukkan batas latihan Inggris berikutnya. Checkpoint sumber/backend U424
sudah publik pada commit `51426054b71910557f3d2a9d166248d65a987258`;
seluruh 42 berkas / 19.866.836 byte dibaca kembali secara anonim dan diaudit
ulang secara independen. Overlay enam berkas kontrol pemulihannya juga sudah
publik pada commit `c7951cc776924ebad27d544e4208d749a941b5de` dan telah
diverifikasi ulang secara anonim dan independen. Rilis pembaca U397 serta DOI
Zenodo tidak berubah.

## Checkpoint sumber/backend publik U425

Latihan berikutnya tentang deret satu sisi yang dapat dijumlahkan mutlak dan
perluasan analitik ke cakram satuan sudah diterjemahkan lengkap, termasuk
`Petunjuk` sumbernya. Manifes lokal kini memiliki 425 unit (R006 340, R007 35,
R008 50), sedangkan O001 mencatat secara terpisah bahwa sumber tidak
menyediakan solusi. Dua build backend U425 identik pada seluruh 27 berkas /
18.027.168 byte, dengan 4.003 rekaman dan inventaris POSIX SHA-256
`729587820f9ea940bb7f25377705ceb3ed37015e15c3b86d557d541823e3b9e2`.
Build pembaca integrasi epoch-tetap menghasilkan 241 halaman / 2.427.763 byte,
SHA-256
`2166d72eaedfb0bece00d2df99902694c39a0151eb2e8243f568e68587623ba7`;
halaman 232 memuat U425 lengkap dalam Bahasa Indonesia lalu menunjukkan batas
latihan Inggris berikutnya. Seluruh gerbang U425 lulus. Checkpoint
sumber/backend U425 sudah publik pada commit
`7ffd500b2bd48c7bac13664f86e0eb04498cae97`; seluruh 42 berkas / 19.941.579
byte dibaca kembali secara anonim dan diaudit ulang secara independen. Overlay
enam berkas kontrol pemulihan juga sudah publik pada commit
`23835b0329a6397d74889aaf62fc993d02945e0e` dan telah diverifikasi ulang secara
anonim serta independen. Rilis pembaca dan DOI tetap U397.
