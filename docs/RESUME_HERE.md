# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-15  
**Current phase:** P0 authoring-contract formalization. Product/domain discovery is mature; geometry-authoring, workflow/macro and numerical-governance contracts exist as canonical drafts, representative architecture-independent acceptance scenarios are specified, and the Project Schema v0.2 evolution is documented but not yet materialized. GitHub CI is explicitly deferred as technical debt and is not a documentation gate.

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
12. `docs/spec/11_biomeche_integration.md`
13. `docs/spec/12_reporting_traceability.md`
14. `docs/spec/15_pressure_acquisition_qualification.md`
15. `docs/research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md`
16. `docs/TECHNICAL_DEBT.md`
17. `docs/DECISIONS.md`
18. `docs/BIBLIOGRAPHY.md`

`BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` is the current functional authority. The old functional spec is historical/audit material.

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
REQUIREMENT TRACEABILITY                             DONE v0.1
GEOMETRY AUTHORING CONTRACT                          CANONICAL DRAFT v0.1
WORKFLOW / PRESET / MACRO CONTRACT                   CANONICAL DRAFT v0.1
NUMERICAL / TOLERANCE / QUALIFICATION REGISTRY      CANONICAL DRAFT v0.1
P0 AUTHORING ACCEPTANCE CATALOG                      DONE v0.1
PROJECT SCHEMA v0.2 CHANGE-SET                       DONE design draft / NOT MATERIALIZED
CROSS-DOCUMENT REVIEW + FREEZE                       NEXT
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

## 5. Geometry Authoring Contract — current P0 direction

Canonical draft:

`docs/spec/16_geometry_authoring_contract.md`

Key rules:

```text
semantic operation is authoritative
preview != committed revision
invalid/unresolved state is explicit
capture condition survives into design provenance
landmark provenance includes source method/review state
placement uses a typed reference, not anonymous XYZ
requested dose and realized constrained dose can differ explicitly
geometry dose != mechanical dose
mirror transforms semantics, not only coordinates
inspection definitions are reproducible
clinical/contact surface intent is separate from production realization
deterministic replay is version-bound
```

Required P0 operation families include:

```text
template / outline / sizing
medial + lateral arch
heel cup / relief / camber / medial heel skive / mechanical heel region
rearfoot + forefoot wedge
corrective element
offload feature
sculpt
scan conform
height/thickness/DFM constraints
```

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

Canonical draft:

`docs/spec/17_workflow_preset_macro.md`

Market audit showed reusable design knowledge is table stakes, so `GAP-COMP-001` is now:

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

Rules include exact version/hash, typed inputs, explicit defaults/overrides/dependencies, compatibility and mirror policy, deterministic expansion, suggestion != confirmation and historical immutability.

---

## 7. Numerical / Tolerance / Qualification Registry

Canonical draft:

`docs/spec/18_numerical_qualification_registry.md`

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

Every governed number has rule ID/version, units, scope, owner and status:

```text
OPEN
PROVISIONAL
QUALIFIED
FROZEN_CONVENTION
DEPRECATED
```

Critical doctrine:

```text
study dose != universal default
display precision != acceptance tolerance
algorithm replay epsilon != manufacturing tolerance
landmark uncertainty != registration tolerance != manufacturing tolerance
no global CAD_TOLERANCE
no fallback from missing qualification limit to a UI default
```

---

## 8. P0 Authoring Acceptance Catalog

Canonical test specification:

`docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`

It currently defines 22 representative architecture-independent scenarios, including:

```text
arch dose/placement
heel semantic decomposition
wedge side/mirror semantics
met-pad landmark-relative vs normalized placement
pressure-target offload
sculpt replay
scan conform
requested vs constrained realized dose
weight-bearing UNKNOWN behavior
landmark review provenance
section/distance/thickness semantics
CAD-vs-physical deviation map
workflow version expansion
overrides
suggestion vs confirmation
unsafe mirror blocking
OPEN manufacturing tolerance
UI default not usable as qualification limit
profile-scoped evidence rule
replay epsilon distinct from part tolerance
```

Synthetic test numbers are explicitly non-clinical.

---

## 9. Project Schema v0.2 change-set

Design document:

`docs/spec/19_project_schema_v0_2_changeset.md`

**Important:** no JSON Schema, fixture or migration has been changed yet.

Proposed additive evolution covers:

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
manufacturing acceptance rule refs
optional acquisition-compatibility assessment
```

Migration rule:

```text
missing historical info -> UNKNOWN / LEGACY_UNKNOWN
never invent provenance
standalone v0.1 operations remain valid without fabricating a workflow source
```

Materialize schema v0.2 only after cross-document review.

---

## 10. Requirement traceability

Canonical:

`docs/TRACEABILITY_MATRIX.md`

A requirement family is considered incomplete documentation if it lacks:

```text
canonical owner
acceptance direction
evidence/rationale
explicit open/qualification state
```

New acceptance namespaces:

```text
GAUTH-001..040
WFLOW-001..030
NREG-001..030
```

Existing namespaces remain in force (`SCHEMA`, `XACC`, `ARCH`, `HEEL`, `CE`, `OFF`, `MAT`, `MAN`, `BINT`, `RPT`, `PAQ`, etc.).

---

## 11. CI / GitHub Actions technical debt — deferred

Canonical debt register:

`docs/TECHNICAL_DEBT.md`

Item:

```text
TD-CI-001 — GitHub Actions / fixture-validation reliability
STATUS: DEFERRED BY PROJECT OWNER
```

Known state includes 19 fixtures with 3 newer IDs not recognized by the current validator and a workflow pipeline that may mask a validator exit status through `| tee` without explicit `pipefail`.

Current rule:

```text
CI does not block documentation/specification work.
Do not use current green CI as proof that main is fully qualified.
Do not weaken/delete semantic requirements because the harness is behind.
```

Fix later in a dedicated engineering pass using the exit criteria already written in `TECHNICAL_DEBT.md`.

---

## 12. Pressure/device qualification state

Methodology: `spec/15_pressure_acquisition_qualification.md` — frozen.

FM12050/PFM2120:

```text
source/family intake          DONE
bench protocol structure     READY
machine-readable result form READY
real physical-unit qualification  NOT DONE
sensor geometry/conversion   TO QUALIFY
numeric PASS limits          profile/evidence owned
```

This can proceed in parallel when hardware/reference evidence is available.

---

## 13. Research state

Completed:

- EasyCAD2 manual + validation, 25/25 behavioral baseline;
- scan, pressure, offloading, metatarsal, arch, heel, use-case, PROM, material/manufacturing literature;
- first competitor audit;
- second-pass competitor audit including FitFoot360/FIT360, paro360/paroContour, Canfit/Qwadra/Rodin4D, Amfit and newer Sharp Shape signals;
- literature review focused on reproducible CAD authoring, acquisition context, typed placement, pressure-guided design and process-specific qualification.

Do not restart a generic feature survey unless a new gap requires it.

---

## 14. Architecture state — PARKED

Historical architecture documents remain evidence/hypotheses:

```text
spec/03_geometry_operation_model.md
spec/04_base_template.md
spec/05_parametric_orthosis_geometry.md
spec/CAD_ENGINE_CAPABILITY_SPEC.md
spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md
```

For product semantics, `16_geometry_authoring_contract.md` now takes precedence over the old OpenSubdiv-first hypothesis.

The eventual geometry engine must satisfy the contract; the contract must not be rewritten around the engine.

---

## 15. DONE

- [x] Functional v2 canonical.
- [x] Project Schema v0.1 baseline.
- [x] Coordinate/registration v1 frozen.
- [x] BiomechE integration v1 frozen.
- [x] Reporting/traceability v1 frozen.
- [x] Pressure qualification methodology v1 frozen.
- [x] FM12050 family/source intake + bench plan.
- [x] Competitor + scientific evidence baseline and second pass.
- [x] Requirement Traceability Matrix v0.1.
- [x] Geometry Authoring Contract v0.1.
- [x] Workflow/Preset/Macro Contract v0.1.
- [x] Numerical/Tolerance/Qualification Registry v0.1.
- [x] P0 Authoring Acceptance Catalog v0.1.
- [x] Project Schema v0.2 change-set documented.
- [x] README and SPEC_INDEX realigned.
- [x] `TD-CI-001` explicitly recorded and removed from documentation gating.
- [x] Architecture remains parked.

---

## 16. TODO — exact restart point

### NEXT A — cross-document audit and freeze

Audit together:

```text
16_geometry_authoring_contract.md
17_workflow_preset_macro.md
18_numerical_qualification_registry.md
P0_AUTHORING_ACCEPTANCE_CATALOG.md
19_project_schema_v0_2_changeset.md
02_project_schema.md
functional_acceptance_suite.md
```

Resolve duplication/conflicts and promote `16/17/18` to `FROZEN v1` when complete.

### NEXT B — acceptance integration

Update the existing `functional_acceptance_suite.md` to reference `GAUTH`, `WFLOW`, `NREG` and the new catalog without duplicating owning definitions.

### NEXT C — architecture evaluation scorecard

After freeze, derive a geometry-engine scorecard from actual requirements:

```text
semantic replay support
local deformation/authoring primitives
mirror determinism
inspection queries
thickness/production realization
WASM/desktop/server portability
performance
interoperability
numerical reproducibility
implementation complexity
```

Then compare OpenSubdiv vs ON_SubD/alternatives.

### PARALLEL

Real FM12050, material and process qualification when physical evidence is available.

### DEFERRED

`TD-CI-001` — dedicated future CI/validator repair pass.
