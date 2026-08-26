# Keluarga Matematika Lebl — cuplikan kerja U397 — 2026-08-26

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.8.1_Polinom_Trigonometrik.pdf`:
  pembaca R006 Jilid II terbaru, 226 halaman, sampai akhir Subbagian 11.8.1
  `Polinom trigonometri`.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I lengkap,
  334 halaman, dipertahankan tanpa perubahan.
- `Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`:
  pembaca mandiri 40 halaman untuk Bab 8 R007 yang lengkap dan telah melalui
  QA pemilik lane.
- `lebl-mathematics-family-id-source-backend-wip-u397-20260826.zip`: sumber
  LaTeX, manifes, istilah, ledger koreksi dan O001, bukti QA, overlay pembaca,
  serta backend modular netral-bahasa.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku tetap
dikecualikan. Proof campuran yang memuat bab belum diterjemahkan tidak
dipublikasikan sebagai pembaca Indonesia.

## Cakupan terjemahan

Manifes memuat 397 unit unik: R006 312, R007 35, dan R008 50. R006 Jilid I
lengkap; Jilid II kini mencapai akhir Subbagian 11.8.1. Empat unit baru sejak
U393 mencakup pembukaan deret Fourier dan representasi Laurent, motivasi
fungsi eigen, periodisitas dan pemulihan koefisien, kriteria bernilai real,
serta kebebasan linear. R007 dan R008 mempertahankan batas publik sebelumnya.

Manifes adalah 605.334 byte dengan SHA-256
`e69eff9f1ab797ccb1be2865bc95999631d6fd5a374d5250db3b4cfb816db347`.
Seluruh rumus, label, rujukan, dan struktur dipertahankan. Dua puluh satu
latihan tanpa solusi tetap dipetakan ke O001; tidak ada jawaban atau solusi
yang diciptakan.

## Backend modular v0.4-live

Checkpoint `v0.4-live-2026.08.26-u397-a` memuat 3.831 rekaman, 397 segmen
manifes, 428 unit, 754 konsep, 794 ekspresi, 766 istilah logis kini, 257
koreksi, dan 21 kekosongan solusi O001. Lima belas proyeksi CSV berputar balik
tepat ke seluruh rekaman.

Dua build independen masing-masing menghasilkan 27 berkas dan 16.839.490
byte, dengan nol perbedaan path, ukuran, atau hash. Hash inventaris kanonik:
`0b5720512a26fb12282971daf04d45c5db55d8678afe1a35e5cc44de0675302b`.
Validasi generik, integritas referensial, 397 binding manifes hidup, dan
putar-balik CSV semuanya lulus. Replay B tidak disertakan karena byte-identik.

## QA matematika, istilah, dan layout

ADV-0257 memperbaiki pernyataan antiturunan frekuensi nol: $e^{inx}/(in)$
hanya digunakan untuk $n \ne 0$, sedangkan integran untuk $n=0$ identik dengan
1. Koreksi ini tidak mengubah nilai integral atau rumus pemulihan koefisien
dan telah melalui audit matematika serta bahasa independen. Enam istilah baru
ditambahkan sebagai `LEBL-TERM-0761` sampai `LEBL-TERM-0766`.

Pembaca Jilid II lulus converter tanpa error, sembilan pass TeX dengan tujuh
produk bantu byte-stabil, 85/85 objek font tertanam, 1.227 destinasi bernama,
644 tautan, ekstraksi teks tanpa `??` atau placeholder, serta render halaman
1-2 dan 212-226. Halaman baru 216-217 terpusat dalam tiga piksel dan memakai
sekitar 77% lebar halaman, tanpa potongan, tumpang tindih, atau glif rusak.
Berkas akhir adalah 2.292.242 byte dengan SHA-256
`40b2e2cb27dd59d288ef76453ae293558fcd1ae8efb96e1e87a646f8f0b8f73d`.

## Otoritas, provenance, dan lisensi

Ketiga karya sumber oleh Jiří Lebl tetap mempunyai identitas dan jalur hak
terpisah: R006 *Basic Analysis* v6.3, R007 *Notes on Diffy Qs* v6.11, dan R008
*Guide to Cultivating Complex Analysis* v1.9. Edisi turunan memilih jalur
**CC BY-SA 4.0** secara terpisah. Ini bukan edisi resmi dan tidak menyiratkan
dukungan penulis atau institusi mana pun.

Penerjemahan, penyuntingan, QA istilah, metadata aksesibilitas, dan integrasi
backend dilakukan oleh **OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi
pengguna. Seluruh kredit sumber dan kontributor manusia dipertahankan. Tidak
ada penulis yang dihubungi dan tidak ada isu upstream yang dibuka.

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U397 adalah
`10.5281/zenodo.22105195`. Tag GitHub:
`lebl-family-id-wip.2026.08.26.u397`.
