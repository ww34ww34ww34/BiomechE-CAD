#!/usr/bin/env python3
"""Reproducible BiomechE-CAD visual-reference renderer.

Reads the canonical self-contained HTML, calls its render('Mxx') entry point,
captures the frozen viewports, and writes capture-manifest.json with provenance.
This is packaging evidence only; written specs remain semantic authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError as exc:
    raise SystemExit("Python package 'playwright' is required. Install it in the render environment.") from exc

SCREENS = [
    ("M01", "M01-case-1440x960.png", 1440, 960, "light"),
    ("M02", "M02-import-1440x960.png", 1440, 960, "light"),
    ("M03", "M03-register-1440x960.png", 1440, 960, "light"),
    ("M04", "M04-base-1440x960.png", 1440, 960, "light"),
    ("M05", "M05-parametric-1440x960.png", 1440, 960, "light"),
    ("M06", "M06-corrections-1440x960.png", 1440, 960, "light"),
    ("M07", "M07-sculpt-dark-1440x960.png", 1440, 960, "dark"),
    ("M08", "M08-materials-1440x960.png", 1440, 960, "light"),
    ("M09", "M09-inspect-1440x960.png", 1440, 960, "light"),
    ("M10", "M10-biomeche-dark-1440x960.png", 1440, 960, "dark"),
    ("M11", "M11-dfm-1440x960.png", 1440, 960, "light"),
    ("M12", "M12-history-1440x960.png", 1440, 960, "light"),
    ("M13", "M13-physical-qc-1440x960.png", 1440, 960, "light"),
    ("M14", "M14-compact-1024x768.png", 1024, 768, "light+compact"),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_value(repo_root: Path, *args: str) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo_root), *args],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return None


def main() -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--html",
        type=Path,
        default=here.parent / "biomeche-cad-mockups-v1.html",
        help="Canonical self-contained HTML source",
    )
    parser.add_argument("--out", type=Path, default=here)
    parser.add_argument(
        "--chromium",
        default=shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome"),
        help="Chromium/Chrome executable path",
    )
    parser.add_argument("--settle-ms", type=int, default=100)
    args = parser.parse_args()

    if not args.chromium:
        raise SystemExit("No Chromium/Chrome executable found; pass --chromium <path>.")

    html_path = args.html.resolve()
    out_dir = args.out.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    source = html_path.read_text(encoding="utf-8")
    source_sha256 = hashlib.sha256(source.encode("utf-8")).hexdigest()

    # docs/ux/mockups/v1/rendered -> repository root is five parents up.
    repo_root = here.parents[4] if len(here.parents) >= 5 else here
    source_blob = git_value(repo_root, "hash-object", str(html_path))
    source_commit = git_value(repo_root, "rev-parse", "HEAD")

    captures = []
    runtime_errors: list[str] = []
    started = datetime.now(timezone.utc).isoformat()

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            executable_path=args.chromium,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )
        page = browser.new_page(viewport={"width": 1440, "height": 960}, device_scale_factor=1)
        page.on("pageerror", lambda exc: runtime_errors.append(str(exc)))
        page.set_content(source, wait_until="load")

        for screen_id, filename, width, height, theme in SCREENS:
            page.set_viewport_size({"width": width, "height": height})
            before = len(runtime_errors)
            page.evaluate("(id) => render(id)", screen_id)
            page.wait_for_timeout(args.settle_ms)
            target = out_dir / filename
            page.screenshot(path=str(target), full_page=False)
            captures.append(
                {
                    "screenId": screen_id,
                    "file": filename,
                    "viewportCssPx": [width, height],
                    "deviceScaleFactor": 1,
                    "theme": theme,
                    "title": page.title(),
                    "runtimeExceptions": len(runtime_errors) - before,
                    "sha256": sha256(target),
                    "fileSizeBytes": target.stat().st_size,
                }
            )

        browser_version = browser.version
        browser.close()

    manifest = {
        "schema": "BiomechE.CAD.VisualCaptureManifest/1",
        "generatedAtUtc": started,
        "sourceHtml": str(html_path),
        "sourceHtmlSha256": source_sha256,
        "sourceHtmlGitBlobSha": source_blob,
        "sourceCommitSha": source_commit,
        "browser": {"name": "Chromium", "version": browser_version},
        "renderMethod": "Playwright Page.setContent + explicit render('Mxx') + screenshot",
        "settleMs": args.settle_ms,
        "visualAuditRef": "docs/ux/VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md",
        "runtimeExceptionTotal": len(runtime_errors),
        "runtimeErrors": runtime_errors,
        "captures": captures,
    }
    (out_dir / "capture-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(manifest, indent=2))
    return 0 if not runtime_errors and len(captures) == len(SCREENS) else 2


if __name__ == "__main__":
    raise SystemExit(main())
