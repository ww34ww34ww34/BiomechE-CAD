# Sensor Medica FM12050 / PFM2120 — Pressure Qualification Intake

**Date:** 2026-08-15  
**Status:** SOURCE INTAKE / NOMINAL PROFILE IDENTIFIED / NOT METROLOGICALLY QUALIFIED  
**Purpose:** bridge the generic pressure-acquisition qualification methodology in `spec/15_pressure_acquisition_qualification.md` to the first concrete Sensor Medica product family without inventing missing geometry, conversion or performance data.

---

## 1. Result of the source hunt

The first concrete qualification candidate can now be identified at product-family level:

```text
commercial model: FREEMED DYNAMIC 120x50
commercial code:  PFM2120
production code:  FM12050
manufacturer:      Sensor Medica
```

The evidence comes from the controlled Sensor Medica technical dossier in Drive, not from secondary reseller pages.

The source-intake records are catalogued in `docs/research/SOURCES.md` under:

```text
INTAKE-FM12050-MANUAL-3.0
INTAKE-FM12050-PRODUCTION-2.0
INTAKE-FM12050-BOM-1.8
INTAKE-FREEMED-IOP-014-0.3
INTAKE-FM12050-DATASHEET-1.3
INTAKE-FM12050-CAL-MX20643-2021
```

Machine-readable intake snapshot:

```text
qualification/intake/fm12050-pfm2120-source-profile-2026-08-15.json
```

These `INTAKE-*` identifiers are deliberately **not** canonical bibliography IDs yet. Frozen specifications continue to rely only on sources already registered in `docs/BIBLIOGRAPHY.md`.

---

## 2. Current nominal product facts

Current controlled manual and production documentation jointly establish the following nominal/product facts:

```text
FREEMED DYNAMIC 120x50 / PFM2120 / FM12050
outer dimensions: 1240 x 740 mm
weight: 8.5 kg
power: 15 VDC
computer interface: USB
nominal pressure range: 0–150 N/cm²
maximum sampling frequency: 400 Hz
manual describes automatic calibration
production uses 2 sensor matrices of 60 x 50 logical elements
production uses 2 TAS rev. B controller assemblies
serial/controller/firmware/calibration parameters are recorded per unit
```

The two `60 x 50` matrices imply 6000 logical sensing elements and agree with the older controlled datasheet that explicitly states 6000 sensors.

This establishes **logical topology**, not yet canonical metric `SensorGeometry`.

---

## 3. Historical datasheet evidence

The older `Datasheet12050 rev 1.3` additionally records:

```text
6000 sensors
2.5 dpi nominal spatial resolution
up to 400 Hz
10-bit acquisition
resistive conductive-rubber / gold-contact sensor technology
0–150 N/cm² nominal pressure range
1,000,000 cycles nominal durability
```

These values are useful for consistency checking and qualification planning.

They are **not** allowed to silently override newer controlled documentation. In particular:

```text
2.5 dpi
```

must not be converted into exact canonical cell-center coordinates or represented cell areas without the current drawing/mapping evidence.

---

## 4. Existing production calibration provenance

The manufacturing cycle already records, per unit:

```text
platform serial
controller serials
firmware version
Calibration
V-Calibration
Threshold
```

and directs final testing through `IOP-014`.

This is a strong starting point because the product data model does not need to invent unit-specific calibration provenance from scratch.

---

## 5. What IOP-014 currently establishes

The reviewed current instruction `IOP-014 rev 0.3` is best classified as:

```text
FACTORY FUNCTIONAL / VISUAL TEST
```

The procedure:

```text
connects the FreeMed platform
starts FreeStep
checks noise / activation halo
applies distributed human body load
adjusts Calibration / Threshold when required
repeats the functional visual check
records calibration values on the assembly/test sheet
```

This should be preserved as a production gate.

It is **not equivalent** to the additional metrological qualification required by `PAQ-*`, because the reviewed instruction does not specify a traceable reference load/pressure and quantified acceptance rules for:

```text
linearity / scale error
repeatability
hysteresis
creep
saturation
COP positional error
timing/jitter
measurement uncertainty
```

The new qualification plan is therefore an additional evidence layer, not a replacement for IOP-014.

---

## 6. Historical unit example — MX20643

A real historical `FM12050 - Calibration Sheet` was located for:

```text
product code: PFM2120
device serial: MX20643
test date: 17/11/2021
controller serials: MX200702 / MX200703
firmware: 13.1
```

Recorded mode-specific parameters:

```text
STATIC & POSTURO
  Threshold     32
  V-Calibration 0
  Calibration   Auto

DYNAMIC
  Threshold     24
  V-Calibration 8
  Calibration   512
```

This is especially important semantically: **the same physical product already has mode-specific calibration state**.

Therefore a future qualified profile must not store one undifferentiated `calibration = valid` flag for static, posturographic and dynamic use.

The MX20643 sheet remains a historical factory record; it is not assumed to describe the current BiomechE development unit.

---

## 7. What remains unknown before metric SensorGeometry freeze

The source search has **not yet** established authoritatively:

```text
exact active sensing-area dimensions
exact metric center of every cell
represented physical area per cell
exact pitch / edge-cell geometry
physical seam/gap between the two 60x50 matrices
logical matrix concatenation/order
row/column -> physical-axis mapping
dead/masked sensor encoding
```

Therefore BiomechE-CAD SHALL continue to treat `120 x 50` as logical topology only.

No metric mapping is inferred from product naming, overall enclosure dimensions or historical `2.5 dpi` alone.

---

## 8. What remains unknown before raw→pressure freeze

Current accessible GitHub code search did not locate the FreeStep/device acquisition adapter or the semantics of:

```text
Threshold
V-Calibration
Calibration
raw ADC/sample values
per-sensor vs global coefficients
saturation/clipping
```

The accessible BiomechE repository intentionally sees hardware-independent physical `SensorGeometry`/pressure semantics rather than FreeMed-specific adapter internals.

Consequently the next qualification step must obtain the acquisition adapter/source or a controlled interface specification. The missing conversion SHALL NOT be reconstructed by guessing from test-sheet numbers.

---

## 9. First real qualification target

The first actual `PressureAcquisitionQualificationProfile` should be built for **one selected physical PFM2120/FM12050 unit**, not for the whole FreeMed family.

Required first-unit intake:

```text
current device serial
hardware revision
controller serials/revisions
firmware version
current assembly/calibration sheet
current FreeStep/acquisition software version
current physical sensor mapping
current raw→physical conversion path
```

Then qualify, in order:

```text
1. zero / zero drift
2. force/pressure scale and linearity versus reference
3. repeatability
4. hysteresis / creep
5. saturation / dead-cell behavior
6. force-closure consistency
7. COP accuracy if COP is an intended output
8. timing / frame loss / jitter for dynamic or stabilometry
9. protocol/human repeatability separately
```

Static-load qualification should precede broader dynamic/stabilometric claims unless a specific product need dictates otherwise.

---

## 10. Why no numeric thresholds are frozen here

Scientific literature and existing project evidence already show that validity depends on:

```text
device technology
calibration
metric
ROI
protocol
number of contacts/steps
intended use
```

The current source intake adds manufacturer/product facts but does not provide an independent metrological reference study for this exact unit.

Therefore this file intentionally freezes **no new accuracy, repeatability, COP or timing threshold**.

The values will move from `OPEN` to numeric only after a named measurement method and acceptance rationale are available.

---

## 11. Product-data consequences already justified

Even before bench qualification, the source intake supports these data-model requirements:

```text
product model != physical unit
unit serial must survive
controller serials/firmware can matter
calibration state is mode-specific
factory functional test != metrological qualification
current calibration record != historical calibration record
logical matrix topology != metric SensorGeometry
nominal datasheet spec != achieved qualification performance
```

These are consistent with the already-frozen `D-CAD-024` and `D-CAD-026`; no geometry-kernel decision is involved.

---

## 12. Next evidence acquisition

Priority source hunt:

```text
A. current physical development-unit serial
B. matching current calibration/assembly sheet
C. electrical/sensor drawing that fixes active area + matrix mapping
D. acquisition adapter / FreeStep SDK source or controlled interface document
E. reference-load/calibration tooling specification
F. any existing quantitative bench reports for the selected serial/model
```

Once A–D are available, the nominal source intake can be promoted into a versioned real-device profile. Once E–F plus new measurements exist, metrological PAQ acceptance limits can start moving from `OPEN` to qualified values.
