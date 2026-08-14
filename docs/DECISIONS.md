# BiomechE-CAD — Architectural and Product Decisions

This file records cross-cutting decisions separately from research evidence.

**Status convention**

- `BASELINE` — current working direction; may be refined by a later explicit decision.
- `FROZEN` — implementation should treat the decision as stable until explicitly superseded.
- `OPEN` — not decided.

---

## D-CAD-001 — Markdown is the canonical specification source

**Status:** BASELINE  
**Date:** 2026-08-14

Canonical project specifications and handover material live as Markdown under `docs/`.

---

## D-CAD-002 — EasyCAD2 is the initial behavioral benchmark, not the architectural ceiling

**Status:** BASELINE  
**Date:** 2026-08-14

Preserve useful EasyCAD2 clinical/manufacturing behavior while improving openness, provenance, versioning, regression testability and integration with BiomechE.

---

## D-CAD-003 — Prefer non-destructive, versioned clinical/design operations

**Status:** BASELINE  
**Date:** 2026-08-14

Where technically reasonable, heel, arch, wedge, corrective element, ROI deformation, smoothing and sculpt actions should remain reconstructable/versioned rather than only irreversible final geometry.

---

## D-CAD-004 — Canonical physical units align with BiomechE

**Status:** BASELINE  
**Date:** 2026-08-14

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

Pressure, Scan3D, Scan2D/Image2D and BiomechE-derived inputs preserve source identity, units, side, acquisition conditions, coordinate system, registration history and quality/provenance metadata.

---

## D-CAD-006 — Plantar pressure remains quantitative data

**Status:** BASELINE  
**Date:** 2026-08-14

Pressure may be rendered as a color overlay, but its authoritative representation remains numeric and metric. ROI statistics and design/outcome comparisons must refer to quantitative values and source provenance rather than an RGB texture.

---

## D-CAD-007 — Material/stiffness regions are separate from pure geometry

**Status:** BASELINE  
**Date:** 2026-08-14

The data model must represent differentiated material, density or stiffness regions without requiring those properties to be encoded only as geometry.

---

## D-CAD-008 — CAM/GCODE is downstream of the product geometry/design model

**Status:** BASELINE  
**Date:** 2026-08-14

CNC/toolpath/GCODE generation belongs to a separate manufacturing/post-processing layer with machine/profile versioning.

---

## D-CAD-009 — Exports are tied to immutable project revisions

**Status:** BASELINE  
**Date:** 2026-08-14

STL/3MF/GCODE/project package/report artifacts must identify the exact design revision and manufacturing profile from which they were generated. Hashes and validation state should be retained where practical.

---

## D-CAD-010 — Every P0 feature must become testable

**Status:** BASELINE  
**Date:** 2026-08-14

Each P0 requirement requires acceptance criteria and, where applicable, deterministic geometric or data invariants. UI-level validation alone is insufficient.

---

## D-CAD-011 — SubD/control-cage is a strong geometry hypothesis, but the foundation engine is not selected

**Status:** OPEN / QUALIFICATION DEFERRED  
**Date:** 2026-08-14

The EasyCAD2 audit plus the project-owner fact that EasyCAD2 uses OpenSubdiv support a stable/mostly-stable control-cage + smooth-surface architecture as a strong hypothesis.

However, **OpenSubdiv is no longer considered a frozen or presumptive P0 dependency**.

When architecture work resumes, the principal SubD foundation candidates are:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

The project should prefer **one** authoritative P0 SubD foundation rather than maintaining OpenSubdiv and ON_SubD representations in parallel without a concrete need.

The comparison must use public/stable APIs only and the same orthosis fixtures.

---

## D-CAD-012 — General-purpose NURBS/B-Rep is not a P0 product prerequisite

**Status:** BASELINE  
**Date:** 2026-08-14

The validated EasyCAD2 workflow does not require NURBS surface authoring, trimmed B-Rep, STEP/IGES, general loft/sweep/revolve, arbitrary shell/offset, fillet/chamfer or a full solid-boolean kernel as MVP product requirements.

This does not prevent a future foundation such as openNURBS from providing additional capabilities incidentally; extra capabilities must not redefine the product specification.

---

## D-CAD-013 — Additional geometry libraries must earn entry through a named requirement or failing fixture

**Status:** BASELINE  
**Date:** 2026-08-14

Do not add OCCT, Manifold, CGAL, openNURBS, OpenSubdiv or another major geometry dependency merely for theoretical capability coverage.

A dependency is justified only when:

1. a named product requirement/acceptance fixture needs it;
2. the need/failure is reproducible;
3. the candidate materially improves robustness, portability, performance or interoperability;
4. license, target-platform feasibility and conversion/synchronization cost are documented.

---

## D-CAD-014 — Clinical prescription and manufacturing realization are separate concepts

**Status:** BASELINE  
**Date:** 2026-08-14

The clinical/design prescription must remain stable and traceable independently from the exact lower-surface, sidewall, closure, material and manufacturing realization.

A change in manufacturing profile must not silently change the semantic prescription.

---

## D-CAD-015 — Architecture selection is temporarily parked; functionality and scientific evidence lead current work

**Status:** BASELINE  
**Date:** 2026-08-14

Current project priority is:

```text
EasyCAD2 behavior
+ scientific/biomechanical literature
+ measurable clinical/design parameters
+ outcome/traceability requirements
        ↓
functional product specification
        ↓
architecture/library selection later
```

The active canonical research document is:

`docs/research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md`

Architecture research is preserved, not discarded. The OpenSubdiv vs openNURBS/ON_SubD shoot-out resumes only after the functional/evidence matrix is sufficiently mature to define the required tests.

---

## D-CAD-016 — Clinically meaningful CAD features preserve dose, anatomical placement, units and reference frame

**Status:** BASELINE  
**Date:** 2026-08-14

A named feature such as `RearfootWedge`, `ForefootWedge`, `MedialArch` or `MetatarsalPad` must not survive only as anonymous final geometry.

Where applicable preserve:

```text
feature type
side / anatomical region
numerical dose
units
reference frame / landmark
placement / extent
material/mechanical properties
intent
algorithm/version
```

This is supported by literature showing dose- and placement-dependent biomechanical effects and is independent of eventual CAD implementation.

---

## D-CAD-017 — Outcome thresholds are context/protocol specific, not universal constants

**Status:** BASELINE  
**Date:** 2026-08-14

Guideline thresholds or research targets must be stored with population/context, protocol, ROI, metric and evidence source.

Example: diabetic-foot pressure-offloading criteria must not be silently reused as universal thresholds for flatfoot, plantar fasciitis, sport or other indications.

---

## OPEN DECISIONS

Architecture / implementation decisions intentionally deferred:

- OpenSubdiv vs openNURBS/ON_SubD as P0 SubD foundation;
- exact canonical cage topology/resolution and topology-family count;
- C++20 / C ABI / WASM deployment details;
- exact project storage/container format;
- exact coordinate/registration contract;
- exact mathematical realization of heel/arch/wedge operations;
- corrective-element internal representation;
- scan-conform implementation;
- production lower-surface/closure algorithms;
- whether Manifold or another solid/mesh library is needed;
- whether STEP/.3dm interoperability becomes a product requirement.

Functional/scientific questions currently active:

- population-specific indication profiles;
- arch dose and placement evidence;
- heel containment vs cushioning evidence;
- metatarsal element dose/placement;
- offloading ROI + neighboring-region safety metrics;
- pressure metric selection (peak/PTI/FTI/contact area/COP/shear when available);
- material/stiffness prescription semantics;
- post-production outcome verification;
- PROM/comfort/fit/adherence model.
