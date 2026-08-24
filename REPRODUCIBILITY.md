# Reproduksi cuplikan kerja U336

Paket ini mempertahankan pekerjaan publik pada 24 Agustus 2026.

## Batas isi

- `translation/ra/`: R006 Jilid I lengkap; Jilid II diterima berurutan sampai
  akhir Bagian 11.4, `Eksponensial kompleks dan fungsi trigonometri`, termasuk
  sebelas latihan. `Prinsip maksimum dan teorema dasar aljabar` belum dimuat.
- `translation/diffyqs/`: R007 sampai rumus integral tentu untuk kondisi awal
  pada raw line 87 `ch-first-order-ode.tex`.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann pada
  raw line 1644 sumber `ca.tex`.
- `translation/TRANSLATION_MANIFEST.jsonl`: 336 unit (R006 271, R007 15,
  R008 50), 484.083 byte, SHA-256
  `05e5e333ae2e9ee427887c96d91848d9e99b95e4c3391f77a209ede8677a002c`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

Identitas rilis checkpoint ini adalah tag GitHub
`lebl-family-id-wip.2026.08.24.u336` dan DOI versi Zenodo
`10.5281/zenodo.22082567`. Statusnya tetap parsial sampai seluruh korpus tiga
buku selesai.

## Membangun pembaca Jilid II

1. Salin pohon `translation/ra/` ke direktori build baru.
2. Ganti `realanal2.tex` dan `ch-approximate.tex` pada salinan dengan berkas
   dari `release/u336/`. Salin pula aset Figure 11.6 dari
   `release/u336/figures/` ke subdirektori `figures/` build. Jangan menimpa
   pohon terjemahan hidup.
3. Jalankan converter sumber proyek dan wajibkan pesan akhir nol error.
4. Jalankan `makeindex` untuk indeks dan glosarium, kemudian lima pass
   `pdflatex` sampai log dan referensi stabil.
5. Verifikasi hasil terhadap
   `qa/R006_COMPLEX_TRIG_SECTION_READER_U336_20260824.md`.

Cutoff berakhir pada target raw line 2271 dari `ch-approximate.tex`, tepat pada
akhir Bagian 11.4. Overlay `ch-approximate.tex` adalah 81.802 byte, SHA-256
`362969b9ce085c1e454cd3c8d7eeaa6ce2ab185c3fbc98a624c21f8c06814920`.
Ia dibuat oleh cutoff sumber deterministik, bukan dengan memangkas PDF.
Nomor untuk dua referensi yang targetnya berada setelah cutoff dibekukan dari
build penuh v6.3; target tidak dibuat seolah-olah hadir atau dapat diklik.

PDF acuan U336 adalah 198 halaman, 2.091.363 byte, SHA-256
`78543d4e8087e68589e8f15d0a3a969b3282247c7c9c2cdcb6f658dfa4b68e4f`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.24-u336-a/`. Ia memuat 2.701
rekaman, lima belas proyeksi CSV, 26 berkas, dan 11.659.282 byte. Hash
inventaris kanoniknya adalah
`e39eec0b1c05b39a274ffc6fa1f23408e81c8d163a76bb4d6d8339cfb4be2321`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik dari snapshot v0.3 ditambah manifes, terminologi, koreksi, dan QA
hidup. Validasi harus menegakkan:

- dataset dan seluruh rekaman lulus JSON Schema;
- ID rekaman unik dan relasi referensial utuh;
- lima belas CSV memakai dialek LF + quote-all yang ditetapkan;
- `record_json` dari CSV mengembalikan tepat 2.701 rekaman kanonik;
- build ulang mempunyai inventaris path, ukuran, dan SHA-256 identik.

Receipt ada di `qa/BACKEND_V0_4_LIVE_U336_20260824.md`. Replay B telah
dibuktikan identik tetapi tidak disertakan dalam paket publik.

## Istilah, hak, dan pengecualian

`control/` memuat terminologi, komponen hak, dan kandidat koreksi sumber.
`qa/TERMINOLOGY_QA_REVALIDATION_20260824.md` memuat laporan audit istilah
lapangan yang tersanitasi. Pencarian arXiv terbatas tidak menemukan sumber TeX
matematika berbahasa Indonesia; fallback analisis kompleks Indonesia dan
keputusan istilah dicatat secara eksplisit tanpa menyertakan ulang karya
berhak cipta.

Lisensi turunan adalah CC BY-SA 4.0. Lihat `LICENSE.md`,
`translation/ra/LICENSE.md`, dan `authority/R006_AUTHORITY.md`. Foto sampul
ritel `cover*.png`, `cover*.xcf`, dan thumbnail terkait tidak disertakan karena
haknya tidak termasuk dalam lisensi buku. Paket juga mengecualikan cache,
render sementara, build penuh dengan ekor belum diterjemahkan, raw provenance
dumps, backend replay B, dan arsip otoritas mentah.

Penerjemahan, penataan, QA istilah, dan backend dilakukan oleh **OpenAI Codex gpt-5.6-sol, Ultra**
atas instruksi pengguna, dengan seluruh kredit sumber dan kontributor manusia
dipertahankan.
