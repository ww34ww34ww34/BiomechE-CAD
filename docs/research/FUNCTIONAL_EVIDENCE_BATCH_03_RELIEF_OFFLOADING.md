# BiomechE-CAD — Functional Evidence Batch 03: Relief, Aperture and Offloading

**Date:** 2026-08-14  
**Status:** research input to `FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md`  
**Architecture:** intentionally out of scope / parked.  
**Bibliography:** all external-source metadata is canonical in `docs/BIBLIOGRAPHY.md`.

---

## 0. Why this batch matters

For BiomechE-CAD, a local `relief`, `aperture`, `cut-out`, `depression` or other offloading feature must not be treated as a purely geometric indentation.

The literature consistently supports treating plantar offloading as a **load-redistribution problem** [REF-CAD-020; REF-CAD-029; REF-CAD-030]:

```text
reduce load in target ROI
        ↓
load is transferred elsewhere
        ↓
check target + surrounding regions + comfort/fit
```

Therefore the functional specification must preserve the intent, anatomical target, geometry/material dose and the measured redistribution outcome.

---

# 1. Evidence summary

## 1.1 Systematic review evidence — apertures are useful, but not a universal recipe

The systematic review/meta-analysis on footwear and insole features for the diabetic at-risk foot included 54 studies and reports pressure-reduction evidence for arch profile, metatarsal additions, pressure-informed design and apertures, while emphasizing heterogeneity [REF-CAD-007].

**Functional implication:** support aperture/relief features, but do not encode a single geometry as universally optimal.

---

## 1.2 Local pressure reduction can create adjacent overload

The 2024 pilot study on calcaneal and metatarsal-head offloading insoles found reductions in target-region peak pressure and pressure-time integral, with load transfer to surrounding regions and possible higher PTI nearby [REF-CAD-029, Abstract—Results/Conclusion; Fig. 6].

**Functional implication:** every offloading evaluation must include an automatically generated **surrounding safety region** rather than reporting only the target ROI.

---

## 1.3 Pressure redistribution is strongly patient-specific

Custom-made insoles in neuropathic diabetic feet showed heterogeneous individual response: in the analysed first-metatarsal-head high-risk feet, some achieved substantial offloading, some intermediate response and others inadequate response, with increased medial-midfoot loading [REF-CAD-020, Abstract—Results].

**Functional implication:** a CAD feature cannot be labelled successful from geometry alone. The project model should allow post-design pressure verification and comparison.

---

## 1.4 Total-contact redistribution is part of the mechanism

Kato et al. reported marked peak-pressure reduction together with increased contact area under custom orthoses [REF-CAD-030, pp. 115–118].

**Functional implication:** BiomechE-CAD should track not only local peak pressure but also:

```text
contact area
pressure-time integral
distribution to adjacent regions
```

where the acquisition system provides them.

---

## 1.5 Rigid relief concepts have quantitative support

The rigid relief orthosis study combined non-yielding local relief with total-contact fitting and measured significant pressure reduction at the first metatarsal head, while also reporting pressure changes at secondary sites [REF-CAD-031, pp. 115–122].

**Functional implication:** relief geometry and global supporting/contact geometry interact; a relief cannot be analysed in isolation.

---

## 1.6 “Donut”/ring relief is not intrinsically safe

In a pes-planus running study, a metatarsal dome reduced mean and peak pressure, a U-shaped pad reduced mean pressure, while a donut-shaped pad increased peak pressure compared with no pad [REF-CAD-032, pp. 71–85].

**Functional implication:** BiomechE-CAD must not treat `DONUT`/ring relief as an automatically safe primitive or default prescription.

---

## 1.7 Current guideline context

The IWGDF framework treats offloading as a context-specific clinical outcome in diabetic-foot prevention/treatment pathways [GUIDE-IWGDF-2023].

**Important product rule:** any numerical pressure target taken from a guideline must be attached to its population, protocol and clinical context; it must never become a global CAD threshold.

---

# 2. Functional taxonomy for BiomechE-CAD

BiomechE-CAD should not expose a single undifferentiated `Relief` operation.

Recommended clinical/design taxonomy:

```text
LocalRelief
Aperture
URelief
ChannelRelief
HeelSpurRelief
MetatarsalHeadRelief
HalluxRelief
CustomOffloadRegion
```

These are semantic feature types, not geometry-kernel primitives.

---

# 3. Required parameter model

Minimum shared model:

```text
OffloadFeature
  id
  side
  featureType

  targetAnatomy
  targetROI
  referenceLandmarks[]

  centerPosition_mm
  normalizedPosition
  orientation_deg

  width_mm
  length_mm
  radius_mm [when applicable]
  depth_mm / reliefHeight_mm

  edgeTransitionWidth_mm
  transitionProfile
  floorProfile

  supportMode
  materialRegionRef [optional]

  intendedMetric
  intendedDirection  // reduce/increase/redistribute
  evidenceContext

  author
  timestamp
  algorithmVersion
```

No parameter should silently inherit a literature-derived value as a universal default [REF-CAD-013; REF-CAD-041; REF-CAD-042].

---

# 4. Target ROI + safety-ring model

Every relief/offloading feature should define at least two analysis regions:

```text
TARGET ROI
  anatomical region intended for pressure reduction

SAFETY RING
  neighbouring region where transferred load is inspected
```

Optionally:

```text
GLOBAL FOOT MASK
```

for detecting remote load transfer [REF-CAD-004; REF-CAD-020; REF-CAD-029].

Suggested data object:

```text
OffloadAssessment
  baselineDataset
  postDesignDataset

  targetROI
  safetyRingROI
  comparisonRegions[]

  targetPeakPressure
  targetPTI
  targetContactArea

  ringPeakPressure
  ringPTI
  ringContactArea

  globalPeakPressure
  globalLoadDistribution

  comfortScore [optional]
  fitScore [optional]
```

---

# 5. Acceptance semantics — do not hardcode universal clinical thresholds

A relief feature is geometrically valid when its geometry satisfies design/manufacturing constraints.

A relief feature is **biomechanically verified** only when a defined measurement protocol reports the requested outcome. Threshold literature is heterogeneous and context-dependent [REF-CAD-037; REF-CAD-038; GUIDE-IWGDF-2023].

Generic acceptance structure:

```text
Target condition:
  target metric moves in requested direction
  and meets protocol-specific target if one is defined

Redistribution condition:
  surrounding-region metrics are measured and reported
  and do not violate protocol-specific safety limits

Manufacturing condition:
  minimum thickness / continuity / manufacturability remain valid

Usability condition:
  comfort / fit / adherence feedback can be attached when relevant
```

The software may warn:

```text
TARGET IMPROVED
BUT ADJACENT LOAD INCREASED
```

rather than reporting a simple green PASS.

---

# 6. Design rule: relief and material are independent variables

An offloading feature may be produced by one or more mechanisms:

```text
geometric depression
aperture/cut-out
local cushioning
local stiffness reduction
surrounding support increase
combination
```

Evidence that geometry and mechanical properties can both change outcomes supports keeping them separate [REF-CAD-008; REF-CAD-009; REF-CAD-010; REF-CAD-021].

Therefore the product model must keep separate:

```text
OffloadGeometry
MechanicalPropertyRegion
```

A future optimizer may combine them, but it must not collapse them into one opaque scalar.

---

# 7. Design rule: pressure outcome is not inferred from CAD height alone

Do not implement rules like:

```text
3 mm deeper relief = X% pressure reduction
```

unless a validated, population-specific model exists.

Current evidence supports individual variability and redistribution effects [REF-CAD-020; REF-CAD-029].

The CAD should therefore support:

```text
DESIGN PREDICTION [future / explicitly model-based]
vs
MEASURED OUTCOME [authoritative when available]
```

as separate data classes.

---

# 8. Proposed P0/P1 scope

## P0

- named local relief/offloading feature;
- anatomical ROI/landmark positioning;
- width/length/depth/transition parameters;
- target ROI + safety ring;
- visual/quantitative comparison hooks;
- min-thickness/manufacturing validation;
- full version/history traceability.

## P1

- guided offloading workflow from pressure map;
- automatic candidate ROI proposal;
- measured before/after pressure comparison UI;
- comfort/fit outcome integration;
- material/stiffness coupling presets.

## P2 / R&D

- automatic pressure-to-relief optimization;
- predictive surrogate model;
- FE-based tissue stress estimation;
- automatic multi-objective optimization including neighbouring load transfer and comfort.

---

# 9. New functional acceptance tests

## OFF-001 — target ROI semantics

A relief is attached to a named anatomical ROI and remains attached when the underlying template changes within supported limits.

## OFF-002 — explicit geometry dose

Width, length/radius, depth/height and edge-transition width are stored numerically with units.

## OFF-003 — safety ring

Every pressure-verification workflow automatically evaluates a surrounding region in addition to the target ROI [REF-CAD-029].

## OFF-004 — redistribution reporting

The software reports whether pressure reduction in the target is accompanied by increased load in adjacent or remote regions [REF-CAD-004; REF-CAD-020; REF-CAD-029].

## OFF-005 — no universal threshold leakage

A clinical pressure threshold can only be applied when its population/protocol/evidence context is attached [REF-CAD-037; REF-CAD-038; GUIDE-IWGDF-2023].

## OFF-006 — donut/ring not assumed beneficial

No relief primitive is labelled intrinsically therapeutic or safe without measurement/context [REF-CAD-032].

## OFF-007 — geometry/material separation

Changing local stiffness without changing geometry and changing geometry without changing stiffness are both independently representable [REF-CAD-009; REF-CAD-010].

## OFF-008 — manufacturing integrity

A local relief cannot silently violate minimum thickness or produce a non-manufacturable region [EC2-MANUAL-1.1, pp. 52–53; EC2-VAL-PLAN-1.4, US24].

## OFF-009 — outcome traceability

Measured outcome datasets identify the exact design and manufacturing revision.

---

# 10. Product conclusion

The functional abstraction should be:

```text
ANATOMICAL TARGET
      +
OFFLOAD INTENT
      +
GEOMETRIC / MATERIAL DOSE
      +
TARGET + SURROUNDING OUTCOME
      +
MANUFACTURING VALIDATION
```

not simply:

```text
lower surface here
```

This distinction should remain valid regardless of the future geometry engine.

---

## Bibliography links

[EC2-MANUAL-1.1]: ../BIBLIOGRAPHY.md#ec2-manual-11
[EC2-VAL-PLAN-1.4]: ../BIBLIOGRAPHY.md#ec2-val-plan-14
[GUIDE-IWGDF-2023]: ../BIBLIOGRAPHY.md#guide-iwgdf-2023
[REF-CAD-004]: ../BIBLIOGRAPHY.md#ref-cad-004
[REF-CAD-007]: ../BIBLIOGRAPHY.md#ref-cad-007
[REF-CAD-008]: ../BIBLIOGRAPHY.md#ref-cad-008
[REF-CAD-009]: ../BIBLIOGRAPHY.md#ref-cad-009
[REF-CAD-010]: ../BIBLIOGRAPHY.md#ref-cad-010
[REF-CAD-013]: ../BIBLIOGRAPHY.md#ref-cad-013
[REF-CAD-020]: ../BIBLIOGRAPHY.md#ref-cad-020
[REF-CAD-021]: ../BIBLIOGRAPHY.md#ref-cad-021
[REF-CAD-029]: ../BIBLIOGRAPHY.md#ref-cad-029
[REF-CAD-030]: ../BIBLIOGRAPHY.md#ref-cad-030
[REF-CAD-031]: ../BIBLIOGRAPHY.md#ref-cad-031
[REF-CAD-032]: ../BIBLIOGRAPHY.md#ref-cad-032
[REF-CAD-037]: ../BIBLIOGRAPHY.md#ref-cad-037
[REF-CAD-038]: ../BIBLIOGRAPHY.md#ref-cad-038
[REF-CAD-041]: ../BIBLIOGRAPHY.md#ref-cad-041
[REF-CAD-042]: ../BIBLIOGRAPHY.md#ref-cad-042
