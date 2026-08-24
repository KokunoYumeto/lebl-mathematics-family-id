# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Edisi Bahasa Indonesia yang terbuka, dapat dibangun ulang, dan dapat diproses
mesin untuk tiga buku matematika karya Jiří Lebl. Repositori ini masih aktif
dikerjakan; cakupan setiap buku dinyatakan secara eksplisit.

## Mulai membaca

- **[Analisis Dasar II — WIP sampai akhir Subbagian 11.4.1, 192 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u333/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.4.1_Eksponensial_Kompleks.pdf)**
- **[Analisis Dasar I — edisi lengkap, 334 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u333/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf)**
- [Rilis GitHub U333](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.24.u333)
- [Salinan pelestarian Zenodo U333](https://doi.org/10.5281/zenodo.22076849)
  (concept DOI: [10.5281/zenodo.22059779](https://doi.org/10.5281/zenodo.22059779))

PDF Jilid II berakhir setelah seluruh Subbagian 11.4.1, `Eksponensial
kompleks`. Subbagian berikutnya, `Fungsi trigonometri dan pi`, dan ekor yang
belum diterjemahkan tidak dimuat. Ini adalah cuplikan pembaca yang jujur,
bukan PDF hibrida dengan ekor berbahasa Inggris.

## Status korpus

| ID | Buku | Peran kurikulum | Status Bahasa Indonesia |
|---|---|---|---|
| R006 | *Basic Analysis I–II* | C10/C20 | Jilid I lengkap; Jilid II kontigu sampai akhir Subbagian 11.4.1 (U268) |
| R007 | *Notes on Diffy Qs* | B70 | Pendahuluan lengkap; Bab 1 sampai rumus integral tentu untuk kondisi awal (U015) |
| R008 | *Guide to Cultivating Complex Analysis* | C50 | Kontigu sampai akhir bagian bola Riemann (U050) |

Manifes hidup memuat **333 unit**: R006 268, R007 15, dan R008 50. Setiap unit
mengikat irisan sumber dan sasaran dengan SHA-256; SHA-256 manifes adalah
`de03bdf56a20104420dde65bbb47778189f58a97134b6867aa32f6cbd1ba0385`.
Backend produksi v0.4 memuat
**2.692 rekaman** netral-lokal dan lima belas proyeksi CSV. Checkpoint
`v0.4-live-2026.08.24-u333-a` memuat 26 berkas dan 11.574.002 byte;
inventaris replay identik mempunyai SHA-256
`d0aac7d8017ba5f6540f5fa1ab344982146ab35347d7f7337d38513948823bf1`.
Validasi skema, integritas referensial, dan putar-balik CSV semuanya lulus.
PDF pembaca Jilid II U333 mempunyai SHA-256
`6f1f38221af120d6459cdc217e789ca1f7a9d4f353f5720db00ff271ce637061`.

## Isi repositori

- [`translation/`](translation/) — sumber LaTeX Bahasa Indonesia dan manifes
  unit terjemahan;
- [`backend/`](backend/) — skema, alat validasi, proyeksi CSV/JSONL, dan
  checkpoint modular;
- [`control/`](control/) — terminologi, komponen hak, dan ledger koreksi;
- [`authority/`](authority/) — identitas sumber, batas lisensi, dan bukti
  penggunaan istilah Bahasa Indonesia;
- [`qa/`](qa/) — bukti build, audit unit, dan validasi backend;
- [`release/u333/`](release/u333/) — overlay sumber untuk membangun pembaca
  Jilid II pada batas R006-U268;
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
Halaman pembuka, seluruh batas baru, Figure 11.6 yang dilokalkan, Figure 11.7,
bibliografi, indeks, dan daftar notasi
dirender dan diperiksa. Teks memakai blok penuh yang terpusat; tidak ada formula
terpotong, tumpang tindih, glyph rusak, atau ekor yang tidak diterjemahkan.

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
