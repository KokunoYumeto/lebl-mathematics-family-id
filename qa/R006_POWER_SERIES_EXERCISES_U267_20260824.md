# QA R006 U267 — latihan deret pangkat dan teorema identitas

Tanggal: 2026-08-24  
Status: **lulus**

## Batas dan identitas

- Sumber: `source/ra-v6.3/ch-approximate.tex` baris mentah 1632–1768
  inklusif, 137 baris / 4.168 byte UTF-8 LF, SHA-256
  `63ffcfaab0e5f3e24bc84514b80d2876d99b33e6bed5625a028b97aaf8b9d4c0`.
- Target: `translation/ra/ch-approximate.tex` baris mentah 1631–1768
  inklusif, 138 baris / 4.507 byte UTF-8 LF, SHA-256
  `039b73b85b51a45711ef2b72da12135e2e13cb658d2204d945cdf65e472948c4`.
- Berkas target hidup sesudah unit: 184.531 byte, SHA-256
  `b4afcb1ab5992d5fea33c3acfe68d2e3b5b6a9831acbd2814b7af33ff1d06b86`.
- Unit: `ra.v2.functions-as-limits.power-series-analytic.exercises`.
- Batas berikutnya: sumber baris 1770 / target baris 1770,
  `\sectionnewpage`, lalu Bagian *Complex exponential and trigonometric
  functions* pada sumber 1771 / target 1771.

## QA struktur dan bahasa

- Kesebelas lingkungan `exercise`, dua lingkungan `enumerate`, empat `\item`,
  empat lingkungan `equation*`, satu lingkungan `cases`, dua petunjuk
  pemenggalan halaman, dan 13 baris komentar dipertahankan serta seimbang.
- Urutan 189 perintah TeX, seluruh komentar/penanda MathBook XML, urutan
  lingkungan, 85 blok matematika, dan 85 pasang kurung kurawal cocok setelah
  hanya tiga `\text{if}` diterjemahkan serta dua klarifikasi terdeklarasi
  dinormalisasi.
- Tidak ada label atau referensi pada sumber maupun target. Tidak ada solusi
  sumber yang dapat hilang atau berubah status.
- Tidak ada residu Inggris yang tampak bagi pembaca, `U+FFFD`, `??`, mojibake,
  atau perubahan urutan latihan. Bahasa Indonesia dinilai alami dan konsisten
  oleh dua audit independen.

## Audit matematika

Semua 17 tugas/subsoal diperiksa ulang: kedua urutan penjumlahan bertanda
memberi 0 dan 2; fungsi $1/(1+x^2)$ analitik real dengan jari-jari 1 di titik
asal; penerapan teorema identitas, faktorisasi titik nol, batas turunan,
koefisien binomial umum, perpanjangan bernilai real, dan taksiran cakram satuan
semuanya benar setelah dua koreksi berikut.

- `LEBL-ID-ADV-0228`: sumber menghilangkan hipotesis bahwa fungsi seluruh
  tersebut bukan fungsi nol. Target menambahkannya; tanpa itu $f\equiv0$
  merupakan kontra-contoh langsung terhadap klaim berhingga banyak titik nol.
- `LEBL-ID-ADV-0229`: sumber tidak menyatakan domain lokal $h(x)=f(x)$ dan
  $g(y)=-if(iy)$. Target membatasi $x,y$ real agar cukup dekat dengan 0 serta
  memenuhi $x\in U$ dan $iy\in U$, tepat yang dijamin oleh keterbukaan $U$ dan
  diperlukan untuk turunan di titik asal.

Kedua koreksi diaudit independen dan dinyatakan cukup, tanpa mengubah formula
tampil, kesimpulan yang dimaksud, atau topologi latihan. `LEBL-TERM-0647`–
`LEBL-TERM-0651` mengikat fungsi nol, titik nol fungsi, koefisien binomial umum,
bernilai real, dan cakram satuan. Tidak ada kontak dengan penulis.

Identifikasi edisi: **OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi
pengguna; semua kredit sumber dan manusia dipertahankan.
