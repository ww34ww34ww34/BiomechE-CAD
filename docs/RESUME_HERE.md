# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-15  
**Current phase:** product/domain discovery is mature. The project has moved into **P0 authoring-contract formalization**: requirement traceability exists; geometry-authoring, workflow/macro and numerical-governance contracts have been materialized as canonical drafts. GitHub Actions/fixture-validation reliability is explicitly deferred as `TD-CI-001` and is **not a documentation gate**.

---

## 1. Read these first

Read in this order:

1. `docs/RESUME_HERE.md`
2. `docs/SPEC_INDEX.md`
3. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
4. `docs/TRACEABILITY_MATRIX.md`
5. `docs/spec/02_project_schema.md`
6. `docs/spec/01_coordinate_registration.md`
7. `docs/spec/16_geometry_authoring_contract.md`
8. `docs/spec/17_workflow_preset_macro.md`
9. `docs/spec/18_numerical_qualification_registry.md`
10. `docs/spec/11_biomeche_integration.md`
11. `docs/spec/12_reporting_traceability.md`
12. `docs/spec/15_pressure_acquisition_qualification.md`
13. `docs/research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md`
14. `docs/TECHNICAL_DEBT.md`
15. `docs/DECISIONS.md`
16. `docs/BIBLIOGRAPHY.md`

The functional authority is `BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`. The old `BIOMECHE_CAD_FUNCTIONAL_SPEC.md` remains historical/audit evidence.

---

## 2. Mission

BiomechE-CAD is a vertical CAD for custom foot orthoses. It must match mature orthotic-CAD authoring productivity while providing stronger scientific and lifecycle semantics:

```text
EVIDENCE
+ ACQUISITION PROVENANCE
+ SEMANTIC PRESCRIPTION
+ REPRODUCIBLE AUTHORING
+ QUANTITATIVE BIOMECHANICS
+ IMMUTABLE DESIGN REVISION
+ MATERIAL / MANUFACTURING LINEAGE
+ PHYSICAL-PART IDENTITY
+ OUTCOME LOOP
+ REPRODUCIBLE REPORTING
```

The product is not a generic CAD and must not be redesigned around whichever geometry library eventually wins.

---

## 3. Current work order

```text
FUNCTIONALITY + EASYCAD2 + SCIENTIFIC EVIDENCE       DONE baseline
        ↓
FUNCTIONAL SPEC v2                                   CANONICAL
        ↓
PROJECT SCHEMA / PROVENANCE                          ACTIVE baseline
        ↓
COORDINATE / REGISTRATION                            FROZEN v1
        ↓
BIOMECHE INTEGRATION                                 FROZEN v1
        ↓
REPORTING / TRACEABILITY                             FROZEN v1
        ↓
PRESSURE ACQUISITION QUALIFICATION METHOD            FROZEN v1
        ↓
COMPETITOR + LITERATURE SECOND PASS                  DONE
        ↓
REQUIREMENT TRACEABILITY MATRIX                      DONE v0.1
        ↓
GEOMETRY AUTHORING CONTRACT                          CANONICAL DRAFT v0.1
        ↓
WORKFLOW / PRESET / MACRO CONTRACT                   CANONICAL DRAFT v0.1
        ↓
NUMERICAL / TOLERANCE / QUALIFICATION REGISTRY      CANONICAL DRAFT v0.1
        ↓
DOCUMENT REVIEW + FREEZE OF THESE THREE CONTRACTS    NEXT
        ↓
REPRESENTATIVE GEOMETRY ACCEPTANCE / FIXTURE SPECS   NEXT
        ↓
SCHEMA v0.2 CHANGESET DOCUMENTATION                  NEXT
        ↓
REAL DEVICE / MATERIAL / PROCESS QUALIFICATION       PARALLEL
        ↓
GEOMETRY ENGINE SHOOT-OUT                            LATER
```

OpenSubdiv vs openNURBS/ON_SubD remains intentionally parked.

---

## 4. Frozen principles

The following remain authoritative:

- EasyCAD2 is behavioral evidence, not scientific truth.
- BiomechE-CAD is orthosis-specific, not generic freeform CAD.
- A committed `DesignRevision` is immutable.
- Semantic prescription survives final geometry.
- Dose, units, placement, side and anatomical reference are structured data.
- Raw acquisitions and imported result bundles remain immutable/hash-addressed evidence.
- Exact reusable definitions use `id + version + hash/snapshot`; never implicit `latest`.
- Geometry dose and material/mechanical dose are separate.
- Pressure is quantitative; a heatmap is a derived view.
- Offloading = target ROI + safety ring + remote redistribution.
- Scientific thresholds are population/protocol/ROI specific.
- `MeasuredOutcome != PredictedOutcome`.
- `UNAVAILABLE` is never converted to zero.
- BiomechE is quantitative KPI authority; CAD owns prescription/design/lifecycle semantics.
- `DesignRevision != ManufacturingArtifact != PhysicalOrthosis`.
- CAD nominal geometry != measured manufactured geometry.
- Reports are immutable derived artifacts over exact source entities.
- Device/manufacturing qualification is intended-use/profile-specific.
- Unknown numerical limits remain `OPEN`.

Canonical physical units remain:

```text
mm, s, N, kPa, deg, mm²
```

---

## 5. New P0 authoring conclusions

### 5.1 Capture context

A scan that influences geometry preserves acquisition context. Weight-bearing state is first-class when known:

```text
NON_WEIGHT_BEARING
PARTIAL_WEIGHT_BEARING
FULL_WEIGHT_BEARING
OTHER_NAMED
UNKNOWN
```

`UNKNOWN` is valid; silent inference is not.

### 5.2 Landmark provenance

A design-significant landmark preserves point + frame + side + source acquisition + source method + author/algorithm + quality/review state.

### 5.3 Placement is typed

P0 placement modes include:

```text
INTRINSIC_SQ
LANDMARK_RELATIVE_MM
LANDMARK_LINE_RELATIVE_MM
NORMALIZED_FOOT_LENGTH
ROI_RELATIVE
PRESSURE_TARGET_RELATIVE
CUSTOM_REGISTERED_REFERENCE
```

This prevents study-specific placement rules from being collapsed into one universal coordinate.

### 5.4 Orthosis-specific operations remain semantic concepts

P0 authoring must distinguish at least:

```text
template/outline/sizing
medial/lateral arch
heel cup / relief / camber / medial heel skive / mechanical heel region
rearfoot / forefoot wedge
corrective element
offload feature
sculpt
scan conform
height/thickness/DFM constraints
```

Several operations may share low-level geometry primitives later; their domain meaning must remain distinct.

### 5.5 Inspection is P0

Sections, distance, height, angle, thickness and deviation-map results preserve the exact source revision, geometric definition, frame/method and algorithm version.

### 5.6 Clinical surface vs production realization

Keep logically separate:

```text
clinical/contact-surface intent
thickness field
lower/shoe-facing surface rule
sidewall/closure rule
manufacturing profile
```

No specific mesh/SubD/BRep representation is frozen by this decision.

---

## 6. Workflow/macro conclusion

Expanded competitor research changed `GAP-COMP-001` priority:

```text
P0  semantic infrastructure
P1  advanced automation / authoring UX
```

The market repeatedly exposes reusable design knowledge through macros, histories, profiles, templates and saved adjustments.

BiomechE-CAD therefore defines:

```text
PresetDefinition        one operation/family
WorkflowDefinition      ordered multi-step reusable knowledge
WorkflowApplication     project-owned exact expansion
```

P0 rules:

- exact version/hash;
- deterministic semantic expansion;
- committed child operations survive independently of library availability;
- typed inputs;
- defaults classified by numerical authority;
- manual overrides explicit;
- dependencies explicit;
- mirror policy explicit;
- incompatible context is not silently coerced;
- suggestion != user confirmation;
- later library edits cannot rewrite historical revisions.

---

## 7. Numerical/tolerance doctrine

All product-significant numbers belong to a named authority class:

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

Every governed rule has:

```text
ruleId + version
status: OPEN / PROVISIONAL / QUALIFIED / FROZEN_CONVENTION / DEPRECATED
value/range/function + unit
scope/applicability
owner spec/profile
rationale/evidence/method
```

Important consequences:

- study dose != universal product default;
- display precision != computational precision != acceptance tolerance;
- geometry replay epsilon != manufacturing tolerance;
- landmark uncertainty != registration tolerance != manufacturing tolerance;
- no universal `CAD_TOLERANCE`;
- missing manufacturing/device limits remain `OPEN` rather than falling back to UI defaults.

---

## 8. Requirement traceability baseline

Canonical:

`docs/TRACEABILITY_MATRIX.md`

It maps the major families:

```text
product scope
project schema/provenance
coordinate/registration
scan/capture context
landmarks
base template
arch/heel/wedge/corrective elements
offloading/sculpt/scan conform
inspection/thickness/DFM
materials/manufacturing/physical part
workflow/preset/macro
BiomechE/pressure/outcome loop
PROM/reporting
architecture
```

into:

```text
priority/status
canonical owner
acceptance family
evidence/rationale
current open gap
```

A requirement without an owner and acceptance direction is now considered documentation debt.

---

## 9. Acceptance namespaces

Existing:

```text
SCHEMA-001..030
OFF-001..009
CE-001..010
ARCH-001..014
HEEL-001..015
PROF-001..012
PROM-001..020
MAT-001..018
MAN-001..018
XACC-001..050
BINT-001..018
RPT-001..018
PAQ-001..020
```

New authoring-phase families:

```text
GAUTH-001..040   Geometry Authoring Contract
WFLOW-001..030   Workflow/Preset/Macro Contract
NREG-001..030    Numerical/Qualification Registry
```

Executable CI coverage is currently not the documentation gate; see technical debt below.

---

## 10. CI / GitHub Actions technical debt — explicitly deferred

Canonical debt register:

`docs/TECHNICAL_DEBT.md`

Current item:

```text
TD-CI-001
GitHub Actions / fixture-validation reliability
STATUS: DEFERRED BY PROJECT OWNER
```

Known issues include:

```text
19 current fixtures
3 newer fixture IDs unknown to current validator
pipeline may mask validator exit code through `| tee` without explicit pipefail
historical 16/16 PASS applies only to its historical commit
```

Project-owner rule as of this checkpoint:

```text
DO NOT let GitHub CI block documentation/specification work.
DO NOT use current CI green state as proof of qualification.
DO NOT weaken/delete semantic requirements because the harness is behind.
```

Exit criteria for the debt are documented in `TECHNICAL_DEBT.md` and will be handled in a later dedicated engineering pass.

---

## 11. Pressure/device qualification state

Methodology remains frozen in:

`docs/spec/15_pressure_acquisition_qualification.md`

FM12050/PFM2120 source intake exists:

`docs/research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md`

Bench protocol exists:

`docs/validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md`

Machine-readable result template exists:

`qualification/templates/pressure-bench-result-0.1.json`

Current truth:

```text
family/model intake          DONE
bench test structure         READY
metrological qualification  NOT DONE
exact first physical unit    STILL REQUIRED
sensor geometry/conversion   STILL TO QUALIFY
numeric PASS limits          remain profile/evidence owned
```

This can continue in parallel when real hardware/reference evidence is available.

---

## 12. Scientific/market evidence state

Completed research includes:

- EasyCAD2 manual + validation baseline, 25/25 user stories;
- pressure/scan/offloading/metatarsal/arch/heel evidence batches;
- use-case profile boundaries;
- PROM/comfort/adherence evidence;
- material/manufacturing evidence;
- competitor baseline: EasyCAD2, OrthoCAD, Insolution, Voxelcare, Sharp Shape;
- second-pass competitor expansion: FitFoot360/FIT360, paro360/paroContour, Canfit/Qwadra/Rodin4D, Amfit and newer Sharp Shape workflow signals;
- literature answers supporting acquisition-context provenance, reproducible CAD authoring, typed placement, separation of geometry/mechanics and profile-owned manufacturing/device thresholds.

Do not restart a generic competitor-feature survey unless a new gap requires it.

---

## 13. Architecture state — PARKED

Do not select a geometry engine yet.

Historical architecture documents remain useful evidence/hypotheses, especially:

```text
spec/03_geometry_operation_model.md
spec/04_base_template.md
spec/05_parametric_orthosis_geometry.md
spec/CAD_ENGINE_CAPABILITY_SPEC.md
spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md
```

But current product/domain authority is now `16_geometry_authoring_contract.md`.

The future engine must pass the contract; the contract is not rewritten around the engine.

---

## 14. DONE

- [x] EasyCAD2 25-story behavioral baseline.
- [x] Functional/scientific evidence batches through material/manufacturing.
- [x] Functional Specification v2 canonical.
- [x] Project Schema v0 baseline.
- [x] Coordinate/registration frozen v1.
- [x] BiomechE integration frozen v1.
- [x] Reporting/traceability frozen v1.
- [x] Pressure-acquisition qualification methodology frozen v1.
- [x] FM12050/PFM2120 source intake + bench-protocol structure.
- [x] First competitor functional-gap audit.
- [x] Second-pass competitor + literature audit.
- [x] Requirement Traceability Matrix v0.1.
- [x] Geometry Authoring Contract v0.1 created.
- [x] Workflow/Preset/Macro Contract v0.1 created.
- [x] Numerical/Tolerance/Qualification Registry v0.1 created.
- [x] README corrected to point to Functional Spec v2.
- [x] `SPEC_INDEX.md` realigned to current authoring phase.
- [x] CI problem recorded as `TD-CI-001` and explicitly removed from documentation gating.
- [x] Architecture still parked.

---

## 15. TODO — exact restart point

### NEXT A — documentation review/freeze

Review the three new canonical drafts as a single P0 authoring package:

```text
spec/16_geometry_authoring_contract.md
spec/17_workflow_preset_macro.md
spec/18_numerical_qualification_registry.md
```

Goal: move each from `CANONICAL DRAFT FOR FREEZE v0.1` to `FROZEN v1` after checking coverage and cross-document consistency.

### NEXT B — representative geometry acceptance scenarios

Specify architecture-independent cases for at least:

```text
arch dose + placement
heel semantic decomposition
rear/forefoot wedge direction/pivot
met-pad landmark-relative vs normalized placement
corrective element
pressure-target offload
sculpt replay
scan conform
right->left mirror
section/distance/angle
thickness method
CAD-vs-measured deviation map
requested-vs-constrained realized dose
workflow expansion + override
numerical-rule resolution / OPEN behavior
```

These can be fixture **specifications** even while GitHub CI is deferred.

### NEXT C — Project Schema v0.2 change-set documentation

Define, without immediately migrating JSON/schema fixtures:

```text
richer ScanAcquisition capture context
richer Landmark provenance/review state
workflowDefinitions[]
WorkflowApplication
sourceWorkflowRef
parameter override records
numerical rule references
```

The change set must include migration/backward-compatibility rules before materializing schema v0.2.

### PARALLEL

- qualify the first physical FM12050 unit when hardware/reference data are available;
- qualify actual material/process/manufacturing profiles;
- follow BiomechE upstream dynamic pressure/region semantics after freeze;
- select built-in PROMs only after exact version/language/licensing review.

### DEFERRED

`TD-CI-001` — repair GitHub Actions/validator in a dedicated engineering pass. It is intentionally **not** the current task.

### LATER

Only after the authoring contracts + representative geometry acceptance are mature:

```text
OpenSubdiv vs openNURBS/ON_SubD architecture shoot-out
```
