import os
import json
from PyPDF2 import PdfReader

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def extract_headings(pdf_path):
    reader = PdfReader(pdf_path)
    outline = []
    title = reader.metadata.title or os.path.basename(pdf_path).replace(".pdf", "")

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        for line in text.split("\n"):
            clean = line.strip()
            if not clean:
                continue
            if clean.isupper() and 5 < len(clean) < 80:
                outline.append({"level": "H1", "text": clean, "page": i + 1})
            elif clean.istitle() and len(clean.split()) <= 6:
                outline.append({"level": "H2", "text": clean, "page": i + 1})

    return {
        "title": title,
        "outline": outline
    }

def process_all_pdfs():
    pdf_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print("⚠ No PDF files found in uploads/ folder.")
        return

    for filename in pdf_files:
        pdf_path = os.path.join(UPLOAD_FOLDER, filename)
        result = extract_headings(pdf_path)

        json_filename = os.path.splitext(filename)[0] + ".json"
        json_path = os.path.join(OUTPUT_FOLDER, json_filename)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

        print(f"✅ Processed: {filename} → {json_filename}")

if _name_ == "_main_":
    process_all_pdfs()