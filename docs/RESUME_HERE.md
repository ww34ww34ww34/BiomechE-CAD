# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-15  
**Current phase:** **GEOMETRY ENGINE EVALUATION — SCORECARD BASELINE v0.1 COMPLETE; PoC QUALIFICATION NEXT.**  
**Selection status:** **NO GEOMETRY ENGINE SELECTED.**

The P0 authoring documentation remains frozen v1. The geometry-engine scorecard has now been derived from the frozen contracts and `AUTH-C01..C22`; the next executable architecture task is the candidate-neutral PoC/benchmark qualification sequence. Project Schema v0.2 remains approved but not materialized. GitHub CI remains deliberately deferred as `TD-CI-001` and is not a gate for this phase.

---

## 1. Read these first

1. `docs/RESUME_HERE.md`
2. `docs/P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md`
3. `docs/SPEC_INDEX.md`
4. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
5. `docs/TRACEABILITY_MATRIX.md`
6. `docs/spec/01_coordinate_registration.md`
7. `docs/spec/02_project_schema.md`
8. `docs/spec/16_geometry_authoring_contract.md`
9. `docs/spec/17_workflow_preset_macro.md`
10. `docs/spec/18_numerical_qualification_registry.md`
11. `docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`
12. `docs/spec/19_project_schema_v0_2_changeset.md`
13. `docs/validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md`
14. `docs/validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md`
15. `docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md`
16. `docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`
17. `docs/DECISIONS.md`
18. `docs/TECHNICAL_DEBT.md`
19. `docs/BIBLIOGRAPHY.md`
20. `docs/NEXT_CHAT_PROMPT.md`

Additional frozen/context specs remain authoritative where referenced: `11_biomeche_integration.md`, `12_reporting_traceability.md`, `15_pressure_acquisition_qualification.md`.

`BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` is the functional authority. The old functional spec is historical/audit material.

---

## 2. Mission

BiomechE-CAD is a vertical CAD for custom foot orthoses. It should match mature orthotic-CAD productivity while preserving stronger scientific and lifecycle semantics:

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

The geometry engine is downstream of these contracts and is replaceable implementation infrastructure, not clinical/domain authority.

---

## 3. Current work order

```text
FUNCTIONALITY + EASYCAD2 + SCIENTIFIC EVIDENCE       DONE baseline
FUNCTIONAL SPEC v2                                   CANONICAL
PROJECT SCHEMA / PROVENANCE                          ACTIVE baseline v0.1
COORDINATE / REGISTRATION                            FROZEN v1
BIOMECHE INTEGRATION                                 FROZEN v1
REPORTING / TRACEABILITY                             FROZEN v1
PRESSURE ACQUISITION QUALIFICATION METHOD            FROZEN v1
COMPETITOR + LITERATURE SECOND PASS                  DONE
REQUIREMENT TRACEABILITY                             ACTIVE canonical baseline
GEOMETRY AUTHORING CONTRACT                          FROZEN v1
WORKFLOW / PRESET / MACRO CONTRACT                   FROZEN v1
NUMERICAL / TOLERANCE / QUALIFICATION REGISTRY      FROZEN v1
P0 AUTHORING ACCEPTANCE CATALOG                      FROZEN semantic test-spec v1 — 22 scenarios
PROJECT SCHEMA v0.2 CHANGE-SET                       APPROVED / NOT MATERIALIZED
CROSS-DOCUMENT AUDIT                                 DONE — 0 blockers
ACCEPTANCE SUITE INTEGRATION                         DONE — canonical addendum v1
P0 AUTHORING FREEZE AUDIT                            DONE — architecture-entry GO
GEOMETRY ENGINE EVALUATION SCORECARD                 DONE baseline v0.1 — NO WINNER
GEOMETRY ENGINE POC/QUALIFICATION PLAN               DONE plan v0.1 — EXECUTION NEXT
ARCHITECTURE SHOOT-OUT / FINAL SELECTION             BLOCKED ON POC EVIDENCE
```

Principal candidates remain:

```text
A. product-owned clinical/domain layer + Pixar OpenSubdiv
B. product-owned clinical/domain layer + openNURBS / ON_SubD
```

Other geometry libraries are not admitted by default.

---

## 4. Frozen product principles — DO NOT REOPEN WITHOUT NEW EVIDENCE/DECISION

- EasyCAD2 is behavioral evidence, not scientific truth.
- BiomechE-CAD is orthosis-specific, not generic CAD.
- A committed `DesignRevision` is immutable.
- Semantic prescription survives final geometry.
- Capture context and landmark provenance are first-class when design-relevant.
- Dose, units, placement, side and anatomical reference are structured data.
- Placement is typed anatomical/reference semantics, not anonymous XYZ.
- Raw acquisitions/results remain immutable/hash-addressed evidence.
- Reusable definitions resolve exact `id + version + hash/snapshot` and retain historical expansion.
- Geometry dose and mechanical/material dose are distinct.
- Mirror is semantic and side-aware.
- Pressure is quantitative; heatmaps are derived views.
- Offloading is target ROI + safety ring + remote redistribution.
- Scientific thresholds are population/protocol/ROI specific.
- `MeasuredOutcome != PredictedOutcome`.
- `UNAVAILABLE` is never zero.
- `OPEN` remains `OPEN`.
- Algorithm tolerance, device limit, manufacturing tolerance and clinical threshold are different authority classes.
- BiomechE is KPI authority; CAD owns prescription/design/lifecycle semantics.
- `DesignRevision != ManufacturingArtifact != PhysicalOrthosis`.
- CAD nominal geometry != measured manufactured geometry.
- Reports are immutable derived artifacts over exact source entities.
- The geometry kernel must satisfy the frozen contract, never redefine it.

Canonical units:

```text
mm, s, N, kPa, deg, mm²
```

---

## 5. P0 frozen authoring package

### Geometry Authoring Contract — `spec/16_geometry_authoring_contract.md`

Key frozen rules:

```text
semantic operation is authoritative
preview != committed revision
invalid/unresolved state is explicit
capture condition survives into design provenance
landmark provenance includes source method/review state
placement uses typed anatomical/reference semantics
requested dose and constrained realized dose are distinguishable
geometry dose != mechanical dose
sculpt must be replayable, not anonymous baked mesh state
scan conform keeps source/registration/ROI/projection/residual/version provenance
mirror transforms semantics, not only coordinates
inspection definitions are reproducible
clinical/contact surface intent is separate from production realization
deterministic replay is version-bound
```

### Workflow / Preset / Macro — `spec/17_workflow_preset_macro.md`

```text
PresetDefinition      one operation/family
WorkflowDefinition    ordered reusable multi-step knowledge
WorkflowApplication   project-owned exact expansion
```

Exact version/hash, typed inputs, explicit defaults/overrides/dependencies, compatibility/mirror policies, deterministic expansion and human confirmation are frozen.

### Numerical / Tolerance / Qualification — `spec/18_numerical_qualification_registry.md`

Authority classes include:

```text
CONVENTION
UI_CONVENIENCE_DEFAULT
PRODUCT_DEFAULT
EVIDENCE_PROFILE_RULE
ALGORITHM_PARAMETER
ALGORITHM_NUMERICAL_TOLERANCE
DEVICE_QUALIFICATION_LIMIT
MANUFACTURING_ACCEPTANCE_LIMIT
OUTCOME_INTERPRETATION_RULE
```

Status/lifecycle vocabulary:

```text
OPEN
PROVISIONAL
QUALIFIED
FROZEN_CONVENTION
DEPRECATED
```

No cross-class silent fallback is allowed.

---

## 6. P0 Authoring Acceptance — FROZEN

Canonical catalog: `docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`.

```text
AUTH-C01..C14  geometry / acquisition / inspection
AUTH-C15..C18  workflow / macro
AUTH-C19..C22  numerical governance
```

Frozen namespaces:

```text
GAUTH-001..040
WFLOW-001..030
NREG-001..030
```

The geometry scorecard maps all 22 scenarios to architecture tests. `C17/C19/C20/C21` are mainly product/governance compatibility tests rather than reasons to prefer a geometry library; the stack must nevertheless not make them impossible.

---

## 7. Geometry Engine Evaluation Scorecard — BASELINE v0.1

Canonical file:

`docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md`

Evaluation order is frozen for this architecture pass:

```text
1. HARD GATES
2. WEIGHTED CRITERIA
3. POC/BENCHMARK UNCERTAINTIES
4. FINAL EVIDENCE-GRADED SCORING
```

Hard gates cover:

```text
HG-01 product-owned semantic isolation
HG-02 replayable derived geometry
HG-03 stable authoring coordinates / IDs
HG-04 limit/surface differential queries
HG-05 local deformation / sculpt / semantic mirror feasibility
HG-06 spatial query / scan-conform path
HG-07 reproducible inspection path
HG-08 production realization / DFM path
HG-09 explicit numerical control
HG-10 one C++ core native/server/web-WASM
HG-11 interactive/incremental feasibility
HG-12 large-scan feasibility
HG-13 license/distribution acceptability
HG-14 API/dependency containment
HG-15 AUTH-C01..C22 coverage
```

Weighted criteria total **100 points** and are applied only after hard-gate compatibility. License is deliberately a hard gate, not a compensable score.

Evidence grades:

```text
A  current primary evidence + project PoC
B  current primary API/source evidence only
C  inference/indirect evidence
U  unknown / not demonstrated
```

No final candidate recommendation is allowed while a selection-critical hard gate remains `UNKNOWN`.

---

## 8. Current candidate evidence snapshot

### OpenSubdiv

Evaluation baseline: upstream `v3.7.0`.

Current primary evidence is strongest for:

```text
focused high-performance SubD evaluation
static-topology deforming surfaces at interactive rates
limit-surface basis evaluation
first/second derivative basis access
lean C++ core — standard-library-only core dependency statement
optional CPU/GPU evaluation backends
```

Still requires PoC/adapter proof for:

```text
WASM product build
stable product authoring addressing
nearest-point / scan projection
large-scan acceleration
sections / thickness / deviation
production lower surface / closure / solid
minimum-thickness / DFM
.NET
STL/3MF/CNC handoff
cross-platform determinism
```

### openNURBS / ON_SubD

Evaluation baseline: upstream `v8.32.26160.13001`.

Current primary evidence is strongest for:

```text
broader C++ geometry/interchange toolkit
ON_SubD surface/limit-point concepts
surface tangent/normal data
component evaluation caches/invalidation
SubD surface mesh fragments
3DM ecosystem/interchange
```

`rhino3dm 8.32.1` provides current family-level evidence for `.NET` and JavaScript/WebAssembly/browser deployment. This is **not** proof that every native `ON_SubD` authoring API has WASM parity.

A direct public `ON_SubD::ClosestPoint`-style primitive has not yet been established by the reviewed public SubD header, so nearest-point/projection remains PoC/adapter territory.

### No selection conclusion yet

Current evidence lead only:

```text
OpenSubdiv     focused evaluator / lean core / explicit derivative evaluation
ON_SubD        toolkit breadth / existing .NET + WASM family precedent
```

Selection-critical unknowns remain spatial queries, production-body/DFM, determinism, interactive workload performance and complete frozen acceptance coverage.

---

## 9. PoC / qualification plan

Canonical plan:

`docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`

Execution sequence:

```text
Q0  native build/dependency audit + direct WASM build
Q1  canonical representation/replay + derivatives/normals
Q2  local authoring + sculpt + semantic mirror
Q3  scan/spatial queries + inspection
Q4  production body / lower surface / closure / DFM
Q5  determinism + incremental invalidation/performance
Q6  rendering interop + .NET boundary + manufacturing handoff
Q7  engine-backed AUTH-C01..C22 harness + final score
```

Candidate-neutral fixtures must be used before candidate-specific optimization.

First benchmark pass is **MEASURED / NOT YET QUALIFIED** where no engineering performance budget exists. Do not invent p95/memory/WASM limits silently. A future `ARCH-PERF-*` profile must explicitly own those budgets before PASS/FAIL is declared.

Replay epsilon remains an `ALGORITHM_NUMERICAL_TOLERANCE`; it must never be borrowed from manufacturing acceptance tolerance.

---

## 10. Auxiliary-library admission rule

OCCT, Manifold, CGAL, libigl, geometry-central or another library enters only when a frozen hard gate + failed/insufficient PoC demonstrates a specific missing primitive.

Required admission conditions:

```text
concrete frozen requirement
measured/proven gap
sharply bounded responsibility
no second semantic geometry authority
product-owned serialization/replay remains canonical
license/WASM/dependency/performance evaluated
replaceable adapter boundary
```

The first likely trigger to investigate is **HG-08 / production realization**, but no auxiliary library is currently approved or selected.

---

## 11. Project Schema v0.2 — unchanged

`docs/spec/19_project_schema_v0_2_changeset.md` remains:

```text
APPROVED CHANGE-SET / NOT MATERIALIZED
```

Do not modify JSON Schema, fixtures or migrations as part of geometry-engine evaluation unless separately authorized.

---

## 12. CI / GitHub Actions technical debt — intentionally deferred

Canonical debt register: `docs/TECHNICAL_DEBT.md`.

```text
TD-CI-001 — GitHub Actions / fixture-validation reliability
STATUS: DEFERRED BY PROJECT OWNER — NON-BLOCKING FOR CURRENT PHASE
```

Rules:

```text
CI does not block documentation or architecture-analysis work.
Current green CI is not proof that main is fully qualified.
Semantic requirements are not weakened/deleted because the harness is behind.
Do not spend geometry-engine evaluation time fixing CI.
```

---

## 13. DONE

- [x] Functional v2 canonical.
- [x] Coordinate/registration v1 frozen.
- [x] BiomechE integration v1 frozen.
- [x] Reporting/traceability v1 frozen.
- [x] Pressure qualification methodology v1 frozen.
- [x] Geometry Authoring Contract **FROZEN v1**.
- [x] Workflow/Preset/Macro Contract **FROZEN v1**.
- [x] Numerical/Tolerance/Qualification Registry **FROZEN v1**.
- [x] P0 Authoring Acceptance Catalog **FROZEN semantic test-spec v1** — 22 scenarios.
- [x] Project Schema v0.2 change-set **APPROVED / NOT MATERIALIZED**.
- [x] Cross-document audit — 0 blockers.
- [x] Acceptance-suite integration addendum v1.
- [x] Definitive P0 authoring freeze audit — architecture-entry GO.
- [x] Geometry Engine Evaluation Scorecard **baseline v0.1**.
- [x] Hard gates separated from weighted criteria.
- [x] `GAUTH/WFLOW/NREG/AUTH-Cxx` mapped to stack capabilities/tests.
- [x] Updated primary-source comparison OpenSubdiv vs ON_SubD captured.
- [x] Candidate uncertainties converted into explicit PoCs.
- [x] Geometry Engine PoC/Qualification Plan **v0.1**.
- [x] No engine selected prematurely.
- [x] `TD-CI-001` remains excluded from current gating.

---

## 14. TODO — exact restart point

### NEXT A — Q0 build / portability qualification

For **both candidates**, before optimization:

1. pin exact upstream tag/commit;
2. create the same narrow product-owned C++20 adapter/harness;
3. build native desktop Release;
4. build headless/server target;
5. capture dependency/link/binary manifest;
6. attempt direct Emscripten/WebAssembly build of the same core/adapter;
7. record bundle/heap/startup and native-vs-WASM numerical evidence where executable.

### NEXT B — shared canonical geometry fixture

Then create candidate-neutral `FIX-GEOM-01` and execute representation/replay + point/derivative/normal tests before implementing high-level orthosis operators.

### AFTER

Proceed Q2..Q7 and fill weighted scores only with evidence grades. Final architecture selection remains blocked until selection-critical hard gates close.

### PARALLEL

Real FM12050/material/manufacturing qualification when physical evidence is available.

### DEFERRED

`TD-CI-001` — dedicated future CI/validator repair pass.

---

## 15. New-chat handover

A copy/paste continuation prompt is maintained at:

`docs/NEXT_CHAT_PROMPT.md`

That prompt must now resume from **Q0 Geometry Engine PoC Qualification**, not from generic CAD research or from scorecard design.