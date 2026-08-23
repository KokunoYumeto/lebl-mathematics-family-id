# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Edisi Bahasa Indonesia yang terbuka, dapat dibangun ulang, dan dapat diproses
mesin untuk tiga buku matematika karya Jiří Lebl. Repositori ini masih aktif
dikerjakan; cakupan setiap buku dinyatakan secara eksplisit di bawah.

## Mulai membaca

- **[Analisis Dasar I - edisi lengkap, 334 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/r006-v6.3-id-wip.2026.08.23.u227/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf)**
- **[Analisis Dasar II - WIP sampai bukti lengkap Teorema 10.7.2, 154 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/r006-v6.3-id-wip.2026.08.23.u227/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_Akhir_Bukti_Teorema_Penggantian_Variabel.pdf)**
- [Rilis GitHub U227](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/r006-v6.3-id-wip.2026.08.23.u227)
- [Salinan pelestarian Zenodo](https://doi.org/10.5281/zenodo.22063321)
  (concept DOI: [10.5281/zenodo.22059779](https://doi.org/10.5281/zenodo.22059779))

PDF Jilid II sengaja berakhir tepat setelah bukti lengkap Teorema 10.7.2,
penggantian variabel. Pembukaan Bagian 10.7, Proposisi 10.7.1, pernyataan
teorema, gambar, dan bukti sudah disertakan. Latihan Bagian 10.7 belum
diterjemahkan dan tidak muncul dalam pembaca. Tidak ada ekor berbahasa Inggris
yang disamarkan sebagai bagian edisi Indonesia.

## Status korpus

| ID | Buku | Peran kurikulum | Status Bahasa Indonesia |
|---|---|---|---|
| R006 | *Basic Analysis I–II* | C10/C20 | Jilid I lengkap; Jilid II sampai bukti lengkap Teorema 10.7.2, dengan latihan Bagian 10.7 belum diterjemahkan |
| R007 | *Notes on Diffy Qs* | B70 | belum diterjemahkan |
| R008 | *Guide to Cultivating Complex Analysis* | C50 | belum diterjemahkan |

Checkpoint ini memuat 227 unit R006 yang diterima: 224 unit isi dan tiga
driver pembaca. Backend produksi v0.3 adalah checkpoint deterministik yang
telah divalidasi untuk 167 unit; 60 unit yang lebih baru sudah ada dalam
manifes dan ledger hidup, tetapi belum diklaim sebagai proyeksi backend v0.4.

## Isi repositori

- [`translation/`](translation/) — sumber LaTeX Bahasa Indonesia dan manifes
  unit terjemahan;
- [`backend/`](backend/) — skema, alat validasi, proyeksi CSV/JSONL, dan
  checkpoint produksi modular;
- [`control/`](control/) — terminologi, komponen hak, dan ledger koreksi;
- [`authority/`](authority/) — identitas rilis sumber dan batas lisensi;
- [`qa/`](qa/) — bukti build dan batas pembaca yang dipilih;
- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — urutan rekonstruksi dan
  pemeriksaan hash.

Backend memakai ID semantik yang netral-lokal, bukan judul terjemahan atau
nomor halaman, sehingga unit yang sama dapat dipetakan ke Bahasa Indonesia,
Tionghoa, atau bahasa lain tanpa mengubah identitas konsep sumber.

## Otoritas, perubahan, dan lisensi

Sumber R006 adalah Jiří Lebl, *Basic Analysis: Introduction to Real Analysis*,
rilis `v6.3`, commit
`00f5a8635cfba0d908cd95da53068572f30687b1`. Edisi turunan ini memilih cabang
**CC BY-SA 4.0** dari tawaran lisensi ganda sumber. Penerjemahan, penataan,
metadata aksesibilitas, koreksi yang dinyatakan, dan integrasi backend dilakukan
oleh OpenAI Codex gpt-5.6-sol, Ultra atas instruksi pengguna.

Ini adalah edisi independen dan tidak menyiratkan dukungan Jiří Lebl atau
institusi mana pun. Foto sampul ritel yang all-rights-reserved tidak termasuk.
Lihat [`LICENSE.md`](LICENSE.md) untuk ketentuan lengkap.

## Menemukan kesalahan

Kandidat koreksi sumber disimpan dan dideduplicasi dalam ledger internal.
Tidak ada percakapan otomatis dengan penulis. Sesudah seluruh korpus tiga buku
selesai, paling banyak satu laporan upstream yang ringkas dan berkeyakinan
tinggi dapat dikirim, ditandatangani sebagai Codex yang bertindak atas
instruksi pengguna.
