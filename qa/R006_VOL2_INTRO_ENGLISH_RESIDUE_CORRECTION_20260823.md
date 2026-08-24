# R006 Jilid II — koreksi residu Bahasa Inggris pada pendahuluan

Status: koreksi pembaca diterapkan; struktur dan rujukan tidak berubah.

## Temuan

Inspeksi visual independen terhadap PDF U319 pada halaman fisik 5 menemukan
bahwa lima butir jalur mata kuliah dalam
`translation/ra/frag-vol2-intro.tex` masih memuat kata pembaca
`Chapter`, `Chapters`, `chapter`, `and`, dan `maybe`. Ini bukan judul karya
atau nama diri yang harus dipertahankan; seluruh konteksnya merupakan prosa
Bahasa Indonesia. Klaim QA lama bahwa unit tersebut sepenuhnya berbahasa
Indonesia karena itu dikoreksi sebelum publikasi U319.

## Perubahan

- `Chapter`/`Chapters`/`chapter` → `Bab`;
- `and` → `dan`;
- `maybe` → `mungkin`.

Lima butir, urutan, seluruh nomor bab/bagian, komentar sumber, label, dan
rujukan tetap sama. Tidak ada rumus atau isi matematika yang berubah.

## Identitas dan QA struktural

- Sebelum: 3.840 byte; SHA-256
  `ea1aff3edf70c380659d3845ea517f1e547f2fc9364ff839b3164a50281b6f6c`.
- Sesudah: 3.831 byte; SHA-256
  `26c1a2869d7b5bf66b7877bfe26b768ef7903c0e120fa852cf729dc1e9bd2700`.
- Sebelum/sesudah: 45 kurung kurawal buka dan 45 tutup, satu pasangan
  `enumerate`, lima `item`, 35 rujukan yang diperiksa, dan 51 perintah TeX.
- Pencarian baris aktif setelah koreksi menemukan nol kemunculan
  `Chapter`, `Chapters`, `chapter`, `and`, atau `maybe` di luar komentar dan
  nama perintah/kunci TeX.
- Baris manifes `ra.v1.intro.about-book` diperbarui dengan hash target dan
  bukti QA ini; jumlah unit tetap 319.

Rebuild pembaca, ekstraksi teks, pemeriksaan font, dan inspeksi visual ulang
halaman 5–6 dicatat dalam
`qa/builds/ra-id-volume2-swapping-limits-section-reader-20260823/BUILD_RECEIPT.md`.

Provenans penerjemahan dan QA: **OpenAI Codex gpt-5.6-sol, Ultra** atas
instruksi pengguna. Jiří Lebl tetap merupakan penulis karya sumber; kredit
sumber dan kontributor manusia dipertahankan.
