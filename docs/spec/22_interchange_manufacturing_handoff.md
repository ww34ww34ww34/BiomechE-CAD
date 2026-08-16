# BiomechE-CAD — Interchange & Manufacturing Handoff Contract

**Version:** v1  
**Status:** **FROZEN v1**  
**Date:** 2026-08-16  
**Architecture:** implementation-neutral; no export library selected.  
**Manufacturing authority:** `10_manufacturing.md`.  
**Coordinate authority:** `01_coordinate_registration.md` plus explicit manufacturing coordinate convention.  
**Numerical authority:** `18_numerical_qualification_registry.md`.

---

## 0. Purpose

Define how BiomechE-CAD exchanges geometry/data with scanners, external CAD/CAM and manufacturing workflows without allowing a transport format to become authority for clinical prescription semantics.

Core rule:

```text
PROJECT SEMANTIC MODEL
!= INTERCHANGE REPRESENTATION
!= MANUFACTURING PACKAGE
!= DOWNSTREAM MACHINE ARTIFACT
```

Every handoff must declare what survives, what is transformed, what is lost and which exact artifact/hash was released.

---

## 1. Standards rationale

Current standards support a layered rather than file-centric model:

- ISO/IEC 25422:2025 defines the 3MF specification suite;
- ISO/ASTM 52915:2020 defines AMF v1.2 as an additive-manufacturing interchange format;
- ISO 17295:2023 defines AM positioning, coordinate and orientation reporting concepts;
- ISO/ASTM 52951:2026 defines an application/organization-specific AM part data package and a referenceable information flow from design to acceptance.

Therefore BiomechE-CAD treats a file format as a **capability-bounded carrier** inside a broader product-owned manifest/package.

---

# 2. Interchange artifact classes

```text
GEOMETRY_REFERENCE
SEMANTIC_PROJECT_EXCHANGE
MANUFACTURING_GEOMETRY
MANUFACTURING_PACKAGE
CAM_EXCHANGE_ARTIFACT
DOWNSTREAM_MACHINE_ARTIFACT
INSPECTION_DATA
PHYSICAL_PART_SCAN
REPORT_PACKAGE
```

A file extension alone never determines semantic class.

---

# 3. Common artifact contract

```text
InterchangeArtifact
  artifactId
  artifactClass

  sourceProjectId
  sourceDesignRevisionId?
  sourceManufacturingProfileId?
  sourceManufacturingGeometryRevisionId?

  formatId
  formatVersion/profile
  extensionsUsed[]

  generatedAt
  generatorId/version

  units
  sourceFrameRef
  outputFrameConvention
  transformApplied
  handedness
  side

  byteHash
  hashAlgorithm
  byteLength

  capabilityManifestRef
  lossManifestRef
  validationResultRef

  releaseState
  supersedes?
```

Once released for manufacturing or external acceptance, bytes/hash are immutable.

---

# 4. Format capability manifest

For every importer/exporter implementation maintain an exact, versioned capability record:

```text
FormatCapabilityProfile
  formatId
  formatVersion
  implementationId/version

  geometryCapabilities[]
  unitSemantics
  coordinateSemantics
  objectIdentitySupport
  transformSupport
  colorSupport
  materialSupport
  multiMaterialSupport
  metadataSupport
  extensionSupport[]
  productionIdentitySupport

  limits[]
  unsupportedFeatures[]
  knownCompatibilityConstraints[]
```

Capability is implementation/version specific; do not infer support only from what the general format standard permits.

---

# 5. Explicit loss manifest

Every lossy conversion SHALL be able to produce or resolve an explicit loss summary:

```text
LossManifest
  semanticPrescriptionLost
  typedPlacementLost
  requestedDoseLost
  workflowPresetProvenanceLost
  materialRegionSemanticsLost
  materialPropertiesLost
  coordinateMetadataLost
  unitsMetadataLost
  objectIdentityLost
  parametricEditabilityLost
  sourceProvenanceLost
  inspectionDefinitionsLost
  notes[]
```

A geometry-only export may be valid for a downstream process while being semantically lossy. That is acceptable only when the authoritative project/manufacturing manifest preserves the missing information.

---

# 6. Units

Canonical internal length is millimetres, but every exchange artifact records its output unit/conversion policy.

Rules:

```text
no silent unit inference at export
no silent scale guessing at import
unit conversion is explicit and reproducible
post-import dimensions are sanity-checked
```

For formats/implementations where units cannot be reliably transported, the manufacturing package/sidecar manifest supplies the authoritative unit contract.

---

# 7. Coordinate frame / orientation

Every manufacturing handoff defines:

```text
source anatomical/CAD frame
source-to-manufacturing transform
manufacturing coordinate convention
part orientation
handedness
side
```

Baking a transform into geometry is permitted only if the manifest records the transform and resulting convention.

Camera/view orientation is never manufacturing orientation by implication.

ISO 17295 terminology should be used where applicable to additive-manufacturing positioning/orientation reporting [STD-ISO-17295-2023].

---

# 8. Tessellation / geometry realization

When a clinical/authoring surface is tessellated for exchange, preserve:

```text
source design/manufacturing geometry revision
tessellator ID/version
quality strategy
parameters or qualification profile
resulting geometry summary
geometry validation result
dimensional sanity result
```

No universal tessellation tolerance is frozen here. It is an explicit algorithm/manufacturing qualification parameter owned by NREG/profile.

The exported mesh is a derived ManufacturingArtifact, not the semantic prescription.

---

# 9. STL policy

STL may be supported as a **geometry-only manufacturing/reference transport** when required by downstream systems.

BiomechE-CAD SHALL treat STL alone as insufficient for full semantic round-trip. The product-owned manifest must preserve as applicable:

```text
units
side
coordinate/orientation contract
design revision
manufacturing profile/revision
material assignment
artifact hash
generator version
required QC
```

An STL importer also requires an explicit unit/orientation resolution policy.

---

# 10. 3MF policy

3MF is a preferred candidate when a richer additive-manufacturing carrier is useful because the current specification suite provides a core format plus extensions, including material/property and production-related mechanisms.

However:

```text
3MF package != BiomechE-CAD project semantic model
```

Exporter policy records exact core/extension versions used and receiver compatibility.

Potential mapped content may include:

```text
mesh/object structure
units
object transforms
material/property resources
production identifiers
selected metadata
```

Clinical prescription, source-acquisition lineage and workflow expansion remain in the product-owned package unless an explicit versioned mapping is defined.

---

# 11. AMF policy

AMF v1.2 may be supported where ecosystem compatibility requires it. The exporter declares exact profile/version and mapped properties.

ISO/ASTM 52915:2020 itself recognizes that additional final-part information can remain outside the format. AMF is therefore an interchange carrier, not complete product lineage.

---

# 12. OBJ / PLY policy

OBJ/PLY may be admitted for scan/reference/visual geometry where needed.

Their use defines:

```text
units policy
coordinate policy
geometry/normal handling
color/property handling if used
material-sidecar handling if used
losses
```

They are not assumed to carry BiomechE-CAD prescription semantics.

---

# 13. Native semantic project exchange

A portable semantic project exchange should carry or reference:

```text
project/case identity under privacy policy
source-asset manifests + hashes
coordinate/registration state
landmarks/ROIs
DesignRevision semantic operations
workflow/preset applications
material prescriptions
inspection definitions/results
BiomechE result references
manufacturing lineage
report lineage
```

Large binaries may remain external/hash-addressed. Exact Project Schema v0.2 materialization remains outside this document until separately authorized.

---

# 14. Manufacturing package

Canonical package concept:

```text
ManufacturingPackage
  packageId
  packageVersion

  designRevisionId
  manufacturingProfileId/revision
  manufacturingGeometryRevisionId

  manifest
  geometryArtifacts[]
  downstreamArtifacts[]

  material/lot requirements
  coordinate/orientation contract
  process requirements
  post-process requirements
  QC plan
  acceptance limits + authority refs

  generator/software versions
  source hashes
  package integrity metadata

  releaseApproval
  releasedAt
  releasedBy
```

This aligns conceptually with the design-to-acceptance data-package approach in ISO/ASTM 52951:2026 while remaining BiomechE-CAD-specific.

---

# 15. Package vs file integrity

Hash each immutable file as raw bytes and hash/canonicalize the manifest by a documented method where required.

The project already references SHA-family/JCS guidance for selected metadata (`STD-NIST-FIPS-180-4`, `STD-RFC-8785`).

A package-level integrity value does not replace individual artifact hashes where per-file lineage is required.

---

# 16. CAM / downstream manufacturing boundary

BiomechE-CAD may hand off manufacturing geometry and profile metadata to an external CAM or machine-specific system.

The product SHALL preserve:

```text
source manufacturing geometry revision
receiving system/profile identity where known
derived downstream artifact identity/hash
software/post-processor version where available
coordinate/orientation contract
relationship to manufacturing run
```

Regenerating a downstream artifact creates a new artifact identity/hash even when the semantic design is unchanged.

---

# 17. External manufacturer boundary

When manufacturing is performed externally:

```text
BiomechE-CAD clinical/design semantics remain authoritative in project
manufacturer receives released manufacturing package
manufacturer may produce derived process artifacts
returned production/QC evidence links back to package/run/physicalPart
```

External edits to released geometry cannot masquerade as the original design. If accepted, they require a new manufacturing geometry/artifact state and explicit provenance/deviation review.

---

# 18. Round-trip levels

Define four round-trip claims:

```text
BYTE_ROUND_TRIP
FORMAT_SEMANTIC_ROUND_TRIP
GEOMETRIC_EQUIVALENCE
PRODUCT_SEMANTIC_ROUND_TRIP
```

They are not interchangeable.

Examples:

- STL can achieve geometric equivalence while failing product semantic round-trip;
- 3MF can preserve more manufacturing metadata while still not preserving full clinical authoring semantics;
- a native semantic package can preserve product state while regenerated tessellation bytes differ.

Any test must state which round-trip level it claims.

---

# 19. Validation on export/import

At minimum validate as applicable:

```text
serialization success
format conformance where a conformance suite/library supports it
finite coordinates
units/scale sanity
side/orientation contract
required geometry validity
referenced objects/materials resolved
hash computed
loss manifest generated
receiver compatibility known or warning emitted
```

A successful file write is not automatically a manufacturing-release PASS.

---

# 20. Failure / warning policy

### Typical blocking states

```text
unknown output units for manufacturing
invalid required geometry
missing required manufacturing profile
unresolved side for a side-specific part
package integrity failure
required semantic-to-manufacturing mapping missing
```

### Typical warnings

```text
loss of editability
loss of non-required metadata
receiver extension compatibility unknown
format does not carry material semantics but sidecar package does
```

Exact severity may be profile-dependent, but silent loss is forbidden.

---

# 21. Acceptance tests

```text
XCHG-001 every artifact records exact format/version/generator/hash
XCHG-002 export records source DesignRevision/manufacturing geometry revision
XCHG-003 unit conversion is explicit and dimensionally reproducible
XCHG-004 output coordinate/orientation transform round-trips through manifest
XCHG-005 STL export is labelled geometry-only/lossy for product semantics
XCHG-006 3MF exporter records core/extension versions actually used
XCHG-007 unsupported extension/content creates explicit loss/warning
XCHG-008 tessellation records algorithm/version/qualification parameters
XCHG-009 semantic project export preserves typed placement/workflow provenance where claimed
XCHG-010 manufacturing package preserves materials/process/QC/acceptance authority refs
XCHG-011 released artifact bytes/hash are immutable
XCHG-012 regenerated downstream artifact receives a new identity/hash
XCHG-013 external modification cannot masquerade as original released geometry
XCHG-014 import with unknown units does not silently assume mm
XCHG-015 format conformance does not imply product semantic round-trip
XCHG-016 round-trip test states byte/format/geometric/product level
XCHG-017 export write success != manufacturing release
XCHG-018 package/artifact integrity failure is blocking
```

---

# 22. Frozen invariants

```text
file format != product semantic authority
STL geometry != complete prescription
3MF/AMF metadata != complete clinical lineage
export transform != anatomical frame mutation
successful serialization != manufacturing acceptance
regenerated artifact != same immutable artifact
format conformance != product semantic round-trip
lossy export != lost project provenance
```

---

# 23. Product conclusion

For every exchange/handoff BiomechE-CAD must answer:

```text
What exact revision was exported?
Into which format/version/extensions?
What coordinate/unit transform was applied?
What semantic information survived?
What was lost and where is it preserved instead?
What exact bytes/hash were released?
Which manufacturing profile/QC plan applies?
Can downstream evidence be traced back to the physical part?
```

This contract is independent of the export library and geometry engine.

---

## Bibliography / standards links

[STD-ISO-17295-2023]: ../BIBLIOGRAPHY.md#std-iso-17295-2023
[STD-NIST-FIPS-180-4]: ../BIBLIOGRAPHY.md#std-nist-fips-180-4
[STD-RFC-8785]: ../BIBLIOGRAPHY.md#std-rfc-8785

**Current-source supplements pending canonical bibliography normalization:**

- ISO/IEC 25422:2025, *Information technology — 3D Manufacturing Format (3MF) specification suite*.
- ISO/ASTM 52915:2020, *Specification for additive manufacturing file format (AMF) Version 1.2*, Edition 3, confirmed current in 2026.
- ISO/ASTM 52951:2026, *Additive manufacturing — Data — Data packages for AM parts*.
