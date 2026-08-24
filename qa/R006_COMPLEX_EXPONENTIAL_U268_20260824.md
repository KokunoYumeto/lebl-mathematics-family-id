# R006 U268 — eksponensial kompleks

Status: **LULUS / diterima**  
Tanggal: 2026-08-24  
Unit: `ra.v2.functions-as-limits.complex-exponential.opening`

## Batas dan identitas

- Sumber: `source/ra-v6.3/ch-approximate.tex`, baris mentah 1770–1862
  inklusif; pembukaan bagian *Complex exponential and trigonometric
  functions* dan subbagian lengkap *The complex exponential*.
- Irisan sumber UTF-8/LF: 93 baris, 3.393 byte, SHA-256
  `56efbabe75d1862fc13e3b16a52b5f8ef341308135e8bd5307fee16efd638d63`.
- Target: `translation/ra/ch-approximate.tex`, baris mentah 1770–1862
  inklusif.
- Irisan target UTF-8/LF: 93 baris, 3.608 byte, SHA-256
  `ee982d44d0f539c05f512eb27ddba4192c6aa1a9e6bea705e9e18d3883dd85f7`.
- Target R006 penuh setelah penerimaan: 184.745 byte, SHA-256
  `ea35f4bbbc3bb4a00b780339e59b45b57eca2a539da93ccc386f010c5c99cbfa`.

Konvensi hash irisan: baris dipilih secara inklusif, digabung dengan LF,
diakhiri satu LF, dan dikodekan UTF-8 tanpa BOM.

## Pemeriksaan struktur dan matematika

Pemeriksaan deterministik dan dua audit independen lulus:

- 93/93 baris; 80/80 perintah TeX; 18/18 token lingkungan dalam urutan yang
  sama; enam blok `equation*`; dua label; enam pemanggilan referensi; satu
  komentar; 42/42 rentang matematika sebaris; kurung kurawal seimbang 65/65.
- Semua 48 ekspresi matematika dipertahankan. Satu-satunya perubahan tekstual
  di dalam matematika ialah `\text{for all }` menjadi
  `\text{untuk setiap }`.
- Definisi deret seluruh untuk (E(z)), kesamaan dengan eksponensial real,
  definisi (e^z), ketidaknolannya, invers (e^{-z}), pangkat bilangan bulat,
  dan ekspansi deret pangkat di sembarang pusat (a\in\mathbb C) semuanya
  tepat.
- Bukti hukum eksponen mempertahankan kedua penerapan teorema identitas:
  tetapkan (y\in\mathbb R) lalu lanjutkan (x\) menjadi (z\in\mathbb C);
  kemudian tetapkan (z\in\mathbb C) dan lanjutkan (y\) menjadi
  (w\in\mathbb C).
- Label/referensi `sec:complexexp`, `cor:powerseranalytic`,
  `vI-sec:logandexp`, `sec:logandexp`, `fig:complexexpgraphs`, dan
  `thm:identityanalytic`, serta `\glsadd{not:complexexp}` dan identitas aset
  `real_imag_exp`, tetap utuh.

## Aksesibilitas, bahasa, dan terminologi

Teks alternatif gambar memuat seluruh fakta sumber: kedua permukaan
sinusoidal pada arah (y), amplitudo membesar bersama (x), osilasi tak
terlihat pada skala gambar untuk (x<0), pergeseran gelombang panel kanan,
irisan (y=0) panel kiri sama dengan (e^x), irisan panel kanan bernilai nol,
dan irisan tersebut ditandai tebal. Audit independen menemukan ambiguitas panel
pada terjemahan awal; frasa itu diperbaiki menjadi `grafik kiri` dan `grafik
kanan`, lalu audit ulang lulus. Batas keterangan gambar tetap persis:
(x\in[-4,4]), (y\in[-6,6]), dan sumbu vertikal
([-e^4,e^4]\approx[-54.6,54.6]).

Audit terminologi lapangan pada
`qa/terminology_qa/ARXIV_OR_FALLBACK_TERMINOLOGY_AUDIT_20260824.md`
mendukung pilihan unit ini. Tambahkan `LEBL-TERM-0652` sampai
`LEBL-TERM-0658`: `eksponensial kompleks`, `eksponensial real`, `arah real`,
`arah imajiner`, `berosilasi`, `grafik permukaan`, dan `hukum eksponen`.
Tidak ada residu Inggris yang menghadap pembaca; `proof` hanya nama lingkungan
LaTeX. Tidak diperlukan koreksi sumber atau entri adverse baru.

## Putusan

Unit diterima sebagai R006 U268 / unit manifest global U333. Lanjutkan pada
baris sumber dan target 1863, subbagian *Trigonometric functions and \(\pi\)*.
Provenans produksi persis `OpenAI Codex gpt-5.6-sol, Ultra` tetap hadir pada
driver, metadata repositori, dan metadata rilis; seluruh kredit sumber dan
kontributor manusia dipertahankan. Tidak ada penulis yang dihubungi.
