# BiomechE-CAD — Visual Reference Cross-Document Audit

**Status:** **SOURCE-LEVEL VISUAL BASELINE PASS / RENDER CAPTURE PENDING**  
**Date:** 2026-08-16  
**Phase:** `VIS-01..VIS-04`  
**Scope:** visual brief, navigable HTML mockup source, manifest and requirement mapping. Pixel/render validation is explicitly outside this result until canonical captures are rendered and reviewed.

---

## 0. Verdict

```text
VIS-01 visual/human-factors brief             PASS
VIS-02 M01..M14 mockup source                 PASS — all 14 present in navigable HTML
VIS-03 editable/source-controlled archive     PASS
VIS-03 rendered PNG reference archive         PENDING RENDER TOOLING
VIS-04 requirement ↔ screen traceability      PASS — manifest v1
SOURCE-LEVEL SEMANTIC CONFLICTS                0 blocking conflicts found
PIXEL / RENDER / BROWSER VISUAL REVIEW         NOT EXECUTED
```

This is sufficient to preserve a versioned **visual design source baseline** in the repository. It is not yet a claim that every screen has been visually inspected as a rendered 1440×960/1024×768 image.

---

# 1. Assets audited

```text
docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
docs/ux/mockups/v1/README.md
docs/ux/mockups/v1/manifest.md
docs/ux/mockups/v1/biomeche-cad-mockups-v1.html
docs/research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md
```

---

# 2. Screen completeness — PASS

The HTML screen navigator declares:

```text
M01 M02 M03 M04 M05 M06 M07 M08 M09 M10 M11 M12 M13 M14
```

The source contains individual screen definitions for the complete set and uses a single self-contained renderer/shell.

Screen set:

```text
M01 Project / Patient / Case
M02 Import / Scan qualification
M03 Registration / Landmarks
M04 Base orthosis / Template
M05 Parametric authoring
M06 Corrective / Offloading elements
M07 Sculpt / Local editing
M08 Materials / mechanical prescription
M09 Inspection / Geometry QC
M10 BiomechE Before / After / Delta
M11 DFM / Manufacturing preparation
M12 Revision / Provenance / Report
M13 Physical-part QC / Outcome follow-up
M14 Responsive / compact reference
```

---

# 3. Frozen semantic mapping audit — PASS

## M01

Preserves case/side/profile/revision context and demonstrates an unresolved opposite-side source. No diagnosis or automatic side inference introduced.

## M02

Shows `ORIGINAL`, `PROCESSED`, `REGISTERED` as distinct assets, explicit units/side/capture/processing lineage and blocking unresolved laterality.

Consistent with `20_input_scan_reference_data.md`.

## M03

Distinguishes suggested vs confirmed landmarks, registration method/version and residual measurement without presenting residual as clinical/manufacturing tolerance.

## M04

Shows a versioned semantic template without exposing `41×17`, OpenSubdiv or another engineering representation as product authority.

## M05

Shows semantic parametric operation, direct+numeric editing and requested/realized dose.

## M06

Shows named corrective element, target anatomy/ROI, landmark-relative placement, mechanical-profile separation and target/safety-region context. Mock numeric values are explicitly illustrative.

## M07

Shows replayable sculpt parameters, protected regions and explicit calculating/stale-preview language.

## M08

Shows material/mechanical prescription separately from geometry and distinguishes nominal/measured/calibrated/modelled property state.

## M09

Shows reproducible inspection context and requested/realized values; no hidden manufacturing PASS is inferred from a measured thickness.

## M10

Shows BiomechE `BASELINE / OUTCOME / DELTA`, metric/ROI/units/protocol state, numeric table and a stale-overlay warning. Heatmap remains a view over quantitative authority.

## M11

Shows committed design, manufacturing profile, DFM checks, artifact generation and **separate manufacturing release**. A missing acceptance authority is blocking.

## M12

Shows immutable revision history distinct from working state and derived manufacturing/report artifacts.

## M13

Shows `PhysicalOrthosis` identity distinct from design/artifact/run and preserves QC/service/multidimensional outcome semantics.

## M14

Shows constrained layout while retaining case, side, working/preview state and warning access. It does not claim phone/full authoring parity.

---

# 4. Human-factors evidence mapping — PASS

The visual reference maps `HF-VIS-001..010` derived from the current ISO 9241-210 / IEC 62366-1 / FDA HFE / WCAG 2.2 evidence baseline.

Source-level evidence of the following is present:

```text
context before action
non-color-only state labels/icons
numeric counterpart to drag semantics
feedback after state-changing action
stronger treatment of manufacturing release/blocking conditions
focus/selection/active side concept separation in the visual specification
dense but structured workstation layout
numeric units/legibility
provenance progressive disclosure
```

Actual accessibility contrast/target/focus behavior requires rendered/implementation evaluation.

---

# 5. Visual palette / status audit — PASS AT SPEC LEVEL

The visual brief defines:

```text
light + dark palettes
teal/blue/sage/warm medical-tech direction
no dominant purple
separate process-status vs quantitative-map color systems
text/icon/shape + color state encoding
```

No clinical meaning is encoded solely by palette choice in the specification/source design.

Actual contrast ratios have **not** been measured on rendered screens in this audit.

---

# 6. Numerical/default audit — PASS

Mockups contain sample numeric values to demonstrate formatting and requested/realized/comparison behavior.

They are explicitly labelled as mock/illustrative where a reader might otherwise infer a product default.

No mockup value has been promoted into:

```text
PRODUCT_DEFAULT
EVIDENCE_PROFILE_RULE
MANUFACTURING_ACCEPTANCE_LIMIT
OUTCOME_INTERPRETATION_RULE
ENGINEERING_PERFORMANCE_BUDGET
```

The written specs/NREG remain authority.

---

# 7. Architecture neutrality — PASS

The mockup source uses stylized SVG/CSS orthosis/scan/heatmap placeholders solely to communicate visual layout.

It does not select:

```text
OpenSubdiv
ON_SubD/openNURBS
OCCT
Manifold
any rendering engine
any UI framework
```

No geometry-engine hard gate is closed by appearance.

---

# 8. Rendered-reference gap

The planned structure includes:

```text
docs/ux/mockups/v1/rendered/M01_...png
...
docs/ux/mockups/v1/rendered/M14_...png
```

Those canonical captures are not present yet because this session did not have a connected browser/render pipeline capable of opening the newly committed repository HTML and returning deterministic viewport captures.

This gap means the following are **not yet qualified**:

```text
pixel layout at 1440×960
pixel layout at 1024×768
text clipping/overflow
actual light/dark contrast
SVG/CSS browser rendering details
responsive breakpoints in a real browser
visual density/aesthetic quality after rendering
```

The editable HTML remains the authoritative source-level mockup until captures are generated.

---

# 9. Recommended render-capture protocol

When a browser/render runner is available:

1. open the exact committed `biomeche-cad-mockups-v1.html`;
2. capture M01..M13 at 1440×960;
3. capture M14 at 1024×768;
4. capture declared dark representative screens M07 and M10 in dark mode;
5. verify no console/runtime errors;
6. inspect clipping/overflow/focus/status readability;
7. record browser/version/device-scale factor;
8. save captures under `rendered/` with manifest hashes;
9. update each manifest entry to `RENDERED / REVIEWED`;
10. rerun VIS audit before declaring visual golden baseline fully qualified.

---

# 10. VIS status

```text
VIS-01  visual brief / design system           DONE
VIS-02  canonical navigable M01..M14 source    DONE
VIS-03  source/version archive                 DONE
VIS-03R rendered image archive                 TODO
VIS-04  requirement ↔ screen traceability      DONE at source level
VIS-04R render/browser visual audit             TODO
```

---

# 11. Closure decision

The project may now use the committed HTML + manifest as its **canonical visual source reference v1** for implementation planning.

Before claiming pixel-level visual parity or using screenshots as golden regression references, complete `VIS-03R/VIS-04R`.

After this source-level visual closure, geometry-engine Q0 may resume if the project owner chooses; bibliography normalization and render capture can proceed without reopening product semantics.
