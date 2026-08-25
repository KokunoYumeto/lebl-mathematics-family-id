# R006 U284 — latihan Arzelà--Ascoli I

Status: **PASS; diterima sebagai unit terjemahan kontigu**  
Tanggal: 2026-08-25  
Provenance runtime: `OpenAI Codex gpt-5.6-sol, Ultra`

## Batas dan identitas

- ID stabil:
  `ra.v2.equicontinuity-arzela-ascoli.exercises.counterexamples-compact-operators-and-kronecker`.
- Sumber beku: `source/ra-v6.3/ch-approximate.tex`, raw lines 2947–3064
  inclusive; 118 LF lines; 4.739 byte; SHA-256
  `225cc7713ef6f9b7c799ad1efec944d64693fead47ebd52e383b9e43fcdc4800`.
- Sasaran: `translation/ra/ch-approximate.tex`, raw lines 2957–3076
  inclusive; 120 LF lines; 5.242 byte; SHA-256
  `59c6625851e550462b89db8c66c0356e7d63bc7e6b409a0610a43a51dd5a28f2`.
- Batas berikutnya: source raw line 3066 / target raw line 3078, latihan
  teorema eksistensi Peano yang menutup Bagian 11.6.

## Cakupan dan istilah

Unit memuat judul latihan dan sepuluh latihan lengkap: dua contoh tandingan
hipotesis Arzelà--Ascoli; keluarga Hölder dengan titik pangkal; operator Volterra
dan citranya yang tidak tertutup; operator kernel kontinu; keluarga integral
lintasan pada lingkaran satuan; konvergensi titik demi titik plus
ekuikontinuitas; fungsi periodik; ekuikontinuitas titik demi titik pada domain
kompak; dan kesimpulan subbarisan fase melalui Kronecker.

`LEBL-TERM-0732` mengikat *Kronecker density theorem* ke `teorema kepadatan
Kronecker`, dengan `teorema kerapatan Kronecker` sebagai varian. Pencarian
terbatas tidak menemukan contoh Indonesia dengan nama eponim persis, sehingga
entri ini dicatat jujur sebagai komposisi: penggunaan analisis real Indonesia
mendukung `teorema kepadatan`, sedangkan pernyataan sumber memasok arti tepat;
predikat *dense* tetap diterjemahkan `rapat` sesuai register lane.

## Koreksi sumber terikat

- `LEBL-ID-ADV-0244` (P3): bagian (b) sumber berbunyi `Let C ... the closed
  unit ball` tanpa kopula `be`. Sasaran memulihkan hanya predikat `adalah bola
  satuan tertutup`; himpunan, citra `T(C)`, dan klaim matematikanya tidak berubah.
- `LEBL-ID-ADV-0245` (P2): sumber menyebut `gamma` hanya sebagai parametrisasi,
  lalu memakai integral panjang-busur `ds`. Definisi yang dirujuk dalam
  `ch-one-dim-ints-sv.tex` raw lines 1018–1033 mensyaratkan lintasan mulus atau
  mulus sepotong-sepotong. Sasaran menambahkan tepat hipotesis `lintasan mulus
  sepotong-sepotong yang memparametrisasi S^1`; domain, citra, integran, formula,
  dan kesimpulan subbarisan tidak berubah.

## QA independen

- Struktur: PASS. Urutan 182 kontrol TeX aktif identik. Aliran lingkungan
  identik: 30 peristiwa / 15 pasangan seimbang (`exercise` 10, `equation*` 3,
  `enumerate` 1, `samepage` 1), dengan penyarangan terjaga.
- Matematika: 58 payload inline dan tiga display identik byte demi byte dan
  berurutan. Lima `exerciseref` (termasuk dua versi berbintang dalam dua
  `volIref`), satu `sectionref`, satu catatan kaki, satu URL `href`, dan semua
  payload rujukan persis dipertahankan. Dua koreksi deklaratif di atas tidak
  mengubah payload matematika.
- Kurung kurawal aktif 74/74 seimbang tanpa underflow. Komentar sasaran hanya
  dua pengikat koreksi serta `%` kosong warisan catatan kaki.
- Audit matematis atas kesepuluh latihan PASS. Secara khusus, hipotesis yang
  gagal pada dua latihan pembuka adalah ekuikontinuitas seragam dan kekompakan
  domain; operator Volterra dan operator kernel memenuhi klaim kekompakan;
  kualifikasi lintasan baru cukup untuk mendefinisikan integral dan memberi
  panjang berhingga.
- Bahasa Indonesia: PASS setelah tiga penyempurnaan prosa pada definisi
  lingkaran satuan, kuantifikasi ruang metrik kompak, dan nama penuh teorema
  Arzelà--Ascoli. Petunjuk, catatan, referensi lintas-jilid, catatan kaki, serta
  indeks dilokalkan. Tidak ada residu prosa Inggris selain nama diri, URL,
  simbol, dan pengenal TeX.

Ledger koreksi sesudah audit memuat 245 peristiwa unik, 220.783 byte, SHA-256
`9559996396d2b90c34e446e9c90de9268f7433c39c810135322cd7ca0c354f3f`.
Sasaran hidup lengkap sesudah U284 adalah 190.455 byte, SHA-256
`4a7f32629ac7fe1967200793d178654c9e0b44d4aaed5da043432292223b051e`.
Tidak ada penulis yang dihubungi.
