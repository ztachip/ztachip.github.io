# ztachip Documentation Website

This repository publishes the programmer documentation at
`https://ztachip.github.io/`.

The site follows the same five-document order as the main ztachip README:

1. Technical Overview
2. Hardware Architecture
3. Programmer Guide
4. Vision AI Stack Programmer Guide
5. MicroPython Programmer Guide

The documentation is stored directly in this repository as web-native Markdown.
The Programmer Guide and Vision AI Stack Programmer Guide are static web
conversions of the original PDF documents, with their technical content
preserved and obvious spelling and grammar errors corrected.

GitHub Pages does not download or convert the source PDFs during a build. The
workflow only builds the committed Markdown and image assets with MkDocs.

## Local preview

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000/`.
