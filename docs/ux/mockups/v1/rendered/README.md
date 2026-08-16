# BiomechE-CAD — Rendered Visual Reference Archive

**Status:** REPRODUCIBLE RENDER CONTRACT COMPLETE / PNG MATERIALIZATION OPTIONAL CACHE  
**Date:** 2026-08-16  
**Source:** `../biomeche-cad-mockups-v1.html`  
**Renderer:** `render_reference.py`  
**Browser audit:** `../../VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md`

This directory owns the reproducible rendered-reference contract for the canonical M01..M14 visual baseline.

## Authority model

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
HTML SOURCE           = CANONICAL VISUAL / INTERACTION SOURCE
RENDERER + MANIFEST   = REPRODUCIBLE RENDER EVIDENCE
PNG FILE              = DERIVED MATERIALIZED REFERENCE / CACHE
```

A committed PNG is therefore useful for review convenience but is not required to preserve product or visual semantics when the exact source and renderer remain versioned and the capture can be regenerated deterministically.

## Canonical target filenames

```text
M01-case-1440x960.png
M02-import-1440x960.png
M03-register-1440x960.png
M04-base-1440x960.png
M05-parametric-1440x960.png
M06-corrections-1440x960.png
M07-sculpt-dark-1440x960.png
M08-materials-1440x960.png
M09-inspect-1440x960.png
M10-biomeche-dark-1440x960.png
M11-dfm-1440x960.png
M12-history-1440x960.png
M13-physical-qc-1440x960.png
M14-compact-1024x768.png
```

## Reproduce the archive

The renderer uses the same evidence shape as the completed browser audit: Playwright drives an installed Chromium, loads the self-contained HTML with `Page.setContent`, explicitly executes `render('Mxx')`, captures the frozen viewport and writes `capture-manifest.json`.

Example from the repository root:

```bash
python docs/ux/mockups/v1/rendered/render_reference.py \
  --chromium /path/to/chromium
```

Requirements:

```text
Python 3
Python package: playwright
Chromium / Chrome executable
```

The script does **not** download a browser and does not require network access when those prerequisites already exist.

## Generated manifest metadata

For every capture the generated `capture-manifest.json` records:

```text
screenId
file
sourceHtmlSha256
sourceHtmlGitBlobSha
sourceCommitSha
browser name/version
viewportCssPx
deviceScaleFactor
theme
capture timestamp
runtime exception count
sha256
fileSizeBytes
visualAuditRef
```

## Validation state

The canonical browser audit already executed all `M01..M14` using Chromium `144.0.7559.96`:

```text
M01..M13             1440 x 960
M14                  1024 x 768
M07 / M10            dark reference
runtime exceptions   0
VIS-04R               PASS WITH corrective items
```

A second renderer-validation run performed while adding `render_reference.py` again executed all 14 screens with zero runtime exceptions on Chromium `144.0.7559.96`. It used the same source-equivalent reconstruction methodology documented by the original audit; it is implementation validation of the renderer, not a replacement for the canonical audit record.

## Storage policy

The repository does not require binary PNG duplication as an architecture, semantic or documentation gate. Materialize and commit PNGs only when a review/release process specifically benefits from frozen binary copies.

Do not create placeholder images. If materialized PNGs are committed, keep `capture-manifest.json` beside them and verify its hashes.
