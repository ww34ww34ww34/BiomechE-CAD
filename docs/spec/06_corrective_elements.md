# BiomechE-CAD — Corrective Elements Functional Specification

**Version:** v0 — functional/evidence-led  
**Date:** 2026-08-14  
**Status:** active functional baseline  
**Architecture:** deliberately unspecified. No dependency on OpenSubdiv/openNURBS/OCCT/Manifold is implied.

---

## 0. Purpose

Define clinically meaningful corrective/offloading elements as **prescription objects**, with explicit anatomical placement, geometric/mechanical dose, intended effect and outcome hooks.

The product must avoid two common abstractions that lose clinical meaning:

```text
Generic3DObject
```

and

```text
anonymous baked mesh deformation
```

Instead, each element should remain identifiable as a named orthotic intervention.

---

# 1. EasyCAD2 baseline

EasyCAD2 provides:

- a corrective element library organized by rearfoot/midfoot/forefoot/proprio/custom categories;
- element positioning;
- rotation;
- independent X/Y/Z scaling;
- integration relative to upper/lower orthosis surfaces (`SOMMA` / `INTERSEZIONE` semantics in the manual);
- direct element vertex editing;
- save-as-CUSTOM element preset;
- global/per-element hardness and regional rigidity concepts.

BiomechE-CAD should preserve this flexibility while adding anatomical coordinates, evidence context and measurable placement/outcome.

---

# 2. Element taxonomy

Minimum semantic taxonomy:

```text
Rearfoot
  HeelCupSupport
  HeelSpurRelief
  RearfootPost
  RearfootLateralSupport
  RearfootMedialSupport

Midfoot
  MedialArchSupport
  LateralArchSupport
  MidfootRelief
  NavicularRelief

Forefoot
  MetatarsalDome
  MetatarsalPad
  MetatarsalBar
  MetatarsalHeadRelief
  ForefootPost
  FirstRayRelief
  FifthRaySupport
  HalluxRelief

Proprioceptive
  ProprioceptiveElement

Custom
  CustomSupport
  CustomRelief
```

The library may contain vendor/user-facing aliases, but the stored semantic type should be stable and versioned.

---

# 3. Shared element contract

```text
CorrectiveElement
  id
  type
  side

  intendedEffect
    SUPPORT
    OFFLOAD
    REDISTRIBUTE
    CONTAIN
    POST
    PROPRIOCEPTIVE

  targetAnatomy
  targetROI
  referenceLandmarks[]

  position
    absolute_mm
    normalized_anatomical

  rotation_deg

  size
    length_mm
    width_mm
    height_mm

  shapeProfile
  transitionProfile

  mechanicalProfileRef [optional]

  sourcePreset
  sourceEvidence[]

  author
  timestamp
  algorithmVersion
```

A custom element remains a `CorrectiveElement`; customization does not erase its side, placement, provenance or intended function.

---

# 4. Metatarsal family — first-class P0 capability

## 4.1 Why it is first-class

Evidence supports metatarsal additions as a meaningful pressure-redistribution strategy, but response depends strongly on placement, geometry, population and other orthosis features.

Key evidence:

### Systematic review/meta-analysis — mechanical metatarsalgia

**Ruiz-Ramos et al., 2024**  
PMID: `39399760`  
DOI: `10.1016/j.jor.2023.12.006`

Five studies, 158 participants. Customized/bespoke orthotic treatment reduced pressure beneath central 2nd–4th metatarsal heads overall.

### Diabetic neuropathy — placement study

**Hastings et al., 2007**  
PMID: `17257544`  
DOI: `10.3113/FAI.2007.0015`

In the studied population, metatarsal-pad placement about 6.1–10.6 mm proximal to the metatarsal-head line produced consistent pressure reduction; too-distal placement could increase pressure.

This is evidence for **placement sensitivity**, not a universal default.

### Older adults with forefoot pain

**Effects of metatarsal domes on plantar pressures in older people**, 2020  
PMID: `32375847`

All tested dome conditions reduced forefoot pressure; a proximal position about 5 mm proximal to the metatarsal heads offered the best balance in that cohort without adversely increasing proximal pressure.

### Metatarsalgia placement study

**Optimum position of metatarsal pad in metatarsalgia for pressure relief**  
PMID: `15973088`

Placement immediately proximal to the metatarsal-head pressure peak reduced pressure more effectively than a more proximal location in that small cohort.

### Healthy forefoot comparison

**Comparison of the Forefoot Pressure-Relieving Effects of Foot Orthoses**, 2022  
PMID: `36031787`

Compared soft cushioning with different metatarsal-pad concepts and confirms that pressure effect depends on design/placement rather than merely presence of a pad.

### Rheumatoid arthritis

**Orthotic management of plantar pressure and pain in rheumatoid arthritis**  
PMID: `10521640`

Custom orthoses with bar/dome configurations reduced metatarsal pressure; in that study the custom moulded orthosis with a metatarsal dome was most effective for subjective pain.

---

# 5. Metatarsal element parameter model

```text
MetatarsalElement
  type
    DOME
    PAD
    BAR
    RELIEF
    APERTURE

  targetMetatarsals
    MTH1
    MTH2
    MTH3
    MTH4
    MTH5
    CENTRAL_2_4
    CUSTOM_GROUP

  reference
    metatarsalHeadLine
    pressurePeak
    footLengthReference
    scanLandmarkSet

  longitudinalPosition_mm
  longitudinalPosition_normalized

  transversePosition_mm
  transversePosition_normalized

  width_mm
  length_mm
  height_mm
  rotation_deg

  profile
    DOME
    BAR
    ELLIPTIC
    U_SHAPED
    CUSTOM

  proximalTransition_mm
  distalTransition_mm
  medialTransition_mm
  lateralTransition_mm

  mechanicalProfileRef

  intendedEffect
    SUPPORT_PROXIMAL_TISSUE
    OFFLOAD_MTH
    REDISTRIBUTE_FOREFOOT
```

Both millimetres and normalized anatomical location should be reportable.

---

# 6. Placement must be landmark-aware

The software should allow placement relative to:

```text
MTH line
individual MTH landmarks
pressure peak
foot length percentage
scan-derived anatomical landmark
user-defined landmark
```

A user may enter/drag the element visually, but the resulting placement must be numerically inspectable.

Example report:

```text
Metatarsal Dome
Target: MTH2–4
Center: 7.2 mm proximal to MTH line
Foot-length coordinate: 72.8%
Height: 5.0 mm
Width: 42 mm
Rotation: -2.0°
```

This is more clinically useful than `x=154.33, y=31.4` in an arbitrary model frame.

---

# 7. Placement evidence must never silently become a global preset

Published values such as:

```text
6–11 mm proximal to MTH line
5 mm proximal to MTH heads
76% of foot length
```

come from different populations, protocols, pad shapes and outcome definitions.

BiomechE-CAD may expose them as **evidence-linked optional presets**, for example:

```text
Preset source:
  Hastings 2007
Population:
  diabetes + peripheral neuropathy + prior forefoot ulcer
Target:
  pressure reduction
```

but must not call any one of them `optimal` globally.

---

# 8. Outcome model for corrective elements

For an element intended to change plantar load, support:

```text
ElementOutcomeAssessment
  designRevision
  manufacturingRevision
  pressureDataset

  targetROI
  adjacentROIs[]

  peakPressure
  pressureTimeIntegral
  contactArea
  forceFraction [when available]

  comfortScore [optional]
  painScore [optional]
  fitScore [optional]
```

This is necessary because literature shows both successful pressure relief and cases of increased or redistributed pressure.

---

# 9. Pressure redistribution must be visible

Several studies show that offloading at the forefoot or metatarsal heads can increase load in the midfoot or other regions.

Therefore the analysis UI should support:

```text
BEFORE
AFTER
DELTA
```

for:

```text
target ROI
adjacent ROI
whole-foot regional map
```

A metatarsal element should not receive a simple `successful` label merely because its own center has lower pressure.

---

# 10. Geometry dose and mechanical dose are independent

For all corrective elements:

```text
GeometricDose
  height
  width
  length
  position
  transition

MechanicalDose
  material
  stiffness/hardness
  cushioning
  density/lattice [future]
```

must be independently versioned when possible.

This follows from evidence that both shape and material/stiffness can alter pressure/comfort outcomes.

---

# 11. Comfort and adherence are legitimate secondary outcomes

Pressure optimization can conflict with comfort.

Examples in the literature include configurations that improve pressure redistribution while reducing subjective convenience/comfort.

BiomechE-CAD should therefore allow outcome attachment for:

```text
comfort
pain
fit
stability
adherence/wear time
```

without mixing these with geometric validity.

---

# 12. P0 / P1 / P2

## P0

- clinically named element taxonomy;
- element placement/rotation/XYZ size;
- anatomical landmark references;
- absolute + normalized placement reporting;
- metatarsal dome/pad/bar/relief;
- custom element presets;
- support/offload semantic intent;
- target + adjacent ROI analysis hooks;
- version/history.

## P1

- evidence-linked placement presets;
- pressure-guided element placement assistant;
- automated before/after regional comparison;
- comfort/fit outcome workflow;
- per-element material/stiffness calibration.

## P2 / R&D

- predictive element-response model;
- automatic optimization of shape + placement + material;
- population-specific recommendation models;
- FE/tissue-stress optimization.

---

# 13. Functional acceptance tests

## CE-001 — semantic identity

Each library element retains a stable clinical type and intended effect through save/load/history.

## CE-002 — anatomical placement

Position can be reported relative to a landmark system, not only arbitrary XYZ.

## CE-003 — dual coordinate reporting

Metatarsal element placement is reportable in millimetres and normalized foot coordinates.

## CE-004 — placement edit

Moving a pad by a known delta produces the same numeric delta in the stored placement measurement.

## CE-005 — target + adjacent analysis

When a pressure dataset is compared, both target and neighbouring regions are evaluated.

## CE-006 — no universal “optimal” preset

Evidence-derived placement presets preserve population/protocol/source metadata.

## CE-007 — custom preset provenance

A customized element can be saved and reused without losing the original semantic family, author, source and version.

## CE-008 — geometry/mechanical independence

Element shape can be changed without changing its mechanical profile, and vice versa.

## CE-009 — outcome traceability

Pressure/comfort outcome data is tied to the exact design/manufacturing revision.

## CE-010 — reportability

A report can state at minimum:

```text
element type
anatomical target
position
size/height
rotation
mechanical profile
intended effect
outcome metrics when available
```

---

# 14. Key sources

- Ruiz-Ramos M et al. PMID `39399760`; DOI `10.1016/j.jor.2023.12.006`.
- Hastings MK et al. PMID `17257544`; DOI `10.3113/FAI.2007.0015`.
- Optimum position of metatarsal pad in metatarsalgia. PMID `15973088`.
- Effects of metatarsal domes on plantar pressures in older people. PMID `32375847`.
- Comparison of the Forefoot Pressure-Relieving Effects of Foot Orthoses. PMID `36031787`.
- Orthotic management of plantar pressure and pain in rheumatoid arthritis. PMID `10521640`.
- The effects of insole configurations on forefoot plantar pressure and walking convenience in diabetic neuropathy. PMID `17046124`; DOI `10.1016/j.clinbiomech.2006.08.004`.
- Footwear and insole design features for offloading the diabetic at risk foot. PMID `33532602`.
- Foot orthoses for forefoot pressure reduction — systematic review 2026. PMID `41931962`; DOI `10.1016/j.foot.2026.102251`.

---

# 15. Product conclusion

The metatarsal/corrective-element editor should behave less like an object-placement tool and more like a **measurable prescription editor**:

```text
WHAT element?
WHERE relative to anatomy?
HOW MUCH geometric dose?
WHAT mechanical dose?
WHAT effect is intended?
WHAT happened at target and surrounding regions?
```

This requirement remains independent of the future geometry kernel.
