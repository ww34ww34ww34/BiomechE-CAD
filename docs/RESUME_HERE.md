# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-16  
**Current phase:** **P0-DOC-CLOSURE — remaining product documentation + canonical visual reference package.**  
**Architecture status:** **NO GEOMETRY ENGINE SELECTED. Q0..Q7 PoC plan preserved but temporarily deferred by project priority.**

The P0 authoring core is frozen and remains authoritative. The project owner has chosen to continue documentation before executing geometry-engine PoCs. The current work plan is:

`docs/P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md`

The goal is to close the remaining `ACTIVE v0` / provisional product documents, add missing implementation-neutral contracts, perform a final cross-document audit, and then create/save a versioned set of visual mockups as a canonical visual/interaction reference.

Project Schema v0.2 remains **APPROVED / NOT MATERIALIZED**. `TD-CI-001` remains deliberately deferred and non-blocking.

---

## 1. Read these first

1. `docs/RESUME_HERE.md`
2. `docs/P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md`
3. `docs/SPEC_INDEX.md`
4. `docs/P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md`
5. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
6. `docs/TRACEABILITY_MATRIX.md`
7. `docs/spec/01_coordinate_registration.md`
8. `docs/spec/02_project_schema.md`
9. `docs/spec/16_geometry_authoring_contract.md`
10. `docs/spec/17_workflow_preset_macro.md`
11. `docs/spec/18_numerical_qualification_registry.md`
12. `docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`
13. `docs/spec/19_project_schema_v0_2_changeset.md`
14. `docs/validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md`
15. `docs/validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md`
16. `docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md`
17. `docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`
18. `docs/DECISIONS.md`
19. `docs/TECHNICAL_DEBT.md`
20. `docs/BIBLIOGRAPHY.md`
21. `docs/NEXT_CHAT_PROMPT.md`

`BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` remains the functional product authority. The previous functional spec is historical/audit material.

---

## 2. Mission

BiomechE-CAD is a vertical CAD for custom foot orthoses. It must combine mature orthotic-CAD productivity with stronger scientific and lifecycle semantics:

```text
acquisition provenance
+ semantic prescription
+ reproducible authoring
+ quantitative biomechanics
+ immutable design revision
+ material/manufacturing lineage
+ physical-part identity
+ measured outcome loop
+ reproducible reporting
```

The geometry engine is downstream infrastructure. It must satisfy product contracts and must never become the authority for clinical/domain semantics.

---

## 3. Frozen product principles — do not reopen without new evidence/decision

- EasyCAD2 is behavioral evidence, not scientific truth.
- BiomechE-CAD is orthosis-specific, not generic CAD.
- A committed `DesignRevision` is immutable.
- Semantic prescription survives final geometry.
- Capture context and landmark provenance are first-class when design-relevant.
- Placement is typed anatomical/reference semantics, not anonymous XYZ.
- Dose, units, placement, side and anatomical reference are structured data.
- Reusable definitions resolve exact `id + version + hash/snapshot` and preserve historical expansion.
- Geometry dose and mechanical/material dose are distinct.
- Mirror is semantic and side-aware.
- Pressure is quantitative; heatmaps are derived views.
- Offloading is target ROI + safety ring + remote redistribution.
- Scientific thresholds are population/protocol/ROI specific.
- `MeasuredOutcome != PredictedOutcome`.
- `UNAVAILABLE` is never zero.
- `OPEN` remains `OPEN`.
- Algorithm tolerance, device limit, manufacturing tolerance and clinical threshold are separate authority classes.
- BiomechE is KPI authority; CAD owns prescription/design/lifecycle semantics.
- `DesignRevision != ManufacturingArtifact != PhysicalOrthosis`.
- CAD nominal geometry != measured manufactured geometry.
- Reports are immutable derived artifacts over exact source entities.
- The geometry kernel must satisfy the frozen contract, never redefine it.

Canonical units remain:

```text
mm, s, N, kPa, deg, mm²
```

---

## 4. Frozen P0 authoring package

The following are already frozen/canonical and are inputs to the documentation-closure phase, not targets for redesign:

```text
01 coordinate / registration                  FROZEN v1
11 BiomechE integration                       FROZEN v1
12 reporting / traceability                   FROZEN v1
15 pressure-acquisition qualification method  FROZEN v1
16 Geometry Authoring Contract                FROZEN v1
17 Workflow / Preset / Macro Contract         FROZEN v1
18 Numerical / Tolerance / Qualification      FROZEN v1
P0 Authoring Acceptance Catalog               FROZEN semantic test-spec v1
AUTH-C01..C22                                  FROZEN scenarios
```

The prior cross-document audit found **0 blocking semantic contradictions**.

---

## 5. Current documentation closure scope

Canonical work plan:

`docs/P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md`

### Wave 1 — close existing ACTIVE v0 specifications

```text
DOC-00  baseline inventory / closure audit
DOC-01  06 corrective elements -> v1
DOC-02  08 material/stiffness -> v1
DOC-03  09 analysis/QC/DFM -> v1
DOC-04  10 manufacturing -> v1
DOC-05  13 use-case profiles -> v1
DOC-06  14 PROM/comfort/adherence -> v1
```

### Wave 2 — resolve provisional/historical ambiguity

```text
DOC-07  04 base template + 05 parametric orthosis geometry disposition
```

Each concept in `04/05` must become one of:

```text
PRODUCT SEMANTIC
ALGORITHM HYPOTHESIS
SUPERSEDED BY FROZEN CONTRACT
ENGINE-SPECIFIC
OPEN / UNSUPPORTED NUMERICAL DEFAULT
```

### Wave 3 — missing implementation-neutral contracts

```text
DOC-08  Input / Scan / Reference Data Contract
DOC-09  Product Workflow & Interaction Contract
DOC-10  Interchange & Manufacturing Handoff Contract
DOC-11  Realtime Interaction & Performance Contract
DOC-12  Validation & Verification Master Plan
```

### Wave 4 — safety/governance stream

```text
DOC-13  Intended Use / Risk / Privacy / Security boundary package
```

When executed, current regulatory/security facts and standards must be verified from current primary authoritative sources.

### Wave 5 — closure

```text
DOC-14  final cross-document audit + documentation freeze
```

Desired verdict:

```text
PRODUCT / FUNCTIONAL / SEMANTIC DOCUMENTATION: COMPLETE FOR P0
```

---

## 6. Visual reference package — required after documentation closure

The project owner explicitly requires a saved visual reference after the written product semantics are stable.

The visual package is part of the current plan, not an optional branding exercise.

Proposed authority document:

`docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md`

Proposed asset structure:

```text
docs/ux/mockups/v1/
```

Minimum canonical screens:

```text
M01 project / patient / case
M02 import / scan qualification
M03 registration / landmarks
M04 base orthosis / template
M05 parametric authoring
M06 corrective / offloading elements
M07 sculpt / local freeform edit
M08 materials / regional mechanical prescription
M09 inspection / geometry QC
M10 BiomechE before / after / delta
M11 DFM / manufacturing preparation
M12 revision / provenance / report
M13 physical-part QC / outcome follow-up
M14 compact / responsive reference
```

Where practical, preserve both:

```text
editable/source-controlled mockup form (HTML/CSS, SVG or equivalent)
+
rendered reference export (PNG or equivalent)
```

Each mockup must have a manifest entry linking it to the written requirements/spec sections it represents.

Authority rule:

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
MOCKUP = VISUAL / INTERACTION REFERENCE
```

A mockup may not silently redefine clinical/domain semantics.

---

## 7. Geometry engine evaluation — preserved, not cancelled

The architecture work already completed remains valid:

- Geometry Engine Evaluation Scorecard v0.1;
- hard gates `HG-01..HG-15`;
- weighted criteria = 100 points;
- OpenSubdiv vs openNURBS/ON_SubD evidence snapshot;
- candidate-neutral PoC qualification plan `Q0..Q7`;
- no winner selected.

Principal candidates remain:

```text
A. product-owned domain layer + Pixar OpenSubdiv
B. product-owned domain layer + openNURBS / ON_SubD
```

Architecture PoC execution resumes only after documentation/visual closure or by explicit project-owner decision.

Do not select a winner from research evidence alone.

---

## 8. Performance doctrine during documentation closure

Performance remains a first-class product requirement even while implementation is deferred.

`DOC-11` must define the product-owned performance contract for:

```text
input-to-preview latency
operation rebuild latency
commit latency
surface queries
scan registration/conform
inspection/deviation maps
render frame time
memory/allocation behavior
large-scan throughput
WASM startup/heap/transfer
serialization/replay
```

Do not invent PASS thresholds. Until explicit `ARCH-PERF-*` budgets are approved, measured results remain:

```text
MEASURED / NOT YET QUALIFIED
```

---

## 9. Project Schema v0.2 — unchanged

`docs/spec/19_project_schema_v0_2_changeset.md` remains:

```text
APPROVED CHANGE-SET / NOT MATERIALIZED
```

Do not modify JSON Schema, fixtures or migrations during documentation closure unless explicitly authorized.

---

## 10. CI technical debt — unchanged

`TD-CI-001` remains:

```text
DEFERRED BY PROJECT OWNER
NON-BLOCKING FOR CURRENT PHASE
```

Do not spend documentation-closure time repairing CI/validator infrastructure unless explicitly requested.

---

## 11. DONE

- [x] Functional spec v2 canonical.
- [x] Coordinate/registration v1 frozen.
- [x] BiomechE integration v1 frozen.
- [x] Reporting/traceability v1 frozen.
- [x] Pressure-acquisition qualification methodology v1 frozen.
- [x] Geometry Authoring Contract v1 frozen.
- [x] Workflow/Preset/Macro Contract v1 frozen.
- [x] Numerical/Tolerance/Qualification Registry v1 frozen.
- [x] P0 Authoring Acceptance Catalog `AUTH-C01..C22` frozen.
- [x] Project Schema v0.2 change-set approved / not materialized.
- [x] P0 authoring cross-document audit — 0 blockers.
- [x] Geometry Engine Evaluation Scorecard v0.1.
- [x] Geometry Engine PoC/Qualification Plan Q0..Q7.
- [x] No geometry engine selected prematurely.
- [x] `P0-DOC-CLOSURE` work plan created.
- [x] Canonical visual-reference/mockup phase included in the plan.

---

## 12. TODO — exact restart point

### NEXT — DOC-00

Execute:

```text
DOC-00 — P0 Documentation Closure Audit
```

Deliverable:

`docs/validation/P0_DOCUMENTATION_CLOSURE_AUDIT_2026-08-16.md`

The audit must inventory all `docs/spec/*` documents, classify authority/status, identify actual gaps/duplication, establish freeze criteria and verify that the current plan still has the right closure scope.

### THEN

Proceed sequentially with `DOC-01..DOC-06`, because those documents already contain substantial evidence/model/acceptance material and can be closed with low architecture uncertainty.

### AFTER WRITTEN CLOSURE

Execute `VIS-01..VIS-04` and save the visual baseline in the repository.

### ONLY AFTER THAT, unless explicitly reprioritized

Resume geometry-engine qualification `Q0..Q7`.

---

## 13. New-chat handover

Copy/paste continuation prompt:

`docs/NEXT_CHAT_PROMPT.md`

The next chat must resume from **DOC-00 P0 Documentation Closure Audit**, not from Q0 geometry-engine PoC and not from generic CAD market research.
