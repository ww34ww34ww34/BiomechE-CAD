# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint:** 2026-08-14 — architecture selection is parked. Current work is functionality + EasyCAD2 parity + scientific/biomechanical evidence. Batches 02–06 and formal specs for corrective elements, analysis/QC and indication profiles are active. Canonical bibliography now extends through `REF-CAD-079`.

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
- `REF-CAD-001..079` scientific sources;
- separate vendor and architecture namespaces.

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
PROMMeasurement
AdherenceMeasurement
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

### NEXT — `PROM-001`

Research and specify **PROM / comfort / fit / adherence** as cross-profile outcome objects.

Must cover:

```text
1. PROM instrument identity/version/language
2. pain vs function vs comfort vs fit vs satisfaction
3. patient-specific meaningful change / interpretation limits where evidence allows
4. wear time / percentage steps worn / indoor vs outdoor adherence
5. timing relative to design/manufacturing revision
6. generic outcome schema without inventing one BiomechE score
7. profile relevance:
   diabetes
   metatarsalgia
   flatfoot
   heel pain
   sport
8. acceptance semantics
9. bibliography IDs + locators
```

### THEN

```text
2. MATERIAL/MANUFACTURING evidence
   hardness / modulus / density
   fatigue / creep / compression set
   durability
   additive/CNC process effects
   tolerances and material-property provenance

3. Promote mature Batch 03–06 findings into
   BIOMECHE_CAD_FUNCTIONAL_SPEC.md

4. Define Project Schema v0
   including IndicationProfile / targets / PROM / adherence

5. Derive kernel-independent functional acceptance suite

6. Refine shear/COP after target acquisition hardware is fixed

7. Competitor gap audit in parallel

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
- [x] Bibliography expanded through `REF-CAD-079`.
- [x] `D-CAD-018` indication-profile baseline decision recorded.
- [x] `SPEC_INDEX.md` updated through Batch 06.

## 9. TODO

- [ ] `PROM-001` PROM/comfort/fit/adherence deep dive — **NEXT**.
- [ ] Material durability/manufacturing evidence.
- [ ] Promote mature evidence into consolidated P0/P1 functional spec.
- [ ] Project Schema v0.
- [ ] Kernel-independent acceptance suite.
- [ ] Expand shear/COP when target hardware is fixed.
- [ ] Competitor feature-gap audit in parallel.
- [ ] Progressively migrate older historical docs when edited.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
