# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Edisi Bahasa Indonesia yang terbuka, dapat dibangun ulang, dan dapat diproses
mesin untuk tiga buku matematika karya Jiří Lebl. Repositori ini masih aktif
dikerjakan; cakupan setiap buku dinyatakan secara eksplisit di bawah.

## Mulai membaca

- **[Analisis Dasar I — edisi lengkap, 334 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.23.u310/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf)**
- **[Analisis Dasar II — WIP sampai akhir Subbagian 11.2.1, Kekontinuan, 176 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/lebl-family-id-wip.2026.08.23.u310/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.2.1_Kekontinuan.pdf)**
- [Rilis GitHub U310](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.23.u310)
- [Salinan pelestarian Zenodo U310](https://doi.org/10.5281/zenodo.22071911)
  (concept DOI: [10.5281/zenodo.22059779](https://doi.org/10.5281/zenodo.22059779))

PDF Jilid II sengaja berakhir setelah seluruh Subbagian 11.2.1,
`Kekontinuan`. Subbagian berikutnya, `Integration`, dan seluruh ekor yang belum
diterjemahkan tidak dimuat. Ini adalah cuplikan pembaca yang jujur, bukan PDF
sumber lengkap dengan ekor berbahasa Inggris.

## Status korpus

| ID | Buku | Peran kurikulum | Status Bahasa Indonesia |
|---|---|---|---|
| R006 | *Basic Analysis I–II* | C10/C20 | Jilid I lengkap; Jilid II kontigu sampai akhir Subbagian 11.2.1, Kekontinuan (U251) |
| R007 | *Notes on Diffy Qs* | B70 | Bab pendahuluan lengkap (U012); berikutnya `ch-first-order-ode.tex` |
| R008 | *Guide to Cultivating Complex Analysis* | C50 | Kontigu sampai pemetaan eksponensial atas garis dan pita (U047); berikutnya bola Riemann |

Manifes hidup memuat **310 unit**: R006 251, R007 12, dan R008 47.
Setiap unit mengikat irisan sumber dan sasaran dengan SHA-256. Backend produksi
v0.4 memuat **2.623 rekaman** netral-lokal dan lima belas proyeksi CSV; dua
build independen menghasilkan 26 berkas dan 11.027.539 byte yang identik.
Validasi skema, integritas referensial, dan putar-balik CSV semuanya lulus.

## Isi repositori

- [`translation/`](translation/) — sumber LaTeX Bahasa Indonesia dan manifes
  unit terjemahan;
- [`backend/`](backend/) — skema, alat validasi, proyeksi CSV/JSONL, dan
  checkpoint produksi modular;
- [`control/`](control/) — terminologi, komponen hak, dan ledger koreksi;
- [`authority/`](authority/) — identitas rilis sumber, batas lisensi, dan bukti
  penggunaan istilah Bahasa Indonesia;
- [`qa/`](qa/) — bukti build, audit unit, dan validasi backend;
- [`release/u310/`](release/u310/) — overlay sumber untuk membangun pembaca
  Jilid II pada batas U251;
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — urutan rekonstruksi dan
  pemeriksaan hash.

Backend memakai ID semantik yang netral-lokal, bukan judul terjemahan atau
nomor halaman. Unit yang sama dengan demikian dapat dipetakan ke Bahasa
Indonesia, Tionghoa, atau bahasa lain tanpa mengubah identitas konsep sumber.

## QA istilah dan keterbacaan

Pemeriksaan lapangan satu kali mencoba sumber TeX arXiv yang relevan, tetapi
bahasanya ternyata Inggris sehingga tidak dipakai sebagai bukti istilah
Indonesia. Dua sumber akademik Indonesia kemudian diperiksa langsung sebagai
fallback. Hanya dua penyempurnaan yang dibenarkan—`hasil kali Kartesius` dan
`terhitung tak hingga`—dan keduanya telah dipropagasikan. Laporan lengkap ada
di [`authority/terminology_evidence/`](authority/terminology_evidence/).

Pembaca Jilid II dibangun dari cutoff sumber, bukan pemotongan halaman PDF.
Halaman pembuka, seluruh batas baru, gambar, bibliografi, indeks, dan daftar
notasi dirender dan diperiksa. Teks memakai blok penuh yang terpusat; tidak ada
formula terpotong, tumpang tindih, atau ekor yang tidak diterjemahkan.

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
