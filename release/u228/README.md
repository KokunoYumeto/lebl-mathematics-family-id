# Overlay pembaca R006 Jilid II - U228

Direktori ini memuat tiga berkas framing yang menghasilkan pembaca WIP U228
yang berakhir tepat setelah seluruh latihan Bagian 10.7. Batas ini melengkapi
bagian penggantian variabel dan seluruh Bab 10 tanpa menampilkan ekor Bab 11
yang belum diterjemahkan.

Pohon matematika berasal dari `translation/ra/`. Overlay hanya:

1. menyatakan batas WIP dalam judul dan metadata PDF;
2. memakai uraian topik biasa untuk tautan pendahuluan yang berada di luar
   cuplikan; dan
3. menempatkan satu `\end{document}` setelah latihan keenam dan terakhir pada
   Bagian 10.7, sebelum driver dapat memuat `ch-approximate.tex`.

Semua rujukan ke Latihan 10.7.2-10.7.4 tetap berupa tautan internal hidup
karena ketiga latihan itu kini berada di dalam pembaca.

Untuk mereproduksi pembaca:

1. Salin `translation/ra/` ke direktori build terisolasi.
2. Timpa `realanal2.tex`, `frag-vol2-intro.tex`, dan `ch-multivar-int.tex`
   dengan berkas dari direktori ini.
3. Bangun `realanal.tex` terlebih dahulu agar `realanal.aux` menyediakan peta
   referensi silang Jilid I yang sah.
4. Jalankan `pdflatex realanal2.tex`, `makeindex realanal2.idx`,
   `makeindex -s realanal2.ist -o realanal2.gls realanal2.glo`, lalu ulangi
   `pdflatex realanal2.tex` sampai dua log terakhir identik.
5. Pastikan halaman terakhir berisi keenam latihan Bagian 10.7, semua tautan
   dan markah mengarah ke halaman di dalam berkas, dan tidak ada Bab 11 atau
   prosa pembaca berbahasa Inggris.

Bukti build terukur berada di
`qa/R006_VOLUME2_WIP_RELEASE_U228_BUILD_RECEIPT.md`.

