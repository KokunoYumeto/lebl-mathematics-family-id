# Overlay pembaca R007 Bab 8 — U357

Direktori ini memuat overlay sumber yang diperlukan untuk mereproduksi pembaca
parsial 40 halaman R007, *Notes on Diffy Qs: Persamaan Diferensial untuk
Insinyur — Bab 8: Sistem nonlinear*.

## Batas dan identitas

- Hulu: `jirilebl/diffyqs`, tag `v6.11`, commit
  `066f96506d0954cc3efb900db0d68d121733b2dc`.
- Bab sumber: `ch-nonlin-systems.tex`, 108.130 byte, SHA-256
  `9af714bde1b6d84f45c7812829e1d5ad099a0866bd0f7d6588f5d2277edc7d22`.
- Bab Indonesia: `ch-nonlin-systems.tex`, 112.655 byte, SHA-256
  `08420ee211ac98641c3a6e535c6587ff6890e1515326e627e361c5ed5ea6ee61`.
- Overlay label Indonesia: `id-localization.tex`, 3.461 byte, SHA-256
  `1f02f6678c1d2ebeb44f8b881e2206ed70d4345283eb188f8f579815ee3b062b`.
- Overlay gambar: `figures/nlin-pend.pdf_t`, 939 byte, SHA-256
  `01bc3cdb0d660cc9f4b53eccc5eb714c2f479bd773caf059c51370f739a789ad`.
- Sampul parsial: `nonlinear-systems-reader-cover-id.tex`.

## Rekonstruksi

1. Ambil sumber hulu v6.11 pada commit di atas ke direktori build baru.
2. Ganti hanya `ch-nonlin-systems.tex` dengan berkas di direktori ini dan
   salin `figures/nlin-pend.pdf_t` ke direktori gambar build.
3. Muat `id-localization.tex` tepat sebelum `\input{ch-nonlin-systems.tex}`.
   Bab-bab hulu sebelumnya sengaja tidak dilokalkan dalam build QA campuran.
4. Jalankan `pdflatex`, `makeindex`, lalu `pdflatex` sampai tidak ada permintaan
   rerun atau referensi tak terdefinisi.
5. Ambil halaman fisik 351--389 dari proof 472 halaman dan dahului dengan PDF
   satu halaman yang dibangun dari `nonlinear-systems-reader-cover-id.tex`.
6. Hasil acuan harus 40 halaman, 1.524.418 byte, SHA-256
   `8d392ef36104027fd680d1bfd73a153ea3e69ead1d4c6867143ab9d2f8f6c3ad`.

Proof lengkap campuran hanya untuk QA dan bukan pembaca publik. Pembaca parsial
menyatakan cakupan sebenarnya; bab R007 lain yang belum selesai tidak disamarkan
sebagai terjemahan. Lisensi turunan yang dipilih adalah CC BY-SA 4.0. Terjemahan,
integrasi, dan QA dilakukan dengan **OpenAI Codex gpt-5.6-sol, Ultra** atas
instruksi pengguna; seluruh kredit penulis sumber dan kontributor manusia
dipertahankan.
