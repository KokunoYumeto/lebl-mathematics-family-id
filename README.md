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

## Status checkpoint U361

Ini masih *work in progress*, bukan klaim bahwa ketiga buku sudah selesai.

- R006: Jilid I lengkap (334 halaman). Jilid II memiliki pembaca 200 halaman
  yang berakhir bersih setelah Bagian 11.5, termasuk seluruh tujuh latihan
  tentang prinsip maksimum, teorema dasar aljabar, fungsi rasional, dan
  singularitas terisolasi.
- R007: pendahuluan lengkap; Bab 1 berlanjut sampai solusi integral tentu untuk
  kondisi awal; Bab 8, *Sistem nonlinear*, lengkap sebagai 20 unit dan pembaca
  mandiri 40 halaman.
- R008: terjemahan berurutan mencapai akhir bagian bola Riemann.

Manifes hidup memuat 361 unit unik: R006 276, R007 35, dan R008 50. Backend
v0.4-live U361 memuat 3.520 rekaman, termasuk 361 segmen manifes, 372 unit,
710 konsep, 722 ekspresi, tepat 722 istilah logis kini, seluruh 241 koreksi
sumber yang tercatat, serta tujuh pemetaan kekosongan solusi O001. Lima belas
proyeksi CSV berputar balik tepat ke seluruh rekaman, dan dua build independen
identik pada path, ukuran, dan SHA-256.

## Pembaca utama

- `output/pdf/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`
- `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.5_Latihan.pdf`
- `output/pdf/Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`

Pembaca Jilid II terbaru menggunakan blok halaman penuh dan terpusat, memiliki
semua font tertanam, serta lulus build lima-pass, pemeriksaan referensi,
ekstraksi teks, dan inspeksi visual halaman baru.

## Publikasi

- Repositori: <https://github.com/KokunoYumeto/lebl-mathematics-family-id>
- Rilis U361: <https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.25.u361>
- Konsep Zenodo stabil: <https://doi.org/10.5281/zenodo.22059779>
- Katalog Figshare: <https://doi.org/10.6084/m9.figshare.33314802>

Setiap checkpoint publik diberi label parsial dengan cakupan dan pengecualian
yang eksplisit. Tidak ada penulis yang dihubungi selama produksi dan tidak ada
isu upstream baru yang dibuka.

Untuk pemulihan kerja, mulai dari
[`00_control/TASK_AND_RECOVERY.md`](00_control/TASK_AND_RECOVERY.md).
