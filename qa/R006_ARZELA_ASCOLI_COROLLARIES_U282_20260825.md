# R006 U282 — korolari Arzelà--Ascoli

Status: **PASS; diterima sebagai unit terjemahan kontigu**  
Tanggal: 2026-08-25  
Provenance runtime: `OpenAI Codex gpt-5.6-sol, Ultra`

## Batas dan identitas

- ID stabil:
  `ra.v2.equicontinuity-arzela-ascoli.corollaries.compact-set-and-derivative-bound`.
- Sumber beku: `source/ra-v6.3/ch-approximate.tex`, raw lines 2874–2913
  inclusive; 40 LF lines; 1.479 byte; SHA-256
  `64f22a6e86c2a396829a74c4aed1ab2d2d94abe353c0cf99cb329bc1c4c9731b`.
- Sasaran: `translation/ra/ch-approximate.tex`, raw lines 2883–2923
  inclusive; 41 LF lines; 1.670 byte; SHA-256
  `8b5d9e9b6bf3c6b68f57fa5550010955999d3ae68b087b19cf5470f928793050`.
- Batas berikutnya: source raw line 2915 / target raw line 2925, dimulai
  dengan penerapan klasik pada teorema eksistensi Peano, lalu operator integral
  kompak.

## Cakupan

Unit mempertahankan dua korolari. Korolari pertama menyatakan kekompakan suatu
himpunan tertutup, terbatas, dan ekuikontinu seragam dalam `C(X,\C)`, beserta
penjelasan melalui kekompakan sekuensial dan contoh pembanding bola satuan
tertutup. Korolari kedua mempertahankan hipotesis barisan fungsi diferensiabel
pada `[a,b]`, keterbatasan seragam turunannya, dan keterbatasan nilai pada satu
titik; kesimpulannya adalah keberadaan subbarisan yang konvergen seragam.

Pembuktian lengkap mempertahankan teorema nilai rata-rata, batas Lipschitz
bersama, ekuikontinuitas seragam, batas pada titik pangkal, keterbatasan seragam
seluruh barisan, dan penerapan Arzelà--Ascoli. Seluruh istilah memakai entri
ledger yang telah diterima; tidak diperlukan entri terminologi baru.

## Koreksi sumber terikat

`LEBL-ID-ADV-0243` mencatat satu koreksi P2 yang sempit. Korolari mendefinisikan
semua fungsi pada `[a,b]`, tetapi display sumber menguantifikasi `x,y \in X`
tanpa memperkenalkan `X` dalam korolari itu. Sasaran mengganti hanya pengenal
domain yang tak terdefinisi tersebut dengan `x,y \in [a,b]`. Batas turunan,
estimasi Lipschitz, dan semua payload matematika lain tidak berubah.

## QA independen

- Struktur: PASS. Sumber 40 LF lines dan sasaran 41 LF lines, masing-masing
  nol CR; baris ekstra tunggal adalah komentar pengikat `ADV-0243`.
- Urutan 55 kontrol TeX aktif identik. Aliran lingkungan identik: 10 peristiwa
  / lima pasangan seimbang (`cor` 2, `proof` 1, `equation*` 2).
- Dua puluh payload matematika inline identik dan berurutan. Dua display identik
  setelah satu lokalisasi teks `for all` menjadi `untuk semua` dan satu-satunya
  koreksi domain `X` menjadi `[a,b]`.
- Hyperlink TeX ke label `thm:arzelaascoli` dan teks Arzelà--Ascoli persis
  dipertahankan. Tidak
  ada label, rujukan biasa, catatan kaki, `href`, atau indeks. Kurung kurawal
  aktif 32/32 seimbang tanpa underflow.
- Matematika: PASS. Keterbatasan himpunan memberi keterbatasan titik demi titik;
  ketertutupan mempertahankan limit dalam himpunan; dalam ruang metrik,
  kekompakan sekuensial ekuivalen dengan kekompakan. Estimasi nilai rata-rata
  memberi konstanta Lipschitz bersama, sedangkan nilai pangkal dan
  `|x-x_0| <= b-a` memberi batas seragam.
- Bahasa Indonesia: PASS. Seluruh predikat dan kuantor terjaga; terminologi
  konsisten; tidak ada residu prosa Inggris selain eponim, simbol, dan pengenal
  TeX.

Ledger koreksi sesudah audit memuat 243 peristiwa unik, 218.621 byte, SHA-256
`8f7851552aa31496ce3c0743eb3124835399f2dcb9669920dee26e4a14f29049`.
Sasaran hidup lengkap sesudah U282 adalah 189.836 byte, SHA-256
`7c5ad3a2456a6d479dda1107e985ad64c0b5edc9d8a8086c2d0ea6a1364d92fc`.
Tidak ada penulis yang dihubungi.
