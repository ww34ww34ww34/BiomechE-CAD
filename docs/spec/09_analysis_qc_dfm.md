# BiomechE-CAD — Analysis, Outcome Metrics, QC and DFM Functional Specification

**Version:** v0 — evidence-led metric policy  
**Date:** 2026-08-14  
**Status:** active functional baseline  
**Architecture:** out of scope / parked.

---

## 0. Purpose

Define what BiomechE-CAD must measure, compare and report when evaluating an orthosis design.

This specification deliberately distinguishes:

```text
GEOMETRIC QC
BIOMECHANICAL OUTCOME
ACQUISITION QUALITY
MANUFACTURING / DFM QC
```

A design can be geometrically valid and still fail its intended pressure outcome. Conversely, an apparent pressure improvement can be unreliable if acquisition/calibration/protocol changed.

---

# 1. Core rule: metrics are always protocol-bound

No pressure number is meaningful without its acquisition context.

Every outcome dataset must preserve at least:

```text
PressureAcquisition
  sourceDevice
  deviceSerial/model [when available]
  sensorTechnology
  calibrationId / calibrationDate
  units
  sampleRate_Hz

  inShoe_or_platform
  footwear
  orthosisRevision
  manufacturingRevision

  subjectSide
  timestamp
  walkingSurface
  walkingSpeed / speedProtocol
  activity
  numberOfSteps

  regionMaskVersion
  operator
  qualityFlags
```

Rationale: published reliability studies show that walking speed, number of steps and calibration affect plantar-pressure measurements; cross-system studies also show that values from different devices are not automatically interchangeable.

---

# 2. P0 plantar-loading metrics

## 2.1 Peak plantar pressure — P0

```text
PeakPressure
units: kPa
scope: sensor / ROI / foot
```

Peak plantar pressure is widely used and is the principal quantitative metric in diabetic-foot offloading literature/guidelines.

Store:

```text
per-step values
aggregate
aggregation method
ROI definition
```

Do not store only a rendered maximum color.

---

## 2.2 Pressure-time integral — P0

```text
PTI = integral pressure(t) dt
units: kPa*s
```

PTI captures temporal exposure that peak pressure alone cannot represent.

A systematic review found that PTI and peak-pressure conclusions differ clearly in a meaningful subset of diabetic-foot studies; PTI should therefore be available rather than discarded.

**Product rule:** do not claim PTI is universally superior to peak pressure. Report both where the acquisition supports them.

---

## 2.3 Contact area — P0

```text
ContactArea
units: mm2 or cm2 with canonical conversion
```

Contact area is important for understanding redistribution/total-contact mechanisms.

It should be available:

```text
whole foot
anatomical ROI
before/after
```

when the pressure system can calculate it reliably.

---

## 2.4 Contact time — P0 when available

```text
ContactTime
units: s or % stance
```

Useful for contextualizing PTI and loading duration.

---

## 2.5 Mean / average pressure — P0 when well-defined

The exact definition must be stored because systems differ.

Examples:

```text
mean across active sensors at instant
mean peak pressure across steps
regional average pressure over stance
```

Never use the label `mean pressure` without the computation definition.

---

# 3. Force metrics — P0/P1 depending on acquisition

If the device provides calibrated force or force can be validly derived from pressure × sensor area:

```text
PeakForce        N
ForceTimeIntegral N*s
RegionalLoadFraction %
```

Store derivation metadata.

Do not fabricate force from a pressure image lacking calibrated sensor area/geometry.

---

# 4. Center of pressure — P1 quantitative feature

When source data support it:

```text
COP trajectory
COP path length
COP mediolateral displacement
COP anteroposterior progression
phase-specific COP metrics
```

Forefoot/rearfoot wedge literature shows that orthotic dose can alter COP trajectory, making COP relevant to prescription analysis.

The original time-series trajectory should remain available; derived scalar metrics are secondary.

---

# 5. Shear stress — P1/P2, never inferred silently

Mechanical plantar loading includes:

```text
normal pressure
+
tangential shear stress
```

Reviews identify shear as potentially important to diabetic foot tissue injury, but shear measurement technology is less common and less standardized than normal plantar pressure.

Therefore:

- support shear datasets when a validated device provides them;
- preserve shear units, axes, calibration and coordinate frame;
- do **not** estimate or label shear from pressure-only hardware unless an explicit validated predictive model is being used;
- model-derived shear is stored separately from measured shear.

---

# 6. Step-level data and aggregation policy

Do not reduce a walking trial immediately to one scalar.

Minimum conceptual model:

```text
Trial
  Step[]
    regional metrics
  aggregate
  variability
```

Store or derive:

```text
step count
mean
median [recommended]
standard deviation / dispersion
min/max when useful
excluded steps + reason
```

Reliability literature indicates that multiple steps are required for stable estimates and that required step count varies by metric/region.

No universal fixed number of steps is hardcoded as clinically sufficient; protocol profiles define it.

---

# 7. Speed and activity are part of the result

Published reliability work shows plantar loading changes with gait speed.

Therefore a comparison engine must check:

```text
activity same?
walking/running speed protocol comparable?
footwear comparable?
measurement system comparable?
```

If not, the UI should flag:

```text
COMPARISON HAS PROTOCOL DIFFERENCES
```

rather than silently computing a clinical delta.

---

# 8. Device comparability and calibration

Recent cross-system research reports discrepancies between plantar-pressure systems for parameters including pressure, force, PTI, FTI, contact area and contact time.

Therefore:

```text
same device + same calibration + same protocol
```

is the preferred longitudinal comparison.

Cross-device comparisons are allowed only with explicit provenance/warning and, if available, a validated harmonization/calibration process.

Threshold-based decisions require stronger acquisition-quality checks than simple relative ranking.

---

# 9. ROI model

Every pressure metric must identify its mask/region definition.

Support at least:

```text
whole foot
heel
medial heel
lateral heel
midfoot
medial midfoot
lateral midfoot
MTH1
MTH2
MTH3
MTH4
MTH5
hallux
lesser toes
custom polygon/semantic ROI
```

For offloading features add:

```text
targetROI
safetyRingROI
comparisonROI[]
```

ROI versions/landmarks are part of provenance.

---

# 10. Before / after / delta analysis

Canonical comparison:

```text
BASELINE DATASET
        vs
OUTCOME DATASET
```

For each compatible metric/ROI report:

```text
absolute baseline
absolute outcome
absolute delta
relative delta %
measurement protocol compatibility
quality state
```

Example:

```text
MTH2-4 PeakPressure
Baseline: 310 kPa
Outcome: 225 kPa
Delta: -85 kPa
Relative: -27.4%
Protocol: comparable
```

The example is illustrative and not a clinical threshold.

---

# 11. Threshold policy

Thresholds are **context objects**, not global constants.

```text
MetricThreshold
  population
  indication
  metric
  ROI
  thresholdType
  value
  units
  baselineDefinition
  measurementProtocol
  evidenceReference
  evidenceVersion/date
```

This is required because systematic reviews of diabetic in-shoe pressure thresholds report heterogeneous proposed cutoffs and limited evidence for several threshold schemes.

The IWGDF diabetic-foot context may define pressure-relief targets, but those targets must not apply automatically to metatarsalgia, flatfoot, sport or asymptomatic populations.

---

# 12. Measurement vs prediction

Keep separate:

```text
MeasuredOutcome
PredictedOutcome
```

A future ML/FE/surrogate model may predict pressure/shear, but a predicted value must never overwrite a measured dataset.

Prediction should include:

```text
modelId
modelVersion
training/validation provenance
uncertainty
applicability domain
```

---

# 13. Geometric QC — P0

Independent of pressure data, BiomechE-CAD requires measurable geometry checks:

```text
length
width
local/global height
arch height
heel cup height
wedge/post angle
corrective-element position
corrective-element height/size
section profile
local thickness
minimum thickness
```

Prescription geometry should be verified against what is actually present in the final design/manufacturing artifact.

---

# 14. Manufacturing / DFM QC — P0

Minimum functional requirements:

```text
minimum thickness
invalid/degenerate geometry detection
orientation/unit sanity
closed/watertight artifact where process requires it
material/manufacturing profile compatibility
export revision/hash
```

Exact algorithms depend on future architecture/manufacturing choices and are not specified here.

---

# 15. Quality state for each comparison

Suggested state model:

```text
VALID
VALID_WITH_WARNINGS
NOT_COMPARABLE
INSUFFICIENT_DATA
```

Warnings may include:

```text
different pressure system
different calibration
insufficient steps
different walking speed
different footwear
changed ROI/masking version
missing units
missing side
sensor saturation/dropout
```

---

# 16. Evidence basis

## Pressure + PTI

**The value of reporting pressure-time integral data in addition to peak pressure data in studies on the diabetic foot: a systematic review**  
PMID `23273847`  
DOI `10.1016/j.clinbiomech.2012.12.002`

Supports retaining PTI in addition to peak pressure; differences between the two measures were present in a meaningful subset of studies.

## Pressure measurement technology

**In-shoe plantar pressure measurement technologies for the diabetic foot: a systematic review**, 2024  
PMID `38699042`  
DOI `10.1016/j.heliyon.2024.e29672`

Supports device/protocol/calibration provenance and recognizes instrumented insoles as the prevailing in-shoe approach.

## Reliability / step count / speed

**Reliability of an in-shoe pressure measurement system during treadmill walking**  
PMID `8696496`  
DOI `10.1177/107110079601700404`

Shows loading metrics vary with speed and multiple steps may be needed for high reliability.

## Cross-system comparability

**Discrepancies between plantar pressure devices: Evaluating cross-system reliability for biomechanics, clinical use and predictive modelling**  
PMID `40743570`  
DOI `10.1016/j.foot.2025.102190`

Supports warnings against treating values from different measurement systems as directly interchangeable.

## Threshold uncertainty

**In-shoe pressure thresholds for people with diabetes and neuropathy at risk of ulceration: A systematic review**  
PMID `33280984`.

**Plantar pressure thresholds as a strategy to prevent diabetic foot ulcers: A systematic review**  
PMID `38390156`.

Both report heterogeneous thresholds/protocols and limited evidence for several proposed thresholds.

## Shear

**Plantar shear stress measurements — A review**  
PMID `24820135`  
DOI `10.1016/j.clinbiomech.2014.04.009`

**Plantar shear stress in the diabetic foot: A systematic review and meta-analysis**  
PMID `34324731`  
DOI `10.1111/dme.14661`

Support treating shear as a distinct mechanical quantity, not as a synonym for pressure.

---

# 17. P0/P1/P2 summary

## P0

```text
PeakPressure
PTI
ContactArea
ContactTime when available
MeanPressure with explicit definition
Force/FTI when source supports it
trial + step provenance
ROI/versioning
before/after/delta
protocol compatibility
context-specific thresholds
geometric QC
basic DFM QC
```

## P1

```text
COP trajectory/derived metrics
shear import/analysis when measured
advanced quality scoring
population/protocol profiles
comfort/fit/adherence outcomes
pressure-guided design assistant
```

## P2 / R&D

```text
predicted pressure/shear
automatic optimization
cross-device harmonization models
FE tissue stress
longitudinal risk prediction
```

---

# 18. Functional acceptance tests

## AQ-001 — raw numeric authority

Pressure data remain numeric and metric; color maps are derived views.

## AQ-002 — protocol provenance

A pressure trial cannot be marked fully valid without units, side, device/source and acquisition protocol metadata required by its profile.

## AQ-003 — step-aware aggregation

The UI can show the number of included steps and the aggregate method.

## AQ-004 — peak + PTI

When time-series pressure is available, both peak pressure and PTI can be computed by ROI.

## AQ-005 — contact area

Contact area can be compared by compatible ROI where supported.

## AQ-006 — compatibility warning

Changing device, calibration, speed/activity or masking rules produces an explicit comparison warning.

## AQ-007 — target + safety ring

Offloading assessment displays target and surrounding-region deltas.

## AQ-008 — contextual threshold

A threshold cannot exist without context/provenance fields.

## AQ-009 — measured/predicted separation

Predicted outcome cannot be presented or serialized as measured outcome.

## AQ-010 — geometry-to-artifact verification

Requested prescription values such as wedge angle and element placement can be measured on the final design/artifact.

---

# 19. Product conclusion

BiomechE-CAD should not ask only:

```text
Did peak pressure decrease?
```

It should be able to ask:

```text
Where?
By how much?
For how long?
What happened nearby?
Under which protocol?
On which device/calibration?
Across how many steps?
Was contact redistributed?
Did geometry match prescription?
Was the produced artifact the revision actually tested?
```

That evidence model is independent of the geometry engine and is therefore appropriate to freeze before architecture selection.
