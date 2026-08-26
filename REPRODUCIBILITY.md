# Reproduksi cuplikan kerja U397

Paket ini mempertahankan pekerjaan publik pada 26 Agustus 2026. Statusnya
parsial sampai seluruh korpus tiga buku selesai.

Identitas checkpoint: tag GitHub `lebl-family-id-wip.2026.08.26.u397`, DOI
versi Zenodo `10.5281/zenodo.22105195`, concept DOI
`10.5281/zenodo.22059779`, dan commit isi GitHub
`1f4af23981dae23328b2539ee3f623c15879aa89`.

## Batas isi

- `translation/ra/`: R006 Jilid I lengkap; Jilid II hidup sampai akhir
  Subbagian 11.8.1 `Polinom trigonometri`. Cursor berikutnya adalah source raw
  line 4363 / target raw line 4371, pembukaan Subbagian `Fourier series`.
- `translation/diffyqs/`: R007 kontigu sampai raw line 87
  `ch-first-order-ode.tex`, ditambah Bab 8 `ch-nonlin-systems.tex` lengkap.
  Cursor aktif tetap raw line 89; paket helper Bab 8 tidak mengubahnya.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann pada
  raw line 1644 sumber `ca.tex`.
- `translation/TRANSLATION_MANIFEST.jsonl`: 397 unit (R006 312, R007 35,
  R008 50), 605.334 byte, SHA-256
  `e69eff9f1ab797ccb1be2865bc95999631d6fd5a374d5250db3b4cfb816db347`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

## Membangun pembaca R006 Jilid II U397

Overlay reproduksi ada di `release/u397/`.

1. Salin pohon `translation/ra/` ke direktori build baru.
2. Ganti `realanal2.tex` dan `ch-approximate.tex` dengan berkas overlay.
3. Bangun Jilid I dalam direktori yang sama agar `realanal.aux` tersedia.
4. Jalankan `build_u397.ps1`, yang menjalankan converter, empat siklus indeks
   dan glosarium, serta sembilan pass `pdflatex` untuk Jilid II.

Overlay membekukan prefiks target line 1-4370. Hasil acuan harus 226 halaman,
2.292.242 byte, SHA-256
`40b2e2cb27dd59d288ef76453ae293558fcd1ae8efb96e1e87a646f8f0b8f73d`.
Tujuh produk bantu harus identik antara pass 8 dan 9. Receipt:
`qa/R006_FOURIER_TRIGONOMETRIC_POLYNOMIAL_READER_U397_20260826.md`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.26-u397-a/`. Ia memuat 3.831 rekaman,
397 segmen manifes, 794 ekspresi, 15 proyeksi CSV, 27 berkas, dan 16.839.490
byte. Hash inventaris kanonik:
`0b5720512a26fb12282971daf04d45c5db55d8678afe1a35e5cc44de0675302b`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik. `backend/tools/backend_tool.py validate` harus menegakkan
skema, ID unik, referensi utuh, garis keturunan edisi yang asiklik dan
se-resource, 397 binding manifes hidup, binding O001, serta putar-balik tepat
3.831 rekaman melalui 15 proyeksi CSV. Replay `-u397-b` terbukti identik tetapi
dikecualikan dari paket untuk menghindari duplikasi byte.

## Istilah, koreksi, dan pengecualian

`control/TERMINOLOGY.csv` memuat 766 istilah kini dan SHA-256
`6d80796cb5ce4a1ec762975c448caf3396c454f104c4de07624f36de75c8c206`.
`control/ADVERSE_LEDGER.jsonl` memuat 257 peristiwa dan SHA-256
`bf945c64af9c7a174b65f440f1f2956863bf6c7b1fe40e9955ced43596939d17`.
`control/O001_SOLUTION_GAP_LEDGER.jsonl` memuat 21 kekosongan latihan dan
SHA-256
`3ca713f97246a5008a82e05df49441667e7a379979a89634913b4f41d27637a8`.

ADV-0257 membatasi antiturunan $e^{inx}/(in)$ pada $n \ne 0$ dan menyatakan
secara eksplisit bahwa integran untuk $n=0$ identik dengan 1. Koreksi ini
terikat pada unit U311 dan tidak mengubah hasil integral atau rumus koefisien.

Paket mengecualikan cache, render sementara, proof campuran, replay backend,
raw provenance dump, arsip otoritas mentah, dan gambar sampul ritel yang
haknya tidak termasuk dalam lisensi buku.

Penerjemahan, penataan, QA istilah, dan backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna, dengan seluruh
kredit sumber dan kontributor manusia dipertahankan.
