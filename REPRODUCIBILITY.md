# Reproduksi checkpoint keluarga parsial U429

Paket ini mempertahankan pekerjaan publik pada 30 Agustus 2026. R006 Jilid I
dan Jilid II lengkap; status keluarga tetap parsial sampai R007 dan R008
selesai.

Identitas sumber yang telah dipublikasikan adalah commit GitHub
`e55907983ca54bb2c94d90230eb949b64a6ee7ff` dan tree
`97cc963dc211728a20be1c18f9c8890f01790ae9`. Identitas rilis adalah tag
`lebl-family-id-wip.2026.08.30.u429` dan DOI versi Zenodo
`10.5281/zenodo.22172396`; concept DOI tetap
`10.5281/zenodo.22059779`.

## Batas isi

- `translation/ra/`: R006 Jilid I dan Jilid II lengkap. Unit manifes R006
  terakhir adalah latihan peluruhan koefisien Fourier yang dapat lambat secara
  sembarang, beserta remark dan hint sumber eksplisit.
- `translation/diffyqs/`: R007 kontigu sampai raw line 87
  `ch-first-order-ode.tex`, ditambah Bab 8 `ch-nonlin-systems.tex` lengkap.
  Cursor aktif tetap raw line 89.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann;
  cursor aktif tetap raw line 1648 sumber.
- `translation/TRANSLATION_MANIFEST.jsonl`: 429 unit (R006 344, R007 35,
  R008 50), 671.315 byte, SHA-256
  `b493ed47379b99c8cd5cae0d123063702082c27e654b4e64ea59d2faa6cca52e`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

## Membangun pembaca R006 lengkap

Overlay reproduksi ada di `release/u429/` dalam arsip sumber.

1. Salin pohon `translation/ra/` ke direktori build baru.
2. Ganti `realanal2.tex` dan `ch-approximate.tex` dengan berkas overlay U429.
3. Bangun Jilid I dalam direktori yang sama agar `realanal.aux` tersedia.
4. Jalankan `build_u429.ps1` untuk converter, indeks, glosarium, dan pass TeX
   Jilid II sampai produk bantu stabil.

Target lengkap `translation/ra/ch-approximate.tex` adalah 198.362 byte,
SHA-256
`cfaa1339706c31f16255642adcccb33903343808bc2d1bf195d70d3f25004133`.
Hasil acuan `Analisis_Dasar_II_Bahasa_Indonesia_v6.3.pdf` harus 241 halaman,
2.427.379 byte, SHA-256
`e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3`.
PDF dan tujuh produk bantu harus byte-identik antara dua pass final. Receipt:
`qa/R006_FOURIER_ARBITRARILY_SLOW_COEFFICIENT_DECAY_EXERCISE_U429_20260830.md`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.30-u429-a/`. Ia memuat 4.021 rekaman,
858 ekspresi, 429 segmen manifes, 15 proyeksi CSV, 27 berkas, dan 18.208.054
byte. Hash inventaris kanonik:
`e6ab83c87774c191ba28b4efa1d0cef3ac551d74482c52b6c968816e51c76057`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik. `backend/tools/backend_tool.py validate` harus menegakkan
skema, ID unik, referensi utuh, garis keturunan edisi yang asiklik dan
se-resource, 429 binding manifes hidup, 372 pemeriksaan komponen langsung,
binding O001, serta putar-balik tepat 4.021 rekaman melalui 15 proyeksi CSV.
Replay `-u429-b` terbukti identik tetapi dikecualikan dari paket untuk
menghindari duplikasi byte.

## Istilah, koreksi, dan O001

`control/TERMINOLOGY.csv` memuat 797 istilah kini / 819 baris fisik dan
SHA-256
`4c965c8a7d39320a3b59f7aea3fa8342c5499ef364ee9aff38de86b58743b9a9`.
`control/ADVERSE_LEDGER.jsonl` memuat 268 peristiwa dan SHA-256
`97574309b30de27a14b388c6ef06bab7d9a09a8f2af7c8613ccfcbe405609f6b`.
`control/O001_SOLUTION_GAP_LEDGER.jsonl` memuat 34 baris unik dan SHA-256
`115098fec77d4dbe16edbaac8a75bf8bdd2e4af5c536b400d691103aa1c6bffb`.

O001 mengikat 34 latihan tanpa solusi sumber, termasuk 14 hint eksplisit dan
20 keadaan tanpa hint. Tidak ada jawaban, bukti, atau solusi yang diciptakan.

## Perakitan arsip dan rilis

Nama arsip final adalah
`lebl-mathematics-family-id-source-backend-wip-u429-20260830.zip`. Builder harus menolak
output yang telah ada, mengurutkan entry menurut `(casefold(path), path)`,
memakai timestamp tetap `2026-08-30 00:00:00`, mode Unix `0755` untuk
direktori dan `0644` untuk berkas, flag UTF-8, serta DEFLATE level 9. Builder
juga harus memeriksa integritas ZIP, entry duplikat, path `.git`, nama mirip
kredensial, marker profil lokal, dan enam gambar sampul ritel yang wajib
dikecualikan.

Urutan sembilan aset publik dan semua hash byte-invarian berada di
`ASSET_POLICY.json`. `SHA256SUMS.txt` dihasilkan dari
`SHA256SUMS.template.txt`, memuat delapan aset selain dirinya sendiri, dan
memakai dua spasi antara hash heksadesimal lowercase dan nama berkas.

Paket mengecualikan cache, render sementara, proof campuran, replay backend,
raw provenance dump, arsip otoritas mentah, dan gambar sampul ritel yang
haknya tidak termasuk dalam lisensi buku.
