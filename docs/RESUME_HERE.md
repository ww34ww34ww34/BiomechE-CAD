# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Current checkpoint:** 2026-08-14 — architecture selection is parked; current work is functionality + EasyCAD2 parity + scientific/biomechanical evidence.

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

## 2. EasyCAD2 primary baseline

Primary sources:

- EasyCAD2 Manual 1.1.x.x — 13/01/2024;
- EasyCAD2 Validation Plan 1.4.x.x — 15/01/2026;
- EasyCAD2 Validation Report 1.4.x.x — 20/01/2026, 25/25 PASS.

Confirmed workflow includes DIMA, pressure, Scan3D, thickness/flatten, heel/camber, medial/lateral arch, rear/forefoot wedge, corrective elements, custom element editing, material/rigidity regions, sculpt, scan-conform deformation, sections/measurements, minimum-thickness handling, production, STL/GCODE, reporting and history.

See `docs/references/easycad2/README.md` and `docs/validation/easycad2_geometry_parity.md`.

## 3. Current work mode

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

Active canonical research:

- `docs/research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md`
- `docs/research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md`
- `docs/research/SOURCES.md`

Architecture background is preserved in:

- `docs/research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md`
- `docs/spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md`

## 4. Main functional conclusions now supported

1. **Pressure remains quantitative data.** It needs provenance, registration, ROI queries and revision-to-revision comparison.
2. **Outcome targets are context-specific.** Literature/guideline thresholds must carry population, protocol, ROI, metric and source; they are not universal constants.
3. **Dose matters.** Rearfoot/forefoot posting, metatarsal placement, arch geometry and mechanical properties should remain structured prescription variables.
4. **Local offloading redistributes load.** Target ROI and surrounding regions should both be measurable.
5. **Geometry and mechanical properties are separate design dimensions.** Material, hardness, stiffness, density and regional structures should not be encoded only as geometry.
6. **Acquisition conditions matter.** Scan device/protocol/weight-bearing and registration provenance belong to the project.
7. **Clinical response is heterogeneous.** The software must not hardcode one universal orthotic doctrine.
8. **Outcome traceability matters.** The design/material/manufacturing revision should be linkable to later pressure and patient-reported outcomes.

## 5. Current evidence matrix coverage

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

## 6. Domain entities emerging from evidence

Independent of the eventual CAD kernel, the product model increasingly needs:

```text
Prescription
Acquisition
OutcomeTarget
OutcomeMeasurement
MaterialRegion
StiffnessRegion
DesignRevision
ManufacturingProfile
ClinicalOutcome
PROMMeasurement
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

## 7. Architecture state — PARKED

The generic B-Rep/NURBS-heavy P0 was already rejected.

A SubD/control-cage strategy remains a strong hypothesis, but no foundation engine is selected.

When architecture resumes, compare at least:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

P0 should avoid keeping both SubD representations synchronized unless a specific requirement justifies it.

See `docs/DECISIONS.md`, especially `D-CAD-011` through `D-CAD-017`.

## 8. Exact restart point

Do not resume kernel selection yet.

Next work:

```text
1. relief/aperture evidence:
   size, depth, transition, neighboring load transfer

2. metatarsal element evidence:
   bar vs dome/pad, height, shape, placement

3. arch evidence:
   height, extent, position, hardness/stiffness interaction

4. heel evidence:
   cup height/shape, wrap/camber, cushioning/material

5. pressure/outcome metric policy:
   peak, mean, PTI/FTI, contact area, COP, shear when supported

6. separate evidence by use-case/population

7. promote mature matrix rows into formal functional requirements

8. derive acceptance tests independent of geometry kernel
```

Competitor research can proceed in parallel, but competitors are feature evidence, not scientific evidence.

## 9. DONE

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
- [x] Decisions and spec index updated for the functionality-first phase.

## 10. TODO

- [ ] Relief/aperture evidence batch.
- [ ] Metatarsal shape/height evidence batch.
- [ ] Arch dose/position evidence batch.
- [ ] Heel geometry/material evidence batch.
- [ ] Pressure metric policy.
- [ ] Use-case/population evidence profiles.
- [ ] PROM/comfort/fit/adherence specification.
- [ ] Material durability/manufacturing evidence.
- [ ] Promote mature matrix rows into P0/P1 functional specification.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
