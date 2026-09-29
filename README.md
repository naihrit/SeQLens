# SeQLens: DNA Sequence Interpreter & Mutation Scanner



## Overview of the Project

SeQLens is a lightweight bioinformatics web application designed to analyze DNA nucleotide sequences. The system accepts a user-provided DNA sequence, performs transcription into messenger RNA (mRNA) codons, translates these codons into corresponding amino acid abbreviations, and cross-references the sequence against a database of documented pathogenic mutations and clinical markers.

---

## Features

* **Complementary Transcription**: Groups input sequences into 3-nucleotide codons and converts them into RNA triplets using base-pairing logic ($A \rightarrow U$, $T \rightarrow A$, $G \rightarrow C$, $C \rightarrow G$).
* **Amino Acid Translation**: Maps RNA codons to standard amino acid abbreviations (e.g., `AUG` $\rightarrow$ `Met`).


* **Clinical Mutation Detection**: Scans sequence codons for known pathological variants, including markers for Sickle Cell Anemia, Cystic Fibrosis, Beta-Thalassemia, and oncogenic driver mutations such as $TP53$, $BRAF\ V600E$, and $KRAS$.


* **Interactive UI**: Clean interface built with vanilla web technologies, featuring light and dark visualization modes.

---

## Technologies/Tools Used

* **Backend**: Python 3, Flask, Flask-CORS


* **Frontend**: HTML5, CSS3, JavaScript (Fetch API)


* **Environment & Package Management**: Python Virtual Environment (`venv`), `pip`


---

## Steps to Install & Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

```

### 2. Set Up a Virtual Environment (Recommended)

* **Windows**:
```bash
python -m venv venv
venv\Scripts\activate

```


* **macOS / Linux**:
```bash
python3 -m venv venv
source venv/bin/activate

```



### 3. Install Dependencies

Install all required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt

```

### 4. Run the Application

1. **Start the Backend API Server**:
```bash
python app.py

```


*The Flask backend server will launch at `[http://127.0.0.1:5000](http://127.0.0.1:5000)`.*
2. **Launch the User Interface**:
* Locate the `index.html` file in your project directory.
* Double-click `index.html` to open it directly in any modern web browser (Chrome, Edge, Firefox, Safari).
* Enter a DNA sequence (up to 18 characters) into the input box and click **Interpret**.



---

## Instructions for Testing

### 1. Backend API Testing (CLI / Terminal)

You can verify the backend independently from the terminal using `curl` or PowerShell:

* **macOS / Linux / Git Bash**:
```bash
curl -X POST http://127.0.0.1:5000/translate -H "Content-Type: application/json" -d '{"seq": "CAC"}'

```


* **Windows PowerShell**:
```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/translate -Method Post -ContentType "application/json" -Body '{"seq": "CAC"}'

```



### 2. Frontend Test Cases

Enter the following test sequences in the web interface to verify functionality:

| Test Case | Input DNA | Expected Codon | Expected Output |
| --- | --- | --- | --- |
| **Normal Codon** | `TAC` | `AUG` | `AUG = Met` |
| **Sickle Cell Marker** | `CAC` | `GUG` | `GUG = Val`, `GUG = Sickle Cell Anemia (HBB: p.Glu6Val / HbS)` |
| **Empty Input** | *(empty)* | N/A | Alert: *"Please Enter the DNA sequence"* |

---


### Light Mode Interface

`![Light Mode UI](screenshots/light_mode.png)`

### Dark Mode Interface & Result Output

`![Dark Mode UI](screenshots/dark_mode.png)`
