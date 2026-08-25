# R006 U277 — pembukaan ekuikontinuitas dan contoh keterbatasan

Status: **PASS; diterima sebagai unit terjemahan kontigu**  
Tanggal: 2026-08-25  
Provenance runtime: `OpenAI Codex gpt-5.6-sol, Ultra`

## Batas dan identitas

- ID stabil:
  `ra.v2.equicontinuity-arzela-ascoli.opening.pointwise-uniform-boundedness-counterexamples`
- Sumber beku: `source/ra-v6.3/ch-approximate.tex`, raw lines 2542–2617
  inclusive; 76 LF lines; 2.538 byte; SHA-256
  `c993189f77c71003fe127dbc458a0d82910b4710add80e5553d7a578e0150c2b`.
- Sasaran: `translation/ra/ch-approximate.tex`, raw lines 2552–2627
  inclusive; 76 LF lines; 2.780 byte; SHA-256
  `c4a037c2adf5914ba6d920df08adaf51eba9e43ed4e04ce10754a1c5e89c9266`.
- Batas berikutnya: source raw line 2619 / target raw line 2629,
  paragraf pembuka domain terhitung dan argumen diagonal.

## Cakupan

Unit memuat judul Bagian 11.6, motivasi analog Bolzano--Weierstrass,
definisi *terbatas titik demi titik* dan *terbatas seragam*, hubungan dengan
norma seragam pada domain kompak, serta tiga contoh yang membedakan
keterbatasan dan konvergensi titik demi titik/seragam.

Istilah baru yang diterima:

- `LEBL-TERM-0723`: *equicontinuity* → `ekuikontinuitas`;
- `LEBL-TERM-0724`: *pointwise bounded* → `terbatas titik demi titik`;
- `LEBL-TERM-0725`: *uniformly bounded* → `terbatas seragam`.

Pilihan itu selaras dengan penggunaan bidang Indonesia yang terdokumentasi
dalam tulisan Sufri mengenai teorema Arzelà--Ascoli di Jurnal Sainmatika
Universitas Jambi. Ledger istilah hidup kini memuat 725 baris, 103.486 byte,
SHA-256
`9b49ecbe667a8fd7ac30232afcfefa8c5dd4b101e2f68b4fb7c86e2534d7f296`.

## QA independen

- Audit struktur: PASS. Urutan 89 token perintah/simbol kontrol identik;
  14 peristiwa lingkungan identik dan seimbang; `sec:arzelaascoli` terjaga;
  nol rujukan/sitasi; nol komentar; delta kurung kurawal 0/0.
- Audit matematika: PASS. Seluruh hipotesis, kuantor, implikasi, tiga contoh,
  titik kritis `1/n^2`, maksimum `n/2`, estimasi, dan limit dipertahankan tanpa
  penguatan atau pelemahan.
- Matematika inline: 29/29 payload identik dan berurutan; display 3/3.
- Audit Bahasa Indonesia: PASS; tidak ada penambahan, penghilangan, atau
  residu prosa Inggris. Nama diri dan identifier TeX dipertahankan.
- Audit sumber: tidak ada cacat berkeyakinan tinggi dan tidak ada koreksi
  sumber baru. Catatan ekspositori opsional tidak diperlakukan sebagai cacat.

Sasaran hidup lengkap sesudah U277 adalah 188.777 byte, SHA-256
`9bbd37532b79e5b8c392f10501d8c9b3c67a7ceeddfafd12342c50eb8bdff587`.
Build pembaca baru ditangguhkan sampai batas semantik yang cukup besar;
pembaca publik U361 tetap benar karena cutoff-nya berakhir sebelum unit ini.
Tidak ada penulis yang dihubungi.
