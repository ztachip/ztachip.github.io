# ztachip Documentation Website

This repository contains the source for the ztachip documentation website.

The documentation is built with **Sphinx**, **MyST Markdown**, and the
**Read the Docs theme** to provide the same class of navigation, search,
chapter hierarchy, and responsive presentation used by mature hardware and
software projects.

## Local preview

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make html
python3 -m http.server 8000 -d _build/html
```

Open `http://localhost:8000`.

## GitHub Pages

The included GitHub Actions workflow automatically builds and deploys the
documentation whenever the `master` branch is updated.

For an organization/user Pages repository named `ztachip.github.io`, place
the contents of this archive at the **repository root**.
