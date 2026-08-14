# BiomechE-CAD — Functional + Scientific Evidence Matrix

**Status:** ACTIVE RESEARCH BASELINE — batch 1  
**Date:** 2026-08-14  
**Scope:** define *what BiomechE-CAD must do and why* before resuming geometry-kernel selection.  
**Architecture status:** deliberately deferred. No row in this document requires OpenSubdiv, openNURBS, Manifold, OCCT or any other specific geometry library.

---

## 0. Purpose

BiomechE-CAD is being specified as a vertical CAD for custom foot orthoses in which product functionality is derived from three distinct evidence classes:

1. **EasyCAD2 behavioral evidence** — establishes an existing professional workflow baseline and feature parity target.
2. **Scientific / clinical / biomechanical literature** — establishes why a feature is useful, what quantities should remain explicit, what outcomes can be measured, and where evidence is uncertain.
3. **BiomechE-CAD product decisions** — establish traceability, versioning, quantitative data handling and acceptance criteria beyond EasyCAD2.

The work order is now:

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

| ID | Feature | EasyCAD2 evidence | Scientific purpose / evidence | Confidence | BiomechE-CAD requirement | Priority |
|---|---|---|---|---|---|---|
| FSE-001 | Scan3D acquisition + provenance | US9: STL, heel/1st/5th landmarks, Align | 3D scanning is promising/faster but accuracy/reliability and protocols vary; weight-bearing condition can materially change resulting orthotic design | MODERATE for capture; protocol-sensitive | Store source, device, units, side, condition, landmarks, transforms and quality metadata | **P0** |
| FSE-002 | Quantitative plantar-pressure layer | US8: `.bpe/.csv`, X/Y/rotation/scale | Pressure-informed design improves targeted offloading versus shape-only in defined diabetic-foot studies; pressure is also used in current guidelines to verify offloading | HIGH FOR DIABETIC OFFLOADING; broader use MODERATE | Pressure remains numerical data, registered to anatomy, queryable by ROI; never reduce authority to RGB | **P0** |
| FSE-003 | Pressure-guided design / ROI target | Partial EC2 support via pressure acquisition and deformation workflow | Shape+pressure custom insoles achieved greater high-pressure-region relief than shape-only; systematic review supports pressure-informed design and iterative optimization | MODERATE-HIGH in diabetic/offloading context | `OutcomeTarget` / ROI / metric / baseline / target / protocol / evidence source | **P0 data model; P1 guided workflow** |
| FSE-004 | Template / DIMA / patient-specific morphology | US7: template, shoe size, L/W; US9 scan | Custom shape is clinically relevant, but response is not automatically superior in every population; shape and capture condition must remain explicit | MODERATE / context-dependent | Editable patient-specific outline, dimensions and morphology; preserve source and design revision | **P0** |
| FSE-005 | Medial/lateral arch support | US12: start/center/end, height/depth/curvature | Arch profiles can redistribute plantar load; reviews show heterogeneous effects depending on population and outcome | MODERATE for pressure redistribution; MIXED for universal clinical benefit | Arch is a named prescription with explicit geometry parameters and side/region, not baked anonymous geometry | **P0** |
| FSE-006 | Rearfoot posting / wedge | US13: rearfoot wedge in degrees, full/partial | Controlled dose-response study found significant approximately linear changes in several rearfoot/knee biomechanical variables as rearfoot post angle varied | MODERATE for biomechanical dose response | Preserve signed angle in degrees, reference axis, medial/lateral sense, region, extent and algorithm version | **P0** |
| FSE-007 | Forefoot posting / wedge | US13: forefoot wedge in degrees, full/partial | Orthotic modifications can alter plantar pressure/COP, but feature-specific evidence is less mature than rearfoot posting | EMERGING/MODERATE | Preserve angle, pivot/reference, side, full/partial extent and measured output angle | **P0 by EC2 parity; continue evidence audit** |
| FSE-008 | Heel cup / heel wrap / camber | US11: heel/wrap/camber | Heel-cup/arch combinations redistribute heel pressure; softer heel plugs can reduce hindfoot pressure in plantar-fasciitis patients; design-combination modeling supports heel-cup height as a meaningful factor | MODERATE for pressure redistribution | Named heel containment/support operation with height/depth/shape/transition parameters; no universal therapeutic claim | **P0** |
| FSE-009 | Metatarsal bar / dome / pad | US14 element library; metatarsal family documented | Meta-analysis supports reduction of central metatarsal pressure with customized orthotic treatment; 2026 review reports consistent forefoot-load reductions with metatarsal pads/soft contoured orthoses | MODERATE-HIGH for pressure redistribution | Named anatomical element, position relative to metatarsal region, dimensions, height, rotation, side, intended support/offload goal | **P0** |
| FSE-010 | Local relief / aperture / offloading zone | EC2 elements + sculpt/ROI deformation | Offloading can reduce ROI pressure but may transfer load to surrounding regions; reviews support apertures/metatarsal modifications in defined diabetic-foot contexts | MODERATE | Relief is an anatomical ROI operation; software must inspect target **and surrounding regions** rather than optimize a single cell blindly | **P0** |
| FSE-011 | Global material / stiffness | US22: overall/per-element hardness; US16 rigidity regions | Human studies show orthosis stiffness changes plantar pressure and some kinematics; effects vary by region and population | MODERATE | Keep material/mechanical properties separate from geometry; store actual or profile-derived physical properties where known | **P0 semantics; P1 calibration/export depth** |
| FSE-012 | Regional stiffness / density / metamaterial | US16 closed modifier region; five-level hardness workflow | Pressure-derived personalized metamaterials, graded stiffness and 2026 gradient/porous/lattice studies show strong technical promise but limited clinical maturity | EMERGING | First-class `MaterialRegion` / `StiffnessRegion`; do not force property into geometric height alone | **P0 data capability; P1/P2 manufacturing realization** |
| FSE-013 | Custom element editor + sculpt/local deformation | US15 custom vertex element; US17 sculpt | Independent therapeutic evidence applies to the resulting clinical feature, not to “sculpt” as a CAD command | DOMAIN-ONLY | Provide precise, undoable local editing; every edit should retain ROI, magnitude and provenance when practical | **P0** |
| FSE-014 | Scan-conform / global deformation | US18: conform mesh to scan | Scan literature supports patient-specific morphology but also shows protocol variability; no evidence supports blind conformance as universally optimal treatment | MIXED / DOMAIN-ONLY | Conform is a controlled design operation with strength/ROI/source scan and residual/deviation QC, not an automatic truth operation | **P0** |
| FSE-015 | Geometric QC: section, height, thickness, angle | US19/20/24 | Required to verify that a numerical prescription (e.g. wedge angle) and manufacturing constraints are actually present in the produced design | DOMAIN + manufacturing safety | Sections, angle verification, height, thickness map, minimum-thickness diagnostics, before/after metrics | **P0** |
| FSE-016 | Production artifact + manufacturing profile | US21 STL/GCODE; printer/CNC profiles | 3D-printed orthoses show promising clinical/comfort results, but manufacturing methods/materials and evaluation remain heterogeneous | MODERATE for feasibility; heterogeneous | Export must bind geometry revision + material/manufacturing profile + validation state + hash | **P0 STL/project; P1 3MF/advanced manufacturing** |
| FSE-017 | Post-production pressure verification / iterative optimization | Not explicit as a closed loop in EasyCAD2 validation | Repeated in-shoe pressure measurement and modification can materially improve and preserve offloading; IWGDF provides explicit pressure-relief criteria for high-risk diabetes use cases | HIGH FOR SPECIFIC DIABETIC-FOOT USE CASE | Native loop: baseline → design → manufacture → measure → compare → revise. Population/protocol-specific targets, never universal hardcoded thresholds | **P1 workflow; P0 schema hooks strongly recommended** |
| FSE-018 | Patient-reported outcome, comfort, fit, adherence | EC2 PDF report but not full PROM workflow | Orthotic effectiveness depends on actual wear; comfort/fit are frequent adherence barriers; modern 3D-printed orthosis reviews include comfort, fit and satisfaction among meaningful outcomes | MODERATE | Link PROM/comfort/fit/adherence to exact CAD/manufacturing revision | **P1; schema should allow from P0** |
| FSE-019 | Traceable prescription → design → outcome | EC2 history/undo/report partially supports lineage | Literature repeatedly shows heterogeneous/inter-individual responses; quantitative iteration requires knowing what design generated what outcome | PRODUCT-CRITICAL | Preserve prescription parameters, source evidence, operations, manufacturing revision and outcome datasets | **P0** |

---

# 3. Detailed evidence cards

## FSE-001 — Scan3D acquisition and provenance

### EasyCAD2 baseline

EasyCAD2 validation includes STL scan loading, heel/1st/5th landmarks and alignment.

### Literature

**Farhan et al., 2021 — systematic review**  
PMID `33413570`; DOI `10.1186/s13047-020-00442-8`.

- Six comparative studies.
- 3D scanning appeared faster than traditional casting, but reliability and accuracy were variable.
- Evidence quality was low to moderate.

**Allan et al., 2023 — scoping review**  
PMID `37106385`; DOI `10.1186/s13047-023-00617-z`.

- 78 studies showed large variation in scanner specification, markers, weight-bearing, number of scans, measurements and analysis.
- The paper proposed a 16-item reporting checklist.

**Does Scanner Choice Matter for the Design of Foot Orthosis?, 2025**  
PMID `39943509`.

- Scanner-output quality varied, but weight-bearing condition was more influential on medial arch height and heel width of resulting designs than scanner choice in the tested workflow.

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

**No automatic assumption:** a higher-resolution scan is not automatically a clinically better prescription source.

---

## FSE-002 / FSE-003 — Quantitative pressure and pressure-guided design

### EasyCAD2 baseline

Pressure `.bpe/.csv` can be loaded and registered with translation/rotation/scale.

### Strong external evidence for targeted offloading contexts

**Owings et al., 2008 — shape + pressure vs shape-only custom insoles**  
PMID `18252899`; DOI `10.2337/dc07-2288`.

In 20 participants with diabetes and 70 elevated-pressure metatarsal regions, pressure-informed insoles provided better offloading in 64/70 regions. Mean peak pressure was lower by 32% and 21% relative to the two shape-only insole conditions; force-time integral reductions were also greater.

**Bus et al., 2011 — in-shoe pressure-guided optimization**  
PMID `21610125`; DOI `10.2337/dc10-2206`.

Repeated pressure measurement and modification of customized footwear reduced mean peak pressure in selected high-pressure ROIs from 303 to 208 kPa after an average 1.6 modification rounds.

**Footwear and insole design features for offloading the diabetic at-risk foot — systematic review/meta-analyses, 2021**  
PMID `33532602`.

The review found significant pressure reductions for arch profiles, metatarsal additions and pressure-informed design and specifically recommended pressure analysis to improve footwear/insole design.

**IWGDF prevention guideline 2023 update**  
DOI `10.1002/dmrr.3651`.

For the narrow context of therapeutic footwear in persons with diabetes at risk of recurrent ulceration, demonstrated pressure relief is defined using an in-shoe pressure criterion such as ≥30% reduction at high-pressure locations versus current therapeutic footwear or peak pressure <200 kPa when measured with a validated/calibrated system under the specified measurement conditions.

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

**Important:** `30%` and `200 kPa` must **not** become universal BiomechE-CAD thresholds. They belong to a specific clinical guideline/use case.

---

## FSE-005 — Arch support

### EasyCAD2 baseline

Medial/lateral arch parameters include start, center, end, height, depth, curvature/roundness-related controls.

### Literature

**Footwear and insole design features for diabetic at-risk foot — systematic review/meta-analysis**  
PMID `33532602`.

Arch-profile designs were associated with significant plantar-pressure reduction in the included offloading literature.

**Evidence for foot orthoses for adults with flatfoot — systematic review, 2021**  
PMID `34844639`.

The authors judged the overall adult-flatfoot evidence weak/inconsistent, highlighting limited methodological quality.

**Foot orthoses for flexible flatfeet — systematic review/meta-analysis of patient-reported outcomes, 2023**  
PMID `36611153`; DOI `10.1186/s12891-022-06044-8`.

Substantial heterogeneity prevented a broad conclusion; pain in adults may improve, but evidence does not support a universal claim.

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

Rearfoot wedge is expressed in degrees and can be full or partial.

### Literature

**Telfer et al., 2013 — controlled dose-response study**  
PMID `23631857`; DOI `10.1016/j.jbiomech.2013.03.036`.

Nine custom orthoses per participant varied only rearfoot posting in 2° increments from 6° lateral to 10° medial. Significant linear effects were reported for several rearfoot/ankle/knee kinematic and kinetic variables.

### Functional consequence

Wedge must remain a prescription object:

```text
angle_deg
medial/lateral sign convention
rearfoot/forefoot
pivot/reference axis
full/partial
application extent
transition profile
```

The manufactured result must support a measurement fixture that verifies the requested angle within a declared tolerance.

---

## FSE-008 — Heel cup / heel support

### Evidence

**Prefabricated orthotic design crossover, 2024**  
PMID `39140763`; DOI `10.1097/PXR.0000000000000292`.

Heel-cup + arch-support designs increased contact area and reduced heel-region peak pressure/pressure-time integral in the tested healthy population.

**Balsdon & Dombroski, 2026 — custom orthoses with/without heel plug**  
PMID `40366378`; DOI `10.1097/PXR.0000000000000450`.

In 21 participants with plantar fasciitis, the softer heel-plug condition reduced hindfoot average pressure, peak pressure and contact-area measurements relative to the otherwise matched custom orthosis; both orthosis conditions improved FFI versus baseline.

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

### Evidence

**Ruiz-Ramos et al., 2024/2025 — systematic review/meta-analysis**  
PMID `39399760`; DOI `10.1016/j.jor.2023.12.006`.

Five studies / 158 participants supported reduction of plantar pressure under central 2nd–4th metatarsal heads with bespoke/customized orthotic treatment versus no treatment; superiority over some standardized orthoses/footwear or isolated metatarsal domes was not demonstrated.

**Thiaspras et al., 2026 — systematic review**  
PMID `41931962`; DOI `10.1016/j.foot.2026.102251`.

Across 12 studies / 456 participants, all included studies reported reductions in peak plantar pressure and/or PTI; metatarsal pads and soft contoured orthoses were among the more consistent forefoot-load-reducing approaches.

### Functional consequence

Metatarsal features need anatomical semantics and position reporting, not only arbitrary mesh IDs:

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

---

## FSE-010 — Local offloading and load transfer

### Evidence

**Custom-made diabetic insoles, 2004**  
PMID `15234488`.

Response varied materially between feet: successful offloading in one-third, moderate in one-third and unsuccessful in one-third in the reported first-metatarsal-head risk analysis; load was redistributed toward the medial midfoot.

**Calcaneus/metatarsal offloading pilot, 2024**  
PMID `38758937`.

Offloading reduced target-ROI peak pressure/PTI but transferred loading to surrounding areas and showed inter-individual variability.

### Functional consequence

An offloading tool must show:

```text
TARGET ROI
SURROUNDING RING / NEIGHBOR REGIONS
BEFORE / AFTER METRICS
```

A design optimizer must not minimize only the target cell while creating a harmful neighboring concentration.

---

## FSE-011 / FSE-012 — Stiffness, material and regional mechanical properties

### Human evidence

**Desmyttere et al., 2020**  
PMID `32818861`; DOI `10.1016/j.gaitpost.2020.07.146`.

Changing stiffness and rearfoot posting changed kinematics and plantar pressures; higher stiffness produced region-specific pressure changes including increases up to 31.7% in the tested healthy cohort.

**Cherni et al., 2022**  
PMID `34973589`; DOI `10.1016/j.clinbiomech.2021.105553`.

In 19 individuals with flexible flatfeet, stiffness mainly altered midfoot pressure while posting mainly affected rearfoot pressure.

### Personalized / regional material evidence

**Muir et al., 2022**  
PMID `35987171`; DOI `10.1016/j.clinbiomech.2022.105739`.

Pressure-informed 3D-printed personalized metamaterial insoles reduced peak pressure and PTI in defined offloading regions in a feasibility study.

**Graded stiffness heel offloading, 2023**  
PMID `36706604`.

Graded-stiffness configurations redistributed heel pressure more effectively than simple offloading configurations in an in-vivo pilot, emphasizing that local relief can create perimeter loading.

**Gradient lattice pressure→rod-diameter mapping, 2026**  
PMID `42049041`; DOI `10.1088/1873-4030/ae6593`.

Computational/mechanical work proposed regional modulus customization from plantar-pressure mapping and reported substantial simulated peak-pressure reduction.

**Partition TPMS / region-specific lattice, 2026**  
PMID `42147489`.

Recent work assigned different lattice structures to plantar regions based on pressure distribution and demonstrated region-dependent tradeoffs between cushioning and structural stability.

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

**Atallah et al., 2025 — systematic review**  
PMID `40890671`; DOI `10.1186/s12891-025-09070-4`.

Across 62 included clinical orthosis studies of several orthosis categories, 3D-printed insoles showed pressure-redistribution and comfort benefits in the included literature, while the review emphasized small samples, non-standardized assessments, material selection and durability limitations.

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

For diabetic offloading, both controlled studies and IWGDF guidance support pressure measurement as a way to verify and optimize therapeutic footwear. This does not imply identical targets for sport, flatfoot, plantar fasciitis or other indications.

The data model therefore needs generic metrics rather than a single hardcoded definition of success.

Possible metrics:

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

---

## FSE-018 — Comfort, fit, adherence and PROMs

**Lower-limb assistive-device adherence scoping review, 2022**  
PMID `35753880`; DOI `10.1016/j.jmpt.2022.04.003`.

Reported non-use ranged widely; barriers included device properties and poor fit, while comfort, education and individualized adjustment were recurring factors.

**3D-printed orthoses clinical outcomes systematic review, 2025**  
PMID `40890671`.

Comfort, fit, function and satisfaction are meaningful reported outcomes alongside biomechanics.

**Foot/ankle PROM systematic review, 2025**  
PMID `41033023`; DOI `10.1016/j.foot.2025.102209`.

The literature uses a large number of PROMs, including VAS pain, FAOS, FAAM and others; therefore BiomechE-CAD should not invent a proprietary single outcome score.

### Functional consequence

Store PROM instruments and scores with instrument/version metadata and timestamp; link them to the exact orthosis revision in use.

---

# 4. Product rules derived from the literature

## RULE-FSE-001 — Preserve the prescribed dose

When literature or clinical practice uses a numerical dose (e.g. posting angle), preserve that dose as structured data rather than only resulting geometry.

## RULE-FSE-002 — Preserve the measured response

Biomechanical outcome data must remain linked to the exact design/manufacturing revision that produced it.

## RULE-FSE-003 — No universal therapeutic truth table

Evidence is often population-specific and heterogeneous. BiomechE-CAD must not encode rules such as:

```text
more arch = better
more stiffness = better
lower pressure everywhere = better
custom always > prefabricated
```

## RULE-FSE-004 — Pressure optimization is regional redistribution

A local pressure decrease is insufficient if surrounding regions become overloaded. Target + neighbor metrics should be first-class.

## RULE-FSE-005 — Geometry and mechanics are separate prescription dimensions

Heel shape, arch geometry, wedge angle and metatarsal geometry must be distinguishable from material hardness, stiffness, density or lattice properties.

## RULE-FSE-006 — Acquisition conditions belong to the evidence chain

Weight-bearing, scanner/protocol and registration conditions can alter morphology and derived design. Preserve them.

## RULE-FSE-007 — Outcome targets are context/protocol specific

Guideline thresholds such as IWGDF diabetic-foot offloading criteria belong to an explicit clinical profile, not global application constants.

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

1. **Forefoot wedge/posting** — isolate dose/placement evidence distinct from rearfoot posting.
2. **Heel cup/wrap/camber** — distinguish geometry effects from cushioning/material effects.
3. **Arch parameter dose** — height/length/position-specific response rather than generic arch-support comparisons.
4. **Metatarsal element placement** — distance proximal/distal to MTH and dose/height evidence.
5. **Relief/aperture geometry** — size, depth, transition and neighboring-pressure effects.
6. **Pressure metrics** — peak pressure vs PTI/FTI vs contact area vs shear; define which are valid by use case.
7. **Comfort/fit/adherence** — orthosis-specific PROM and measurement choices.
8. **Manufacturing tolerances and durability** — material/process-specific evidence.
9. **Population profiles** — diabetes/offloading, flexible flatfoot, plantar heel pain, metatarsalgia, sport/performance must remain separate.
10. **Competitor mapping** — audit competitor features against this matrix without using competitors as scientific evidence.

---

# 8. Source ledger — batch 1

| Ref | Citation | Role |
|---|---|---|
| SCI-001 | Telfer S et al. J Biomech. 2013. PMID 23631857. DOI 10.1016/j.jbiomech.2013.03.036 | rearfoot-posting dose response |
| SCI-002 | Farhan M et al. J Foot Ankle Res. 2021. PMID 33413570. DOI 10.1186/s13047-020-00442-8 | 3D scanning review |
| SCI-003 | Allan JJ et al. J Foot Ankle Res. 2023. PMID 37106385. DOI 10.1186/s13047-023-00617-z | scan methodology/provenance |
| SCI-004 | Owings TM et al. Diabetes Care. 2008. PMID 18252899. DOI 10.2337/dc07-2288 | shape+pressure custom design |
| SCI-005 | Bus SA et al. Diabetes Care. 2011. PMID 21610125. DOI 10.2337/dc10-2206 | pressure-guided footwear optimization |
| SCI-006 | IWGDF Prevention Guideline 2023 update. DOI 10.1002/dmrr.3651 | population-specific offloading target guidance |
| SCI-007 | Paton et al./review indexed PMID 33532602 | footwear/insole offloading features systematic review/meta-analysis |
| SCI-008 | Ruiz-Ramos M et al. J Orthop. PMID 39399760. DOI 10.1016/j.jor.2023.12.006 | central metatarsal pressure meta-analysis |
| SCI-009 | Thiaspras L et al. Foot. 2026. PMID 41931962. DOI 10.1016/j.foot.2026.102251 | forefoot-load systematic review |
| SCI-010 | Desmyttere G et al. Gait Posture. 2020. PMID 32818861. DOI 10.1016/j.gaitpost.2020.07.146 | stiffness/posting biomechanical effects |
| SCI-011 | Cherni Y et al. Clin Biomech. 2022. PMID 34973589. DOI 10.1016/j.clinbiomech.2021.105553 | stiffness/posting in flexible flatfeet |
| SCI-012 | Muir BC et al. Clin Biomech. 2022. PMID 35987171. DOI 10.1016/j.clinbiomech.2022.105739 | pressure-based personalized metamaterial insole |
| SCI-013 | Graded stiffness heel offloading. PMID 36706604 | graded-stiffness regional offloading |
| SCI-014 | Wang Lihong et al. Med Eng Phys. 2026. PMID 42049041. DOI 10.1088/1873-4030/ae6593 | pressure-to-lattice mechanical mapping |
| SCI-015 | Partition TPMS insole. 2026. PMID 42147489 | region-specific lattice structures |
| SCI-016 | Atallah H et al. BMC Musculoskelet Disord. 2025. PMID 40890671. DOI 10.1186/s12891-025-09070-4 | 3D-printed orthoses clinical systematic review |
| SCI-017 | Patient compliance with lower-limb assistive devices. 2022. PMID 35753880. DOI 10.1016/j.jmpt.2022.04.003 | adherence/fit/comfort |
| SCI-018 | PROMs in foot/ankle literature. 2025. PMID 41033023. DOI 10.1016/j.foot.2025.102209 | outcome-instrument landscape |
| SCI-019 | Heel plug custom FO study. 2026. PMID 40366378. DOI 10.1097/PXR.0000000000000450 | heel pressure/cushioning |
| SCI-020 | Prefabricated orthotic design crossover. PMID 39140763. DOI 10.1097/PXR.0000000000000292 | heel cup/arch pressure redistribution |
| SCI-021 | Custom-made diabetic insole load redistribution. PMID 15234488 | inter-individual offloading response |
| SCI-022 | Calcaneus/metatarsal offloading pilot. PMID 38758937 | target vs neighboring load transfer |
| SCI-023 | Evidence for adult flatfoot orthoses systematic review. PMID 34844639 | uncertainty / mixed evidence |
| SCI-024 | Flexible-flatfoot PROM systematic review/meta-analysis. PMID 36611153. DOI 10.1186/s12891-022-06044-8 | population-specific outcomes |

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
