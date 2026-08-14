# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-14  
**Technical phase commit:** `8a708047d1258833c5de515088af3a83c91ef630` — `feat: add rich fixtures and freeze coordinate semantics`  
**Current phase:** rich Project Schema/acceptance fixtures created; kernel-independent validation harness started; coordinate/registration semantics frozen. **Next: BiomechE integration.**

---

## 1. Product mission

BiomechE-CAD is a professional CAD/data system for custom foot orthoses integrated with BiomechE. The product contract is intentionally evidence-led and kernel-independent:

```text
Acquisition
 -> quantitative evidence
 -> indication/context
 -> semantic prescription
 -> immutable DesignRevision
 -> material / manufacturing realization
 -> ManufacturingArtifact
 -> PhysicalOrthosis + QC
 -> wear/service state
 -> measured outcomes + patient experience
 -> compatible comparison / iteration
```

EasyCAD2 remains the behavioral benchmark, not scientific truth and not the architectural ceiling.

---

## 2. Read these first in a new chat

Read in this order before making changes:

1. `docs/RESUME_HERE.md`
2. `docs/SPEC_INDEX.md`
3. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
4. `docs/spec/02_project_schema.md`
5. `docs/validation/functional_acceptance_suite.md`
6. `docs/spec/01_coordinate_registration.md`
7. `docs/DECISIONS.md`
8. `docs/BIBLIOGRAPHY.md`

The v2 functional specification is canonical. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is a historical/audit baseline and must be preserved.

---

## 3. Architecture state — STILL PARKED

Do **not** resume geometry-library selection yet.

Do not reopen:

```text
OpenSubdiv vs openNURBS / ON_SubD
```

and do not add OCCT, Manifold or another geometry kernel merely for capability coverage.

Current sequence:

```text
FUNCTIONALITY + LITERATURE                    DONE baseline
        ↓
FUNCTIONAL SPEC v2                            DONE / CANONICAL
        ↓
PROJECT SCHEMA v0                            DONE baseline
        ↓
ACCEPTANCE SUITE                             DONE baseline
        ↓
RICH FIXTURES                                DONE current batch
        ↓
COORDINATE / REGISTRATION SEMANTICS          FROZEN baseline
        ↓
BIOMECHE INTEGRATION                         NEXT
        ↓
REPORTING / TRACEABILITY                     NEXT
        ↓
COMPETITOR + REAL-WORLD QUALIFICATION        PARALLEL
        ↓
ARCHITECTURE SHOOT-OUT                       LATER
```

---

## 4. Frozen product/data principles

The following remain baseline constraints:

- EasyCAD2 is behavioral evidence, not scientific truth.
- Dose, placement, units and anatomical reference frame survive as semantic data.
- Final geometry must not erase the prescription that produced it.
- A committed `DesignRevision` is immutable; an edit creates a successor revision.
- Raw acquisition/evidence is immutable and hash-addressable.
- Reusable definitions resolve the exact `id + version + hash/snapshot`; never implicit `latest`.
- `PhysicalOrthosis`, `DesignRevision` and `ManufacturingArtifact` have distinct identities.
- `CAD export != manufactured part != accepted part`.
- Nominal material, effective/manufactured property and service-aged property are distinct.
- Pressure is quantitative data; a heatmap is a derived view.
- Offloading means redistribution: `target ROI + safety ring + remote regions`.
- Arch and heel are multi-parameter prescriptions.
- Geometry dose and mechanical/material dose are distinct.
- Scientific thresholds are population/protocol/ROI specific.
- `MeasuredOutcome != PredictedOutcome`.
- PROM, pain, function, comfort, fit, satisfaction and adherence remain distinct.
- No hidden universal `BiomechE Score`.

Canonical physical units remain:

```text
mm, s, N, kPa, deg, mm²
```

---

## 5. Project Schema v0

Canonical specification:

`docs/spec/02_project_schema.md`

Machine-readable reference:

`schemas/biomeche-cad-project-0.1.schema.json`

Reference conventions:

```text
UUIDv7 preferred for new IDs
RFC 3339 timestamps
SHA-256 baseline digest
RFC 8785/JCS where canonical JSON hashing is required
JSON Schema Draft 2020-12 reference serialization
W3C PROV Entity/Activity/Agent-compatible provenance
FHIR only as interoperability adapter, not internal CAD model
```

Schema acceptance namespace:

`SCHEMA-001..SCHEMA-030`

---

## 6. Rich fixture batch — DONE

### Project fixtures

```text
fixtures/project/bilateral-project.json
fixtures/project/pressure-design-outcome-loop.json
fixtures/project/manufacturing-qc-lineage.json
fixtures/project/migration-v0.1.json
```

They are real Project Schema v0 manifests, not illustrative fragments.

Coverage includes:

- bilateral side ownership and semantic mirror lineage;
- pressure pre/post acquisitions with raw assets, matrix/metric/CAD frames, explicit registration, ROI, design and measured outcome comparison;
- design → manufacturing profile/run → artifact → physical orthosis → QC lineage;
- explicit legacy migration provenance without inventing missing prescription history.

### Acceptance fixtures

```text
fixtures/acceptance/mirror-semantics.json
fixtures/acceptance/registration-known-transform.json
fixtures/acceptance/roi-version-comparison.json
fixtures/acceptance/profile-non-transfer.json
fixtures/acceptance/prom-versioning.json
fixtures/acceptance/offload-safety-ring.json
fixtures/acceptance/material-property-provenance.json
fixtures/acceptance/blocking-qc.json
```

Important failure/guard states are represented deliberately, including:

```text
ROI version mismatch -> NOT_COMPARABLE
unconfirmed/non-active profile transfer -> BLOCK
blocking QC failure -> QC_BLOCKED / no acceptedAt
```

The fixtures use `extensions.acceptance` only to describe executable expected behavior; the enclosing document remains a full Project Schema v0 project.

---

## 7. Executable kernel-independent validation — STARTED

Files:

```text
tools/validate_fixtures.py
requirements-dev.txt
```

Run locally/CI with:

```text
python -m pip install -r requirements-dev.txt
python tools/validate_fixtures.py
```

The harness performs:

1. JSON Schema Draft 2020-12 validation;
2. currently implemented kernel-independent semantic checks;
3. fixture-specific `XACC-*` expectations.

Current implemented semantic coverage includes, where applicable:

```text
SCHEMA-001  schema-validation entry point
SCHEMA-002  persistent-ID uniqueness
SCHEMA-003  ownership/case relationships
SCHEMA-005  revision DAG
SCHEMA-006  exact definition id+version+hash resolution
SCHEMA-008  canonical manifest/reference serialization entry point
SCHEMA-010  LEFT/RIGHT consistency
SCHEMA-011  explicit registration frames/direction
SCHEMA-012  ROI identity/reference
SCHEMA-014  outcome→revision linkage
SCHEMA-016  exact PROM definition/version
SCHEMA-017  material-property provenance
SCHEMA-018  design→run→artifact→physical-part lineage
SCHEMA-020  blocking QC gate
SCHEMA-023  migration information-loss state
SCHEMA-026  algorithm/version traceability
SCHEMA-027  provenance output integrity
SCHEMA-029  profile confirmation state
SCHEMA-030  package/reference validation entry point
```

Fixture-specific current XACC coverage:

```text
XACC-003..005  semantic bilateral mirror
XACC-008       known registration transform
XACC-010       ROI version comparison guard
XACC-023..024  profile confirmation/non-transfer
XACC-025       PROM historical versioning
XACC-027       offload target+safety-ring+remote semantics
XACC-031       nominal vs measured material provenance
XACC-034       blocking QC
```

### Validation status / important caveat

During authoring, the 12 rich fixture objects passed the implemented semantic checks: **12/12 PASS**.

The repository now contains the executable JSON-Schema-first harness, but this chat environment could not perform a fresh full checkout execution because the local sandbox could not resolve `github.com`. GitHub also reports no CI/status checks associated with the technical phase commit.

Therefore do **not** overstate the result as a CI-qualified/full-suite pass yet. The immediate environment-level qualification TODO is:

```text
fresh checkout
 -> install requirements-dev.txt
 -> python tools/validate_fixtures.py
 -> record exact output
```

Geometry-dependent acceptance remains intentionally out of scope until actual geometry operators exist.

---

## 8. Coordinate / registration contract — FROZEN semantic baseline

Canonical:

`docs/spec/01_coordinate_registration.md`

Cross-cutting decision:

`D-CAD-023`

### 8.1 Fundamental separation

```text
matrix/index topology
    != physical sensor geometry
    != device/exam coordinates
    != anatomical coordinates
    != CAD coordinates
```

Memory orientation never implies physical/anatomical orientation.

### 8.2 Canonical CAD/anatomical frame

`CAD-ANAT-1` is right-handed and subject-centric:

```text
+X = heel/posterior -> distal/anterior/forefoot
+Y = subject RIGHT -> subject LEFT
+Z = plantar/support side -> dorsal/superior
X × Y = Z
```

LEFT and RIGHT objects use the same right-handed Cartesian convention.

### 8.3 Side and medial/lateral

`side` means patient anatomical side, never screen side, matrix side or inferred coordinate sign.

With canonical `+Y = subject left`:

```text
RIGHT medial = +Y
LEFT  medial = -Y
```

`MEDIAL/LATERAL` therefore remains explicit anatomical semantics.

### 8.4 Intrinsic anatomical coordinates

Frozen side-normalized semantics:

```text
s : 0 heel/posterior -> 1 distal/forefoot
q : -1 lateral -> 0 centre -> +1 medial
```

Both RIGHT and LEFT medial locations have positive `q`.

A semantic mirror changes side and reflects canonical Cartesian `Y`, but preserves the anatomical meaning/numeric value of `s/q`. This supersedes any historical hypothesis implying that semantic mirror must negate `q`.

### 8.5 Pressure mapping

Pressure import preserves independently:

```text
numeric samples in kPa
(row,column) storage topology
physical sensor centres/represented areas in mm
platform/device frame
BiomechE exam frame when available
registration to CAD/anatomical frame
side + protocol + provenance
```

Normal bridge:

```text
(row,column)
 -> explicit sensor geometry
 -> platform metric point
 -> BiomechE/device ExamFrame2D
 -> explicit registration
 -> CAD-ANAT-1
```

A resampled heatmap is never the authoritative metric pressure source.

### 8.6 BiomechE adapter baseline

The current sibling BiomechE contract reviewed for the future adapter explicitly separates matrix topology, physical `SensorGeometry` and exam coordinates. Current `ExamFrame2D` semantics use anterior and subject-left axes; side-aware foot-local transverse semantics are lateral→medial on both feet.

The pinned integration-side snapshot is recorded in the bibliography as:

`ARCH-BIOMECHE-COORD-2026-08-14`

### 8.7 Scan3D landmark frame

Initial anatomical landmark family:

```text
H  = posterior heel/calcaneal landmark
M1 = first metatarsal-head landmark
M5 = fifth metatarsal-head landmark
F  = (M1 + M5) / 2
```

The longitudinal/transverse basis is constructed explicitly and side-aware. A separate dorsal/superior orientation witness is mandatory: three roughly plantar/coplanar landmarks alone do not justify silently choosing the normal that looks correct on screen.

### 8.8 Image2D calibration

Image coordinates begin as pixels `(u,v)`. They become metric only through explicit calibration, using a planar homography or a simpler transform only when acquisition geometry justifies it.

No implicit `mm/pixel` constant.

### 8.9 Transform algebra

Normative persisted convention:

```text
T_target_from_source
p_target = T_target_from_source * p_source
```

Column-vector algebra is normative.

Composition:

```text
T_C_from_A = T_C_from_B * T_B_from_A
```

JSON matrices are serialized as nested row-major textual arrays. This says nothing about C/C++/GPU in-memory layout.

A reflection has determinant `-1` and is not a proper rigid registration.

### 8.10 Tolerances

Semantic identity/direction/side/unit/version requirements are exact.

`registration-known-transform.json` uses `1e-12 mm` only as a synthetic arithmetic tolerance for an analytically known double-precision transform. It is **not** a scanner/platform/device tolerance.

The following real-world tolerances remain explicitly `OPEN` until qualified from actual acquisition/process systems:

```text
pressure sensor physical-position tolerance
platform -> ExamFrame registration error
Scan3D landmark repeatability / registration residual
Image2D calibration error
pressure <-> scan cross-modality registration
manufacturing positioning/dimensional acceptance per process/profile
```

Do not replace `OPEN` with literature-derived generic constants.

---

## 9. Bibliography additions from coordinate freeze

Canonical bibliography now includes:

```text
REF-CAD-107                  H/M1/M5 anatomical COP-registration method
STD-ISB-GLOBAL-CS-1995       ISB global coordinate-system reporting context
STD-ISB-FOOT-KINEMATICS-2021 ISB foot-kinematics recommendation context
ARCH-BIOMECHE-COORD-2026-08-14 pinned sibling BiomechE integration snapshot
```

They support coordinate/landmark/reporting semantics. They do not create universal product tolerances.

---

## 10. Exact restart point — NEXT

### NEXT 1 — `docs/spec/11_biomeche_integration.md`

Freeze the actual integration adapter against the pinned BiomechE contract. At minimum define:

```text
BiomechE exam/acquisition identity
pressure numeric payload ownership
SensorGeometry physical centres/represented areas
ExamFrame2D -> CAD-ANAT-1 transform chain
LEFT/RIGHT ownership
protocol + quality/provenance propagation
raw/derived asset references
pre/post acquisition compatibility
ROI/version compatibility
MeasuredOutcome linkage
which BiomechE algorithms/results are referenced vs recomputed
failure/unresolved registration states
round-trip/import invariants
```

Do not duplicate BiomechE biomechanics inside the CAD layer when a versioned result/reference can be consumed.

### NEXT 2 — `docs/spec/12_reporting_traceability.md`

Define prescription/design/manufacturing/QC/outcome reports with exact revision/evidence provenance and explicit exclusions for predicted vs measured claims.

### Parallel

- competitor functional-gap audit;
- qualify actual pressure/scan/Image2D acquisition systems and their tolerances;
- PROM selection/licensing/psychometric qualification;
- material/process qualification and actual manufacturing acceptance limits;
- expand kernel-independent executable `SCHEMA-* / XACC-*` coverage.

### Later only

Resume the OpenSubdiv vs openNURBS/ON_SubD shoot-out only after the integration/reporting/qualification contract is mature enough to judge candidates with the same fixtures.

---

## 11. DONE

- [x] EasyCAD2 audit and 25/25 behavior coverage.
- [x] Scientific evidence work through material/manufacturing Batch 08.
- [x] Functional + Scientific Evidence Matrix.
- [x] Canonical centralized bibliography with stable IDs/locators.
- [x] Use-case/indication profiles.
- [x] Functional Specification v2 canonical.
- [x] Project Schema v0 canonical baseline.
- [x] JSON Schema Draft 2020-12 reference schema.
- [x] Minimal project fixture.
- [x] Kernel-independent Functional Acceptance Suite v0.
- [x] `SCHEMA-001..030` semantics.
- [x] `XACC-001..050` acceptance scenarios.
- [x] Four requested rich Project Schema fixtures.
- [x] Eight requested rich acceptance fixtures.
- [x] Failure-state fixtures for ROI incompatibility, profile non-transfer and blocking QC.
- [x] Kernel-independent Python validation harness added.
- [x] 12/12 rich fixtures passed implemented in-authoring semantic checks.
- [x] `docs/spec/01_coordinate_registration.md` semantic baseline frozen.
- [x] Canonical right-handed `CAD-ANAT-1` axes and side semantics frozen.
- [x] Side-normalized `s/q` semantics frozen.
- [x] Matrix topology vs physical sensor geometry separation frozen.
- [x] Source→target transform/vector/composition/serialization convention frozen.
- [x] Semantic mirror separated from rigid registration.
- [x] Real-world tolerances left explicitly `OPEN` rather than invented.
- [x] Coordinate/registration bibliography sources added.
- [x] BiomechE coordinate/acquisition snapshot pinned as architecture/integration reference.
- [x] `D-CAD-023` recorded.
- [x] `docs/SPEC_INDEX.md` advanced to BiomechE integration as NEXT.
- [x] Architecture remains parked; no new geometry kernel added.

## 12. TODO

- [ ] Run `python tools/validate_fixtures.py` from a fresh accessible checkout/CI and record exact JSON-Schema + semantic output.
- [ ] Add CI wiring for fixture validation if/when repository CI policy permits.
- [ ] Expand executable coverage for remaining geometry-independent `SCHEMA-* / XACC-*` cases.
- [ ] Add later fixtures for `section-height`, `ruler-known-distance`, `min-thickness-dfm` when their executable semantics are ready.
- [ ] Create/freeze `docs/spec/11_biomeche_integration.md` — **NEXT**.
- [ ] Create/freeze `docs/spec/12_reporting_traceability.md`.
- [ ] Qualify actual pressure platform/device geometry and registration tolerances.
- [ ] Qualify selected Scan3D landmark repeatability/registration.
- [ ] Qualify selected Image2D calibration path.
- [ ] Expand shear/COP only after target hardware/protocol is fixed.
- [ ] Competitor functional-gap audit in parallel.
- [ ] Select built-in PROMs after profile fit, psychometric and licensing review.
- [ ] Qualify real materials/processes and product-specific QC limits.
- [ ] Progressively migrate historical docs when touched, without destroying audit history.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD architecture shoot-out.
