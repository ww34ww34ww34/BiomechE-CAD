# BiomechE-CAD — Functional Evidence Batch 05: Heel / Rearfoot Containment, Relief and Cushioning

**Date:** 2026-08-14  
**Status:** ACTIVE research baseline — `HEEL-001` deep dive  
**Architecture:** intentionally out of scope / parked.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is authoritative for source metadata and locators.

---

## 0. Purpose

Define what the heel/rearfoot feature family must mean functionally before any geometry kernel or implementation operator is frozen.

The central conclusion is:

> **“Heel” is not one operation. Rearfoot containment geometry, local relief and cushioning/material properties are separate prescription dimensions with different mechanisms and evidence.**

BiomechE-CAD should therefore avoid a single opaque `HeelStrength` or a single baked mesh deformation.

Recommended functional decomposition:

```text
HEEL CONTAINMENT GEOMETRY
+ LOCAL HEEL RELIEF / OFFLOAD
+ HEEL MECHANICAL / CUSHIONING REGION
+ CONTEXT / INDICATION
+ MEASURED OUTCOME
```

EasyCAD2 already validates a heel/wrap/camber workflow [EC2-VAL-PLAN-1.4, US11; EC2-MANUAL-1.1, pp. 24–30]. That establishes a professional behavioral baseline but does not prove that every available geometry parameter has a known clinical dose-response curve.

---

# 1. Evidence hierarchy and caution

Heel-related literature mixes several distinct populations and mechanisms:

```text
adult plantar heel pain / plantar fasciitis
pediatric calcaneal apophysitis (Sever's)
diabetic / high-risk offloading
healthy volunteers
finite-element / computational models
```

Results must remain tied to their population and protocol.

In particular:

- plantar-fasciitis evidence does not automatically define diabetic offloading rules;
- pediatric Sever's evidence does not define adult CAD defaults;
- finite-element dose findings are useful for parameter selection but are not therapeutic prescriptions;
- heel pressure reduction alone does not prove better pain/function outcome.

The 2023 heel-pain clinical practice guideline also cautions that foot orthoses should not be treated as an isolated short-term intervention for plantar fasciitis; they may be used as part of a multimodal treatment approach [GUIDE-HEEL-PAIN-2023, Foot Orthoses recommendation].

---

# 2. EasyCAD2 behavioral baseline

EasyCAD2 validates heel/camber generation without mesh distortion [EC2-VAL-PLAN-1.4, US11]. The manual places heel/wrap/camber among the principal modification tools [EC2-MANUAL-1.1, pp. 24–30].

For BiomechE-CAD this supports preserving at least:

```text
heel containment / cup
wrap
camber / transition
side-specific editing
measurable height/profile
```

but we must separate **EasyCAD parity parameters** from **scientifically calibrated doses**.

---

# 3. Heel containment is a real biomechanical mechanism

## 3.1 Confinement changes heel-pad mechanics

A human study in patients with unilateral plantar fasciitis used ultrasound shear-wave elastography to compare standing with and without a plastic heel cup. The heel cup increased heel-pad layer thickness and reduced measured shear-wave speed/stiffness, supporting a confinement mechanism rather than simple vertical cushioning [REF-CAD-059, Abstract—Results/Conclusion].

Functional consequence:

```text
containment geometry
!=
soft cushioning material
```

The CAD should therefore make containment dimensions independently editable.

## 3.2 Individualized heel cup geometry can be scan-derived

Li et al. created individualized 3D-printed nylon heel cups from 3D scans. The device was 5 mm thick in that experimental design and wrapped the plantar heel from the upper calcaneal margin toward the arch; the study combined plantar-pressure analysis, pain assessment and FE simulation [REF-CAD-058, Methods—Heel cup design/fabrication; Abstract—Results].

This supports:

- patient-specific rearfoot geometry;
- explicit cup thickness/wall geometry;
- scan provenance;
- separate reporting of geometry and material.

It does **not** justify 5 mm as a universal heel-cup thickness.

---

# 4. Heel cup height is a legitimate design variable, but human dose-response evidence is limited

A muscle-driven finite-element Taguchi study explicitly varied heel-cup height at 14, 16 and 18 mm together with arch height, medial posting and material stiffness [REF-CAD-046, Table 2]. In that model, heel-cup height contributed materially to hindfoot pressure and plantar-fascia strain variance [REF-CAD-046, Results/Table 4].

Therefore `heelCupHeight_mm` is justified as a first-class numerical design parameter.

However, this is **model-based** evidence. The current research did not identify a strong adult human trial that isolates several heel-cup heights while holding all other orthosis properties constant.

Product rule:

```text
heelCupHeight_mm = explicit P0 authoring dose
```

but not:

```text
16 mm = universally optimal
```

---

# 5. Wrap / medial wall / lateral wall should be explicit even though their individual clinical dose is not yet established

Containment studies support the importance of enclosing/confining the heel pad [REF-CAD-059; REF-CAD-060]. EasyCAD2 also exposes a wrap-oriented heel workflow [EC2-MANUAL-1.1, pp. 24–30].

Therefore the P0 model should preserve at least:

```text
posteriorCupHeight_mm
medialWallHeight_mm
lateralWallHeight_mm
medialWrapExtent
lateralWrapExtent
posteriorRadius / cup width
wall flare / opening angle
proximal transition
```

Current evidence is insufficient to claim universal optimal values for medial/lateral wall height, wall flare or wrap extent. These remain **clinically meaningful authoring variables**, not evidence-calibrated defaults.

---

# 6. Heel cup and heel wedge are not interchangeable interventions

In boys with calcaneal apophysitis (Sever's disease), a randomized crossover study found substantially greater pain relief with a heel cup than with a heel wedge, and most participants preferred the cup [REF-CAD-061, Abstract—Results]. A related study reported increased heel-pad thickness and reduced heel peak pressure when a rigid custom heel cup was worn [REF-CAD-060, pp. 516–522; Abstract—Results].

This is pediatric, diagnosis-specific evidence, so it must **not** become an adult default. But it supports a product taxonomy that keeps:

```text
HeelCup / Containment
```

separate from:

```text
HeelWedge / Lift / Posting
```

and records the intended effect of each.

---

# 7. Cushioning / heel plug is an independent mechanical prescription

## 7.1 Same geometry, different local material can change heel pressure

In a 2026 crossover study in plantar-fasciitis patients, two custom foot orthoses had the same overall materials/specifications except that one contained a softer PORON heel plug. The heel-plug condition significantly reduced hindfoot average pressure, peak pressure and pressure contact area, while pain/function improved with both orthoses and comfort did not significantly differ between the two conditions [REF-CAD-018, pp. 198–204; Abstract—Methods/Results].

Functional consequence:

```text
HeelContainmentGeometry
```

and

```text
HeelMechanicalRegion
```

must be independently versioned.

## 7.2 Cushioning should carry physical/material provenance

Subject-specific modeling work on diabetic footwear shows that optimal cushioning behavior cannot be inferred from a generic material name alone; loading conditions and tissue characteristics influence the response [REF-CAD-064, pp. 531–538; Abstract].

At minimum retain when known:

```text
materialId
commercialName [optional]
hardnessScale + value
elastic/effective modulus
thickness_mm
density
compression / fatigue state [future]
manufacturing process
```

A future pressure-driven material assistant may use these fields, but no universal `soft = better` rule is justified.

---

# 8. Conformity can matter more than material choice

A finite-element study systematically varied heel insole conformity, thickness and material. In that model, conformity was the most influential design variable for peak heel pressure, while material selection had a smaller effect; predicted pressure relief increased from a flat to a fully conforming design [REF-CAD-063, pp. 2363–2370; Abstract—Methods/Results].

This is important for product semantics:

```text
fit / conformity
```

must not be collapsed into:

```text
softness
```

BiomechE-CAD should be able to quantify rearfoot conformity/deviation to the selected scan/reference independently from material.

---

# 9. Heel relief / spur relief is an offloading feature, not the same thing as a cup

EasyCAD2 contains heel-spur relief/corrective-element workflows in addition to general heel shaping [EC2-MANUAL-1.1, pp. 31–35]. The general offloading evidence established in Batch 03 shows that local relief must be evaluated as load redistribution, including neighboring regions [REF-CAD-029; REF-CAD-031].

Recommended semantic separation:

```text
HeelCup
  contain / support

HeelRelief
  locally reduce/support target load

HeelPlug
  modify local mechanical compliance
```

For `HeelRelief` preserve:

```text
targetROI
reference landmark
center position
width / length / radius
depth / relief height
transition width/profile
material region [optional]
intended metric
safety ring
```

The current literature audit did **not** identify a robust universal dose-response for `heel spur relief depth` or a unique optimal relief shape. Therefore those remain explicit prescription variables whose effect should be verified, not hidden evidence-based defaults.

---

# 10. Camber is a useful CAD variable, but evidence is presently domain-level

EasyCAD2 validates camber as part of heel modification [EC2-VAL-PLAN-1.4, US11]. In the targeted heel literature reviewed for this batch, camber as an isolated variable was not consistently studied independently from heel cup, arch contour, posting or global orthosis shape.

Therefore:

```text
camber = P0 authoring / prescription parameter
```

but:

```text
camber = scientifically calibrated universal therapeutic dose
```

is **not supported** at present.

Required semantics:

```text
camberAmplitude_mm / normalized amount
longitudinal start/peak/end
reference plane/frame
transition profile
```

with acceptance based on geometric reproducibility until stronger clinical evidence exists.

---

# 11. Plantar heel pain evidence requires outcome humility

A systematic review/meta-analysis of randomized trials found moderate-quality evidence for a small medium-term pain benefit of foot orthoses versus sham, but no consistent superiority of customized over prefabricated orthoses and uncertainty about clinical importance [REF-CAD-066, pp. 322–328; Abstract—Results/Conclusion].

The 2023 clinical practice guideline similarly recommends against orthoses as an isolated short-term intervention and allows them as part of multimodal management [GUIDE-HEEL-PAIN-2023, Foot Orthoses recommendation/evidence synthesis].

A multicenter randomized trial from 1999 also found high short-term improvement rates with several prefabricated inserts used with stretching, including silicone and rubber heel devices; this again cautions against equating “custom” with automatic superiority [REF-CAD-062, pp. 214–221; Abstract—Results].

Product consequence:

BiomechE-CAD should support sophisticated heel design without embedding claims such as:

```text
custom heel cup > prefabricated device
more containment = better
softer plug = better for everyone
```

---

# 12. Pressure-guided plantar-fasciitis workflows support measurement, not a universal geometry recipe

A randomized study of chronic plantar fasciitis used CAD/CAM orthoses designed from dynamic plantar-pressure information and reported improvements in pain, plantar-fascia thickness and several patient-reported domains when combined with a night splint [REF-CAD-065, pp. 241–252; Abstract—Methods/Results]. Importantly, peak pressure did not simply decrease across every mask.

This reinforces a BiomechE-CAD rule already established elsewhere:

```text
clinical outcome
!=
minimize one pressure scalar everywhere
```

For heel workflows, pressure/force outcomes should remain regional and protocol-bound.

---

# 13. Proposed P0 heel prescription model

```text
HeelPrescription
  id
  side

  containment
    cupHeightPosterior_mm
    cupHeightMedial_mm
    cupHeightLateral_mm
    cupWidth_mm
    cupRadius/Profile
    medialWrapExtent
    lateralWrapExtent
    wallFlare
    proximalTransition

  camber
    amplitude_mm
    start
    peak
    end
    transitionProfile

  localRelief[]
    targetROI
    landmarkReference
    position
    width_mm
    length_mm
    depth_mm
    transition
    intendedEffect

  mechanicalRegions[]
    materialId
    hardnessScale
    hardnessValue
    modulus_MPa [when known]
    thickness_mm
    cushioningIntent

  reference
    scanId
    acquisitionCondition
    heelLandmarkSet
    coordinateFrame

  context
    indicationProfile
    activity
    footwear

  intendedOutcomes[]
  evidenceReferences[]
  algorithmVersion
```

The model is deliberately geometry-kernel independent.

---

# 14. Heel outcome model

At minimum support separate regions:

```text
medial heel
central heel
lateral heel
whole hindfoot
adjacent midfoot
```

and where data support them:

```text
PeakPressure
PTI
MeanPressure
PeakForce / load fraction
ContactArea
ContactTime
```

Optional clinical/research outcomes:

```text
pain score
Foot Function Index / FHSQ / FAOS as instrumented PROMs
comfort
fit
wear/adherence
plantar fascia thickness [research/clinical import]
heel-pad thickness/stiffness [research import]
```

A pressure improvement and a pain/function improvement are stored as different outcome classes.

---

# 15. Safety / redistribution rules

A heel intervention can redistribute load to midfoot/forefoot or change contact area. Therefore heel verification should use:

```text
HEEL TARGET ROI
+
ADJACENT MIDFOOT SAFETY ROI
+
OPTIONAL WHOLE-FOOT REGIONAL MAP
```

This follows the same principle as Batch 03 offloading: do not report a local heel decrease as a complete success without checking load transfer.

---

# 16. Evidence-linked presets

BiomechE-CAD may later provide presets such as:

```text
Source example: REF-CAD-058
Population: adults with plantar heel pain
Device concept: individualized rigid nylon heel cup
```

or:

```text
Source example: REF-CAD-060
Population: pediatric Sever's disease
Device concept: rigid heel cup / heel-pad confinement
```

but presets must display:

```text
population
protocol
source
geometry/material known from the study
unknown parameters
confidence
```

No evidence-linked preset may silently become the project-wide default.

---

# 17. P0 / P1 / P2 consequence

## P0

- named `HeelCup`, `HeelRelief`, `HeelMechanicalRegion`, `HeelCamber` semantics;
- independent medial/lateral/posterior cup heights;
- width/radius/wrap/transition parameters;
- camber parameters;
- local heel relief with anatomical ROI/landmark;
- local material/cushioning region independent from geometry;
- scan/reference provenance;
- heel geometric QC;
- pressure/outcome hooks;
- revision/history traceability.

## P1

- pressure-guided heel workflow;
- rearfoot conformity/deviation map;
- automatic heel target + adjacent safety-region dashboard;
- evidence-linked presets;
- material property calibration;
- PROM/comfort/fit workflow.

## P2 / R&D

- subject-specific heel-pad FE model;
- predictive pressure/tissue-stress model;
- automatic multi-objective optimization of cup geometry + relief + material;
- regional lattice/metamaterial heel design;
- patient-specific tissue-property integration.

---

# 18. Functional acceptance semantics

## HEEL-001 — semantic separation

`HeelCup`, `HeelRelief`, `HeelMechanicalRegion` and `HeelCamber` remain distinct objects/operations through save/load/history.

## HEEL-002 — independent cup heights

Posterior, medial and lateral cup heights are independently inspectable and versioned.

## HEEL-003 — explicit wrap

Medial/lateral wrap extent and cup width/profile are stored numerically rather than only baked into mesh geometry.

## HEEL-004 — height dose

Requested heel-cup height can be measured on the resulting design/artifact within a declared tolerance.

## HEEL-005 — geometry/mechanics independence

Changing heel-plug material does not silently alter containment geometry; changing cup geometry does not silently replace the material profile.

## HEEL-006 — material provenance

Hardness values preserve scale and units/context; modulus is not inferred from hardness unless a validated conversion exists.

## HEEL-007 — relief provenance

Heel relief records ROI, landmark, dimensions, depth and transition.

## HEEL-008 — target + neighboring outcome

Pressure verification evaluates heel target and adjacent/remote regions rather than heel alone.

## HEEL-009 — scan/reference linkage

Patient-specific containment remains linked to the scan/acquisition and landmark frame used to define it.

## HEEL-010 — camber persistence

Camber amplitude/start/peak/end survive save/load/mirror/history deterministically.

## HEEL-011 — no universal optimum

No cup height, wrap extent, relief depth or cushioning hardness is globally labelled optimal without context/evidence metadata.

## HEEL-012 — population-specific preset

A pediatric Sever's preset cannot be applied as an adult plantar-fasciitis rule without an explicit context change/warning.

## HEEL-013 — pressure vs PROM separation

A heel pressure metric and pain/function score remain separate outcome measurements tied to the same revision.

## HEEL-014 — manufactured artifact verification

Final artifact QC can measure heel-cup height, local thickness and relief depth and compare them with the prescription.

## HEEL-015 — conformity metric

When a reference scan is present, rearfoot conformity/deviation can be quantified independently from material properties.

---

# 19. Evidence gaps explicitly retained

Current research does **not** establish a universal optimum for:

```text
posterior heel-cup height
medial wall height
lateral wall height
wall flare
wrap extent
heel-cup width/radius
camber amplitude
camber longitudinal position
heel-spur relief depth/shape
heel-plug hardness
```

Evidence is strongest for the importance of:

```text
containment / conformity
heel-cup height as a design factor
cushioning/material as an independent factor
regional pressure/contact-area measurement
patient/population context
```

These gaps are product knowledge, not deficiencies to hide with arbitrary defaults.

---

# 20. Product conclusion

The heel editor should behave as a measurable prescription system:

```text
WHAT is being changed?
  containment / relief / material / camber

WHERE?
  anatomical heel region + landmarks

HOW MUCH?
  geometry dose + mechanical dose

WHY?
  intended effect + context + evidence

WHAT HAPPENED?
  heel outcome + neighboring redistribution + PROM/comfort
```

This functional contract remains valid regardless of the future geometry foundation.

---

# 21. Canonical bibliography links

[EC2-MANUAL-1.1]: ../BIBLIOGRAPHY.md#ec2-manual-11
[EC2-VAL-PLAN-1.4]: ../BIBLIOGRAPHY.md#ec2-val-plan-14
[GUIDE-HEEL-PAIN-2023]: ../BIBLIOGRAPHY.md#guide-heel-pain-2023
[REF-CAD-018]: ../BIBLIOGRAPHY.md#ref-cad-018
[REF-CAD-029]: ../BIBLIOGRAPHY.md#ref-cad-029
[REF-CAD-031]: ../BIBLIOGRAPHY.md#ref-cad-031
[REF-CAD-046]: ../BIBLIOGRAPHY.md#ref-cad-046
[REF-CAD-058]: ../BIBLIOGRAPHY.md#ref-cad-058
[REF-CAD-059]: ../BIBLIOGRAPHY.md#ref-cad-059
[REF-CAD-060]: ../BIBLIOGRAPHY.md#ref-cad-060
[REF-CAD-061]: ../BIBLIOGRAPHY.md#ref-cad-061
[REF-CAD-062]: ../BIBLIOGRAPHY.md#ref-cad-062
[REF-CAD-063]: ../BIBLIOGRAPHY.md#ref-cad-063
[REF-CAD-064]: ../BIBLIOGRAPHY.md#ref-cad-064
[REF-CAD-065]: ../BIBLIOGRAPHY.md#ref-cad-065
[REF-CAD-066]: ../BIBLIOGRAPHY.md#ref-cad-066
