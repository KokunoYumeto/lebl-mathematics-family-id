# QA R006 U265 — catatan penutup analitik real

Tanggal: 2026-08-24  
Status: **lulus; subbagian selesai**

- Sumber: `source/ra-v6.3/ch-approximate.tex` baris 1541–1554,
  620 byte UTF-8/LF, SHA-256
  `110a138042690e16a8579209650d870cfa545cbc7ac81438b1c71be63d3f877a`.
- Target: `translation/ra/ch-approximate.tex` baris 1536–1549,
  715 byte UTF-8/LF, SHA-256
  `b9634ee7f3f392501511ce4b5d9297174073bfffac01baeaf336ec056b5c6ee1`.
- Isi: konsekuensi global deret pangkat, contoh fungsi rasional, dan batas
  domain analitik.
- Batas berikutnya: sumber 1556 / target 1551, *Identity theorem for analytic
  functions*.

QA deterministik: 14/14 baris; 5/5 perintah; 2/2 token lingkungan; 5/5
matematika sebaris; satu blok tampil identik setelah normalisasi teks Indonesia
dan spasi tak semantis; 6/6 pasangan kurung kurawal; 10/10 pembatas dolar.

Audit independen akhir: **PASS**. Rumusan domain disempurnakan menjadi
`mendefinisikan fungsi analitik pada daerah konvergensinya` dan `di setiap
titik selain z=1`; makna global dan pengecualian tunggal tetap persis. Tidak
ada residu Inggris, mojibake, perubahan rumus, atau cacat sumber.

Identifikasi edisi: **OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi
pengguna; semua kredit sumber dan manusia dipertahankan.
