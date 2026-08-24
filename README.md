# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Edisi Bahasa Indonesia yang terbuka, dapat dibangun ulang, dan dapat diproses
mesin untuk tiga buku matematika karya Jiří Lebl. Repositori ini masih aktif
dikerjakan; cakupan setiap buku dinyatakan secara eksplisit.

## Mulai membaca

- **[Analisis Dasar II — WIP sampai seluruh Latihan Bagian 11.2, 180 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u319/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.2_Latihan.pdf)**
- **[Analisis Dasar I — edisi lengkap, 334 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.24.u319/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf)**
- [Rilis GitHub U319](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.24.u319)
- [Salinan pelestarian Zenodo U319](https://doi.org/10.5281/zenodo.22073827)
  (concept DOI: [10.5281/zenodo.22059779](https://doi.org/10.5281/zenodo.22059779))

PDF Jilid II berakhir setelah seluruh Bagian 11.2, `Pertukaran limit`, termasuk
sepuluh latihan penutup. Bagian 11.3, `Power series and analytic functions`,
dan ekor yang belum diterjemahkan tidak dimuat. Ini adalah cuplikan pembaca
yang jujur, bukan PDF hibrida dengan ekor berbahasa Inggris.

## Status korpus

| ID | Buku | Peran kurikulum | Status Bahasa Indonesia |
|---|---|---|---|
| R006 | *Basic Analysis I–II* | C10/C20 | Jilid I lengkap; Jilid II kontigu sampai seluruh Latihan Bagian 11.2 (U254) |
| R007 | *Notes on Diffy Qs* | B70 | Pendahuluan lengkap; Bab 1 sampai rumus integral tentu untuk kondisi awal (U015) |
| R008 | *Guide to Cultivating Complex Analysis* | C50 | Kontigu sampai akhir bagian bola Riemann (U050) |

Manifes hidup memuat **319 unit**: R006 254, R007 15, dan R008 50. Setiap unit
mengikat irisan sumber dan sasaran dengan SHA-256. Backend produksi v0.4 memuat
**2.650 rekaman** netral-lokal dan lima belas proyeksi CSV. Dua build independen
menghasilkan 26 berkas dan 11.227.185 byte yang identik; validasi skema,
integritas referensial, dan putar-balik CSV semuanya lulus.

## Isi repositori

- [`translation/`](translation/) — sumber LaTeX Bahasa Indonesia dan manifes
  unit terjemahan;
- [`backend/`](backend/) — skema, alat validasi, proyeksi CSV/JSONL, dan
  checkpoint modular;
- [`control/`](control/) — terminologi, komponen hak, dan ledger koreksi;
- [`authority/`](authority/) — identitas sumber, batas lisensi, dan bukti
  penggunaan istilah Bahasa Indonesia;
- [`qa/`](qa/) — bukti build, audit unit, dan validasi backend;
- [`release/u319/`](release/u319/) — overlay sumber untuk membangun pembaca
  Jilid II pada batas R006-U254;
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
Halaman pembuka, seluruh batas baru, bibliografi, indeks, dan daftar notasi
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
