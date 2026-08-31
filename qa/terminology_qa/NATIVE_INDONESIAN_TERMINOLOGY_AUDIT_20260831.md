# Audit terminologi matematika Bahasa Indonesia asli — 31 Agustus 2026

Status: PASS — audit terminologi, regenerasi manifes, replay backend, build deterministik, QA pembaca, dan validasi integritas paket rilis selesai.

## Ruang lingkup dan metode

Audit satu kali ini membandingkan istilah pembaca R006, R007, dan R008 dengan
sumber matematika yang ditulis dalam Bahasa Indonesia. Sumber hanya dipakai
sebagai saksi terminologi; prosa yang hak ciptanya terbatas tidak disalin ke
edisi. Nomor halaman di bawah adalah nomor halaman fisik PDF, disertai nomor
cetak bila berguna. Keputusan mempertimbangkan makna matematika, kelaziman
bidang, dan konsistensi seluruh keluarga buku.

Audit dilakukan oleh OpenAI Codex gpt-5.6-sol, Ultra atas instruksi pengguna.
Atribusi penulis sumber, penulis buku asli, lisensi, dan kontributor manusia
tetap dipertahankan.

## Identitas saksi

| Bidang | Sumber | Identitas byte lokal | Cakupan yang diperiksa |
|---|---|---|---|
| Analisis real | Firdaus Ubaidillah, *Analisis Real*, UNEJ Press, 2021, ISBN 978-623-6039-75-5 | `UNEJ_Analisis_Real.pdf`; 1.888.723 byte; SHA-256 `9bd4c9422be825d1073827d326de3b94f8f481c594eac953f700abea5509d33c`; 164 halaman | PDF hlm. 4, 23–24, 40–41, 78–79, 114, 118 |
| Fondasi analisis | Endang Cahya, *Pengantar Analisis Real*, MPMT5303 Modul 1, Universitas Terbuka | `UT_MPMT5303_M1.pdf`; 445.252 byte; SHA-256 `4cc8b6c2e2d522facbb7de4016e20c55891ca12db3981452d5f470e6e487d99f`; 63 halaman | PDF hlm. 3–5, 16–17, 22–23, 28, 30–31, 36–37 |
| Persamaan diferensial | Firdaus Ubaidillah, *Persamaan Diferensial Biasa*, UNEJ Press, 2020 | `UNEJ_PDB.pdf`; 1.791.039 byte; SHA-256 `7101942c6ecd49b0f5bcfe0a418e1703bb7c5a934a36de7893e2432af1cf257`; 172 halaman | PDF hlm. 22, 32, 35–39, 50–52, 65, 125–126, 153, 159 |
| Persamaan diferensial | SPADA Indonesia, mata kuliah 3062 *Persamaan Diferensial Elementer*, bagian 1 | `SPADA_PDB.html`; 88.250 byte; SHA-256 `d179175817d44dc26aa16fbd98bf31e48640bba0eb1ca929cbb7cdeb8d6ef1b7` | Modul 65515 dan 65517; snapshot baris 381, 469–481, 528–556 |
| Analisis kompleks | Ikhsanul Halikin dan Firdaus Ubaidillah, *Analisis Kompleks*, 2019 | `UNEJ_Analisis_Kompleks.pdf`; 1.646.355 byte; SHA-256 `41ec1d0c961aa1f8b94c21db511f8686304510c6fc5272f570d1967888fe14a5`; 205 halaman | PDF hlm. 50–51, 56, 60, 84, 97, 108, 137–138, 148–149, 162–163, 166, 171, 175, 180, 182, 189–190, 199 |
| Integrasi real | Solikhin dan Abdul Aziz, *Integral Riemann, McShane, dan Henstock*, Penerbit UNDIP, 2025, ISBN PDF 978-623-417-462-5 | snapshot katalog `UNDIP_Integral_catalog_816.html`; 19.852 byte; SHA-256 `1eb58cbc654efeaa335ff34ab7a9aa279a4af52cf685a3dea5c5f4e713e9df8c` | Judul, abstrak, metadata, dan lisensi CC BY-NC-SA 4.0; bukan isi buku penuh |

## Keputusan pembaca yang diterapkan

### R007 — persamaan separabel

UNEJ memakai `Persamaan Diferensial Peubah Terpisah (Separabel)` dan kemudian
`peubah terpisah atau separabel` pada PDF hlm. 32 (cetak 18), serta mengulang
`peubah terpisah (separabel)` pada PDF hlm. 37 (cetak 23). SPADA modul 65517
mencantumkan bentuk `Persamaan diferensial separable`. Dua saksi independen ini
mendukung keluarga istilah *separabel*, sedangkan bentuk lama
`persamaan terpisahkan` dapat dipahami tetapi bukan bentuk perkuliahan yang
ditunjukkan saksi.

Keputusan: gunakan `persamaan diferensial separabel` pada judul/definisi dan
`persamaan separabel` pada prosa ringkas. Delapan kemunculan semantik dalam
`translation/diffyqs/ch-first-order-ode.tex` dinormalkan. Glosarium menambahkan
`LEBL-TERM-0803`, konsep `concept.ode.separable-equation`; variasi yang dicatat
adalah `persamaan separabel` dan `persamaan diferensial peubah terpisah`.

### R007 — faktor integrasi

UNEJ memakai `faktor integrasi` pada PDF hlm. 32 dan 39; SPADA modul 65517
mencatat variasi `faktor integral`. Glosarium keluarga sejak semula memilih
`faktor integrasi`, tetapi bab R007 memakai `faktor pengintegrasi` delapan kali.

Keputusan: normalkan seluruh delapan kemunculan R007 menjadi `faktor integrasi`,
perluas cakupan `LEBL-TERM-0320` ke R006;R007, catat `faktor integral` sebagai
variasi, dan tandai bentuk lama sebagai bentuk yang tidak dipilih.

### R008 — fungsi penuh

UNEJ mendefinisikan `Fungsi penuh (entire function)` pada PDF hlm. 97 (cetak 81),
memakainya berulang pada PDF hlm. 108, 148–149, 162–163, 166, 171, dan 182,
serta mencantumkannya dalam glosarium pada PDF hlm. 199 (cetak 183). Edisi R008
sebelumnya mencampur bentuk Inggris `entire`, `fungsi menyeluruh`,
`fungsi holomorfik seluruh`, dan `fungsi seluruh` untuk konsep yang sama.

Keputusan: definisikan sekali sebagai `fungsi penuh (entire function)` dan gunakan
`fungsi penuh` sesudahnya. Seluruh 38 kemunculan konsep dinormalkan dengan
penyesuaian tata bahasa, tanpa perubahan matematika. Glosarium menambahkan
`LEBL-TERM-0804`, konsep `concept.complex-analysis.entire-function`.

### R007 — residu penghubung Inggris

QA visual pembaca menemukan enam penghubung Inggris `and` yang tersisa di
`ch-systems.tex`. Keenamnya diganti menjadi `dan` pada baris 5442, 6347, 6611,
7051, 7217, dan 7221. Receipt terpisah membuktikan bahwa itu merupakan enam
perubahan semantik tunggal dan bahwa urutan perintah, lingkungan, label,
referensi, sitasi, aset, rentang matematika, serta keseimbangan kurung kurawal
TeX tidak berubah.

## Istilah yang dipertahankan

- R006: `batas atas/bawah`, `supremum`, `infimum`, `barisan Cauchy`,
  `subbarisan`, `fungsi kontinu`, `diferensiabel`, `turunan`, `partisi`, dan
  `integral Riemann` cocok dengan saksi. `terintegral Riemann` dicatat sebagai
  variasi saksi, tetapi pilihan yang lebih eksplisit `terintegralkan secara
  Riemann` tetap dipertahankan.
- Fondasi: `elemen`, `himpunan bagian sejati`, `domain`, `daerah hasil`,
  `injektif`, `surjektif`, `bijektif`, `prinsip induksi`, dan `terhitung`
  dipertahankan. Variasi saksi tidak memerlukan perubahan pembaca.
- R007: `solusi`/`penyelesaian`, `persamaan eksak`, `masalah nilai awal`,
  `persamaan karakteristik`, `transformasi Laplace`, `titik kesetimbangan`, dan
  `stabil asimtotik` konsisten. Paket ini tidak cukup untuk memutuskan
  `syarat awal` versus `kondisi awal`; tidak dilakukan penggantian massal.
- R008: `cakram`, `domain`, `cabang utama argumen`, `fungsi holomorfik`,
  `integral garis` dengan variasi `integral lintasan`/`integral kontur`,
  `residu`, `singularitas terisolasi`, `kutub`, dan `pemetaan konformal`
  dipertahankan. Pilihan itu menjaga perbedaan matematis buku serta telah
  mempunyai variasi yang cukup dalam glosarium.

## Batas hak dan reproduksi

PDF UNEJ dan modul UT digunakan hanya sebagai bukti terminologi berhalaman.
Tidak ada prosa ekspresif, gambar, latihan, atau tata letak dari sumber tersebut
yang dimasukkan ke edisi Lebl. Snapshot SPADA dan katalog UNDIP dipakai sebagai
metadata/terminologi saja. Berkas saksi tidak termasuk dalam paket rilis.

## Gerbang penyelesaian

- [x] Identitas byte dan halaman sumber dicatat.
- [x] Perbandingan pembaca dan glosarium selesai.
- [x] Tiga koreksi terbatas diterapkan pada sumber kanonik.
- [x] Manifes 5.884 unit diregenerasi dan diverifikasi.
- [x] Dua replay backend baru identik dan lulus validasi.
- [x] Pembaca R007 dan R008 dibangun deterministik serta diperiksa visual.
- [x] Paket rilis patch GitHub dan Zenodo terikat ke lineage yang sama dan lulus validasi integritas pra-publikasi.
