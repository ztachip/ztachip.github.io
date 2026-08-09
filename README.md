# ztachip Documentation Website

This repository publishes the programmer documentation at
`https://ztachip.github.io/`.

The site follows the same five-document order as the main ztachip README:

1. Technical Overview
2. Hardware Architecture
3. Programmer Guide
4. Vision AI Stack Programmer Guide
5. MicroPython Programmer Guide

The main `ztachip/ztachip` repository remains the source of truth. During each
GitHub Pages build, `tools/sync_source_docs.py` downloads the canonical source
material. Markdown documents are cleaned up for web presentation, while the two
ODT/PDF-backed programmer guides are converted with Pandoc and their embedded
images are extracted automatically.

## Local preview

Install Pandoc, then:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make html
python3 -m http.server 8000 -d _build/html
```

Open `http://localhost:8000`.
