# Deployment

The repository is deployed automatically by `.github/workflows/pages.yml`.
GitHub Pages must be configured with **Source: GitHub Actions**.

After applying a documentation patch:

```bash
git add .
git commit -m "Reorganize ztachip documentation"
git push
```

The workflow will synchronize the five canonical guides from
`ztachip/ztachip`, convert the office-document guides with Pandoc, build the
Sphinx site, and deploy it to `https://ztachip.github.io/`.
