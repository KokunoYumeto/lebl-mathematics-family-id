# Production backend checkpoint v0.3

Paket publik U216 hanya memuat `v0.3/`, snapshot produksi yang tervalidasi dan
terikat hash untuk 167 unit R006. Snapshot ini berisi 2.193 record, 15 proyeksi
CSV yang pulang-pergi tanpa kehilangan, validasi skema/referensi, serta bukti
dua replay byte-identik. Identitas pastinya berada di `v0.3/dataset.json` dan
`v0.3/VALIDATION.json`.

Manifes terjemahan hidup U216 memuat 216 unit, sehingga 49 unit terbaru belum
diproyeksikan sebagai backend v0.4. Jangan menafsirkan v0.3 sebagai klaim
cakupan penuh U216.

Paket ringkas sengaja tidak menyertakan pohon historis v0.1/v0.2. Oleh karena
itu, `build_production_v03.py` hanya dipertahankan sebagai referensi implementasi:
generator tersebut memerlukan seed v0.2 yang tidak ada dalam paket ini. Jangan
menjalankannya dan mengklaim reproduksi mandiri dari paket U216. Reproduksi
byte-identik v0.3 telah dibuktikan pada saat checkpoint dibuat; generator
backend berikutnya harus membawa seed, skema, alat, dan bukti baru secara
lengkap serta menaikkan versi bersama-sama.
