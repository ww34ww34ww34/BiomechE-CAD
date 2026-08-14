# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Current checkpoint:** 2026-08-14 — architecture selection remains parked. Current work is functionality + EasyCAD2 parity + scientific/biomechanical evidence. Relief/offloading, corrective elements, pressure/outcome metrics, `ARCH-001` and `HEEL-001` now have evidence-led functional baselines. Canonical bibliography is active through `REF-CAD-067` plus `GUIDE-HEEL-PAIN-2023`.

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
[REF-CAD-063, pp. 2363–2370]
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

Active scientific evidence documents use canonical bibliography IDs. Heel research added `GUIDE-HEEL-PAIN-2023` and `REF-CAD-058..067`; `REF-CAD-018` was enriched with exact 2026 publication details and pages.

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
- `docs/research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md`
- `docs/spec/06_corrective_elements.md`
- `docs/spec/09_analysis_qc_dfm.md`

Architecture background is preserved in:

- `docs/research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md`
- `docs/spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md`

## 5. Main functional conclusions now supported

1. **Pressure remains quantitative data.** Provenance, registration, ROI queries and revision comparisons are first-class.
2. **Outcome targets are context-specific.** Population/protocol/ROI/metric/source belong to the target object.
3. **Dose matters.** Posting, metatarsal placement, arch geometry, heel geometry and mechanical properties survive as structured prescription variables.
4. **Offloading is redistribution.** Target ROI, surrounding safety region and remote load transfer are evaluated together.
5. **Metatarsal elements are landmark-based prescriptions.** Position is reportable in mm and normalized anatomical coordinates.
6. **Geometry and mechanics are separate dimensions.** Material, hardness, stiffness, density and regional structure are not encoded only as shape.
7. **Acquisition conditions matter.** Scan and pressure protocol metadata belong to the evidence chain.
8. **Peak pressure alone is insufficient.** PTI and contact area are P0 where source data permit; force/FTI are retained when valid.
9. **Shear is a separate physical quantity.** Never silently infer it from normal pressure.
10. **Clinical response is heterogeneous.** Do not hardcode one universal orthotic doctrine.
11. **Evidence traceability is mandatory.** External-source-derived concepts cite stable bibliography IDs and truthful locators.
12. **Arch support is not one scalar.** Geometry dose, mechanical dose, clinical/activity context and outcome remain separable.
13. **Higher arch support is not globally better.** Height may improve selected outcomes while increasing medial-midfoot or remote loading.
14. **Heel is not one scalar.** `HeelCup`, `HeelRelief`, `HeelMechanicalRegion` and `HeelCamber` are distinct concepts.
15. **Heel containment and cushioning are mechanistically different.** Confinement geometry can alter heel-pad mechanics independently from local material softness.
16. **Heel-cup height is a legitimate explicit design factor, but no universal adult human optimum is currently established.**
17. **Wrap/wall geometry and camber remain P0 authoring parameters even where isolated clinical dose-response evidence is weak.**
18. **Heel relief inherits target + neighboring load-transfer semantics.** It is not automatically successful because local pressure falls.
19. **Custom is not automatically clinically superior to prefabricated.** Population, protocol and outcome context must remain explicit.
20. **Pressure and PROM outcomes are separate.** A pressure reduction does not automatically imply pain/function superiority.

## 6. Current evidence matrix / research-batch coverage

Main matrix covers `FSE-001..FSE-019` across acquisition, pressure, morphology, arch, wedge, heel, metatarsal, offloading, material/stiffness, editing, scan conform, QC, manufacturing, outcomes and traceability.

Research batches:

```text
Batch 02 — parameter/dose/placement
Batch 03 — relief/aperture/offloading
Batch 04 — ARCH-001 arch-support deep dive
Batch 05 — HEEL-001 heel/rearfoot deep dive
```

`FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md` defines:

- arch geometry dose vs mechanical dose;
- height evidence and limitations;
- combined arch/posting/heel-cup/material interactions;
- midfoot and remote safety regions;
- context-specific outcome interpretation;
- `ARCH-001..ARCH-014` acceptance semantics.

`FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md` defines:

- heel containment/cup semantics;
- posterior/medial/lateral wall height and wrap as explicit authoring parameters;
- heel-cup height as a modeled design factor;
- containment vs local relief vs cushioning/material separation;
- heel plug/material provenance;
- conformity as distinct from softness;
- heel-spur/local relief with ROI/transition/safety-ring semantics;
- camber as P0 authoring parameter with current evidence gap;
- plantar heel pain evidence caution and multimodal-treatment context;
- regional pressure/PTI/contact-area/PROM outcome model;
- `HEEL-001..HEEL-015` acceptance semantics.

## 7. Domain entities emerging from evidence

Independent of the eventual CAD kernel, the product model increasingly needs:

```text
Prescription
ArchSupportPrescription
HeelPrescription
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

A heel prescription now needs at least:

```text
containment:
  posterior/medial/lateral cup heights
  cup width/radius/profile
  medial/lateral wrap
  wall flare / transition

camber:
  amplitude
  start / peak / end
  transition

local relief:
  ROI / landmark
  dimensions / depth
  transition

mechanical region:
  material
  hardness scale + value
  modulus when known
  thickness

context:
  scan/reference
  indication/activity/footwear
  intended outcomes
  evidence references
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
1. USE-CASE / POPULATION EVIDENCE PROFILES — NEXT
   a. diabetic offloading
   b. mechanical metatarsalgia
   c. flexible flatfoot
   d. plantar heel pain
   e. sport / performance
   f. generic custom orthosis

   For each profile define:
   - population / indication boundary
   - relevant CAD features
   - evidence-supported metrics
   - context-specific targets/warnings
   - evidence confidence
   - contraindication / non-transfer rules where literature supports them
   - required acquisition/protocol metadata
   - acceptance semantics

2. PROM / comfort / fit / adherence specification

3. material durability / manufacturing evidence

4. promote mature Arch / Heel / Offload / Corrective Element findings into the consolidated functional specification

5. define Project Schema v0 from the evidence-led domain model

6. derive the kernel-independent acceptance suite

7. refine shear/COP policy when target acquisition hardware is fixed

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
- [x] Bibliography expanded through `REF-CAD-067` + `GUIDE-HEEL-PAIN-2023`.
- [x] Active evidence documents use canonical bibliography IDs.
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
- [x] `ARCH-001..ARCH-014` acceptance semantics defined.
- [x] `HEEL-001` deep research completed.
- [x] Heel containment vs relief vs cushioning/material separation formalized.
- [x] Heel-cup height/wrap/camber evidence boundaries documented.
- [x] Heel target + adjacent redistribution semantics defined.
- [x] `HEEL-001..HEEL-015` acceptance semantics defined.
- [x] `SPEC_INDEX.md` updated through Batch 05.

## 11. TODO

- [ ] Use-case/population evidence profiles.
- [ ] PROM/comfort/fit/adherence specification.
- [ ] Material durability/manufacturing evidence.
- [ ] Promote mature evidence into the consolidated P0/P1 functional specification.
- [ ] Derive Project Schema v0 from evidence-led domain entities.
- [ ] Derive kernel-independent functional acceptance suite.
- [ ] Expand shear/COP policy when target acquisition systems are fixed.
- [ ] Gradually migrate older historical/validation docs when edited.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
