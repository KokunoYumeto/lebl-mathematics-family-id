# R006 U281 — teorema Arzelà--Ascoli dan pembuktian

Status: **PASS; diterima sebagai unit terjemahan kontigu**  
Tanggal: 2026-08-25  
Provenance runtime: `OpenAI Codex gpt-5.6-sol, Ultra`

## Batas dan identitas

- ID stabil:
  `ra.v2.equicontinuity-arzela-ascoli.theorem-and-proof`.
- Sumber beku: `source/ra-v6.3/ch-approximate.tex`, raw lines 2764–2872
  inclusive; 109 LF lines; 3.855 byte; SHA-256
  `cdde09f5054166ac4a397113774f477f34bfea66ffc85849db52d5b26a83c711`.
- Sasaran: `translation/ra/ch-approximate.tex`, raw lines 2773–2881
  inclusive; 109 LF lines; 4.222 byte; SHA-256
  `be8e2f16e2f727658c7483fe52d16af1aaa3e049c726a6600e6973b9709ebe93`.
- Batas berikutnya: source raw line 2874 / target raw line 2883, dimulai
  dengan korolari kekompakan himpunan tertutup, terbatas, dan ekuikontinu
  seragam dalam `C(X,\C)`.

## Cakupan dan istilah

Unit mempertahankan jembatan pembuka, catatan kaki eponim, pernyataan utama
teorema Arzelà--Ascoli, penjelasan ruang fungsi, dan pembuktian lengkap.
Hipotesis kekompakan ruang metrik, keterbatasan titik demi titik, serta
ekuikontinuitas seragam dipertahankan. Kesimpulan keterbatasan seragam dan
keberadaan subbarisan yang konvergen seragam dipertahankan.

Pembuktian mempertahankan penutup berhingga untuk keterbatasan seragam,
pemilihan subbarisan pada subhimpunan rapat terhitung, pemadatan penutup oleh
bola-`delta`, serta argumen `epsilon/3` yang menghasilkan barisan Cauchy secara
seragam. `LEBL-TERM-0730` mengikat *Arzela--Ascoli theorem* ke `teorema
Arzelà--Ascoli`, dengan ejaan aksen TeX sumber tetap dipertahankan dalam
identitas TeX.

## Koreksi sumber terikat

Terdapat tepat satu perubahan editorial sumber, dicatat sebagai
`LEBL-ID-ADV-0242`. Sumber berakhir dengan komentar `%FIXME: reference?`
setelah menyimpulkan bahwa barisan fungsi bersifat Cauchy secara seragam dan
menggunakan kelengkapan `\C`. Sasaran menambahkan rujukan aktif yang tepat,
`\propref{prop:unifcauchymetric}`, yaitu proposisi terdahulu yang menyatakan
bahwa barisan fungsi Cauchy secara seragam dengan kodomain lengkap secara
Cauchy konvergen seragam. Tidak ada rumus atau kesimpulan yang diubah.

Penyebutan `reverse triangle inequality` dalam sumber sah secara matematis:
`||a|-|b|| <= |a-b|` menyiratkan `|a| <= |a-b|+|b|`. Oleh sebab itu,
penyebutan tersebut dipertahankan sebagai `ketaksamaan segitiga terbalik` dan
tidak dicatat sebagai kesalahan sumber.

## QA independen

- Struktur: PASS. Sumber dan sasaran masing-masing memiliki 109 baris LF dan
  nol CR. Aliran lingkungan identik: 26 peristiwa / 13 pasangan seimbang
  (`thm` 1, `proof` 1, `equation*` 10, `split` 1).
- Kontrol TeX aktif berjumlah 165 pada sumber dan 166 pada sasaran; satu-satunya
  tambahan adalah `\propref{prop:unifcauchymetric}` yang dinyatakan dalam
  `ADV-0242`. Jika tambahan itu dikeluarkan, urutan kontrol identik.
- Matematika: 54 payload inline identik dan berurutan. Sepuluh display identik
  secara matematis setelah dua lokalisasi teks `for all` menjadi `untuk semua`.
  Semua hipotesis, kuantor, penutup berhingga, pilihan indeks, batas, dan
  inferensi kelengkapan lolos audit.
- Metadata TeX: satu label `thm:arzelaascoli` persis sama; satu catatan kaki dan
  dua URL `href` persis sama; entri indeks dilokalkan; kurung kurawal aktif
  seimbang tanpa underflow.
- Bahasa Indonesia: PASS. Prosa, catatan kaki, dan indeks alami; terminologi
  selaras dengan ledger; tidak ada residu prosa Inggris selain nama diri,
  eponim, URL, label, dan pengenal TeX.
- Ledger koreksi sesudah audit: 242 peristiwa unik; tepat satu `ADV-0242` dan
  nol `ADV-0243`.

Sasaran hidup lengkap sesudah U281 adalah 189.645 byte, SHA-256
`8ac63e0faaa3143b49185933e840f72faf7c9a6cf0efdf89699cc7c7a64bf7fc`.
Tidak ada penulis yang dihubungi.
