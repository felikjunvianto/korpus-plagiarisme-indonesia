# README #

* [Versi Bahasa Indonesia](#versi-bahasa-indonesia)
* [English Version](#english-version)

# Versi Bahasa Indonesia #

## Perkenalan ##

Korpus ini terdiri dari kumpulan dokumen dalam Bahasa Indonesia yang telah disisipkan beberapa kasus plagiarisme buatan. Korpus ini disusun dan digunakan sebagai bahan pengujian dalam tugas akhir saya yang berjudul ["Perbaikan Komponen Candidate Retrieval untuk Meningkatkan Kinerja Metode Deteksi Plagiarisme Eksternal pada Dokumen Berbahasa Indonesia"](http://lontar.cs.ui.ac.id/Lontar/opac/themes/ng/detail.jsp?id=42843&lokasi=lokal).

Korpus ini disusun dengan mengikuti format korpus kompetisi deteksi plagiarisme [PAN 2011](http://www.uni-weimar.de/medien/webis/events/pan-11/pan11-web/plagiarism-detection.html). Kasus plagiarisme buatan disusun dengan mengikuti pedoman yang dijabarkan dalam publikasi ["An Evaluation Framework for Plagiarisme Evaluation"](http://www.uni-weimar.de/medien/webis/publications/papers/stein_2010p.pdf#page=4) oleh Potthast et. al (2011).

Korpus ini berisi 65 dokumen berbahasa Indonesia dengan total 94 kasus plagiarisme buatan.

## Pengumpulan dan Prapemrosesan Dokumen ##

Kumpulan dokumen dalam korpus ini didapat dari sumber berikut.

- terjemahan artikel PAN CLEF,
- blog-blog berbahasa Indonesia,
- korpus lain (artikel Kompas & ulasan film),
- artikel pilihan Wikipedia bahasa Indonesia, dan
- novel Indonesia (lokal & terjemahan).

Setelah dikumpulkan, dilakukan tahap prapemrosesan pada setiap dokumen dengan langkah-langkah berikut.

- melakukan normalisasi agar setiap baris pada dokumen mengandung maksimal 100 karakter.
- menghilangkan spasi berlebih di akhir paragraf, antar paragraf, dan sebelum tanda baca.
- membuang dan mengganti beberapa karakter non-ASCII menjadi karakter ASCII, contohnya karakter ” pada isi dokumen diganti menjadi karakter ".

Statistik dari korpus plagiarisme bahasa Indonesia ini adalah sebagai berikut.

**Statistik dokumen**

- Dokumen sumber = **30**
- Dokumen mencurigakan = **35**
  - berisi kasus plagiarisme = **20**
  - tanpa kasus plagiarisme = **15**

**Statistik kasus plagiarisme**

- Kasus plagiarisme yang disimulasi = **45**
- Kasus plagiarisme buatan = **49**
	- salinan utuh (`no obfuscation`) = **11**
	- pengocokan urutan kata secara acak (`random-shuffling`) = **14**
	- penggantian dengan padanan kata (`semantic-variation`) = **18**
	- pengocokan kata dengan mempertahankan urutan POS/*part-of-speech* (`pos-preserving`) = **6**

## Panduan Penggunaan ##

## Lisensi ##

![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)

Korpus ini didaftarkan di bawah lisensi Creative Commons Attribution 4.0 International. Untuk melihat salinan dari lisensi ini, kunjungi laman http://creativecommons.org/licenses/by/4.0/.

## Kontak ##

Jika Anda memiliki saran, masukan, dan/atau pertanyaan, silakan langsung [membuat issue baru](https://github.com/felikjunvianto/korpus-plagiarisme-indonesia/issues/new) atau mengirimkan surel ke saya melalui [felikjunvianto93 {at} gmail {dot} com](mailto:felikjunvianto93@gmail.com).

# English Version #

## Introduction ##

This corpus consists of documents in Bahasa Indonesia which has been inserted with some artificial plagiarism cases. This corpus was compiled and used as test case in my undergraduate thesis which titled ["Improvement on Candidate Retrieval Component to Enhance Performance of External Plagiarism Detection Method on Indonesian Documents"](http://lontar.cs.ui.ac.id/Lontar/opac/themes/ng/detail.jsp?id=42843&lokasi=lokal).

This corpus was compiled while following the format of plagiarism detection competition corpus of [PAN 2011](http://www.uni-weimar.de/medien/webis/events/pan-11/pan11-web/plagiarism-detection.html). The inserted artificial plagiarism cases were compiled while following the outlined guide in ["An Evaluation Framework for Plagiarisme Evaluation"](http://www.uni-weimar.de/medien/webis/publications/papers/stein_2010p.pdf#page=4) publication by Potthast et. al (2011).

This corpus consists of 65 Indonesian documents and a total of 94 artificial plagiarism cases.

## Document Curating and Preprocessing ##

## How to Use ##

## License ##

![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)

This corpus is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

## Contact ##

If you have any suggestions and/or questions, don't hesitate to [create new issue](https://github.com/felikjunvianto/korpus-plagiarisme-indonesia/issues/new) or shoot me an email to [felikjunvianto93 {at} gmail {dot} com](mailto:felikjunvianto93@gmail.com).
