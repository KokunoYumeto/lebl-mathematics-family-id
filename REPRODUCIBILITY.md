# Batas paket sumber

Paket ini mempertahankan pekerjaan publik pada 22 Agustus 2026.

- `translation/ra/` adalah pohon kerja LaTeX R006. Terjemahan pembaca telah
  diterima secara berurutan sampai Proposisi 10.6.3 beserta buktinya pada awal
  Bagian 10.6 Jilid II. Materi setelah batas itu masih berupa sumber upstream
  dan tidak diklaim telah diterjemahkan.
- `translation/TRANSLATION_MANIFEST.jsonl` mengikat 214 unit yang telah
  diterima pada irisan sumber dan sasaran dengan SHA-256.
- `control/` memuat terminologi, komponen hak, dan koreksi sumber yang diperlukan
  untuk melanjutkan produksi tanpa mengandalkan ingatan percakapan.
- `backend/production/v0.3/` adalah snapshot deterministik dan tervalidasi untuk
  checkpoint 167 unit. Manifes hidup yang lebih baru disertakan secara terpisah
  dan belum diproyeksikan sebagai versi backend baru.
- `qa/` memuat bukti build lengkap Jilid I, bukti batas unit Jilid II terbaru,
  dan bukti build pembaca WIP 145 halaman yang dipublikasikan.

Foto sampul ritel `cover*.png`, `cover*.xcf`, dan thumbnail terkait tidak ada
dalam paket karena haknya tidak termasuk dalam lisensi buku. Artefak ini tidak
diperlukan untuk membangun PDF pembaca bebas.

Lisensi turunan: CC BY-SA 4.0. Lihat `LICENSE.md` untuk pilihan lisensi turunan
yang eksplisit, lalu `translation/ra/LICENSE.md` dan
`authority/R006_AUTHORITY.md` untuk tawaran ganda upstream, atribusi, identitas
sumber, dan hash.
