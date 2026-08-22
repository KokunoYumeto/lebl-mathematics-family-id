# QA terminologi penggunaan bidang Bahasa Indonesia — 2026-08-22

## Tujuan dan batas

Pemeriksaan satu kali ini membandingkan istilah edisi R006 dengan penggunaan
nyata dalam bahan analisis real berbahasa Indonesia. Pemeriksaan ini tidak
mengubah isi matematika, identitas karya sumber, atau kredit Jiří Lebl. Sumber
luar digunakan sebagai bukti terminologi saja dan tidak dimasukkan ke paket
rilis pembaca.

## Pemeriksaan arXiv

Pencarian terbatas pada arXiv untuk naskah matematika berbahasa Indonesia yang
relevan dengan analisis real, integral Riemann, Teorema Green, kalkulus
multivariabel, dan ukuran Jordan tidak menemukan naskah yang memenuhi dua
syarat sekaligus: isi utama berbahasa Indonesia dan sumber TeX yang dapat
diunduh.

Kandidat terdekat adalah:

- E. Septiati dan N. Karjanto, *Challenges in teaching Real Analysis classes
  at the University of PGRI, South Sumatra, Indonesia*, arXiv:2008.00182,
  <https://arxiv.org/abs/2008.00182>.
- Paket sumber yang diunduh:
  `arxiv-2008.00182-source`, 7.868 byte, SHA-256
  `c11869e512de4b3e1e8d73a5551669d5090316a981bb17292dd01e3c560a1ec7`.
- TeX hasil dekompresi: `arxiv-2008.00182.tex`, 21.640 byte, SHA-256
  `a54893466f4297b1c90361dc588095c8a229e56d9cca6bc35127c51a67545e74`.

Pemeriksaan langsung terhadap judul, abstrak, semua bagian, dan isi TeX
menunjukkan bahwa naskah tersebut ditulis dalam bahasa Inggris. Lokasi dan
afiliasinya berada di Indonesia, tetapi hal itu tidak menjadikannya bukti
terminologi matematika berbahasa Indonesia. Kandidat ini karena itu ditolak
secara eksplisit sebagai bukti istilah.

## Sumber pengganti yang diperiksa langsung

Karena arXiv tidak menghasilkan sumber yang sesuai, pemeriksaan beralih ke
modul universitas berbahasa Indonesia:

- Prof. Dr. Supama, M.Si., *Beberapa Konsep Dasar*, Modul 1 dalam MATA4217
  Analisis I, Edisi 2, Universitas Terbuka, berkas resmi
  <https://pustaka.ut.ac.id/lib/wp-content/uploads/pdfmk/MATA421702-M1.pdf>.
- Salinan bukti lokal: `universitas-terbuka-MATA421702-M1.pdf`, 1.384.321
  byte, 60 halaman, SHA-256
  `6d55ddc986abb1a6df5513d6d5db88ff86f6709fe8358e14d8a7ae2850485412`.
- PDF diperiksa melalui ekstraksi teks berhalaman dan render visual halaman
  1, 2, 6, dan 10. Sumber tidak diperlakukan sebagai bahan berlisensi terbuka;
  salinan ini hanya menjadi bukti audit terminologi dan tidak akan disertakan
  dalam rilis edisi Lebl.

Istilah yang teramati secara langsung meliputi `himpunan kosong`, `himpunan
bagian sejati`, `hasil kali silang (Cartesian product)`, `daerah asal/daerah
definisi (domain)`, `daerah kawan (co-domain)`, `daerah hasil (range)`, `fungsi
injektif`, `fungsi surjektif`, `fungsi bijektif`, `fungsi invers`, `kardinal
suatu himpunan`, `himpunan terhitung`, dan `himpunan tak terhitung`. Definisi
1.10.1 pada halaman cetak 1.42 (halaman PDF 42) juga memberikan pasangan
bilingual langsung `denumerabel (terhitung tak hingga)` dan mendefinisikan
`enumerasi`. Ragam
pembuktian formalnya juga konsisten dengan edisi ini: `untuk setiap`,
`terdapat`, `sedemikian sehingga`, `maka`, dan `Diberikan`.

## Rekonsiliasi dengan glosarium R006

| Konsep | Sebelum QA | Bukti lapangan | Keputusan |
|---|---|---|---|
| Cartesian product | `produk Kartesius` | UT memakai `hasil kali silang`; publikasi matematika perguruan tinggi Indonesia lazim memakai `hasil kali Kartesius` | Ubah pilihan utama menjadi `hasil kali Kartesius`; simpan `produk Kartesius` sebagai varian; tolak `hasil kali silang` dalam edisi ini karena bertabrakan dengan istilah *vector cross product*. |
| element | `elemen`, varian `anggota` | UT memakai `anggota` | Pertahankan pilihan dan varian; bukti ditambahkan. |
| empty set | `himpunan kosong` | Sama | Pertahankan; bukti ditambahkan. |
| proper subset | `himpunan bagian sejati` | Sama | Pertahankan; bukti ditambahkan. |
| domain | `domain` | `daerah asal`; `daerah definisi` | Pertahankan `domain` sebagai bentuk ringkas yang mapan; tambahkan kedua bentuk penjelas sebagai varian. |
| range | `daerah hasil` | Sama | Pertahankan; bukti ditambahkan. |
| codomain | `kodomain` | `daerah kawan` | Pertahankan `kodomain`; tambahkan `daerah kawan` sebagai varian penjelas. |
| injective/surjective/bijective | `injektif`; `surjektif`; `bijektif` | Sama | Pertahankan; bukti ditambahkan. |
| inverse function | `fungsi invers` | Sama | Pertahankan; bukti ditambahkan. |
| cardinality | `kardinalitas` | `kardinal suatu himpunan` | Pertahankan `kardinalitas` untuk sifat; tambahkan `kardinal` untuk konteks bilangan kardinal. |
| countably infinite | `tak berhingga terhitung` | `denumerabel (terhitung tak hingga)` dalam definisi formal bilingual | Ubah pilihan utama menjadi `terhitung tak hingga`; simpan `denumerabel` dan bentuk lama sebagai varian. |
| countable/uncountable | `terhitung`; `tak terhitung` | Sama | Pertahankan dan teguhkan penolakan `tercacah`/`tak tercacah` pada edisi ini. |
| enumeration | `enumerasi` | Sama dalam definisi formal | Pertahankan; bukti ditambahkan. |
| composition of functions | `komposisi fungsi` | `fungsi komposisi` | Pertahankan pilihan utama; tambahkan bentuk sumber sebagai varian. |

## Perubahan dan propagasi

`LEBL-TERM-0032` diubah menjadi `hasil kali Kartesius`. Tiga kemunculan lama
dipropagasikan di `translation/ra/ch-vol1-intro.tex` dan
`translation/ra/notations.tex`. `LEBL-TERM-0057` diubah menjadi `terhitung tak
hingga` berdasarkan definisi bilingual langsung, dan 12 kemunculan lama
dipropagasikan di `translation/ra/ch-vol1-intro.tex` dan
`translation/ra/ch-real-nums.tex`. Entri glosarium terkait diperluas dengan
bukti dan varian yang teramati. Tidak ada alasan semantis atau konvensi yang cukup
kuat untuk mengganti 125 kemunculan `domain`, lima kemunculan `kodomain`, atau
34 kemunculan `kardinalitas`; perubahan global tersebut justru akan mengurangi
keringkasan dan konsistensi tanpa memperbaiki makna.

Putusan: dua koreksi istilah dipropagasikan; semua pilihan utama lain yang
dibandingkan lulus QA, dengan bukti dan varian diperkuat secara eksplisit.
