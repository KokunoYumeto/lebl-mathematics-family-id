# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Edisi Bahasa Indonesia yang terbuka, dapat dibangun ulang, dan dapat diproses
mesin untuk tiga buku matematika karya Jiří Lebl. Repositori ini masih aktif
dikerjakan; cakupan setiap buku dinyatakan secara eksplisit.

## Mulai membaca

- **[Analisis Dasar II — WIP sampai akhir Bagian 11.4, 198 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u336/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.4_Latihan.pdf)**
- **[Analisis Dasar I — edisi lengkap, 334 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u336/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf)**
- [Rilis GitHub U336](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.24.u336)
- [Salinan pelestarian Zenodo U336](https://doi.org/10.5281/zenodo.22082567)
  (concept DOI: [10.5281/zenodo.22059779](https://doi.org/10.5281/zenodo.22059779))

PDF Jilid II berakhir setelah seluruh Bagian 11.4, `Eksponensial kompleks dan
fungsi trigonometri`, termasuk sebelas latihan. Bagian berikutnya, `Prinsip
maksimum dan teorema dasar aljabar`, dan ekor yang belum diterjemahkan tidak
dimuat. Ini adalah cuplikan pembaca yang jujur, bukan PDF hibrida dengan ekor
berbahasa Inggris.

## Status korpus

| ID | Buku | Peran kurikulum | Status Bahasa Indonesia |
|---|---|---|---|
| R006 | *Basic Analysis I–II* | C10/C20 | Jilid I lengkap; Jilid II kontigu sampai akhir Bagian 11.4 (U271) |
| R007 | *Notes on Diffy Qs* | B70 | Pendahuluan lengkap; Bab 1 sampai rumus integral tentu untuk kondisi awal (U015) |
| R008 | *Guide to Cultivating Complex Analysis* | C50 | Kontigu sampai akhir bagian bola Riemann (U050) |

Manifes hidup memuat **336 unit**: R006 271, R007 15, dan R008 50. Setiap unit
mengikat irisan sumber dan sasaran dengan SHA-256; SHA-256 manifes adalah
`05e5e333ae2e9ee427887c96d91848d9e99b95e4c3391f77a209ede8677a002c`.
Backend produksi v0.4 memuat
**2.701 rekaman** netral-lokal, 672 ekspresi, dan lima belas proyeksi CSV.
Checkpoint `v0.4-live-2026.08.24-u336-a` memuat 26 berkas dan 11.659.282 byte;
inventaris replay identik mempunyai SHA-256
`e39eec0b1c05b39a274ffc6fa1f23408e81c8d163a76bb4d6d8339cfb4be2321`.
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
- [`release/u336/`](release/u336/) — overlay sumber untuk membangun pembaca
  Jilid II pada batas R006-U271;
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
