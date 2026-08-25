# Reproduksi cuplikan kerja U370

Paket ini mempertahankan pekerjaan publik pada 25 Agustus 2026. Statusnya
parsial sampai seluruh korpus tiga buku selesai.

Identitas checkpoint: tag GitHub `lebl-family-id-wip.2026.08.25.u370`, DOI
versi Zenodo `10.5281/zenodo.22088826`, dan concept DOI
`10.5281/zenodo.22059779`.

## Batas isi

- `translation/ra/`: R006 Jilid I lengkap; Jilid II hidup sampai seluruh
  latihan Bagian 11.6. Cursor berikutnya adalah source raw line 3137 / target
  raw line 3149, *The Stone--Weierstrass theorem*.
- `translation/diffyqs/`: R007 kontigu sampai raw line 87
  `ch-first-order-ode.tex`, ditambah Bab 8 `ch-nonlin-systems.tex` lengkap.
  Cursor aktif tetap raw line 89; paket helper Bab 8 tidak mengubahnya.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann pada
  raw line 1644 sumber `ca.tex`.
- `translation/TRANSLATION_MANIFEST.jsonl`: 370 unit (R006 285, R007 35,
  R008 50), 545.833 byte, SHA-256
  `4f937735e3416439f7e82ae3ed3be2978d5cf5b7844987066c64c01a56186789`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

## Membangun pembaca R006 Jilid II U370

Overlay reproduksi ada di `release/u370/`.

1. Salin pohon `translation/ra/` ke direktori build baru.
2. Ganti `realanal2.tex` dan `ch-approximate.tex` dengan berkas overlay.
3. Bangun Jilid I agar `realanal.aux` tersedia.
4. Jalankan `build_u370.ps1`, atau reproduksi converter, empat pass indeks dan
   glosarium, serta sembilan pass `pdflatex` untuk Jilid II.

Overlay membekukan prefiks target line 1–3147. Hasil acuan harus 208 halaman,
2.161.063 byte, SHA-256
`00fde02788a34292a44f38fed3146df2dbb4db8d942672e59fd54c9e362b51b7`.
Tujuh produk bantu harus identik antara pass 8 dan 9. Receipt:
`qa/R006_ARZELA_ASCOLI_SECTION_READER_U370_20260825.md`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.25-u370-a/`. Ia memuat 3.573 rekaman,
370 segmen manifes, 740 ekspresi, 15 proyeksi CSV, 27 berkas, dan 15.377.121
byte. Hash inventaris kanonik:
`f317d2add54525af1680678b181a86315340c1e06db8cf72dc9c1793f3e62e75`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik. Validasi harus menegakkan skema, ID unik, referensi utuh,
binding ledger O001 tanpa alias jalur, 15 proyeksi CSV, dan putar-balik tepat
3.573 rekaman. Replay `-u370-b` terbukti identik tetapi dikecualikan dari paket
untuk menghindari duplikasi byte.

## Istilah, koreksi, dan pengecualian

`control/TERMINOLOGY.csv` memuat 733 istilah kini dan SHA-256
`580653f43e23e73ff95b9dea299f9e1e636c9db65b1dac4a9508d4531e5c0148`.
`control/ADVERSE_LEDGER.jsonl` memuat 245 peristiwa dan SHA-256
`9559996396d2b90c34e446e9c90de9268f7433c39c810135322cd7ca0c354f3f`.
`control/O001_SOLUTION_GAP_LEDGER.jsonl` memuat tujuh kekosongan latihan dan
SHA-256
`06d3cb8a5616f3f2009c36336e19a05f429e9336257f451ea33adb117166da4e`.

Paket mengecualikan cache, render sementara, proof campuran, replay backend,
raw provenance dump, arsip otoritas mentah, dan gambar sampul ritel yang
haknya tidak termasuk dalam lisensi buku.

Penerjemahan, penataan, QA istilah, dan backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna, dengan seluruh
kredit sumber dan kontributor manusia dipertahankan.
