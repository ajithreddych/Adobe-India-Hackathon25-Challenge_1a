# PDF Outline Extractor – Adobe India Hackathon 2025 Round 1A

## 🧠 Problem Statement

In Round 1A: **Understand Your Document**, the goal is to build an offline system that accepts PDF documents and extracts a structured outline including:
- Title
- Headings: H1, H2, H3
- Each heading's level and page number

The output must be a valid JSON file in a defined structure, enabling machines to semantically understand document hierarchies.

---

## 📁 Input/Output Format

### 🔽 Input:
PDF files placed inside `/app/input/`

### 🔼 Output:
JSON files generated inside `/app/output/` directory in the format:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
