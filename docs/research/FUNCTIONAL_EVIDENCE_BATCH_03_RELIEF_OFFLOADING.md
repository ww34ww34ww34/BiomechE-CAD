# BiomechE-CAD — Functional Evidence Batch 03: Relief, Aperture and Offloading

**Date:** 2026-08-14  
**Status:** research input to `FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md`  
**Architecture:** intentionally out of scope / parked.

---

## 0. Why this batch matters

For BiomechE-CAD, a local `relief`, `aperture`, `cut-out`, `depression` or other offloading feature must not be treated as a purely geometric indentation.

The literature consistently shows that plantar offloading is a **load-redistribution problem**:

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

**Footwear and insole design features for offloading the diabetic at risk foot — systematic review and meta-analyses**  
PMID: `33532602`  
URL: https://pubmed.ncbi.nlm.nih.gov/33532602/

Key product-relevant findings:

- 54 studies were included.
- Arch profile, metatarsal additions and pressure-informed design showed significant peak-pressure reductions in meta-analysis.
- The review specifically reports that **apertures** can reduce plantar pressure.
- The authors emphasize heterogeneity and recommend pressure analysis to improve and modify insole/footwear design.

**Functional implication:** support aperture/relief features, but do not encode a single geometry as universally optimal.

---

## 1.2 Local pressure reduction can create adjacent overload

**The effect of calcaneus and metatarsal head offloading insoles on gait and plantar pressure — pilot study, 2024**  
PMID: `38758937`  
URL: https://pubmed.ncbi.nlm.nih.gov/38758937/

The tested offloading insoles reduced peak pressure and pressure-time integral in the target ROI, but load was transferred to surrounding regions; the authors explicitly note the potential for increased pressure-time integral in neighbouring locations.

**Functional implication:** every offloading evaluation must include an automatically generated **surrounding safety region** rather than reporting only the target ROI.

---

## 1.3 Pressure redistribution is strongly patient-specific

**Pressure relief and load redistribution by custom-made insoles in diabetic patients with neuropathy and foot deformity**  
PMID: `15234488`  
URL: https://pubmed.ncbi.nlm.nih.gov/15234488/

In the analysed high-risk first-metatarsal-head feet:

- some had substantial reduction;
- some had intermediate reduction;
- others did not achieve adequate offloading;
- load was transferred toward the medial midfoot.

**Functional implication:** a CAD feature cannot be labelled successful from geometry alone. The project model should allow post-design pressure verification and comparison.

---

## 1.4 Total-contact redistribution is part of the mechanism

**The reduction and redistribution of plantar pressures using foot orthoses in diabetic patients**  
PMID: `8792110`  
URL: https://pubmed.ncbi.nlm.nih.gov/8792110/

The custom orthoses in this study substantially reduced peak plantar pressure while increasing contact area.

**Functional implication:** BiomechE-CAD should track not only local peak pressure but also:

```text
contact area
pressure-time integral
distribution to adjacent regions
```

where the acquisition system provides them.

---

## 1.5 Rigid relief concepts have quantitative support

**Reduction of plantar pressure with the rigid relief orthosis**  
PMID: `8468692`  
URL: https://pubmed.ncbi.nlm.nih.gov/8468692/

The rigid relief orthosis combined a non-yielding local relief beneath a vulnerable site with total-contact fitting and showed significant pressure reduction at the first metatarsal head, with pressure changes at secondary regions as well.

**Functional implication:** relief geometry and global supporting/contact geometry interact; a relief cannot be analysed in isolation.

---

## 1.6 “Donut”/ring relief is not intrinsically safe

**The effect of 3 foot pads on plantar pressure of pes planus foot type**  
PMID: `20231746`  
DOI: `10.1123/jsr.19.1.71`  
URL: https://pubmed.ncbi.nlm.nih.gov/20231746/

In the tested group during slow running:

- a metatarsal dome reduced peak and mean pressure;
- a U-shaped pad reduced mean pressure;
- a donut-shaped pad **increased peak plantar pressure** compared with no pad.

**Functional implication:** BiomechE-CAD must not treat `DONUT`/ring relief as an automatically safe primitive or default prescription.

---

## 1.7 Current guideline context

**IWGDF Guidelines 2023 — Prevention and Offloading**  
Official source: https://iwgdfguidelines.org/guidelines-2023/

The current IWGDF framework treats offloading as an outcome that must be demonstrated in defined diabetic-foot contexts and supports therapeutic footwear/insoles as part of prevention and treatment pathways.

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

No parameter should silently inherit a literature-derived value as a universal default.

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

for detecting remote load transfer.

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

A relief feature is **biomechanically verified** only when a defined measurement protocol reports the requested outcome.

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

Current evidence supports individual variability and redistribution effects.

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

Every pressure-verification workflow automatically evaluates a surrounding region in addition to the target ROI.

## OFF-004 — redistribution reporting

The software reports whether pressure reduction in the target is accompanied by increased load in adjacent or remote regions.

## OFF-005 — no universal threshold leakage

A clinical pressure threshold can only be applied when its population/protocol/evidence context is attached.

## OFF-006 — donut/ring not assumed beneficial

No relief primitive is labelled intrinsically therapeutic or safe without measurement/context.

## OFF-007 — geometry/material separation

Changing local stiffness without changing geometry and changing geometry without changing stiffness are both independently representable.

## OFF-008 — manufacturing integrity

A local relief cannot silently violate minimum thickness or produce a non-manufacturable region.

## OFF-009 — outcome traceability

Measured outcome datasets identify the exact design and manufacturing revision used.

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
