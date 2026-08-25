# R006 U283 — penerapan Arzelà--Ascoli

Status: **PASS; diterima sebagai unit terjemahan kontigu**  
Tanggal: 2026-08-25  
Provenance runtime: `OpenAI Codex gpt-5.6-sol, Ultra`

## Batas dan identitas

- ID stabil:
  `ra.v2.equicontinuity-arzela-ascoli.applications.peano-and-compact-integral-operator`.
- Sumber beku: `source/ra-v6.3/ch-approximate.tex`, raw lines 2915–2945
  inclusive; 31 LF lines; 1.132 byte; SHA-256
  `caf3eabd6d7446aa3a6556b4cde084bcdc6dd638709ba052f7c9f36c36106a0d`.
- Sasaran: `translation/ra/ch-approximate.tex`, raw lines 2925–2955
  inclusive; 31 LF lines; 1.248 byte; SHA-256
  `b2bda41053827038571b9335218eda3223fbd8c1f03dc71faf3bfd2d7e693aa4`.
- Batas berikutnya: source raw line 2947 / target raw line 2957, awal
  `Exercises` Bagian 11.6.

## Cakupan dan istilah

Unit mempertahankan penerapan klasik korolari Arzelà--Ascoli pada pembuktian
teorema eksistensi Peano, termasuk rujukan latihan yang memasok hipotesis rinci.
Unit juga mempertahankan operator integral
`T(f)(x)=integral_0^1 f(t)k(x,t)dt`, linearitasnya pada `C([0,1],C)`, citra bola
satuan terbuka, kekompakan penutup citra, kekompakan relatif, dan definisi
operator kompak.

`LEBL-TERM-0731` mengikat *compact operator* ke `operator kompak`. Istilah ini
didukung secara langsung oleh kurikulum bilingual MA6131 Analisis Fungsional
ITB, yang memetakan *Compact Operator* ke *Operator Kompak*, serta oleh jurnal
matematika Indonesia yang memakai bentuk yang sama. Entri indeks
`relatively compact` dan `compact operator` dilokalkan menjadi `relatif kompak`
dan `operator kompak`.

## QA independen

- Struktur: PASS. Sumber dan sasaran masing-masing 31 baris LF, nol CR. Urutan
  41 kontrol TeX aktif identik. Aliran lingkungan identik: empat peristiwa / dua
  pasangan `equation*` yang seimbang.
- Empat payload matematika inline dan dua display identik byte demi byte.
  Rujukan latihan `exercise:peanoexistence` persis dipertahankan; tidak ada
  label atau rujukan lain. Dua `myindex` dilokalkan; kurung kurawal aktif 12/12
  seimbang; komentar 0/0.
- Matematika: PASS. Kernel kontinu pada persegi kompak mendefinisikan operator
  linear; citra bola satuan terbatas seragam dan ekuikontinu seragam, sehingga
  Arzelà--Ascoli memberi penutupan kompak. Ini tepat merupakan karakterisasi
  operator kompak yang dipakai sumber. Tidak ada koreksi sumber yang diperlukan.
- Bahasa Indonesia: PASS setelah tiga penyempurnaan prosa: korolari pembuka kini
  terikat jelas pada Arzelà--Ascoli, dua penyebutan berikutnya memakai istilah
  penuh `teorema Arzelà--Ascoli`, dan predikat umum jamak tentang
  operator-operator dipertahankan. Tidak ada residu prosa Inggris selain nama
  diri, simbol, dan pengenal TeX.

Sasaran hidup lengkap sesudah U283 adalah 189.952 byte, SHA-256
`3c0421db8e12bcdd68b2e5fc315337308aad406855d0431b4acae4f91ffe1760`.
Tidak ada penulis yang dihubungi.
