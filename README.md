

```markdown
# Adobe Hackathon — Round 1A Submission

## 📋 Problem Statement
Extract a structured outline (Title, H1, H2, H3 with page numbers) from a PDF (≤ 50 pages) and output it in a clean JSON format.

## 🧰 Solution Overview
- Python-based PDF outline extractor using **PyMuPDF**.
- Packaged inside a lightweight Docker container for portability.
- Works completely offline (no internet required).
- Compatible with **amd64, CPU-only**, ≤ 200 MB.
- Processes a 50-page PDF in ≤ 10 seconds.

## 📂 Folder Structure

```pdf\_extractor/
├── Dockerfile
├── extractor.py
├── requirements.txt
├── input/                # put your PDFs here
├── output/               # JSON outputs appear here
├── README.md
├── approach\_explanation.md
├── test\_runtime.py       # optional: measures runtime

```

## 🚀 How to Run

### 📄 Build Docker Image:
```bash
docker build --platform linux/amd64 -t pdf_extractor:001 .
````

### 📄 Run the Extractor:

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf_extractor:001
```

### ⏱ Optional: Measure Runtime

```bash
python test_runtime.py
```

---

## 📝 Libraries & Tools Used

### 📚 Python Libraries

* [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz`) — for reading PDF and extracting text + font information.
* `os` — to work with file paths.
* `json` — to output results in JSON.
* `time`, `subprocess` — (in `test_runtime.py`) for measuring execution time.

### 🐳 Tools

* **Python 3.10**
* **Docker** — to package the solution.

  * Base image: `python:3.10-slim`
  * No GPU, no internet, amd64 CPU-only, ≤ 200 MB.

---

## ✅ Constraints Met

* Runs within **≤ 10 seconds** for a 50-page PDF.
* Works **offline** — no network calls.
* Compatible with **amd64, CPU-only machines**.
* Model/code size ≤ 200 MB.
* No hardcoded headings or file-specific logic.
* Extracts:
  ✔ Title
  ✔ Headings (H1, H2, H3)
  ✔ Page numbers
  ✔ Outputs valid JSON in the required format.

---

## 📋 Included Files

* `Dockerfile` — defines container environment.
* `extractor.py` — core extraction logic.
* `requirements.txt` — Python dependencies (`PyMuPDF`).
* `approach_explanation.md` — explanation of methodology.
* `test_runtime.py` — optional script to measure runtime.
* `input/` — place PDFs here.
* `output/` — resulting JSONs appear here.

---
