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

## Status checkpoint U393

Ini masih *work in progress*, bukan klaim bahwa ketiga buku sudah selesai.

- R006: Jilid I lengkap (334 halaman). Jilid II memiliki pembaca 224 halaman
  yang berakhir bersih setelah Bagian 11.7, termasuk teorema aproksimasi
  Weierstrass, teorema Stone--Weierstrass versi real dan kompleks, penerapan
  aproksimasi variabel terpisah, serta seluruh empat belas latihan.
- R007: pendahuluan lengkap; Bab 1 berlanjut sampai solusi integral tentu untuk
  kondisi awal; Bab 8, *Sistem nonlinear*, lengkap sebagai 20 unit dan pembaca
  mandiri 40 halaman.
- R008: terjemahan berurutan mencapai akhir bagian bola Riemann.

Manifes hidup memuat 393 unit unik: R006 308, R007 35, dan R008 50. Backend
v0.4-live U393 memuat 3.806 rekaman, termasuk 393 segmen manifes, 424 unit,
748 konsep, 786 ekspresi, tepat 760 istilah logis kini, seluruh 256 koreksi
sumber yang tercatat, serta 21 pemetaan kekosongan solusi O001. Lima belas
proyeksi CSV berputar balik tepat ke seluruh rekaman, dan dua build independen
identik pada path, ukuran, dan SHA-256.

## Pembaca utama

- `output/pdf/Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`
- `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.7_Latihan.pdf`
- `output/pdf/Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`

Pembaca Jilid II terbaru menggunakan blok halaman penuh dan terpusat, memiliki
semua font tertanam, serta lulus sembilan pass TeX, pemeriksaan referensi,
ekstraksi teks, dan inspeksi visual halaman baru.

## Publikasi

- Repositori: <https://github.com/KokunoYumeto/lebl-mathematics-family-id>
- Rilis U393: <https://github.com/KokunoYumeto/lebl-mathematics-family-id/releases/tag/lebl-family-id-wip.2026.08.26.u393>
- DOI versi U393: <https://doi.org/10.5281/zenodo.22104149>
- Konsep Zenodo stabil: <https://doi.org/10.5281/zenodo.22059779>
- Koleksi Figshare Bahasa Indonesia: <https://doi.org/10.6084/m9.figshare.c.8668413>

Setiap checkpoint publik diberi label parsial dengan cakupan dan pengecualian
yang eksplisit. Tidak ada penulis yang dihubungi selama produksi dan tidak ada
isu upstream baru yang dibuka.

Untuk batas isi, reproduksi build, dan hash checkpoint publik, lihat
[`RELEASE_NOTES.md`](RELEASE_NOTES.md) dan
[`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).
