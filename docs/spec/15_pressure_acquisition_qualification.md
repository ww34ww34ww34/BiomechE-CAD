# 15 — Pressure Acquisition Qualification

**Status:** FROZEN methodological baseline v1  
**Date:** 2026-08-15  
**Scope:** qualification contract for plantar-pressure acquisition systems/protocols consumed by BiomechE and BiomechE-CAD.  
**Depends on:** Coordinate/Registration v1, BiomechE Integration v1, Analysis/QC v0, Project Schema v0.  

> This specification freezes **what must be qualified and preserved**, not universal numeric performance thresholds. Device/protocol-specific acceptance limits remain owned by a versioned qualification profile backed by bench/human evidence.

---

## 1. Why a dedicated qualification contract is required

Plantar-pressure results are not defined by the sensor matrix alone. Technical performance, calibration, protocol, region, parameter and population can all affect reliability and comparability.

Relevant evidence already captured in the canonical bibliography shows that:

- device technology, calibration, accuracy, hysteresis, creep and COP performance matter to pressure-system suitability [REF-CAD-109, pp.141–144; Abstract];
- hardware performance should be assessed with dedicated methods rather than assumed from vendor nominal specifications [REF-CAD-110, pp.158–167; Abstract];
- the number of included steps can materially affect regional in-shoe pressure reliability in a specific protocol/population, but the published 12-step result is context-specific rather than universal [REF-CAD-108, pp.880–884; Abstract—Methods/Findings/Interpretation];
- cross-system pressure, force and temporal outputs are not automatically interchangeable [REF-CAD-036, Abstract—Methods/Results/Conclusions];
- pressure-system selection and calibration remain tightly linked to intended clinical/biomechanical use [REF-CAD-034, Abstract—Methods/Results/Conclusion].

Therefore BiomechE-CAD SHALL NOT encode a single hidden `pressure_device_is_valid = true` flag detached from the actual exam/profile.

---

## 2. Qualification object

Conceptual P0 object:

```text
PressureAcquisitionQualificationProfile
  profileId
  version
  contentHash
  status

  intendedUse
  supportedExamTypes[]
  supportedOutcomeFamilies[]
  populationOrUseBoundaries[]

  deviceDefinition
  sensorGeometryDefinition
  acquisitionFirmwareSoftware

  calibrationProtocol
  benchQualification
  protocolQualification
  longitudinalQualification
  crossDevicePolicy

  acceptanceRules[]
  knownLimitations[]
  evidenceRefs[]
  qualificationArtifacts[]

  qualifiedAt
  qualifiedBy
  reviewOrExpiryPolicy
```

The exact storage class may evolve; the semantics above are frozen.

The profile SHALL be referenced by exact `id + version + content hash/snapshot`, never `latest` implicitly.

---

## 3. Intended-use first

A qualification is valid only inside its declared use domain.

At minimum state:

```text
STATIC_LOAD
STABILOMETRY
GAIT_OVERGROUND
GAIT_TREADMILL
IN_SHOE_WALK
IN_SHOE_RUN
other named functional protocols
```

and which result families are qualified, for example:

```text
mean/peak pressure
force
contact area
pressure-time integral
force-time integral
COP
regional pressure
spatiotemporal contact data
```

A system qualified for static load is not automatically qualified for dynamic peak-pressure, COP or stabilometry merely because the same hardware is used.

---

## 4. Device identity

A qualified acquisition SHALL resolve the exact device context, including where applicable:

```text
manufacturer
product family
model
hardware revision
serial number or unit identity
sensor technology
active area
sensor/cell count
nominal spatial arrangement
ADC/value representation
nominal pressure/force range
firmware version
acquisition-software version
transport mode
```

Vendor specifications are input evidence, not proof of achieved qualification performance.

If two nominally identical units show materially different qualification behavior, qualification may be unit-specific rather than model-wide.

---

## 5. Physical sensor geometry

Qualification preserves actual metric sensor geometry rather than relying on raster dimensions.

For every active pressure element:

```text
metric center position [mm]
represented physical area [mm²]
logical index mapping
masked/dead-cell state
```

For a regular grid, pitch/active-area semantics SHALL be explicit.

The same matrix dimensions with a different physical pitch are not equivalent geometry.

---

## 6. Calibration qualification

The calibration profile SHALL identify:

```text
calibration method
reference instrument/load source
traceability of reference when applicable
load/pressure points
loading/unloading sequence
preconditioning
temperature/humidity conditions where relevant
sensor warm-up requirements
calibration coefficients/model
calibration date
operator/tool/software
acceptance result
```

Qualification SHALL characterize, where relevant to the technology/use:

```text
zero offset / zero drift
sensitivity / gain
linearity
accuracy / error versus reference
repeatability
hysteresis
creep / relaxation
saturation / clipping
sensor-to-sensor variability
calibration drift over time/use
```

No Shore-like or generic vendor quality label substitutes for these measured device characteristics.

---

## 7. Force-closure check

For normal-pressure systems with known represented area, the qualification harness SHOULD include a force-closure comparison:

```text
F_pressure = Σ pressure_i * represented_area_i
```

with correct unit conversion.

Compare against an independent reference load/force measurement when available.

The acceptance limit is profile-specific.

This check can expose:

```text
scale/calibration error
sensor-area error
saturation
inactive cells
mapping defects
unit conversion error
```

It does not by itself qualify regional pressure accuracy.

---

## 8. COP qualification

COP qualification is separate from pressure-amplitude qualification.

Evaluate at minimum where the intended use requires COP:

```text
static known-load location accuracy
repeatability
path/trajectory behavior for moving reference loads where feasible
edge effects
load-dependence
missing/dead sensor effects
coordinate-frame correctness
```

COP errors SHALL be reported in physical units in the declared frame.

A visually smooth COP trace is not evidence of spatial accuracy.

---

## 9. Temporal qualification

Where dynamic/stabilometric outcomes are intended, preserve/qualify:

```text
nominal sampling rate
measured/effective sampling behavior
timestamp source
monotonicity
jitter
frame drops
duplicate timestamps
transport buffering/latency where relevant
synchronization error versus external channels where used
```

A high advertised frame rate does not by itself prove timing accuracy or suitability for a named dynamic KPI.

The required temporal performance is exam/outcome specific.

---

## 10. Spatial-resolution and sensor-density policy

BiomechE-CAD SHALL NOT hard-code one universal `minimum sensors/cm²` or cell width as scientific truth.

Qualification records:

```text
physical sensor pitch/area
effective resolution
interpolation/resampling policy
ROI size relative to sensor geometry
edge/partial-cell policy
```

and then validates the intended KPI/ROI performance empirically or against an accepted test method.

A platform may be adequate for total force while inadequate for a small local ROI; qualification is metric- and task-specific.

---

## 11. Dynamic protocol qualification

For dynamic walking/running protocols, freeze at least:

```text
approach protocol
walking/running speed policy
barefoot vs footwear/in-shoe context
number of accepted passes/contacts/steps
left/right requirements
steady-state or acceleration rules
contact inclusion/exclusion criteria
partial-foot/edge-hit rejection
trial aggregation method
outlier policy
repeat-on-failure rule
```

The number of accepted steps is profile-specific.

`REF-CAD-108` demonstrates why this field matters; it does not authorize a universal 12-step requirement.

---

## 12. Static protocol qualification

For static load:

```text
stance instruction
foot placement/orientation policy
visual target / eyes-open-closed state if relevant
settling period
measurement window duration
minimum total load
left/right assignment method
repeat count
window aggregation
```

shall be explicit and versioned.

Static pressure and stabilometry are separate intended uses even if captured in one standing session.

---

## 13. Stabilometry-specific qualification

If the same platform is used for posturography/stabilometry, qualify separately:

```text
COP spatial noise floor
COP drift
stationary-load stability
sampling/timing behavior
filter profile
analysis-window duration
coordinate orientation
external synchronization if used
```

A pressure profile qualified for foot-region peak pressure does not automatically qualify sway-spectrum or path-length outcomes.

---

## 14. In-shoe-specific qualification

In-shoe systems introduce additional factors:

```text
insole size/fit
sensor location relative to anatomy
wrinkling/folding
footwear interaction
preload
cable/wireless effects
sensor migration
temperature/sweat effects where relevant
repeated-use drift
shoe-specific calibration/applicability
```

Comparisons between platform barefoot pressure and in-shoe shod pressure require explicit compatibility policy; they are not direct substitutes.

---

## 15. Human repeatability / reproducibility qualification

Bench performance is necessary but not sufficient for a protocol that produces human outcome metrics.

A protocol qualification SHOULD estimate, as appropriate:

```text
within-trial variability
within-session repeatability
between-session repeatability
operator/repositioning effect
region-specific variability
metric-specific variability
```

Reported statistics may include:

```text
ICC
coefficient of variation
standard error of measurement
repeatability coefficient
Bland-Altman bias/limits where appropriate
```

The statistical method and acceptance criterion belong to the profile and intended decision.

A single global ICC for the whole device SHALL NOT silently qualify every ROI/metric.

---

## 16. Acceptance limits are profile-owned

A qualified profile contains explicit acceptance rules such as:

```text
metric
condition / test point
reference method
statistic
lower/upper limit
severity
rationale/evidence
```

Possible severities:

```text
BLOCKING
WARNING
INFORMATIONAL
```

Examples of *classes* of limits, not frozen values:

```text
force-scale error
COP positional error
repeatability CV
saturation count
dead-sensor count
sampling jitter
frame-loss rate
minimum valid steps
maximum edge-clipping fraction
```

This document intentionally supplies no universal numeric thresholds.

---

## 17. Quality state during routine acquisition

Qualification defines how runtime acquisition maps defects to:

```text
VALID
DEGRADED
UNAVAILABLE
```

Examples:

```text
calibration expired
insufficient valid steps
edge-clipped footprint
sensor saturation
excessive missing cells
timestamp discontinuity
unsupported firmware
wrong device/profile pairing
unresolved side
force-closure failure
```

`DEGRADED` remains quantitative only when the profile explicitly allows the affected KPI to survive with warnings.

`UNAVAILABLE` never becomes zero.

---

## 18. Calibration lifecycle

The profile SHALL define at least one of:

```text
calendar-based recalibration interval
usage/cycle-based interval
pre-session verification
reference-load quick check
condition-triggered recalibration
```

and events that invalidate or suspend qualification, for example:

```text
sensor repair/replacement
firmware change
major software acquisition-path change
mechanical damage
failed verification
transport/storage event outside qualified conditions
```

A recalibration creates new provenance; it does not rewrite old acquisitions.

---

## 19. Software/firmware change control

Qualification SHALL declare whether each version change is:

```text
NO_IMPACT
REQUIRES_REGRESSION
REQUIRES_PARTIAL_REQUALIFICATION
REQUIRES_FULL_REQUALIFICATION
```

for relevant acquisition semantics.

Examples requiring review:

```text
ADC scaling
sensor calibration model
sample-rate/timestamp path
filtering
contact detection
automatic masking
interpolation
device geometry table
```

UI-only changes do not automatically require hardware requalification, but they may still require reporting/visual regression tests.

---

## 20. Cross-device comparability

Default policy:

```text
same metric name + same unit
DOES NOT imply
cross-device comparability
```

A cross-device comparison requires one of:

```text
A) explicit evidence that the product profile accepts the difference;
B) validated harmonization/calibration with provenance;
C) comparison state VALID_WITH_WARNINGS under a named policy;
D) otherwise NOT_COMPARABLE.
```

This is directly motivated by published cross-system discrepancies [REF-CAD-036, Abstract—Methods/Results/Conclusions].

---

## 21. Qualification artifact set

A completed qualification package SHOULD preserve immutable/hash-addressed artifacts such as:

```text
bench raw data
reference-instrument data
calibration logs
analysis scripts/build IDs
human protocol data where used
statistical output
plots/reports
hardware/firmware/software manifest
final profile JSON/snapshot
review/approval record
```

The report is not the sole evidence; raw qualification evidence remains available.

---

## 22. Project/acquisition linkage

Every routine `PRESSURE` or pressure-bearing `BIOMECHE_RESULT` acquisition used for a qualified comparison SHOULD resolve:

```text
qualificationProfileRef
calibrationRef
actual device/unit identity
actual acquisition software/firmware
protocolRef
quality state
```

If the actual combination is outside the profile applicability domain, the result is not silently marked qualified.

---

## 23. First Sensor Medica / BiomechE qualification direction

The initial product-specific work should target the actual Sensor Medica pressure-acquisition systems used by BiomechE, one physical/device family at a time.

Do **not** create a generic `SensorMedicaPressureProfile` spanning every freeMed, treadmill or in-shoe system.

Recommended order:

```text
1. identify exact platform model + hardware revision + serial/unit
2. capture authoritative datasheet/service/calibration information
3. freeze SensorGeometry mapping and device raw->physical conversion
4. bench qualification
5. static-load protocol qualification
6. dynamic overground protocol qualification
7. stabilometry qualification if required
8. cross-device work only when a real product workflow needs it
```

Exact product specs and acceptance limits remain OPEN until the concrete hardware/datasheet/test setup is identified and measured.

---

## 24. Acceptance family — `PAQ-*`

### `PAQ-001` — exact qualification-profile identity
Acquisition resolves exact profile `id + version + hash/snapshot`.

### `PAQ-002` — intended-use boundary
A profile cannot qualify an exam/outcome family outside its declared scope.

### `PAQ-003` — exact device/unit identity
Runtime acquisition resolves model/revision and unit identity when qualification is unit-specific.

### `PAQ-004` — physical SensorGeometry exactness
Logical sensor indices resolve the qualified metric positions/represented areas.

### `PAQ-005` — calibration provenance
Calibration method/reference/date/version are preserved.

### `PAQ-006` — force-closure evidence
Where configured, pressure-derived force and reference force meet the profile-specific acceptance rule.

### `PAQ-007` — saturation/dead-cell gate
Runtime defects produce the profile-defined VALID/DEGRADED/UNAVAILABLE state.

### `PAQ-008` — COP qualification scope
COP cannot be reported as qualified when the profile does not include COP performance.

### `PAQ-009` — temporal qualification scope
Dynamic/stabilometric KPI requiring timing cannot be qualified by a profile lacking timing evidence.

### `PAQ-010` — protocol exactness
Activity, speed/stance, footwear, passes/steps/window and aggregation resolve the named protocol version.

### `PAQ-011` — step-count profile ownership
Minimum accepted steps are read from the profile; no universal hidden constant is applied.

### `PAQ-012` — region/metric-specific repeatability
A global device reliability statistic cannot substitute for the required metric/ROI qualification record.

### `PAQ-013` — calibration expiry gate
Expired/failed verification produces the profile-defined non-valid state.

### `PAQ-014` — firmware/software compatibility
Unsupported acquisition firmware/software pairing cannot remain silently qualified.

### `PAQ-015` — requalification trigger
A qualification-impacting hardware/software change is recorded and triggers the defined review/requalification path.

### `PAQ-016` — cross-device default guard
Different device systems are `NOT_COMPARABLE` unless explicit cross-device policy/harmonization exists.

### `PAQ-017` — platform vs in-shoe context guard
Barefoot platform and shod in-shoe results do not silently share a compatibility state.

### `PAQ-018` — raw qualification evidence preservation
Qualification report remains linked to immutable raw/reference/test artifacts.

### `PAQ-019` — historical calibration stability
New calibration does not change the calibration identity/provenance of historical acquisitions.

### `PAQ-020` — no invented tolerance
An OPEN limit cannot be converted into an undocumented numeric default by implementation/UI.

---

## 25. Mapping to existing contracts

```text
PAQ-004           -> coordinate/registration pressure mapping
PAQ-005/010/013   -> BINT-008 protocol provenance
PAQ-007           -> BINT-006/007 quality-state propagation
PAQ-016/017       -> BINT-011/012 comparison compatibility
PAQ-018/019       -> Project Schema provenance/immutability
```

---

## 26. What is FROZEN vs OPEN

### FROZEN

```text
qualification is profile- and intended-use-specific
exact device/calibration/protocol identity is required
bench + protocol evidence are distinct
quality state is explicit
cross-device comparability is opt-in, not assumed
historical calibration/provenance is immutable
acceptance rules are versioned/profile-owned
```

### OPEN

```text
exact Sensor Medica platform/model first qualified
specific calibration reference method
actual numeric accuracy/repeatability/COP/timing limits
minimum passes/steps per concrete protocol
recalibration interval
cross-device harmonization equations/limits
real registration tolerance to scan/CAD frames
```

These OPEN values require concrete hardware, measurement procedure and evidence; they are not architecture questions.

---

## 27. Freeze conclusion

The acquisition qualification chain is:

```text
intended use
 -> exact device/unit + SensorGeometry
 -> calibration profile
 -> bench evidence
 -> human/protocol evidence where required
 -> versioned acceptance rules
 -> runtime quality state
 -> BiomechE KPI provenance
 -> CAD comparison/reporting
```

This methodological contract can be implemented and tested before the geometry-engine shoot-out and prevents unqualified device/protocol assumptions from leaking into clinical/design outcome comparisons.
