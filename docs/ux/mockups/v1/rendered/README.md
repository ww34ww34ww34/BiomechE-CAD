# BiomechE-CAD — Rendered Visual Reference Archive

**Status:** ARCHIVE CONTRACT READY / PNG BINARIES NOT YET STORED  
**Date:** 2026-08-16  
**Source:** `../biomeche-cad-mockups-v1.html`  
**Browser audit:** `../../VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md`

This directory is the canonical destination for rendered visual-reference captures.

## Target filenames

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

## Required manifest metadata for each binary

```text
screenId
sourceHtmlBlobSha
sourceCommitSha
browserName
browserVersion
viewportCssPx
deviceScaleFactor
theme
captureTimestamp
sha256
fileSizeBytes
visualAuditRef
```

## Current execution state

A Chromium/CDP pass executed all `M01..M14` and generated PNG captures during the 2026-08-16 audit. The transient sandbox was reset before the binary files could be transferred to GitHub, and the available GitHub contents connector did not expose a direct local-binary upload path in that session.

Therefore:

```text
RENDER EXECUTION      DONE — 14/14
BROWSER AUDIT         DONE — PASS WITH CORRECTIVE ITEMS
REPOSITORY PNG FILES  NOT YET STORED
```

Do not create placeholder PNGs and do not label this directory as a golden binary archive until the actual captures are stored and hashed.

The absence of binary PNG copies does not alter semantic or interaction authority:

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
HTML SOURCE           = CANONICAL VISUAL/INTERACTION SOURCE
PNG CAPTURE           = RENDERED REFERENCE ARTIFACT
```
