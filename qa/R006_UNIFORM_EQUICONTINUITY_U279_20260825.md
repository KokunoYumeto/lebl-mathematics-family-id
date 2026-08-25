# R006 U279 — ekuikontinuitas seragam dan kriteria limit seragam

Status: **PASS; diterima sebagai unit terjemahan kontigu**  
Tanggal: 2026-08-25  
Provenance runtime: `OpenAI Codex gpt-5.6-sol, Ultra`

## Batas dan identitas

- ID stabil:
  `ra.v2.equicontinuity-arzela-ascoli.uniform-equicontinuity.definition-and-uniform-limit-criterion`.
- Sumber beku: `source/ra-v6.3/ch-approximate.tex`, raw lines 2661–2738
  inclusive; 78 LF lines; 2.520 byte; SHA-256
  `6d7386a4066eb27100a6886a966f23c115cac297e395435af971c7fc79930209`.
- Sasaran: `translation/ra/ch-approximate.tex`, raw lines 2671–2748
  inclusive; 78 LF lines; 2.724 byte; SHA-256
  `f0f4cdde992b6f42fd21daffe23bd43133b9c654c6c8ba84fe4fc2bd87f67fea`.
- Batas berikutnya: source raw line 2740 / target raw line 2749, proposisi
  bahwa ruang metrik kompak mempunyai himpunan bagian rapat terhitung.

## Cakupan dan istilah

Unit memuat transisi dari domain terhitung, definisi ekuikontinuitas seragam,
ekuikontinuitas di suatu titik, ekuivalensinya pada domain kompak yang dirujuk
sebagai latihan, serta proposisi lengkap bahwa barisan fungsi kontinu yang
konvergen seragam pada ruang metrik kompak bersifat ekuikontinu seragam.
Pembuktian `epsilon/3`, keluarga berhingga, dan pertidaksamaan segitiga lengkap
dipertahankan.

Istilah baru:

- `LEBL-TERM-0727`: *uniform equicontinuity* → `ekuikontinuitas seragam`;
- `LEBL-TERM-0728`: *uniformly equicontinuous* → `ekuikontinu seragam`,
  dengan varian `ekuikontinu secara seragam`.

Pilihan ini mempertahankan bentuk bidang Indonesia `ekuikontinu` yang
didokumentasikan dalam tulisan Sufri mengenai Arzelà--Ascoli dan mengikuti
register ledger `kontinu seragam`, `konvergen seragam`, dan `terbatas seragam`.

## QA independen

- Struktur: PASS sesudah satu perbaikan struktur-prosa yang mengganti tambahan
  payload `$S$` dengan `himpunan itu`. Urutan 85 kontrol TeX aktif identik;
  14 peristiwa lingkungan identik; lima komentar `%mbxlatex` identik byte.
- Matematika inline: 35/35 payload identik dan berurutan. Empat display identik
  setelah hanya prosa `\text{...}` diterjemahkan.
- Dua hook `\myindex` dipertahankan dan dilokalkan. Tidak ada label, rujukan,
  sitasi, catatan kaki, atau aset.
- Kurung kurawal seimbang tanpa kedalaman prefix negatif. Tidak ada residu
  prosa Inggris yang menghadap pembaca.
- Audit matematika dan Bahasa Indonesia: PASS. Urutan kuantor, syarat
  kekompakan, konvergensi seragam, pemisahan `n \geq N` / `n > N`, keluarga
  berhingga, ketiga suku `epsilon/3`, dan kesimpulan dipertahankan tanpa
  penguatan atau pelemahan.
- Tidak ada cacat sumber berkeyakinan tinggi dan tidak ada koreksi sumber baru.

Sasaran hidup lengkap sesudah U279 adalah 189.169 byte, SHA-256
`6ce23c7245a82244648355a4c7471553b3500125896eb5f1f58ca3f91b786aeb`.
Tidak ada penulis yang dihubungi.
