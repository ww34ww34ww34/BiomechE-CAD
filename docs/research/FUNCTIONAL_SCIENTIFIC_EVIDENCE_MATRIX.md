# BiomechE-CAD — Functional + Scientific Evidence Matrix

**Status:** ACTIVE RESEARCH BASELINE — batch 1  
**Date:** 2026-08-14  
**Scope:** define *what BiomechE-CAD must do and why* before resuming geometry-kernel selection.  
**Architecture status:** deliberately deferred. No row in this document requires OpenSubdiv, openNURBS, Manifold, OCCT or any other specific geometry library.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is the canonical authority for source metadata and locators.

---

## 0. Purpose

BiomechE-CAD is being specified as a vertical CAD for custom foot orthoses in which product functionality is derived from three distinct evidence classes:

1. **EasyCAD2 behavioral evidence** — establishes an existing professional workflow baseline and feature parity target.
2. **Scientific / clinical / biomechanical literature** — establishes why a feature is useful, what quantities should remain explicit, what outcomes can be measured, and where evidence is uncertain.
3. **BiomechE-CAD product decisions** — establish traceability, versioning, quantitative data handling and acceptance criteria beyond EasyCAD2.

The work order is:

```text
FUNCTIONALITY
    +
SCIENTIFIC EVIDENCE
    +
EASYCAD2 PARITY
    +
MEASURABLE ACCEPTANCE CRITERIA
        ↓
PRODUCT REQUIREMENTS
        ↓
ARCHITECTURE / LIBRARY SELECTION LATER
```

The central rule is:

> Do not promote a geometric implementation mechanism into a product requirement. Define the clinical/design operation, its parameters, inputs, outputs and measurable effects first.

A second documentation rule is now mandatory:

> Any externally-derived concept should cite a stable source ID from `docs/BIBLIOGRAPHY.md` plus the most precise truthful locator available.

---

# 1. Evidence notation

## 1.1 Source classes

- `EC2` — EasyCAD2 manual / validation evidence.
- `GUIDELINE` — clinical guideline or consensus statement.
- `SR/MA` — systematic review / meta-analysis.
- `RCT/CONTROLLED` — randomized or controlled human study.
- `HUMAN` — prospective/crossover/feasibility human study.
- `MODEL` — finite-element/computational/modeling evidence.
- `DOMAIN` — engineering/workflow requirement without independent clinical-effect evidence.

## 1.2 Evidence confidence used here

This matrix does **not** treat all systematic reviews as automatically high certainty. Confidence is stated qualitatively:

- **HIGH FOR A NARROW USE CASE** — guideline or convergent evidence for a defined population/outcome.
- **MODERATE** — multiple human studies/reviews support an effect, but design/population heterogeneity remains.
- **EMERGING** — promising feasibility, small cohorts, modeling or recent technology.
- **MIXED** — literature is heterogeneous or conflicting; feature should remain available but software must not encode a universal therapeutic claim.
- **DOMAIN-ONLY** — useful CAD/workflow capability whose clinical benefit depends on the prescription it realizes.

---

# 2. Executive functional matrix

| ID | Feature | EasyCAD2 evidence | Scientific evidence IDs | Confidence | BiomechE-CAD requirement | Priority |
|---|---|---|---|---|---|---|
| FSE-001 | Scan3D acquisition + provenance | [EC2-VAL-PLAN-1.4, US9]; [EC2-MANUAL-1.1, pp. 21–23] | [REF-CAD-002; REF-CAD-003] | MODERATE for capture; protocol-sensitive | Store source, device, units, side, condition, landmarks, transforms and quality metadata | **P0** |
| FSE-002 | Quantitative plantar-pressure layer | [EC2-VAL-PLAN-1.4, US8]; [EC2-MANUAL-1.1, pp. 19–20] | [REF-CAD-004; REF-CAD-005; REF-CAD-007; GUIDE-IWGDF-2023] | HIGH FOR DIABETIC OFFLOADING; broader use MODERATE | Pressure remains numerical data, registered to anatomy, queryable by ROI; never reduce authority to RGB | **P0** |
| FSE-003 | Pressure-guided design / ROI target | EC2 provides pressure acquisition/registration but not a complete closed loop | [REF-CAD-004; REF-CAD-005; REF-CAD-007; GUIDE-IWGDF-2023] | MODERATE-HIGH in diabetic/offloading context | `OutcomeTarget` / ROI / metric / baseline / target / protocol / evidence source | **P0 data model; P1 guided workflow** |
| FSE-004 | Template / DIMA / patient-specific morphology | [EC2-VAL-PLAN-1.4, US7/US9]; [EC2-MANUAL-1.1, pp. 15–18, 21–23] | [REF-CAD-002; REF-CAD-003] | MODERATE / context-dependent | Editable patient-specific outline, dimensions and morphology; preserve source and design revision | **P0** |
| FSE-005 | Medial/lateral arch support | [EC2-VAL-PLAN-1.4, US12]; [EC2-MANUAL-1.1, pp. 24–30] | [REF-CAD-007; REF-CAD-027; REF-CAD-028] | MODERATE for pressure redistribution; MIXED for universal clinical benefit | Arch is a named prescription with explicit geometry parameters and side/region, not baked anonymous geometry | **P0** |
| FSE-006 | Rearfoot posting / wedge | [EC2-VAL-PLAN-1.4, US13] | [REF-CAD-001] | MODERATE for biomechanical dose response | Preserve signed angle in degrees, reference axis, medial/lateral sense, region, extent and algorithm version | **P0** |
| FSE-007 | Forefoot posting / wedge | [EC2-VAL-PLAN-1.4, US13] | [REF-CAD-015; REF-CAD-016] | EMERGING/MODERATE | Preserve angle, pivot/reference, side, full/partial extent and measured output angle | **P0 by EC2 parity; continue evidence audit** |
| FSE-008 | Heel cup / heel wrap / camber | [EC2-VAL-PLAN-1.4, US11]; [EC2-MANUAL-1.1, pp. 24–30] | [REF-CAD-018; REF-CAD-019] | MODERATE for pressure redistribution | Named heel containment/support operation with height/depth/shape/transition parameters; no universal therapeutic claim | **P0** |
| FSE-009 | Metatarsal bar / dome / pad | [EC2-MANUAL-1.1, pp. 31–35] | [REF-CAD-011; REF-CAD-012; REF-CAD-013; REF-CAD-014; REF-CAD-041; REF-CAD-042; REF-CAD-043; REF-CAD-044] | MODERATE-HIGH for pressure redistribution | Named anatomical element, landmark-relative placement, dimensions, height, rotation, side and intended support/offload goal | **P0** |
| FSE-010 | Local relief / aperture / offloading zone | EC2 elements + sculpt/ROI deformation [EC2-MANUAL-1.1, pp. 31–40] | [REF-CAD-007; REF-CAD-020; REF-CAD-029; REF-CAD-030; REF-CAD-031; REF-CAD-032] | MODERATE | Relief is an anatomical ROI operation; inspect target **and surrounding regions** | **P0** |
| FSE-011 | Global material / stiffness | [EC2-VAL-PLAN-1.4, US16/US22] | [REF-CAD-009; REF-CAD-010; REF-CAD-016; REF-CAD-017] | MODERATE | Keep material/mechanical properties separate from geometry; store actual or profile-derived properties where known | **P0 semantics; P1 calibration/export depth** |
| FSE-012 | Regional stiffness / density / metamaterial | [EC2-VAL-PLAN-1.4, US16] | [REF-CAD-008; REF-CAD-021; REF-CAD-022; REF-CAD-023] | EMERGING | First-class `MaterialRegion` / `StiffnessRegion`; do not force property into geometric height alone | **P0 data capability; P1/P2 manufacturing realization** |
| FSE-013 | Custom element editor + sculpt/local deformation | [EC2-VAL-PLAN-1.4, US15/US17]; [EC2-MANUAL-1.1, pp. 31–40] | DOMAIN-ONLY | DOMAIN-ONLY | Precise, undoable local editing; retain ROI, magnitude and provenance where practical | **P0** |
| FSE-014 | Scan-conform / global deformation | [EC2-VAL-PLAN-1.4, US18]; [EC2-MANUAL-1.1, pp. 36–40] | [REF-CAD-002; REF-CAD-003] | MIXED / DOMAIN-ONLY | Conform is a controlled operation with strength/ROI/source scan and residual/deviation QC, not an automatic truth operation | **P0** |
| FSE-015 | Geometric QC: section, height, thickness, angle | [EC2-VAL-PLAN-1.4, US19/US20/US24]; [EC2-MANUAL-1.1, pp. 42–44, 52–53] | DOMAIN + manufacturing safety | DOMAIN | Sections, angle verification, height, thickness map, minimum-thickness diagnostics, before/after metrics | **P0** |
| FSE-016 | Production artifact + manufacturing profile | [EC2-VAL-PLAN-1.4, US5/US21]; [EC2-MANUAL-1.1, pp. 44–50] | [REF-CAD-024] | MODERATE for feasibility; heterogeneous | Export binds geometry revision + material/manufacturing profile + validation state + hash | **P0 STL/project; P1 3MF/advanced manufacturing** |
| FSE-017 | Post-production pressure verification / iterative optimization | Not explicit as a closed loop in EasyCAD2 validation | [REF-CAD-004; REF-CAD-005; REF-CAD-037; REF-CAD-038; GUIDE-IWGDF-2023] | HIGH FOR SPECIFIC DIABETIC-FOOT USE CASE | Native loop: baseline → design → manufacture → measure → compare → revise; context-specific targets only | **P1 workflow; P0 schema hooks strongly recommended** |
| FSE-018 | Patient-reported outcome, comfort, fit, adherence | EC2 PDF report but not full PROM workflow | [REF-CAD-016; REF-CAD-024; REF-CAD-025; REF-CAD-026] | MODERATE | Link PROM/comfort/fit/adherence to exact CAD/manufacturing revision | **P1; schema should allow from P0** |
| FSE-019 | Traceable prescription → design → outcome | EC2 history/undo/report partially supports lineage | [REF-CAD-004; REF-CAD-005; REF-CAD-020; REF-CAD-024] | PRODUCT-CRITICAL | Preserve prescription parameters, source evidence, operations, manufacturing revision and outcome datasets | **P0** |

---

# 3. Detailed evidence cards

## FSE-001 — Scan3D acquisition and provenance

### EasyCAD2 baseline

EasyCAD2 validation includes STL scan loading, heel/1st/5th landmarks and alignment [EC2-VAL-PLAN-1.4, US9; EC2-MANUAL-1.1, pp. 21–23].

### Literature

A systematic review found 3D scanning promising and often faster than traditional casting, while reliability/accuracy varied and evidence quality was low to moderate [REF-CAD-002]. A later scoping review documented wide variation in scanner specifications, markers, weight-bearing conditions, number of scans, measurements and analysis and proposed a reporting checklist [REF-CAD-003].

### Functional consequence

`Scan3D` is not just an STL blob. Minimum schema direction:

```text
ScanAcquisition
  source/device
  timestamp
  side
  units
  scanner accuracy/resolution [when known]
  weightBearingCondition
  captureProtocol
  landmarks
  coordinateSystem
  registrationTransform
  operator
  qualityFlags
```

**No automatic assumption:** a higher-resolution scan is automatically a clinically better prescription source.

---

## FSE-002 / FSE-003 — Quantitative pressure and pressure-guided design

### EasyCAD2 baseline

Pressure `.bpe/.csv` can be loaded and registered with translation/rotation/scale [EC2-MANUAL-1.1, pp. 19–20; EC2-VAL-PLAN-1.4, US8].

### Strong external evidence for targeted offloading contexts

In the Owings et al. study, pressure-informed custom insoles provided better offloading in 64/70 elevated-pressure metatarsal regions; mean peak pressure and FTI were reduced relative to shape-only comparators, with additional load transfer to midfoot [REF-CAD-004, pp. 839–844; Abstract—Results].

Repeated in-shoe pressure measurement and modification also improved selected high-pressure ROIs in therapeutic footwear [REF-CAD-005]. A systematic review/meta-analysis supports pressure-informed design among useful offloading features in diabetic at-risk feet [REF-CAD-007]. IWGDF guidance demonstrates that quantitative pressure-relief criteria can be meaningful in a defined diabetic-foot context, but must remain context/protocol specific [GUIDE-IWGDF-2023; REF-CAD-006].

### Functional consequence

Pressure must remain:

```text
numeric
metric
registered
source-traceable
ROI-queryable
comparable across design revisions
```

Introduce a generic target model:

```text
OutcomeTarget
  population/context
  protocol
  ROI
  metric
  baselineRevision
  targetType
  targetValue
  units
  evidenceReference
```

**Important:** threshold values from diabetic-foot guidance must **not** become universal BiomechE-CAD thresholds [REF-CAD-037; REF-CAD-038; GUIDE-IWGDF-2023].

---

## FSE-005 — Arch support

### EasyCAD2 baseline

Medial/lateral arch parameters include start, center, end, height, depth and curvature/roundness-related controls [EC2-VAL-PLAN-1.4, US12; EC2-MANUAL-1.1, pp. 24–30].

### Literature

Arch-profile designs are associated with plantar-pressure reduction in parts of the diabetic offloading literature [REF-CAD-007]. However, adult/flexible-flatfoot systematic reviews emphasize weak, heterogeneous or population-dependent evidence and do not justify a universal therapeutic rule [REF-CAD-027; REF-CAD-028].

### Functional consequence

BiomechE-CAD should make arch geometry **precisely controllable and measurable** but should not encode “more arch support = better”.

Store at minimum:

```text
side
medial/lateral
start
center
end
height_mm
depth/width
curvature/roundness
transition
reference frame
```

---

## FSE-006 — Rearfoot posting / wedge as numerical prescription

### EasyCAD2 baseline

Rearfoot wedge is expressed in degrees and can be full or partial [EC2-VAL-PLAN-1.4, US13].

### Literature

Telfer et al. varied only rearfoot posting in 2° increments from 6° lateral to 10° medial and reported significant approximately linear effects for several rearfoot/ankle/knee kinematic and kinetic variables [REF-CAD-001, pp. 1489–1495; Abstract—Methods/Results].

### Functional consequence

Wedge remains a prescription object:

```text
angle_deg
medial/lateral sign convention
rearfoot/forefoot
pivot/reference axis
full/partial
application extent
transition profile
```

The manufactured result should support a measurement fixture that verifies the requested angle within a declared tolerance.

---

## FSE-008 — Heel cup / heel support

Heel-cup/arch combinations can change heel pressure/contact area in the tested population [REF-CAD-019]. A custom-orthosis study with and without a softer heel plug supports separating cushioning/material from containment geometry [REF-CAD-018].

### Functional consequence

Separate at least:

```text
heel cup / containment geometry
heel relief or plug region
material property
transition/camber
```

because geometry and cushioning are distinct design variables.

---

## FSE-009 — Metatarsal bar / dome / pad

A systematic review/meta-analysis supports central metatarsal pressure reduction with bespoke/custom orthotic treatment [REF-CAD-011, pp. 111–118]. A 2026 systematic review also reports forefoot peak-pressure/PTI reductions across included orthotic studies, including metatarsal pads/soft contoured designs [REF-CAD-012]. Placement studies show that position relative to metatarsal landmarks/pressure peaks materially changes response [REF-CAD-013; REF-CAD-014; REF-CAD-041; REF-CAD-042].

### Functional consequence

Metatarsal features need anatomical semantics and position reporting, not arbitrary mesh IDs:

```text
MetatarsalBar
MetatarsalDome
MetatarsalRelief
region / target MTHs
position relative to landmarks
width
length
height
rotation
falloff
support vs offload intent
```

See `docs/spec/06_corrective_elements.md` for the formal parameter model.

---

## FSE-010 — Local offloading and load transfer

Custom-made diabetic insoles show material inter-individual response and load transfer to medial midfoot [REF-CAD-020]. A 2024 offloading pilot similarly reduced target-ROI peak pressure/PTI while transferring loading to surrounding areas [REF-CAD-029, Abstract—Results/Conclusion; Fig. 6]. Other studies demonstrate total-contact redistribution [REF-CAD-030] and secondary-site effects of rigid relief [REF-CAD-031]. Pad shape can also worsen peak pressure in a tested context [REF-CAD-032].

### Functional consequence

An offloading tool must show:

```text
TARGET ROI
SURROUNDING RING / NEIGHBOR REGIONS
BEFORE / AFTER METRICS
```

A design optimizer must not minimize only the target cell while creating a harmful neighboring concentration.

See `FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md`.

---

## FSE-011 / FSE-012 — Stiffness, material and regional mechanical properties

Human studies show that stiffness, posting and orthotic configuration can change plantar pressure and biomechanics, with region-specific effects and possible comfort trade-offs [REF-CAD-009; REF-CAD-010; REF-CAD-016; REF-CAD-017].

Pressure-informed and graded/regional mechanical-property approaches are technically promising but clinically less mature [REF-CAD-008; REF-CAD-021; REF-CAD-022; REF-CAD-023].

### Functional consequence

The project model must be future-safe for:

```text
MaterialRegion
StiffnessRegion
DensityRegion
LatticeRegion
mechanical property provenance
```

but current evidence does **not** justify an automatic universal pressure→stiffness prescription rule.

---

## FSE-016 — 3D printing / manufacturing outcome

A 2025 systematic review reports promising clinical/comfort outcomes across 3D-printed orthosis literature while emphasizing heterogeneity, small samples, non-standardized assessment, material selection and durability limitations [REF-CAD-024].

### Functional consequence

Manufacturing method/material must be versioned with the design. A CAD revision alone is insufficient to explain an outcome.

```text
DesignRevision
+ ManufacturingProfile
+ MaterialProfile
+ ExportArtifact/hash
+ QC state
```

---

## FSE-017 — Closed-loop outcome verification

This is a major differentiator from treating CAD as a one-way STL generator.

```text
measurement
  ↓
prescription
  ↓
design revision
  ↓
manufacture
  ↓
post-production measurement
  ↓
comparison
  ↓
revision
```

Pressure-informed design and iterative in-shoe optimization have direct human evidence in diabetic-foot contexts [REF-CAD-004; REF-CAD-005]. IWGDF and pressure-threshold reviews further demonstrate why target definitions must carry clinical context and protocol rather than become global constants [GUIDE-IWGDF-2023; REF-CAD-037; REF-CAD-038].

Possible metrics include:

```text
PeakPressure
MeanPressure
PressureTimeIntegral / ForceTimeIntegral
ContactArea
COP trajectory/features
regional load distribution
section/profile metrics
pain/comfort/function PROMs
```

Metric policy is formalized in `docs/spec/09_analysis_qc_dfm.md` [REF-CAD-033; REF-CAD-034; REF-CAD-035; REF-CAD-036; REF-CAD-039; REF-CAD-040].

---

## FSE-018 — Comfort, fit, adherence and PROMs

Assistive-device adherence literature identifies fit/comfort/device properties as relevant to actual use [REF-CAD-025]. The 3D-printed orthosis outcome review includes comfort/fit/function/satisfaction among meaningful outcomes [REF-CAD-024]. A foot/ankle PROM systematic review demonstrates the breadth of instruments used and argues against inventing one proprietary universal score [REF-CAD-026]. Pressure optimization itself may also conflict with convenience/comfort in some configurations [REF-CAD-016].

### Functional consequence

Store PROM instruments and scores with instrument/version metadata and timestamp; link them to the exact orthosis revision in use.

---

# 4. Product rules derived from the literature

## RULE-FSE-001 — Preserve the prescribed dose

When literature or clinical practice uses a numerical dose, preserve that dose as structured data rather than only resulting geometry [REF-CAD-001; REF-CAD-013; REF-CAD-015].

## RULE-FSE-002 — Preserve the measured response

Biomechanical outcome data must remain linked to the exact design/manufacturing revision that produced it [REF-CAD-004; REF-CAD-005; REF-CAD-020].

## RULE-FSE-003 — No universal therapeutic truth table

Evidence is often population-specific and heterogeneous [REF-CAD-007; REF-CAD-024; REF-CAD-027; REF-CAD-028]. BiomechE-CAD must not encode rules such as:

```text
more arch = better
more stiffness = better
lower pressure everywhere = better
custom always > prefabricated
```

## RULE-FSE-004 — Pressure optimization is regional redistribution

A local pressure decrease is insufficient if surrounding regions become overloaded [REF-CAD-004; REF-CAD-020; REF-CAD-029; REF-CAD-030]. Target + neighbor metrics should be first-class.

## RULE-FSE-005 — Geometry and mechanics are separate prescription dimensions

Heel shape, arch geometry, wedge angle and metatarsal geometry must be distinguishable from material hardness, stiffness, density or lattice properties [REF-CAD-009; REF-CAD-010; REF-CAD-018; REF-CAD-021].

## RULE-FSE-006 — Acquisition conditions belong to the evidence chain

Scanner/protocol, weight-bearing and registration conditions belong to the acquisition provenance [REF-CAD-002; REF-CAD-003].

## RULE-FSE-007 — Outcome targets are context/protocol specific

Guideline/threshold values belong to explicit clinical profiles, not global application constants [GUIDE-IWGDF-2023; REF-CAD-037; REF-CAD-038].

---

# 5. Proposed software entities emerging from evidence

The following concepts are now functionally justified independently of geometry architecture:

```text
Prescription
  featureType
  parameters + units
  side
  anatomicalRegion
  intent
  evidenceReference[]

Acquisition
  type
  source/device
  protocol
  coordinateFrame
  registration
  quality

OutcomeTarget
  population/context
  ROI
  metric
  baseline
  target
  protocol
  evidenceReference

OutcomeMeasurement
  dataset
  metric definitions
  ROI values
  acquisition protocol
  timestamp

MaterialRegion
  ROI
  material/profile
  physical properties

DesignRevision
  prescription snapshot
  operations
  manufacturing profile
  export hash

ClinicalOutcome
  pressure metrics
  PROMs
  comfort/fit
  adherence
  revision link
```

These are *domain concepts*, not a C++/C#/WASM implementation decision.

---

# 6. Priority consequence

## P0 — must be possible from the first serious CAD baseline

```text
patient-specific DIMA/morphology
Scan3D + provenance + registration
quantitative pressure + registration + ROI queries
heel / arch / wedge numerical prescription
metatarsal and relief elements
custom/local editing
material/stiffness semantics
sections / height / angle / thickness QC
versioned project/history
manufacturing profile + immutable export revision
traceability prescription -> design
```

Recommended P0 schema hooks even if UI arrives later:

```text
OutcomeTarget
OutcomeMeasurement
ClinicalOutcome
MaterialRegion
```

## P1 — strong product differentiators

```text
pressure-guided design assistant
post-production pressure verification loop
before/after ROI dashboards
PROM / comfort / fit / adherence workflow
regional material/stiffness realization
3MF / material-aware output
advanced scan quality/protocol analytics
positive mould / other manufacturing workflows
```

## P2 / R&D

```text
automatic pressure->geometry optimization
automatic pressure->stiffness/lattice mapping
predictive pressure redistribution
FEM-based design support
explainable AI prescription assistance
multi-objective optimization across pressure / comfort / material / weight
```

---

# 7. Research gaps / next evidence batches

The matrix is intentionally incomplete. Next batches should focus on:

1. **Arch parameter dose** — height/length/position-specific response rather than generic arch-support comparisons.
2. **Heel cup/wrap/camber** — distinguish geometry effects from cushioning/material effects.
3. **Population profiles** — diabetes/offloading, flexible flatfoot, plantar heel pain, metatarsalgia, sport/performance remain separate.
4. **Comfort/fit/adherence** — orthosis-specific PROM and measurement choices.
5. **Manufacturing tolerances and durability** — material/process-specific evidence.
6. **Competitor mapping** — audit competitor features against this matrix without using competitors as scientific evidence.

Completed/partially completed research that now has dedicated documents:

- forefoot wedge / metatarsal placement / arch-hardness / heel dose: `FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md`;
- relief/aperture and neighbour load transfer: `FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md`;
- corrective-element formal model: `docs/spec/06_corrective_elements.md`;
- pressure/PTI/contact-area/shear/protocol metric policy: `docs/spec/09_analysis_qc_dfm.md`.

---

# 8. Bibliography governance

The old local `SCI-001...SCI-024` table has been removed because it duplicated metadata.

Canonical source IDs are maintained only in:

`docs/BIBLIOGRAPHY.md`

This document cites those stable IDs inline. When a full text is later acquired and an exact page/table/figure locator becomes available, update the bibliography entry without changing the source ID.

---

# 9. Current conclusion

The scientific literature supports **building a CAD that preserves prescription variables, acquisitions and outcomes as structured data**, rather than a CAD whose authoritative artifact is only the final mesh.

The strongest product opportunity is not to claim that one arch/wedge/material rule is universally correct. It is to make this chain explicit and measurable:

```text
PATIENT / ACQUISITION
        ↓
QUANTITATIVE EVIDENCE
        ↓
PRESCRIPTION
        ↓
DESIGN REVISION
        ↓
MATERIAL + MANUFACTURING
        ↓
OUTCOME MEASUREMENT
        ↓
COMPARISON / ITERATION
```

That functional contract should be stabilized before the project resumes the OpenSubdiv vs openNURBS or broader geometry-stack decision.

---

## Bibliography links

[EC2-MANUAL-1.1]: ../BIBLIOGRAPHY.md#ec2-manual-11
[EC2-VAL-PLAN-1.4]: ../BIBLIOGRAPHY.md#ec2-val-plan-14
[GUIDE-IWGDF-2023]: ../BIBLIOGRAPHY.md#guide-iwgdf-2023
[REF-CAD-001]: ../BIBLIOGRAPHY.md#ref-cad-001
[REF-CAD-002]: ../BIBLIOGRAPHY.md#ref-cad-002
[REF-CAD-003]: ../BIBLIOGRAPHY.md#ref-cad-003
[REF-CAD-004]: ../BIBLIOGRAPHY.md#ref-cad-004
[REF-CAD-005]: ../BIBLIOGRAPHY.md#ref-cad-005
[REF-CAD-006]: ../BIBLIOGRAPHY.md#ref-cad-006
[REF-CAD-007]: ../BIBLIOGRAPHY.md#ref-cad-007
[REF-CAD-008]: ../BIBLIOGRAPHY.md#ref-cad-008
[REF-CAD-009]: ../BIBLIOGRAPHY.md#ref-cad-009
[REF-CAD-010]: ../BIBLIOGRAPHY.md#ref-cad-010
[REF-CAD-011]: ../BIBLIOGRAPHY.md#ref-cad-011
[REF-CAD-012]: ../BIBLIOGRAPHY.md#ref-cad-012
[REF-CAD-013]: ../BIBLIOGRAPHY.md#ref-cad-013
[REF-CAD-014]: ../BIBLIOGRAPHY.md#ref-cad-014
[REF-CAD-015]: ../BIBLIOGRAPHY.md#ref-cad-015
[REF-CAD-016]: ../BIBLIOGRAPHY.md#ref-cad-016
[REF-CAD-017]: ../BIBLIOGRAPHY.md#ref-cad-017
[REF-CAD-018]: ../BIBLIOGRAPHY.md#ref-cad-018
[REF-CAD-019]: ../BIBLIOGRAPHY.md#ref-cad-019
[REF-CAD-020]: ../BIBLIOGRAPHY.md#ref-cad-020
[REF-CAD-021]: ../BIBLIOGRAPHY.md#ref-cad-021
[REF-CAD-022]: ../BIBLIOGRAPHY.md#ref-cad-022
[REF-CAD-023]: ../BIBLIOGRAPHY.md#ref-cad-023
[REF-CAD-024]: ../BIBLIOGRAPHY.md#ref-cad-024
[REF-CAD-025]: ../BIBLIOGRAPHY.md#ref-cad-025
[REF-CAD-026]: ../BIBLIOGRAPHY.md#ref-cad-026
[REF-CAD-027]: ../BIBLIOGRAPHY.md#ref-cad-027
[REF-CAD-028]: ../BIBLIOGRAPHY.md#ref-cad-028
[REF-CAD-029]: ../BIBLIOGRAPHY.md#ref-cad-029
[REF-CAD-030]: ../BIBLIOGRAPHY.md#ref-cad-030
[REF-CAD-031]: ../BIBLIOGRAPHY.md#ref-cad-031
[REF-CAD-032]: ../BIBLIOGRAPHY.md#ref-cad-032
[REF-CAD-033]: ../BIBLIOGRAPHY.md#ref-cad-033
[REF-CAD-034]: ../BIBLIOGRAPHY.md#ref-cad-034
[REF-CAD-035]: ../BIBLIOGRAPHY.md#ref-cad-035
[REF-CAD-036]: ../BIBLIOGRAPHY.md#ref-cad-036
[REF-CAD-037]: ../BIBLIOGRAPHY.md#ref-cad-037
[REF-CAD-038]: ../BIBLIOGRAPHY.md#ref-cad-038
[REF-CAD-039]: ../BIBLIOGRAPHY.md#ref-cad-039
[REF-CAD-040]: ../BIBLIOGRAPHY.md#ref-cad-040
[REF-CAD-041]: ../BIBLIOGRAPHY.md#ref-cad-041
[REF-CAD-042]: ../BIBLIOGRAPHY.md#ref-cad-042
[REF-CAD-043]: ../BIBLIOGRAPHY.md#ref-cad-043
[REF-CAD-044]: ../BIBLIOGRAPHY.md#ref-cad-044
