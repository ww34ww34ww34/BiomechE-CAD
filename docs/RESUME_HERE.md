# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-15  
**Current phase:** coordinate/registration, BiomechE integration, reporting/traceability and pressure-acquisition qualification methodology are frozen. The kernel-independent fixture suite is running in GitHub Actions and currently passes 16/16 fixtures. **Next: first real Sensor Medica device/protocol qualification + executable BINT/RPT/PAQ expansion.**

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
10. `docs/validation/fixture_validation_report_2026-08-15.md`
11. `docs/DECISIONS.md`
12. `docs/BIBLIOGRAPHY.md`

The v2 functional specification is canonical. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is the preserved historical/audit baseline.

---

## 2. Architecture state — PARKED

Do **not** resume:

```text
OpenSubdiv vs openNURBS / ON_SubD
```

Do not add OCCT, Manifold or another geometry kernel merely for capability coverage.

Current sequence:

```text
FUNCTIONALITY + LITERATURE                     DONE baseline
        ↓
FUNCTIONAL SPEC v2                             DONE / CANONICAL
        ↓
PROJECT SCHEMA v0                              DONE baseline
        ↓
ACCEPTANCE SUITE                               DONE baseline
        ↓
RICH FIXTURES                                  DONE current batch
        ↓
COORDINATE / REGISTRATION                      FROZEN v1
        ↓
BIOMECHE INTEGRATION                           FROZEN v1
        ↓
REPORTING / TRACEABILITY                       FROZEN v1
        ↓
PRESSURE ACQUISITION QUALIFICATION METHOD      FROZEN v1
        ↓
CI PRE-KERNEL VALIDATION                       PASS — 16 fixtures / 0 failures
        ↓
REAL DEVICE / PROTOCOL QUALIFICATION           NEXT
        ↓
BINT / RPT / PAQ EXECUTABLE EXPANSION          PARALLEL
        ↓
COMPETITOR DEEP AUDIT / WORKFLOW AUTOMATION    PARALLEL
        ↓
ARCHITECTURE SHOOT-OUT                         LATER
```

---

## 3. Frozen product/data principles

- EasyCAD2 is behavioral evidence, not scientific truth.
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

## 4. Project Schema / acceptance baseline

Canonical:

```text
docs/spec/02_project_schema.md
schemas/biomeche-cad-project-0.1.schema.json
docs/validation/functional_acceptance_suite.md
```

Schema rules:

```text
native semantic state = authoritative
committed DesignRevision = immutable
raw evidence = immutable/hash-addressed
exact reusable-definition version/hash
physical manufactured copy = own identity
nominal != measured != predicted != service-aged
storage/container/database/kernel = OPEN
```

Acceptance namespaces:

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

`BINT`, `RPT` and `PAQ` semantic definitions live in their owning frozen specs; the exact currently executable subset is recorded in the fixture validation report.

---

## 5. Coordinate / registration freeze

Canonical:

`docs/spec/01_coordinate_registration.md`

Decision:

`D-CAD-023` — FROZEN.

```text
CAD-ANAT-1
right-handed
+X = heel/posterior -> distal/anterior
+Y = subject RIGHT -> subject LEFT
+Z = plantar -> dorsal
X × Y = Z
```

Side semantics:

```text
RIGHT medial = +Y
LEFT  medial = -Y
intrinsic s: heel -> distal
intrinsic q: lateral -> medial
q > 0 = medial on both feet
```

Transform convention:

```text
p_target = T_target_from_source * p_source
T_C_from_A = T_C_from_B * T_B_from_A
```

Matrix row/column order is storage topology only; physical SensorGeometry/frame mapping is explicit.

Real scanner/platform/image/landmark/manufacturing tolerances remain `OPEN` until qualified.

---

## 6. BiomechE integration freeze

Canonical:

`docs/spec/11_biomeche_integration.md`

Decision:

`D-CAD-024` — FROZEN.

Authority split:

```text
BiomechE     = quantitative biomechanical KPI/result authority
BiomechE-CAD = prescription/design/manufacturing/physical-part/outcome/report authority
```

P0 bridge:

```text
whole result bundle
  -> immutable BIOMECHE_RESULT Acquisition + hash/provenance

selected KPI/result
  -> normalized OutcomeMeasurement
```

Every imported result preserves producer/build/commit, result-contract, exam, algorithm/profile/RegionModel versions, units, side/frame, protocol/trial/step/window, quality/reason flags and source acquisition/hash as required by its semantic contract.

Current upstream pin:

```text
ww34ww34ww34/BiomechE
d5e467a1a5551f4280cfef5b483da1999f1566e0
```

At that pin dynamic gait is frozen through `DYN-005`; `DYN-006` dynamic pressure/force/integral/region work remains upstream NEXT. CAD SHALL NOT invent replacement formulas.

---

## 7. Reporting / traceability freeze

Canonical:

`docs/spec/12_reporting_traceability.md`

Decision:

`D-CAD-025` — FROZEN.

```text
Project entities / measurements     authoritative
Report source manifest              exact derivation snapshot
PDF / HTML / charts                 derived presentation
```

Historical report rule:

```text
DesignRevision N -> Report R1
DesignRevision N+1 later
R1 still references N forever
```

Regeneration/reissue creates a new report artifact. Calculations use authoritative full-precision values; display rounding happens only after calculations.

---

## 8. Pressure acquisition qualification freeze

Canonical:

`docs/spec/15_pressure_acquisition_qualification.md`

Methodological baseline:

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

Qualification is exam/outcome-specific. A platform qualified for static load is not automatically qualified for dynamic peak pressure, stabilometry or COP.

Required qualification dimensions include, as applicable:

```text
device/hardware/firmware/software identity
physical sensor geometry
zero/gain/linearity/accuracy
repeatability
hysteresis/creep
saturation/dead cells
force closure
COP performance
timing/jitter/frame loss
protocol/activity/speed/footwear
passes/contacts/steps/window
human repeatability/reproducibility
calibration lifecycle
cross-device policy
```

Numeric acceptance limits remain profile-owned and evidence-backed. `OPEN` cannot become an undocumented implementation constant.

Acceptance family:

```text
PAQ-001..020
```

---

## 9. CI / executable fixture state

Workflow:

`.github/workflows/validate-fixtures.yml`

Harness:

```text
python -m pip install -r requirements-dev.txt
python tools/validate_fixtures.py
```

Canonical run report:

`docs/validation/fixture_validation_report_2026-08-15.md`

Latest qualified run:

```text
commit:    93fdf584881b1f8e24285919b1579ba8cc312fc1
workflow:  Validate project fixtures
run:       31849317559 / run 4
fixtures:  16
failures:  0
```

The suite includes:

```text
5 project fixtures
11 acceptance fixtures
```

and currently executes a subset of `SCHEMA`, `XACC`, `BINT`, `RPT` and `PAQ` checks.

Important: this CI PASS is a schema/semantic pre-kernel result. It is **not** a claim of real hardware accuracy, clinical efficacy, geometry qualification or manufacturing capability.

---

## 10. Literature/evidence added in the integration/qualification phase

Canonical IDs already in `docs/BIBLIOGRAPHY.md`:

```text
REF-CAD-108  Arts & Bus 2011 — protocol/step-count reliability
REF-CAD-109  Giacomozzi 2010 — comparative PMD technical assessment
REF-CAD-110  Giacomozzi 2010 — PMD hardware qualification methods
REF-CAD-111  Sahoo et al. 2011 — biomedical provenance framework
REF-CAD-112  Johns et al. 2023 — biomedical provenance scoping review
REF-CAD-113  Wilkinson et al. 2016 — FAIR provenance/qualified references
```

Existing `REF-CAD-005`, `REF-CAD-034` and `REF-CAD-036` remain central for iterative pressure-guided optimization, device/protocol provenance and cross-device guards.

---

## 11. Competitor first-pass audit

Canonical research file:

`docs/research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md`

Reviewed public-market systems include EasyCAD2, Vertex OrthoCAD, Insolution/OrthoPodoCad, Voxelcare and Sharp Shape AOMS.

Interpretation rule:

```text
NOT EVIDENCED ON REVIEWED PUBLIC SOURCE
!=
PROVEN ABSENT
```

Market table stakes already include scan ingestion, orthosis-specific CAD, corrections/templates and CNC/3D-print output.

BiomechE-CAD differentiation target:

```text
scientific evidence
+ quantitative biomechanics
+ semantic prescription
+ immutable revision
+ manufacturing / physical-part lineage
+ outcome loop
+ reproducible reporting
```

Backlog signals:

```text
GAP-COMP-001  versioned workflow macro/preset orchestration
GAP-COMP-002  external clinical-media adapter
GAP-COMP-003  future cloud/offline synchronization contract
GAP-COMP-004  qualified manufacturing-profile UX breadth
```

---

## 12. DONE

- [x] EasyCAD2 25-story behavioral baseline + validation evidence.
- [x] Scientific/evidence batches through Batch 08.
- [x] Functional Specification v2 canonical.
- [x] Project Schema v0 + JSON Schema reference.
- [x] Kernel-independent Functional Acceptance Suite baseline + `XACC-001..050`.
- [x] Rich project/acceptance fixture batch.
- [x] Coordinate/registration semantic freeze v1 + `D-CAD-023`.
- [x] BiomechE integration semantic freeze v1 + `BINT-001..018` + `D-CAD-024`.
- [x] Reporting/traceability semantic freeze v1 + `RPT-001..018` + `D-CAD-025`.
- [x] BiomechE result-import fixture.
- [x] Historical report-source exactness fixture.
- [x] GitHub Actions fixture-validation workflow.
- [x] First CI-qualified 15-fixture run.
- [x] Pressure acquisition qualification methodological freeze v1 + `PAQ-001..020`.
- [x] Synthetic pressure-qualification fixture proving profile identity, protocol ownership, cross-device guard and `OPEN means OPEN`.
- [x] CI-qualified expanded run: **16 fixtures / 0 failures**.
- [x] Literature/provenance/device-qualification research update.
- [x] First public-source competitor functional-gap audit.
- [x] Architecture still parked.

---

## 13. TODO — exact restart point

### NEXT A — first real Sensor Medica pressure qualification

Identify the exact first physical platform/device to qualify. Capture:

```text
manufacturer/product/model
hardware revision
serial/unit identity
authoritative datasheet/service information
sensor geometry/pitch/represented area
raw->physical conversion
firmware/acquisition software
calibration procedure/reference
```

Then build measured qualification evidence for the intended first use, preferably static load before broader dynamic/stabilometry claims:

```text
zero/drift
scale/linearity/accuracy
repeatability
hysteresis/creep
saturation/dead cells
force closure
COP if intended
sampling/timing if intended
```

Do not convert vendor nominal specifications into achieved qualification results.

### NEXT B — executable acceptance expansion

Add fixtures/checks for:

```text
BINT-011/012  protocol + cross-device compatibility
BINT-015      append-only reanalysis
RPT-014/015   report reissue + semantic reproducibility
PAQ-004/006/007/008/009/012..019
remaining kernel-independent SCHEMA/XACC cases
```

### NEXT C — follow BiomechE upstream `DYN-006+`

When upstream dynamic pressure/force/integral/region semantics freeze:

```text
pin the new BiomechE commit
update the integration source snapshot
map exact KPI IDs/versions
add fixtures/acceptance
```

### PARALLEL

- deepen competitor audit using manuals/trials where legally available;
- specify `GAP-COMP-001` workflow macro/preset orchestration;
- qualify actual material/process profiles and manufacturing tolerances;
- select built-in PROMs only after population/psychometric/licensing review;
- shear only after target hardware is fixed;
- report signing/archive profile only after deployment/legal requirements are known.

### LATER

Only after these gates:

```text
OpenSubdiv vs openNURBS / ON_SubD shoot-out
```

The future engine must pass the already-frozen functional/schema/coordinate/integration/reporting/qualification/acceptance contract. The contract is not rewritten around the winning library.
