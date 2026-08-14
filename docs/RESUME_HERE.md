# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-15  
**Current phase:** coordinate/registration, BiomechE integration and reporting/traceability semantic baselines are frozen; rich fixtures and executable pre-kernel validation are active. Architecture selection remains parked.

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
9. `docs/DECISIONS.md`
10. `docs/BIBLIOGRAPHY.md`

The v2 functional specification is canonical. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is a historical/audit baseline and must be preserved.

---

## 2. Product mission

BiomechE-CAD is an evidence-led CAD/data system for custom foot orthoses integrated with BiomechE:

```text
Acquisition
 -> quantitative biomechanical evidence
 -> indication/context
 -> semantic prescription
 -> immutable DesignRevision
 -> material/manufacturing realization
 -> ManufacturingArtifact
 -> PhysicalOrthosis + QC
 -> wear/service state
 -> measured outcomes + patient experience
 -> compatible comparison / iteration
 -> traceable report
```

EasyCAD2 remains the behavioral benchmark, not scientific truth and not the architectural ceiling.

---

## 3. Architecture state — STILL PARKED

Do **not** resume:

```text
OpenSubdiv vs openNURBS / ON_SubD
```

Do not add OCCT, Manifold or another geometry kernel merely for capability coverage.

Current sequence:

```text
FUNCTIONALITY + LITERATURE                    DONE baseline
        ↓
FUNCTIONAL SPEC v2                            DONE / CANONICAL
        ↓
PROJECT SCHEMA v0                             DONE baseline
        ↓
ACCEPTANCE SUITE                              DONE baseline
        ↓
RICH FIXTURES                                 DONE current batch
        ↓
COORDINATE / REGISTRATION                     FROZEN v1
        ↓
BIOMECHE INTEGRATION                          FROZEN v1
        ↓
REPORTING / TRACEABILITY                      FROZEN v1
        ↓
EXECUTABLE BINT/RPT + REAL QUALIFICATION      NEXT
        ↓
COMPETITOR DEEP AUDIT                         PARALLEL
        ↓
ARCHITECTURE SHOOT-OUT                        LATER
```

---

## 4. Frozen product/data principles

- Dose, placement, units and anatomical reference frame survive as semantic data.
- Final geometry does not erase the prescription.
- A committed `DesignRevision` is immutable; edits create successor revisions.
- Raw acquisition/evidence and imported BiomechE result bundles are immutable/hash-addressed.
- Reusable definitions resolve exact `id + version + hash/snapshot`; never implicit `latest`.
- `DesignRevision`, `ManufacturingArtifact` and `PhysicalOrthosis` have distinct identities.
- `CAD export != manufactured part != accepted part`.
- Nominal material, manufactured/effective property and service-aged property are distinct.
- Pressure is quantitative data; a heatmap is a derived view.
- Offloading = target ROI + safety ring + remote redistribution.
- Arch/heel are multi-parameter prescriptions.
- Geometry dose and material/mechanical dose are separate.
- Scientific thresholds are population/protocol/ROI specific.
- `MeasuredOutcome != PredictedOutcome`.
- PROM, pain/function, comfort, fit, satisfaction and adherence remain separate.
- No hidden universal `BiomechE Score`.

Canonical units:

```text
mm, s, N, kPa, deg, mm²
```

---

## 5. Project Schema v0

Canonical:

```text
docs/spec/02_project_schema.md
schemas/biomeche-cad-project-0.1.schema.json
```

Core rules:

```text
native semantic state = authoritative
committed DesignRevision = immutable
raw evidence = immutable/hash-addressed
exact reusable-definition version/hash
physical manufactured copy = own identity
nominal != measured != predicted != service-aged
storage/container/database/kernel = OPEN
```

Reference conventions:

```text
UUIDv7 preferred
RFC 3339 timestamps
SHA-256 content/asset digest
RFC 8785/JCS where canonical JSON hashing is needed
JSON Schema Draft 2020-12
W3C PROV-compatible Entity/Activity/Agent semantics
FHIR only at interoperability boundary
```

Schema acceptance namespace: `SCHEMA-001..030`.

---

## 6. Rich fixtures / validator

Project fixtures:

```text
fixtures/project/minimal-valid-project.json
fixtures/project/bilateral-project.json
fixtures/project/pressure-design-outcome-loop.json
fixtures/project/manufacturing-qc-lineage.json
fixtures/project/migration-v0.1.json
```

Existing acceptance fixtures:

```text
mirror-semantics.json
registration-known-transform.json
roi-version-comparison.json
profile-non-transfer.json
prom-versioning.json
offload-safety-ring.json
material-property-provenance.json
blocking-qc.json
```

New integration/reporting fixtures:

```text
fixtures/acceptance/biomeche-result-import.json
fixtures/acceptance/report-source-exactness.json
```

Harness:

```text
python -m pip install -r requirements-dev.txt
python tools/validate_fixtures.py
```

The harness validates JSON Schema Draft 2020-12 first and then currently implemented kernel-independent semantic invariants.

**Important:** do not claim a fresh-checkout/CI PASS unless that command has actually run in the target environment. The current chat environment has not provided a direct repository checkout/runtime path for executing the committed harness, so the next implementation/CI pass must retain the real run output.

---

## 7. Coordinate / registration freeze

Canonical:

`docs/spec/01_coordinate_registration.md`

Decision:

`D-CAD-023` — FROZEN.

`CAD-ANAT-1`:

```text
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

## 8. BiomechE integration freeze

Canonical:

`docs/spec/11_biomeche_integration.md`

Decision:

`D-CAD-024` — FROZEN.

Core authority split:

```text
BiomechE
  = quantitative biomechanical KPI/result authority

BiomechE-CAD
  = prescription/design/manufacturing/physical-part/outcome/report authority
```

P0 bridge:

```text
whole result bundle
  -> immutable BIOMECHE_RESULT Acquisition + hash/provenance

selected KPI/result
  -> normalized OutcomeMeasurement
```

Every imported result preserves the semantic identity needed by its contract:

```text
BiomechE product/version/build/commit
result-contract version
exam type
algorithm/profile version
RegionModel/ROI mapping
units
side/frame
protocol/trial/step/window
quality state / reason flags
source acquisition/hash
```

Rules:

- `UNAVAILABLE` is never numeric zero.
- `DEGRADED` cannot be silently upgraded.
- Cross-device/protocol comparisons are gated.
- Reanalysis creates a new result/measurement identity; history is not overwritten.
- CAD does not duplicate a BiomechE KPI formula under the same metric identity.

Current upstream pin:

```text
ww34ww34ww34/BiomechE
d5e467a1a5551f4280cfef5b483da1999f1566e0
```

Upstream status at this pin:

```text
DYN-001 GO
DYN-002 GO
DYN-003 GO structurally
DYN-004 GO structurally
DYN-005 GO
DYN-006 NEXT / not frozen
```

Therefore CAD may bind frozen DYN-001..005 semantics but SHALL NOT invent DYN-006+ dynamic pressure/force/integral/region formulas.

Acceptance family introduced in the integration spec:

```text
BINT-001..018
```

---

## 9. Reporting / traceability freeze

Canonical:

`docs/spec/12_reporting_traceability.md`

Decision:

`D-CAD-025` — FROZEN.

Authority model:

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

Regeneration/reissue creates R2; it never mutates R1.

Significant reports should retain a machine-readable semantic source manifest with exact:

```text
design revision/hash
acquisition/protocol/quality
BiomechE KPI/version
ROI/profile/evidence
material/lot/manufacturing run/artifact/part
QC
outcomes
PROM/comfort/fit/satisfaction/adherence
report generator/build
rounding/display policy
```

Semantic reproducibility is distinguished from byte-identical PDF rendering.

Acceptance family introduced:

```text
RPT-001..018
```

---

## 10. Literature/evidence added in this phase

New evidence focuses on integration validity and provenance rather than geometry:

```text
REF-CAD-108  Arts & Bus 2011 — protocol/step-count reliability
REF-CAD-109  Giacomozzi 2010 — comparative PMD technical assessment
REF-CAD-110  Giacomozzi 2010 — PMD hardware qualification methods
REF-CAD-111  Sahoo et al. 2011 — biomedical provenance framework
REF-CAD-112  Johns et al. 2023 — biomedical provenance scoping review
REF-CAD-113  Wilkinson et al. 2016 — FAIR provenance/qualified references
```

Existing pressure-guided optimization evidence `REF-CAD-005` and cross-device evidence `REF-CAD-036` remain central.

Current upstream integration source:

```text
ARCH-BIOMECHE-INTEGRATION-2026-08-15
```

---

## 11. Competitor first-pass audit

New research file:

`docs/research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md`

Reviewed public-market sources include:

```text
EasyCAD2
Vertex OrthoCAD
Insolution Manager / OrthoPodoCad ecosystem
Voxelcare
Sharp Shape AOMS
```

Important interpretation rule:

```text
NOT EVIDENCED ON REVIEWED PUBLIC SOURCE
!=
PROVEN ABSENT
```

Market table stakes already include scan ingestion, orthosis-specific CAD, corrections/templates and CNC/3D-print output.

BiomechE-CAD differentiation target is therefore:

```text
scientific evidence
+ quantitative biomechanics
+ semantic prescription
+ immutable revision
+ manufacturing / physical-part lineage
+ outcome loop
+ reproducible reporting
```

First real backlog signals from competitor audit:

```text
GAP-COMP-001  versioned workflow macro/preset orchestration
GAP-COMP-002  external clinical-media adapter
GAP-COMP-003  future cloud/offline synchronization contract
GAP-COMP-004  qualified manufacturing-profile UX breadth
```

`GAP-COMP-001` is the most actionable next functional UX item and does not depend on the geometry kernel.

---

## 12. Acceptance namespaces

Existing canonical baseline:

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
```

New domain-contract families:

```text
BINT-001..018
RPT-001..018
```

The next acceptance maintenance pass should merge their summary catalog into `docs/validation/functional_acceptance_suite.md` while preserving the frozen definitions in specs 11/12.

---

## 13. DONE

- [x] EasyCAD2 25-story behavioral baseline + validation evidence.
- [x] Scientific/evidence batches through Batch 08.
- [x] Functional Specification v2 canonical.
- [x] Project Schema v0 + JSON Schema reference.
- [x] `SCHEMA-001..030` semantics.
- [x] Kernel-independent Functional Acceptance Suite baseline + `XACC-001..050`.
- [x] Rich project fixture batch.
- [x] Rich acceptance fixture batch.
- [x] Kernel-independent Python fixture harness started.
- [x] Coordinate/registration semantic freeze v1.
- [x] `D-CAD-023`.
- [x] BiomechE integration semantic freeze v1.
- [x] `BINT-001..018` domain acceptance contract.
- [x] `D-CAD-024`.
- [x] Reporting/traceability semantic freeze v1.
- [x] `RPT-001..018` domain acceptance contract.
- [x] `D-CAD-025`.
- [x] BiomechE result-import acceptance fixture.
- [x] Historical report-source exactness acceptance fixture.
- [x] Validator extended for BiomechE import and report-source semantics.
- [x] Literature/provenance research update.
- [x] First public-source competitor functional-gap audit.
- [x] Architecture still parked.

---

## 14. TODO — exact restart point

### NEXT A — executable validation qualification

1. Run from a real checkout/CI environment:

```text
python -m pip install -r requirements-dev.txt
python tools/validate_fixtures.py
```

2. Persist the result/log.
3. Fix any JSON-Schema/semantic issue found by actual execution before expanding coverage.
4. Add/merge `BINT-*` and `RPT-*` catalog into the canonical acceptance-suite document.
5. Add reanalysis append-only, protocol mismatch, cross-device and report-regeneration fixtures.

### NEXT B — real acquisition/pressure qualification

Define actual product profiles for the target Sensor Medica/BiomechE acquisition systems:

```text
device/model/geometry
calibration identity/procedure
sampling/timestamp behavior
accuracy/repeatability qualification
protocol/activity/speed/footwear
minimum valid trial/step/window policy by exam/profile
cross-device comparison policy
registration tolerance
quality failure/degraded states
```

Do not import literature step counts or device thresholds as universal constants.

### NEXT C — follow BiomechE upstream `DYN-006+`

When upstream freezes dynamic pressure/force/integral/region semantics:

```text
pin new BiomechE commit
update ARCH-BIOMECHE integration bibliography entry or create successor snapshot
map exact new KPI IDs/versions
add fixtures
add acceptance
```

### PARALLEL — competitor/product UX

1. Deepen competitor audit using current manuals/trials where legally available.
2. Specify `GAP-COMP-001` versioned workflow macro/preset orchestration.
3. Specify external clinical-media adapter boundary.
4. Keep cloud/offline synchronization as a future implementation contract, not a reason to choose the geometry kernel now.

### PARALLEL — qualification

- actual material/process profiles and manufacturing tolerances;
- PROM selection/licensing/psychometric qualification;
- shear only after target hardware is fixed;
- report legal signature/archive profile only when deployment requirements are known.

### LATER

Only after these qualification/specification gates:

```text
OpenSubdiv vs openNURBS / ON_SubD shoot-out
```

The future engine must pass the already-frozen product/schema/coordinate/integration/reporting/acceptance contract. The contract is not rewritten around the winning library.
