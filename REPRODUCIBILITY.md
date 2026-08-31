# Reproducibility — rilis keluarga Lebl lengkap

Dokumen ini mengikat input pembaca, sumber, backend, dan metadata rilis lengkap
secara deterministik. Jalankan perintah dari akar repositori dengan Python 3.

## Input pembaca beku

| ID | Jalur input | Berkas rilis | Halaman | Byte | SHA-256 |
|---|---|---|---:|---:|---|
| R006-volume-1 | `output/pdf/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf` | `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf` | 334 | 2870909 | `38743ea0e7ce52bdadf5233fc9d6e79e00717f9ba55a393f2bf46ea21c65ef56` |
| R006-volume-2 | `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf` | `Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf` | 241 | 2427379 | `e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3` |
| R007 | `output/pdf/Catatan_tentang_Diffy_Qs_Bahasa_Indonesia_v6.11.pdf` | `Catatan_tentang_Diffy_Qs_Bahasa_Indonesia_v6.11.pdf` | 502 | 5135134 | `1c18dfc1572d22ef7fc5d8ad25be18f3b91f1bffea5b9f9d521ff4e56ca969d4` |
| R008 | `output/pdf/Panduan_Mengolah_Analisis_Kompleks_Bahasa_Indonesia_v1.9.pdf` | `Panduan_Mengolah_Analisis_Kompleks_Bahasa_Indonesia_v1.9.pdf` | 338 | 2822132 | `87e4810abdedbdd8121995a8e53936891135037f03054dce76a06beebc3cfaae` |

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
- Backend: `backend/production/v0.4-complete-2026.08.31-a`; 27 berkas; 122843339 byte; SHA-256 inventaris `4223a618b201cdc41db050c8bf929fd8b5b5628dc253fce2c5a8eef39ca18b9e`.
- Arsip: `lebl-mathematics-family-id-source-backend-complete-20260830.zip`; 1004 berkas; 140585717 byte tak terkompresi; 18076597 byte ZIP; SHA-256 `baeea18043520f1b47825df0c9b1343f203bc1ec67119266953e19133381ab92`.

Arsip ZIP dibuat dengan urutan nama kanonik, timestamp anggota tetap 2026-08-30
00:00:00, mode POSIX tetap, UTF-8, dan kompresi DEFLATE level 9. Inventaris backend
dihash dari JSON kanonik berisi jalur relatif, ukuran, dan SHA-256 setiap berkas.

## Perintah deterministik

```text
python -B publication/final-2026.08.30/prepare_release.py
python -B publication/final-2026.08.30/validate_release.py
```

Preparasi gagal tertutup jika DOI versi belum dicadangkan, QA/ledger hak tidak lulus,
identitas input berubah, arsip sumber tidak deterministik, atau metadata rilis tidak
sesuai konfigurasi final.

## Identitas publik

- Repositori: https://github.com/KokunoYumeto/lebl-mathematics-family-id
- Rilis GitHub: https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id.2026.08.30.complete
- DOI versi Zenodo: https://doi.org/10.5281/zenodo.22182427
- DOI konsep Zenodo: https://doi.org/10.5281/zenodo.22059779
