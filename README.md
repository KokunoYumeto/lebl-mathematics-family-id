# Keluarga Matematika Lebl — Edisi Bahasa Indonesia

Repositori ini memuat edisi turunan Bahasa Indonesia untuk tiga buku terbuka
karya Jiří Lebl:

- *Basic Analysis: Introduction to Real Analysis, Volumes I–II* (R006),
- *Notes on Diffy Qs: Differential Equations for Engineers* (R007), dan
- *Guide to Cultivating Complex Analysis: Working the Complex Field* (R008).

Tujuannya adalah pembaca yang nyaman digunakan, sumber LaTeX yang dapat
dibangun ulang, serta backend modular netral-bahasa. Setiap buku tetap memiliki
identitas edisi, otoritas, dan lisensi tersendiri. Edisi turunan ini memilih
jalur CC BY-SA 4.0 yang tersedia pada masing-masing sumber.

Terjemahan, penyuntingan, QA istilah, dan integrasi backend dilakukan oleh
OpenAI Codex gpt-5.6-sol, Ultra atas instruksi pengguna. Jiří Lebl tetap
merupakan penulis karya sumber; semua kredit sumber dan kontributor manusia
dipertahankan. Edisi ini independen dan tidak menyiratkan dukungan penulis.

## Status checkpoint U370

Ini masih *work in progress*, bukan klaim bahwa ketiga buku sudah selesai.

- R006: Jilid I lengkap (334 halaman). Jilid II memiliki pembaca 208 halaman
  yang berakhir bersih setelah Bagian 11.6, termasuk teorema
  Arzelà--Ascoli, kedua korolari, penerapan operator kompak, dan seluruh sebelas
  latihan hingga pembuktian teorema eksistensi Peano melalui metode Euler.
- R007: pendahuluan lengkap; Bab 1 berlanjut sampai solusi integral tentu untuk
  kondisi awal; Bab 8, *Sistem nonlinear*, lengkap sebagai 20 unit dan pembaca
  mandiri 40 halaman.
- R008: terjemahan berurutan mencapai akhir bagian bola Riemann.

Manifes hidup memuat 370 unit unik: R006 285, R007 35, dan R008 50. Backend
v0.4-live U370 memuat 3.573 rekaman, termasuk 370 segmen manifes, 381 unit,
721 konsep, 740 ekspresi, tepat 733 istilah logis kini, seluruh 245 koreksi
sumber yang tercatat, serta tujuh pemetaan kekosongan solusi O001. Lima belas
proyeksi CSV berputar balik tepat ke seluruh rekaman, dan dua build independen
identik pada path, ukuran, dan SHA-256.

## Pembaca utama

- `output/pdf/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`
- `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.6_Latihan.pdf`
- `output/pdf/Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`

Pembaca Jilid II terbaru menggunakan blok halaman penuh dan terpusat, memiliki
semua font tertanam, serta lulus sembilan pass TeX, pemeriksaan referensi,
ekstraksi teks, dan inspeksi visual halaman baru.

## Publikasi

- Repositori: <https://github.com/KokunoYumeto/lebl-mathematics-family-id>
- Rilis U370: <https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.25.u370>
- Konsep Zenodo stabil: <https://doi.org/10.5281/zenodo.22059779>
- Item Figshare: <https://doi.org/10.6084/m9.figshare.33314802>

Setiap checkpoint publik diberi label parsial dengan cakupan dan pengecualian
yang eksplisit. Tidak ada penulis yang dihubungi selama produksi dan tidak ada
isu upstream baru yang dibuka.

Untuk batas isi, reproduksi build, dan hash checkpoint publik, lihat
[`RELEASE_NOTES.md`](RELEASE_NOTES.md) dan
[`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).
