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

## Checkpoint sumber/backend U430

R007 kini berlanjut melalui pembahasan perbedaan integral tentu dan integral
tak tentu, kegunaan rumus integral tentu untuk perhitungan dan penggambaran
grafik, serta definisi lokal *bentuk tertutup*. U430 memuat 430 unit (R006
344, R007 36, R008 50), dengan istilah `closed form` → `bentuk tertutup`
terikat secara eksplisit sebagai `LEBL-TERM-0798`.

Dua build backend U430 identik pada 27 berkas / 18.239.374 byte, dengan 4.026
rekaman, 860 ekspresi, 798 istilah logis, 430 ikatan manifes, dan 374
pemeriksaan komponen langsung. Seluruh skema, integritas referensial, dan 15
putar balik CSV lulus; inventaris POSIX SHA-256-nya
`bba7789a35d3d5b6db5c90a65a0cdbff6ed1330eba893e07018ba2adbf6c508f`.
Checkpoint ini hanya memperbarui sumber/backend; rilis pembaca U429 dan DOI
Zenodo `10.5281/zenodo.22172396` tetap menjadi batas pembaca terkini.

## Checkpoint U429 - R006 lengkap

R006 *Basic Analysis* Jilid I-II kini lengkap. U429 memuat 429 unit (R006
344, R007 35, R008 50) dan menutup latihan terakhir Jilid II tentang fungsi
kontinu dengan peluruhan koefisien Fourier yang lambat secara sebarang,
termasuk catatan dan petunjuk sumber. Dua build backend U429 identik pada 27
berkas / 18.208.054 byte, dengan 4.021 rekaman, 858 ekspresi, 797 istilah
logis, dan 34 pemetaan O001; inventaris POSIX SHA-256-nya
`e6ab83c87774c191ba28b4efa1d0cef3ac551d74482c52b6c968816e51c76057`.

Pembaca final Jilid II memiliki 241 halaman / 2.427.379 byte, SHA-256
`e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3`.
Dua pass final identik byte demi byte pada PDF dan tujuh produk bantu; 98 dari
98 baris font tertanam, seluruh 687 tautan dan 33 entri kerangka valid, serta
halaman 1-2 dan 231-241 lulus inspeksi visual. Rilis U429 mempertahankan status
keluarga *parsial* karena R007 dan R008 belum selesai.

Checkpoint sumber/backend U429 telah dipublikasikan pada commit
`e55907983ca54bb2c94d90230eb949b64a6ee7ff`, tree
`97cc963dc211728a20be1c18f9c8890f01790ae9`, dan seluruh 42 berkas /
20.178.050 byte telah dibaca kembali secara anonim. Inventaris kanonik
publisher memiliki SHA-256
`d9fdbc0921be59836e5c1447720711fd040d682574eac148acf2c723d7402118`.

## Checkpoint sumber/backend publik U428 (historis)

Checkpoint substantif terbaru memuat 428 unit (R006 343, R007 35, R008 50) sampai
latihan dua bagian tentang konvergensi jumlah parsial Fourier simetris pada
lompatan ke rata-rata limit sepihak. Dua build backend U428 identik pada 27
berkas / 18.151.570 byte, dengan 4.015 rekaman, 856 ekspresi, 797 istilah
logis, dan 33 pemetaan O001; inventaris POSIX SHA-256-nya
`77e1b2128513b78305740126ff974949efe6e220c720b66e65b8a09521802275`.
Build integrasi epoch-tetap menghasilkan 241 halaman / 2.427.826 byte,
SHA-256
`b566883b66b32b84edd186a97ae643d7371b4474c3b543b6a6ed0df7f128329f`;
halaman 231–233 lulus inspeksi visual, dan halaman 232 memuat U428 lengkap
sebelum batas Inggris U429 yang masih utuh.

Checkpoint sumber/backend U428 sudah publik pada commit
`0916d113a5ce9d826d3c03fe0c869830c6e37070` dan overlay kontrol
`daa1c9dee22bfcec459d3b54e9f1ab575f6b25be`; keduanya sudah dibaca kembali
byte demi byte secara anonim. Rilis pembaca dan DOI Zenodo U397 tetap tidak
berubah pada checkpoint sumber tersebut.

## Checkpoint sumber/backend publik U427 (historis)

Checkpoint terbaru memuat 427 unit (R006 342, R007 35, R008 50) sampai
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

Checkpoint sumber/backend U427 sudah publik pada commit
`89d415893405d413bc344112a36bfe497bf2e2bd`, tree
`ef2186c2d65a98acf9835d7560fc5ca57be34fd2`, dan seluruh 42 berkas /
20.048.428 byte telah dibaca kembali byte demi byte secara anonim. Inventaris
kanoniknya memiliki SHA-256
`59bb0972b85e7b3ea8bed0bba6731f535257aace66f5feec55e5240ac6e2d899`.
Overlay kontrol pemulihan juga sudah publik pada commit
`b7a8341fd6f23575c269f7c24a415966227877cc`, tree
`907cfe0eeb0e68cecd35fc15e2e63b06baf51b7c`; seluruh enam berkas / 577.053
byte telah dibaca kembali secara anonim dan inventarisnya memiliki SHA-256
`4f90527ec10f505ac531431d62fcc54fc5c14f67d5eb2e5ca66ab22aede9f573`.
Rilis pembaca dan DOI Zenodo U397 tetap tidak berubah.

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
- `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf`
- `output/pdf/Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`

Pembaca final Jilid II menggunakan blok halaman penuh dan terpusat, memiliki
semua font tertanam, serta lulus build TeX konvergen, pemeriksaan referensi,
ekstraksi teks, validasi tautan/kerangka, dan inspeksi visual halaman akhir.

## Publikasi

- Repositori: <https://github.com/KokunoYumeto/lebl-mathematics-family-id>
- Rilis U429: <https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.30.u429>
- DOI versi U429: <https://doi.org/10.5281/zenodo.22172396>
- Rilis historis U397: <https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.26.u397>
- DOI versi historis U397: <https://doi.org/10.5281/zenodo.22105195>
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
