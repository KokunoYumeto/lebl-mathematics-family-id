# Reproduksi cuplikan kerja U330

Paket ini mempertahankan pekerjaan publik pada 24 Agustus 2026.

## Batas isi

- `translation/ra/`: R006 Jilid I lengkap; Jilid II diterima berurutan sampai
  akhir Subbagian 11.3.4, `Fungsi analitik`. `Identity theorem` belum dimuat.
- `translation/diffyqs/`: R007 sampai rumus integral tentu untuk kondisi awal
  pada raw line 87 `ch-first-order-ode.tex`.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann pada
  raw line 1644 sumber `ca.tex`.
- `translation/TRANSLATION_MANIFEST.jsonl`: 330 unit (R006 265, R007 15,
  R008 50), 472.659 byte, SHA-256
  `c45f42524e598f724e5845c1a7e3c38b9c43de241dcae63b48870b2683d1b34b`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

Identitas rilis checkpoint ini adalah tag GitHub
`lebl-family-id-wip.2026.08.24.u330` dan DOI versi Zenodo
`10.5281/zenodo.22074515`. Statusnya tetap parsial sampai seluruh korpus tiga
buku selesai.

## Membangun pembaca Jilid II

1. Salin pohon `translation/ra/` ke direktori build baru.
2. Ganti `realanal2.tex` dan `ch-approximate.tex` pada salinan dengan berkas
   dari `release/u330/`. Salin pula aset Figure 11.6 dari
   `release/u330/figures/` ke subdirektori `figures/` build. Jangan menimpa
   pohon terjemahan hidup.
3. Jalankan converter sumber proyek dan wajibkan pesan akhir nol error.
4. Jalankan `makeindex` untuk indeks dan glosarium, kemudian lima pass
   `pdflatex` sampai log dan referensi stabil.
5. Verifikasi hasil terhadap
   `qa/R006_VOLUME2_POWER_SERIES_ANALYTIC_READER_U330_BUILD_RECEIPT.md`.

Cutoff berakhir pada target raw line 1549 dari `ch-approximate.tex`, tepat pada
akhir Subbagian 11.3.4. Overlay `ch-approximate.tex` adalah 54.933 byte,
SHA-256
`f466efb755040b41da42989f3ff9a95321f528769ba8fcb540e2c8094ae77073`.
Ia dibuat oleh `backend/tools/make_partial_tex.py`, bukan dengan memangkas PDF.
Nomor untuk dua referensi yang targetnya berada setelah cutoff dibekukan dari
build penuh v6.3; target tidak dibuat seolah-olah hadir atau dapat diklik.

PDF acuan U330 adalah 188 halaman, 1.991.475 byte, SHA-256
`28c0844666712d94bed82789e014faf8dbbba32c2384b77cd745423c4f845aa1`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.24-u330-figfix-a/`. Ia memuat 2.683
rekaman, lima belas proyeksi CSV, 26 berkas, dan 11.495.077 byte. Hash
inventaris kanoniknya adalah
`8c60d50e03a80441dcc5e73ba398ab37f1b258048cb34368d44d474296ac68df`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik dari snapshot v0.3 ditambah manifes, terminologi, koreksi, dan QA
hidup. Validasi harus menegakkan:

- dataset dan seluruh rekaman lulus JSON Schema;
- ID rekaman unik dan relasi referensial utuh;
- lima belas CSV memakai dialek LF + quote-all yang ditetapkan;
- `record_json` dari CSV mengembalikan tepat 2.683 rekaman kanonik;
- build ulang mempunyai inventaris path, ukuran, dan SHA-256 identik.

Receipt ada di `qa/BACKEND_V0_4_LIVE_U330_FIGFIX_20260824.md`. Replay B telah
dibuktikan identik tetapi tidak disertakan dalam paket publik.

## Istilah, hak, dan pengecualian

`control/` memuat terminologi, komponen hak, dan kandidat koreksi sumber.
`authority/terminology_evidence/` memuat laporan audit istilah lapangan.
Kandidat TeX arXiv terbukti berbahasa Inggris; fallback akademik Indonesia dan
keputusan istilah dicatat secara eksplisit.

Lisensi turunan adalah CC BY-SA 4.0. Lihat `LICENSE.md`,
`translation/ra/LICENSE.md`, dan `authority/R006_AUTHORITY.md`. Foto sampul
ritel `cover*.png`, `cover*.xcf`, dan thumbnail terkait tidak disertakan karena
haknya tidak termasuk dalam lisensi buku. Paket juga mengecualikan cache,
render sementara, build penuh dengan ekor belum diterjemahkan, raw provenance
dumps, backend replay B, dan arsip otoritas mentah.

Penerjemahan, penataan, QA istilah, dan backend dilakukan oleh **OpenAI Codex gpt-5.6-sol, Ultra**
atas instruksi pengguna, dengan seluruh kredit sumber dan kontributor manusia
dipertahankan.
