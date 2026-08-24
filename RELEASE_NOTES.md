# Keluarga Matematika Lebl — cuplikan kerja U333 — 2026-08-24

Ini adalah cuplikan pelestarian publik yang jujur dan dapat direproduksi,
bukan klaim bahwa seluruh korpus tiga buku telah selesai.

## Isi pembaca

- `Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.4.1_Eksponensial_Kompleks.pdf`:
  cuplikan R006 Jilid II, 192 halaman. Berkas berakhir tepat setelah seluruh
  Subbagian 11.4.1, `Eksponensial kompleks`; `Fungsi trigonometri dan pi` dan
  ekor berikutnya tidak dimuat.
- `Analisis_Dasar_I_Bahasa_Indonesia_v6.3.pdf`: edisi R006 Jilid I yang
  lengkap, 334 halaman.
- `lebl-mathematics-family-id-source-backend-wip-u333-20260824.zip`: sumber
  LaTeX, manifes terjemahan, terminologi, ledger koreksi, bukti otoritas/QA,
  overlay pembaca U333, dan backend modular netral-lokal.

Foto sampul ritel yang haknya tidak termasuk dalam lisensi buku sengaja
dikecualikan. Pembaca Jilid II dibuat melalui cutoff sumber, bukan pemotongan
PDF; daftar isi, bibliografi, indeks, dan daftar notasi dibangun secara normal.

## Cakupan terjemahan

Manifes memuat 333 unit yang diterima:

- R006: 268 unit; Jilid I lengkap dan Jilid II sampai akhir Subbagian 11.4.1;
- R007: 15 unit; pendahuluan lengkap dan Bab 1 sampai rumus integral tentu
  untuk kondisi awal;
- R008: 50 unit; sampai akhir bagian bola Riemann.

Manifes adalah 478.547 byte dengan SHA-256
`de03bdf56a20104420dde65bbb47778189f58a97134b6867aa32f6cbd1ba0385`.
Tidak ada ID unit duplikat dan seluruh hash komponen valid. Unit baru menutup
teorema identitas, seluruh latihan deret pangkat, dan subbagian eksponensial
kompleks tanpa mengubah identitas struktur sumber.

## Backend modular v0.4

Checkpoint `v0.4-live-2026.08.24-u333-a` memuat 2.692 rekaman netral-lokal,
666 rekaman ekspresi, dan lima belas proyeksi CSV. Dua build independen
masing-masing menghasilkan 26 berkas, 11.574.002 byte, dan tidak mempunyai
satu pun perbedaan path, ukuran, atau hash. Hash inventaris kanonik adalah
`d0aac7d8017ba5f6540f5fa1ab344982146ab35347d7f7337d38513948823bf1`.
Validasi tiga skema JSON, integritas referensial UUID, dialek CSV, dan
putar-balik tepat 2.692 rekaman semuanya lulus. Build replay tidak disertakan
agar byte tidak digandakan.

## QA istilah, matematika, dan layout

Pencarian arXiv terbatas tidak menemukan sumber matematika berbahasa Indonesia
dengan sumber TeX yang dapat diunduh. Sebagai fallback yang dinyatakan secara
jujur, buku analisis kompleks Indonesia karya Zetriuslita diperiksa melalui
ekstraksi dan render halaman. Audit itu menguatkan istilah hidup, termasuk
`fungsi analitik`, `lingkungan`, `deret pangkat`, `jari-jari konvergensi`,
`bagian real`, `bagian imajiner`, `fungsi trigonometri`, dan `rumus Euler`.
Materi bukti berhak cipta tidak disertakan; hanya laporan keputusan tersanitasi
yang dipublikasikan.

Build cutoff mempunyai 638 ID unik; hanya dua target setelah batas yang
sengaja dibekukan. Converter berakhir dengan nol error, lima pass TeX stabil,
semua 80 baris font tertanam, dan ekstraksi tidak memuat U+FFFD atau referensi
`??`. PDF tidak terenkripsi, tidak memuat JavaScript atau AcroForm, dan
mempertahankan 29 tujuan outline. PDF belum bertag dan 54 dari 80 baris objek
font—terutama font matematika lama—tidak mempunyai ToUnicode eksplisit;
keterbatasan aksesibilitas nonblocking ini dinyatakan, bukan disembunyikan.

PDF akhir 192 halaman adalah 2.058.059 byte dengan SHA-256
`6f1f38221af120d6459cdc217e789ca1f7a9d4f353f5720db00ff271ce637061`.
Halaman 170–192 dan seluruh lokasi overfull dirender dan diperiksa, termasuk
Figure 11.7 dua panel: tidak ada clipping, overlap, glyph rusak, formula tidak
terbaca, atau blok teks yang tidak terpusat.

## Otoritas, provenance, dan lisensi

Karya sumber matematika, masing-masing oleh Jiří Lebl, dipertahankan sebagai
identitas dan jalur hak terpisah: R006 *Basic Analysis* v6.3 commit
`00f5a8635cfba0d908cd95da53068572f30687b1`; R007 *Notes on Diffy Qs*
v6.11 commit `066f96506d0954cc3efb900db0d68d121733b2dc`; dan R008 *Guide to
Cultivating Complex Analysis* v1.9 commit
`a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.

Edisi turunan memilih jalur **CC BY-SA 4.0** secara terpisah untuk ketiga
sumber. Jiří Lebl dikreditkan sebagai penulis. Penerjemahan, penyuntingan, QA
istilah, metadata aksesibilitas, dan integrasi backend dilakukan oleh
**OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi pengguna. Ini bukan edisi
resmi dan tidak menyiratkan dukungan penulis atau institusi mana pun.

Zenodo mempertahankan concept DOI `10.5281/zenodo.22059779`; versi U333 adalah
`10.5281/zenodo.22076849`. Repositori publik berada di
<https://github.com/KokunoYumeto/lebl-mathematics-family-id> dan rilis GitHub
`lebl-family-id-wip.2026.08.24.u333` mencerminkan aset substantif yang sama.
