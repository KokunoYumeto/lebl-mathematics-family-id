# Batas dan reproduksi paket sumber U228

Paket ini mempertahankan pekerjaan publik pada 23 Agustus 2026.

- `translation/ra/` adalah pohon kerja LaTeX R006. Terjemahan pembaca telah
  diterima berurutan sampai akhir Bagian 10.7, penggantian variabel. Materi
  sesudah batas itu tetap berupa sumber upstream dan tidak diklaim telah
  diterjemahkan.
- `translation/TRANSLATION_MANIFEST.jsonl` mengikat 228 unit: 225 unit isi dan
  tiga driver pembaca, masing-masing dengan irisan sumber/sasaran dan SHA-256.
- `release/u228/` menyediakan overlay framing yang menghasilkan pembaca WIP
  Jilid II 155 halaman dan berhenti tepat setelah keenam latihan Bagian 10.7.
- `control/` memuat terminologi, komponen hak, dan koreksi sumber yang diperlukan
  untuk melanjutkan produksi tanpa mengandalkan ingatan percakapan.
- `backend/production/v0.3/` adalah snapshot deterministik dan tervalidasi untuk
  167 unit. Manifes hidup berada 60 unit di depan dan belum diproyeksikan sebagai
  backend v0.4. Paket ringkas tidak memuat seed historis v0.1/v0.2, sehingga v0.3
  adalah snapshot terikat hash, bukan build yang berdiri sendiri.
- `qa/` memuat bukti build Jilid I, bukti tiga unit penutup Bagian 10.6, bukti
  teorema penggantian variabel, dan pembaca WIP U228 155 halaman.

Urutan reproduksi pembaca U228 dijelaskan di `release/u228/README.md`. Foto
sampul ritel `cover*.png`, `cover*.xcf`, dan thumbnail terkait tidak ada dalam
paket karena haknya tidak termasuk dalam lisensi buku. Artefak tersebut tidak
diperlukan untuk membangun PDF pembaca bebas.

Lisensi turunan: CC BY-SA 4.0. Lihat `LICENSE.md`,
`translation/ra/LICENSE.md`, dan `authority/R006_AUTHORITY.md` untuk pilihan
lisensi, atribusi, identitas sumber, dan hash.
