# Keluarga Matematika Lebl — Penyempurnaan Terminologi Bahasa Indonesia

Status: **lengkap**. Repositori ini memuat edisi Bahasa Indonesia lengkap dari tiga
karya matematika terbuka Jiří Lebl. R006 disajikan dalam dua jilid, sehingga rilis
pembaca terdiri dari empat PDF.

Rilis patch ini menormalkan tiga istilah berdasarkan saksi akademik asli berbahasa
Indonesia: persamaan diferensial separabel, faktor integrasi, dan fungsi penuh.
Enam residu penghubung Inggris `and` pada R007 juga diperbaiki menjadi `dan`.

## Pembaca

| ID | Berkas | Halaman | Byte | SHA-256 | Sumber |
|---|---|---:|---:|---|---|
| R006-volume-1 | `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf` | 334 | 2870909 | `38743ea0e7ce52bdadf5233fc9d6e79e00717f9ba55a393f2bf46ea21c65ef56` | Basic Analysis: Introduction to Real Analysis, Volume I v6.3 |
| R006-volume-2 | `Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf` | 241 | 2427379 | `e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3` | Basic Analysis: Introduction to Real Analysis, Volume II v6.3 |
| R007 | `Catatan_tentang_Diffy_Qs_Bahasa_Indonesia_v6.11.pdf` | 502 | 5135112 | `5395c01c7e1b3d170dfc5d2ecb4e55fcc7cc08890ef8706a385d6ae292a72d62` | Notes on Diffy Qs: Differential Equations for Engineers v6.11 |
| R008 | `Panduan_Mengolah_Analisis_Kompleks_Bahasa_Indonesia_v1.9.pdf` | 338 | 2822050 | `efe8146e7a16fc4386b4e21cfb3454e5b1684ed6dd2f19c20a83f5b6023e6106` | Guide to Cultivating Complex Analysis: Working the Complex Field v1.9 |

## Cakupan dan backend modular

Manifes final memuat **5884 unit**: R006 2625, R007 1732, dan R008 1527. Status keluarga dan ketiga sumber adalah lengkap.

Backend netral-bahasa final berada di `backend/production/v0.4-complete-2026.08.31-tqa-release-a` dan memuat 27 berkas (122779068 byte). SHA-256 inventaris kanoniknya adalah `4005b1bf3ee6c7b4b4e70f658eea141d188479727c31617df7b8038cdc8dcabc`.

Paket sumber/backend `lebl-mathematics-family-id-source-backend-complete-terminology-20260831.zip` memuat 1016 berkas, 140492120 byte tak terkompresi, dan 18121930 byte ZIP; SHA-256 `afbfc12d5bedf27dca3bd412a3183092ecbf64ba30976c15a0128820b883a51c`.

## Sumber, hak, dan provenance

Jiří Lebl tetap penulis karya sumber. R006 menggunakan Basic Analysis v6.3, R007
menggunakan Notes on Diffy Qs v6.11, dan R008 menggunakan Guide to Cultivating
Complex Analysis v1.9. Untuk masing-masing karya, edisi turunan ini memilih cabang
lisensi CC BY-SA 4.0 yang tersedia pada sumber; rincian komponen pihak ketiga berada
di ledger hak dalam paket sumber.

Penerjemahan, penyuntingan, QA istilah dan matematika, penataan pembaca, dan integrasi
backend dilakukan oleh **OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna.
Edisi ini independen dan tidak menyiratkan dukungan penulis.

## Rilis publik

- Repositori: https://github.com/KokunoYumeto/lebl-mathematics-family-id
- Rilis GitHub: https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id.2026.08.31.terminology
- DOI versi Zenodo: https://doi.org/10.5281/zenodo.22215300
- DOI konsep Zenodo: https://doi.org/10.5281/zenodo.22059779

Gunakan DOI versi untuk mengutip byte rilis ini dan DOI konsep untuk mengikuti revisi
berikutnya dalam garis keturunan yang sama.
