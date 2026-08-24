# Keluarga Matematika Lebl — cuplikan kerja U361 — 2026-08-25

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.5_Latihan.pdf`:
  pembaca R006 Jilid II terbaru, 200 halaman, sampai akhir Bagian 11.5 beserta
  seluruh tujuh latihan.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I lengkap,
  334 halaman, dipertahankan tanpa perubahan.
- `Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`:
  pembaca mandiri 40 halaman untuk Bab 8 R007 yang lengkap dan telah melalui
  QA pemilik lane.
- `lebl-mathematics-family-id-source-backend-wip-u361-20260825.zip`: sumber
  LaTeX, manifes, istilah, ledger koreksi dan O001, bukti QA, overlay pembaca,
  serta backend modular netral-bahasa.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku tetap
dikecualikan. Proof campuran yang memuat bab belum diterjemahkan tidak
dipublikasikan sebagai pembaca Indonesia.

## Cakupan terjemahan

Manifes memuat 361 unit unik: R006 276, R007 35, dan R008 50. R006 Jilid I
lengkap; Jilid II kini mencapai akhir Bagian 11.5. R007 tetap memiliki
pendahuluan lengkap, Bab 1 kontigu sampai solusi integral tentu untuk kondisi
awal, dan Bab 8 lengkap sebagai 20 unit disjoint. R008 mencapai akhir bagian
bola Riemann.

Manifes adalah 527.420 byte dengan SHA-256
`3bba4abf924cff036d02b8f7e39e5442afa1117b20d107832cc38cee1ce77ac4`.
Unit U274–U276 mempertahankan semua rumus, label, tujuh latihan, dan empat
petunjuk sumber. Tujuh latihan tanpa solusi dipetakan ke O001; tidak ada
jawaban atau solusi yang diciptakan.

## Backend modular v0.4-live

Checkpoint `v0.4-live-2026.08.24-u361-e` memuat 3.520 rekaman, 361 segmen
manifes, 372 unit, 710 konsep, 722 ekspresi, 722 istilah logis kini, 241
koreksi, dan tujuh kekosongan solusi O001. Lima belas proyeksi CSV berputar
balik tepat ke seluruh rekaman.

Dua build independen masing-masing menghasilkan 27 berkas dan 15.051.229
byte, dengan nol perbedaan path, ukuran, atau hash. Hash inventaris kanonik:
`a8396edb38b192a955431715b0eb44abae823bfd80370f876089c1c0f4ef96af`.
Validasi skema, integritas referensial, alias jalur O001, dan putar-balik CSV
semuanya lulus. Replay `-u361-f` tidak disertakan karena byte-identik.

## QA matematika, istilah, dan layout

Dua klarifikasi sumber dicatat secara terpisah: lingkungan tertusuk harus
berpusat di `z0` (`LEBL-ID-ADV-0240`) dan argumen nol lokal perlu kualifikasi
fungsi yang identik nol secara lokal (`LEBL-ID-ADV-0241`). Keduanya telah
melalui audit matematika independen. Pilihan istilah Indonesia tetap konsisten
dengan audit penggunaan bidang yang terdokumentasi.

Pembaca Jilid II lulus converter tanpa error, lima pass TeX yang stabil, 80/80
font tertanam, pemeriksaan referensi, ekstraksi teks, serta render halaman 1–2
dan 184–200. Halaman baru terbaca, terpusat, dan tidak terpotong. Berkas akhir
adalah 2.112.324 byte dengan SHA-256
`3e03748a32b19a7fabc38be7dbc9f1c8bc845eb99f5896dd5d93877176ceab72`.

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

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U361 adalah
`10.5281/zenodo.22087498`. Tag GitHub:
`lebl-family-id-wip.2026.08.25.u361`.
