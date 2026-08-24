# Reproduksi cuplikan kerja U333

Paket ini mempertahankan pekerjaan publik pada 24 Agustus 2026.

## Batas isi

- `translation/ra/`: R006 Jilid I lengkap; Jilid II diterima berurutan sampai
  akhir Subbagian 11.4.1, `Eksponensial kompleks`. `Fungsi trigonometri dan
  pi` belum dimuat.
- `translation/diffyqs/`: R007 sampai rumus integral tentu untuk kondisi awal
  pada raw line 87 `ch-first-order-ode.tex`.
- `translation/complex-analysis/`: R008 sampai akhir bagian bola Riemann pada
  raw line 1644 sumber `ca.tex`.
- `translation/TRANSLATION_MANIFEST.jsonl`: 333 unit (R006 268, R007 15,
  R008 50), 478.547 byte, SHA-256
  `de03bdf56a20104420dde65bbb47778189f58a97134b6867aa32f6cbd1ba0385`.

Setiap baris manifes adalah JSON sah yang mengikat identitas unit, irisan
sumber/sasaran, dan hash komponennya. Tidak ada ID unit duplikat.

Identitas rilis checkpoint ini adalah tag GitHub
`lebl-family-id-wip.2026.08.24.u333` dan DOI versi Zenodo
`10.5281/zenodo.22076849`. Statusnya tetap parsial sampai seluruh korpus tiga
buku selesai.

## Membangun pembaca Jilid II

1. Salin pohon `translation/ra/` ke direktori build baru.
2. Ganti `realanal2.tex` dan `ch-approximate.tex` pada salinan dengan berkas
   dari `release/u333/`. Salin pula aset Figure 11.6 dari
   `release/u333/figures/` ke subdirektori `figures/` build. Jangan menimpa
   pohon terjemahan hidup.
3. Jalankan converter sumber proyek dan wajibkan pesan akhir nol error.
4. Jalankan `makeindex` untuk indeks dan glosarium, kemudian lima pass
   `pdflatex` sampai log dan referensi stabil.
5. Verifikasi hasil terhadap
   `qa/R006_VOLUME2_COMPLEX_EXPONENTIAL_READER_U333_BUILD_RECEIPT.md`.

Cutoff berakhir pada target raw line 1862 dari `ch-approximate.tex`, tepat pada
akhir Subbagian 11.4.1. Overlay `ch-approximate.tex` adalah 66.543 byte,
SHA-256
`468729fb18049785586a0638872cd049ffc61762de4149013685c354cb4daaf0`.
Ia dibuat oleh cutoff sumber deterministik, bukan dengan memangkas PDF.
Nomor untuk dua referensi yang targetnya berada setelah cutoff dibekukan dari
build penuh v6.3; target tidak dibuat seolah-olah hadir atau dapat diklik.

PDF acuan U333 adalah 192 halaman, 2.058.059 byte, SHA-256
`6f1f38221af120d6459cdc217e789ca1f7a9d4f353f5720db00ff271ce637061`.

## Membangun dan memvalidasi backend

Checkpoint kanonik ada di
`backend/production/v0.4-live-2026.08.24-u333-a/`. Ia memuat 2.692
rekaman, lima belas proyeksi CSV, 26 berkas, dan 11.574.002 byte. Hash
inventaris kanoniknya adalah
`d0aac7d8017ba5f6540f5fa1ab344982146ab35347d7f7337d38513948823bf1`.

`backend/production/build_live_v04.py` membangun checkpoint secara
deterministik dari snapshot v0.3 ditambah manifes, terminologi, koreksi, dan QA
hidup. Validasi harus menegakkan:

- dataset dan seluruh rekaman lulus JSON Schema;
- ID rekaman unik dan relasi referensial utuh;
- lima belas CSV memakai dialek LF + quote-all yang ditetapkan;
- `record_json` dari CSV mengembalikan tepat 2.692 rekaman kanonik;
- build ulang mempunyai inventaris path, ukuran, dan SHA-256 identik.

Receipt ada di `qa/BACKEND_V0_4_LIVE_U333_20260824.md`. Replay B telah
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
