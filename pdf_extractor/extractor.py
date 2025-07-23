import fitz  # PyMuPDF
import os
import json

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = None
    headings = []
    font_sizes = set()

    text_spans = []

    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            for l in b.get("lines", []):
                for s in l.get("spans", []):
                    text = s["text"].strip()
                    if not text:
                        continue
                    size = round(s["size"], 1)
                    font_sizes.add(size)
                    text_spans.append({
                        "text": text,
                        "size": size,
                        "page": page_num
                    })

    first_page_spans = [s for s in text_spans if s["page"] == 1]
    if first_page_spans:
        largest = max(first_page_spans, key=lambda x: x["size"])
        title = largest["text"]

    sorted_sizes = sorted(list(font_sizes), reverse=True)
    h_levels = {}
    if len(sorted_sizes) > 0: h_levels[sorted_sizes[0]] = "H1"
    if len(sorted_sizes) > 1: h_levels[sorted_sizes[1]] = "H2"
    if len(sorted_sizes) > 2: h_levels[sorted_sizes[2]] = "H3"

    outline = []
    for s in text_spans:
        level = h_levels.get(s["size"])
        if level:
            outline.append({
                "level": level,
                "text": s["text"],
                "page": s["page"]
            })

    return {
        "title": title if title else "",
        "outline": outline
    }

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        # 🔷 Fix: skip temp files and non-pdfs
        if filename.startswith("~$") or not filename.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(input_dir, filename)
        result = extract_outline(pdf_path)
        json_filename = os.path.splitext(filename)[0] + ".json"
        with open(os.path.join(output_dir, json_filename), "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
