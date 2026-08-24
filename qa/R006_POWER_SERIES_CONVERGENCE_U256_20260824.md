# QA R006 U256 — jari-jari konvergensi

Tanggal: 2026-08-24  
Status: **lulus; unit diterima secara struktural**

## Batas dan identitas

- Sumber: source/ra-v6.3/ch-approximate.tex baris mentah 1104–1168,
  2.523 byte UTF-8/LF, SHA-256
  d70fc78296466bcd89028b0920dba965d39e08ccb6eba6cfe03711536f2e3015.
- Target: translation/ra/ch-approximate.tex baris mentah 1099–1163,
  2.671 byte UTF-8/LF, SHA-256
  ef224e06310f36d95c8aef4ba22fa31e4e4da9a2efbe19884a70c0c4838c76cb.
- Isi: pembukaan subbagian, proposisi jari-jari konvergensi, gambar dan teks
  alternatifnya, serta bukti lengkap sebagaimana tercetak pada sumber.
- Batas berikutnya: sumber 1170 / target 1165.

## QA deterministik dan independen

- 65/65 baris; 91/91 perintah TeX dalam urutan identik.
- 12/12 token lingkungan dan 27/27 rentang matematika sebaris identik.
- Dua blok matematika tampil identik; 59/59 pasangan kurung kurawal dan
  54/54 pembatas dolar.
- Ketujuh identitas referensi/label/aset terlindungi identik, termasuk
  vI-sec:moreonseries, vI-prop:powerserrealradius,
  fig:radiusconvcomplex, dan aset radiusconvcomplex.
- Arti ketiga kasus \(\rho\), konvergensi mutlak, bola tertutup, dan seluruh
  detail spasial serta label pada teks alternatif gambar dipertahankan.
- Istilah mengikuti ledger: deret pangkat, jari-jari konvergensi,
  konvergen mutlak, konvergen secara seragam, bola tertutup, cakram,
  dan jumlah parsial.
- Audit dwibahasa independen: **PASS** untuk teks TeX utama. Residu prosa
  Inggris, mojibake, dan karakter pengganti pada teks utama: nol. Audit visual
  U330 kemudian menemukan label Inggris di dalam overlay Xfig; pelokalan dan
  gerbang build ulangnya dicatat terpisah dalam
  `qa/R006_RADIUS_CONVERGENCE_FIGURE_LOCALIZATION_U256_20260824.md`.

## Cacat sumber yang dipertahankan

LEBL-ID-ADV-0226 mencatat bahwa baris sumber 1158–1167 hanya membatasi jumlah
parsial penuh. Itu membuktikan keterbatasan seragam, bukan konvergensi seragam;
argumen yang lengkap memerlukan estimasi ekor atau pemanggilan uji-M
Weierstrass. Proposisinya benar. Edisi ini mempertahankan bukti sumber tanpa
menyisipkan perbaikan diam-diam. Tidak ada kontak dengan penulis.

Identifikasi edisi tetap **OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi
pengguna; Jiří Lebl dan semua kontributor manusia tetap dikreditkan.
