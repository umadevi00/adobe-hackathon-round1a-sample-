# Adobe Hackathon — Round 1A Submission

## 📋 Problem Statement
Extract a structured outline (Title, H1, H2, H3 with page numbers) from a PDF (≤ 50 pages) and output it in a clean JSON format.

## 🧰 Solution Overview
- Python-based PDF outline extractor using **PyMuPDF**.
- Wrapped in a lightweight Docker container.
- Works offline (no internet required).
- Compatible with **amd64, CPU-only**, ≤ 200 MB.
- Processes a 50-page PDF in ≤ 10 seconds.

## 📂 Folder Structure
```pdf_extractor/
├── Dockerfile
├── extractor.py
├── requirements.txt
├── input/ # put your PDFs here
├── output/ # JSON outputs appear here
├── README.md
├── approach_explanation.md
├── test_runtime.py # optional: measures runtime```

## 🚀 How to Run

### 📄 Build Docker Image:
```bash
docker build --platform linux/amd64 -t pdf_extractor:001 .


