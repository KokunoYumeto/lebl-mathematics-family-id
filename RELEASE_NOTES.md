# Keluarga Matematika Lebl — R006 lengkap, keluarga parsial U429 — 2026-08-30

Ini adalah cuplikan pelestarian publik yang dapat direproduksi. Kedua jilid
R006 *Analisis Dasar* kini lengkap dalam Bahasa Indonesia, tetapi keluarga
tiga buku secara keseluruhan tetap parsial karena R007 dan R008 belum selesai.

## Isi pembaca

- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid II lengkap,
  241 halaman, 2.427.379 byte, SHA-256
  `e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3`.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I lengkap,
  334 halaman, dipertahankan byte-identik dari rilis U397.
- `Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`:
  pembaca mandiri 40 halaman untuk Bab 8 R007 yang lengkap, dipertahankan
  byte-identik dari rilis U397.
- `lebl-mathematics-family-id-source-backend-wip-u429-20260830.zip`: sumber LaTeX, manifes, istilah, ledger koreksi
  dan O001, bukti QA, overlay reproduksi pembaca, serta backend modular
  netral-bahasa U429.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku tetap
dikecualikan. Proof campuran yang memuat bagian belum diterjemahkan tidak
dipublikasikan sebagai pembaca Indonesia.

## Cakupan terjemahan

Manifes memuat 429 unit unik: R006 344, R007 35, dan R008 50. R006 Jilid I dan
Jilid II lengkap. Unit terakhir R006 adalah latihan tentang peluruhan koefisien
Fourier yang dapat lambat secara sembarang, beserta remark penjelas dan hint
sumber eksplisit. R007 mempertahankan cursor kanonik pada raw line 89
`ch-first-order-ode.tex` dan pembaca Bab 8 lengkap; R008 mempertahankan cursor
pada raw line 1648 sumber analisis kompleks.

Manifes adalah 671.315 byte dengan SHA-256
`b493ed47379b99c8cd5cae0d123063702082c27e654b4e64ea59d2faa6cca52e`.
Seluruh 429 binding manifes hidup lulus. Tiga puluh empat latihan tanpa solusi
sumber tetap dipetakan ke O001; tidak ada jawaban atau solusi yang diciptakan.

## Backend modular v0.4-live

Checkpoint `v0.4-live-2026.08.30-u429-a` memuat 4.021 rekaman, 858 ekspresi,
797 istilah logis kini, 268 koreksi aktif, 33 aset, 650 relasi, 429 segmen
manifes, 785 konsep, dan 477 unit. Lima belas proyeksi CSV berputar balik tepat
ke seluruh 4.021 rekaman.

Dua build independen masing-masing menghasilkan 27 berkas dan 18.208.054
byte, dengan nol perbedaan path, ukuran, atau hash. Hash inventaris kanonik:
`e6ab83c87774c191ba28b4efa1d0cef3ac551d74482c52b6c968816e51c76057`.
Validasi skema, integritas referensial, 429 binding manifes, 372 pemeriksaan
komponen langsung, dan putar-balik CSV semuanya lulus. Replay B tidak
disertakan karena byte-identik.

## QA matematika dan pembaca lengkap

Unit U429 mempertahankan semua kuantor, sembilan payload matematika, kedua
rujukan silang, remark, dan hint eksplisit sumber. Tidak ada syarat tambahan,
bukti, atau solusi yang disisipkan.

Build pembaca final memakai epoch tetap. PDF dan tujuh produk bantu identik
antara pass 5 dan 6. Log final tidak memuat error fatal, LaTeX, kontrol tak
terdefinisi, glif hilang, rujukan tak terdefinisi, permintaan rerun, label
ganda, tujuan tak sah, atau outline buruk. Seluruh 687 tautan, 33 entri outline,
dan 98 baris font lulus; seluruh font tertanam. Halaman 1–2 dan 231–241 lulus
inspeksi visual deterministik.

## Identitas sumber dan publikasi

Checkpoint sumber/backend publik U429 terikat pada commit
`e55907983ca54bb2c94d90230eb949b64a6ee7ff` dan tree
`97cc963dc211728a20be1c18f9c8890f01790ae9`. Transaksi sumber memublikasikan
tepat 42 path reguler / 20.178.050 byte dengan inventaris kanonik SHA-256
`d9fdbc0921be59836e5c1447720711fd040d682574eac148acf2c723d7402118`.

Identitas rilis:

- tag GitHub: `lebl-family-id-wip.2026.08.30.u429`;
- DOI versi Zenodo: `10.5281/zenodo.22172396`;
- arsip sumber/backend:
  `lebl-mathematics-family-id-source-backend-wip-u429-20260830.zip`.

Concept DOI tetap `10.5281/zenodo.22059779`; versi U397 dan seluruh checkpoint
historis tetap dipertahankan. GitHub dan Zenodo harus memuat sembilan aset
dalam urutan serta kebijakan byte yang dibekukan oleh `ASSET_POLICY.json`.

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
