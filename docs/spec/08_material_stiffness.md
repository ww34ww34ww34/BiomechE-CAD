# BiomechE-CAD — Material and Stiffness Functional Specification

**Version:** v1 — evidence-led frozen product contract  
**Status:** **FROZEN v1**  
**Date:** 2026-08-16  
**Architecture:** implementation-neutral.  
**Evidence basis:** `docs/research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md` and `docs/BIBLIOGRAPHY.md`.  
**Authority boundary:** geometry semantics remain in `16_geometry_authoring_contract.md`; numerical/default/tolerance ownership remains in `18_numerical_qualification_registry.md`; manufacturing realization/QC remains in `10_manufacturing.md`.

---

## 0. Freeze rationale

This v1 freezes the distinction among material identity, mechanical prescription, measured properties, process-conditioned state and service-aged state. It does **not** freeze one preferred material, Shore value, modulus conversion, lattice law, lifetime or manufacturing acceptance limit.

Current evidence and standards support the separation already used by BiomechE-CAD:

```text
nominal material identity
!= measured material/coupon property
!= effective structural/lattice response
!= manufactured final-part property
!= service-aged property
```

Systematic-review evidence for orthotic materials remains heterogeneous (`REF-CAD-094`), subject-specific experiments show that effective cushioning stiffness can depend on loading context (`REF-CAD-099`), and ISO 868 explicitly states that Shore indentation hardness has no simple universal relationship to a fundamental material property. Therefore no generic hardness→modulus or material-name→mechanics shortcut is permitted.

---

## 1. Scope

This specification defines how BiomechE-CAD represents material identity, regional mechanical prescription, measured properties and service-aged state.

Core rule:

```text
NOMINAL MATERIAL
!=
MANUFACTURED EFFECTIVE PROPERTY
!=
SERVICE-AGED PROPERTY
```

A material name or Shore value SHALL NOT be treated as a complete mechanical model.

---

## 2. MaterialDefinition

```text
MaterialDefinition
  materialId
  revision

  supplier
  tradeName
  formulationCode?
  materialFamily
    EVA
    PE_FOAM
    PU_FOAM
    TPU
    EPU
    PA11
    PA12
    OTHER

  nominalDensity?
  nominalProperties[]
  datasheetRef?

  intendedRoles[]
    CUSHION
    ACCOMMODATE
    SUPPORT
    MOTION_CONTROL
    COVER
    SHEAR_LAYER
    STRUCTURAL
    OTHER

  evidenceRefs[]
```

### Requirements

- Supplier/trade name/formulation SHALL be separately storable.
- A generic material family SHALL NOT silently imply supplier-specific properties.
- Nominal properties SHALL be marked as nominal/datasheet, never as measured final-part values.
- Any product default or recommendation SHALL resolve to an explicit NREG/profile/evidence record rather than being encoded by material family name.

---

## 3. MaterialLot / feedstock

```text
MaterialLot
  lotId
  materialId
  supplierLot?
  manufactureDate?
  expiryDate?
  receivedDate?
  storageConditions?
  certificateRefs[]
  incomingMeasurements[]
```

Lot identity is P0 schema data when available and SHOULD become mandatory in qualified production profiles that rely on lot traceability.

---

## 4. MechanicalPropertyMeasurement

```text
MechanicalPropertyMeasurement
  propertyType
  value / curveRef
  units

  sourceType
    SUPPLIER_NOMINAL
    INCOMING_QC
    COUPON_TEST
    FINAL_PART_TEST
    SERVICE_STATE_TEST

  testMethod
  testStandard?
  instrument?
  specimenGeometry?
  specimenThickness?
  location/region?

  temperature?
  humidity?
  conditioning?
  dwell/rate/frequency?
  preload?

  timestamp
  operator?
  dataQuality
  sourceRefs[]
```

Supported property classes should include where relevant:

```text
density
hardness
compression stress-strain
compression stress value
effective stiffness
resilience
hysteresis
compression set
shear stiffness
friction coefficient
mass
thermal/moisture properties
```

A scalar property must preserve the conditions under which it is valid; a curve must preserve independent/dependent variable units and the test protocol needed for interpretation.

---

## 5. Hardness semantics

```text
HardnessMeasurement extends MechanicalPropertyMeasurement
  value
  scale
  testMethod
  dwellTime?
  specimenThickness?
```

### Invariants

1. A hardness numeric value without a scale is invalid.
2. Scale/method SHALL survive round-trip and reporting.
3. Shore A/D/C or other scales SHALL NOT be silently mixed.
4. No generic hardness-to-Young-modulus conversion is permitted.
5. If a conversion/calibration is later supported, it SHALL be named, versioned, material/process-specific, qualification-scoped and evidence-backed.

ISO 868 demonstrates why: Shore hardness is an empirical control measurement and has no simple universal relationship to a fundamental material property [STD-ISO-868-2003].

---

## 6. Compression / cushioning semantics

For flexible cellular materials, the system SHALL support curves or multiple operating points rather than forcing one linear modulus.

```text
CompressionResponse
  stressStrainCurveRef?
  loadDisplacementCurveRef?
  effectiveStiffnessPoints[]
  loadingRange
  loadingRate
  preload
  cycleNumber/state
  method
```

Relevant standards include compression stress-strain characterization and compression-set testing [STD-ISO-3386-1-2025; STD-ISO-1856-2018].

Evidence also supports loading-context dependence rather than a universal optimum: `REF-CAD-099` found subject/load-related differences in the tested cushioning-stiffness optimum.

---

## 7. MaterialRegion

```text
MaterialRegion
  regionId
  side
  referenceFrame
  roiOrMaskRef

  materialDefinitionId
  materialLotId?

  nominalThickness
  intendedRole
  targetPropertyProfile?

  transitionProfile?
  evidenceRefs[]
```

Material regions SHALL remain independent from pure geometry operations.

A region can express:

```text
same geometry + different material
same material + different structural/lattice response
different material + same geometry
```

Mirroring a material region is side-aware and SHALL preserve semantic ROI meaning and source material/mechanical prescription rather than only reflecting a raw mask.

---

## 8. MaterialStack

```text
MaterialStack
  stackId
  layers[] // ordered foot-side -> shoe-side
    layerId
    materialDefinitionId
    materialLotId?
    thickness
    intendedRole
    localRegionRef?

  interfaces[]
    interfaceId
    layerA
    layerB
    bondMethod
    adhesiveMaterialId?
    processProfileRef?
```

Layer order is semantically significant and SHALL be immutable within a manufacturing revision.

Interface mechanics such as shear/friction SHALL NOT be inferred from normal pressure or hardness alone [REF-CAD-104; REF-CAD-105].

---

## 9. Structural / lattice effective property

```text
StructuralMaterialRegion
  baseMaterialId
  structuralFamily
    SOLID
    INFILL
    LATTICE
    TPMS
    CUSTOM

  structuralParameters
  nominalEffectiveProperties?
  calibratedEffectiveProperties?
  calibrationRef?
```

### Rule

```text
base material modulus
!=
effective structural/lattice stiffness
```

BiomechE-CAD SHALL preserve both. Pressure-derived lattice design remains P2/R&D unless validated for the target clinical/profile context [REF-CAD-008; REF-CAD-098].

---

## 10. PostProcessMaterialState

```text
PostProcessMaterialState
  stepId
  processType
    HEAT_MOLD
    THERMOFORM
    ANNEAL
    UV_CURE
    THERMAL_CURE
    LAMINATE
    ADHESIVE_BOND
    SURFACE_FINISH
    OTHER

  processProfileId
  timestamp
  operator?
  resultingMeasurements[]
```

Material property-changing post-processing SHALL be retained because heating has experimentally altered stiffness/stress-strain behavior of common insole material combinations [REF-CAD-096].

---

## 11. Durability qualification

```text
DurabilityTest
  testId
  specimenOrArtifactId
  testType
    CONSTANT_LOAD_FATIGUE
    CONSTANT_STRAIN_FATIGUE
    CUSTOM_CYCLIC
    SERVICE_FOLLOWUP

  cycleCount
  load/strain profile
  frequency?
  environment

  initialMeasurements[]
  intervalMeasurements[]
  finalMeasurements[]

  acceptanceRuleRef?
  result
```

ISO 3385 and ISO 24999 provide complementary constant-load and constant-strain fatigue semantics for flexible cellular materials [STD-ISO-3385-2014; STD-ISO-24999-2008].

No cycle count from a study or standard SHALL become a universal orthosis lifetime. Acceptance belongs to an explicit material/manufacturing qualification profile.

---

## 12. ServiceState

```text
ServiceState
  physicalArtifactId
  timestamp

  estimatedCalendarAge
  estimatedWearTime?
  estimatedWeightBearingExposure?
  estimatedCycles?

  visibleWearState?
  thicknessMeasurements[]
  mechanicalMeasurements[]
  pressureVerificationRef?
  patientExperienceBundleRef?

  disposition
    CONTINUE
    RECHECK
    REPLACE
    UNKNOWN
```

Visible compression alone SHALL NOT be used as an automatic replacement rule; longitudinal evidence shows physical compression and functional pressure performance need not degrade identically [REF-CAD-103].

Any `CONTINUE/RECHECK/REPLACE` automation requires a named qualified rule; otherwise disposition remains human-entered or `UNKNOWN`.

---

## 13. Property source and confidence

Every property shown in the UI/report SHOULD identify its source:

```text
NOMINAL / DATASHEET
MEASURED MATERIAL
MEASURED COUPON
MEASURED PART
CALIBRATED EFFECTIVE
MODELLED
ESTIMATED
SERVICE-MEASURED
```

The product SHALL visually distinguish measured from modeled/estimated properties.

If uncertainty is available from the test/fit/calibration method, it SHALL be preserved rather than discarded when presenting a single nominal value.

---

## 14. P0 / P1 / P2

### P0

- MaterialDefinition + revision;
- MaterialLot hooks;
- hardness scale/method semantics;
- nominal density/thickness;
- MaterialRegion;
- MaterialStack + interface provenance;
- base vs effective structural property distinction;
- post-process state;
- measured-vs-nominal property source;
- ServiceState schema;
- round-trip/report serialization.

### P1

- coupon registry;
- compression curves;
- compression-set/fatigue imports;
- shear/friction test records;
- local measured properties;
- service-aging dashboard;
- material qualification profiles.

### P2

- service-life prediction;
- pressure→material optimization;
- lattice/property inverse design;
- adaptive replacement recommendation;
- closed-loop material calibration.

---

## 15. Acceptance tests

```text
MAT-001  material identity/revision round-trip
MAT-002  material lot/feedstock round-trip
MAT-003  hardness scale+method required
MAT-004  no silent hardness->modulus conversion
MAT-005  density and thickness independent
MAT-006  stack order/interface round-trip
MAT-007  base/effective structural properties separate
MAT-008  geometry/material dose independent
MAT-009  post-process state explicit
MAT-010  measured property test provenance complete
MAT-011  initial/service states separate
MAT-012  fatigue protocol/cycles survive round-trip
MAT-013  compression-set method/conditioning retained
MAT-014  no shear/friction inference from normal pressure/hardness
MAT-015  material ROI mapping mirror/save/load invariant
MAT-016  material change does not alter semantic prescription silently
MAT-017  nominal supplier != measured final-part property
MAT-018  evidence-linked preset preserves profile/population/source
```

---

## 16. Frozen invariants

```text
material family != supplier formulation
nominal property != measured property
hardness != modulus
base material property != structural effective property
geometry dose != mechanical dose
post-process state != pre-process material state
new part != service-aged part
study cycle count != universal lifetime
```

Numerical limits/defaults remain under `NREG` and relevant qualification profiles.

---

## Bibliography

[REF-CAD-008]: ../BIBLIOGRAPHY.md#ref-cad-008
[REF-CAD-094]: ../BIBLIOGRAPHY.md#ref-cad-094
[REF-CAD-096]: ../BIBLIOGRAPHY.md#ref-cad-096
[REF-CAD-098]: ../BIBLIOGRAPHY.md#ref-cad-098
[REF-CAD-099]: ../BIBLIOGRAPHY.md#ref-cad-099
[REF-CAD-103]: ../BIBLIOGRAPHY.md#ref-cad-103
[REF-CAD-104]: ../BIBLIOGRAPHY.md#ref-cad-104
[REF-CAD-105]: ../BIBLIOGRAPHY.md#ref-cad-105
[STD-ISO-868-2003]: ../BIBLIOGRAPHY.md#std-iso-868-2003
[STD-ISO-1856-2018]: ../BIBLIOGRAPHY.md#std-iso-1856-2018
[STD-ISO-3385-2014]: ../BIBLIOGRAPHY.md#std-iso-3385-2014
[STD-ISO-24999-2008]: ../BIBLIOGRAPHY.md#std-iso-24999-2008
[STD-ISO-3386-1-2025]: ../BIBLIOGRAPHY.md#std-iso-3386-1-2025
