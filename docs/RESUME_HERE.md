# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-15  
**Current phase:** **P0 AUTHORING DOCUMENTATION FROZEN v1 — architecture-entry GO.** Product/domain discovery is mature. Geometry-authoring, workflow/macro and numerical-governance contracts are frozen; the P0 semantic acceptance catalog is frozen; Project Schema v0.2 is an approved change-set but is not materialized. The next principal task is the **Geometry Engine Evaluation Scorecard**. GitHub CI remains deferred as `TD-CI-001` and is not a documentation/architecture-analysis gate.

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
15. `docs/spec/11_biomeche_integration.md`
16. `docs/spec/12_reporting_traceability.md`
17. `docs/spec/15_pressure_acquisition_qualification.md`
18. `docs/research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md`
19. `docs/TECHNICAL_DEBT.md`
20. `docs/DECISIONS.md`
21. `docs/BIBLIOGRAPHY.md`
22. `docs/NEXT_CHAT_PROMPT.md`

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

The geometry engine is downstream of these contracts.

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
REQUIREMENT TRACEABILITY                             DONE v0.3
GEOMETRY AUTHORING CONTRACT                          FROZEN v1
WORKFLOW / PRESET / MACRO CONTRACT                   FROZEN v1
NUMERICAL / TOLERANCE / QUALIFICATION REGISTRY      FROZEN v1
P0 AUTHORING ACCEPTANCE CATALOG                      FROZEN semantic test-spec v1 — 22 scenarios
PROJECT SCHEMA v0.2 CHANGE-SET                       APPROVED / NOT MATERIALIZED
CROSS-DOCUMENT AUDIT                                 DONE — 0 blocking contradictions
ACCEPTANCE SUITE INTEGRATION                         DONE — canonical addendum v1
P0 AUTHORING FREEZE AUDIT                            DONE — architecture-entry GO
GEOMETRY ENGINE EVALUATION SCORECARD                 NEXT
ARCHITECTURE SHOOT-OUT                               AFTER SCORECARD
```

OpenSubdiv vs openNURBS/ON_SubD remains undecided.

---

## 4. Frozen product principles

- EasyCAD2 is behavioral evidence, not scientific truth.
- BiomechE-CAD is orthosis-specific, not generic CAD.
- A committed `DesignRevision` is immutable.
- Semantic prescription survives final geometry.
- Dose, units, placement, side and anatomical reference are structured data.
- Raw acquisitions/results remain immutable/hash-addressed evidence.
- Reusable definitions resolve exact `id + version + hash/snapshot`.
- Geometry dose and mechanical/material dose are distinct.
- Pressure is quantitative; heatmaps are derived views.
- Offloading is target ROI + safety ring + remote redistribution.
- Scientific thresholds are population/protocol/ROI specific.
- `MeasuredOutcome != PredictedOutcome`.
- `UNAVAILABLE` is never zero.
- BiomechE is KPI authority; CAD owns prescription/design/lifecycle semantics.
- `DesignRevision != ManufacturingArtifact != PhysicalOrthosis`.
- CAD nominal geometry != measured manufactured geometry.
- Reports are immutable derived artifacts over exact source entities.
- Device/manufacturing qualification is intended-use/profile-specific.
- Unknown numeric limits remain `OPEN`.
- Algorithm tolerance, device limit, manufacturing tolerance and clinical threshold are distinct authority classes.

Canonical units:

```text
mm, s, N, kPa, deg, mm²
```

---

## 5. P0 authoring package — FROZEN

### Geometry Authoring — `spec/16_geometry_authoring_contract.md`

Frozen v1 rules include:

```text
semantic operation is authoritative
preview != committed revision
invalid/unresolved state is explicit
capture condition survives into design provenance
landmark provenance includes source method/review state
placement uses typed anatomical/reference semantics
requested dose and constrained realized dose are distinguishable
geometry dose != mechanical dose
mirror transforms semantics, not only coordinates
inspection definitions are reproducible
clinical/contact surface intent is separate from production realization
deterministic replay is version-bound
```

Typed placement modes:

```text
INTRINSIC_SQ
LANDMARK_RELATIVE_MM
LANDMARK_LINE_RELATIVE_MM
NORMALIZED_FOOT_LENGTH
ROI_RELATIVE
PRESSURE_TARGET_RELATIVE
CUSTOM_REGISTERED_REFERENCE
```

### Workflow / Preset / Macro — `spec/17_workflow_preset_macro.md`

Frozen v1 model:

```text
PresetDefinition      one operation/family
WorkflowDefinition    ordered reusable multi-step knowledge
WorkflowApplication   project-owned exact expansion
```

Frozen rules include exact version/hash, typed inputs, explicit defaults/overrides/dependencies, compatibility and mirror policies, deterministic expansion, suggestion != confirmation and historical immutability.

### Numerical / Tolerance / Qualification — `spec/18_numerical_qualification_registry.md`

Frozen v1 authority classes:

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

Frozen status/lifecycle vocabulary:

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

22 representative architecture-independent scenarios:

```text
AUTH-C01..C14  geometry / acquisition / inspection
AUTH-C15..C18  workflow / macro
AUTH-C19..C22  numerical governance
```

New acceptance namespaces:

```text
GAUTH-001..040
WFLOW-001..030
NREG-001..030
```

Integration with the older acceptance baseline is canonical through:

`docs/validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md`.

`TD-CI-001` affects future execution infrastructure, not these frozen semantic expectations.

---

## 7. Cross-document and freeze audit

Cross-audit:

`docs/validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md`

Result:

```text
BLOCKING CONTRADICTIONS             0
NON-BLOCKING HARMONIZATIONS         5
NEW ARCHITECTURE DEPENDENCIES       0
NEW UNIVERSAL CLINICAL DEFAULTS     0
NEW UNIVERSAL MANUFACTURING LIMITS  0
```

Definitive freeze audit:

`docs/P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md`

Verdict:

```text
P0 AUTHORING DOCUMENTATION       FROZEN v1
ARCHITECTURE EVALUATION          GO
GEOMETRY KERNEL SELECTION        NOT YET DECIDED
SCHEMA v0.2                      APPROVED CHANGE-SET / NOT MATERIALIZED
REAL DEVICE/PROCESS LIMITS       QUALIFICATION PENDING
CI                              DEFERRED TECHNICAL DEBT
```

---

## 8. Project Schema v0.2

`docs/spec/19_project_schema_v0_2_changeset.md` is now:

```text
APPROVED CHANGE-SET / NOT MATERIALIZED
```

Approved additive concepts:

```text
formal Scan captureContext
richer Landmark provenance/review
workflowDefinitions[]
workflowApplications[]
ParameterOverrideRecord
NumericalRuleRef
OperationEvaluation requested-vs-realized state
GeometryInspection typed measurements
manufacturing acceptance-rule refs
optional acquisition-compatibility assessment
```

Current machine-readable schema remains v0.1. No JSON Schema, migration or fixture change is implied by approval.

---

## 9. CI / GitHub Actions technical debt — intentionally deferred

Canonical debt register: `docs/TECHNICAL_DEBT.md`.

```text
TD-CI-001 — GitHub Actions / fixture-validation reliability
STATUS: DEFERRED BY PROJECT OWNER — NON-BLOCKING FOR DOCUMENTATION
```

Rules while open:

```text
CI does not block documentation or architecture-analysis work.
Current green CI is not proof that main is fully qualified.
Semantic requirements are not weakened/deleted because the harness is behind.
Future CI repair begins from TECHNICAL_DEBT.md.
```

Do not reopen this debt during the geometry-engine scorecard unless the project owner explicitly asks.

---

## 10. Pressure/device/material qualification state

Pressure methodology is frozen; real performance values are not.

FM12050/PFM2120:

```text
source/family intake               DONE
bench protocol structure           READY
machine-readable result form       READY
real physical-unit qualification   NOT DONE
sensor geometry/conversion         TO QUALIFY
numeric PASS limits                profile/evidence owned
```

Material/manufacturing semantics are mature, but real machine/process/material tolerances remain qualification-owned.

These tracks can proceed in parallel when physical evidence is available and do not reopen the P0 authoring freeze.

---

## 11. Architecture state

Historical architecture material remains useful background:

```text
spec/03_geometry_operation_model.md
spec/04_base_template.md
spec/05_parametric_orthosis_geometry.md
spec/CAD_ENGINE_CAPABILITY_SPEC.md
spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md
research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md
```

For product/domain semantics, the frozen P0 authoring package takes precedence.

The future engine must satisfy the contract; the contract must not be rewritten around the engine.

---

## 12. DONE

- [x] Functional v2 canonical.
- [x] Project Schema v0.1 baseline.
- [x] Coordinate/registration v1 frozen.
- [x] BiomechE integration v1 frozen.
- [x] Reporting/traceability v1 frozen.
- [x] Pressure qualification methodology v1 frozen.
- [x] FM12050 family/source intake + bench plan.
- [x] Competitor + scientific evidence baseline and second pass.
- [x] Requirement Traceability Matrix v0.3.
- [x] Geometry Authoring Contract **FROZEN v1**.
- [x] Workflow/Preset/Macro Contract **FROZEN v1**.
- [x] Numerical/Tolerance/Qualification Registry **FROZEN v1**.
- [x] P0 Authoring Acceptance Catalog **FROZEN semantic test-spec v1** — 22 scenarios.
- [x] Project Schema v0.2 change-set **APPROVED / NOT MATERIALIZED**.
- [x] Cross-document audit — 0 blockers.
- [x] Acceptance-suite integration addendum v1.
- [x] Definitive P0 authoring freeze audit.
- [x] Canonical next-chat prompt.
- [x] `TD-CI-001` recorded and excluded from documentation gating.
- [x] Architecture still unselected.

---

## 13. TODO — exact restart point

### NEXT A — Geometry Engine Evaluation Scorecard

Derive hard gates and weighted criteria **directly from the frozen contracts and `AUTH-C01..C22`**.

At minimum cover:

```text
semantic/domain isolation
stable/replayable representation
SubD/surface quality
local parametric deformation
sculpt/freeform feasibility
mirror/bilateral behavior
surface point/normal/derivative queries
scan nearest-point/projection/conform support
section/distance/height/angle/thickness queries
deviation-map feasibility
production body / lower-surface / closure path
minimum-thickness / DFM path
determinism / numerical control
interactive performance / incremental invalidation
large scan handling
C++20 compatibility
single-core portability desktop/server/web-WASM
license / API stability / transitive dependencies
serialization isolation
.NET interoperability where useful
STL/3MF/CNC/manufacturing handoff
frozen acceptance-scenario coverage
```

Principal candidates to start with:

```text
A. product-owned clinical layer + Pixar OpenSubdiv
B. product-owned clinical layer + openNURBS / ON_SubD
```

Do not choose a winner before defining the scorecard.

### NEXT B — Candidate research / PoC plan

Use current primary sources for APIs, versions, licenses, WASM/portability and dependency graphs. Identify unknowns that require proof-of-concept benchmarks rather than assumptions.

### PARALLEL

Real FM12050/material/manufacturing qualification when physical evidence is available.

### DEFERRED

`TD-CI-001` — dedicated future CI/validator repair pass.

---

## 14. New-chat handover

A copy/paste continuation prompt is maintained at:

`docs/NEXT_CHAT_PROMPT.md`

Use that prompt when moving to another conversation.