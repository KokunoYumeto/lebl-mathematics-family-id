# R006 U278 — subbarisan diagonal pada domain terhitung

Status: **PASS; diterima sebagai unit terjemahan kontigu**  
Tanggal: 2026-08-25  
Provenance runtime: `OpenAI Codex gpt-5.6-sol, Ultra`

## Batas dan identitas

- ID stabil:
  `ra.v2.equicontinuity-arzela-ascoli.countable-domain-diagonal-subsequence`.
- Sumber beku: `source/ra-v6.3/ch-approximate.tex`, raw lines 2619–2659
  inclusive; 41 LF lines; 1.785 byte; SHA-256
  `c50ac6870300c79b387dc02523fa9490673247bf0d6e313a05396300a47a9bed`.
- Sasaran: `translation/ra/ch-approximate.tex`, raw lines 2629–2669
  inclusive; 41 LF lines; 1.974 byte; SHA-256
  `c18c46e64933f4d4411984980095258cdf99a4fbef4c93e10b7818c6ecbcbecf`.
- Batas berikutnya: source raw line 2661 / target raw line 2671, transisi
  menuju definisi ekuikontinuitas seragam.

## Cakupan dan istilah

Unit mempertahankan proposisi bahwa barisan fungsi yang terbatas titik demi
titik pada domain terhitung memiliki subbarisan yang konvergen titik demi
titik, beserta konstruksi subbarisan bersarang dan pemilihan diagonal
`\{f_{k,k}\}`. Kasus hingga, kasus terhitung tak hingga, semua kuantor, serta
argumen ekor barisan dipertahankan.

Istilah baru `LEBL-TERM-0726`, *diagonal argument* → `argumen diagonal`,
dibedakan dari *Cantor diagonalization* → `diagonalisasi Cantor`. Istilah
`terhitung`, `terhitung tak hingga`, `enumerasi`, `subbarisan`, `ekor`,
`terbatas titik demi titik`, dan `konvergen titik demi titik` mengikuti ledger
hidup.

## QA independen

- Struktur: PASS. Kedua slice memiliki 41 baris LF. Urutan 74 token
  perintah/kontrol identik, dengan SHA-256 urutan
  `889f40df71c5c26d5442c7a1d16be1a2f7d16fc8cededfd9b310a2511d1d7813`.
- Lingkungan: empat peristiwa identik (`prop` dan `proof`); label
  `prop:subsequenceoncountableX` terjaga; nol rujukan, sitasi, perintah indeks,
  komentar, dan matematika display.
- Matematika inline: 32/32 payload identik dan berurutan; SHA-256 urutan
  `21518d8bf0d9f21edc3ff729bc5d7fda0800fc38dd5416a7c06ddfbdfd817f32`.
- Kurung kurawal struktural: 45 buka / 45 tutup pada kedua slice, seimbang
  tanpa prefix negatif.
- Audit matematika dan Bahasa Indonesia: PASS. Hipotesis, kesimpulan,
  subbarisan bersarang, pemilihan diagonal, kuantor, dan pemisahan kasus
  dipertahankan tanpa penguatan atau pelemahan; tidak ada residu prosa Inggris.

Sumber memakai enumerasi tak hingga sebelum kemudian menangani kasus hingga.
Ini hanya kelonggaran ekspositori ringan dan tidak mengganggu argumen; sasaran
mempertahankannya, sehingga tidak dicatat sebagai koreksi sumber.

Sasaran hidup lengkap sesudah U278 adalah 188.966 byte, SHA-256
`bf1ffaad1f7956eb16e633250d9294ef105d2a5be3c6d9a6e40fd876f9f766d3`.
Tidak ada penulis yang dihubungi.
