# BiomechE-CAD — Architectural and Product Decisions

This file records cross-cutting decisions separately from research evidence.

**Status convention**

- `BASELINE` — current working direction used by the specification; may be refined by a later explicit decision.
- `FROZEN` — implementation should treat the decision as stable until explicitly superseded.
- `OPEN` — not decided.

---

## D-CAD-001 — Markdown is the canonical specification source

**Status:** BASELINE  
**Date:** 2026-08-14

Canonical project specifications and handover material live as Markdown under `docs/`. PDF/DOCX may later be generated as snapshots, but must not become the only authoritative source.

---

## D-CAD-002 — EasyCAD2 is the initial behavioral benchmark, not the architectural ceiling

**Status:** BASELINE  
**Date:** 2026-08-14

EasyCAD2 is currently the most detailed reference for workflow and feature coverage. BiomechE-CAD should preserve useful clinical/manufacturing capability while improving openness, provenance, versioning, regression testability and integration with BiomechE.

---

## D-CAD-003 — Prefer non-destructive, versioned geometry operations

**Status:** BASELINE  
**Date:** 2026-08-14

Where technically reasonable, heel, arch, wedge, corrective element, ROI deformation, smoothing and sculpt actions should be represented as reconstructable/versioned operations rather than only as irreversible mutations of the final mesh.

---

## D-CAD-004 — Canonical physical units align with BiomechE

**Status:** BASELINE  
**Date:** 2026-08-14

Public/canonical quantities should use:

```text
distance = mm
angle = deg
pressure = kPa
force = N
area = mm2
```

Conversions are explicit and must not silently alter prescription semantics.

---

## D-CAD-005 — Acquisition provenance and registration are first-class data

**Status:** BASELINE  
**Date:** 2026-08-14

Pressure, Scan3D, Scan2D/Image2D and BiomechE-derived inputs preserve source identity, units, side, coordinate system, transformation/registration history and quality/provenance metadata.

---

## D-CAD-006 — Plantar pressure remains quantitative data

**Status:** BASELINE  
**Date:** 2026-08-14

Pressure may be rendered as a color overlay, but its authoritative representation remains numeric and metric. Algorithms, ROI statistics and design suggestions should refer to quantitative values and source provenance rather than an RGB texture.

---

## D-CAD-007 — Material/stiffness regions are separate from pure geometry

**Status:** BASELINE  
**Date:** 2026-08-14

The data model must be capable of representing regions with differentiated material, density or stiffness without requiring those properties to be encoded only as external settings or geometric deformation.

---

## D-CAD-008 — CAM/GCODE is downstream of the geometry core

**Status:** BASELINE  
**Date:** 2026-08-14

The CAD core defines the orthosis geometry and manufacturing semantics. CNC post-processing/toolpath/GCODE generation belongs to a separate CAM/post-processor layer with machine/profile versioning.

---

## D-CAD-009 — Exports are tied to immutable project revisions

**Status:** BASELINE  
**Date:** 2026-08-14

An STL/3MF/GCODE/project package/report must identify the exact project revision and manufacturing profile from which it was generated. Export artifacts should carry hashes and validation state where practical.

---

## D-CAD-010 — Every P0 feature must become testable

**Status:** BASELINE  
**Date:** 2026-08-14

Each P0 requirement requires acceptance criteria and, where applicable, deterministic geometry invariants or golden-regression fixtures. UI-level validation alone is insufficient for geometric correctness.

---

## D-CAD-011 — OpenSubdiv-first canonical control-cage architecture

**Status:** BASELINE  
**Date:** 2026-08-14

BiomechE-CAD will use a **canonical orthosis control cage + versioned operation stack** as the leading P0 geometry architecture, with OpenSubdiv as the expected smooth limit-surface evaluator.

Rationale:

- EasyCAD2 primary documentation validates direct mesh/vertex editing, parametric heel/arch/wedge changes, element positioning, sculpt and scan-conforming deformation;
- the project owner states that EasyCAD2 uses OpenSubdiv;
- official OpenSubdiv documentation is specifically optimized for deforming subdivision surfaces with static topology at interactive frame rates.

This does **not** imply that BiomechE-CAD will clone EasyCAD2 internals or formulas.

---

## D-CAD-012 — General-purpose NURBS/B-Rep is not a P0 prerequisite

**Status:** BASELINE  
**Date:** 2026-08-14

The validated EasyCAD2 product behavior does not require BiomechE-CAD to make NURBS surface authoring, trimmed B-Rep, STEP/IGES, general loft/sweep/revolve, arbitrary shell/offset, fillet/chamfer or a full solid-boolean kernel prerequisites for the MVP.

Utility B-spline curves remain allowed where useful. Exact CAD/NURBS/B-Rep may later enter through adapters for explicit interoperability/manufacturing use cases.

---

## D-CAD-013 — Additional geometry libraries must earn entry through a failing fixture

**Status:** BASELINE  
**Date:** 2026-08-14

Do not add OCCT, CGAL, Manifold, openNURBS or another major geometry dependency merely for theoretical capability coverage.

A dependency is justified only when:

1. a named P0/P1 acceptance fixture cannot be implemented robustly with the current cage/OpenSubdiv/focused-algorithm stack;
2. the failure is reproducible;
3. the candidate library materially improves robustness or interoperability;
4. license, portability, WASM/server feasibility and conversion cost are documented.

---

## D-CAD-014 — Clinical upper surface and manufacturing body are separated

**Status:** BASELINE  
**Date:** 2026-08-14

The canonical cage primarily authors the clinical upper/contact surface. Lower surface, sidewalls, thickness and Bridge/Straight/Oblique/Hybrid closure are derived manufacturing geometry.

This allows clinical prescription to remain stable while production profiles change.

This is a BiomechE-CAD design choice, not a claim about EasyCAD2 internals.

---

## OPEN DECISIONS

The following decisions remain open or require qualification before freezing:

- exact project storage/container format;
- exact coordinate and registration contract;
- concrete canonical cage topology/resolution and topology-family count;
- OpenSubdiv boundary/crease rules;
- operation dependency/evaluation details beyond the current staged baseline;
- exact heel/camber mathematical operator;
- exact medial/lateral arch operator calibration;
- wedge reference axes and measurement fixture;
- corrective-element field/cage representation and `PLACE_FROM_BASE` semantics;
- scan-conform projection semantics;
- production lower-surface/closure algorithms;
- physical stiffness/material model;
- initial manufacturing target priority: additive, CNC or equal priority;
- public API/ABI boundary for CAD engine integration;
- whether a second geometry library is eventually needed after the cage qualification suite.

A library choice must follow these requirements, not define them retroactively.
