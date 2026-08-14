# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint:** 2026-08-14 — functional/scientific research is consolidated through Batch 08. **`docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` is now the canonical functional baseline.** Architecture selection remains parked. Canonical bibliography extends through `REF-CAD-106` plus `STD-*` standards.

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

Cite exact truthful locators. Never invent pages. Standards entries support official scope/test/qualification semantics but do not imply automatic conformance.

---

## 3. Current work order

```text
EASYCAD2 + LITERATURE + BATCH 03–08
        ↓
FUNCTIONAL SPEC v2 — DONE
        ↓
PROJECT SCHEMA v0 — NEXT
        ↓
KERNEL-INDEPENDENT ACCEPTANCE SUITE
        ↓
COORDINATE / REGISTRATION FREEZE
        ↓
BIOMECHE INTEGRATION + REPORTING
        ↓
ARCHITECTURE SHOOT-OUT LATER
```

Do **not** resume OpenSubdiv vs ON_SubD yet.

---

## 4. Canonical functional specification

### Current canonical

`docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`

It consolidates normative requirements from:

```text
Batch 03 — relief/offloading
Batch 04 — arch
Batch 05 — heel
Batch 06 — indication profiles
Batch 07 — PROM/comfort/fit/adherence
Batch 08 — material/manufacturing
```

and active subordinate specs:

```text
spec/06_corrective_elements.md
spec/08_material_stiffness.md
spec/09_analysis_qc_dfm.md
spec/10_manufacturing.md
spec/13_use_case_profiles.md
spec/14_prom_comfort_adherence.md
```

The previous `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is preserved as the historical detailed baseline instead of being destructively overwritten.

### Functional P0 now explicitly includes

```text
patient/case/revision management
DX/SX + semantic mirror
DIMA/template custom
quantitative pressure import/registration/ROI
Scan3D landmarks/registration/provenance
Scan2D/Image2D calibration
thickness/flatten
heel containment/relief/camber/mechanics
medial/lateral arch
rearfoot/forefoot wedges
corrective elements + metatarsal placement
relief/aperture + safety-ring assessment
material/stiffness regions
sculpt/smooth
scan conform
sections/ruler/height/thickness
PeakPressure/PTI/ContactArea when available
context-bound targets/thresholds
IndicationProfile
PROM registry + measurement provenance
comfort/fit/satisfaction as separate outcomes
adherence/wear exposure
ManufacturingProfile/Run/PhysicalOrthosis
DFM + profile-specific minimum thickness
QC state distinct from export success
STL/project package
report + revision/hash traceability
undo/history/replay
offline authoring
```

---

## 5. Evidence-led domain model to turn into schema

```text
Patient
Case
OrthosisProject
DesignRevision

IndicationProfile[]
activeInterpretationProfile

Acquisition
ScanAcquisition
PressureAcquisition
Image2DAcquisition
Registration

Prescription
ArchSupportPrescription
HeelPrescription
RearfootWedgePrescription
ForefootWedgePrescription
CorrectiveElement
OffloadFeature
SculptOperation
ScanConformOperation

MaterialDefinition
MaterialLot
MaterialRegion
MaterialStack
StructuralMaterialRegion
MechanicalPropertyMeasurement
DurabilityTest
ServiceState

OutcomeTarget
OutcomeMeasurement
OffloadAssessment
MetricThreshold

PROMInstrumentDefinition
PROMMeasurement
ComfortAssessment
FitUsabilityAssessment
SatisfactionAssessment
AdherenceMeasurement
PatientExperienceBundle
InterpretationRule

ManufacturingProfile
ManufacturingRun
ManufacturingArtifact
PhysicalOrthosis
PostProcessStep
QCRequirement
QCMeasurement
ManufacturedGeometryMeasurement

ExportArtifact
ReportArtifact
AuditEvent
```

This model remains geometry-kernel independent.

---

## 6. Key adopted semantics

- EasyCAD2 is behavioral evidence, not scientific truth.
- Dose, placement, units and anatomical reference survive as structured prescription data.
- Offloading is redistribution: target + safety ring + remote regions.
- Arch and heel are multi-component prescriptions, not single sliders.
- Geometry and mechanical/material dose remain independent.
- Pressure is quantitative; heatmaps are derived views.
- Measured and predicted outcomes remain distinct.
- Thresholds are population/protocol/ROI specific.
- `IndicationProfile` is an evidence-context layer, not a diagnosis engine.
- Active diabetic plantar ulcer uses a separate clinical pathway guard.
- Pain, function, comfort, fit, satisfaction and adherence are separate constructs.
- PROM version/language/scoring/licensing are first-class metadata.
- Material nominal property, manufactured effective property and service-aged property are distinct.
- `50 Shore` without scale/method is invalid.
- Export success does not mean physical-part acceptance.
- CAD nominal geometry and manufactured measured geometry remain distinct.

---

## 7. Acceptance semantics already defined

```text
OFF-001..OFF-009
CE-001..CE-010
ARCH-001..ARCH-014
HEEL-001..HEEL-015
PROF-001..PROF-012
PROM-001..PROM-020
MAT-001..MAT-018
MAN-001..MAN-018
```

The future cross-domain suite must add project/revision, registration, mirror, pressure-comparability, history/replay, reporting and traceability invariants.

---

## 8. Architecture state — PARKED

Later comparison remains:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

Prefer one P0 SubD foundation. No major geometry dependency enters merely for theoretical capability coverage.

---

## 9. Exact restart point

### NEXT — `spec/02_project_schema.md` v0

Translate the consolidated functional/domain model into a versioned project schema.

The schema must cover at minimum:

```text
project identity + schema version
patient/case external references
left/right projects
acquisitions + hashes + provenance
registration references
IndicationProfile attachment + active interpretation profile
prescriptions / semantic operations
ROI/masks/landmarks references
material definitions/lots/regions/stacks
DesignRevision graph/history
OutcomeTarget / OutcomeMeasurement
PROM / comfort / fit / satisfaction
AdherenceMeasurement
ManufacturingProfile / Run / Artifact
PhysicalOrthosis
QC requirements/measurements
service state / durability links
export/report artifacts + hashes
algorithm versions
migration metadata
```

### THEN

```text
2. kernel-independent functional acceptance suite
3. freeze `spec/01_coordinate_registration.md`
4. `spec/11_biomeche_integration.md`
5. `spec/12_reporting_traceability.md`
6. competitor functional-gap audit in parallel
7. product-specific PROM/material/process qualification
8. architecture shoot-out only after these freezes
```

---

## 10. DONE

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
- [x] `MAT-001..018` and `MAN-001..018`.
- [x] Bibliography through `REF-CAD-106` plus `STD-*`.
- [x] `D-CAD-020` material/process/artifact/service-state decision.
- [x] **Functional specification v2 consolidated and made canonical.**
- [x] Historical functional spec preserved for audit.
- [x] P0/P1/P2 scope explicitly reconciled.
- [x] `SPEC_INDEX.md` updated to v2.

## 11. TODO

- [ ] `spec/02_project_schema.md` v0 — **NEXT**.
- [ ] Kernel-independent cross-domain acceptance suite.
- [ ] `spec/01_coordinate_registration.md` freeze before implementation.
- [ ] `spec/11_biomeche_integration.md`.
- [ ] `spec/12_reporting_traceability.md`.
- [ ] Expand shear/COP when target hardware is fixed.
- [ ] Competitor feature-gap audit in parallel.
- [ ] Built-in PROM selection after licensing/psychometric review.
- [ ] Product-specific material/process qualification and tolerances.
- [ ] Progressively migrate historical docs when edited.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
