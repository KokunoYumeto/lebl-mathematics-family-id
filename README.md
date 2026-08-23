# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Edisi Bahasa Indonesia yang terbuka, dapat dibangun ulang, dan dapat diproses
mesin untuk tiga buku matematika karya Jiří Lebl. Repositori ini masih aktif
dikerjakan; cakupan setiap buku dinyatakan secara eksplisit di bawah.

## Mulai membaca

- **[Analisis Dasar I - edisi lengkap, 334 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/r006-v6.3-id-wip.2026.08.23.u228/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf)**
- **[Analisis Dasar II - WIP sampai akhir Bagian 10.7, 155 halaman](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/download/r006-v6.3-id-wip.2026.08.23.u228/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_Akhir_Bagian_10.7.pdf)**
- [Rilis GitHub U228](https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/r006-v6.3-id-wip.2026.08.23.u228)
- [Salinan pelestarian Zenodo](https://doi.org/10.5281/zenodo.22070430)
  (concept DOI: [10.5281/zenodo.22059779](https://doi.org/10.5281/zenodo.22059779))

PDF Jilid II pada rilis U228 sengaja berakhir tepat setelah keenam latihan pada
akhir Bagian 10.7, penggantian variabel. Pohon `main` melanjutkan Bab 11 secara
kontigu sampai pembukaan fungsi bernilai kompleks (U233), tetapi kelanjutan
itu belum dimasukkan ke PDF rilis dan tidak disamarkan sebagai bagian pembaca.

## Status korpus

| ID | Buku | Peran kurikulum | Status Bahasa Indonesia |
|---|---|---|---|
| R006 | *Basic Analysis I–II* | C10/C20 | Jilid I lengkap; Jilid II sampai akhir Bagian 10.7 (Bab 11 dan seterusnya belum diterjemahkan) |
| R007 | *Notes on Diffy Qs* | B70 | belum diterjemahkan |
| R008 | *Guide to Cultivating Complex Analysis* | C50 | belum diterjemahkan |

Checkpoint U228 yang dipublikasikan memuat 228 unit R006 yang diterima: 225
unit isi dan tiga driver pembaca. Pohon `main` melanjutkan terjemahan ke 233
unit (230 unit isi dan tiga driver), termasuk pembukaan bidang kompleks,
definisi bagian real/imajiner, konjugat dan modulus, serta sifat dan limit
bilangan kompleks melalui proposisi kontinuitas, konvergensi deret, dan
pembukaan fungsi bernilai kompleks pada `ch-approximate.tex`. Audit bounded
U231, U232, dan U233 tercatat di
[`qa/R006_COMPLEX_PLANE_U231_20260823.md`](qa/R006_COMPLEX_PLANE_U231_20260823.md)
dan [`qa/R006_COMPLEX_SERIES_U232_20260823.md`](qa/R006_COMPLEX_SERIES_U232_20260823.md),
serta [`qa/R006_COMPLEX_VALUED_FUNCTIONS_U233_20260823.md`](qa/R006_COMPLEX_VALUED_FUNCTIONS_U233_20260823.md).
Backend produksi v0.3 adalah checkpoint deterministik yang
telah divalidasi untuk 167 unit; 61 unit yang lebih baru sudah ada dalam
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
