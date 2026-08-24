# Revalidasi QA terminologi Bahasa Indonesia — batas U319

Status: **lulus**. Pemeriksaan satu kali yang sudah lengkap direvalidasi pada
batas aman sebelum terjemahan berikutnya. Tidak ada perubahan isi matematika
atau perubahan pilihan utama yang dibenarkan; empat entri glosarium diperluas
dengan varian lapangan yang teramati.

## Bukti arXiv yang diperiksa ulang

- Kandidat: E. Septiati dan N. Karjanto, *Challenges in teaching Real
  Analysis classes at the University of PGRI, South Sumatra, Indonesia*,
  arXiv:2008.00182, <https://arxiv.org/abs/2008.00182>.
- Paket sumber lokal: `authority/terminology_evidence/2026-08-22-indonesian-field-usage-qa/arxiv-2008.00182-source`,
  7.868 byte, SHA-256
  `c11869e512de4b3e1e8d73a5551669d5090316a981bb17292dd01e3c560a1ec7`.
- TeX hasil dekompresi: `authority/terminology_evidence/2026-08-22-indonesian-field-usage-qa/arxiv-2008.00182.tex`,
  21.640 byte, SHA-256
  `a54893466f4297b1c90361dc588095c8a229e56d9cca6bc35127c51a67545e74`.
- Putusan: isi TeX berbahasa Inggris; afiliasi Indonesia tidak menjadikannya
  bukti terminologi matematika Bahasa Indonesia. Kandidat ditolak.

Pencarian arXiv terbatas tambahan dengan istilah `persamaan diferensial`,
`analisis kompleks`, `analisis real`, `fungsi holomorfik`, `teorema titik
tetap`, `turunan parsial`, dan `ruang metrik` tidak mengidentifikasi naskah
matematika relevan yang isi utamanya Bahasa Indonesia dan paket TeX-nya dapat
diunduh. Klaim ini hanya menyatakan hasil pencarian terbatas, bukan bukti bahwa
tidak ada naskah semacam itu di seluruh arXiv.

## Sumber pengganti tambahan

- Dr. Usmadi, M.Pd., *Analisis Real (Bahan Ajar)*, Program Studi Pendidikan
  Matematika, Universitas Muhammadiyah Sumatera Barat, 2020,
  <https://eprints.umsb.ac.id/185/1/Bahan%20Ajar%20Analisis%20Real%202020.pdf>.
- PDF lokal: `Bahan_Ajar_Analisis_Real_2020.pdf`, 471.133 byte, 48 halaman,
  SHA-256
  `ba65292b6a2230dd00f29725035386e7e8a9300d65bb6a358ba0ae45d36f3d91`.
- Ekstraksi langsung: `Bahan_Ajar_Analisis_Real_2020.txt`, 137.746 byte,
  SHA-256
  `2c09a2690f1ba868ae5239bb6a5470bc00f43f57ea21b673da43ed842450b3b9`.
- Render yang diperiksa visual: halaman PDF 13 (`persekitaran`, `kitaran`),
  23 (`persekitaran`, `himpunan terbuka`), 40 (`sub barisan`,
  Bolzano--Weierstrass, `ketaksamaan`), dan 45 (`barisan bagian`).

Sumber PDF dan render hanya merupakan bukti QA lokal dan tidak boleh masuk
paket rilis pembaca.

## Perbandingan dan putusan

| Konsep | Edisi | Sumber tambahan | Putusan |
|---|---|---|---|
| inequality | `ketaksamaan`, dengan `pertidaksamaan` kontekstual | dominan `ketaksamaan` | Pertahankan pembagian konteks; tambah entri umum LEBL-TERM-0626. |
| neighborhood | `lingkungan` | `persekitaran`; sinonim `kitaran` | Pertahankan `lingkungan`; catat kedua varian pada LEBL-TERM-0625 dan LEBL-TERM-0341. |
| subsequence | `subbarisan` | `sub barisan`; `barisan bagian` | Pertahankan bentuk tertutup yang konsisten; catat kedua varian pada LEBL-TERM-0135. |
| convergence | `konvergensi`; `konvergen` | sama | Tidak berubah. |
| open set | `himpunan terbuka` | sama | Tidak berubah. |
| supremum | `supremum`; `batas atas terkecil` | sama | Tidak berubah. |
| monotone sequence | `barisan monoton` | sama | Tidak berubah. |

Hitung korpus TeX terjemahan yang diperiksa: `ketaksamaan` 139,
`pertidaksamaan` 21, `lingkungan` 36, `persekitaran` 0, `subbarisan` 104,
`konvergensi` 127, `himpunan terbuka` 82, `supremum` 92, dan `barisan monoton`
32. Dua istilah alternatif yang hidup tetap masuk akal dalam konteksnya;
tidak ada penggantian massal yang meningkatkan makna atau konsistensi.

## Provenans dan kredit

Identifikasi yang diwajibkan hadir dalam metadata repositori, rilis, dan
driver pembaca: **OpenAI Codex gpt-5.6-sol, Ultra**. Jiří Lebl tetap merupakan
penulis karya sumber; seluruh kredit sumber dan kontributor manusia
dipertahankan.

Laporan otoritatif yang diperluas:
`authority/terminology_evidence/2026-08-22-indonesian-field-usage-qa/TERMINOLOGY_QA_REPORT.md`.
