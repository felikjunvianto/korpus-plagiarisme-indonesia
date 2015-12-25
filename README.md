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

Korpus ini disusun dengan mengikuti format korpus kompetisi deteksi plagiarisme [PAN 2011](http://www.uni-weimar.de/medien/webis/events/pan-11/pan11-web/plagiarism-detection.html). Kasus plagiarisme buatan disusun dengan mengikuti pedoman yang dijabarkan dalam publikasi ["An Evaluation Framework for Plagiarism Evaluation"](http://www.uni-weimar.de/medien/webis/publications/papers/stein_2010p.pdf#page=4) oleh Potthast et. al (2011).

Korpus ini berisi 65 dokumen berbahasa Indonesia dalam teks biasa (*plaintext*) dengan total 94 kasus plagiarisme buatan.

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

Untuk menggunakan korpus ini sebagai kasus uji metode deteksi plagiarisme yang sedang Anda kembangkan, Anda cukup meng-[*clone*](https://help.github.com/articles/which-remote-url-should-i-use/) atau [mengunduh](https://github.com/felikjunvianto/korpus-plagiarisme-indonesia/archive/master.zip) repositori ini ke komputer Anda. Anda kemudian akan mendapati isi dari korpus ini, yaitu dua buah direktori sebagai berikut.

- `source-documents/`: berisi dokumen-dokumen yang **dicurigai diplagiat**. Semua kasus plagiarisme buatan dalam korpus ini dijamin memplagiat potongan teks dalam dokumen yang terdapat pada direktori ini.
- `suspicious-documents/`: direktori berisi dokumen-dokumen yang **dicurigai memplagiat** atau **mengandung bagian teks yang memplagiat**.

Untuk setiap dokumen mencurigakan dalam direktori `suspicious-documents/`, disediakan "kunci jawaban" dalam format XML yang berisi informasi mengenai potongan teks mana yang memplagiat (jika ada) beserta potongan teks mana yang diplagiat. Sebagai contoh, berikut adalah potongan isi dari berkas `suspicious-document-00014.xml` (kunci jawaban untuk dokumen mencurigakan `suspicious-document-00014.txt`):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<document reference="suspicious-document00014.txt">
	<feature name="plagiarism" type="simulated" this_offset="1331" this_length="1117" source_reference="source-document00022.txt" source_offset="58120" source_length="2237"/>
	<feature name="plagiarism" type="simulated" this_offset="3153" this_length="347" source_reference="source-document00026.txt" source_offset="100621" source_length="365"/>
...
```

Setiap `<feature>` dalam berkas `suspicious-document-00014.xml` menyatakan sebuah kasus plagiarisme. Lokasi dari bagian teks yang memplagiat dan bagian teks yang diplagiat dapat diturunkan dari atribut `<feature>` berikut:

- `this_offset`: menyatakan posisi karakter pertama dari bagian teks yang memplagiat dalam dokumen mencurigakan, dihitung dari awal dokumen (*zero-based*).
- `this_length`: menyatakan panjang bagian teks yang memplagiat pada kasus plagiarisme ini.
- `source_reference`: menyatakan nama dokumen sumber yang diplagiat pada kasus plagiarisme ini.
- `source_offset`: menyatakan posisi karakter pertama dari bagian teks yang diplagiat dalam dokumen sumber, dihitung dari awal dokumen (*zero-based*).
- `source_length`: menyatakan panjang bagian teks yang diplagiat pada kasus plagiarisme ini.

Hasil deteksi metode pendeteksi plagiarisme Anda harus dicetak dalam berkas format XML yang memenuhi [skema XML berikut](http://www.uni-weimar.de/medien/webis/corpora/corpus-pan-pc-09/document.xsd), atau dengan kata lain, jika mengutip penjelasan dari [laman kompetisi deteksi plagiarisme eksternal PAN 2011](http://www.uni-weimar.de/medien/webis/events/pan-11/pan11-web/plagiarism-detection.html):

> For each suspicious document `suspicious-documentXYZ.txt` found in the evaluation corpora, your plagiarism detector shall output an XML file `suspicious-documentXYZ.xml` which contains meta information about all plagiarism cases detected within:
>
>```xml
><document reference="suspicious-documentXYZ.txt">
>  <feature name="detected-plagiarism"
>           this_offset="5"
>           this_length="1000"
>           source_reference="source-documentABC.txt"
>           source_offset="100"
>           source_length="1000"
>  />
>  ...
></document>

Untuk mengukur kinerja dari metode pendeteksi plagiarisme Anda, unduh [*script Python 2*](http://www.uni-weimar.de/medien/webis/events/pan-09/pan09-code/pan09-plagiarism-detection-performance-measures.py) yang disediakan oleh panitia perlombaan PAN 2011 untuk mengevaluasi hasil keluaran metode deteksi plagiarisme secara mandiri. Kemudian, jalankan perintah berikut dari *Command Prompt* (Windows) atau *Terminal* (Linux, Mac) komputer Anda:

```
python pan09-plagiarism-detection-performance-measures.py -p [lokasi direktori kunci jawaban disimpan] -d [lokasi direktori keluaran metode deteksi plagiarisme disimpan]
```

Untuk melihat bantuan, jalankan perintah berikut:

```
python pan09-plagiarism-detection-performance-measures.py -h
```

Berikut adalah contoh keluaran eksekusi *script* yang berhasil:

```
Reading /home/felikjunvianto/suspicious-documents
Reading /home/felikjunvianto/detection-results
Processing... (this may take a while)
Plagdet Score 0.47446724569483506
Recall 0.5761431431431431
Precision 0.8546522222222222
Granularity 1.7333333333333333
```

Evaluasi kinerja metode deteksi plagiarisme tersebut disajikan dalam 4 metrik; *Plagdet Score*, *Recall*, *Precision*, serta *Granularity*. Pembahasan lebih detil mengenai keempat metrik tersebut dapat ditemukan [di sini](http://www.uni-weimar.de/medien/webis/publications/papers/stein_2010p.pdf#page=2).

## Lisensi ##

![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)

Korpus ini didaftarkan di bawah lisensi **Creative Commons Attribution 4.0 International**. Untuk melihat salinan dari lisensi ini, kunjungi laman http://creativecommons.org/licenses/by/4.0/.

## Kontak ##

Jika Anda memiliki saran, masukan, dan/atau pertanyaan, silakan langsung [membuat issue baru](https://github.com/felikjunvianto/korpus-plagiarisme-indonesia/issues/new) atau mengirimkan surel ke saya melalui [felikjunvianto93 {at} gmail {dot} com](mailto:felikjunvianto93@gmail.com).

# English Version #

## Introduction ##

This corpus consists of documents in Bahasa Indonesia which has been inserted with some artificial plagiarism cases. This corpus was compiled and used as test case in my undergraduate thesis which titled ["Improvement on Candidate Retrieval Component to Enhance Performance of External Plagiarism Detection Method on Indonesian Documents"](http://lontar.cs.ui.ac.id/Lontar/opac/themes/ng/detail.jsp?id=42843&lokasi=lokal).

This corpus was compiled while following the format of plagiarism detection competition corpus of [PAN 2011](http://www.uni-weimar.de/medien/webis/events/pan-11/pan11-web/plagiarism-detection.html). The inserted artificial plagiarism cases were compiled while following the outlined guide in ["An Evaluation Framework for Plagiarism Evaluation"](http://www.uni-weimar.de/medien/webis/publications/papers/stein_2010p.pdf#page=4) publication by Potthast et. al (2011).

This corpus consists of 65 Indonesian plaintext documents and a total of 94 artificial plagiarism cases.

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

To use this corpus as test cases for plagiarism detection method you are currently developing, you only need to [*clone*](https://help.github.com/articles/which-remote-url-should-i-use/) or [download](https://github.com/felikjunvianto/korpus-plagiarisme-indonesia/archive/master.zip) this repository to your computer. You then will find the content of this corpus, which are two directories as follow.

- `source-documents/`: contains documents which are **suspected to be plagiarized**. All artificial plagiarism cases in this corpus are guaranteed to plagiarize passage in document from this directory.
- `suspicious-documents/`: contains documents which are **suspected to plagiarize** or **contain plagiarizing text**.

For every suspicious document in `suspicious-documents/` directory, a "answer key" has been provided in XML format, containing information regarding which part of text that is plagiarizing (if any) along with which part of text it plagiarized. For example, the following is snippet of of file `suspicious-document-00014.xml` (answer key for suspicious document `suspicious-document-00014.txt`):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<document reference="suspicious-document00014.txt">
	<feature name="plagiarism" type="simulated" this_offset="1331" this_length="1117" source_reference="source-document00022.txt" source_offset="58120" source_length="2237"/>
	<feature name="plagiarism" type="simulated" this_offset="3153" this_length="347" source_reference="source-document00026.txt" source_offset="100621" source_length="365"/>
...
```

Every `<feature>` in file `suspicious-document-00014.xml` represents a plagiarism case. Location of the plagiarizing passage and plagiarized passage can be derived from following `<feature>` attributes:

- `this_offset`: represents the first-character position of plagiarizing passage in suspicious document, counted from the start of the document (*zero-based*).
- `this_length`: represents the length of the plagiarizing passage for this plagiarism case.
- `source_reference`: represents the name of the plagiarized source document for this plagiarism case.
- `source_offset`: represents the first-character position of plagiarized passage in source document, counted from the start of the document (*zero-based*).
- `source_length`: represents the length of plagiarized passage for this plagiarism case.

Your plagiarism detection method must output the detection results in XML-format files which must be valid in respect of following [XML schema](http://www.uni-weimar.de/medien/webis/corpora/corpus-pan-pc-09/document.xsd), or in other words, quoting explanation from [PAN 2011 external plagiarism detection competition page](http://www.uni-weimar.de/medien/webis/events/pan-11/pan11-web/plagiarism-detection.html):

> For each suspicious document `suspicious-documentXYZ.txt` found in the evaluation corpora, your plagiarism detector shall output an XML file `suspicious-documentXYZ.xml` which contains meta information about all plagiarism cases detected within:
>
>```xml
><document reference="suspicious-documentXYZ.txt">
>  <feature name="detected-plagiarism"
>           this_offset="5"
>           this_length="1000"
>           source_reference="source-documentABC.txt"
>           source_offset="100"
>           source_length="1000"
>  />
>  ...
></document>

To measure the performance of your plagiarism detection method, download a [Python 2 script](http://www.uni-weimar.de/medien/webis/events/pan-09/pan09-code/pan09-plagiarism-detection-performance-measures.py) provided by the committee of PAN 2011 competition to self-evaluate the output of plagiarism detection method. Then, run the following command from *Command Prompt* (Windows) or *Terminal* (Linux, Mac) of your computer:

```
python pan09-plagiarism-detection-performance-measures.py -p [location of directory where answer keys are saved] -d [location of directory where outputs of plagiarism detection method are saved]
```

To view help, run this command:

```
python pan09-plagiarism-detection-performance-measures.py -h
```

An example of successful script execution output is as follow:

```
Reading /home/felikjunvianto/suspicious-documents
Reading /home/felikjunvianto/detection-results
Processing... (this may take a while)
Plagdet Score 0.47446724569483506
Recall 0.5761431431431431
Precision 0.8546522222222222
Granularity 1.7333333333333333
```

The performance evaluation of plagiarism detection method is presented in 4 metrics; *Plagdet Score*, *Recall*, *Precision*, and *Granularity*. More detailed explanations about these four metrics can be found [here](http://www.uni-weimar.de/medien/webis/publications/papers/stein_2010p.pdf#page=2).

## License ##

![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)

This corpus is licensed under the **Creative Commons Attribution 4.0 International License**. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

## Contact ##

If you have any suggestions and/or questions, don't hesitate to [create new issue](https://github.com/felikjunvianto/korpus-plagiarisme-indonesia/issues/new) or shoot me an email to [felikjunvianto93 {at} gmail {dot} com](mailto:felikjunvianto93@gmail.com).
