#!/usr/bin/env python3
"""Synchronize the five canonical ztachip guides into the Sphinx site.

The main source repository remains the source of truth. Markdown guides are
fetched directly. The two office-document guides are converted to MyST-friendly
Markdown with Pandoc, including embedded images.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
STATIC = DOCS / "_static" / "source"
RAW = "https://raw.githubusercontent.com/ztachip/ztachip/refs/heads/master/"
GITHUB = "https://github.com/ztachip/ztachip/blob/master/"

SOURCES = {
    "technical": "Documentation/Overview.md",
    "hardware": "Documentation/HardwareDesign.md",
    "micropython": "micropython/MicropythonUserGuide.md",
    "programmer_odt": "Documentation/ztachip_programmer_guide.odt",
    "vision_odt": "Documentation/visionai_programmer_guide.odt",
}

# Conservative editorial fixes only. These correct spelling, grammar, and
# terminology without changing examples, algorithms, interfaces, or meaning.
TEXT_REPLACEMENTS = [
    (r"\bopensourse\b", "open-source"),
    (r"\bOpensourse\b", "Open-source"),
    (r"\bRISCV\b", "RISC-V"),
    (r"\bRiscV\b", "RISC-V"),
    (r"\bmicropython\b", "MicroPython"),
    (r"\bMicropython\b", "MicroPython"),
    (r"\bconverage\b", "coverage"),
    (r"\bGuassian\b", "Gaussian"),
    (r"\bMobinet\b", "MobileNet"),
    (r"\bSSD-Mobinet\b", "SSD-MobileNet"),
    (r"\bCorder Detection\b", "Corner Detection"),
    (r"\bseperate\b", "separate"),
    (r"\bSeperate\b", "Separate"),
    (r"\bextentions\b", "extensions"),
    (r"\bupto\b", "up to"),
    (r"\bhighlevel\b", "high-level"),
    (r"\boverlayed\b", "overlaid"),
    (r"\bdont\b", "don't"),
    (r"\barithmetics\b", "arithmetic"),
    (r"\bsysthesis\b", "synthesis"),
    (r"\bBistream\b", "Bitstream"),
    (r"\bDevlopment\b", "Development"),
    (r"\bPCORES\b", "P-cores"),
    (r"\bPCOREs\b", "P-cores"),
]

PHRASE_REPLACEMENTS = [
    ("used to moved data", "used to move data"),
    ("there is no memory stall cycles", "there are no memory stall cycles"),
    ("The 2 metrics", "The two metrics"),
    ("a 20GOPS of hardware computing resource", "20 GOPS of hardware computing resources"),
    ("a 8 unit wide", "an 8-unit-wide"),
    ("a 8x8 matrix", "an 8x8 matrix"),
    ("sequential steps of tensor operations", "sequence of tensor operations"),
    ("applied to efficiently compared to", "applied efficiently compared with"),
    ("ztachip domain are applications", "The ztachip domain consists of applications"),
    ("Tensor-core programs are codes", "Tensor-core programs are code"),
    ("PCORE programs are codes", "P-core programs are code"),
    ("Please familiar yourself", "Please familiarize yourself"),
    ("Each instructions can perform", "Each instruction can perform"),
    ("you dont have to", "you don't have to"),
    ("You would normally assigned", "You would normally assign"),
]


def fetch(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "ztachip-docs-build/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r, dest.open("wb") as f:
        shutil.copyfileobj(r, f)


def edit_prose(markdown: str) -> str:
    """Apply editorial fixes outside fenced code blocks and inline code."""
    chunks = re.split(r"(```.*?```)", markdown, flags=re.S)
    for i in range(0, len(chunks), 2):
        # Protect inline code from terminology replacements.
        inline = re.split(r"(`[^`\n]+`)", chunks[i])
        for j in range(0, len(inline), 2):
            text = inline[j]
            for pattern, replacement in TEXT_REPLACEMENTS:
                text = re.sub(pattern, replacement, text)
            for old, new in PHRASE_REPLACEMENTS:
                text = text.replace(old, new)
            # Web-style punctuation/spacing cleanup only.
            text = re.sub(r"\b([0-9]+)fps\b", r"\1 FPS", text)
            text = re.sub(r"\b([0-9]+)GOPS\b", r"\1 GOPS", text)
            text = text.replace("etc...", "etc.")
            inline[j] = text
        chunks[i] = "".join(inline)
    return "".join(chunks)


def rewrite_repo_links(md: str, source_dir: str, image_prefix: str) -> str:
    """Make source-repository links work from the separate Pages repository."""
    # Images in the source Markdown live under Documentation/images.
    if source_dir == "Documentation":
        md = re.sub(
            r"(!\[[^\]]*\]\()images/([^\)]+)(\))",
            lambda m: f"{m.group(1)}{image_prefix}/{m.group(2)}{m.group(3)}",
            md,
        )
    # Relative links to RTL/SW files should point back to the canonical repo.
    def link_repl(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        if target.startswith(("http://", "https://", "#", "/")):
            return match.group(0)
        if target.startswith("images/"):
            return match.group(0)
        base_parts = Path(source_dir).parts
        resolved = Path(*base_parts, target)
        # Normalize ../ components without requiring the target to exist.
        parts: list[str] = []
        for part in resolved.parts:
            if part == "..":
                if parts:
                    parts.pop()
            elif part != ".":
                parts.append(part)
        url = GITHUB + "/".join(parts)
        return f"[{label}]({url})"
    md = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", link_repl, md)
    return md


def sync_source_images(md: str, source_subdir: str, site_subdir: str) -> str:
    """Download source Markdown images locally and rewrite their paths."""
    refs = sorted(set(re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md)))
    for ref in refs:
        if not ref.startswith(source_subdir + "/"):
            continue
        filename = ref[len(source_subdir) + 1 :]
        remote = RAW + "Documentation/images/" + filename
        local = STATIC / site_subdir / filename
        try:
            fetch(remote, local)
        except Exception as exc:
            print(f"warning: could not fetch image {remote}: {exc}", file=sys.stderr)
    return md


def prepare_markdown(source: str, dest: Path, title: str, image_area: str) -> None:
    with tempfile.TemporaryDirectory() as td:
        raw = Path(td) / "source.md"
        fetch(RAW + source, raw)
        md = raw.read_text(encoding="utf-8")
    md = edit_prose(md)
    # Avoid duplicate page titles while preserving the original first heading as
    # a section when it differs from the page title.
    if source.endswith("Overview.md") and md.startswith("# Abstract"):
        md = "## Abstract" + md[len("# Abstract"):]
    elif source.endswith("HardwareDesign.md") and md.lower().startswith("# hardware architecture"):
        md = md.split("\n", 1)[1].lstrip()
    elif source.endswith("MicropythonUserGuide.md"):
        first = md.splitlines()[0] if md.splitlines() else ""
        if first.startswith("#"):
            md = "\n".join(md.splitlines()[1:]).lstrip()
    image_prefix = f"_static/source/{image_area}"
    md = rewrite_repo_links(md, str(Path(source).parent), image_prefix)
    md = sync_source_images(md, image_prefix, image_area)
    banner = (
        f"# {title}\n\n"
        "```{admonition} Source of truth\n"
        ":class: tip\n"
        "This web page is synchronized from the corresponding document in the "
        "main `ztachip/ztachip` repository. Technical content and examples are "
        "preserved; only web formatting and editorial corrections are applied.\n"
        "```\n\n"
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(banner + md.rstrip() + "\n", encoding="utf-8")


def convert_odt(source: str, outdir: Path, guide_title: str, media_name: str) -> None:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc is required to convert the ODT programmer guides")

    outdir.mkdir(parents=True, exist_ok=True)
    media_dir = STATIC / "media" / media_name
    if media_dir.exists():
        shutil.rmtree(media_dir)
    media_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        odt = td_path / "guide.odt"
        converted = td_path / "guide.md"
        extracted = td_path / "media"
        fetch(RAW + source, odt)
        subprocess.run(
            [pandoc, str(odt), "--from=odt", "--to=gfm", "--wrap=none",
             f"--extract-media={extracted}", "-o", str(converted)],
            check=True,
        )
        md = converted.read_text(encoding="utf-8")
        # Pandoc typically extracts under media/media/...; copy all payload files.
        for item in extracted.rglob("*"):
            if item.is_file():
                target = media_dir / item.name
                # De-duplicate names conservatively.
                if target.exists() and target.read_bytes() != item.read_bytes():
                    stem, suffix = target.stem, target.suffix
                    n = 2
                    while (media_dir / f"{stem}-{n}{suffix}").exists():
                        n += 1
                    target = media_dir / f"{stem}-{n}{suffix}"
                shutil.copy2(item, target)

    # Normalize all Pandoc image paths to our site media folder by filename.
    def image_repl(match: re.Match[str]) -> str:
        alt, ref = match.group(1), match.group(2)
        filename = Path(ref.split("#", 1)[0]).name
        return f"![{alt}](../_static/source/media/{media_name}/{filename})"
    md = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image_repl, md)
    md = edit_prose(md)

    # Split a long office document into first-level chapters when possible.
    # This changes only presentation/navigation, never the text within sections.
    top = list(re.finditer(r"(?m)^#\s+(.+?)\s*$", md))
    if len(top) <= 1:
        body = md
        index = (
            f"# {guide_title}\n\n"
            "```{admonition} Web edition\n:class: tip\n"
            "Converted from the original ztachip office document. Figures, tables, "
            "examples, and technical content are preserved; only formatting and "
            "editorial corrections are applied.\n```\n\n" + body
        )
        (outdir / "index.md").write_text(index, encoding="utf-8")
        return

    def slug(text: str) -> str:
        s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
        return s[:70] or "section"

    chapters: list[tuple[str, str]] = []
    intro = md[: top[0].start()].strip()
    used: set[str] = set()
    for i, m in enumerate(top):
        heading = m.group(1).strip()
        end = top[i + 1].start() if i + 1 < len(top) else len(md)
        block = md[m.start():end].strip() + "\n"
        name = slug(heading)
        base = name
        n = 2
        while name in used or name == "index":
            name = f"{base}-{n}"
            n += 1
        used.add(name)
        (outdir / f"{name}.md").write_text(block, encoding="utf-8")
        chapters.append((heading, name))

    toc = "\n".join(name for _, name in chapters)
    index = (
        f"# {guide_title}\n\n"
        "```{admonition} Web edition\n:class: tip\n"
        "Converted from the original ztachip office document. Figures, tables, "
        "examples, and technical content are preserved; only formatting and "
        "editorial corrections are applied.\n```\n\n"
        + (intro + "\n\n" if intro else "")
        + "```{toctree}\n:maxdepth: 3\n:caption: Contents\n\n"
        + toc + "\n```\n"
    )
    (outdir / "index.md").write_text(index, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-office", action="store_true", help="skip ODT conversion")
    args = parser.parse_args()

    print("Synchronizing Technical Overview...")
    prepare_markdown(SOURCES["technical"], DOCS / "technical-overview.md", "Technical Overview", "technical-overview")
    print("Synchronizing Hardware Architecture...")
    prepare_markdown(SOURCES["hardware"], DOCS / "hardware-architecture.md", "Hardware Architecture", "hardware-architecture")
    print("Synchronizing MicroPython Programmer Guide...")
    prepare_markdown(SOURCES["micropython"], DOCS / "micropython-programmer-guide.md", "MicroPython Programmer Guide", "micropython")

    if not args.skip_office:
        print("Converting Programmer Guide...")
        convert_odt(SOURCES["programmer_odt"], DOCS / "programmer-guide", "Programmer Guide", "programmer-guide")
        print("Converting Vision AI Stack Programmer Guide...")
        convert_odt(SOURCES["vision_odt"], DOCS / "vision-ai-stack-programmer-guide", "Vision AI Stack Programmer Guide", "vision-ai-stack")

    print("Documentation synchronization complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
