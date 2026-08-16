# BiomechE-CAD — P0 Documentation Closure & Visual Reference Plan

**Status:** ACTIVE WORK PLAN v1  
**Date:** 2026-08-16  
**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Phase name:** `P0-DOC-CLOSURE`  
**Architecture status:** no geometry engine selected; architecture PoC remains deferred until this documentation closure phase is complete or explicitly resumed.

---

## 1. Purpose

This plan closes the remaining product/functional documentation before returning to geometry-engine PoC qualification.

The work must **not reopen frozen contracts without new evidence**. Existing frozen authorities remain authoritative:

- coordinate / registration semantics;
- BiomechE integration semantics;
- reporting / traceability semantics;
- pressure-acquisition qualification methodology;
- Geometry Authoring Contract v1;
- Workflow / Preset / Macro Contract v1;
- Numerical / Tolerance / Qualification Registry v1;
- P0 Authoring Acceptance Catalog `AUTH-C01..C22`.

The objective is to finish the remaining product documentation around those contracts, eliminate provisional/historical ambiguity, create missing cross-cutting specifications, and then produce a **versioned visual reference package** so future UI and implementation work has an explicit visual target as well as written requirements.

---

## 2. Definition of documentation closure

`P0-DOC-CLOSURE` is complete only when all of the following are true:

1. no P0 product specification that is required for implementation remains `ACTIVE v0`, unless explicitly classified as intentionally provisional;
2. `spec/04_base_template.md` and `spec/05_parametric_orthosis_geometry.md` have a definitive status: canonical/frozen, superseded, or historical;
3. missing cross-cutting contracts listed in this plan exist and are internally consistent;
4. requirement/acceptance traceability is updated;
5. a final cross-document audit reports no blocking contradiction;
6. open numerical values remain `OPEN` rather than receiving invented defaults;
7. architecture-specific implementation details remain outside product-semantic authority;
8. Project Schema v0.2 remains `APPROVED / NOT MATERIALIZED` unless explicitly authorized separately;
9. `TD-CI-001` remains non-blocking unless explicitly reopened;
10. the visual-reference package is created, versioned, indexed and linked to the relevant product requirements.

---

# 3. Workstream overview

```text
DOC-00  Baseline inventory + closure criteria
DOC-01  Corrective Elements v1
DOC-02  Material / Stiffness v1
DOC-03  Analysis / QC / DFM v1
DOC-04  Manufacturing v1
DOC-05  Use-Case Profiles v1
DOC-06  PROM / Comfort / Adherence v1
DOC-07  Base Template + Parametric Geometry disposition
DOC-08  Input / Scan / Reference Data Contract
DOC-09  Product Workflow & Interaction Contract
DOC-10  Interchange & Manufacturing Handoff Contract
DOC-11  Realtime Interaction & Performance Contract
DOC-12  Validation & Verification Master Plan
DOC-13  Intended-Use / Risk / Privacy / Security boundary package
DOC-14  Final cross-document audit + closure freeze
VIS-01  Visual reference brief
VIS-02  Canonical mockup set
VIS-03  Visual package versioning / repository archive
VIS-04  Requirement ↔ screen traceability
```

`DOC-13` is product-important but may be executed as a parallel regulatory/security stream if it would otherwise block the core CAD documentation closure. It must not silently alter the frozen clinical/domain semantics.

---

# 4. DOC-00 — Baseline inventory and document governance

## Goal

Create one authoritative inventory of every specification and classify it as:

```text
FROZEN
CANONICAL ACTIVE
PROVISIONAL
HISTORICAL / SUPERSEDED
QUALIFICATION-DEPENDENT
```

## Activities

- inspect every `docs/spec/*` document;
- identify duplicated or superseded semantics;
- verify ownership against `BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`;
- ensure frozen `16/17/18` override older authoring assumptions;
- identify missing acceptance mappings;
- resolve numbering/document-index anomalies, including the absent `07` number, without inventing a document merely to fill the sequence;
- define freeze criteria for each remaining document.

## Deliverable

`docs/validation/P0_DOCUMENTATION_CLOSURE_AUDIT_2026-08-16.md`

## Exit gate

Every document has one unambiguous status and authority owner.

---

# 5. DOC-01 — Corrective Elements v1

**Current:** `spec/06_corrective_elements.md` — ACTIVE v0.

## Goal

Promote the clinically named corrective/offloading model to a stable v1 contract while keeping `spec/16_geometry_authoring_contract.md` authoritative for placement/replay/geometry semantics.

## Focus

- semantic taxonomy;
- target anatomy / ROI;
- intended effect;
- requested vs realized dose;
- landmark-aware placement;
- geometry vs mechanical dose;
- evidence-linked presets without universal defaults;
- side-aware mirror behavior;
- custom element provenance;
- target + safety-ring / adjacent-region outcome linkage;
- acceptance `CE-*` reconciliation with `GAUTH-*`, `WFLOW-*`, `NREG-*`, `AUTH-C*`.

## Exit gate

`06` becomes `FROZEN v1` or `CANONICAL v1` with no semantic overlap conflict with `16/17/18`.

---

# 6. DOC-02 — Material / Stiffness v1

**Current:** `spec/08_material_stiffness.md` — ACTIVE v0.

## Goal

Freeze material identity and mechanical-dose semantics independently from geometry.

## Focus

- MaterialDefinition / revision;
- lots/feedstock;
- nominal vs measured vs calibrated effective properties;
- hardness scale/method semantics;
- compression curves / nonlinear response;
- MaterialRegion / MaterialStack;
- structural/lattice effective properties;
- post-processing state;
- service-aged state;
- material qualification provenance;
- `MAT-*` reconciliation with manufacturing/QC/numerical registry.

## Exit gate

No hidden material-property inference and no generic hardness→modulus shortcut; all material authority is explicit and traceable.

---

# 7. DOC-03 — Analysis / Outcome / QC / DFM v1

**Current:** `spec/09_analysis_qc_dfm.md` — ACTIVE v0.

## Goal

Consolidate quantitative analysis, geometric inspection and DFM semantics without mixing clinical outcome thresholds with manufacturing limits or algorithm tolerances.

## Focus

- pressure metrics and protocol provenance;
- before/after/delta;
- ROI versioning;
- target/safety-ring/remote redistribution;
- measured vs predicted outcome;
- geometric inspection primitives;
- section/distance/height/angle/thickness/deviation semantics;
- DFM checks and explicit authority class for limits;
- quality states;
- acceptance namespace harmonization.

## Exit gate

Every metric and threshold has a named authority/provenance class; no ambiguous `tolerance` remains.

---

# 8. DOC-04 — Manufacturing v1

**Current:** `spec/10_manufacturing.md` — ACTIVE v0.

## Goal

Freeze the design→artifact→run→physical orthosis lifecycle.

## Focus

- ManufacturingProfile / revision;
- ManufacturingRun;
- immutable ManufacturingArtifact;
- AM / CNC provenance;
- material/lot linkage;
- post-processing;
- QC requirements and measurements;
- acceptance state;
- CAD nominal vs measured manufactured geometry;
- physical-part identity;
- service-state lineage;
- multi-material/regional realization;
- manufacturing package boundaries.

## Exit gate

`DesignRevision != ManufacturingArtifact != PhysicalOrthosis` is fully represented and acceptance cannot silently bypass profile-defined blocking QC.

---

# 9. DOC-05 — Use-Case Profiles v1

**Current:** `spec/13_use_case_profiles.md` — ACTIVE v0.

## Goal

Freeze evidence-context profiles and non-transfer semantics.

## Focus

- population / indication / activity / protocol context;
- profile-specific defaults;
- applicability boundaries;
- non-transfer of thresholds or presets;
- evidence profile versioning;
- interaction with workflows/presets and NREG;
- P0 vs P1 profile behavior.

## Exit gate

A recommendation/default/threshold cannot escape its intended profile context without an explicit decision.

---

# 10. DOC-06 — PROM / Comfort / Adherence v1

**Current:** `spec/14_prom_comfort_adherence.md` — ACTIVE v0.

## Goal

Freeze patient-reported outcome and wear/adherence semantics as outcomes separate from geometry validity and pressure measurements.

## Focus

- pain, comfort, fit, satisfaction, function and adherence separation;
- instrument/version provenance;
- timepoint semantics;
- revision/physical-part linkage;
- missing/unavailable semantics;
- longitudinal comparison;
- clinical vs UX wording boundaries.

## Exit gate

PROM/comfort/adherence cannot be silently collapsed into a single success score.

---

# 11. DOC-07 — Base Template + Parametric Orthosis Geometry disposition

**Current:**

- `spec/04_base_template.md` — candidate / not frozen;
- `spec/05_parametric_orthosis_geometry.md` — provisional math / not clinical authority.

## Goal

Remove ambiguity created by pre-freeze architecture hypotheses.

## Method

For every concept in `04/05`, classify:

```text
PRODUCT SEMANTIC — keep and promote
ALGORITHM HYPOTHESIS — keep provisional / move to architecture research
SUPERSEDED BY 16/17/18 — mark superseded
ENGINE-SPECIFIC — move outside canonical product specification
UNSUPPORTED NUMERICAL DEFAULT — convert to OPEN
```

## Exit gate

Both documents receive an explicit final status and cannot be mistaken for authority that overrides the frozen authoring contracts.

---

# 12. DOC-08 — Input / Scan / Reference Data Contract

## Proposed file

`docs/spec/20_input_scan_reference_data.md`

## Goal

Define what may enter BiomechE-CAD and how original data remains distinguishable from processed/derived data.

## Minimum scope

```text
3D scan / foot mesh
point cloud
STL / OBJ / PLY / 3MF or other admitted inputs
pressure acquisition / pressure map
BiomechE quantitative results
manual / automatic landmarks
reference template / reference orthosis
external manufacturing scan
```

For each source preserve as applicable:

```text
source type
file / dataset hash
units / scale
side
coordinate frame
orientation / handedness
capture context
sensor/scanner identity
calibration / qualification context
mesh / point-cloud quality
holes / non-manifold / normals
cropping / denoise / decimation provenance
landmark provenance + confidence/review state
registration transform + residual/quality
original vs processed vs derived identity
```

## Exit gate

No derived/cleaned dataset can silently replace original acquisition authority.

---

# 13. DOC-09 — Product Workflow & Interaction Contract

## Proposed file

`docs/spec/21_product_workflow_interaction.md`

## Goal

Define the end-to-end user workflow independently from the eventual UI toolkit.

## Canonical workflow to formalize

```text
Patient / Case
  ↓
Acquire / Import
  ↓
Qualify input
  ↓
Register / landmarks
  ↓
Choose base/template
  ↓
Generate initial orthosis
  ↓
Parametric edits
  ↓
Corrective elements
  ↓
Free sculpt / local edits
  ↓
Material prescription
  ↓
Inspect / measure
  ↓
BiomechE comparison
  ↓
QC / DFM
  ↓
Manufacturing preparation
  ↓
Commit immutable DesignRevision
  ↓
Manufacture / inspect physical part
  ↓
Outcome follow-up
```

## Interaction semantics to specify

- selection and focus;
- preview / apply / cancel / commit;
- undo/redo vs immutable committed revisions;
- direct manipulation + numeric input coherence;
- warnings vs blocking errors;
- LEFT/RIGHT context visibility;
- linked 2D/3D views;
- visibility/isolation layers;
- landmark/ROI inspection;
- workflow/preset invocation and human confirmation;
- provenance visibility;
- keyboard/mouse/touch expectations where product-relevant;
- accessibility and high-density clinical workstation use.

## Exit gate

An implementation team can derive screen/state flows without inventing clinical/domain behavior.

---

# 14. DOC-10 — Interchange & Manufacturing Handoff Contract

## Proposed file

`docs/spec/22_interchange_manufacturing_handoff.md`

## Goal

Define export/import semantics and information-loss boundaries independently from specific geometry-engine APIs.

## Formats to evaluate/document

At minimum where relevant:

```text
STL
3MF
OBJ / PLY for scan/reference exchange
project package
CNC/toolpath handoff
other formats only when a frozen workflow requires them
```

For each admitted format specify:

```text
units
axes / handedness
side
transform baking policy
precision / tessellation policy
metadata preservation
material-region preservation or loss
semantic information loss
hash / revision identity
round-trip expectations
lossless vs intentionally lossy boundary
```

## Exit gate

No exporter/importer is free to invent coordinate, unit, side or metadata conventions.

---

# 15. DOC-11 — Realtime Interaction & Performance Contract

## Proposed file

`docs/spec/23_realtime_performance_contract.md`

## Goal

Define the **performance doctrine** of BiomechE-CAD before engine selection, while leaving unjustified numeric thresholds `OPEN`.

## Architectural/product principles

```text
interactive authoring first
incremental recomputation
bounded dirty-region invalidation
preview quality != committed/final quality
LOD where it preserves semantic correctness
large-scan streaming/decimation strategies allowed
no unnecessary copies/allocations
rendering cadence separated from expensive authoring computation
background work must not reorder semantic commits
performance instrumentation must be low-overhead and reproducible
```

## Metrics

```text
input-to-preview latency
operation rebuild latency
commit latency
surface query latency
scan registration / conform latency
section / thickness / deviation-map latency
render frame time / FPS
memory peak
allocation volume
large-scan throughput
WASM startup / heap / transfer cost
serialization / replay time
```

Use min/p50/p95/p99/max/mean where meaningful.

## Numerical policy

No arbitrary universal PASS threshold. Unapproved budgets remain:

```text
MEASURED / NOT YET QUALIFIED
```

Future explicit profiles may define `ARCH-PERF-*` budgets.

## Exit gate

The engine scorecard/PoC can measure against one stable product-owned performance contract instead of candidate-specific expectations.

---

# 16. DOC-12 — Validation & Verification Master Plan

## Proposed file

`docs/validation/VALIDATION_VERIFICATION_MASTER_PLAN.md`

## Goal

Unify the existing acceptance namespaces into one evidence hierarchy.

## Evidence ladder

```text
Requirement
  ↓
Semantic acceptance case
  ↓
Unit / property test
  ↓
Integration test
  ↓
Golden / canonical geometry fixture
  ↓
Numerical qualification
  ↓
Performance qualification
  ↓
Manufacturing verification
  ↓
Physical-part QC
  ↓
Clinical/biomechanical outcome evidence where applicable
```

## Must define

- requirement IDs and ownership;
- test type;
- evidence artifact;
- repeatability/reproducibility expectations;
- PASS / FAIL / INDETERMINATE / NOT APPLICABLE;
- `OPEN` handling;
- qualification lifecycle;
- version invalidation/requalification triggers;
- distinction between software verification, process qualification, device qualification and clinical validation;
- release evidence package expectations.

## Exit gate

Every P0 requirement family has an explicit validation route and evidence owner.

---

# 17. DOC-13 — Intended Use / Risk / Privacy / Security boundary package

## Goal

Create a separate product-safety/governance package rather than mixing these concerns into geometry documents.

## Topics

- intended user;
- intended use / use environment;
- intended patient/population assumptions;
- clinical decision-support boundary;
- human authority/override;
- automation/recommendation boundary;
- patient identifiers and pseudonymization;
- access control / audit trail;
- data retention/export/deletion policy;
- software/update provenance;
- cybersecurity assumptions;
- risk-management hooks;
- regulatory classification assumptions and explicit unknowns.

## Research rule

Current legislation/standards must be verified from current authoritative primary sources when this stream is executed. Regulatory assumptions must not be guessed from memory.

## Exit gate

Risks and regulatory assumptions are explicit, versioned and separable from technical implementation choices.

---

# 18. DOC-14 — Final cross-document audit and freeze

## Goal

Perform a complete closure audit after all document streams above.

## Audit dimensions

```text
terminology consistency
authority ownership
side/laterality
coordinate/registration
requested vs realized dose
geometry vs material/mechanical dose
revision immutability
workflow/preset versioning
OPEN values
numerical authority classes
BiomechE ownership
manufacturing lineage
physical-part identity
input provenance
interchange loss boundaries
performance governance
acceptance/evidence coverage
```

## Deliverables

- `docs/validation/P0_DOCUMENTATION_FINAL_CROSS_AUDIT_2026-08-XX.md`;
- updated `TRACEABILITY_MATRIX.md`;
- updated `SPEC_INDEX.md`;
- updated `DECISIONS.md` where an actual decision was frozen;
- updated `RESUME_HERE.md`;
- updated `NEXT_CHAT_PROMPT.md`.

## Closure verdict

The desired result is:

```text
PRODUCT / FUNCTIONAL / SEMANTIC DOCUMENTATION: COMPLETE FOR P0
VISUAL REFERENCE PACKAGE: COMPLETE v1
ARCHITECTURE QUALIFICATION: READY TO RESUME
```

---

# 19. VIS-01 — Visual Reference Brief

Visual work begins **after the product workflow and core P0 documents are stable enough that screens will not encode obsolete semantics**.

## Proposed canonical file

`docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md`

## Goal

Translate written product semantics into a coherent visual language and list of reference screens without making UI appearance an accidental source of domain rules.

## Visual principles to capture

- professional medical/CAD character;
- calm, precise and information-dense rather than decorative;
- clear LEFT/RIGHT and patient/case context;
- strong distinction between editable preview and committed revision;
- provenance, warnings and quality states visible but not visually overwhelming;
- quantitative values legible and directly inspectable;
- 3D model remains central where appropriate;
- BiomechE pressure/analysis views integrated rather than bolted on;
- visual semantics consistent between desktop and responsive/web targets;
- light/dark variants only if both remain clinically readable;
- no visual element may imply an unsupported clinical threshold/default.

---

# 20. VIS-02 — Canonical mockup set

Create and review a minimum reference set. The exact number may grow, but the baseline should cover the whole P0 workflow.

## Required mockups

### M01 — Project / Patient / Case workspace

Shows project identity, side, source acquisitions, revision state and primary workflow entry.

### M02 — Import / Scan qualification

Shows raw source, preprocessing state, units/side/orientation, quality warnings and provenance.

### M03 — Registration / Landmarks

Shows foot/scan, anatomical frame, landmarks, registration status and review/confidence.

### M04 — Base orthosis / Template generation

Shows base/template choice, dimensional controls, requested values, preview and commit semantics.

### M05 — Parametric authoring

Shows heel/arch/post/wedge or equivalent orthosis-specific parameters with numeric + direct manipulation.

### M06 — Corrective / Offloading elements

Shows clinically named element library, anatomical placement, target ROI, geometric dose, mechanical profile and evidence/preset provenance.

### M07 — Sculpt / Local freeform editing

Shows replayable sculpt/local operations, tool settings, affected region and preview/commit state.

### M08 — Materials / Regional mechanical prescription

Shows MaterialRegion/stack, nominal/measured/effective-property distinction and regional assignment.

### M09 — Inspection / Geometry QC

Shows sections, distances, heights, angles, thickness and deviation/quality inspection.

### M10 — BiomechE before / after / delta

Shows pressure/KPI analysis, target + safety ring/adjacent regions, protocol comparability and quality state.

### M11 — DFM / Manufacturing preparation

Shows manufacturing profile, min-thickness/geometry checks, export/handoff configuration and blocking/warning states.

### M12 — Revision / provenance / report

Shows immutable design revisions, source lineage, manufacturing artifact linkage, report generation and comparison/history.

### M13 — Physical-part QC / outcome follow-up

Shows manufactured-part identity, QC measurements, service state and linked outcome/PROM follow-up.

### M14 — Compact/responsive reference

Shows how the same semantic hierarchy survives reduced viewport/tablet/web layouts without hiding critical state.

---

# 21. VIS-03 — Repository storage and versioning

The mockups must be **saved in the repository**, not left only inside a chat.

## Proposed structure

```text
docs/ux/
  BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
  mockups/
    v1/
      README.md
      manifest.md
      M01_project_case.*
      M02_import_scan.*
      M03_registration_landmarks.*
      M04_base_template.*
      M05_parametric_authoring.*
      M06_corrective_elements.*
      M07_sculpt.*
      M08_materials.*
      M09_inspection_qc.*
      M10_biomeche_delta.*
      M11_dfm_manufacturing.*
      M12_revision_provenance.*
      M13_physical_qc_followup.*
      M14_responsive.*
```

## Canonical asset policy

Prefer storing both:

1. **editable/source-controlled mockup form** where practical (`HTML/CSS`, `SVG`, or another text-diffable source);
2. **rendered reference export** (`PNG` or equivalent) for stable visual comparison.

The rendered image is the visual reference; the source file is the editable implementation/design source.

`manifest.md` should record for each mockup:

```text
mockup ID
version
status
screen purpose
requirements/spec sections represented
source asset
rendered asset
viewport / theme
known simplifications
approval state
supersedes / superseded by
```

When binary assets are stored, preserve immutable filenames/version directories or hashes so a later redesign does not silently replace the approved visual baseline.

---

# 22. VIS-04 — Requirement ↔ screen traceability

Mockups are not merely branding assets. Each canonical screen must point back to product authority.

Examples:

```text
M03 -> 01 coordinate/registration + 20 input/scan + GAUTH landmark provenance
M06 -> 06 corrective elements + 16 geometry authoring + 17 preset/workflow
M08 -> 08 material/stiffness + 10 manufacturing
M10 -> 09 analysis/QC + 11 BiomechE integration
M11 -> 09 analysis/QC/DFM + 10 manufacturing + 22 interchange
M12 -> 02 project schema + 12 reporting/traceability
```

The final visual-reference document must state explicitly:

```text
WRITTEN SPECIFICATION IS SEMANTIC AUTHORITY.
MOCKUP IS VISUAL / INTERACTION REFERENCE.
```

If they conflict, the discrepancy must be resolved explicitly rather than allowing the mockup to silently redefine the product.

---

# 23. Recommended execution sequence

## Wave 1 — Close current ACTIVE v0 specs

```text
DOC-00
DOC-01  06 corrective elements
DOC-02  08 material/stiffness
DOC-03  09 analysis/QC/DFM
DOC-04  10 manufacturing
DOC-05  13 use-case profiles
DOC-06  14 PROM/comfort/adherence
```

## Wave 2 — Remove provisional ambiguity

```text
DOC-07  04/05 disposition
```

## Wave 3 — Add missing implementation-neutral contracts

```text
DOC-08  input/scan/reference
DOC-09  workflow/interaction
DOC-10  interchange/handoff
DOC-11  realtime/performance
DOC-12  V&V master plan
```

## Wave 4 — Product governance package

```text
DOC-13  intended use/risk/privacy/security
```

May run in parallel if appropriate, but current authoritative sources must be researched when executed.

## Wave 5 — Closure audit

```text
DOC-14
```

## Wave 6 — Visual reference package

```text
VIS-01  visual brief
VIS-02  M01..M14 mockups
VIS-03  save/version package in repo
VIS-04  requirement↔screen traceability
```

## Wave 7 — Resume architecture qualification

Only after the documentation/visual closure, or by explicit project-owner decision:

```text
Q0..Q7 geometry-engine PoC qualification
```

---

# 24. Per-task operating method

Each documentation task should follow the same lightweight method:

```text
1. Read current document + frozen upstream authorities.
2. Search existing repository evidence before adding new concepts.
3. Use current primary-source web research only where a real evidence gap exists.
4. Draft changes without inventing universal defaults.
5. Cross-check schema/traceability implications, but do not materialize Project Schema v0.2 unless explicitly authorized.
6. Reconcile acceptance IDs and add missing cases only when justified.
7. Perform local cross-document contradiction check.
8. Freeze/promote/status the document.
9. Update SPEC_INDEX / TRACEABILITY / RESUME_HERE as needed.
10. Keep DONE/TODO and restart point current.
```

---

# 25. Explicit non-goals during P0-DOC-CLOSURE

Do not:

- select OpenSubdiv, ON_SubD or another engine;
- optimize or benchmark an engine unless architecture qualification is explicitly resumed;
- fix `TD-CI-001` as a side task;
- modify runtime JSON Schema/fixtures/migrations merely because documentation evolves;
- introduce OCCT/CGAL/Manifold/etc. pre-emptively;
- convert evidence-specific values into global clinical defaults;
- create visual mockups before the related written semantics are stable enough to avoid immediate obsolescence.

---

# 26. Progress checklist

## Documentation

- [ ] DOC-00 baseline inventory / closure audit
- [ ] DOC-01 corrective elements v1
- [ ] DOC-02 material/stiffness v1
- [ ] DOC-03 analysis/QC/DFM v1
- [ ] DOC-04 manufacturing v1
- [ ] DOC-05 use-case profiles v1
- [ ] DOC-06 PROM/comfort/adherence v1
- [ ] DOC-07 base-template / parametric-geometry disposition
- [ ] DOC-08 input/scan/reference contract
- [ ] DOC-09 workflow/interaction contract
- [ ] DOC-10 interchange/handoff contract
- [ ] DOC-11 realtime/performance contract
- [ ] DOC-12 V&V master plan
- [ ] DOC-13 intended-use/risk/privacy/security package
- [ ] DOC-14 final cross-document audit / closure freeze

## Visual reference

- [ ] VIS-01 visual brief
- [ ] VIS-02 M01..M14 canonical mockups
- [ ] VIS-03 editable + rendered assets saved/versioned in repository
- [ ] VIS-04 requirement↔screen traceability
- [ ] visual baseline approval recorded

## Architecture

- [ ] resume Q0 only after documentation/visual closure or explicit owner decision

---

# 27. Exact next task

Start with:

```text
DOC-00 — P0 Documentation Closure Audit
```

Then execute `DOC-01` through `DOC-06` sequentially, because those specifications already contain substantial evidence and acceptance material and can be closed with the least architectural uncertainty.

The first new specification should be `DOC-08` only after those existing active documents have been harmonized, so new contracts are built on a cleaner canonical baseline.
