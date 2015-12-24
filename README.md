# README #

- [Versi Bahasa Indonesia](#versi-bahasa-indonesia)
  - [Pendahuluan](#pendahuluan)
  - [Pengumpulan dan Prapemrosesan Dokumen](#pengumpulan-dan-prapemrosesan-dokumen)
  - [Panduan Penggunaan](#panduan-penggunaan)
  - [Lisensi](#lisensi)
  - [Kontak](#kontak)
- [English Version](#english-version)
  - [Introduction](#introduction)
  - [Document Curating and Preprocessing](#document-curating-and-preprocessing)
  - [How to Use](#how-to-use)
  - [License](#license)
  - [Contact](#contact)

# Versi Bahasa Indonesia #

## Pendahuluan ##

Korpus ini terdiri dari kumpulan dokumen dalam Bahasa Indonesia yang telah disisipkan beberapa kasus plagiarisme buatan. Korpus ini disusun dan digunakan sebagai bahan pengujian dalam tugas akhir saya yang berjudul ["Perbaikan Komponen Candidate Retrieval untuk Meningkatkan Kinerja Metode Deteksi Plagiarisme Eksternal pada Dokumen Berbahasa Indonesia"](http://lontar.cs.ui.ac.id/Lontar/opac/themes/ng/detail.jsp?id=42843&lokasi=lokal).

Korpus ini disusun dengan mengikuti format korpus kompetisi deteksi plagiarisme [PAN 2011](http://www.uni-weimar.de/medien/webis/events/pan-11/pan11-web/plagiarism-detection.html). Kasus plagiarisme buatan disusun dengan mengikuti pedoman yang dijabarkan dalam publikasi ["An Evaluation Framework for Plagiarisme Evaluation"](http://www.uni-weimar.de/medien/webis/publications/papers/stein_2010p.pdf#page=4) oleh Potthast et. al (2011).

Korpus ini berisi 65 dokumen berbahasa Indonesia dengan total 94 kasus plagiarisme buatan.

## Pengumpulan dan Prapemrosesan Dokumen ##

Kumpulan dokumen dalam korpus ini didapat dari sumber berikut.

- terjemahan artikel PAN CLEF,
- blog-blog berbahasa Indonesia,
- korpus-korpus lain (artikel [Kompas](http://www.kompas.com/) & ulasan film),
- [artikel pilihan Wikipedia bahasa Indonesia](https://id.wikipedia.org/wiki/Wikipedia:Artikel_pilihan), dan
- novel berbahasa Indonesia (lokal & terjemahan).

Setelah dikumpulkan, dilakukan tahap prapemrosesan pada setiap dokumen dengan langkah-langkah berikut.

- melakukan normalisasi agar setiap baris pada dokumen mengandung maksimal 100 karakter.
- menghilangkan spasi berlebih di akhir paragraf, antar paragraf, dan sebelum tanda baca.
- mengganti beberapa karakter non-ASCII menjadi karakter ASCII, contohnya karakter `”` pada isi dokumen diganti menjadi karakter `"`.

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
	- penggantian kata dengan sinonim, antonim, hipernim, atau hiponim secara acak (`semantic-variation`) = **18**
	- pengocokan kata dengan mempertahankan urutan POS/*part-of-speech* (`pos-preserving`) = **6**

## Panduan Penggunaan ##

[Under Construction]

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

Documents for this corpus were acquired from following sources.

- translation of PAN CLEF articles,
- Indonesian blogs,
- other corpora ([Kompas](http://www.kompas.com/) articles & film reviews),
- [featured articles from Wikipedia bahasa Indonesia](https://id.wikipedia.org/wiki/Wikipedia:Artikel_pilihan), and
- novels in bahasa Indonesia (local & translated).

After the documents were collected, each document was preprocessed with following steps.

- performing normalization so that each line of the document contains maximum of 100 characters.
- removing extra space characters at the end of paragraph, in-between paragraphs, and before any punctuation marks.
- replacing some non-ASCII characters with its ASCII counterpart, for example replacing `”` character inside document with `"` character.

Statistics of this plagiarism corpus in bahasa Indonesia are as follows.

**Document statistics**

- Source documents = **30**
- Suspicious documents = **35**
  - with plagiarism cases = **20**
  - witout plagiarism cases = **15**

**Plagiarism case statistics**

- Simulated plagiarism cases = **45**
- Artificial plagiarism cases = **49**
	- verbatim copy (`no obfuscation`) = **11**
	- shuffling word order at random (`random-shuffling`) = **14**
	- replacing words with their synonym, antonym, hypernym, or hyponym at random (`semantic-variation`) = **18**
	- shuffling word order while preserving their POS/*part-of-speech* ordering (`pos-preserving`) = **6**

## How to Use ##

[Under Construction]

## License ##

![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)

This corpus is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

## Contact ##

If you have any suggestions and/or questions, don't hesitate to [create new issue](https://github.com/felikjunvianto/korpus-plagiarisme-indonesia/issues/new) or shoot me an email to [felikjunvianto93 {at} gmail {dot} com](mailto:felikjunvianto93@gmail.com).
