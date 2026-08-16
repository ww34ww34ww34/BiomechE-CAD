# BiomechE-CAD — Input, Scan and Reference Data Contract

**Version:** v1  
**Status:** **FROZEN v1**  
**Date:** 2026-08-16  
**Architecture:** implementation-neutral.  
**Evidence basis:** `REF-CAD-002`, `REF-CAD-003`, frozen coordinate/registration, BiomechE integration, reporting/provenance and pressure-acquisition contracts.  
**Schema status:** semantic contract only; Project Schema v0.2 remains `APPROVED / NOT MATERIALIZED`.

---

## 0. Purpose

Define every external or captured data object that may enter BiomechE-CAD and preserve a reproducible chain from **original evidence** to any processed/registered/derived representation used for authoring, inspection, outcome analysis or manufacturing verification.

Core rule:

```text
ORIGINAL ACQUISITION
!= PROCESSED DATASET
!= REGISTERED DATASET
!= DERIVED REFERENCE
!= CAD GEOMETRY
```

No cleaned, cropped, decimated, registered, resampled or converted dataset may silently replace the original source authority.

---

## 1. Evidence rationale

A systematic review comparing 3D scanning with traditional foot/ankle morphology capture found limited evidence and highly variable accuracy/reliability across methods and measured parameters [REF-CAD-002]. A 2023 scoping review found substantial variation in scanner specifications, weight-bearing conditions, markers, number of scans, measurement definitions and statistical methods, and proposed a 16-item reporting checklist [REF-CAD-003].

BiomechE-CAD therefore treats capture protocol and processing provenance as part of the design evidence, not metadata that may be discarded after mesh creation.

This contract does **not** declare 3D scanning intrinsically superior to casting/impression or define a universal scanner accuracy requirement.

---

# 2. Admitted input families

P0/P1 may support the following semantic source families where an importer exists:

```text
FOOT_3D_SCAN
FOOT_POINT_CLOUD
FOOT_SURFACE_MESH
2D_FOOT_IMAGE_OR_SCAN
PRESSURE_ACQUISITION
PRESSURE_MAP_OR_DERIVED_RESULT
BIOMECHE_RESULT_PACKAGE
LANDMARK_SET
ROI_OR_MASK_SET
REFERENCE_TEMPLATE
REFERENCE_ORTHOSIS_GEOMETRY
PHYSICAL_ORTHOSIS_SCAN
MANUFACTURING_REFERENCE
EXTERNAL_PROJECT_REFERENCE
OTHER_VERSIONED_SOURCE
```

File extension is not source semantics. For example, an STL may represent a foot scan, a CAD export, a physical-part scan reconstruction or another artifact; its role must be explicit.

---

# 3. Common `SourceAsset` contract

```text
SourceAsset
  sourceAssetId
  sourceFamily
  semanticRole

  originalFileName?
  mediaType?
  formatId?
  formatVersion?

  byteHash
  hashAlgorithm
  byteLength?

  importedAt
  importedBy
  sourceSystem?
  sourceSystemVersion?

  patientCaseRef?         // policy controlled
  side
  unitsState
  coordinateFrameState

  captureContextRef?
  acquisitionQualificationRef?

  parentSourceRefs[]
  provenanceActivityRefs[]

  integrityState
  qualityState
  warnings[]
```

The raw content is immutable after import. Correction means creating a new source/derived asset linked to the previous one, never replacing bytes behind the same content identity.

---

# 4. Original / processed / registered / derived lineage

Canonical lineage classes:

```text
ORIGINAL
PROCESSED
REGISTERED
RESAMPLED
SEGMENTED
ANNOTATED
DERIVED
```

Example:

```text
scanner output ORIGINAL
  ↓ crop / denoise
processed point cloud PROCESSED
  ↓ meshing
surface mesh DERIVED
  ↓ anatomical registration
registered mesh REGISTERED
  ↓ conform/query
CAD reference field DERIVED
```

Each non-original node SHALL preserve:

```text
parent source ID(s)
operation type
algorithm ID/version
parameters
operator or automated agent
started/completed timestamp where relevant
output hash
warnings/quality metrics
```

This is consistent with the project's W3C PROV-inspired entity/activity/agent provenance model [STD-W3C-PROV-O-2013; REF-CAD-111; REF-CAD-112; REF-CAD-113].

---

# 5. Capture context

When relevant to geometry or interpretation, preserve:

```text
CaptureContext
  captureContextId
  method
    3D_SCANNER
    PHOTOGRAMMETRY
    STRUCTURED_LIGHT
    LASER
    DEPTH_CAMERA
    IMPRESSION_DIGITIZATION
    FLATBED_2D
    PRESSURE_PLATFORM
    IN_SHOE_PRESSURE
    OTHER

  deviceManufacturer?
  deviceModel?
  deviceSerial?
  hardwareRevision?
  firmwareVersion?
  acquisitionSoftware?
  acquisitionSoftwareVersion?

  operator?
  site?
  timestamp

  subjectPosition?
  weightBearingState
    NON_WEIGHT_BEARING
    PARTIAL_WEIGHT_BEARING
    FULL_WEIGHT_BEARING
    DYNAMIC
    UNKNOWN

  supportSurface?
  footwearContext?
  socksContext?
  activityContext?

  markersUsed?
  markerProtocolRef?
  numberOfCaptures?
  selectedCaptureIndex?

  environment?
  notes?
```

`UNKNOWN` is explicit and is not silently converted to a default capture condition.

---

# 6. Scanner/device capability and qualification context

Where known, preserve device claims/qualification separately from an individual acquisition:

```text
AcquisitionDeviceProfile
  profileId
  deviceFamily
  model
  hardwareRevision?
  nominalAccuracy?
  nominalResolution?
  fieldOfView?
  calibrationMethod?
  calibrationState?
  qualificationRefs[]
  sourceType
    VENDOR_NOMINAL
    INTERNAL_QUALIFICATION
    EXTERNAL_QUALIFICATION
```

Vendor nominal accuracy is not equivalent to measured project/device accuracy. A product comparison or clinical conclusion must not silently assume that all scanners or capture methods are interchangeable [REF-CAD-002; REF-CAD-003].

---

# 7. Units, scale and orientation

An input's unit state is explicit:

```text
KNOWN_METRIC
KNOWN_NON_METRIC
DECLARED_BY_FORMAT
INFERRED_WITH_REVIEW
UNKNOWN
```

If units are unknown, conversion into canonical millimetres requires an explicit user/validated-rule decision and provenance record.

No heuristic bounding-box scale guess may silently become authoritative.

For geometric data preserve where available:

```text
source coordinate convention
handedness
axis definitions
origin definition
orientation transform
unit conversion transform
```

The canonical anatomical/CAD frame is governed by `01_coordinate_registration.md`. File coordinates are never assumed to be anatomical coordinates.

---

# 8. Laterality and ownership

Every side-specific source has:

```text
side
  LEFT
  RIGHT
  BILATERAL
  NOT_APPLICABLE
  UNKNOWN
```

Laterality source/provenance should be recordable:

```text
FILE_METADATA
DEVICE_PROTOCOL
CASE_CONTEXT
USER_CONFIRMED
ALGORITHM_SUGGESTED
UNKNOWN
```

Algorithm-suggested laterality remains unconfirmed until a product rule or human confirmation establishes authority.

A mirror operation creates derived data/geometry with explicit side transformation; it does not mutate source-side truth.

---

# 9. 3D point-cloud and mesh quality

For applicable geometry sources, record measurable quality attributes without inventing universal acceptance thresholds:

```text
GeometrySourceQuality
  vertexOrPointCount
  faceCount?
  connectedComponents?
  boundingBox_mm?

  nonFiniteCount
  duplicatePointOrVertexCount?
  degenerateFaceCount?
  nonManifoldEdgeCount?
  boundaryLoopCount?
  isolatedComponentCount?

  normalState
    PROVIDED
    RECOMPUTED
    UNKNOWN
  windingState?

  holeSummary?
  density/resolutionSummary?
  confidenceMapRef?

  selfIntersectionState?
  unitScaleState
  qualityWarnings[]
```

A scan with holes or non-manifold geometry is not automatically invalid for every use. Its usability depends on the downstream operation and qualification profile. The exact acceptance rule remains explicit and context-specific.

---

# 10. Processing provenance

Any cleanup or transformation SHALL be represented as an explicit activity, including as applicable:

```text
crop
outlier removal
denoise
smoothing
hole filling
normal estimation/orientation
remeshing
meshing from points
decimation
subdivision
resampling
segmentation
mask extraction
coordinate conversion
manual cleanup
```

Minimum processing record:

```text
ProcessingActivity
  activityId
  operationType
  inputSourceRefs[]
  algorithmId
  algorithmVersion
  parameters
  operator/agent
  outputSourceRefs[]
  qualityBefore?
  qualityAfter?
  reviewState
```

A visual improvement does not by itself establish metrological validity.

---

# 11. Landmark sets

```text
LandmarkSet
  landmarkSetId
  sourceAssetRefs[]
  side
  frameRef
  definitionVersion

  landmarks[]
    landmarkId
    semanticType
    position
    positionRepresentation
    method
      MANUAL
      SEMI_AUTOMATIC
      AUTOMATIC
      IMPORTED
    algorithmId/version?
    confidence?
    reviewer?
    reviewState
    timestamp
    sourceEvidenceRefs[]
```

Landmark identity/meaning, source method and review state are first-class under the frozen Geometry Authoring Contract.

A later algorithm update does not silently move historical landmarks attached to a committed design revision.

---

# 12. ROI / mask sets

```text
ROISet
  roiSetId
  sourceAssetRefs[]
  side
  frameRef
  definitionVersion
  generationMethod
  algorithmVersion?
  reviewState
  rois[]
```

ROI masks used for outcome comparisons must retain exact version/definition. A changed segmentation creates a new ROISet rather than altering historical results.

---

# 13. Registration

Registration is an explicit derived relationship, not a destructive transformation of the source:

```text
RegistrationRecord
  registrationId
  sourceAssetId
  targetFrameRef
  transform
  transformConvention

  method
  algorithmId/version?
  landmarkSetRef?
  ROIRef?

  initialTransform?
  residualMetrics[]
  inlier/outlierSummary?
  qualityState
  reviewer?
  reviewState

  createdAt
```

The authoritative coordinate/laterality semantics are defined by `01_coordinate_registration.md`.

Registration residual is an algorithm/quality measurement; it is not a manufacturing tolerance or clinical threshold.

---

# 14. Pressure and BiomechE data

Pressure acquisitions remain governed by `15_pressure_acquisition_qualification.md`; quantitative results exchanged with BiomechE remain governed by `11_biomeche_integration.md`.

This input contract requires that an imported pressure/BiomechE package preserve:

```text
source dataset ID/hash
exact device/acquisition/protocol refs
units
side
sensor geometry / physical geometry refs when applicable
algorithm/result version
ROI/mask version
quality flags
result provenance
```

A rendered pressure heatmap is never sufficient as quantitative authority if numeric source data are available/required.

---

# 15. Reference template / reference orthosis

A reference template or external orthosis may be used for viewing, fitting, comparison or authoring only with explicit role:

```text
VISUAL_REFERENCE
BASE_TEMPLATE_CANDIDATE
GEOMETRIC_FIT_REFERENCE
MANUFACTURING_REFERENCE
PHYSICAL_PART_REFERENCE
HISTORICAL_DESIGN_REFERENCE
```

Using an external geometry file as a reference does not make its anonymous geometry a semantic prescription.

If converted into an editable semantic design, the conversion is a versioned authoring activity with explicit assumptions and unresolved semantics.

---

# 16. Physical orthosis / manufactured-part scans

Scans of a physical part are distinct from foot scans and CAD geometry:

```text
PhysicalPartScan
  physicalPartId
  sourceAssetId
  captureContextRef
  registrationRef
  designRevisionRef
  manufacturingArtifactRef
  manufacturingRunRef
  inspectionPurpose
```

Deviation maps and dimensional QC must identify the exact physical part, design/manufacturing reference and alignment method.

---

# 17. File-format admission

P0 importers/exporters may support formats such as:

```text
STL
OBJ
PLY
3MF
other scanner/vendor formats
```

but admission is capability-specific. For every format implementation document:

```text
supported version/profile
units semantics
coordinate semantics
color/material/metadata support
losses on import/export
unsupported extensions
validation behavior
```

A format may be accepted for geometry transport while being insufficient for semantic round-trip.

Detailed interchange rules belong to `22_interchange_manufacturing_handoff.md`.

---

# 18. Error, unresolved and quality states

Canonical source state categories:

```text
VALID_FOR_DECLARED_USE
VALID_WITH_WARNINGS
UNRESOLVED
NOT_USABLE_FOR_DECLARED_USE
CORRUPT_OR_INTEGRITY_FAILURE
```

Examples of unresolved conditions:

```text
unknown units
unknown side
ambiguous orientation
missing capture protocol
registration not reviewed
landmarks suggested but unconfirmed
processing history unavailable
```

The user may still inspect unresolved data. Whether authoring/manufacturing may proceed is defined by workflow/qualification policy, not by silently filling missing metadata.

---

# 19. Original evidence retention

The project SHALL preserve or hash-address original evidence according to retention/storage policy sufficient to maintain reproducibility and audit lineage.

Derived data may be regenerated or cached, but a committed design/report must retain exact source identities/hashes and algorithm/version provenance needed to reproduce its semantic state.

Storage optimization may move large assets to object storage, but must not change their logical identity.

---

# 20. P0 / P1 / P2

## P0

- immutable source identity/hash;
- source family/semantic role;
- units/side/frame state;
- capture context;
- original-vs-derived lineage;
- basic mesh/point-cloud quality summary;
- explicit processing provenance;
- landmark/ROI provenance + review state;
- explicit registration record;
- pressure/BiomechE source linkage;
- unresolved/warning states;
- reference/physical-part scan distinction.

## P1

- richer scanner qualification profiles;
- standardized automated mesh-quality diagnostics;
- confidence maps;
- multi-capture selection/fusion;
- automated landmark suggestions with validation metrics;
- physical-part scan inspection workflow;
- vendor-specific import adapters.

## P2 / R&D

- probabilistic morphology uncertainty;
- multi-scan consensus models;
- automated capture-quality prediction;
- model-based scan correction with uncertainty propagation.

---

# 21. Acceptance tests

```text
INPUT-001 original bytes/hash immutable after import
INPUT-002 processed asset preserves exact parent/activity lineage
INPUT-003 unknown units remain unresolved until explicit resolution
INPUT-004 file frame/orientation is not assumed anatomical frame
INPUT-005 side provenance persists and suggestion != confirmation
INPUT-006 capture weight-bearing/conditions persist where supplied
INPUT-007 scanner nominal capability != acquisition measurement/qualification
INPUT-008 mesh quality metrics are stored without hidden universal threshold
INPUT-009 cleanup/denoise/decimation operation is versioned and replay/audit visible
INPUT-010 landmark method/confidence/review state round-trip
INPUT-011 ROI definition/version survives comparison/reanalysis
INPUT-012 registration stores transform/method/version/residual/review state
INPUT-013 registration residual is not reused as manufacturing/clinical tolerance
INPUT-014 pressure heatmap cannot replace required numeric pressure authority
INPUT-015 BiomechE result import preserves exact result/source/protocol version
INPUT-016 external reference geometry role is explicit
INPUT-017 physical-part scan links exact physical orthosis and manufacturing lineage
INPUT-018 derived/registered source does not overwrite original source identity
INPUT-019 unresolved source can be inspected but cannot be silently promoted to valid
INPUT-020 committed design/report can resolve exact input hashes and derived provenance
```

---

# 22. Frozen invariants

```text
original != processed != registered != derived
file coordinates != anatomical coordinates
vendor accuracy != qualified acquisition accuracy
unknown unit != millimetres
unknown side != guessed confirmed side
algorithm-suggested landmark != reviewed landmark
visual cleanup != metrological validity
pressure heatmap != numeric acquisition
reference geometry != semantic prescription
physical-part scan != CAD design geometry
```

---

# 23. Product conclusion

BiomechE-CAD must always be able to answer:

```text
What exactly entered the system?
From which device/file/source?
Under what capture conditions?
What was original and what was changed?
Which algorithms/operators transformed it?
Which side/frame/units are authoritative?
Which landmarks/ROIs were reviewed?
How was it registered and with what residual?
Which exact source evidence supported this committed design/result?
```

This input contract is frozen independently of geometry-engine selection.

---

## Bibliography

[REF-CAD-002]: ../BIBLIOGRAPHY.md#ref-cad-002
[REF-CAD-003]: ../BIBLIOGRAPHY.md#ref-cad-003
[REF-CAD-111]: ../BIBLIOGRAPHY.md#ref-cad-111
[REF-CAD-112]: ../BIBLIOGRAPHY.md#ref-cad-112
[REF-CAD-113]: ../BIBLIOGRAPHY.md#ref-cad-113
[STD-W3C-PROV-O-2013]: ../BIBLIOGRAPHY.md#std-w3c-prov-o-2013
