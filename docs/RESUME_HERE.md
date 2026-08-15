# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-15  
**Current phase:** the product/domain contracts are mature; coordinate/registration, BiomechE integration, reporting/traceability and pressure-acquisition qualification methodology are frozen. The first Sensor Medica family intake and bench protocol are prepared. A second-pass competitor + literature audit is complete. **Immediate work is now canonical-state/CI reconciliation, requirement traceability, Geometry Authoring Contract P0, workflow macro/preset semantics and numerical/qualification registry — not another broad feature survey and not yet the geometry-kernel shoot-out.**

---

## 1. Read these first

Read in this order before making changes:

1. `docs/RESUME_HERE.md`
2. `docs/SPEC_INDEX.md`
3. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
4. `docs/spec/02_project_schema.md`
5. `docs/validation/functional_acceptance_suite.md`
6. `docs/spec/01_coordinate_registration.md`
7. `docs/spec/11_biomeche_integration.md`
8. `docs/spec/12_reporting_traceability.md`
9. `docs/spec/15_pressure_acquisition_qualification.md`
10. `docs/research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md`
11. `docs/research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md`
12. `docs/research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md`
13. `docs/validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md`
14. `docs/validation/fixture_validation_report_2026-08-15.md` — **historical qualified report; see current validation warning below**
15. `docs/DECISIONS.md`
16. `docs/BIBLIOGRAPHY.md`

The v2 functional specification is canonical. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is the preserved historical/audit baseline.

---

## 2. Mission and work order

BiomechE-CAD is a vertical CAD for custom foot orthoses. It must match mature orthotic-CAD workflow capability while preserving stronger scientific, biomechanical and lifecycle semantics.

Current order:

```text
FUNCTIONALITY + EASYCAD2 + SCIENTIFIC EVIDENCE      DONE baseline
        ↓
FUNCTIONAL SPEC v2                                  DONE / CANONICAL
        ↓
PROJECT SCHEMA v0                                   DONE baseline
        ↓
KERNEL-INDEPENDENT ACCEPTANCE SUITE                 DONE baseline
        ↓
COORDINATE / REGISTRATION                           FROZEN v1
        ↓
BIOMECHE INTEGRATION                                FROZEN v1
        ↓
REPORTING / TRACEABILITY                            FROZEN v1
        ↓
PRESSURE ACQUISITION QUALIFICATION METHOD           FROZEN v1
        ↓
FM12050 / PFM2120 SOURCE INTAKE + BENCH PLAN        READY / NOT YET METROLOGICALLY QUALIFIED
        ↓
COMPETITOR + LITERATURE SECOND PASS                 DONE
        ↓
CANONICAL STATE + VALIDATION RECONCILIATION         NEXT / BLOCKING
        ↓
REQUIREMENT TRACEABILITY MATRIX                     NEXT
        ↓
GEOMETRY AUTHORING CONTRACT P0                      NEXT
        ↓
WORKFLOW / PRESET / MACRO CONTRACT                  NEXT
        ↓
NUMERICAL / QUALIFICATION REGISTRY                  NEXT
        ↓
REAL DEVICE / PROCESS QUALIFICATION                 PARALLEL
        ↓
ARCHITECTURE SHOOT-OUT                              LATER
```

Do **not** resume OpenSubdiv vs openNURBS/ON_SubD merely because the product feature inventory is mature. The engine should be judged only after the authoring/numerical contracts produce sufficient fixtures.

---

## 3. Frozen product/data principles

These remain authoritative unless explicitly superseded in `docs/DECISIONS.md`:

- EasyCAD2 is behavioral evidence, not scientific truth.
- BiomechE-CAD is a vertical orthotic CAD, not a generic modeler.
- Dose, placement, units and anatomical reference frame survive as structured semantics.
- Final geometry does not erase prescription intent.
- A committed `DesignRevision` is immutable; edits create successor revisions.
- Raw acquisition/evidence and imported BiomechE result bundles are immutable/hash-addressed.
- Reusable definitions resolve exact `id + version + hash/snapshot`; never implicit `latest`.
- `DesignRevision`, `ManufacturingArtifact` and `PhysicalOrthosis` have distinct identities.
- `CAD export != manufactured part != accepted part`.
- Nominal material, manufactured/effective property and service-aged property are distinct.
- Pressure is quantitative data; a heatmap is a derived view.
- Offloading = target ROI + safety ring + remote redistribution.
- Geometry dose and material/mechanical dose are separate.
- Scientific thresholds are population/protocol/ROI specific.
- `MeasuredOutcome != PredictedOutcome`.
- PROM, pain/function, comfort, fit, satisfaction and adherence remain separate.
- BiomechE is quantitative KPI authority; CAD owns prescription/design/lifecycle semantics.
- `UNAVAILABLE` is never converted to numeric zero.
- Cross-device/protocol pressure comparison is opt-in through an explicit compatibility/qualification policy.
- Reports are immutable derived artifacts over exact historical source entities.
- Pressure-device qualification is intended-use/profile-specific; no universal hidden step-count, resolution or accuracy constant.
- No hidden universal `BiomechE Score`.

Canonical units:

```text
mm, s, N, kPa, deg, mm²
```

---

## 4. Frozen semantic contracts

### Coordinate / registration — `D-CAD-023` FROZEN

Canonical: `docs/spec/01_coordinate_registration.md`.

```text
CAD-ANAT-1
right-handed
+X = heel/posterior -> distal/anterior
+Y = subject RIGHT -> subject LEFT
+Z = plantar -> dorsal
X × Y = Z

RIGHT medial = +Y
LEFT  medial = -Y
intrinsic s: heel -> distal
intrinsic q: lateral -> medial
q > 0 = medial on both feet

p_target = T_target_from_source * p_source
T_C_from_A = T_C_from_B * T_B_from_A
```

Matrix row/column order is storage topology only; physical SensorGeometry/frame mapping is explicit. Real scanner/platform/image/landmark/manufacturing tolerances remain qualification-owned.

### BiomechE integration — `D-CAD-024` FROZEN

Canonical: `docs/spec/11_biomeche_integration.md`.

```text
BiomechE     = quantitative biomechanical KPI/result authority
BiomechE-CAD = prescription/design/manufacturing/physical-part/outcome/report authority
```

Whole BiomechE result bundles remain immutable evidence; selected results normalize into provenance-bearing `OutcomeMeasurement` records. Quality, protocol, device/calibration, ROI/RegionModel, algorithm/profile and producer build/commit semantics survive import.

Current pinned upstream snapshot in the frozen spec:

```text
ww34ww34ww34/BiomechE
d5e467a1a5551f4280cfef5b483da1999f1566e0
```

At that snapshot dynamic gait was frozen through `DYN-005`; CAD must not invent upstream `DYN-006+` formulas.

### Reporting / traceability — `D-CAD-025` FROZEN

Canonical: `docs/spec/12_reporting_traceability.md`.

```text
Project entities / measurements     authoritative
Report source manifest              exact derivation snapshot
PDF / HTML / charts                 derived presentation
```

Reissue creates a new report identity; historical reports remain pinned to historical sources. Calculations use authoritative full precision; display rounding is a presentation policy.

### Pressure acquisition qualification — `D-CAD-026` FROZEN methodology

Canonical: `docs/spec/15_pressure_acquisition_qualification.md`.

```text
intended use
 -> exact device/unit + SensorGeometry
 -> calibration profile
 -> bench evidence
 -> human/protocol evidence where required
 -> versioned acceptance rules
 -> runtime VALID / DEGRADED / UNAVAILABLE
 -> BiomechE KPI provenance
 -> CAD comparison/reporting
```

Qualification is exam/outcome-specific. Vendor nominal values are not achieved metrological performance. Numeric limits stay `OPEN` until a named method and evidence justify them.

---

## 5. Project Schema / acceptance namespaces

Canonical logical contract:

```text
docs/spec/02_project_schema.md
schemas/biomeche-cad-project-0.1.schema.json
docs/validation/functional_acceptance_suite.md
```

Acceptance namespaces currently include:

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

The next consolidation may add workflow/acquisition/geometry inspection cases, but exact IDs must be allocated without colliding with existing namespaces.

---

## 6. Validation truth — IMPORTANT CURRENT WARNING

### Last historical canonical report

`docs/validation/fixture_validation_report_2026-08-15.md` records an earlier qualified state:

```text
16 fixtures
0 failures
commit 93fdf584881b1f8e24285919b1579ba8cc312fc1
run 31849317559 / run 4
```

That report remains valid **for that historical commit**, but it is not the current `main` state.

### Current-main audit finding

Current `main` contains 19 fixtures, including three newer acceptance fixtures:

```text
fixtures/acceptance/biomeche-protocol-cross-device-non-comparable.json
fixtures/acceptance/biomeche-reanalysis-append-only.json
fixtures/acceptance/report-reissue-semantic-reproducibility.json
```

A later specialized validation attempt on commit `334ba4ce6f6d51c23c9f9c8394eca60046d54263` correctly exposed:

```text
Validated fixtures: 19
failures: 3
```

because `tools/validate_fixtures.py` did not recognize those three fixture IDs.

The three intended semantic additions are:

```text
BINT-011 / BINT-012  protocol + cross-device non-comparability
BINT-015             append-only BiomechE reanalysis
RPT-014 / RPT-015    report reissue + semantic reproducibility
```

### False-green CI mechanism discovered by audit

`.github/workflows/validate-fixtures.yml` currently runs:

```bash
python tools/validate_fixtures.py | tee fixture-validation.log
```

without `pipefail`. Therefore a non-zero validator exit can be masked by `tee`, allowing the Actions job to appear successful.

This explains why a later run appeared green even though the current validator/fixture set was inconsistent.

**Until reconciled:** do not claim current-main `19/19 PASS`. The correct state is:

```text
historical qualified checkpoint: 16/16 PASS
current fixture inventory:        19
current strict validation:        16 PASS + 3 FAIL/unknown-fixture
CI propagation bug:               OPEN / BLOCKING
```

Immediate validation repair must:

```text
1. make workflow propagate validator failures (`pipefail` or equivalent)
2. implement the three declared semantic fixture checks
3. rerun strict CI
4. regenerate the canonical fixture validation report with exact commit/run/IDs
5. remove/update temporary one-shot workflows left by failed self-removal
```

This is a documentation/qualification blocker, not a geometry blocker.

---

## 7. First Sensor Medica pressure qualification target

Canonical intake:

`docs/research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md`

Candidate family is already identified:

```text
Sensor Medica FREEMED DYNAMIC 120x50
commercial code PFM2120
production code FM12050
```

The controlled-source intake establishes product-family facts and mode-specific calibration provenance, but **not** a qualified metric SensorGeometry or raw->pressure conversion.

Execution plan:

`docs/validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md`

Machine-readable result template:

`qualification/templates/pressure-bench-result-0.1.json`

The bench protocol defines `BQ-00..BQ-13` for configuration identity, zero/drift, sensor-map verification, scale/linearity, repeatability, hysteresis, creep, saturation, dead/unstable cells, force closure, COP, timing, mode-specific calibration and calibration lifecycle.

Still required for the first real unit:

```text
physical unit serial + hardware/controller/firmware identity
matching current calibration/assembly record
authoritative metric sensor mapping
raw acquisition / raw->physical semantics
selected reference force/load equipment
position reference if COP is qualified
intended first scope — STATIC_LOAD remains recommended first
named acceptance limits/rationale before PASS can exist
```

---

## 8. Competitor + literature audit state

First-pass market audit:

`docs/research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md`

Second-pass expanded market + scientific audit:

`docs/research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md`

Additional systems reviewed in the second pass include:

```text
FitFoot360 / FIT360
paromed paro360 / paroContour
Qwadra Canfit / Rodin4D ecosystem
Amfit Correct & Confirm
current Sharp Shape AOMS updates
current Sensor Medica EasyCAD2/easyCAD Insole pages
```

Interpretation rule remains:

```text
NOT EVIDENCED ON REVIEWED PUBLIC SOURCE
!=
PROVEN ABSENT
```

### Revised market table stakes

The expanded review confirms that mature orthotic CAD/CAM commonly exposes some combination of:

```text
2D/3D acquisition
pressure integration
orthosis-specific named corrections
templates / prescription workflows
reusable histories / presets / macros / saved adjustment knowledge
bilateral/mirror/copy assistance
sections / distances / angles / overlays
local relief/accommodation
upper/lower or clinical/production realization
CNC / 3D-print manufacturing
patient/history/reorder workflow
```

Therefore scan->CAD->STL/CNC alone is not a differentiator.

### GAP-COMP-001 priority changed

Reusable workflow knowledge is now evidenced across multiple systems, not one competitor. Therefore:

```text
GAP-COMP-001
versioned workflow macro/preset orchestration

P0 = semantic infrastructure
P1 = advanced automation / productivity UX
```

P0 means inspectable/versioned/replayable operation groups, not hidden auto-prescription.

Additional product-gap directions introduced by the second pass:

```text
GAP-COMP-005 bilateral authoring / safe operation transfer
GAP-COMP-006 geometry inspection / nominal-vs-measured difference workflow
GAP-COMP-007 top-vs-bottom / shoe-fit manufacturing realization contract
GAP-COMP-008 acquisition-context / landmark-authoring UX
```

---

## 9. Scientific answers now strong enough for the next spec freeze

The second-pass literature supports the following kernel-independent conclusions.

### CAD authoring reproducibility

A 2025 scoping review of digital FO/AFO CAD found major variability and incomplete reporting of authoring procedures. Therefore every meaningful operation must have explicit parameters, references, ordering and version provenance; a final mesh or screenshot is insufficient.

### Weight-bearing state

Recent scanner/design research indicates orthosis design can change materially with weight-bearing condition. Therefore `weightBearingCondition` must be first-class acquisition/design context; NWB/PWB/FWB are not silently interchangeable.

### Landmark provenance

3D-scanning literature shows reliability depends on measured parameter, acquisition method and operator/algorithm. Landmarks therefore preserve source (`manual`, `algorithm-derived`, `device-provided`, `imported`), source acquisition, version/algorithm where applicable and review/quality state.

### Metatarsal-element placement

Published pressure studies use different populations and reference systems and obtain context-specific effective locations. Therefore placement must support explicit reference modes such as:

```text
DISTANCE_FROM_MET_HEAD_LINE_MM
NORMALIZED_FOOT_LENGTH
LANDMARK_RELATIVE
PRESSURE_TARGET_RELATIVE
CUSTOM_REGISTERED_REFERENCE
```

No global “correct” offset is frozen.

### Arch semantics

Arch support is geometry dose + mechanical dose + context + outcome. Height/extent/position, material/mechanical region and redistribution checks remain separate. Higher support is not automatically better.

### Heel semantics

Heel cup/containment, local heel relief/plug, camber, skive/posting and heel mechanical region remain different named operations even if a common low-level deformation primitive implements them.

### Material/mechanical regions

Variable stiffness/density/infill zones are both a current market workflow concept and scientifically compatible with the existing geometry-vs-mechanical-dose separation. Predicted effective property and measured manufactured property remain distinct.

### Pressure-guided iteration

The data architecture must natively support baseline -> design -> physical orthosis -> outcome -> compatibility-gated comparison -> successor design. Automatic optimization is not required for P0; traceable iterative optimization is.

### Manufacturing tolerance

No reviewed literature supports one universal foot-orthosis manufacturing tolerance. A value reported in one AFO/material/process context is not a global CAD rule. Tolerance is owned by qualified `ManufacturingProfile + feature/region + inspection method + reference uncertainty`.

---

## 10. Kernel-independent Geometry Authoring Contract — what can now be frozen

The next spec can freeze these principles before selecting a geometry foundation:

```text
1. Every named correction is a semantic operation, not only mesh displacement.
2. Operation dose/units/reference/extent/side/version survive commit.
3. Scan weight-bearing state survives as design context.
4. Landmark source/provenance/review state survives.
5. Metatarsal placement supports explicit multiple reference modes.
6. Arch geometry dose and mechanical dose remain distinct.
7. Heel cup, heel relief/plug, skive/posting and heel mechanical region remain distinct.
8. Bilateral mirror/copy/transfer is explicit and side-safe.
9. Multi-operation workflow macros/presets are versioned and inspectable.
10. Pressure-guided iteration is a native lifecycle workflow.
11. Nominal CAD geometry and measured manufactured geometry remain distinct and comparable.
12. Clinical/top geometry and lower/shoe/manufacturing realization remain semantically separable.
```

Still OPEN:

```text
exact kernel/math realization
universal arch/heel/pad/skive/posting doses
universal scanner/registration tolerance
universal manufacturing tolerance
universal material hardness/stiffness
universal infill/lattice density
universal pressure reduction target
automatic diagnosis/prescription rule
FE solver/model selection
final cloud/offline runtime
```

---

## 11. DONE

- [x] EasyCAD2 25-story behavioral baseline + validation evidence.
- [x] Scientific/evidence batches through Batch 08.
- [x] Functional Specification v2 canonical.
- [x] Project Schema v0 + JSON Schema reference.
- [x] Kernel-independent Functional Acceptance Suite baseline + `XACC-001..050`.
- [x] Coordinate/registration semantic freeze v1 + `D-CAD-023`.
- [x] BiomechE integration semantic freeze v1 + `BINT-001..018` + `D-CAD-024`.
- [x] Reporting/traceability semantic freeze v1 + `RPT-001..018` + `D-CAD-025`.
- [x] Pressure acquisition qualification methodological freeze v1 + `PAQ-001..020` + `D-CAD-026`.
- [x] Historical 16-fixture strict semantic checkpoint documented as PASS.
- [x] FM12050/PFM2120 controlled-source intake.
- [x] FM12050/PFM2120 `BQ-00..BQ-13` bench protocol draft.
- [x] Machine-readable pressure bench result template.
- [x] First public-source competitor functional-gap audit.
- [x] Expanded second-pass audit across FitFoot360, paromed, Canfit/Qwadra/Rodin4D, Amfit, Sharp Shape and current Sensor Medica material.
- [x] Literature search addressing CAD reproducibility, scanner/weight-bearing context, landmark provenance, met-pad reference semantics and manufacturing-tolerance transferability.
- [x] `GAP-COMP-001` reclassified as P0 semantic infrastructure / P1 advanced automation.
- [x] Current-main validation false-green mechanism identified.
- [x] Architecture remains parked.

---

## 12. TODO — exact restart point

### BLOCKER A — reconcile validation truth

Fix and strictly requalify the 19-fixture current set:

```text
workflow failure propagation (`pipefail` or equivalent)
BINT-011 / BINT-012 validator implementation
BINT-015 validator implementation
RPT-014 / RPT-015 validator implementation
strict rerun
new exact fixture-validation report
cleanup of temporary failed one-shot workflows
```

Do not call current `main` green before this closes.

### NEXT B — Requirement Traceability Matrix

Create one canonical matrix:

```text
Functional requirement
 -> priority
 -> owning spec
 -> evidence/profile
 -> acceptance ID
 -> fixture/HIL/manual protocol
 -> executable status
 -> latest result
 -> blocker
```

This becomes the measurable definition of “how much P0 is actually specified/testable”.

### NEXT C — Geometry Authoring Contract P0

Formalize at least:

```text
template / outline / sizing
thickness / flatten
arch
heel cup / heel relief / camber / skive
rearfoot + forefoot wedge/posting
corrective element / metatarsal element
relief/offload feature
sculpt/manual deformation
scan conform
sections / distances / angles / local height/thickness
bilateral mirror/copy/transfer
nominal-vs-measured geometry inspection
clinical/top vs lower/shoe realization boundary
```

For every operation define semantic parameters, units, anatomical/reference frame, extent/influence, side/mirror behavior, composition/order, versioning, invalid states and acceptance invariants. Do **not** choose the implementation kernel here.

### NEXT D — Workflow / preset / macro contract

Define P0 reusable-workflow semantics:

```text
MacroDefinition id/version/hash
ordered operation expansion
parameter dependencies/defaults
overrides
preview before commit
profile compatibility guard
side/mirror policy
historical immutability
```

Advanced one-click prescription automation remains P1 and must never hide evidence/profile assumptions.

### NEXT E — Numerical / qualification registry

Separate:

```text
computational tolerance
synthetic fixture tolerance
scanner/acquisition tolerance
registration tolerance
manufacturing capability/tolerance
clinical/outcome threshold
```

No number may migrate between these classes without an explicit qualification rationale.

### PARALLEL F — real FM12050 qualification

Select the physical unit and close SensorGeometry/raw-conversion/reference-equipment inputs; execute STATIC_LOAD qualification before broader dynamic/stabilometric claims unless intended-use priority changes.

### PARALLEL G — bibliography promotion

Promote the high-value second-pass research-intake sources into `docs/BIBLIOGRAPHY.md` before the new Geometry Authoring Contract relies on them canonically. Avoid duplicates of existing entries such as `REF-CAD-099`, `REF-CAD-106` and existing vendor entries.

### LATER

Only after the authoring, workflow, numerical and traceability contracts are sufficiently executable:

```text
OpenSubdiv vs openNURBS / ON_SubD shoot-out
```

The winning engine must satisfy the pre-existing product contract; the contract is not rewritten around the engine.

---

## 13. Documentation maintenance rule

`RESUME_HERE.md` is the canonical current-state handover, not a chronological diary. When a later result supersedes a status, update/compact the old statement rather than leaving contradictory “current” claims.

`docs/BIBLIOGRAPHY.md` remains the single authoritative bibliography for canonical claims. Research-intake files may record candidate sources first, but frozen specifications should rely only on promoted stable IDs/locators.

The exact current validation state must always distinguish:

```text
historical PASS at commit X
current fixture inventory
current strict validator result
hardware/process qualification result
```

A schema/fixture PASS is never a claim of geometry accuracy, device metrology, manufacturing capability or clinical efficacy.
