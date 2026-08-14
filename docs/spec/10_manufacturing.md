# BiomechE-CAD — Manufacturing Functional Specification

**Status:** ACTIVE functional baseline v0  
**Date:** 2026-08-14  
**Architecture:** implementation-neutral.  
**Evidence basis:** `docs/research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md`, EasyCAD2 behavioral baseline and `docs/BIBLIOGRAPHY.md`.

---

## 1. Scope

This specification defines how a BiomechE-CAD design revision becomes a traceable physical manufacturing artifact.

Core rule:

```text
CAD EXPORT
!=
MANUFACTURED PART
!=
ACCEPTED PART
```

Every physical orthosis SHALL preserve a chain from clinical/design revision through material/lot, machine/process, post-processing and QC.

---

## 2. ManufacturingProfile

```text
ManufacturingProfile
  profileId
  revision
  displayName

  processType
    AM_MEX
    AM_PBF_POLYMER
    AM_OTHER
    CNC_MILLING
    HYBRID
    MANUAL_FINISH
    OTHER

  allowedMaterialDefinitions[]
  requiredMaterialLotTraceability

  machineProfileRef
  processParametersSchemaVersion
  postProcessProfileRefs[]

  requiredQC[]
  acceptancePolicyVersion

  evidenceRefs[]
  status
    DEVELOPMENT
    QUALIFIED
    RETIRED
```

Changing any parameter classified as qualification-critical SHALL create a new profile revision.

---

## 3. ManufacturingRun

```text
ManufacturingRun
  runId
  manufacturingProfileId
  profileRevision

  designRevisionId
  manufacturingGeometryRevisionId

  machineId
  machineModel
  machineStateRef?
  operator?

  startTime
  endTime?

  materialLots[]
  processParameters
  environment?

  generatedArtifacts[]
  logRefs[]
  warnings[]
```

A run is an execution record, not a reusable configuration.

---

## 4. Immutable ManufacturingArtifact

```text
ManufacturingArtifact
  artifactId
  designRevisionId
  manufacturingRunId

  side
  artifactType
    STL
    3MF
    AMF
    GCODE
    CNC_TOOLPATH
    PROJECT_PACKAGE
    PHYSICAL_PART_RECORD
    OTHER

  fileHash
  generatedAt
  generatorVersion
  profileRevision
  validationState
```

Once a generated artifact has been used for manufacturing, it SHALL NOT be silently replaced under the same artifact ID/hash.

---

## 5. AM process provenance

For polymer AM preserve as applicable:

```text
AMProcessState
  technology
  machineId / model
  machineProfileVersion

  feedstockMaterialId
  feedstockLotId

  coordinateConvention
  buildOrientation
  buildPosition

  layerHeight
  shell/wall parameters
  infill family + percentage/parameters
  lattice/TPMS family + parameters
  local process overrides[]

  support strategy?
  environment?
  software/slicer/toolpath version

  postProcess[]
```

ISO 17295:2023 provides a common AM orientation/coordinate vocabulary [STD-ISO-17295-2023]. ISO/ASTM 52903-1 defines feedstock requirement semantics for extrusion-based polymer AM [STD-ISOASTM-52903-1-2020].

---

## 6. CNC / subtractive provenance

```text
CNCProcessState
  machineId
  controller/profileVersion

  blankMaterialId
  blankLotId?
  blankDimensions

  fixtureId/profile
  coordinateSystem
  orientation

  tools[]
    toolId
    geometry/ref
    state/lifeRef?

  CAMSoftwareVersion
  toolpathArtifactId

  feedsSpeeds? // when qualification-critical
  offsets/allowances
  postProcessorVersion

  manualFinishing[]
```

EasyCAD2 behavior establishes CNC/GCODE as an existing professional workflow baseline [EC2-MANUAL-1.1, pp.44–50; EC2-VAL-PLAN-1.4, US21]. BiomechE-CAD extends this with versioned process provenance.

---

## 7. Post-processing

```text
PostProcessStep
  stepId
  type
  profileId/revision
  parameters
  timestamp
  operator?
  sourceState
  resultingState
  measurementRefs[]
```

Property-changing operations such as heat/thermoforming/curing/lamination SHALL be recorded. Heating has been shown to change mechanical response of common insole materials [REF-CAD-096].

---

## 8. QCRequirement

```text
QCRequirement
  requirementId
  metric
  location/ROI?
  method
  instrumentClass?
  units
  lowerLimit?
  upperLimit?
  target?
  uncertaintyRequirement?
  conditioning/environment?
  requiredEvidenceRef?
  severity
    INFO
    WARNING
    BLOCKING
```

A tolerance without a measurement method is incomplete.

---

## 9. QCMeasurement

```text
QCMeasurement
  measurementId
  artifactId
  requirementId

  value / dataRef
  units
  method
  instrumentId?
  calibrationRef?
  operator?
  timestamp
  environment?
  uncertainty?

  result
    PASS
    FAIL
    INDETERMINATE
```

Actual measured values SHALL remain distinct from nominal CAD values.

---

## 10. Geometric trueness / dimensional QC

The system SHALL support key-dimensional or full-field comparisons:

```text
ManufacturedGeometryMeasurement
  source
    CALIPER
    SCAN3D
    CMM
    GAUGE
    OTHER

  designReferenceRevision
  alignmentMethod
  dimensions[]
  deviationMapRef?
  measurementUncertainty?
```

For AM, ISO/ASTM 52902:2023 defines standardized test-artifact concepts for assessing/calibrating system geometric capability [STD-ISOASTM-52902-2023]. It does not impose a universal orthosis tolerance.

Therefore:

```text
orthosis tolerance
= ManufacturingProfile requirement
```

not a global hard-coded CAD value.

---

## 11. AM part / process qualification semantics

ISO/ASTM 52901:2017 distinguishes part definition, feedstock, final characteristics/properties, inspection and acceptance [STD-ISOASTM-52901-2017]. ISO/ASTM 52920:2023 provides production-process/site qualification principles [STD-ISOASTM-52920-2023]. ISO/ASTM 52924:2023 classifies polymer AM part properties as mechanical, physical and geometrical [STD-ISOASTM-52924-2023].

BiomechE-CAD SHALL therefore allow a profile to define separate gates:

```text
INPUT / FEEDSTOCK
PROCESS
GEOMETRIC
MECHANICAL / MATERIAL
FUNCTIONAL
DOCUMENTATION
```

---

## 12. Artifact lifecycle

```text
DESIGN_READY
  ↓
ARTIFACT_GENERATED
  ↓
MANUFACTURING_STARTED
  ↓
MANUFACTURED
  ↓
INSPECTION_PENDING
  ↓
ACCEPTED | CONDITIONALLY_ACCEPTED | REJECTED
  ↓
ISSUED_TO_PATIENT
  ↓
IN_SERVICE
  ↓
RECHECK | REPLACED | RETIRED
```

### Blocking rule

If a qualified profile defines a blocking QC requirement, a FAIL or missing required measurement SHALL prevent `ACCEPTED` / validated-production state.

---

## 13. Physical-part identity

```text
PhysicalOrthosis
  physicalPartId
  leftRight
  patient/caseRef

  designRevisionId
  manufacturingArtifactId
  manufacturingRunId
  materialLotRefs[]

  manufacturedAt
  acceptedAt?
  issuedAt?

  serialOrHumanReadableId?
  label/markingRef?

  qcSummary
  currentServiceState
```

The project can therefore distinguish two physical copies produced from the same CAD revision but on different lots/runs.

---

## 14. Multi-material / regional realization

```text
ManufacturedMaterialRegion
  designRegionId
  physicalMaterialId/lot
  structuralRegionParameters?
  realizedThickness?
  interfaceRefs[]
  measuredProperties[]
```

A multi-material/lattice export SHALL preserve the mapping between semantic design region and realized manufacturing region where the selected output format/process permits it.

P0 schema SHALL not depend on STL being able to carry this information.

---

## 15. Production package

A portable manufacturing handoff SHOULD be able to include:

```text
manifest
patient/case pseudonymous ID as policy permits
design revision ID
manufacturing profile + revision
materials / lots
process parameters
geometry/toolpath artifacts + hashes
orientation/coordinate contract
required post-process
required QC plan
acceptance limits
software/generator versions
```

This package supports external manufacturing without making the external system authoritative for clinical prescription semantics.

---

## 16. P0 / P1 / P2

### P0

- ManufacturingProfile revisioning;
- ManufacturingRun;
- material lot linkage;
- immutable export hash;
- AM/CNC process provenance fields;
- post-process provenance;
- QC requirement/measurement schema;
- physical-part identity;
- lifecycle / acceptance state;
- measured vs nominal geometry distinction;
- report/export serialization.

### P1

- build/coupon registry;
- 3D scan deviation maps;
- machine/process capability records;
- automated dimensional inspection import;
- actual material-property QC;
- multi-material realization verification;
- production package exchange.

### P2

- predictive process compensation;
- process digital twin;
- auto-requalification triggers;
- closed-loop manufacturing optimization;
- predictive artifact lifetime.

---

## 17. Acceptance tests

```text
MAN-001  design->profile->run->artifact lineage exact
MAN-002  machine/process/software version round-trip
MAN-003  feedstock/blank lot round-trip
MAN-004  AM orientation/coordinate round-trip
MAN-005  AM infill/lattice/layer/shell params round-trip
MAN-006  CNC tooling/CAM/fixture provenance round-trip
MAN-007  post-process steps versioned
MAN-008  artifact hash immutable
MAN-009  QC metric+method+tolerance complete
MAN-010  acceptance state requires profile-defined QC
MAN-011  blocking failure prevents validated-production status
MAN-012  measured manufactured != nominal CAD geometry
MAN-013  coupon/specimen may link to build/run/part
MAN-014  measured properties link to exact run/artifact
MAN-015  multi-material interfaces traceable
MAN-016  service inspection links exact physical part
MAN-017  no unsupported universal lifetime/replacement rule
MAN-018  qualification-critical process change creates profile revision
```

---

## Bibliography

[EC2-MANUAL-1.1]: ../BIBLIOGRAPHY.md#ec2-manual-11
[EC2-VAL-PLAN-1.4]: ../BIBLIOGRAPHY.md#ec2-val-plan-14
[REF-CAD-096]: ../BIBLIOGRAPHY.md#ref-cad-096
[STD-ISO-17295-2023]: ../BIBLIOGRAPHY.md#std-iso-17295-2023
[STD-ISOASTM-52901-2017]: ../BIBLIOGRAPHY.md#std-isoastm-52901-2017
[STD-ISOASTM-52902-2023]: ../BIBLIOGRAPHY.md#std-isoastm-52902-2023
[STD-ISOASTM-52903-1-2020]: ../BIBLIOGRAPHY.md#std-isoastm-52903-1-2020
[STD-ISOASTM-52920-2023]: ../BIBLIOGRAPHY.md#std-isoastm-52920-2023
[STD-ISOASTM-52924-2023]: ../BIBLIOGRAPHY.md#std-isoastm-52924-2023
