# Batas dan reproduksi paket sumber U227

Paket ini mempertahankan pekerjaan publik pada 23 Agustus 2026.

- `translation/ra/` adalah pohon kerja LaTeX R006. Terjemahan pembaca telah
  diterima berurutan sampai bukti lengkap Teorema 10.7.2, penggantian variabel.
  Materi sesudah batas itu tetap berupa sumber upstream dan tidak diklaim telah
  diterjemahkan.
- `translation/TRANSLATION_MANIFEST.jsonl` mengikat 227 unit: 224 unit isi dan
  tiga driver pembaca, masing-masing dengan irisan sumber/sasaran dan SHA-256.
- `release/u227/` menyediakan overlay framing yang menghasilkan pembaca WIP
  Jilid II 154 halaman dan berhenti tepat setelah bukti teorema, dengan tiga
  rujukan latihan di luar cuplikan ditampilkan tanpa tautan mati.
- `control/` memuat terminologi, komponen hak, dan koreksi sumber yang diperlukan
  untuk melanjutkan produksi tanpa mengandalkan ingatan percakapan.
- `backend/production/v0.3/` adalah snapshot deterministik dan tervalidasi untuk
  167 unit. Manifes hidup berada 60 unit di depan dan belum diproyeksikan sebagai
  backend v0.4. Paket ringkas tidak memuat seed historis v0.1/v0.2, sehingga v0.3
  adalah snapshot terikat hash, bukan build yang berdiri sendiri.
- `qa/` memuat bukti build Jilid I, bukti tiga unit penutup Bagian 10.6, dan
  bukti teorema penggantian variabel dan pembaca WIP U227 154 halaman.

Urutan reproduksi pembaca U227 dijelaskan di `release/u227/README.md`. Foto
sampul ritel `cover*.png`, `cover*.xcf`, dan thumbnail terkait tidak ada dalam
paket karena haknya tidak termasuk dalam lisensi buku. Artefak tersebut tidak
diperlukan untuk membangun PDF pembaca bebas.

Lisensi turunan: CC BY-SA 4.0. Lihat `LICENSE.md`,
`translation/ra/LICENSE.md`, dan `authority/R006_AUTHORITY.md` untuk pilihan
lisensi, atribusi, identitas sumber, dan hash.
