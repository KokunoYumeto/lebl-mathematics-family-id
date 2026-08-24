# QA R006 U264 — korolari deret pangkat analitik

Tanggal: 2026-08-24  
Status: **lulus**

- Sumber: `source/ra-v6.3/ch-approximate.tex` baris 1492–1539,
  1.753 byte UTF-8/LF, SHA-256
  `a257a68269e91d4f425ae1424a2614e546b0d8fe79925d80358ebdb26ba699fb`.
- Target: `translation/ra/ch-approximate.tex` baris 1487–1534,
  1.927 byte UTF-8/LF, SHA-256
  `078daeca54b988bb0ee6fb77a66b3a3824c469dd9d345d8f9e40f10e29913612`.
- Isi: korolari bahwa deret pangkat mendefinisikan fungsi analitik di
  daerah konvergensinya, dengan reduksi kompleks melalui rotasi.

QA deterministik: 48/48 baris; 92/92 perintah; 10/10 token lingkungan;
25/25 matematika sebaris; tiga blok tampil identik setelah normalisasi teks
Indonesia dan spasi tak semantis; 61/61 pasangan kurung kurawal; 50/50
pembatas dolar; dua referensi terlindungi identik.

Audit independen: **PASS**. Ungkapan `peubah real` mempertahankan kedua
ekspresi sebaris secara persis; penyempurnaan `b bernilai real`, `z=x bernilai
real`, dan `pada titik |b|` meningkatkan kealamian tanpa mengubah isi. Tidak
ada residu Inggris, mojibake, perubahan rumus, atau cacat sumber.

Identifikasi edisi: **OpenAI Codex gpt-5.6-sol, Ultra** atas instruksi
pengguna; semua kredit sumber dan manusia dipertahankan.
