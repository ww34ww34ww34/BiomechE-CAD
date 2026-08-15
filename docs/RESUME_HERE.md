# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-15  
**Current phase:** **P0 authoring-contract freeze**. Product/domain discovery is mature. Geometry-authoring, workflow/macro and numerical-governance contracts exist as canonical drafts; 22 representative architecture-independent acceptance scenarios are specified; the Project Schema v0.2 evolution is documented but not materialized; the cross-document audit found **0 blocking semantic contradictions**; acceptance-suite integration is complete through a canonical addendum. GitHub CI remains deferred as `TD-CI-001` and is not a documentation gate.

---

## 1. Read these first

1. `docs/RESUME_HERE.md`
2. `docs/SPEC_INDEX.md`
3. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
4. `docs/TRACEABILITY_MATRIX.md`
5. `docs/spec/02_project_schema.md`
6. `docs/spec/01_coordinate_registration.md`
7. `docs/spec/16_geometry_authoring_contract.md`
8. `docs/spec/17_workflow_preset_macro.md`
9. `docs/spec/18_numerical_qualification_registry.md`
10. `docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`
11. `docs/spec/19_project_schema_v0_2_changeset.md`
12. `docs/validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md`
13. `docs/validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md`
14. `docs/spec/11_biomeche_integration.md`
15. `docs/spec/12_reporting_traceability.md`
16. `docs/spec/15_pressure_acquisition_qualification.md`
17. `docs/research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md`
18. `docs/TECHNICAL_DEBT.md`
19. `docs/DECISIONS.md`
20. `docs/BIBLIOGRAPHY.md`

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
GEOMETRY AUTHORING CONTRACT                          CANONICAL DRAFT v0.1
WORKFLOW / PRESET / MACRO CONTRACT                   CANONICAL DRAFT v0.1
NUMERICAL / TOLERANCE / QUALIFICATION REGISTRY      CANONICAL DRAFT v0.1
P0 AUTHORING ACCEPTANCE CATALOG                      DONE v0.1 — 22 scenarios
PROJECT SCHEMA v0.2 CHANGE-SET                       DONE design draft / NOT MATERIALIZED
CROSS-DOCUMENT AUDIT                                 DONE — 0 blocking contradictions
ACCEPTANCE SUITE INTEGRATION                         DONE — canonical addendum v1
FINAL STATUS NORMALIZATION / FREEZE 16+17+18         NEXT
GEOMETRY ENGINE EVALUATION SCORECARD                 AFTER FREEZE
ARCHITECTURE SHOOT-OUT                               LATER
```

OpenSubdiv vs openNURBS/ON_SubD remains parked.

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

Canonical units:

```text
mm, s, N, kPa, deg, mm²
```

---

## 5. Geometry Authoring Contract

Canonical draft: `docs/spec/16_geometry_authoring_contract.md`.

Core P0 rules:

```text
semantic operation is authoritative
preview != committed revision
invalid/unresolved state is explicit
capture condition survives into design provenance
landmark provenance includes source method/review state
placement uses a typed reference, not anonymous XYZ
requested dose and constrained realized dose are distinguishable
geometry dose != mechanical dose
mirror transforms semantics, not only coordinates
inspection definitions are reproducible
clinical/contact surface intent is separate from production realization
deterministic replay is version-bound
```

Required P0 operation families include template/outline/sizing, medial/lateral arch, heel cup/relief/camber/medial heel skive/mechanical heel region, rear/forefoot wedge, corrective element, offload feature, sculpt, scan conform and height/thickness/DFM constraints.

Typed placement modes include:

```text
INTRINSIC_SQ
LANDMARK_RELATIVE_MM
LANDMARK_LINE_RELATIVE_MM
NORMALIZED_FOOT_LENGTH
ROI_RELATIVE
PRESSURE_TARGET_RELATIVE
CUSTOM_REGISTERED_REFERENCE
```

---

## 6. Workflow / Preset / Macro Contract

Canonical draft: `docs/spec/17_workflow_preset_macro.md`.

Market audit promoted reusable workflow knowledge to:

```text
P0 semantic infrastructure
P1 advanced automation / UX
```

Model:

```text
PresetDefinition      one operation/family
WorkflowDefinition    ordered reusable multi-step knowledge
WorkflowApplication   project-owned exact expansion
```

Rules include exact version/hash, typed inputs, explicit defaults/overrides/dependencies, compatibility and mirror policies, deterministic expansion, suggestion != confirmation and historical immutability.

---

## 7. Numerical / Tolerance / Qualification Registry

Canonical draft: `docs/spec/18_numerical_qualification_registry.md`.

Authority classes:

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

Governed rules carry ID/version, unit, scope, owner and status:

```text
OPEN
PROVISIONAL
QUALIFIED
FROZEN_CONVENTION
DEPRECATED
```

Doctrine:

```text
study dose != universal default
display precision != acceptance tolerance
algorithm replay epsilon != manufacturing tolerance
landmark uncertainty != registration tolerance != manufacturing tolerance
no global CAD_TOLERANCE
missing qualification limit never falls back to a UI convenience value
```

---

## 8. P0 Authoring Acceptance

Canonical catalog: `docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`.

22 representative architecture-independent scenarios cover arch, heel, wedge, met-pad placement modes, pressure-target offload, sculpt, scan conform, requested-vs-realized geometry, weight-bearing `UNKNOWN`, landmark review provenance, section/distance/thickness, CAD-vs-part deviation, workflow versioning/overrides/confirmation/mirror and numerical-rule resolution.

Integration with the older acceptance suite is now explicit through:

`docs/validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md`

New namespaces:

```text
GAUTH-001..040
WFLOW-001..030
NREG-001..030
```

The owning specs remain normative; the addendum avoids duplicating all definitions into the older suite.

---

## 9. Cross-document audit

Canonical audit:

`docs/validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md`

Result:

```text
BLOCKING CONTRADICTIONS             0
NON-BLOCKING HARMONIZATIONS         5
NEW ARCHITECTURE DEPENDENCIES       0
NEW UNIVERSAL CLINICAL DEFAULTS     0
NEW UNIVERSAL MANUFACTURING LIMITS  0
```

Non-blocking harmonizations recorded:

```text
HARM-001  richer placement vocabulary in 16 supersedes compact wording in 06
HARM-002  manufacturing literal limits gain future NumericalRule refs
HARM-003  WorkflowApplication materialized in schema v0.2 later
HARM-004  machine-readable NumericalRule registry later
HARM-005  acceptance-suite integration — NOW CLOSED by canonical addendum v1
```

The package is semantically ready for final status normalization/freeze.

---

## 10. Project Schema v0.2 change-set

Design document: `docs/spec/19_project_schema_v0_2_changeset.md`.

**No JSON Schema, fixture or migration has been changed.**

Proposed additive evolution:

```text
formal ScanAcquisition captureContext
richer Landmark source/review provenance
workflowDefinitions[]
workflowApplications[]
sourceWorkflowApplicationRef / workflowStepId
ParameterOverrideRecord
NumericalRuleRef
OperationEvaluation requested-vs-realized state
GeometryInspection typed measurements
manufacturing acceptance-rule refs
optional acquisition-compatibility assessment
```

Migration doctrine:

```text
missing historical information -> UNKNOWN / LEGACY_UNKNOWN
never invent provenance
standalone v0.1 operations remain valid without fabricated workflow history
```

---

## 11. CI / GitHub Actions technical debt — deferred

Canonical debt register: `docs/TECHNICAL_DEBT.md`.

```text
TD-CI-001 — GitHub Actions / fixture-validation reliability
STATUS: DEFERRED BY PROJECT OWNER — NON-BLOCKING FOR DOCUMENTATION
```

Known issues include 19 current fixtures with 3 newer IDs not recognized by the current validator and a shell pipeline that can hide validator failure through `| tee` without explicit `pipefail`.

Current rule:

```text
CI does not block documentation/specification work.
Current green CI is not proof that main is fully qualified.
Semantic requirements are not weakened/deleted because the harness is behind.
```

Fix later in a dedicated engineering pass using the exit criteria in `TECHNICAL_DEBT.md`.

---

## 12. Pressure/device qualification state

Methodology: `spec/15_pressure_acquisition_qualification.md` — frozen.

FM12050/PFM2120:

```text
source/family intake               DONE
bench protocol structure           READY
machine-readable result form       READY
real physical-unit qualification   NOT DONE
sensor geometry/conversion         TO QUALIFY
numeric PASS limits                profile/evidence owned
```

This can proceed in parallel when hardware/reference evidence is available.

---

## 13. Architecture state — PARKED

Historical architecture hypotheses remain useful evidence:

```text
spec/03_geometry_operation_model.md
spec/04_base_template.md
spec/05_parametric_orthosis_geometry.md
spec/CAD_ENGINE_CAPABILITY_SPEC.md
spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md
```

For product semantics, `16_geometry_authoring_contract.md` now takes precedence over the old OpenSubdiv-first hypothesis.

The eventual engine must satisfy the contract; the contract must not be rewritten around the engine.

---

## 14. DONE

- [x] Functional v2 canonical.
- [x] Project Schema v0.1 baseline.
- [x] Coordinate/registration v1 frozen.
- [x] BiomechE integration v1 frozen.
- [x] Reporting/traceability v1 frozen.
- [x] Pressure qualification methodology v1 frozen.
- [x] FM12050 family/source intake + bench plan.
- [x] Competitor + scientific evidence baseline and second pass.
- [x] Requirement Traceability Matrix v0.3.
- [x] Geometry Authoring Contract v0.1 drafted.
- [x] Workflow/Preset/Macro Contract v0.1 drafted.
- [x] Numerical/Tolerance/Qualification Registry v0.1 drafted.
- [x] P0 Authoring Acceptance Catalog — 22 scenarios.
- [x] Project Schema v0.2 change-set documented.
- [x] Cross-document audit — 0 blockers.
- [x] Acceptance-suite integration addendum v1.
- [x] README/SPEC_INDEX/handover realignment.
- [x] `TD-CI-001` recorded and removed from documentation gating.
- [x] Architecture remains parked.

---

## 15. TODO — exact restart point

### NEXT A — final documentation freeze

Normalize the status headers/cross-references and promote:

```text
16_geometry_authoring_contract.md          -> FROZEN v1
17_workflow_preset_macro.md                -> FROZEN v1
18_numerical_qualification_registry.md     -> FROZEN v1
P0_AUTHORING_ACCEPTANCE_CATALOG.md         -> FROZEN semantic test-spec v1
19_project_schema_v0_2_changeset.md        -> APPROVED CHANGE-SET / NOT MATERIALIZED
```

No CI repair is required for this semantic/documentation freeze.

### NEXT B — geometry-engine evaluation scorecard

Derive the architecture comparison directly from frozen requirements:

```text
semantic replay support
local orthotic deformation primitives
bilateral/mirror determinism
inspection queries
thickness/production realization
numerical reproducibility
performance
WASM/desktop/server portability
interoperability/export
implementation/dependency complexity
```

Then compare OpenSubdiv vs ON_SubD/other justified candidates.

### PARALLEL

Real FM12050, material and manufacturing-process qualification when physical evidence is available.

### DEFERRED

`TD-CI-001` — dedicated future CI/validator repair pass.
