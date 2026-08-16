# BiomechE-CAD — Analysis, Outcome Metrics, QC and DFM Functional Specification

**Version:** v1 — evidence-led frozen product contract  
**Date:** 2026-08-16  
**Status:** **FROZEN v1**  
**Architecture:** implementation-neutral.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is authoritative.  
**Authority boundary:** `11_biomeche_integration.md` owns BiomechE result provenance; `15_pressure_acquisition_qualification.md` owns acquisition qualification methodology; `16_geometry_authoring_contract.md` owns reproducible inspection definitions; `18_numerical_qualification_registry.md` owns all numeric authority classes and lifecycle.

---

## 0. Freeze rationale

This v1 freezes **what is measured, compared, qualified and reported**, not the implementation algorithm or a universal threshold. Current literature continues to show that plantar-pressure metrics are protocol/device dependent and that pressure improvement is not interchangeable with pain, function, comfort or manufacturing conformity. Manufacturing standards likewise support explicit inspection/acceptance requirements rather than a universal orthosis tolerance.

Frozen separation:

```text
GEOMETRIC QC
!= BIOMECHANICAL OUTCOME
!= ACQUISITION QUALITY
!= MANUFACTURING / DFM QC
```

and:

```text
algorithm numerical tolerance
!= device qualification limit
!= manufacturing acceptance limit
!= clinical/outcome interpretation rule
```

---

## 1. Purpose

Define what BiomechE-CAD must measure, compare and report when evaluating an orthosis design.

A design can be geometrically valid and still fail its intended pressure outcome. Conversely, an apparent pressure improvement can be unreliable if acquisition/calibration/protocol changed [REF-CAD-034; REF-CAD-036].

---

# 2. Core rule: metrics are always protocol-bound

No pressure number is meaningful without its acquisition context. Reliability and cross-system literature supports preserving device, calibration, walking speed, step count and protocol metadata [REF-CAD-034; REF-CAD-035; REF-CAD-036].

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

---

# 3. P0 plantar-loading metrics

## 3.1 Peak plantar pressure — P0

```text
PeakPressure
units: kPa
scope: sensor / ROI / foot
```

Peak plantar pressure is widely used in diabetic-foot offloading literature and guideline contexts [REF-CAD-004; REF-CAD-005; REF-CAD-037; GUIDE-IWGDF-2023].

Store per-step values, aggregate method and ROI definition. Do not store only a rendered maximum color.

## 3.2 Pressure-time integral — P0

```text
PTI = integral pressure(t) dt
units: kPa*s
```

PTI captures temporal exposure that peak pressure alone cannot represent. A systematic review found clear differences between PTI and peak-pressure results in 15 of 35 eligible diabetic-foot papers [REF-CAD-033, Abstract—Findings].

**Product rule:** do not claim PTI is universally superior to peak pressure. Report both where acquisition supports them.

## 3.3 Contact area — P0

```text
ContactArea
units: mm2 or cm2 with canonical conversion
```

Contact area is important for understanding redistribution/total-contact mechanisms [REF-CAD-030, pp. 115–118]. It should be available whole-foot, by anatomical ROI and before/after where the system can calculate it reliably.

## 3.4 Contact time — P0 when available

```text
ContactTime
units: s or % stance
```

Useful for contextualizing PTI and loading duration.

## 3.5 Mean / average pressure — P0 when well-defined

The exact definition must be stored because systems differ [REF-CAD-036]. Never use the label `mean pressure` without the computation definition.

---

# 4. Force metrics — P0/P1 depending on acquisition

If the device provides calibrated force or force can be validly derived from pressure × sensor area:

```text
PeakForce         N
ForceTimeIntegral N*s
RegionalLoadFraction %
```

Store derivation metadata. Do not fabricate force from a pressure image lacking calibrated sensor area/geometry.

---

# 5. Center of pressure — P1 quantitative feature

When source data support it:

```text
COP trajectory
COP path length
COP mediolateral displacement
COP anteroposterior progression
phase-specific COP metrics
```

Forefoot/rearfoot wedge literature shows that orthotic dose can alter COP trajectory [REF-CAD-015], making COP relevant to prescription analysis. The original time-series trajectory should remain available; derived scalar metrics are secondary.

---

# 6. Shear stress — P1/P2, never inferred silently

Mechanical plantar loading includes normal pressure plus tangential shear stress. Reviews support treating shear as a distinct quantity and document separate measurement technology and diabetic-foot relevance [REF-CAD-039; REF-CAD-040].

Therefore:

- support shear datasets when a validated device provides them;
- preserve shear units, axes, calibration and coordinate frame;
- do **not** estimate or label shear from pressure-only hardware unless an explicit validated predictive model is being used;
- model-derived shear is stored separately from measured shear.

---

# 7. Step-level data and aggregation policy

Do not reduce a walking trial immediately to one scalar.

```text
Trial
  Step[]
    regional metrics
  aggregate
  variability
```

Store/derive step count, aggregate method, dispersion and excluded steps. Protocol-specific evidence demonstrates that included step count affects reliability [REF-CAD-035; REF-CAD-108].

No universal fixed number of steps is hardcoded as clinically sufficient; protocol profiles define it.

---

# 8. Speed and activity are part of the result

Walking speed changes regional loading [REF-CAD-035]. Therefore a comparison engine must check activity, speed protocol, footwear and measurement-system compatibility.

If they differ, the UI should flag:

```text
COMPARISON HAS PROTOCOL DIFFERENCES
```

rather than silently computing a clinical delta.

---

# 9. Device comparability and calibration

Cross-system research reports discrepancies among plantar-pressure devices for contact area, force, FTI, peak pressure, PTI, mean pressure and contact time, with limited cross-system comparability [REF-CAD-036]. Technical assessment literature further supports explicit calibration/performance qualification [REF-CAD-109; REF-CAD-110].

Preferred longitudinal comparison:

```text
same qualified device + compatible calibration + compatible protocol
```

Cross-device comparisons require explicit provenance/warning and, if available, validated harmonization.

---

# 10. ROI model

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

For offloading features add target ROI, safety-ring ROI and comparison regions because local pressure reduction can redistribute load nearby or remotely [REF-CAD-004; REF-CAD-020; REF-CAD-029]. ROI versions/landmarks are part of provenance.

---

# 11. Before / after / delta analysis

Canonical comparison:

```text
BASELINE DATASET
        vs
OUTCOME DATASET
```

For each compatible metric/ROI report absolute baseline, absolute outcome, absolute delta, relative delta, protocol compatibility and quality state.

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

# 12. Threshold policy

Thresholds are **context objects**, not global constants:

```text
MetricThreshold
  authorityClass
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
  qualificationState
```

Systematic reviews identify multiple threshold schemes and substantial heterogeneity/limited evidence [REF-CAD-037; REF-CAD-038]. IWGDF diabetic-foot targets are therefore attached to their specific guideline context rather than applied automatically to other populations [GUIDE-IWGDF-2023].

All threshold lifecycle semantics defer to `18_numerical_qualification_registry.md`. `OPEN` remains `OPEN`.

---

# 13. Measurement vs prediction

Keep separate:

```text
MeasuredOutcome
PredictedOutcome
```

A future ML/FE/surrogate model may predict pressure/shear, but a predicted value must never overwrite a measured dataset.

Prediction should include model ID/version, training/validation provenance, uncertainty and applicability domain.

---

# 14. Geometric QC — P0

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

EasyCAD2 itself validates sections/measurements and minimum-thickness handling [EC2-MANUAL-1.1, pp. 42–44 and 52–53; EC2-VAL-PLAN-1.4, US19–US20/US24]. Prescription geometry should be verified against what is actually present in the final design/manufacturing artifact.

Each inspection definition must identify its reference frame/landmarks/ROI/method/version so it can be reproduced under `GAUTH`.

---

# 15. Manufacturing / DFM QC — P0

Minimum functional requirements:

```text
minimum thickness
invalid/degenerate geometry detection
orientation/unit sanity
closed/watertight artifact where process requires it
material/manufacturing profile compatibility
export revision/hash
```

Exact algorithms depend on future architecture/manufacturing choices.

Any numeric DFM limit is a `MANUFACTURING_ACCEPTANCE_LIMIT` or another explicit `NREG` authority class owned by a qualified ManufacturingProfile. It is not borrowed from algorithm epsilon or clinical evidence.

---

# 16. Quality state for each comparison

Canonical state model:

```text
VALID
VALID_WITH_WARNINGS
NOT_COMPARABLE
INSUFFICIENT_DATA
```

Warnings may include different pressure system/calibration, insufficient protocol evidence, different walking speed/footwear, changed ROI masking, missing units/side or sensor saturation/dropout [REF-CAD-034; REF-CAD-035; REF-CAD-036].

`NOT_COMPARABLE` is not converted to zero change. `INSUFFICIENT_DATA` is not success/failure.

---

# 17. Evidence basis summary

- Peak pressure + PTI: [REF-CAD-033].
- In-shoe measurement technology/provenance: [REF-CAD-034].
- Reliability / step count / speed: [REF-CAD-035; REF-CAD-108].
- Cross-system comparability: [REF-CAD-036].
- Device technical qualification: [REF-CAD-109; REF-CAD-110].
- Threshold uncertainty: [REF-CAD-037; REF-CAD-038].
- Shear: [REF-CAD-039; REF-CAD-040].
- Load transfer / safety ring: [REF-CAD-004; REF-CAD-020; REF-CAD-029; REF-CAD-030].

---

# 18. P0/P1/P2 summary

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

# 19. Functional acceptance tests

## AQ-001 — raw numeric authority
Pressure data remain numeric and metric; color maps are derived views.

## AQ-002 — protocol provenance
A pressure trial cannot be marked fully valid without units, side, device/source and acquisition protocol metadata required by its profile [REF-CAD-034; REF-CAD-036].

## AQ-003 — step-aware aggregation
The UI can show the number of included steps and the aggregate method [REF-CAD-035].

## AQ-004 — peak + PTI
When time-series pressure is available, both peak pressure and PTI can be computed by ROI [REF-CAD-033].

## AQ-005 — contact area
Contact area can be compared by compatible ROI where supported [REF-CAD-030].

## AQ-006 — compatibility warning
Changing device, calibration, speed/activity or masking rules produces an explicit comparison warning [REF-CAD-034; REF-CAD-035; REF-CAD-036].

## AQ-007 — target + safety ring
Offloading assessment displays target and surrounding-region deltas [REF-CAD-029].

## AQ-008 — contextual threshold
A threshold cannot exist without context/provenance/authority fields [REF-CAD-037; REF-CAD-038; GUIDE-IWGDF-2023].

## AQ-009 — measured/predicted separation
Predicted outcome cannot be presented or serialized as measured outcome.

## AQ-010 — geometry-to-artifact verification
Requested prescription values such as wedge angle and element placement can be measured on the final design/artifact by a reproducible inspection definition.

---

# 20. Frozen invariants

```text
pressure heatmap != numeric source
metric value != metric definition
local improvement != global success
measured != predicted
acquisition quality != clinical outcome
clinical threshold != manufacturing tolerance
manufacturing tolerance != algorithm epsilon
NOT_COMPARABLE != zero delta
```

---

# 21. Product conclusion

BiomechE-CAD should not ask only:

```text
Did peak pressure decrease?
```

It should ask:

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
Which authority owns each threshold/tolerance?
```

That evidence model is independent of the geometry engine.

---

## Bibliography links

[EC2-MANUAL-1.1]: ../BIBLIOGRAPHY.md#ec2-manual-11
[EC2-VAL-PLAN-1.4]: ../BIBLIOGRAPHY.md#ec2-val-plan-14
[GUIDE-IWGDF-2023]: ../BIBLIOGRAPHY.md#guide-iwgdf-2023
[REF-CAD-004]: ../BIBLIOGRAPHY.md#ref-cad-004
[REF-CAD-015]: ../BIBLIOGRAPHY.md#ref-cad-015
[REF-CAD-020]: ../BIBLIOGRAPHY.md#ref-cad-020
[REF-CAD-029]: ../BIBLIOGRAPHY.md#ref-cad-029
[REF-CAD-030]: ../BIBLIOGRAPHY.md#ref-cad-030
[REF-CAD-033]: ../BIBLIOGRAPHY.md#ref-cad-033
[REF-CAD-034]: ../BIBLIOGRAPHY.md#ref-cad-034
[REF-CAD-035]: ../BIBLIOGRAPHY.md#ref-cad-035
[REF-CAD-036]: ../BIBLIOGRAPHY.md#ref-cad-036
[REF-CAD-037]: ../BIBLIOGRAPHY.md#ref-cad-037
[REF-CAD-038]: ../BIBLIOGRAPHY.md#ref-cad-038
[REF-CAD-039]: ../BIBLIOGRAPHY.md#ref-cad-039
[REF-CAD-040]: ../BIBLIOGRAPHY.md#ref-cad-040
[REF-CAD-108]: ../BIBLIOGRAPHY.md#ref-cad-108
[REF-CAD-109]: ../BIBLIOGRAPHY.md#ref-cad-109
[REF-CAD-110]: ../BIBLIOGRAPHY.md#ref-cad-110
