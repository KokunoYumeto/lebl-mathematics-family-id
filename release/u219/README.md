# Overlay pembaca R006 Jilid II — U219

Direktori ini memuat tiga berkas framing yang menghasilkan pembaca WIP U219
tanpa menampilkan ekor sumber berbahasa Inggris. Matematika yang diterjemahkan
sama dengan pohon hidup `translation/ra/`; perbedaannya hanya judul WIP,
referensi pendahuluan ke bab yang belum disertakan, dan `\end{document}` tepat
setelah latihan terakhir Bagian 10.6, Teorema Green.

Untuk mereproduksi pembaca:

1. Salin `translation/ra/` ke direktori build terisolasi.
2. Timpa `realanal2.tex`, `frag-vol2-intro.tex`, dan `ch-multivar-int.tex`
   dengan tiga berkas dari direktori ini.
3. Bangun `realanal.tex` terlebih dahulu agar `realanal.aux` menyediakan peta
   referensi silang Jilid I yang sah.
4. Jalankan `pdflatex realanal2.tex`, `makeindex realanal2.idx`,
   `makeindex -s realanal2.ist -o realanal2.gls realanal2.glo`, lalu ulangi
   `pdflatex realanal2.tex` sampai stabil.

Bukti build terukur berada di
`qa/R006_VOLUME2_WIP_RELEASE_U219_BUILD_RECEIPT.md`. PDF final berukuran
1.660.232 byte dengan 150 halaman dan SHA-256
`ddf89a837d740fd8d84887b7adc1ebafcf2c0777d9cd529314050961be1fc2cc`.
