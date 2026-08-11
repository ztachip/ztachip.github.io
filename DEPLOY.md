# Deployment

The repository is deployed automatically by `.github/workflows/pages.yml`.
GitHub Pages must be configured with **Source: GitHub Actions**.

After applying a documentation patch:

```bash
git add .
git commit -m "Update ztachip documentation"
git push
```

The workflow builds the committed Markdown and image assets with MkDocs and
deploys the generated site to `https://ztachip.github.io/`.
