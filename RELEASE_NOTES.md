# Keluarga Matematika Lebl — cuplikan kerja U370 — 2026-08-25

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.6_Latihan.pdf`:
  pembaca R006 Jilid II terbaru, 208 halaman, sampai akhir Bagian 11.6 beserta
  seluruh sebelas latihan.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I lengkap,
  334 halaman, dipertahankan tanpa perubahan.
- `Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`:
  pembaca mandiri 40 halaman untuk Bab 8 R007 yang lengkap dan telah melalui
  QA pemilik lane.
- `lebl-mathematics-family-id-source-backend-wip-u370-20260825.zip`: sumber
  LaTeX, manifes, istilah, ledger koreksi dan O001, bukti QA, overlay pembaca,
  serta backend modular netral-bahasa.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku tetap
dikecualikan. Proof campuran yang memuat bab belum diterjemahkan tidak
dipublikasikan sebagai pembaca Indonesia.

## Cakupan terjemahan

Manifes memuat 370 unit unik: R006 285, R007 35, dan R008 50. R006 Jilid I
lengkap; Jilid II kini mencapai akhir Bagian 11.6. Sembilan unit baru sejak
U361 mencakup definisi dan contoh keterbatasan, argumen diagonal, definisi dan
kriteria limit ekuikontinu, proposisi himpunan rapat terhitung, teorema
Arzelà--Ascoli beserta bukti lengkap, kedua korolari, penerapan operator
kompak, dan seluruh latihan termasuk pembuktian eksistensi Peano melalui
metode Euler. R007 dan R008 mempertahankan batas publik sebelumnya.

Manifes adalah 545.833 byte dengan SHA-256
`4f937735e3416439f7e82ae3ed3be2978d5cf5b7844987066c64c01a56186789`.
Seluruh rumus, label, rujukan, dan struktur latihan dipertahankan. Tujuh
latihan tanpa solusi tetap dipetakan ke O001; tidak ada jawaban atau solusi
yang diciptakan.

## Backend modular v0.4-live

Checkpoint `v0.4-live-2026.08.25-u370-a` memuat 3.573 rekaman, 370 segmen
manifes, 381 unit, 721 konsep, 740 ekspresi, 733 istilah logis kini, 245
koreksi, dan tujuh kekosongan solusi O001. Lima belas proyeksi CSV berputar
balik tepat ke seluruh rekaman.

Dua build independen masing-masing menghasilkan 27 berkas dan 15.377.121
byte, dengan nol perbedaan path, ukuran, atau hash. Hash inventaris kanonik:
`f317d2add54525af1680678b181a86315340c1e06db8cf72dc9c1793f3e62e75`.
Validasi skema, integritas referensial, alias jalur O001, dan putar-balik CSV
semuanya lulus. Replay `-u370-b` tidak disertakan karena byte-identik.

## QA matematika, istilah, dan layout

Empat klarifikasi sumber baru sejak U361 dicatat terpisah sebagai
`LEBL-ID-ADV-0242` sampai `LEBL-ID-ADV-0245`; masing-masing terikat pada unit,
alasan, dan audit independen. Sebelas istilah baru konsisten dengan audit
penggunaan bidang yang terdokumentasi, termasuk `teorema Arzelà--Ascoli`,
`operator kompak`, dan `metode Euler`.

Pembaca Jilid II lulus converter tanpa error, sembilan pass TeX dengan tujuh
produk bantu byte-stabil pada dua pass terakhir, 80/80 font tertanam,
pemeriksaan 585 tautan internal dan 31 destinasi outline, ekstraksi teks, serta
render 150-dpi halaman 1–2 dan 190–208. Halaman baru terbaca, terpusat, memenuhi
lebar blok halaman, dan tidak terpotong. Berkas akhir adalah 2.161.063 byte
dengan SHA-256
`00fde02788a34292a44f38fed3146df2dbb4db8d942672e59fd54c9e362b51b7`.

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

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U370 adalah
`10.5281/zenodo.22088826`. Tag GitHub:
`lebl-family-id-wip.2026.08.25.u370`.
