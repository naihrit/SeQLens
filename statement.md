# Project Statement: SeQLens



## 1. Problem Statement



Manually analyzing raw genetic nucleotide data to transcribe DNA sequences into messenger RNA, translate codons into peptide residues, and detect known disease-causing variants is time-consuming and prone to human error. Without specialized, accessible computational tools, biology students, researchers, and introductory bioinformaticians struggle to rapidly verify base triplets, resolve amino acid sequences, and screen for clinically relevant mutations.

## 2. Scope of the Project



The scope of the SeQLens project covers the automation of the core molecular biology central dogma pipeline through an interactive web-based interface:

* Accepting short-to-medium DNA nucleotide sequences directly from the user.


* Implementing complementary Watson-Crick base-pairing transcription to generate grouped RNA triplets.


* Translating transcribed triplets into corresponding standard amino acid abbreviations.


* Cross-referencing translated codons against a curated dictionary of documented human genetic disorders, oncogenic markers, and pathology hotspots.


* Providing an accessible frontend interface featuring responsive dark/light visual display modes for ease of use.



## 3. Target Users



* **Students & Educators**: Learners in molecular biology, bioinformatics, and genetics who need a quick tool to understand transcription, translation, and point mutations.


* **Bioinformatics Researchers**: Junior researchers and lab assistants performing rapid local checks on synthetic or clinical nucleotide triplets.


* **Healthcare & Life Sciences Enthusiasts**: Individuals seeking to explore how specific nucleotide alterations correlate with genetic diseases such as Sickle Cell Anemia, Cystic Fibrosis, or specific oncogenic pathways.



## 4. High-Level Features



* **Automated DNA-to-RNA Transcription**: Automatically groups input sequences into 3-nucleotide codons and transcribes them into corresponding messenger RNA codons.


* **Peptide Chain Translation**: Matches RNA triplets to standard amino acid abbreviations using a complete genetic code lookup dictionary.


* **Pathological Variant Screening**: Automatically scans sequences against a database of clinical genetic conditions, including Hemoglobinopathies (Sickle Cell Anemia, HbC), Cystic Fibrosis ($CFTR$), and oncogenic hotspots ($TP53$, $KRAS$, $BRAF$).


* **Decoupled Architecture**: Connects a responsive browser UI to an asynchronous Python Flask REST API for backend sequence processing.


* **Interactive Mode Toggling**: Supports both light and dark themes to optimize viewing comfort during sequence analysis.
