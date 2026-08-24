# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Edisi Bahasa Indonesia yang terbuka, dapat dibangun ulang, dan dapat diproses
mesin untuk tiga buku matematika karya Jiří Lebl. Repositori ini masih aktif
dikerjakan; cakupan setiap buku dinyatakan secara eksplisit.

## Mulai membaca

- **[Analisis Dasar II — WIP sampai akhir Subbagian 11.3.4, 188 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u330/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.3.4_Deret_Pangkat_Analitik.pdf)**
- **[Analisis Dasar I — edisi lengkap, 334 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u330/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf)**
- [Rilis GitHub U330](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.24.u330)
- [Salinan pelestarian Zenodo U330](https://doi.org/10.5281/zenodo.22074515)
  (concept DOI: [10.5281/zenodo.22059779](https://doi.org/10.5281/zenodo.22059779))

PDF Jilid II berakhir setelah seluruh Subbagian 11.3.4, `Fungsi analitik`.
Subbagian berikutnya, `Identity theorem`, dan ekor yang belum diterjemahkan
tidak dimuat. Ini adalah cuplikan pembaca yang jujur, bukan PDF hibrida dengan
ekor berbahasa Inggris.

## Status korpus

| ID | Buku | Peran kurikulum | Status Bahasa Indonesia |
|---|---|---|---|
| R006 | *Basic Analysis I–II* | C10/C20 | Jilid I lengkap; Jilid II kontigu sampai akhir Subbagian 11.3.4 (U265) |
| R007 | *Notes on Diffy Qs* | B70 | Pendahuluan lengkap; Bab 1 sampai rumus integral tentu untuk kondisi awal (U015) |
| R008 | *Guide to Cultivating Complex Analysis* | C50 | Kontigu sampai akhir bagian bola Riemann (U050) |

Manifes hidup memuat **330 unit**: R006 265, R007 15, dan R008 50. Setiap unit
mengikat irisan sumber dan sasaran dengan SHA-256; SHA-256 manifes adalah
`c45f42524e598f724e5845c1a7e3c38b9c43de241dcae63b48870b2683d1b34b`.
Backend produksi v0.4 memuat
**2.683 rekaman** netral-lokal dan lima belas proyeksi CSV. Checkpoint
`v0.4-live-2026.08.24-u330-figfix-a` memuat 26 berkas dan 11.495.077 byte;
inventaris replay identik mempunyai SHA-256
`8c60d50e03a80441dcc5e73ba398ab37f1b258048cb34368d44d474296ac68df`.
Validasi skema, integritas referensial, dan putar-balik CSV semuanya lulus.
PDF pembaca Jilid II U330 mempunyai SHA-256
`28c0844666712d94bed82789e014faf8dbbba32c2384b77cd745423c4f845aa1`.

## Isi repositori

- [`translation/`](translation/) — sumber LaTeX Bahasa Indonesia dan manifes
  unit terjemahan;
- [`backend/`](backend/) — skema, alat validasi, proyeksi CSV/JSONL, dan
  checkpoint modular;
- [`control/`](control/) — terminologi, komponen hak, dan ledger koreksi;
- [`authority/`](authority/) — identitas sumber, batas lisensi, dan bukti
  penggunaan istilah Bahasa Indonesia;
- [`qa/`](qa/) — bukti build, audit unit, dan validasi backend;
- [`release/u330/`](release/u330/) — overlay sumber untuk membangun pembaca
  Jilid II pada batas R006-U265;
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — urutan rekonstruksi dan
  pemeriksaan hash.

Backend memakai ID semantik yang netral-lokal, bukan judul terjemahan atau
nomor halaman. Unit yang sama dapat dipetakan ke Bahasa Indonesia, Tionghoa,
atau bahasa lain tanpa mengubah identitas konsep sumber.

## QA istilah dan keterbacaan

Pemeriksaan lapangan satu kali mencoba paket TeX arXiv yang relevan, tetapi
teksnya ternyata berbahasa Inggris dan tidak dipakai sebagai bukti istilah
Indonesia. Sumber akademik Indonesia kemudian diperiksa langsung, termasuk
bahan ajar Analisis Real. Audit tersebut menguatkan istilah baku yang dipakai,
merekam variasi seperti `persekitaran`/`kitaran` dan `sub barisan`/`barisan
bagian`, serta mempertahankan bentuk pilihan konsisten `lingkungan` dan
`subbarisan`. Bukti dan keputusan lengkap ada di
[`authority/terminology_evidence/`](authority/terminology_evidence/).

Pembaca Jilid II dibangun dari cutoff sumber, bukan pemotongan halaman PDF.
Halaman pembuka, seluruh batas baru, Figure 11.6 yang dilokalkan, bibliografi,
indeks, dan daftar notasi
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
