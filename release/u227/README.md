# Overlay pembaca R006 Jilid II - U227

Direktori ini memuat tiga berkas framing yang menghasilkan pembaca WIP U227
tanpa menampilkan latihan Bagian 10.7 yang belum diterjemahkan. Batas pembaca
berada tepat setelah bukti lengkap Teorema 10.7.2 pada halaman fisik 154.

Pohon matematika berasal dari `translation/ra/`. Overlay hanya:

1. menyatakan batas WIP dalam judul dan metadata PDF;
2. memakai uraian topik biasa untuk tautan pendahuluan yang berada di luar
   cuplikan;
3. menampilkan rujukan ke Latihan 10.7.2-10.7.4 sebagai nomor biasa dengan
   keterangan bahwa latihan tersebut berada di luar cuplikan, sehingga tidak
   ada tautan mati; dan
4. menempatkan satu `\end{document}` setelah `\end{proof}` dan sebelum
   subbagian latihan.

Untuk mereproduksi pembaca:

1. Salin `translation/ra/` ke direktori build terisolasi.
2. Timpa `realanal2.tex`, `frag-vol2-intro.tex`, dan `ch-multivar-int.tex`
   dengan berkas dari direktori ini.
3. Bangun `realanal.tex` terlebih dahulu agar `realanal.aux` menyediakan peta
   referensi silang Jilid I yang sah.
4. Jalankan `pdflatex realanal2.tex`, `makeindex realanal2.idx`,
   `makeindex -s realanal2.ist -o realanal2.gls realanal2.glo`, lalu ulangi
   `pdflatex realanal2.tex` sampai dua log terakhir identik.
5. Pastikan pembaca berjumlah 154 halaman, semua tautan dan markah mengarah ke
   halaman di dalam berkas, dan halaman 154 berakhir dengan tanda QED.

Bukti build terukur berada di
`qa/R006_VOLUME2_WIP_RELEASE_U227_BUILD_RECEIPT.md`. PDF final berukuran
1.687.583 byte dan memiliki SHA-256
`b4da246e79fb30ea74e8fcf48ec0fa50aa2680f52585f6b89f66762d7f7876ed`.
