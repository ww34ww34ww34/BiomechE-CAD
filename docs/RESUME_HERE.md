# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Current checkpoint:** 2026-08-14 — architecture selection is parked; current work is functionality + EasyCAD2 parity + scientific/biomechanical evidence. Relief/offloading, corrective elements, pressure/outcome metrics and the ARCH-001 arch-support deep dive now have evidence-led functional baselines. The canonical bibliography is active through `REF-CAD-057`.

## 1. Product goal

BiomechE-CAD is a professional CAD for custom foot orthoses integrated with BiomechE.

Target product chain:

```text
Acquisition
 -> quantitative evidence
 -> prescription
 -> design revision
 -> material/manufacturing profile
 -> production artifact
 -> outcome measurement
 -> comparison / iteration
```

EasyCAD2 is the detailed behavioral benchmark, not the scientific truth or architectural ceiling.

## 2. Canonical bibliography and citation rule

**Single bibliographic authority:** `docs/BIBLIOGRAPHY.md`.

Stable namespaces include:

```text
EC2-*
GUIDE-*
REF-CAD-*
VENDOR-*
ARCH-*
```

Concepts cite the stable ID plus the most precise truthful locator available:

```text
[EC2-MANUAL-1.1, pp. 31–35]
[REF-CAD-013, pp. 84–88]
[REF-CAD-046, Table 2; Results; Discussion]
```

Locator hierarchy:

```text
exact PDF/manual/article page
> table/figure/numbered section
> HTML section
> PubMed/PMC abstract subsection
> whole source only when no finer locator exists
```

**Never invent a page number.**

`docs/research/SOURCES.md` is an intake/research/verification ledger, not a competing bibliography.

Bibliography migration is complete for the active functional evidence documents currently being used, including the main matrix, Batch 02, Batch 03, corrective elements and analysis/QC/DFM. New sources for the arch deep dive are `REF-CAD-045..057`.

## 3. EasyCAD2 primary baseline

Primary sources:

- `EC2-MANUAL-1.1` — EasyCAD2 Manual 1.1.x.x — 13/01/2024;
- `EC2-VAL-PLAN-1.4` — validation plan 1.4.x.x — 15/01/2026;
- `EC2-VAL-REPORT-1.4` — validation report 1.4.x.x — 20/01/2026, 25/25 PASS.

Confirmed workflow includes DIMA, pressure, Scan3D, thickness/flatten, heel/camber, medial/lateral arch, rear/forefoot wedge, corrective elements, custom element editing, material/rigidity regions, sculpt, scan-conform deformation, sections/measurements, minimum-thickness handling, production, STL/GCODE, reporting and history.

## 4. Current work mode

Architecture/library selection remains intentionally deferred.

```text
EasyCAD2 behavior
+ literature
+ meaningful dose / placement / units
+ measurable outcome
+ acceptance criterion
        ↓
product requirement
        ↓
architecture later
```

Active canonical research/specification:

- `docs/BIBLIOGRAPHY.md`
- `docs/research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md`
- `docs/research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md`
- `docs/research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md`
- `docs/research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md`
- `docs/spec/06_corrective_elements.md`
- `docs/spec/09_analysis_qc_dfm.md`

Architecture background is preserved in:

- `docs/research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md`
- `docs/spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md`

## 5. Main functional conclusions now supported

1. **Pressure remains quantitative data.** Provenance, registration, ROI queries and revision comparisons are first-class.
2. **Outcome targets are context-specific.** Population/protocol/ROI/metric/source belong to the target object.
3. **Dose matters.** Posting, metatarsal placement, arch geometry and mechanical properties survive as structured prescription variables.
4. **Offloading is redistribution.** Target ROI, surrounding safety region and remote load transfer are evaluated together.
5. **Metatarsal elements are landmark-based prescriptions.** Position is reportable in mm and normalized anatomical coordinates.
6. **Geometry and mechanics are separate dimensions.** Material, hardness, stiffness, density and regional structure are not encoded only as shape.
7. **Acquisition conditions matter.** Scan and pressure protocol metadata belong to the evidence chain.
8. **Peak pressure alone is insufficient.** PTI and contact area are P0 where source data permit; force/FTI are retained when valid.
9. **Shear is a separate physical quantity.** Never silently infer it from normal pressure.
10. **Clinical response is heterogeneous.** Do not hardcode one universal orthotic doctrine.
11. **Evidence traceability is mandatory.** External-source-derived concepts cite stable bibliography IDs and truthful locators.
12. **Arch support is not one scalar.** Geometry dose, mechanical dose, clinical/activity context and outcome must remain separable.
13. **Higher arch support is not globally better.** Height may improve selected outcomes while increasing medial-midfoot or remote loading.
14. **Arch height has dose evidence; start/peak/end/curvature/roundness do not yet have robust universal clinical calibration.** They remain legitimate P0 authoring parameters without hidden evidence-derived defaults.
15. **Design arch height and patient structural arch correction are distinct.** Patient measurements require a loading/activity protocol.

## 6. Current evidence matrix / research-batch coverage

Main matrix covers `FSE-001..FSE-019` across acquisition, pressure, morphology, arch, wedge, heel, metatarsal, offloading, material/stiffness, editing, scan conform, QC, manufacturing, outcomes and traceability.

Research batches:

```text
Batch 02 — parameter/dose/placement
Batch 03 — relief/aperture/offloading
Batch 04 — ARCH-001 arch-support deep dive
```

`FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md` now defines:

- EasyCAD2 arch baseline;
- height-dose evidence;
- geometry × posting × heel cup × material interaction;
- human height-dose evidence in specific tasks;
- medial-midfoot and remote load-transfer safety semantics;
- geometry vs hardness/stiffness separation;
- structural arch outcome and loading-context distinction;
- use-case separation;
- evidence gaps for longitudinal extent/peak position/curvature/roundness;
- `ArchSupportPrescription` functional model;
- `ARCH-001..ARCH-014` acceptance semantics.

## 7. Domain entities emerging from evidence

Independent of the eventual CAD kernel, the product model increasingly needs:

```text
Prescription
ArchSupportPrescription
Acquisition
PressureAcquisition
OutcomeTarget
OutcomeMeasurement
OffloadAssessment
CorrectiveElement
MaterialRegion
StiffnessRegion
DesignRevision
ManufacturingProfile
ClinicalOutcome
PROMMeasurement
MetricThreshold
```

An arch prescription now needs at least:

```text
archType
side
start / peak / end
peakHeight_mm
width/depth
curvature/roundness
transitions
reference frame / landmarks
material profile
hardness scale + value
stiffness/modulus when known
intended outcome
safety regions
context/evidence references
```

## 8. Architecture state — PARKED

No foundation engine is selected.

When architecture resumes, compare at least:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

P0 should avoid synchronizing two SubD representations without a named requirement.

## 9. Exact restart point

Do **not** resume kernel selection yet.

Next work:

```text
1. HEEL-001 deep dive — NEXT
   heel cup height/shape
   medial/lateral walls
   wrap
   camber
   heel-spur/local relief
   cushioning / plug / material
   pressure/PTI/contact-area redistribution
   plantar heel pain vs generic containment
   comfort/fit

2. use-case/population profiles
   diabetic offloading
   mechanical metatarsalgia
   flexible flatfoot
   plantar heel pain
   sport/performance

3. PROM/comfort/fit/adherence policy

4. material durability/manufacturing evidence

5. promote mature arch/offloading/corrective-element findings into the consolidated functional specification

6. define Project Schema v0 from the evidence-led domain model

7. derive the kernel-independent acceptance suite

8. only later resume OpenSubdiv vs openNURBS/ON_SubD shoot-out
```

Parallel competitor research remains allowed, but competitor functionality is not scientific evidence.

## 10. DONE

- [x] EasyCAD2 primary behavior consolidated.
- [x] 25-story validation baseline preserved.
- [x] Functional product baseline created.
- [x] Architecture research preserved and architecture selection parked.
- [x] Functional + Scientific Evidence Matrix created.
- [x] Canonical bibliography created and normalized.
- [x] Bibliography expanded through `REF-CAD-057`.
- [x] Active evidence documents migrated to canonical bibliography IDs.
- [x] Pressure-guided design and iterative verification evidence integrated.
- [x] Scan provenance integrated.
- [x] Rearfoot and forefoot wedge dose evidence integrated.
- [x] Metatarsal placement/pressure evidence integrated.
- [x] Relief/aperture Batch 03 completed.
- [x] Target ROI + safety-ring semantics defined.
- [x] Corrective Elements functional spec v0 created.
- [x] Pressure/outcome metric policy v0 created.
- [x] Peak pressure + PTI + contact area P0 policy defined.
- [x] Device/calibration/speed/steps/ROI provenance policy defined.
- [x] Contextual thresholds and measured-vs-predicted separation defined.
- [x] `ARCH-001` deep research completed.
- [x] Arch height identified as explicit measurable dose.
- [x] Arch geometry vs mechanical-dose separation formalized.
- [x] Arch target/midfoot/remote redistribution semantics formalized.
- [x] Arch evidence gaps explicitly recorded instead of hidden by defaults.
- [x] `ARCH-001..ARCH-014` acceptance semantics defined.
- [x] `SPEC_INDEX.md` updated for Batch 04.

## 11. TODO

- [ ] `HEEL-001` heel geometry/material evidence deep dive.
- [ ] Use-case/population evidence profiles.
- [ ] PROM/comfort/fit/adherence specification.
- [ ] Material durability/manufacturing evidence.
- [ ] Expand shear/COP policy when target acquisition systems are fixed.
- [ ] Promote mature evidence into the consolidated P0/P1 functional specification.
- [ ] Derive Project Schema v0 from evidence-led domain entities.
- [ ] Derive kernel-independent functional acceptance suite.
- [ ] Gradually migrate older historical/validation docs when edited.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
