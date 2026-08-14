# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Current checkpoint:** 2026-08-14 — architecture selection is parked; current work is functionality + EasyCAD2 parity + scientific/biomechanical evidence. Relief/offloading, corrective elements and pressure/outcome metric policy now have evidence-led functional baselines. A canonical project bibliography with stable source IDs and page/section locators is now active.

## 1. Product goal

BiomechE-CAD is a professional CAD for custom foot orthoses integrated with BiomechE.

The target product chain is:

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

Every external source used by a canonical research/specification document should have a stable ID there, for example:

```text
EC2-MANUAL-1.1
EC2-VAL-PLAN-1.4
GUIDE-IWGDF-2023
REF-CAD-013
ARCH-OPENSUBDIV
```

Concepts should cite the stable ID plus the most precise truthful locator available:

```text
[EC2-MANUAL-1.1, pp. 31–35]
[REF-CAD-013, pp. 84–88]
[REF-CAD-029, Abstract—Results/Conclusion; Fig. 6]
```

Locator hierarchy:

```text
exact PDF/manual page
> article page/table/figure
> HTML section
> PubMed/PMC Abstract subsection
> whole source only when no finer locator is captured
```

**Never invent a page number.**

`docs/research/SOURCES.md` is now an intake/research/verification ledger, not a competing bibliography. Metadata corrections should be made in `docs/BIBLIOGRAPHY.md`.

Citation migration already completed for:

- `docs/research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md`
- `docs/spec/06_corrective_elements.md`
- `docs/spec/09_analysis_qc_dfm.md`

Older active docs should be migrated progressively as they are edited.

## 3. EasyCAD2 primary baseline

Primary sources:

- `EC2-MANUAL-1.1` — EasyCAD2 Manual 1.1.x.x — 13/01/2024;
- `EC2-VAL-PLAN-1.4` — validation plan 1.4.x.x — 15/01/2026;
- `EC2-VAL-REPORT-1.4` — validation report 1.4.x.x — 20/01/2026, 25/25 PASS.

Confirmed workflow includes DIMA, pressure, Scan3D, thickness/flatten, heel/camber, medial/lateral arch, rear/forefoot wedge, corrective elements, custom element editing, material/rigidity regions, sculpt, scan-conform deformation, sections/measurements, minimum-thickness handling, production, STL/GCODE, reporting and history.

See `docs/BIBLIOGRAPHY.md`, `docs/references/easycad2/README.md` and `docs/validation/easycad2_geometry_parity.md`.

## 4. Current work mode

Architecture/library selection is intentionally deferred.

Current order:

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
- `docs/spec/06_corrective_elements.md`
- `docs/spec/09_analysis_qc_dfm.md`
- `docs/research/SOURCES.md`

Architecture background is preserved in:

- `docs/research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md`
- `docs/spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md`

## 5. Main functional conclusions now supported

1. **Pressure remains quantitative data.** It needs provenance, registration, ROI queries and revision-to-revision comparison.
2. **Outcome targets are context-specific.** Literature/guideline thresholds must carry population, protocol, ROI, metric and source; they are not universal constants.
3. **Dose matters.** Rearfoot/forefoot posting, metatarsal placement, arch geometry and mechanical properties should remain structured prescription variables.
4. **Local offloading is redistribution, not disappearance of load.** Target ROI, surrounding safety region and remote load transfer should be measurable.
5. **Metatarsal elements are landmark-based prescriptions.** Pad/dome/bar/relief position must be reportable relative to anatomical references in mm and normalized coordinates.
6. **Geometry and mechanical properties are separate design dimensions.** Material, hardness, stiffness, density and regional structures should not be encoded only as geometry.
7. **Acquisition conditions matter.** Scan device/protocol/weight-bearing and registration provenance belong to the project.
8. **Pressure outcome is protocol-bound.** Device, calibration, speed/activity, footwear, number of steps and ROI/mask version are part of the result.
9. **Peak pressure alone is insufficient.** PTI and contact area are P0 outcome metrics where source data support them; force/FTI are retained when validly available.
10. **Shear is a separate physical quantity.** It may be imported/measured when hardware supports it but must never be silently inferred from normal pressure.
11. **Clinical response is heterogeneous.** The software must not hardcode one universal orthotic doctrine.
12. **Outcome traceability matters.** The design/material/manufacturing revision should be linkable to later pressure and patient-reported outcomes.
13. **Evidence traceability is now a documentation requirement.** External-source-derived concepts should point to `BIBLIOGRAPHY.md` via stable IDs and precise locators.

## 6. Current evidence matrix coverage

`FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md` currently covers:

```text
FSE-001 Scan3D acquisition/provenance
FSE-002 quantitative plantar pressure
FSE-003 pressure-guided ROI target
FSE-004 patient-specific template/morphology
FSE-005 medial/lateral arch
FSE-006 rearfoot posting/wedge
FSE-007 forefoot posting/wedge
FSE-008 heel cup/wrap/camber
FSE-009 metatarsal bar/dome/pad
FSE-010 local relief/offloading
FSE-011 global material/stiffness
FSE-012 regional stiffness/density/metamaterial
FSE-013 custom element/sculpt
FSE-014 scan-conform/global deformation
FSE-015 geometric QC
FSE-016 manufacturing profile/artifact
FSE-017 post-production verification loop
FSE-018 PROM/comfort/fit/adherence
FSE-019 prescription -> design -> outcome traceability
```

Batch 02 adds direct parameter/placement evidence for forefoot wedge, metatarsal pad, arch support and heel design.

Batch 03 establishes relief/aperture as a target-ROI + surrounding-safety-region problem and adds `OFF-001..OFF-009` acceptance semantics.

`spec/06_corrective_elements.md` converts metatarsal pad/dome/bar/relief into a formal landmark-aware prescription object and now cites canonical bibliography IDs.

`spec/09_analysis_qc_dfm.md` defines the initial outcome metric/protocol policy and now cites canonical bibliography IDs.

## 7. Domain entities emerging from evidence

Independent of the eventual CAD kernel, the product model increasingly needs:

```text
Prescription
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

A meaningful feature should preserve where applicable:

```text
feature type
side / anatomical region
dose
units
reference frame / landmark
placement / extent
material/mechanical properties
intent
source/evidence reference
algorithm/version
```

Pressure/outcome data additionally preserve:

```text
device + calibration
activity/speed protocol
footwear
step count
ROI/mask version
aggregation method
quality/warnings
```

## 8. Architecture state — PARKED

The generic B-Rep/NURBS-heavy P0 was already rejected.

A SubD/control-cage strategy remains a strong hypothesis, but no foundation engine is selected.

When architecture resumes, compare at least:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

P0 should avoid keeping both SubD representations synchronized unless a specific requirement justifies it.

See `docs/DECISIONS.md`, especially `D-CAD-011` through `D-CAD-017`.

## 9. Exact restart point

Do not resume kernel selection yet.

Next work:

```text
1. migrate the remaining active scientific documents to canonical bibliography IDs
   when they are touched:
   - FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md
   - FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md
   - consolidated functional spec sections that cite external evidence

2. arch evidence:
   height, extent, position, curvature, hardness/stiffness interaction

3. heel evidence:
   cup height/shape, wrap/camber, cushioning/material

4. population/use-case profiles:
   diabetic offloading
   mechanical metatarsalgia
   flexible flatfoot
   plantar heel pain
   sport / performance

5. PROM/comfort/fit/adherence policy

6. material durability/manufacturing evidence

7. promote mature evidence rows into the main functional specification

8. define Project Schema entities from the evidence-led data model

9. only later resume geometry architecture shoot-out
```

Competitor research can proceed in parallel, but competitors are feature evidence, not scientific evidence.

## 10. DONE

- [x] EasyCAD2 primary behavior consolidated.
- [x] 25-story validation baseline preserved.
- [x] Functional product baseline created.
- [x] Architecture research preserved.
- [x] Architecture selection explicitly parked.
- [x] Functional + Scientific Evidence Matrix created.
- [x] Scientific source ledger expanded through current 2026 literature.
- [x] Pressure-guided design evidence integrated.
- [x] Scan-provenance evidence integrated.
- [x] Rearfoot and forefoot wedge dose evidence integrated.
- [x] Metatarsal pressure and placement evidence integrated.
- [x] Heel geometry/cushioning evidence started.
- [x] Material/stiffness/regional-property evidence integrated.
- [x] PROM/comfort/fit/adherence direction integrated.
- [x] Parameter/dose evidence batch 02 created.
- [x] Relief/aperture evidence batch 03 created.
- [x] Target ROI + surrounding safety-ring offloading semantics defined.
- [x] Corrective Elements functional spec v0 created.
- [x] Metatarsal pad/dome/bar/relief landmark-placement model defined.
- [x] Pressure/outcome metric policy v0 created.
- [x] Peak pressure + PTI + contact area P0 policy defined.
- [x] Device/calibration/speed/steps/ROI provenance policy defined.
- [x] Contextual threshold and measured-vs-predicted separation defined.
- [x] Canonical `docs/BIBLIOGRAPHY.md` created with stable source IDs and locator policy.
- [x] EasyCAD2 primary sources assigned canonical IDs and page map.
- [x] Scientific references REF-CAD-001..044 consolidated into canonical bibliography.
- [x] Current architecture/vendor references assigned separate non-clinical bibliography namespaces.
- [x] Relief/offloading research migrated to bibliography IDs.
- [x] Corrective-elements specification migrated to bibliography IDs.
- [x] Analysis/QC/DFM specification migrated to bibliography IDs.
- [x] Spec index updated with bibliography governance.

## 11. TODO

- [ ] Migrate `FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md` to canonical bibliography IDs.
- [ ] Migrate `FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md` to canonical bibliography IDs.
- [ ] Gradually migrate older functional/validation docs as they are edited.
- [ ] Arch dose/position/hardness evidence batch.
- [ ] Heel geometry/material evidence batch.
- [ ] Use-case/population evidence profiles.
- [ ] PROM/comfort/fit/adherence specification.
- [ ] Material durability/manufacturing evidence.
- [ ] Expand shear/COP policy when target acquisition systems are fixed.
- [ ] Promote mature matrix rows into the consolidated P0/P1 functional specification.
- [ ] Derive Project Schema v0 from evidence-led domain entities.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
