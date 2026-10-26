"""Stamp a new build id into index.html for cache busting.

Every local asset URL in index.html carries ?v=<build>, and the footer shows
"build <build>". Changing the id makes browsers fetch fresh CSS and icons,
and the footer tells you which version you are looking at.

Run before committing a change you want to see live right away:
  python scripts/bump_build.py
"""
import re
from datetime import datetime, timezone
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "index.html"

build = datetime.now(timezone.utc).strftime("%Y%m%d%H%M")
html = INDEX.read_text(encoding="utf-8")
html, assets = re.subn(r"\?v=[A-Za-z0-9]+", f"?v={build}", html)
html, footer = re.subn(r'(<span class="build"[^>]*>build )[^<]*', rf"\g<1>{build}", html)
INDEX.write_text(html, encoding="utf-8")
print(f"build {build}: {assets} asset urls, {footer} footer stamp")
