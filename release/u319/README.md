# Overlay pembaca R006 Jilid II — U319 / batas R006-U254

Overlay ini membangun pembaca Bahasa Indonesia *Analisis Dasar II* sampai
seluruh sepuluh latihan yang menutup Bagian 11.2, `Pertukaran limit`.

## Batas

- Komponen hidup: `translation/ra/ch-approximate.tex`, 182.186 byte, SHA-256
  `b06e83c2a6508e059bea6e21bd41fed65b5c75545f7221da12090e59b7713e61`.
- Cutoff overlay: target raw line 1030 inclusive, 35.780 byte, SHA-256
  `63edb3e4c91c3f015f84d641fbf67947f0434b870930d42c4700ce67d4c4b7a4`.
- Unit terakhir: `R006-U254`, latihan penutup Bagian 11.2.
- Unit berikutnya dimulai pada source raw line 1040 / target raw line 1035,
  `Power series and analytic functions`; materi itu tidak ada dalam pembaca.

## Cara memakai

Salin seluruh pohon `translation/ra/` ke direktori build baru. Ganti
`realanal2.tex` dan `ch-approximate.tex` pada salinan dengan kedua berkas di
direktori overlay ini. Jangan menerapkan cutoff ke pohon terjemahan hidup.
Jalankan converter, generator indeks/glosarium, lalu lima pass `pdflatex`.

Driver membekukan nomor hanya untuk dua target yang sengaja berada setelah
cutoff, Bagian 11.6 dan 11.7. Nomornya dibuktikan oleh build penuh sumber v6.3;
target tidak disertakan dan tidak dibuat seolah-olah dapat diklik.

Hasil terverifikasi: 180 halaman, 1.909.146 byte, SHA-256
`303ec82e16d133e938247f6611e31e36cb435ff0285a7b33fbbf4f8a5eb91725`.
Receipt lengkap berada di
`qa/R006_VOLUME2_SWAPPING_LIMITS_SECTION_READER_U254_BUILD_RECEIPT.md`.

Penerjemahan, penataan, QA istilah, dan integrasi backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna. Semua kredit
sumber dan kontributor manusia tetap dipertahankan. Lisensi turunan:
CC BY-SA 4.0.
