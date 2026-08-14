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

## OPEN DECISIONS

The following decisions must be resolved before implementation is allowed to constrain the architecture prematurely:

- geometry kernel / mesh representation;
- exact project storage/container format;
- operation dependency/evaluation model;
- coordinate and registration contract;
- heel/camber mathematical operator;
- medial/lateral arch mathematical operators;
- wedge reference axes and geometric construction;
- offset/thickness strategy;
- element integration/boolean strategy;
- physical stiffness/material model;
- initial manufacturing target priority: additive, CNC or equal priority;
- public API/ABI boundary for CAD engine integration.

A library choice must follow these requirements, not define them retroactively.
