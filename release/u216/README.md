# Overlay pembaca R006 Jilid II — U216

Direktori ini memuat tiga berkas framing yang menghasilkan pembaca WIP U216
tanpa menampilkan ekor sumber berbahasa Inggris. Matematika yang diterjemahkan
sama dengan pohon hidup `translation/ra/`; perbedaannya hanya judul WIP,
referensi pendahuluan ke bab yang belum disertakan, dan `\end{document}` tepat
setelah bukti Teorema 10.6.4 untuk domain tipe III.

Untuk mereproduksi pembaca:

1. Salin `translation/ra/` ke direktori build terisolasi.
2. Timpa `realanal2.tex`, `frag-vol2-intro.tex`, dan `ch-multivar-int.tex`
   dengan tiga berkas dari direktori ini.
3. Bangun `realanal.tex` terlebih dahulu agar `realanal.aux` menyediakan peta
   referensi silang Jilid I yang sah.
4. Jalankan `pdflatex realanal2.tex`, `makeindex realanal2.idx`,
   `makeindex -s realanal2.ist -o realanal2.gls realanal2.glo`, lalu ulangi
   `pdflatex realanal2.tex` sampai stabil.

Bukti build yang diukur berada di
`qa/R006_VOLUME2_WIP_RELEASE_BUILD_RECEIPT.md`. PDF terbitan harus berukuran
1.641.445 byte dan memiliki SHA-256
`152eec620c0d42a01a12f6b7f4b3e6e18d914359e164e573fffcad040c09ddb2`.
