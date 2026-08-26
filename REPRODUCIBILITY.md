# Reproduksi cuplikan kerja U393

Paket ini mempertahankan pekerjaan publik pada 26 Agustus 2026. Statusnya
parsial sampai seluruh korpus tiga buku selesai.

Identitas checkpoint: tag GitHub `lebl-family-id-wip.2026.08.26.u393`, DOI
versi Zenodo `10.5281/zenodo.22104149`, concept DOI
`10.5281/zenodo.22059779`, dan commit isi GitHub
`3dcbcbde8bc3f589e8572b0096126f4e67b68d78`.

## Batas isi

- `translation/ra/`: R006 Jilid I lengkap; Jilid II hidup sampai seluruh
  latihan Bagian 11.7. Cursor berikutnya adalah source raw line 4201 / target
  raw line 4209, pembukaan Bagian 11.8 *Deret Fourier*.
- `translation/diffyqs/`: R007 kontigu sampai raw line 87
  `ch-first-order-ode.tex`, ditambah Bab 8 `ch-nonlin-systems.tex` lengkap.
  Cursor aktif tetap raw line 89; paket helper Bab 8 tidak mengubahnya.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann pada
  raw line 1644 sumber `ca.tex`.
- `translation/TRANSLATION_MANIFEST.jsonl`: 393 unit (R006 308, R007 35,
  R008 50), 596.621 byte, SHA-256
  `500d6c59b57825cbfb53a8767a889c2aef6a25f375fe0a6aa3bdb6cb051a17cb`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

## Membangun pembaca R006 Jilid II U393

Overlay reproduksi ada di `release/u393/`.

1. Salin pohon `translation/ra/` ke direktori build baru.
2. Ganti `realanal2.tex` dan `ch-approximate.tex` dengan berkas overlay.
3. Bangun Jilid I agar `realanal.aux` tersedia.
4. Jalankan `build_u393.ps1`, atau reproduksi converter, empat siklus indeks
   dan glosarium, serta sembilan pass `pdflatex` untuk Jilid II.

Overlay membekukan prefiks target line 1–4208. Hasil acuan harus 224 halaman,
2.281.400 byte, SHA-256
`5a8db6dd8f9b559c578fe31678943e093650019686e2e75cc752d1b2b49bb211`.
Tujuh produk bantu harus identik antara pass 8 dan 9. Receipt:
`qa/R006_STONE_WEIERSTRASS_SECTION_COMPLETE_READER_U393_20260826.md`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.26-u393-final-e/`. Ia memuat 3.806
rekaman, 393 segmen manifes, 786 ekspresi, 15 proyeksi CSV, 27 berkas, dan
16.690.330 byte. Hash inventaris kanonik:
`eb022c1d1388f5ef8c84574438f44d8c7ed9a3e05d070d0b2ea20395e9eb781e`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik. `backend/tools/backend_tool.py validate` harus menegakkan
skema, ID unik, referensi utuh, garis keturunan edisi yang asiklik dan
se-resource, binding O001, serta putar-balik tepat 3.806 rekaman melalui 15
proyeksi CSV. Replay `-u393-final-f` terbukti identik tetapi dikecualikan dari
paket untuk menghindari duplikasi byte.

## Istilah, koreksi, dan pengecualian

`control/TERMINOLOGY.csv` memuat 760 istilah kini dan SHA-256
`f9e5f6fa14972e139fed5c0d4afbd6a1d2ee20c3f16d0131e1617d26621e31c1`.
`control/ADVERSE_LEDGER.jsonl` memuat 256 peristiwa dan SHA-256
`1492febaacbbbb9b4d2fed128d73748641cfc0411196b6659332460e8a3f6e35`.
`control/O001_SOLUTION_GAP_LEDGER.jsonl` memuat 21 kekosongan latihan dan
SHA-256
`3ca713f97246a5008a82e05df49441667e7a379979a89634913b4f41d27637a8`.

Paket mengecualikan cache, render sementara, proof campuran, replay backend,
raw provenance dump, arsip otoritas mentah, dan gambar sampul ritel yang
haknya tidak termasuk dalam lisensi buku.

Penerjemahan, penataan, QA istilah, dan backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna, dengan seluruh
kredit sumber dan kontributor manusia dipertahankan.
