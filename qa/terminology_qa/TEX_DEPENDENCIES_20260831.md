# Dependensi TeX tersemat untuk build patch terminologi

Status: **PASS**

Build pembaca R007 dan R008 memakai sumber upstream yang sudah dipatok pada
versi buku masing-masing serta tiga berkas runtime TeX berikut. Berkas disalin
dari arsip runtime resmi CTAN/TeX Live, diverifikasi sebelum dipakai, dan
disimpan bersama skrip build agar build tidak bergantung pada pemasangan paket
otomatis MiKTeX.

| Berkas | Versi | Lisensi | Byte | SHA-256 |
|---|---:|---|---:|---|
| `qa/terminology_qa/tex-deps/tasks-v1.4a/tasks.sty` | 1.4a (2022-01-08) | LPPL-1.3c-or-later | 32.338 | `2e36d1338e5634939be9303ca0f8bdaab20e7e5aa067da36e124b7c6bcf41dac` |
| `qa/terminology_qa/tex-deps/tasks-v1.4a/tasks.cfg` | 1.4a | LPPL-1.3c-or-later | 1.243 | `f0fb11ea45bb2145138d482d8b850244133150dea9fcad98c91df0b076b34d61` |
| `qa/terminology_qa/tex-deps/faktor-v0.1b/faktor.sty` | 0.1b (2006-04-05) | LPPL-1.3b-or-later | 1.832 | `56bb3be229f581c618360841571836a83d4aa4b2136b9ac541140e0a5671f0ad` |

Sumber primer:

- `tasks`: <https://ctan.org/pkg/tasks>
- `faktor`: <https://ctan.org/pkg/faktor>
- arsip runtime resmi: <https://mirrors.ctan.org/systems/texlive/tlnet/archive/>

Skrip `build_terminology_patch_readers.ps1` menolak build jika salah satu hash
di atas tidak cocok. Hak cipta, atribusi, dan pemberitahuan LPPL asli tetap ada
di header tiap berkas.
