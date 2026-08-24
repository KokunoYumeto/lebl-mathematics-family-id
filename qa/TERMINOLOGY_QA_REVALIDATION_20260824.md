# Revalidasi terminologi matematika Bahasa Indonesia — 2026-08-24

Status: **LULUS**. Pemeriksaan terbatas tidak menemukan naskah arXiv yang isi
matematikanya berbahasa Indonesia dan menyediakan sumber TeX yang relevan.
Sesuai rute pengganti yang diminta, dua PDF berbahasa Indonesia dari repositori
universitas diperiksa langsung. Sumber Analisis Kompleks mengonfirmasi
terminologi R006 yang sedang dipakai dan terminologi untuk unit berikutnya.
Tidak ada pilihan utama atau teks terjemahan yang perlu diubah.

## Pencarian arXiv yang dibatasi

API/pencarian arXiv diperiksa dengan frasa bidang `persamaan diferensial`,
`fungsi analitik`, `analisis kompleks`, `deret pangkat`, dan `jari-jari
konvergensi`; pencarian kategori matematika juga dikombinasikan dengan
`Indonesia` dan `Bahasa Indonesia`. Frasa bidang persis menghasilkan nol
entri. Hasil yang lebih luas merupakan karya berbahasa Inggris atau karya
bahasa/NLP, bukan prosa matematika Bahasa Indonesia. Karena itu tidak ada paket
sumber arXiv baru yang dapat dipakai sebagai bukti terminologi. Pernyataan ini
hanya melaporkan pencarian terbatas tersebut, bukan klaim universal mengenai
seluruh isi arXiv.

Bukti arXiv terdahulu juga tetap sah: paket sumber arXiv:2008.00182 telah
diunduh dan TeX-nya diperiksa pada audit 2026-08-22/23, tetapi isi sebenarnya
berbahasa Inggris. Ia tetap ditolak sebagai bukti istilah Bahasa Indonesia.

## Sumber pengganti utama: Analisis Kompleks

- Zetriuslita, *Mudah Memahami Analisis Kompleks*, Fahma Media, cetakan
  pertama, Agustus 2014; bantuan penerbitan Universitas Islam Riau.
- Repositori institusi:
  <https://repository.uir.ac.id/18176/1/Buku%20Analisis%20Kompleks.pdf>.
- Salinan audit lokal:
  `qa/terminology_qa/arxiv_20260824/UIR_Buku_Analisis_Kompleks.pdf`;
  2.672.941 byte; 162 halaman; SHA-256
  `d859bcb7dac4b3fffa740d1154df212db9751622f22923c9d218e152c3773dcf`.
- Ekstraksi teks berhalaman:
  `qa/terminology_qa/arxiv_20260824/UIR_Buku_Analisis_Kompleks.txt`;
  278.288 byte; SHA-256
  `6af8106c3ca43d0ac626721eab0176bce8f49ca7bf78fafdb9b8e7207ebe2519`.
- Halaman PDF 40, 41, 73, 131, dan 157 dirender dan diperiksa visual. Halaman
  tersebut memperlihatkan langsung fungsi eksponen/trigonometri, rumus Euler,
  fungsi analitik dan lingkungan, deret Taylor sebagai deret pangkat, serta
  latihan deret pangkat dan jari-jari konvergensi.

Hak cipta buku menyatakan pembatasan penggandaan. PDF dan render karena itu
hanya bukti QA lokal dan tidak boleh dimasukkan ke rilis Lebl.

## Sumber pengganti tambahan: persamaan diferensial

- Muhammad Ikhsan, *Penyelesaian Model Penelusuran Banjir Gelombang Difusi
  dengan Metode Lax-Friedrichs*, skripsi S1 Matematika, Universitas Bengkulu,
  2022; rekaman institusi <https://repository.unib.ac.id/id/eprint/13376/>.
- Salinan audit lokal:
  `qa/terminology_qa/arxiv_20260824/Ikhsan_2022_Flood_Routing_PDE_Finite_Difference.pdf`;
  3.109.112 byte; 70 halaman; SHA-256
  `23395c7677fc8efd9481bf8cb81d906900a0a9eeddfb230a8acfa5e1d8997158`.

Sumber ini hanya melengkapi bidang R007. Ia mengonfirmasi `persamaan
diferensial`, `persamaan diferensial biasa (PDB)`, `persamaan diferensial
parsial (PDP)`, `turunan`, `turunan parsial`, `deret Taylor`, `syarat awal`, dan
`syarat batas`. Ia bukan bukti untuk istilah khusus analisis kompleks.

## Perbandingan dengan edisi dan glosarium hidup

Artefak yang dibandingkan:

- `00_control/TERMINOLOGY.csv`: 651 baris data, 90.179 byte, SHA-256
  `3b77bdc0c4906d48dbd4ecb46844aec50ddc42533e364578cea34820e62c270a`;
- `translation/ra/ch-approximate.tex`: 184.531 byte, SHA-256
  `b4afcb1ab5992d5fea33c3acfe68d2e3b5b6a9831acbd2814b7af33ff1d06b86`.

Perhitungan teks hanya mencakup bagian Indonesia yang telah diterima sampai
baris target 1768; bagian Inggris yang belum diterjemahkan tidak dipakai untuk
putusan.

| Konsep | Pemakaian sumber Indonesia | Edisi/glosarium | Putusan |
|---|---|---|---|
| analytic function | `fungsi analitik`; juga `keanalitikan` | `fungsi analitik` (`LEBL-TERM-0257`), 14 kali dalam cakupan hidup | Sama; pertahankan. `keanalitikan` tetap bentuk nomina yang tepat bila konsep itu muncul. |
| neighborhood | `lingkungan` | `lingkungan` | Sama; pertahankan. |
| power series | `deret pangkat` | `deret pangkat` (`LEBL-TERM-0185`), 38 kali | Sama; pertahankan. |
| radius of convergence | `jari-jari konvergensi` | sama (`LEBL-TERM-0186`), 15 kali | Sama; pertahankan. |
| real/imaginary part | `bagian real`, `bagian imajiner` | sama (`LEBL-TERM-0621/0622`) | Sama; pertahankan. |
| exponential function | `fungsi pangkat (eksponen)` dan `fungsi-fungsi eksponen` | `fungsi eksponensial` (`LEBL-TERM-0288`) | Varian lapangan nyata, tetapi tidak lebih tepat. Pertahankan `fungsi eksponensial`; gunakan `fungsi eksponen` hanya sebagai varian pencarian. |
| trigonometric function | `fungsi trigonometri` | unit berikutnya belum diterjemahkan | Gunakan `fungsi trigonometri`; bukti langsung mendukungnya. |
| Euler's formula | `rumus Euler` | unit berikutnya belum diterjemahkan | Gunakan `rumus Euler`; bukti langsung mendukungnya. |
| unit circle / unit disc | `lingkaran satuan` untuk *unit circle* | `lingkaran satuan` untuk circle; `cakram satuan` (`LEBL-TERM-0651`) untuk disc | Tidak ada konflik: lingkaran dan cakram berbeda. Pertahankan keduanya. |
| zero function / zero of a function | tidak terwakili | `fungsi nol`; `titik nol fungsi` (`LEBL-TERM-0647/0648`) | Sumber tidak dapat menilai istilah ini; pertahankan berdasarkan makna dan konsistensi internal. |
| differential equation | `persamaan diferensial`, PDB, PDP | sama (`LEBL-TERM-0307/0308/0495`) | Sama; pertahankan untuk R007. |
| linear | sumber tambahan memakai `linier` | edisi konsisten memakai `linear` | Varian ortografis; satu skripsi tidak membenarkan penggantian global. Pertahankan `linear`. |
| initial/boundary condition | `syarat awal`, `syarat batas`; juga `nilai awal` untuk nilai | `syarat awal` sudah dipilih | Pertahankan beda makna antara nilai dan syarat; pakai `syarat batas` ketika konsep itu masuk R007. |

## Putusan dan propagasi

Semua istilah yang relevan dengan bahan R006 yang telah diterjemahkan cocok
dengan penggunaan buku Analisis Kompleks, atau berbeda hanya sebagai varian
yang tidak lebih tepat. Karena itu tidak ada penggantian glosarium dan tidak
ada propagasi teks. Untuk unit berikutnya, `fungsi eksponensial`, `fungsi
trigonometri`, dan `rumus Euler` merupakan pilihan yang telah diputuskan;
matematika, konsistensi korpus, dan bukti lapangan mendukungnya.

Identifikasi produksi persis `OpenAI Codex gpt-5.6-sol, Ultra` sudah tercantum
di `repository/README.md`, driver pembaca R006, dan manifest rilis U330, sambil
mempertahankan Jiří Lebl sebagai penulis sumber serta seluruh kredit manusia.
Tidak ada penulis yang dihubungi dan tidak ada sumber bukti yang dipublikasikan
ulang.
