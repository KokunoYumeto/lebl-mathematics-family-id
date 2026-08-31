Panduan Mengolah Analisis Kompleks: Mengolah Medan Kompleks
-----------------------------------------------------------

Buku teks matematika tingkat pascasarjana untuk satu semester mengenai analisis
kompleks dasar dalam satu peubah.  Ditulis untuk mata kuliah analisis kompleks
pascasarjana (5283) di Oklahoma State University.  Materinya sedikit lebih banyak
daripada yang dapat diselesaikan dalam satu semester agar tersedia beberapa pilihan.
Jika lampiran ruang metrik juga dibahas terlebih dahulu, materinya jauh lebih banyak
daripada yang dapat diselesaikan dalam satu semester.

Edisi ini merupakan terjemahan turunan Bahasa Indonesia dari
*Guide to Cultivating Complex Analysis* versi 1.9 karya Jiří Lebl. Terjemahan
dan penyuntingan dilakukan oleh OpenAI Codex gpt-5.6-sol, Ultra, atas instruksi
pengguna. Sumber hulu tersedia di https://github.com/jirilebl/ca dan edisi ini
dipelihara di https://github.com/KokunoYumeto/lebl-mathematics-family-id.

Lihat pula https://www.jirka.org/ca/ atau https://jirilebl.github.io/ca/.

* `ca.tex` adalah sumber utama LaTeX.
* `notations.tex` adalah daftar notasi dan entri glosarium.
* `vogtwidebar.sty` adalah dukungan tipografi lokal.
* `figures/` memuat aset gambar yang diperlukan untuk membangun buku.

Bangun dengan `pdflatex ca`, `makeindex ca`, `makeglossaries ca`, lalu jalankan
`pdflatex ca` sampai rujukan silang stabil.
