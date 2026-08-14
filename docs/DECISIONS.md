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
time = s
angle = deg
pressure = kPa
force = N
area = mm²
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

## D-CAD-021 — Functional specification v2 is the canonical product-scope baseline

**Status:** BASELINE  
**Date:** 2026-08-14

`docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` is the canonical consolidated functional specification after evidence Batches 03–08.

The previous `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is preserved as a historical detailed baseline and shall not be destructively rewritten merely to remove superseded prose.

Rules:

1. v2 governs product scope and P0/P1/P2 prioritization;
2. detailed subordinate specs govern the semantics of their own domains;
3. evidence metadata remains in `docs/BIBLIOGRAPHY.md` and research batches rather than being duplicated in full;
4. v2 remains implementation-neutral and shall not be altered to fit a preferred geometry kernel;
5. every P0 requirement must ultimately map to at least one kernel-independent acceptance criterion;
6. Project Schema v0 is derived from this functional baseline, not from the current architecture hypothesis.

---

## D-CAD-022 — Project Schema v0 uses immutable revisions, exact definition snapshots and an implementation-neutral manifest

**Status:** BASELINE  
**Date:** 2026-08-14

The logical project contract is defined in `docs/spec/02_project_schema.md` and is independent from database, package/container and geometry-kernel choices.

Rules:

1. committed `DesignRevision` objects are immutable; edits create successor revisions;
2. raw acquisition/source assets are immutable and hash-addressable for integrity/provenance;
3. reusable definitions that influence a committed revision (`BaseTemplate`, `IndicationProfile`, `MaterialDefinition`, `PROMInstrumentDefinition`, `ManufacturingProfile`, presets) resolve to the exact version used plus content hash/snapshot semantics;
4. semantic prescription/operation state is authoritative for native projects; derived meshes are caches/artifacts, while legacy imports may explicitly use `IMPORTED_LEGACY_GEOMETRY` authority mode;
5. physical manufactured copies have identities separate from CAD revisions;
6. measured, predicted, nominal, manufactured and service-aged values remain distinct classes;
7. the reference portable serialization is UTF-8 JSON with JSON Schema Draft 2020-12 validation; this does not select a document database;
8. provenance uses a lightweight Entity/Activity/Agent-compatible graph; W3C PROV is an interoperability model, not a requirement to store RDF;
9. optional FHIR mappings may expose observations, questionnaire responses and provenance without making FHIR the internal authoring schema;
10. package/container format, encryption/signature profile and storage engine remain OPEN.

Machine-readable reference schema: `schemas/biomeche-cad-project-0.1.schema.json`.

---

## D-CAD-023 — Coordinate/registration semantics are frozen before geometry implementation

**Status:** FROZEN  
**Date:** 2026-08-14

`docs/spec/01_coordinate_registration.md` is the kernel-independent semantic authority for orientation, side ownership, anatomical axes, pressure mapping and transform algebra.

Rules:

1. `CAD-ANAT-1` is right-handed and subject-centric: `+X` heel/posterior→distal/anterior, `+Y` subject RIGHT→subject LEFT, `+Z` plantar→dorsal;
2. LEFT/RIGHT is patient anatomical ownership and is never inferred from UI, storage order or an arbitrary coordinate sign;
3. medial/lateral Cartesian direction is side-dependent, while intrinsic `s/q` is side-normalized: `s` heel→distal and `q` lateral→medial on both feet;
4. semantic bilateral mirror creates a new target-side revision, reflects canonical `Y`, preserves intrinsic `s/q` anatomical meaning and is not a rigid registration;
5. pressure matrix `(row,column)` is storage topology only; physical sensor geometry and device/exam axes are explicit before CAD registration;
6. persisted transform algebra uses column vectors and `T_target_from_source`; composition is `T_C_from_A = T_C_from_B * T_B_from_A`; serialized arrays are row-major textual arrays, not an in-memory layout promise;
7. the initial Scan3D anatomical frame uses heel + first/fifth metatarsal-head landmarks with an independent dorsal-orientation witness; a dorsal sign is never guessed from three coplanar landmarks alone;
8. Image2D becomes metric only through explicit calibration; no silent mm-per-pixel assumption;
9. unknown orientation/side/calibration remains explicitly unresolved rather than inferred from visual appearance;
10. real scanner/platform/landmark/image/manufacturing tolerances remain `OPEN` until tied to a qualified acquisition/process system. Synthetic computational tolerances are not device-accuracy claims.

This decision freezes semantics only and does not reopen the geometry-kernel shoot-out.

---

## D-CAD-024 — BiomechE is the quantitative-analysis authority; CAD consumes pinned, provenance-bearing results

**Status:** FROZEN  
**Date:** 2026-08-15

Canonical specification: `docs/spec/11_biomeche_integration.md`.

Rules:

1. BiomechE owns the semantics of its named biomechanical KPI/result definitions; BiomechE-CAD SHALL not maintain a hidden second formula under the same metric identity;
2. imported result bundles preserve producer product/version/build/commit, result-contract version, algorithm/profile/RegionModel versions and source acquisition/hash identity required to reconstruct historical meaning;
3. the complete result bundle remains an immutable/hash-addressed evidence asset while CAD-normalized results use `OutcomeMeasurement`;
4. `VALID`, `DEGRADED` and `UNAVAILABLE` meaning propagates into CAD; unavailable is never numeric zero;
5. device/calibration/protocol/step/window/ROI/region metadata required by a metric survive import and participate in comparison compatibility;
6. cross-device equivalence is not assumed; validated harmonization/policy is explicit;
7. reanalysis of an old acquisition under a new BiomechE build/algorithm creates new result/measurement identities instead of overwriting history;
8. measured and predicted results remain separate;
9. current dynamic bindings are limited to semantics frozen upstream in BiomechE; `DYN-006+` pressure/force/integral/region formulas are not guessed in CAD while upstream remains open;
10. the integration contract is independent of the future CAD geometry foundation.

Current upstream integration pin: `ww34ww34ww34/BiomechE@d5e467a1a5551f4280cfef5b483da1999f1566e0` [ARCH-BIOMECHE-INTEGRATION-2026-08-15].

---

## D-CAD-025 — Reports are immutable derived artifacts over exact source entities

**Status:** FROZEN  
**Date:** 2026-08-15

Canonical specification: `docs/spec/12_reporting_traceability.md`.

Rules:

1. authoritative project entities/measurements remain the source of truth; report PDF/HTML/charts are derived presentation artifacts;
2. an issued report retains immutable bytes/hash and exact historical `sourceRefs`; creating a later design revision cannot make the old report float to current state;
3. regeneration/reissue creates a new `ReportArtifact` identity/provenance while preserving the historical report;
4. clinically/manufacturing significant reports SHOULD retain a machine-readable semantic source manifest with exact revisions, acquisitions, ROI/profile/evidence, material/manufacturing/QC and outcome refs;
5. semantic reproducibility is distinct from byte-identical rendering; PDF bytes may differ unless a deterministic rendering profile explicitly claims bitwise reproducibility;
6. calculations use authoritative full-precision values; display rounding is a final named presentation policy;
7. quality/comparability warnings, `MEASURED/PREDICTED`, and blocking QC states may not be hidden by presentation;
8. privacy filtering is performed from structured source data under `FULL_CLINICAL`, `PSEUDONYMIZED` or `MANUFACTURING_MINIMUM` policy;
9. report generation is a provenance activity; report, export, provenance and audit-event entities remain distinct;
10. signatures/attestation/archival legal profiles remain separate OPEN qualification decisions.

---

## OPEN DECISIONS

Architecture / implementation decisions intentionally deferred:

- OpenSubdiv vs openNURBS/ON_SubD as P0 SubD foundation;
- exact canonical cage topology/resolution and topology-family count;
- C++20 / C ABI / WASM deployment details;
- exact project package/container format and storage engine;
- exact mathematical realization of heel/arch/wedge operations;
- corrective-element internal representation;
- scan-conform implementation;
- production lower-surface/closure algorithms;
- whether Manifold or another solid/mesh library is needed;
- whether STEP/.3dm interoperability becomes a product requirement;
- encryption-at-rest and digital-signature/attestation profile;
- final FHIR implementation-guide/profile mappings;
- final report renderer/PDF archival/signature profile;
- final cloud/offline synchronization/runtime architecture.

Functional/specification/qualification work still active:

- executable `BINT-*` / `RPT-*` coverage expansion;
- deeper competitor functional-gap audit from manuals/trials where legally available;
- workflow macro/preset orchestration semantics (`GAP-COMP-001`);
- external clinical-media adapter semantics (`GAP-COMP-002`);
- real product acquisition/registration qualification and tolerances;
- cross-device pressure harmonization qualification where needed;
- BiomechE `DYN-006+` dynamic pressure/force/integral/region bindings as upstream freezes;
- final built-in PROM set after population fit + licensing review;
- product-specific manufacturing qualification/tolerances and actual material/process library entries.
