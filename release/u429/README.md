# Overlay pembaca lengkap R006 Jilid II — U429

Overlay ini membekukan pembaca lengkap R006 Jilid II pada checkpoint U429.
`ch-approximate.tex` adalah bab lengkap, bukan potongan WIP;
`realanal2.tex` adalah driver rilis; dan `build_u429.ps1` menegakkan identitas
sumber, epoch build, stabilitas PDF serta tujuh produk bantu, jumlah halaman,
font tertanam, dan hash PDF final.

Identitas sumber publik U429:

- commit: `e55907983ca54bb2c94d90230eb949b64a6ee7ff`
- tree: `97cc963dc211728a20be1c18f9c8890f01790ae9`
- `ch-approximate.tex`: 198.362 byte, SHA-256
  `cfaa1339706c31f16255642adcccb33903343808bc2d1bf195d70d3f25004133`
- `realanal2.tex`: 20.444 byte, SHA-256
  `99670a3938d6cd54b7e37158c88185d3baaf9116f2927ff73e57fee5ac1ed03f`

Hasil acuan adalah
`Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf`: 241 halaman, 2.427.379
byte, SHA-256
`e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3`.

Untuk reproduksi, salin seluruh `translation/ra/` ke direktori build
terisolasi, timpa `ch-approximate.tex` dan `realanal2.tex` dengan kedua berkas
overlay ini, salin `build_u429.ps1` ke direktori tersebut, sediakan
`realanal.aux` dari build Jilid I pada pohon yang sama, lalu jalankan skrip.
Skrip sengaja gagal tertutup jika byte sumber, alat bantu, log, halaman, atau
hasil akhir menyimpang.
