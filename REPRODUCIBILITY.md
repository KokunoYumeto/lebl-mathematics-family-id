# Reproducibility — rilis keluarga Lebl lengkap

Dokumen ini mengikat input pembaca, sumber, backend, dan metadata rilis lengkap
secara deterministik. Jalankan perintah dari akar repositori dengan Python 3.

## Input pembaca beku

| ID | Jalur input | Berkas rilis | Halaman | Byte | SHA-256 |
|---|---|---|---:|---:|---|
| R006-volume-1 | `output/pdf/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf` | `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf` | 334 | 2870909 | `38743ea0e7ce52bdadf5233fc9d6e79e00717f9ba55a393f2bf46ea21c65ef56` |
| R006-volume-2 | `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf` | `Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf` | 241 | 2427379 | `e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3` |
| R007 | `output/pdf/Catatan_tentang_Diffy_Qs_Bahasa_Indonesia_v6.11.pdf` | `Catatan_tentang_Diffy_Qs_Bahasa_Indonesia_v6.11.pdf` | 502 | 5135112 | `5395c01c7e1b3d170dfc5d2ecb4e55fcc7cc08890ef8706a385d6ae292a72d62` |
| R008 | `output/pdf/Panduan_Mengolah_Analisis_Kompleks_Bahasa_Indonesia_v1.9.pdf` | `Panduan_Mengolah_Analisis_Kompleks_Bahasa_Indonesia_v1.9.pdf` | 338 | 2822050 | `efe8146e7a16fc4386b4e21cfb3454e5b1684ed6dd2f19c20a83f5b6023e6106` |

Keempat input di atas harus cocok byte demi byte. Preparasi rilis memeriksa framing
PDF, jumlah halaman, marker profil privat, ukuran, dan SHA-256 sebelum menyalin byte.

## Sumber dan lisensi

- R006 — Basic Analysis: Introduction to Real Analysis, Volume I–II, v6.3; cabang lisensi CC BY-SA 4.0.
- R007 — Notes on Diffy Qs: Differential Equations for Engineers, v6.11; cabang lisensi CC BY-SA 4.0.
- R008 — Guide to Cultivating Complex Analysis: Working the Complex Field, v1.9; cabang lisensi CC BY-SA 4.0.

Jiří Lebl tetap penulis ketiga karya sumber. Penerjemahan, penyuntingan, QA istilah
dan matematika, penataan pembaca, serta integrasi backend dilakukan oleh OpenAI
Codex gpt-5.6-sol, Ultra atas instruksi pengguna. Ledger hak mempertahankan atribusi
dan lisensi komponen pihak ketiga secara terpisah.

## Cakupan final dan backend

- Manifes: 5884 unit; R006 2625, R007 1732, R008 1527; status lengkap.
- Backend: `backend/production/v0.4-complete-2026.08.31-tqa-release-a`; 27 berkas; 122779068 byte; SHA-256 inventaris `4005b1bf3ee6c7b4b4e70f658eea141d188479727c31617df7b8038cdc8dcabc`.
- Arsip: `lebl-mathematics-family-id-source-backend-complete-terminology-20260831.zip`; 1016 berkas; 140492120 byte tak terkompresi; 18121930 byte ZIP; SHA-256 `afbfc12d5bedf27dca3bd412a3183092ecbf64ba30976c15a0128820b883a51c`.

Arsip ZIP dibuat dengan urutan nama kanonik, timestamp anggota tetap 2026-08-31
00:00:00, mode POSIX tetap, UTF-8, dan kompresi DEFLATE level 9. Inventaris backend
dihash dari JSON kanonik berisi jalur relatif, ukuran, dan SHA-256 setiap berkas.

## Perintah deterministik

```text
python -B backend/production/validate_complete_backend.py --dataset backend/production/v0.4-complete-2026.08.31-tqa-release-a/dataset.json --csv-dir backend/production/v0.4-complete-2026.08.31-tqa-release-a/csv
powershell -NoProfile -ExecutionPolicy Bypass -File qa/terminology_qa/build_terminology_patch_readers.ps1
```

Validasi backend memakai seluruh dataset, skema, referensi, dan proyeksi CSV yang
dikirim. Build PDF mengharuskan checkout sumber upstream yang dipatok oleh ledger hak
pada `source/diffyqs-v6.11` dan `source/ca-v1.9`; overlay terjemahan, dependensi CTAN
tersemat, hash, mutex TeX global, epoch sumber, dan langkah multipass berada dalam
paket ini. Bukti build A/B yang dipakai untuk rilis disimpan sebagai receipt QA.

## Identitas publik

- Repositori: https://github.com/KokunoYumeto/lebl-mathematics-family-id
- Rilis GitHub: https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id.2026.08.31.terminology
- DOI versi Zenodo: https://doi.org/10.5281/zenodo.22215300
- DOI konsep Zenodo: https://doi.org/10.5281/zenodo.22059779
