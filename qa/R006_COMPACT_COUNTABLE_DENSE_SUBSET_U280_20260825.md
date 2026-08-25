# R006 U280 — subhimpunan rapat terhitung pada ruang metrik kompak

Status: **PASS; diterima sebagai unit terjemahan kontigu**  
Tanggal: 2026-08-25  
Provenance runtime: `OpenAI Codex gpt-5.6-sol, Ultra`

## Batas dan identitas

- ID stabil:
  `ra.v2.equicontinuity-arzela-ascoli.compact-metric-space-countable-dense-subset`.
- Sumber beku: `source/ra-v6.3/ch-approximate.tex`, raw lines 2740–2762
  inclusive; 23 LF lines; 948 byte; SHA-256
  `13558c99d6a7a996f07320cc65cde0370a8daba05339c043bd3ebe03fa597e12`.
- Sasaran: `translation/ra/ch-approximate.tex`, raw lines 2749–2771
  inclusive; 23 LF lines; 1.057 byte; SHA-256
  `06f2c79fed310390a2f89ecabf7b751d88465c0badb47e947b6449c8998913c4`.
- Batas berikutnya: source raw line 2764 / target raw line 2773, jembatan
  menuju teorema Arzelà--Ascoli dan pernyataan teoremanya.

## Cakupan dan istilah

Unit mempertahankan proposisi bahwa setiap ruang metrik kompak memuat
subhimpunan rapat yang terhitung. Pembuktian lengkap melalui penutup berhingga
oleh bola berjari-jari `1/n`, gabungan terhitung dari pusat-pusatnya, dan
argumen ketertutupan/kepadatan dipertahankan.

`LEBL-TERM-0729` mengikat *countable dense subset* ke `subhimpunan rapat yang
terhitung`, selaras dengan penggunaan yang sudah ada dalam R006
`ch-metric.tex`; `himpunan padat terhitung` dipertahankan sebagai varian, bukan
bentuk pilihan.

## QA independen

- Struktur: PASS. Urutan 34 kontrol TeX identik; delapan peristiwa lingkungan
  identik dan seimbang (`prop`, `proof`, dan dua `equation*`).
- Matematika: 19 payload inline dan dua display identik byte demi byte dan
  berurutan. Semua kuantor, indeks `k_n`, penutup berhingga, gabungan yang
  mendefinisikan `D`, pemilihan `n`, pertidaksamaan radius, inklusi bola, dan
  kesimpulan ketertutupan/kepadatan terjaga.
- Tidak ada label, rujukan, sitasi, indeks, komentar, atau catatan kaki.
  Kurung kurawal 32/32 seimbang tanpa kedalaman prefix negatif.
- Bahasa Indonesia: PASS sesudah memperhalus dua calque menjadi `terdapat
  sejumlah berhingga bola` dan `titik-titik ... dalam jumlah berhingga`.
  Tidak ada residu prosa Inggris.
- Inferensi akhir sah karena simetri metrik mengubah
  `x \in B(x_{n,j},\epsilon)` menjadi fakta bahwa setiap lingkungan
  `epsilon` dari `x` memuat `x_{n,j} \in D`. Tidak ada cacat sumber dan tidak
  ada koreksi matematika.

Sasaran hidup lengkap sesudah U280 adalah 189.278 byte, SHA-256
`58d998bc769cc24ee1ffaf64448567b7de1ffd78efb11ac6a5b93f4f0a029376`.
Tidak ada penulis yang dihubungi.
