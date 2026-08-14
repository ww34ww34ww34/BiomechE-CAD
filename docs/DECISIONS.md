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

Pressure may be rendered as a color overlay, but its authoritative representation remains numeric and metric. ROI statistics and design/outcome comparisons refer to quantitative values and provenance rather than an RGB texture.

---

## D-CAD-007 — Material/stiffness regions are separate from pure geometry

**Status:** BASELINE  
**Date:** 2026-08-14

The data model represents differentiated material, density or stiffness regions without requiring those properties to be encoded only as geometry.

---

## D-CAD-008 — CAM/GCODE is downstream of the product geometry/design model

**Status:** BASELINE  
**Date:** 2026-08-14

CNC/toolpath/GCODE generation belongs to a separate manufacturing/post-processing layer with machine/profile versioning.

---

## D-CAD-009 — Exports are tied to immutable project revisions

**Status:** BASELINE  
**Date:** 2026-08-14

STL/3MF/GCODE/project package/report artifacts identify the exact design revision and manufacturing profile from which they were generated. Hashes and validation state should be retained where practical.

---

## D-CAD-010 — Every P0 feature must become testable

**Status:** BASELINE  
**Date:** 2026-08-14

Each P0 requirement requires acceptance criteria and, where applicable, deterministic geometric or data invariants. UI-only validation is insufficient.

---

## D-CAD-011 — SubD/control-cage is a strong geometry hypothesis, but the foundation engine is not selected

**Status:** OPEN / QUALIFICATION DEFERRED  
**Date:** 2026-08-14

The EasyCAD2 audit plus the project-owner fact that EasyCAD2 uses OpenSubdiv support a stable/mostly-stable control-cage + smooth-surface architecture as a strong hypothesis.

However, **OpenSubdiv is not a frozen or presumptive P0 dependency**.

When architecture work resumes, principal candidates are:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

Prefer one authoritative P0 SubD foundation rather than maintaining two synchronized SubD representations without a concrete need. Compare public/stable APIs on the same fixtures.

---

## D-CAD-012 — General-purpose NURBS/B-Rep is not a P0 product prerequisite

**Status:** BASELINE  
**Date:** 2026-08-14

The validated EasyCAD2 workflow does not require NURBS authoring, trimmed B-Rep, STEP/IGES, generic loft/sweep/revolve, shell/offset, fillet/chamfer or a general solid-boolean kernel as MVP product requirements.

Extra capabilities supplied by a future foundation must not redefine the product specification.

---

## D-CAD-013 — Additional geometry libraries must earn entry through a named requirement or failing fixture

**Status:** BASELINE  
**Date:** 2026-08-14

Do not add major geometry dependencies merely for theoretical capability coverage. A dependency is justified only when a named requirement/fixture needs it, the need is reproducible, the candidate materially improves the result and license/platform/conversion costs are documented.

---

## D-CAD-014 — Clinical prescription and manufacturing realization are separate concepts

**Status:** BASELINE  
**Date:** 2026-08-14

The clinical/design prescription remains stable and traceable independently from lower-surface, sidewall, closure, material and manufacturing realization. A manufacturing-profile change must not silently alter prescription semantics.

---

## D-CAD-015 — Architecture selection is parked; functionality and scientific evidence lead current work

**Status:** BASELINE  
**Date:** 2026-08-14

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

Architecture research is preserved, not discarded. Resume the OpenSubdiv vs openNURBS/ON_SubD shoot-out only when requirements and acceptance tests are mature enough.

---

## D-CAD-016 — Clinically meaningful CAD features preserve dose, anatomical placement, units and reference frame

**Status:** BASELINE  
**Date:** 2026-08-14

A named feature such as `RearfootWedge`, `MedialArch`, `HeelCup` or `MetatarsalPad` must not survive only as anonymous final geometry.

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

---

## D-CAD-017 — Outcome thresholds are context/protocol specific, not universal constants

**Status:** BASELINE  
**Date:** 2026-08-14

Guideline thresholds or research targets are stored with population/context, protocol, ROI, metric and evidence source. Diabetic-foot pressure criteria must not leak into metatarsalgia, flatfoot, heel pain or sport by default.

---

## D-CAD-018 — Indication/use-case profiles are a versioned evidence-context layer

**Status:** BASELINE  
**Date:** 2026-08-14

BiomechE-CAD uses versioned `IndicationProfile` objects to determine which CAD features, metrics, targets and warnings are meaningful in a particular population/context.

Initial P0 profile set:

```text
DIABETIC_REULCERATION_PREVENTION
MECHANICAL_METATARSALGIA
FLEXIBLE_FLATFOOT
PLANTAR_HEEL_PAIN
SPORT_PERFORMANCE
GENERIC_CUSTOM_ORTHOSIS
```

Rules:

1. a profile does not diagnose and does not automatically prescribe geometry;
2. every profile-derived target/warning retains profile + evidence provenance;
3. multiple profiles may coexist, but targets never merge anonymously;
4. pediatric/adult, symptomatic/asymptomatic and walking/running evidence do not transfer silently;
5. `GENERIC_CUSTOM_ORTHOSIS` applies no disease-specific hidden threshold;
6. active pathology can trigger a different clinical pathway rather than merely another CAD preset.

Specific safety boundary: an active neuropathic plantar forefoot/midfoot diabetic ulcer must not be presented as equivalent to a recurrence-prevention insole workflow; the IWGDF active-ulcer offloading pathway is surfaced explicitly.

Canonical specification: `docs/spec/13_use_case_profiles.md`.

---

## D-CAD-019 — Patient-reported outcome, comfort, fit and adherence remain separate versioned outcome classes

**Status:** BASELINE  
**Date:** 2026-08-14

BiomechE-CAD will not collapse pain, function, foot-specific health, comfort, fit/usability, satisfaction and adherence into one hidden universal score.

Rules:

1. define the outcome construct before selecting a PROM instrument;
2. store exact instrument version, language/cultural adaptation and scoring algorithm version;
3. preserve domain/subscale scores independently;
4. MID/MCID/MDC/SEM values remain instrument/domain/population/context specific and retain evidence provenance;
5. comfort remains task/protocol specific and separate from pain/function;
6. fit/usability remains separate from comfort;
7. adherence stores method and denominator (`hours`, weight-bearing time, steps, prescribed session, etc.); objective and subjective adherence are not treated as equivalent;
8. every measurement links to the exact design/manufacturing revision in use;
9. questionnaire text/translations/scoring assets are shipped only after copyright/licensing/redistribution review;
10. any future composite endpoint must be named, transparent, profile-specific and independently validated.

Canonical specification: `docs/spec/14_prom_comfort_adherence.md`.

---

## D-CAD-020 — Material identity, manufacturing process, final-part properties and service state are separate provenance layers

**Status:** BASELINE  
**Date:** 2026-08-14

BiomechE-CAD SHALL not treat a supplier material label or a nominal hardness as the complete physical specification of an orthosis.

The canonical chain is:

```text
MaterialDefinition / feedstock
        ↓
MaterialRegion / MaterialStack / structural response
        ↓
ManufacturingProfile + process run + post-process
        ↓
Physical artifact
        ↓
Measured manufactured geometry/properties + QC
        ↓
Service-aged state
```

Rules:

1. supplier/datasheet properties are labelled nominal and remain distinct from measured final-part properties;
2. hardness values require scale and test method; no undocumented Shore-to-modulus conversion is allowed;
3. density, thickness, stack order, interfaces and post-processing are explicit;
4. base-material properties and effective lattice/infill properties are separate;
5. heat/thermoforming/curing/lamination that can change properties is part of manufacturing provenance;
6. feedstock/blank lot, machine/process profile and qualification-critical settings are versioned where available/required;
7. CAD nominal geometry and manufactured measured geometry are separate data classes;
8. export success does not imply manufactured-part acceptance;
9. profile-defined blocking QC failures prevent validated-production status;
10. initial and service-aged material states are separate; no universal lifetime/replacement rule is hardcoded without qualification evidence;
11. physical copies made from the same CAD revision can remain distinct by run, lot and artifact identity.

Canonical specifications:

- `docs/spec/08_material_stiffness.md`
- `docs/spec/10_manufacturing.md`

Evidence batch: `docs/research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md`.

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

Functional/specification work still active:

- promote mature Batches 03–08 into consolidated P0/P1 functional spec;
- Project Schema v0;
- kernel-independent acceptance suite;
- final built-in PROM set after population fit + licensing review;
- shear/COP depth after target acquisition hardware is fixed;
- product-specific manufacturing qualification/tolerances and actual material/process library entries.
