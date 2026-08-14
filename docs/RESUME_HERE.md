# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint:** 2026-08-14 — architecture selection is parked. Current work is functionality + EasyCAD2 parity + scientific/biomechanical evidence. Batches 02–07 and formal specs for corrective elements, analysis/QC, indication profiles and PROM/comfort/adherence are active. Canonical bibliography now extends through `REF-CAD-093` plus COSMIN/FDA PROM guidance.

---

## 1. Product goal

Professional CAD for custom foot orthoses integrated with BiomechE:

```text
Acquisition
 -> quantitative evidence
 -> indication/context
 -> prescription
 -> design revision
 -> material/manufacturing profile
 -> production artifact
 -> wear exposure
 -> outcome measurement
 -> comparison / iteration
```

EasyCAD2 is the detailed behavioral benchmark, not scientific truth or the architectural ceiling.

---

## 2. Canonical evidence governance

**Bibliographic authority:** `docs/BIBLIOGRAPHY.md`.

Stable namespaces:

```text
EC2-*
GUIDE-*
REF-CAD-*
VENDOR-*
ARCH-*
```

Cite the most precise truthful locator:

```text
[EC2-MANUAL-1.1, pp. 31–35]
[REF-CAD-013, pp. 84–88]
[REF-CAD-046, Table 2; Results]
[GUIDE-IWGDF-2023, Offloading guideline]
```

Never invent a page. `docs/research/SOURCES.md` is intake/verification, not a second bibliography.

Current bibliography includes:

- EasyCAD2 manual/validation IDs;
- IWGDF 2023 prevention + offloading guideline context;
- Heel Pain/Plantar Fasciitis CPG 2023;
- COSMIN measurement-instrument selection guidance;
- FDA 2022 PRO instrument guidance for medical-device evaluation;
- `REF-CAD-001..093` scientific sources;
- separate vendor and architecture namespaces.

Questionnaire content/scoring assets require a rights/licensing check separate from scientific validation.

---

## 3. Current work order

```text
EasyCAD2 behavior
+ literature
+ dose / placement / reference frame
+ population / indication context
+ measurable outcome
+ acceptance criterion
        ↓
functional product specification
        ↓
Project Schema + acceptance suite
        ↓
architecture/library selection later
```

Do **not** resume kernel selection yet.

---

## 4. Main completed evidence blocks

### Baseline / EasyCAD2

- 25 validation user stories preserved, 25/25 PASS in the primary validation report.
- DIMA, pressure, scan, heel, arch, wedge, corrective elements, material regions, sculpt, scan conform, QC, production and history consolidated.

### Pressure / outcome policy

- numeric pressure remains authoritative;
- PeakPressure + PTI + ContactArea are P0 where data support them;
- force/FTI when validly available;
- COP P1;
- shear is a separate physical quantity and is never silently inferred;
- device/calibration/activity/speed/footwear/steps/ROI version are provenance;
- `VALID / VALID_WITH_WARNINGS / NOT_COMPARABLE / INSUFFICIENT_DATA` comparison states;
- measured and predicted outcomes remain separate.

### Relief/offloading — Batch 03

- offloading = redistribution;
- target ROI + safety ring + remote regions;
- relief geometry and material dose independent;
- `OFF-001..OFF-009`.

### Corrective elements — `spec/06_corrective_elements.md`

- named clinical elements, not anonymous objects;
- metatarsal pad/dome/bar/relief first-class;
- landmark-relative placement in mm + normalized coordinates;
- evidence-linked presets never universal defaults;
- `CE-001..CE-010`.

### Arch — Batch 04 / `ARCH-001`

- arch support is not one scalar;
- geometry dose vs mechanical dose vs context vs outcome;
- height is an explicit measurable dose;
- higher is not globally better;
- medial midfoot and remote regions need redistribution interpretation;
- start/peak/end/curvature/roundness remain legitimate P0 authoring parameters but lack universal calibrated doses;
- `ARCH-001..ARCH-014`.

### Heel — Batch 05 / `HEEL-001`

- heel is not one scalar;
- `HeelCup`, `HeelRelief`, `HeelMechanicalRegion`, `HeelCamber` are distinct;
- posterior/medial/lateral cup heights and wrap are explicit authoring parameters;
- containment/conformity differs mechanistically from cushioning;
- heel-cup height is a valid design factor but no universal adult optimum is established;
- pressure and pain/PROM outcomes remain separate;
- `HEEL-001..HEEL-015`.

### Indication/use-case profiles — Batch 06 + `spec/13_use_case_profiles.md`

Initial P0 profiles:

```text
DIABETIC_REULCERATION_PREVENTION
MECHANICAL_METATARSALGIA
FLEXIBLE_FLATFOOT
PLANTAR_HEEL_PAIN
SPORT_PERFORMANCE
GENERIC_CUSTOM_ORTHOSIS
```

`IndicationProfile` is a versioned **evidence-context layer**, not a diagnostic engine and not an automatic geometry prescription.

Each profile can define:

```text
population/indication boundary
relevant CAD features
metric bundle
context-valid targets
required acquisition metadata
safety regions
warnings
non-transfer rules
evidence references/confidence
```

Key non-transfer rules:

- diabetic prevention thresholds do not leak into metatarsalgia/flatfoot/heel pain/sport;
- pediatric evidence does not silently become adult evidence;
- walking/general flatfoot evidence does not silently become running evidence;
- healthy runner biomechanics does not establish treatment effect;
- pressure improvement != pain/function improvement;
- injury-prevention effect != performance improvement;
- generic profile has no hidden disease-specific threshold.

### Diabetic active-ulcer guard

`DIABETIC_REULCERATION_PREVENTION` is not the active-ulcer treatment pathway.

For a neuropathic plantar forefoot/midfoot diabetic ulcer, IWGDF 2023 recommends a **non-removable knee-high offloading device** as first-choice healing intervention. If an active ulcer is recorded, surface a separate clinical-pathway warning; do not present a CAD insole alone as equivalent first-line treatment.

Adherence is first-class in the diabetic profile because RCT evidence shows real-world effectiveness depends materially on wear/adherence; future continuous-pressure/wearable integration remains P2.

### PROM / comfort / fit / adherence — Batch 07 + `spec/14_prom_comfort_adherence.md`

Core rule:

```text
pain
function
foot-specific health/QoL
comfort
fit/usability
satisfaction
adherence/wear exposure
```

are separate outcome constructs.

No hidden universal `BiomechE Score` is allowed.

`PROMInstrumentDefinition` preserves:

```text
instrument ID/name
exact version
language / cultural adaptation
respondent / validation context
domains + item count
recall period
response scale + score direction
scoring algorithm version
MID/MCID/MDC/SEM interpretation evidence
license/redistribution status
source references
```

Initial Italian candidate families identified, **not globally selected**:

```text
17-IFFI
FAAM-I/ADL
EFAS Score
```

PROM selection follows construct + measurement properties + feasibility/fit-for-purpose rather than popularity.

Comfort is task/protocol specific and remains separate from pain/function. Validated running tools such as RUN-CAT are evidence that comfort can be multidimensional, not a generic orthosis scale.

Adherence preserves method and denominator:

```text
SELF_REPORT
TEMPERATURE_SENSOR
ACTIVITY_MONITOR
COMBINED_OBJECTIVE

TIME_OUT_OF_BED
WEIGHT_BEARING_TIME
STEPS
PRESCRIBED_SESSION
```

`hours/day`, `% weight-bearing time` and `% steps with device` are not interchangeable. Objective and subjective adherence remain distinct.

Interpretation values such as MID/MCID/MDC are instrument/domain/population/context specific; old measurements remain reproducible with their historical scoring algorithm.

`PROM-001..PROM-020` acceptance semantics are defined.

---

## 5. Current domain model emerging from evidence

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
StiffnessRegion

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

ClinicalEvent
DesignRevision
ManufacturingProfile
ExportArtifact
MetricThreshold
```

This is evidence-led and geometry-kernel independent.

---

## 6. Architecture state — PARKED

The generic NURBS/B-Rep-heavy P0 was rejected.

A SubD/control-cage strategy remains a strong hypothesis, but no foundation is selected.

Later shoot-out:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

Prefer one P0 SubD foundation. Do not add major geometry dependencies without a named requirement/failing fixture.

---

## 7. Exact restart point

### NEXT — `MAT-001 / MAN-001`

Research and specify **material durability + manufacturing evidence**.

Must cover at minimum:

```text
1. material identity / lot / supplier / formulation provenance
2. hardness scale and test method
3. Young/effective modulus where meaningful
4. density
5. thickness × stiffness interaction
6. viscoelasticity / hysteresis
7. compression set
8. creep
9. fatigue / cyclic durability
10. temperature/humidity effects where relevant
11. aging / service-life state
12. additive manufacturing orientation / infill / process parameters
13. CNC material/process parameters where relevant
14. dimensional tolerances
15. post-processing
16. material-region and multi-material realization
17. QC coupons / verification data
18. link actual manufactured properties to design revision
19. acceptance semantics
20. bibliography IDs + locators
```

### THEN

```text
2. Promote mature Batch 03–07 findings into
   BIOMECHE_CAD_FUNCTIONAL_SPEC.md

3. Define Project Schema v0
   including IndicationProfile / targets / PROM / adherence / material provenance

4. Derive kernel-independent functional acceptance suite

5. Refine shear/COP after target acquisition hardware is fixed

6. Competitor gap audit in parallel

7. Select built-in PROM instruments only after
   population fit + psychometric + licensing review

8. Only later resume architecture shoot-out
```

---

## 8. DONE

- [x] EasyCAD2 behavior and 25-story validation baseline consolidated.
- [x] Functionality-first/science-first work mode adopted.
- [x] Canonical bibliography/citation governance established.
- [x] Quantitative pressure/protocol policy established.
- [x] Rearfoot/forefoot wedge dose research.
- [x] Metatarsal placement research and corrective-elements spec.
- [x] Relief/offloading Batch 03 + target/safety-ring model.
- [x] Analysis/QC/DFM spec v0.
- [x] Arch Batch 04 + `ARCH-001..014`.
- [x] Heel Batch 05 + `HEEL-001..015`.
- [x] Use-case/population Batch 06.
- [x] `spec/13_use_case_profiles.md` v0.
- [x] Six initial indication profiles defined.
- [x] Diabetic active-ulcer pathway guard defined.
- [x] Multi-profile provenance / threshold isolation defined.
- [x] `PROF-001..PROF-012` acceptance semantics defined.
- [x] PROM/comfort/fit/adherence Batch 07.
- [x] `spec/14_prom_comfort_adherence.md` v0.
- [x] PROM instrument/version/language/scoring provenance defined.
- [x] Italian candidate PROM families identified without global selection.
- [x] Comfort/fit/satisfaction/adherence separated.
- [x] Objective vs subjective adherence and denominator semantics defined.
- [x] Licensing/redistribution gate for questionnaire content defined.
- [x] `PROM-001..PROM-020` acceptance semantics defined.
- [x] Bibliography expanded through `REF-CAD-093` plus COSMIN/FDA guidance.
- [x] `D-CAD-018` indication-profile baseline decision recorded.
- [x] `D-CAD-019` patient-experience/PROM governance decision recorded.
- [x] `SPEC_INDEX.md` updated through Batch 07.

## 9. TODO

- [ ] `MAT-001 / MAN-001` material durability/manufacturing evidence — **NEXT**.
- [ ] Promote mature evidence into consolidated P0/P1 functional spec.
- [ ] Project Schema v0.
- [ ] Kernel-independent acceptance suite.
- [ ] Expand shear/COP when target hardware is fixed.
- [ ] Competitor feature-gap audit in parallel.
- [ ] Select actual built-in PROMs after fit/psychometric/licensing review.
- [ ] Progressively migrate older historical docs when edited.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
