# BiomechE-CAD — Canonical Mockup Package v1

**Status:** ACTIVE VISUAL BASELINE — VIS-02/03  
**Date:** 2026-08-16  
**Semantic authority:** written frozen/canonical specs.  
**Visual authority:** `../../BIOMECHE_CAD_VISUAL_REFERENCE_V1.md`.

---

## Purpose

This folder contains the versioned visual reference for the BiomechE-CAD P0 workflow.

The primary editable artifact is:

```text
biomeche-cad-mockups-v1.html
```

It is deliberately self-contained and dependency-free so it can be archived, opened locally and compared across future UI implementations.

Rendered references, when produced, live under:

```text
rendered/
```

---

## Screen set

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

See `manifest.md` for requirement mapping and asset state.

---

## Authority rule

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
VISUAL REFERENCE      = SCREEN / INTERACTION INTENT
IMPLEMENTATION        = MUST BE VERIFIED AGAINST BOTH
```

If the visual source conflicts with a frozen product rule, the visual source is the defect.

---

## Visual direction

- premium medical-tech workstation;
- 3D-first authoring;
- high information density without legacy industrial-CAD chrome;
- teal/blue/sage/warm accents, no purple-dominant identity;
- explicit LEFT/RIGHT, case, revision and profile context;
- text/icon/shape + color for state;
- numeric values + units remain first-class;
- requested/realized dose is visible where applicable;
- provenance uses progressive disclosure;
- light-mode canonical baseline plus representative dark/compact coverage.

---

## Versioning

A future visual revision must create `v2/` or clearly version the changed asset and record:

```text
reason
supersedes
requirements affected
interaction changes
semantic changes (should normally be none)
validation/usability evidence if available
```

Do not overwrite the approved v1 baseline without preserving history.
