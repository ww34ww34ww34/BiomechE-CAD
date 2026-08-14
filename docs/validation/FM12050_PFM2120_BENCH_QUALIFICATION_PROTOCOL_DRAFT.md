# FM12050 / PFM2120 — Bench Qualification Protocol

**Status:** DRAFT — execution-ready structure; no metrological PASS limits frozen  
**Date:** 2026-08-15  
**Candidate family:** Sensor Medica FREEMED DYNAMIC 120x50 / `PFM2120` / production code `FM12050`  
**Purpose:** convert the generic `PAQ-*` qualification methodology into a reproducible bench plan for one identified physical unit.

> This document is a **test protocol**, not a test result. It does not claim that any FM12050/PFM2120 unit has passed metrological qualification.

---

## 1. Evidence basis

The protocol is deliberately stricter than a visual/function factory test because plantar-pressure system suitability depends on technology, calibration, accuracy, hysteresis/creep, spatial performance and intended outcome [REF-CAD-109, pp.141–144; Abstract] and because dedicated hardware-performance assessment is recommended rather than assuming nominal vendor performance [REF-CAD-110, pp.158–167; Abstract].

Protocol repeatability also depends on the acquisition procedure and number of accepted contacts/steps; published step-count results are population/protocol specific rather than universal [REF-CAD-108, pp.880–884; Abstract—Background/Methods/Findings/Interpretation].

Cross-system data are not assumed interchangeable [REF-CAD-036, Abstract—Methods/Results/Conclusions].

Canonical qualification semantics: `docs/spec/15_pressure_acquisition_qualification.md`.

Current controlled-source intake: `docs/research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md`.

---

## 2. Relationship to existing factory testing

Existing Sensor Medica `IOP-014` remains a production functional/visual gate.

This bench protocol **adds** quantitative qualification evidence. It does not replace the factory process.

Conceptually:

```text
factory assembly / functional test
        +
quantitative bench qualification
        +
protocol / human repeatability qualification where required
        =
qualified intended-use profile
```

---

## 3. Qualification unit — mandatory identity freeze

Before the first measurement, record:

```text
commercial model             PFM2120
production code              FM12050
platform serial              REQUIRED / OPEN
hardware revision            REQUIRED / OPEN
controller A serial/rev       REQUIRED / OPEN
controller B serial/rev       REQUIRED / OPEN
firmware version             REQUIRED / OPEN
FreeStep/acquisition version REQUIRED / OPEN
adapter/library build         REQUIRED / OPEN
calibration-sheet identity   REQUIRED / OPEN
qualification operator       REQUIRED
qualification timestamp      REQUIRED
```

No data set without exact unit/configuration identity can close a real `PressureAcquisitionQualificationProfile`.

---

## 4. Prerequisites before metrological execution

The following gaps should be closed or explicitly marked unavailable:

```text
metric cell-center / represented-area mapping
ordering of the two logical 60x50 matrices
matrix seam/gap geometry
row/column -> physical-axis mapping
raw sample semantic
Threshold application semantics
V-Calibration semantics
Calibration coefficient/model semantics
clipping/saturation representation
```

If raw→physical conversion remains opaque, a black-box pressure-output qualification can still be performed, but the limitation SHALL be recorded and internal conversion reproducibility cannot be claimed.

---

## 5. Reference equipment

The actual equipment model/accuracy/traceability remains `OPEN` until selected.

Minimum conceptual setup:

```text
REFERENCE FORCE / LOAD SYSTEM
  known applied vertical force
  sufficient range for intended tests
  calibration/verification record

LOAD APPLICATION FIXTURE
  repeatable contact geometry
  controlled position
  stable alignment

POSITION REFERENCE
  known x/y location for COP tests if COP is in intended use

TIME REFERENCE
  independent timing/trigger source if temporal qualification is required

ENVIRONMENT LOGGING
  temperature
  humidity where relevant
```

Reference-system uncertainty must be sufficiently smaller than the acceptance claim being tested. The exact ratio is not frozen here.

---

## 6. Raw evidence policy

Every test run stores immutable/hash-addressed evidence:

```text
raw platform stream or closest available raw export
physical pressure output
reference force/load stream
reference position where applicable
timestamps / trigger data
calibration/config snapshot
environment
operator notes
analysis-script build/version
```

Screenshots are supplementary only.

---

# TEST BLOCKS

## BQ-00 — Configuration snapshot

### Objective
Prove exactly what configuration was tested.

### Record

```text
unit/controller/firmware/software identity
current mode: STATIC / POSTURO / DYNAMIC
Threshold
V-Calibration
Calibration
sensor-map version/hash
adapter/build identity
```

### PASS rule
No hidden or unresolved configuration field that materially affects output.

If a field is technically unavailable, status is `KNOWN_UNAVAILABLE`, not omitted.

---

## BQ-01 — Warm-up and zero stability

### Objective
Characterize startup and unloaded baseline behavior.

### Procedure skeleton

1. start the unit from the defined cold/warm state;
2. acquire unloaded data over named intervals;
3. repeat after the chosen warm-up period;
4. repeat after representative loaded operation if drift assessment requires it.

### Report

```text
per-sensor / aggregate zero offset as technically available
zero drift versus time
spurious active-cell count
noise statistics
mode/configuration
```

### Acceptance limit
`OPEN — profile-owned`.

---

## BQ-02 — Logical-to-physical sensor-map verification

### Objective
Verify that logical cells correspond to the documented physical layout.

### Procedure skeleton

Apply localized loads at a set of known locations spanning:

```text
corners
central regions
matrix seam region
representative interior cells
```

Verify:

```text
row/column orientation
left/right/anterior/posterior physical mapping
matrix concatenation order
seam/gap behavior
```

### Acceptance limit
Exact mapping is semantic/exact; positional tolerance is `OPEN` until fixture/reference uncertainty is known.

---

## BQ-03 — Force/pressure scale and linearity

### Objective
Compare platform-derived load with an independent reference across the intended range.

### Procedure skeleton

Use multiple ascending load points and repeat the series.

Then use a descending series so hysteresis can be separated from simple scale error.

The actual test points SHALL be selected from:

```text
qualified intended-use load range
reference equipment capability
saturation margin
```

and recorded explicitly.

### Compute

Where physical represented areas are known:

```text
F_pressure = Σ pressure_i * represented_area_i
```

with explicit conversion from kPa·mm² to N.

### Report

```text
reference force
platform-derived force
absolute error
relative error where meaningful
fit/residuals
loading direction
repeat number
```

### Acceptance limit
`OPEN — profile-owned`; do not derive a threshold from the nominal datasheet alone.

---

## BQ-04 — Repeatability

### Objective
Characterize repeated measurement under nominally identical conditions.

### Repeat for

```text
representative low/mid/high loads
representative locations
relevant modes
```

### Candidate statistics

```text
mean / SD
coefficient of variation where appropriate
within-run spread
repeatability coefficient or other named statistic
```

The exact statistic and limit must be selected before declaring PASS.

---

## BQ-05 — Hysteresis

### Objective
Measure dependence on load history.

### Procedure
Compare matched points from ascending and descending load sequences after the defined preconditioning.

### Report

```text
ascending response
descending response
difference / hysteresis metric
load point
region / whole-platform quantity
```

### Acceptance limit
`OPEN — technology/intended-use specific`.

---

## BQ-06 — Creep / relaxation

### Objective
Measure time-dependent output under a sustained load.

### Procedure
Apply a stable reference load for a predefined duration and capture the full time series.

### Report

```text
initial response
response versus time
steady/late response
relative and absolute change
recovery after unload if measured
```

### Duration / limit
`OPEN — must be chosen from intended use and sensor technology evidence`.

---

## BQ-07 — Saturation / clipping

### Objective
Identify saturation, clipping or non-physical behavior near the upper intended operating range.

### Safety
Never exceed platform/reference-equipment safe limits.

### Report

```text
applied reference load/pressure
maximum reported sample
number/fraction of saturated cells
clipping indicator if exposed
recovery after unload
```

### Acceptance limit
`OPEN`.

---

## BQ-08 — Dead / unstable sensor behavior

### Objective
Detect cells that are unresponsive, permanently active or unstable under defined loading.

### Report

```text
dead-cell map
unstable-cell map
persistent offset map
intermittent-cell events
```

Do not silently interpolate failed cells during qualification unless a separate validated algorithm is explicitly under test.

---

## BQ-09 — Force closure

### Objective
Test aggregate consistency between pressure-derived force and independent vertical load.

### Inputs

```text
metric SensorGeometry
pressure output
reference vertical force
```

### Report

```text
F_reference
F_pressure
absolute difference
relative difference where meaningful
uncertainty/context
```

### Acceptance limit
`OPEN`.

This check does not prove regional pressure accuracy by itself.

---

## BQ-10 — COP positional qualification

**Run only if COP/stabilometry is in the intended qualified scope.**

### Objective
Compare computed COP with known reference load positions.

### Positions
Include a predefined set spanning central and edge-relevant regions.

### Report

```text
reference x/y
measured COP x/y
Euclidean error
axis-wise error
load level
repeat
```

### Acceptance limit
`OPEN — intended-use specific`.

A smooth visual COP trajectory is not a substitute for this test.

---

## BQ-11 — Timing / sampling qualification

**Required for dynamic/stabilometric outputs whose validity depends on timing.**

### Characterize

```text
nominal sample rate
observed frame/timestamp intervals
jitter
missing frames
duplicate timestamps
monotonicity
latency/synchronization where relevant
```

### Reference
Use an independent trigger/timing method when needed to substantiate the claim.

### Acceptance limit
`OPEN — KPI/protocol dependent`.

---

## BQ-12 — Mode-specific calibration regression

### Objective
Verify that STATIC/POSTURO/DYNAMIC mode state is explicitly tracked and cannot cross-contaminate results.

The historical unit record found during source intake demonstrates separate mode parameters; it does **not** define current acceptable values.

### Test

```text
capture configuration for each supported mode
run a defined repeatable reference load
switch mode/configuration
verify provenance changes
verify result cannot be mislabeled as the previous mode
```

### PASS
Semantic exactness is mandatory; numerical acceptance remains profile-specific.

---

## BQ-13 — Calibration lifecycle regression

### Objective
Prove that recalibration creates new identity/provenance and does not rewrite old acquisitions.

### Test

```text
capture result under calibration C1
create/activate calibration C2
capture/reprocess according to policy
verify C1 historical evidence remains addressable
verify new result identifies C2
```

Maps to `PAQ-013`, `PAQ-015`, `PAQ-019`.

---

# 7. Human/protocol qualification after bench

A bench-qualified device is not automatically a protocol-qualified clinical measurement system.

For each intended protocol, independently freeze:

```text
activity / speed / stance
barefoot / footwear context
number of contacts/steps or window duration
contact inclusion/exclusion
edge-hit handling
repeat count
aggregation statistic
operator positioning rules
```

Then evaluate metric/ROI-specific repeatability as required.

`REF-CAD-108` is retained as evidence that step count can matter; its 12-step result remains specific to that study context.

---

# 8. Cross-device work is later

Do not use the FM12050 bench qualification to imply equivalence with another pressure platform or in-shoe system.

Cross-device comparison remains:

```text
NOT_COMPARABLE
```

unless a dedicated harmonization/comparison protocol passes [REF-CAD-036, Abstract—Methods/Results/Conclusions].

---

# 9. Required output package

For one completed unit qualification:

```text
qualification/profile snapshot
unit/configuration manifest
reference-equipment manifest
raw platform evidence
raw reference evidence
analysis code/build
all BQ result tables
plots as derived evidence
uncertainty/limitations
PASS/FAIL/INDETERMINATE per acceptance rule
review/approval record
```

Hash-address all retained evidence where practical.

---

# 10. Before execution — exact remaining inputs

```text
[ ] current PFM2120/FM12050 physical unit serial
[ ] current controller serials/revisions + firmware
[ ] matching calibration/assembly sheet
[ ] authoritative metric sensor mapping
[ ] raw acquisition adapter/interface semantics
[ ] selected reference load/force system
[ ] selected position fixture for COP if required
[ ] intended first qualification scope (STATIC_LOAD recommended first)
[ ] named numeric acceptance criteria + rationale before PASS declaration
```

Until these fields are resolved, this protocol is ready for planning/tooling but no real-device `QUALIFIED` status may be issued.
