# Keluarga Matematika Lebl — cuplikan kerja U393 — 2026-08-26

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.7_Latihan.pdf`:
  pembaca R006 Jilid II terbaru, 224 halaman, sampai akhir Bagian 11.7 beserta
  seluruh empat belas latihan.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I lengkap,
  334 halaman, dipertahankan tanpa perubahan.
- `Notes_on_Diffy_Qs_Bab_8_Sistem_Nonlinear_Bahasa_Indonesia_v6.11_PARSIAL.pdf`:
  pembaca mandiri 40 halaman untuk Bab 8 R007 yang lengkap dan telah melalui
  QA pemilik lane.
- `lebl-mathematics-family-id-source-backend-wip-u393-20260826.zip`: sumber
  LaTeX, manifes, istilah, ledger koreksi dan O001, bukti QA, overlay pembaca,
  serta backend modular netral-bahasa.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku tetap
dikecualikan. Proof campuran yang memuat bab belum diterjemahkan tidak
dipublikasikan sebagai pembaca Indonesia.

## Cakupan terjemahan

Manifes memuat 393 unit unik: R006 308, R007 35, dan R008 50. R006 Jilid I
lengkap; Jilid II kini mencapai akhir Bagian 11.7. Dua puluh tiga unit baru
sejak U370 mencakup aproksimasi Weierstrass, konvolusi, korolari nilai mutlak,
aljabar pemisah titik, teorema Stone--Weierstrass versi real dan kompleks,
penerapan aproksimasi variabel terpisah, dan seluruh empat belas latihan.
R007 dan R008 mempertahankan batas publik sebelumnya.

Manifes adalah 596.621 byte dengan SHA-256
`500d6c59b57825cbfb53a8767a889c2aef6a25f375fe0a6aa3bdb6cb051a17cb`.
Seluruh rumus, label, rujukan, dan struktur latihan dipertahankan. Dua puluh
satu latihan tanpa solusi tetap dipetakan ke O001; tidak ada jawaban atau
solusi yang diciptakan.

## Backend modular v0.4-live

Checkpoint `v0.4-live-2026.08.26-u393-final-e` memuat 3.806 rekaman, 393
segmen manifes, 424 unit, 748 konsep, 786 ekspresi, 760 istilah logis kini,
256 koreksi, dan 21 kekosongan solusi O001. Lima belas proyeksi CSV berputar
balik tepat ke seluruh rekaman.

Dua build independen masing-masing menghasilkan 27 berkas dan 16.690.330
byte, dengan nol perbedaan path, ukuran, atau hash. Hash inventaris kanonik:
`eb022c1d1388f5ef8c84574438f44d8c7ed9a3e05d070d0b2ea20395e9eb781e`.
Validasi generik, integritas referensial, garis keturunan edisi asiklik,
binding unit-koreksi, dan putar-balik CSV semuanya lulus. Replay E/F dan uji
mutasi negatif diverifikasi secara independen; replay F tidak disertakan
karena byte-identik.

## QA matematika, istilah, dan layout

Sebelas klarifikasi sumber baru sejak U370 tercatat terpisah. `ADV-0256`
memperbaiki asumsi titik interpolasi berbeda sepasang-sepasang yang diperlukan
oleh petunjuk sumber; koreksi ini terikat tepat pada U308 dan telah melalui
audit matematika serta bahasa independen. Istilah `norma C^k` ditambahkan
sebagai `LEBL-TERM-0760`.

Pembaca Jilid II lulus converter tanpa error, sembilan pass TeX dengan tujuh
produk bantu byte-stabil, 80/80 font tertanam, 638 tautan, 13 entri outline,
ekstraksi teks, serta render halaman 1–2 dan 193–224. Halaman 201–215 berisi
Bagian 11.7 lengkap. Blok isi terpusat dalam lima piksel, memakai sekitar
76,5% lebar halaman, dan tidak terpotong. Berkas akhir adalah 2.281.400 byte
dengan SHA-256
`5a8db6dd8f9b559c578fe31678943e093650019686e2e75cc752d1b2b49bb211`.

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

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U393 adalah
`10.5281/zenodo.22104149`. Tag GitHub:
`lebl-family-id-wip.2026.08.26.u393`.
