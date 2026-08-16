# BiomechE-CAD — Corrective Elements Functional Specification

**Version:** v1 — evidence-led frozen product contract  
**Date:** 2026-08-16  
**Status:** **FROZEN v1**  
**Architecture:** deliberately unspecified. No dependency on OpenSubdiv/openNURBS/OCCT/Manifold is implied.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is authoritative for all external references.  
**Authority boundary:** `16_geometry_authoring_contract.md` owns generic placement/replay/requested-vs-realized/mirror semantics; `17_workflow_preset_macro.md` owns reusable definitions; `18_numerical_qualification_registry.md` owns numeric/default/tolerance authority.

---

## 0. Freeze rationale

This v1 freezes the **product semantics** of corrective/offloading elements after cross-document and literature revalidation. It does not freeze a geometry kernel, mesh topology, deformation formula, clinical treatment threshold or universal placement preset.

Evidence continues to support the core design choice that an orthotic addition is a measurable, context-dependent intervention rather than anonymous geometry. Central-metatarsal systematic-review evidence supports pressure reduction from customized treatment while showing heterogeneity; placement studies demonstrate that position matters and cannot be generalized globally; diabetic and heel-pain guidelines likewise require population/pathway-specific interpretation. Therefore:

```text
named semantic element
+ typed anatomical placement
+ explicit requested dose
+ explicit mechanical dose
+ exact evidence/profile context
+ exact design/manufacturing/outcome lineage
```

is frozen, while actual clinical target values remain profile/evidence governed.

---

## 1. Purpose

Define clinically meaningful corrective/offloading elements as **prescription objects**, with explicit anatomical placement, geometric/mechanical dose, intended effect and outcome hooks.

The product must avoid two abstractions that lose clinical meaning:

```text
Generic3DObject
```

and

```text
anonymous baked mesh deformation
```

Instead, each element should remain identifiable as a named orthotic intervention.

---

# 2. EasyCAD2 baseline

EasyCAD2 provides a corrective-element library, element positioning/rotation/XYZ scaling, integration relative to upper/lower orthosis surfaces, direct element-vertex editing and CUSTOM presets [EC2-MANUAL-1.1, pp. 31–35]. The 1.4 validation baseline also covers element transform/customization and material/rigidity behavior [EC2-VAL-PLAN-1.4, US14–US16/US22].

BiomechE-CAD should preserve this flexibility while adding anatomical coordinates, evidence context and measurable placement/outcome.

---

# 3. Element taxonomy

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

# 4. Shared element contract

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

  placementRef
    typed anatomical/reference placement per GAUTH

  requestedDose
    position
    rotation_deg
    length_mm
    width_mm
    height_mm
    shapeProfile
    transitionProfile

  realizedDose [derived/inspection when available]

  mechanicalProfileRef [optional]

  sourcePreset
  sourceEvidence[]

  author
  timestamp
  algorithmVersion
```

A custom element remains a `CorrectiveElement`; customization does not erase its side, placement, provenance or intended function.

Raw anonymous XYZ may exist as derived/cache coordinates but is never the sole persisted placement authority.

---

# 5. Metatarsal family — first-class P0 capability

## 5.1 Why it is first-class

Evidence supports metatarsal additions as a meaningful pressure-redistribution strategy, but response depends strongly on placement, geometry, population and other orthosis features [REF-CAD-011; REF-CAD-012; REF-CAD-013; REF-CAD-041; REF-CAD-042; REF-CAD-043; REF-CAD-044].

### Systematic review/meta-analysis — central metatarsals

Customized/bespoke orthotic treatment reduced pressure beneath central 2nd–4th metatarsal heads overall in the systematic review/meta-analysis by Ruiz-Ramos et al. [REF-CAD-011, pp. 111–118].

### 2026 forefoot review

The 2026 systematic review `REF-CAD-012` supports reductions in forefoot peak pressure and/or PTI across included orthotic interventions while highlighting unresolved mechanistic evidence. This reinforces outcome measurement and explicit intent rather than embedding an unvalidated causal doctrine in geometry.

### Diabetic neuropathy — placement study

In the Hastings et al. cohort, metatarsal-pad placement about 6.1–10.6 mm proximal to the metatarsal-head line consistently reduced pressure, while placement too distal could increase it [REF-CAD-013, pp. 84–88]. This supports **placement sensitivity**, not a universal default.

### Older adults with forefoot pain

Different dome materials and positions were tested; placement 5 mm proximal to the metatarsal heads gave the best balance in the studied older cohort [REF-CAD-041, Abstract—Methods/Results/Conclusions].

### Metatarsalgia placement study

Placement immediately proximal to the metatarsal-head pressure peak reduced pressure more effectively than a more proximal pad location in the small metatarsalgia cohort [REF-CAD-042, pp. 514–520].

### Healthy forefoot comparison

Comparison of cushioning and pad concepts further supports that pressure effect depends on design/placement rather than simply the presence of a pad [REF-CAD-043].

### Rheumatoid arthritis

Custom orthoses with bar/dome configurations reduced metatarsal pressure; in that study the custom moulded orthosis with a metatarsal dome was most effective for subjective pain [REF-CAD-044, pp. 567–575].

---

# 6. Metatarsal element parameter model

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

  placementRef

  requestedDose
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

  realizedDose [optional derived inspection]
  mechanicalProfileRef

  intendedEffect
    SUPPORT_PROXIMAL_TISSUE
    OFFLOAD_MTH
    REDISTRIBUTE_FOREFOOT
```

Both millimetres and normalized anatomical location should be reportable because published studies use both landmark-relative millimetres and normalized foot-length placement [REF-CAD-013; REF-CAD-014; REF-CAD-041].

---

# 7. Placement must be landmark-aware

The software should allow placement relative to:

```text
MTH line
individual MTH landmarks
pressure peak
foot length percentage
scan-derived anatomical landmark
user-defined landmark
```

A user may enter/drag the element visually, but the resulting placement must be numerically inspectable and resolve to the typed placement semantics in `16_geometry_authoring_contract.md`.

Example report:

```text
Metatarsal Dome
Target: MTH2–4
Center: 7.2 mm proximal to MTH line
Foot-length coordinate: 72.8%
Height requested: 5.0 mm
Height realized: <measured or unavailable>
Width: 42 mm
Rotation: -2.0°
```

The values above are illustrative, not defaults.

---

# 8. Placement evidence must never silently become a global preset

Published values such as approximately 6–11 mm proximal to the MTH line [REF-CAD-013], 5 mm proximal to the MTH heads [REF-CAD-041], or 76% of foot length [REF-CAD-014] come from different populations, protocols, pad shapes and outcome definitions.

BiomechE-CAD may expose them as **evidence-linked optional presets** only through exact profile/preset provenance, for example:

```text
Preset source:
  REF-CAD-013 / Hastings 2007
Population:
  diabetes + peripheral neuropathy + prior forefoot ulcer
Target:
  pressure reduction
```

No one value may be labelled globally `optimal`.

---

# 9. Outcome model for corrective elements

For an element intended to change plantar load, support:

```text
ElementOutcomeAssessment
  designRevision
  manufacturingRevision
  pressureDataset

  targetROI
  safetyRingROI? / adjacentROIs[]
  remoteComparisonROIs[]

  peakPressure
  pressureTimeIntegral
  contactArea
  forceFraction [when available]

  comfortScore [optional]
  painScore [optional]
  fitScore [optional]
```

This is necessary because literature shows both successful pressure relief and redistributed/increased loading elsewhere [REF-CAD-004; REF-CAD-020; REF-CAD-029].

---

# 10. Pressure redistribution must be visible

Offloading at the forefoot/metatarsal heads can transfer load to the midfoot or neighbouring regions [REF-CAD-004; REF-CAD-020; REF-CAD-029; REF-CAD-030].

Therefore the analysis UI should support:

```text
BEFORE
AFTER
DELTA
```

for target, safety-ring/adjacent and whole-foot/remote regions where compatible data exist.

A local reduction alone does not create an unconditional `successful` state.

---

# 11. Geometry dose and mechanical dose are independent

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

must be independently versioned when possible. Human studies show that both configuration and stiffness/material can alter regional pressure and subjective response [REF-CAD-009; REF-CAD-010; REF-CAD-016; REF-CAD-017].

---

# 12. Comfort and adherence are legitimate secondary outcomes

Pressure optimization can conflict with comfort. In diabetic neuropathy, increasingly complex support configurations improved pressure in some regions while walking-convenience scores generally worsened [REF-CAD-016, pp. 81–87]. Broader reviews also support storing comfort/fit/adherence as outcomes rather than assuming wear [REF-CAD-024; REF-CAD-025].

These outcomes remain separate from geometry validity and are governed in detail by `14_prom_comfort_adherence.md`.

---

# 13. Mirror semantics

Mirroring a corrective element is a semantic side transformation governed by `GAUTH`, not merely coordinate negation.

The mirrored element SHALL preserve:

```text
semantic family
anatomical target meaning
intended effect
requested dose intent
mechanical profile linkage
preset/evidence provenance
```

while side-specific directions/references are remapped explicitly.

---

# 14. P0 / P1 / P2

## P0

- clinically named element taxonomy;
- element placement/rotation/size;
- anatomical landmark references;
- absolute + normalized placement reporting;
- requested vs realized dose support;
- metatarsal dome/pad/bar/relief;
- custom element presets;
- support/offload semantic intent;
- target + safety-ring/adjacent analysis hooks;
- semantic mirror;
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

# 15. Functional acceptance tests

## CE-001 — semantic identity
Each library element retains a stable clinical type and intended effect through save/load/history.

## CE-002 — anatomical placement
Position can be reported relative to a typed landmark/reference system, not only arbitrary XYZ.

## CE-003 — dual coordinate reporting
Metatarsal element placement is reportable in millimetres and normalized foot coordinates when those representations are defined.

## CE-004 — placement edit
Moving a pad by a known semantic delta produces the corresponding stored placement change and inspectable realized geometry.

## CE-005 — target + adjacent analysis
When a compatible pressure dataset is compared, target and neighbouring/safety regions are evaluated [REF-CAD-020; REF-CAD-029].

## CE-006 — no universal “optimal” preset
Evidence-derived placement presets preserve population/protocol/source metadata [REF-CAD-013; REF-CAD-014; REF-CAD-041; REF-CAD-042].

## CE-007 — custom preset provenance
A customized element can be saved and reused without losing semantic family, author, source, exact preset version/hash and project expansion provenance.

## CE-008 — geometry/mechanical independence
Element shape can be changed without changing its mechanical profile, and vice versa.

## CE-009 — outcome traceability
Pressure/comfort outcome data is tied to the exact design/manufacturing revision.

## CE-010 — reportability
A report can state at minimum element type, anatomical target, typed placement, requested dose, realized dose when available, mechanical profile, intended effect and compatible outcome metrics.

---

# 16. Frozen invariants

```text
CorrectiveElement != anonymous geometry
placement != raw XYZ authority
requested dose != realized dose
geometry dose != mechanical dose
local offload != global outcome success
published placement != universal default
mirror != coordinate reflection only
customization != loss of provenance
```

Numerical values not owned by an evidence/profile/manufacturing/algorithm record remain `OPEN`.

---

# 17. Product conclusion

The corrective-element editor behaves as a **measurable prescription editor**:

```text
WHAT element?
WHERE relative to anatomy?
HOW MUCH requested geometric dose?
WHAT realized dose?
WHAT mechanical dose?
WHAT effect is intended?
WHAT happened at target and surrounding regions?
```

This contract is independent of the future geometry kernel.

---

## Bibliography links

[EC2-MANUAL-1.1]: ../BIBLIOGRAPHY.md#ec2-manual-11
[EC2-VAL-PLAN-1.4]: ../BIBLIOGRAPHY.md#ec2-val-plan-14
[REF-CAD-004]: ../BIBLIOGRAPHY.md#ref-cad-004
[REF-CAD-009]: ../BIBLIOGRAPHY.md#ref-cad-009
[REF-CAD-010]: ../BIBLIOGRAPHY.md#ref-cad-010
[REF-CAD-011]: ../BIBLIOGRAPHY.md#ref-cad-011
[REF-CAD-012]: ../BIBLIOGRAPHY.md#ref-cad-012
[REF-CAD-013]: ../BIBLIOGRAPHY.md#ref-cad-013
[REF-CAD-014]: ../BIBLIOGRAPHY.md#ref-cad-014
[REF-CAD-016]: ../BIBLIOGRAPHY.md#ref-cad-016
[REF-CAD-017]: ../BIBLIOGRAPHY.md#ref-cad-017
[REF-CAD-020]: ../BIBLIOGRAPHY.md#ref-cad-020
[REF-CAD-024]: ../BIBLIOGRAPHY.md#ref-cad-024
[REF-CAD-025]: ../BIBLIOGRAPHY.md#ref-cad-025
[REF-CAD-029]: ../BIBLIOGRAPHY.md#ref-cad-029
[REF-CAD-030]: ../BIBLIOGRAPHY.md#ref-cad-030
[REF-CAD-041]: ../BIBLIOGRAPHY.md#ref-cad-041
[REF-CAD-042]: ../BIBLIOGRAPHY.md#ref-cad-042
[REF-CAD-043]: ../BIBLIOGRAPHY.md#ref-cad-043
[REF-CAD-044]: ../BIBLIOGRAPHY.md#ref-cad-044
