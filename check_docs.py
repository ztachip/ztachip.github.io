from pathlib import Path
import re, sys

root = Path("docs")
errors = []

for f in root.rglob("*.md"):
    txt = f.read_text(encoding="utf-8")
    for m in re.finditer(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)", txt):
        link = m.group(1)
        if link.startswith(("http://", "https://")):
            continue
        target = (f.parent / link).resolve()
        if not target.exists():
            errors.append(f"{f}: missing {link}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("Documentation link check passed.")
