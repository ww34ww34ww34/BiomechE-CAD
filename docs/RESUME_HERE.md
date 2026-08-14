# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint:** 2026-08-14 — architecture selection remains parked. Functional/scientific research is complete through **Batch 08 — material durability + manufacturing**. Active formal specs now include corrective elements, material/stiffness, analysis/QC, manufacturing, use-case profiles and PROM/comfort/adherence. Canonical bibliography extends through `REF-CAD-106` plus `STD-*` test/manufacturing standards.

---

## 1. Product goal

Professional CAD for custom foot orthoses integrated with BiomechE:

```text
Acquisition
 -> quantitative evidence
 -> indication/context
 -> prescription
 -> design revision
 -> material / manufacturing realization
 -> physical artifact + QC
 -> wear exposure / service state
 -> outcome measurement
 -> comparison / iteration
```

EasyCAD2 remains the detailed behavioral benchmark, not scientific truth or the architectural ceiling.

---

## 2. Evidence governance

`docs/BIBLIOGRAPHY.md` is the single bibliographic authority.

Namespaces:

```text
EC2-*
GUIDE-*
REF-CAD-*
STD-*
VENDOR-*
ARCH-*
```

Cite exact truthful locators. Never invent pages.

Standards entries document official scope/test/qualification semantics. They **do not imply full standard conformance** unless a controlled copy has been reviewed and a formal applicability/conformance decision is recorded.

---

## 3. Current work order

```text
EasyCAD2 behavior
+ literature
+ dose / placement / reference frame
+ population / indication context
+ measurable outcomes
+ material / process / actual artifact state
+ acceptance semantics
        ↓
CONSOLIDATED FUNCTIONAL SPEC
        ↓
PROJECT SCHEMA v0
        ↓
KERNEL-INDEPENDENT ACCEPTANCE SUITE
        ↓
ARCHITECTURE SHOOT-OUT LATER
```

Do **not** resume OpenSubdiv vs ON_SubD yet.

---

## 4. Completed functional/scientific blocks

### EasyCAD2 baseline

- primary manual + validation plan/report indexed;
- 25/25 validation stories PASS;
- DIMA, pressure, Scan3D/2D, heel, arch, wedge, corrective elements, stiffness regions, sculpt, scan conform, sections/QC, manufacturing/export and history preserved as behavioral baseline.

### Batch 03 — relief/offloading

```text
TARGET ROI
+ SAFETY RING
+ REMOTE REGIONS
```

Offloading is redistribution, not disappearance of load. `OFF-001..OFF-009` defined.

### `spec/06_corrective_elements.md`

Named anatomical elements, landmark-relative metatarsal placement, evidence-linked presets, `CE-001..CE-010`.

### Batch 04 — arch

Arch is:

```text
GEOMETRY DOSE
+ MECHANICAL DOSE
+ CONTEXT
+ OUTCOME
```

No universal optimal arch; `ARCH-001..ARCH-014`.

### Batch 05 — heel

Heel separates:

```text
HeelCup
HeelRelief
HeelMechanicalRegion
HeelCamber
```

No universal adult cup-height rule; `HEEL-001..HEEL-015`.

### Batch 06 + `spec/13_use_case_profiles.md`

Initial P0 profiles:

```text
DIABETIC_REULCERATION_PREVENTION
MECHANICAL_METATARSALGIA
FLEXIBLE_FLATFOOT
PLANTAR_HEEL_PAIN
SPORT_PERFORMANCE
GENERIC_CUSTOM_ORTHOSIS
```

Profiles are versioned evidence contexts, not diagnosis engines or hidden prescription generators. Active diabetic plantar ulcer is a separate guideline pathway rather than a recurrence-prevention insole preset. `PROF-001..PROF-012`.

### Batch 07 + `spec/14_prom_comfort_adherence.md`

Separate outcome constructs:

```text
pain
function
foot-specific health/QoL
comfort
fit/usability
satisfaction
adherence/wear exposure
```

No hidden universal `BiomechE Score`.

PROM identity preserves exact version/language/scoring algorithm; MID/MCID/MDC/SEM remain instrument/domain/population/context-specific. Objective vs subjective adherence and denominators remain distinct. `PROM-001..PROM-020`.

### Batch 08 — `MAT-001 / MAN-001`

Research:
`docs/research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md`

Formal specs:
- `docs/spec/08_material_stiffness.md`
- `docs/spec/10_manufacturing.md`

Central rule:

```text
NOMINAL MATERIAL
!=
MANUFACTURED EFFECTIVE PROPERTY
!=
SERVICE-AGED PROPERTY
```

Material/manufacturing provenance now separates:

```text
MaterialDefinition
MaterialLot / feedstock
MaterialRegion
MaterialStack + interfaces
Structural/Lattice effective response
ManufacturingProfile
ManufacturingRun
PostProcessStep
ManufacturingArtifact
PhysicalOrthosis
QCRequirement / QCMeasurement
ManufacturedPropertyState
ServiceState
```

Important semantics:

- hardness requires value + scale + method; bare `50 Shore` is invalid;
- Shore hardness is not silently converted to Young/effective modulus;
- density, thickness, material-stack order and interfaces are explicit;
- base material and lattice/infill effective stiffness are separate;
- heat/thermoforming/curing/lamination are property-changing manufacturing provenance;
- cyclic durability, compression set and service aging are separate from initial properties;
- visual compression is not a universal replacement criterion;
- AM feedstock, orientation/position, infill/lattice/process parameters and post-processing are versioned where applicable;
- CNC blank/material, lot, tooling, fixture/CAM/postprocessor and finishing are versioned where applicable;
- CAD nominal geometry and measured manufactured geometry are separate;
- export success does not imply accepted part;
- qualified manufacturing profiles can define blocking QC;
- no universal orthosis lifetime or process tolerance is hardcoded from generic literature/standards.

Acceptance semantics:

```text
MAT-001..MAT-018
MAN-001..MAN-018
```

Bibliography additions:

```text
REF-CAD-094..REF-CAD-106
STD-ISO-868-2003
STD-ISO-1856-2018
STD-ISO-3385-2014
STD-ISO-24999-2008
STD-ISO-3386-1-2025
STD-ISOASTM-52901-2017
STD-ISOASTM-52902-2023
STD-ISOASTM-52903-1-2020
STD-ISOASTM-52920-2023
STD-ISOASTM-52924-2023
STD-ISO-17295-2023
```

`D-CAD-020` records the separation between material identity, process, measured final-part properties and service state.

---

## 5. Current evidence-led domain model

```text
Patient / Case
IndicationProfile[]
activeInterpretationProfile

Acquisition
ScanAcquisition
PressureAcquisition

Prescription
ArchSupportPrescription
HeelPrescription
CorrectiveElement
OffloadFeature
MaterialRegion
MaterialStack
StructuralMaterialRegion

OutcomeTarget
ProfileTarget
OutcomeMeasurement
OffloadAssessment

PROMInstrumentDefinition
PROMMeasurement
ComfortAssessment
FitUsabilityAssessment
SatisfactionAssessment
AdherenceMeasurement
PatientExperienceBundle
InterpretationRule

MaterialDefinition
MaterialLot
MechanicalPropertyMeasurement
PostProcessMaterialState
DurabilityTest
ServiceState

DesignRevision
ManufacturingProfile
ManufacturingRun
ManufacturingArtifact
PhysicalOrthosis
QCRequirement
QCMeasurement
ManufacturedGeometryMeasurement
MetricThreshold
```

This model is still schema-level/domain-level and independent of geometry-kernel choice.

---

## 6. Architecture state — PARKED

Later comparison remains:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

Prefer one P0 SubD foundation. No major geometry dependency enters merely for theoretical capability coverage.

---

## 7. Exact restart point

### NEXT — consolidate the functional specification

Update:

`docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md`

Promote mature requirements from Batches 03–08 and active specs without duplicating evidence metadata.

The consolidated spec must include/reconcile:

```text
1. offloading / safety-ring semantics
2. corrective-element anatomical placement
3. arch geometry/mechanics/context/outcome model
4. heel containment/relief/cushioning split
5. indication-profile/context layer
6. pressure metric/protocol/comparability policy
7. PROM/comfort/fit/adherence model
8. material identity/lot/stack/region/effective-property model
9. manufacturing profile/run/artifact/QC/service-state model
10. final P0/P1/P2 priorities
11. links to bibliography IDs, detailed subordinate specs and acceptance IDs
```

Do **not** copy all research prose into the main spec; promote normative requirements and point to the research/evidence documents.

### AFTER CONSOLIDATION

```text
2. Create `spec/02_project_schema.md` v0
   from the now-mature domain entities.

3. Create kernel-independent functional acceptance suite
   covering OFF / CE / ARCH / HEEL / PROF / PROM / MAT / MAN.

4. Freeze `spec/01_coordinate_registration.md`
   before geometry implementation because schema/measurements require exact frames.

5. Define `spec/11_biomeche_integration.md`
   and `spec/12_reporting_traceability.md`.

6. Competitor functional-gap audit may proceed in parallel.

7. Select built-in PROMs only after fit + psychometric + licensing review.

8. Qualify actual production material/process profiles separately.

9. Only then resume architecture shoot-out.
```

---

## 8. DONE

- [x] EasyCAD2 primary behavior + 25-story baseline.
- [x] Functionality-first/science-first work mode.
- [x] Canonical bibliography/provenance governance.
- [x] Quantitative pressure/protocol policy.
- [x] Relief/offloading Batch 03 + `OFF-*`.
- [x] Corrective-elements spec + `CE-*`.
- [x] Arch Batch 04 + `ARCH-*`.
- [x] Heel Batch 05 + `HEEL-*`.
- [x] Use-case/population Batch 06 + `spec/13` + `PROF-*`.
- [x] Diabetic active-ulcer pathway guard.
- [x] PROM/comfort/fit/adherence Batch 07 + `spec/14` + `PROM-*`.
- [x] Material/manufacturing Batch 08.
- [x] `spec/08_material_stiffness.md` v0.
- [x] `spec/10_manufacturing.md` v0.
- [x] `MAT-001..018` defined.
- [x] `MAN-001..018` defined.
- [x] Bibliography expanded through `REF-CAD-106` and material/AM standards.
- [x] `D-CAD-020` material/process/artifact/service-state decision.
- [x] `SPEC_INDEX.md` updated through Batch 08.

## 9. TODO

- [ ] **Promote Batch 03–08 into consolidated `BIOMECHE_CAD_FUNCTIONAL_SPEC.md` — NEXT.**
- [ ] `spec/02_project_schema.md` v0.
- [ ] Kernel-independent acceptance suite.
- [ ] `spec/01_coordinate_registration.md` freeze before implementation.
- [ ] `spec/11_biomeche_integration.md`.
- [ ] `spec/12_reporting_traceability.md`.
- [ ] Expand shear/COP when target hardware is fixed.
- [ ] Competitor feature-gap audit in parallel.
- [ ] Built-in PROM selection after licensing/psychometric review.
- [ ] Product-specific material/process qualification and tolerances.
- [ ] Progressively migrate historical docs when edited.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
