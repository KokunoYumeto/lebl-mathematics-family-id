# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Edisi Bahasa Indonesia yang terbuka, dapat dibangun ulang, dan dapat diproses
mesin untuk tiga buku matematika karya Jiří Lebl. Repositori ini masih aktif
dikerjakan; cakupan setiap buku dinyatakan secara eksplisit.

## Mulai membaca

- **[Notes on Diffy Qs — Bab 8 Sistem nonlinear, 40 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u357/Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf)**
- **[Analisis Dasar II — WIP sampai akhir Bagian 11.4, 198 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u357/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.4_Latihan.pdf)**
- **[Analisis Dasar I — edisi lengkap, 334 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u357/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf)**
- [Rilis GitHub U357](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.24.u357)
- [Salinan pelestarian Zenodo U357](https://doi.org/10.5281/zenodo.22086636)
  (concept DOI: [10.5281/zenodo.22059779](https://doi.org/10.5281/zenodo.22059779))

Pembaca R007 memuat terjemahan lengkap Bab 8 dan tidak mencampurkan bab hulu
berbahasa Inggris. PDF R006 Jilid II berakhir setelah seluruh Bagian 11.4, `Eksponensial kompleks dan
fungsi trigonometri`, termasuk sebelas latihan. Bagian berikutnya, `Prinsip
maksimum dan teorema dasar aljabar`, dan ekor yang belum diterjemahkan tidak
dimuat. Ini adalah cuplikan pembaca yang jujur, bukan PDF hibrida dengan ekor
berbahasa Inggris.

## Status korpus

| ID | Buku | Peran kurikulum | Status Bahasa Indonesia |
|---|---|---|---|
| R006 | *Basic Analysis I–II* | C10/C20 | Jilid I lengkap; sumber hidup Jilid II sampai lema modulus minimum pertama (U272); pembaca publik sampai akhir Bagian 11.4 |
| R007 | *Notes on Diffy Qs* | B70 | Pendahuluan lengkap; Bab 1 sampai rumus integral tentu untuk kondisi awal (U015); Bab 8 lengkap sebagai 20 unit |
| R008 | *Guide to Cultivating Complex Analysis* | C50 | Kontigu sampai akhir bagian bola Riemann (U050) |

Manifes hidup memuat **357 unit**: R006 272, R007 35, dan R008 50. Setiap unit
mengikat irisan sumber dan sasaran dengan SHA-256; SHA-256 manifes adalah
`783aff8d2d58a6ae8d152816cd7d8799c95c0eda27c04c61b719b5b4d56d47ba`.
Backend produksi v0.4 memuat
**3.326 rekaman** netral-lokal, 714 ekspresi, 700 konsep, 734 rekaman istilah
fisik, tepat 712 istilah logis kini, dan lima belas proyeksi CSV.
Checkpoint `v0.4-live-2026.08.24-u357-a` memuat 26 berkas dan 13.493.718 byte;
inventaris replay identik mempunyai SHA-256
`cf2c08405a3c7926d2f5b1e54d1d7b94733636156256a609b84648791f27976e`.
Validasi skema, integritas referensial, dan putar-balik CSV semuanya lulus.
PDF pembaca Jilid II U336 mempunyai SHA-256
`78543d4e8087e68589e8f15d0a3a969b3282247c7c9c2cdcb6f658dfa4b68e4f`.

## Isi repositori

- [`translation/`](translation/) — sumber LaTeX Bahasa Indonesia dan manifes
  unit terjemahan;
- [`backend/`](backend/) — skema, alat validasi, proyeksi CSV/JSONL, dan
  checkpoint modular;
- [`control/`](control/) — terminologi, komponen hak, dan ledger koreksi;
- [`authority/`](authority/) — identitas sumber, batas lisensi, dan bukti
  penggunaan istilah Bahasa Indonesia;
- [`qa/`](qa/) — bukti build, audit unit, dan validasi backend;
- [`release/u357/`](release/u357/) — overlay sumber untuk membangun pembaca
  R007 Bab 8; overlay R006 U336 tetap dipertahankan;
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — urutan rekonstruksi dan
  pemeriksaan hash.

Backend memakai ID semantik yang netral-lokal, bukan judul terjemahan atau
nomor halaman. Unit yang sama dapat dipetakan ke Bahasa Indonesia, Tionghoa,
atau bahasa lain tanpa mengubah identitas konsep sumber.

## QA istilah dan keterbacaan

Pencarian arXiv terbatas tidak menemukan sumber matematika berbahasa Indonesia
dengan sumber TeX yang dapat diunduh. Sebagai fallback yang dinyatakan secara
jujur, buku analisis kompleks Indonesia karya Zetriuslita diperiksa melalui
ekstraksi dan render halaman. Audit tersebut menguatkan `fungsi analitik`,
`lingkungan`, `deret pangkat`, `jari-jari konvergensi`, `bagian real`, `bagian
imajiner`, `fungsi trigonometri`, dan `rumus Euler`; bentuk pilihan
`fungsi eksponensial` dipertahankan atas varian teramati `fungsi eksponen`.
Laporan tersanitasi ada di
[`qa/TERMINOLOGY_QA_REVALIDATION_20260824.md`](qa/TERMINOLOGY_QA_REVALIDATION_20260824.md).

Pembaca Jilid II dibangun dari cutoff sumber, bukan pemotongan halaman PDF.
Halaman pembuka, seluruh Bagian 11.4, kedua gambar, sebelas latihan,
bibliografi, indeks, dan daftar notasi dirender dan diperiksa. Teks memakai
blok penuh yang terpusat; tidak ada formula terpotong, tumpang tindih, glyph
rusak, atau ekor yang tidak diterjemahkan. Converter berakhir dengan nol error;
639 ID dan 909 referensi silang diperiksa, dengan hanya dua target masa depan
yang sengaja berada di luar cutoff.

Pembaca R007 Bab 8 berasal dari chapter v6.11 lengkap yang diverifikasi ulang
oleh pemilik lane: 1.591 perintah, 444 batas lingkungan, 735 payload inline,
70 payload display, 31 label, 26 panggilan gambar, serta seluruh dependensi
bibliografi cocok. Proof campuran 472 halaman konvergen tanpa error atau
referensi tak terdefinisi; semua 39 halaman bab dirender. Overlay label
menghasilkan `Bab`, `Catatan`, `Contoh`, `Gambar`, `Tabel`, `Latihan`,
`Teorema`, dan `Bukti` tanpa scaffold Inggris. Pembaca 40 halaman mempunyai
SHA-256 `8d392ef36104027fd680d1bfd73a153ea3e69ead1d4c6867143ab9d2f8f6c3ad`.

## Otoritas, perubahan, dan lisensi

Sumber R006 adalah Jiří Lebl, *Basic Analysis: Introduction to Real Analysis*,
rilis `v6.3`, commit
`00f5a8635cfba0d908cd95da53068572f30687b1`. Edisi turunan ini memilih cabang
**CC BY-SA 4.0** dari tawaran lisensi ganda sumber. Penerjemahan, penataan,
metadata aksesibilitas, QA istilah, dan integrasi backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna.

Ini adalah edisi independen dan tidak menyiratkan dukungan Jiří Lebl atau
institusi mana pun. Foto sampul ritel yang all-rights-reserved tidak termasuk.
Lihat [`LICENSE.md`](LICENSE.md) untuk ketentuan lengkap.

## Menemukan kesalahan

Kandidat koreksi sumber disimpan dan dideduplicasi dalam ledger internal.
Tidak ada percakapan otomatis dengan penulis. Sesudah seluruh korpus tiga buku
selesai, paling banyak satu laporan upstream yang ringkas dan berkeyakinan
tinggi dapat dikirim, ditandatangani sebagai Codex yang bertindak atas
instruksi pengguna.
