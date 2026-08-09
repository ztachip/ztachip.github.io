# Deployment

## If this is a new `ztachip.github.io` repository

Extract **the contents of the archive directly into the repository root**.
After extraction the repository root should contain:

```text
.github/
docs/
requirements.txt
Makefile
README.md
DEPLOY.md
```

Do **not** create an extra `ztachip.github.io/ztachip.github.io/` directory.

Commit and push:

```bash
git add .
git commit -m "Add ztachip documentation website"
git push
```

Then in GitHub:

1. Open **Settings -> Pages**.
2. Under **Build and deployment**, choose **GitHub Actions**.
3. Open the **Actions** tab and wait for the documentation workflow to finish.
4. The site will be published at `https://ztachip.github.io/`.

## If you already cloned the repo locally

From the repository root:

```bash
tar -xzf ztachip-documentation-site.tar.gz
```

The archive is intentionally created without a wrapping top-level directory,
so it expands directly into the repository root.
