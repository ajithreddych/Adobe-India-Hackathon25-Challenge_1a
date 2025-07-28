# 📄 PDF Outline Extractor – Adobe India Hackathon 2025 (Round 1A)

## 🎯 Problem Statement

Build a system that reads a PDF document and extracts a structured outline containing:
- **Title**
- **Headings** (`H1`, `H2`, `H3`)
- **Level** and **page number** for each heading

This outline will be used for downstream document intelligence tasks such as semantic search and recommendation systems.

---

## 🧠 Approach

The application is implemented in `Python` and performs the following:

1. **Reads PDFs from `/app/input` directory**
2. **Extracts the document title** from the filename (as a placeholder logic)
3. **Scans each page** of the PDF using `PyPDF2`
4. **(Optional)** You can extend it to detect headings using:
   - Font size & style (requires `pdfminer.six` or `pdfplumber`)
   - Keyword or pattern matching
5. **Writes output** in structured JSON format inside `/app/output`

Currently, the outline extraction is a stub for H1/H2/H3 levels and is fully customizable for future rounds or advanced handling.

---

## 🧰 Libraries Used

- [`PyPDF2`](https://pypi.org/project/PyPDF2/): For reading PDF content
- `os`, `json`: For file system and JSON output handling

> ✅ No external models are used. The solution is heuristic-based and lightweight.

---

## 🐳 How to Build and Run 

> The system is Dockerized and fully compatible with **offline execution** on a Linux `amd64` system with no network access.

### 🔧 Build Docker Image

```bash
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .
