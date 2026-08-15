# BiomechE-CAD — Geometry Authoring Contract P0

**Status:** FROZEN v1  
**Freeze date:** 2026-08-15  
**Freeze decision:** `D-CAD-027`  
**Architecture:** geometry-kernel independent  
**Functional authority:** `BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`  
**Coordinate authority:** `01_coordinate_registration.md`  
**Schema authority:** `02_project_schema.md`  
**Evidence authority:** `../BIBLIOGRAPHY.md`

---

## 0. Purpose

This document defines **what an orthosis authoring operation means**, what information must survive into a committed `DesignRevision`, how placement/dose/context are represented and how geometry can be inspected and replayed.

It deliberately does **not** decide:

```text
OpenSubdiv vs ON_SubD vs another kernel
control cage topology
mesh vs surface internal cache
GPU vs CPU evaluation
native vs WASM runtime
exact implementation of each deformation primitive
```

Those are downstream implementation choices.

The authoring contract exists because the product must be reproducible even if the geometry engine changes.

---

# 1. Core doctrine

## GAUTH-001 — Semantic operation is authoritative

A clinically/manufacturing meaningful edit SHALL remain represented as a typed semantic operation or equivalent typed prescription state.

The final tessellated mesh SHALL NOT erase:

```text
operation type
side
anatomical target
placement/reference
dose + units
spatial extent / transition
source acquisition / registration
mechanical/material context where relevant
algorithm version
operator / provenance
```

A derived geometry cache may be stored for performance but is not sufficient historical authority by itself.

## GAUTH-002 — Geometry dose != mechanical dose

The following are separate concepts:

```text
GeometryDose
  height/depth
  angle
  extent
  curvature/shape
  transition

MechanicalDose
  thickness
  material/effective stiffness
  cushioning
  lattice/infill/structural region
  stack
  post-process/service state
```

A product UI may present them together, but persistence and traceability must not collapse them.

## GAUTH-003 — No hidden universal clinical default

A numerical value reported in one paper, vendor template or historical workflow SHALL NOT become a universal BiomechE-CAD clinical default without a named qualified profile.

Examples:

- metatarsal-pad location findings are population/reference specific (`REF-CAD-013`, `REF-CAD-014`);
- arch geometry/stiffness effects depend on configuration/load/context (`REF-CAD-017`, `REF-CAD-053`, `REF-CAD-055`, `REF-CAD-056`);
- heel/skive/plug effects are modification and population specific (`REF-CAD-018`, `REF-CAD-058..067`).

Product defaults may exist only through the numerical registry defined in `18_numerical_qualification_registry.md`.

---

# 2. Authoring operation envelope

## GAUTH-004 — Minimum operation record

Every committed geometry-affecting operation SHALL preserve at least:

```text
GeometryAuthoringOperation
  operationId
  operationType
  operationOrder
  enabled
  side

  target
  placement
  geometryDose
  transition
  mechanicalDoseRef? / materialRegionRefs[]?

  sourceAcquisitionRefs[]?
  registrationRefs[]?
  landmarkRefs[]?
  roiRefs[]?

  sourcePresetRef?
  sourceMacroRef?
  overrideRecords[]?

  algorithmRef
  authorRef
  createdAt
  rationale?
  evidenceRefs[]?
```

`parameters` may remain an implementation serialization container, but the semantic information above must be recoverable and validated.

## GAUTH-005 — Preview is not a committed revision

Interactive edits MAY exist as mutable preview state.

A commit boundary SHALL create an immutable `DesignRevision` snapshot that freezes:

```text
operation order
parameters
source definitions
algorithm versions
source acquisitions/registrations
profile references
```

Canceling a preview must not mutate the committed parent revision.

## GAUTH-006 — Explicit invalid state

An operation may be:

```text
VALID
VALID_WITH_WARNINGS
INVALID
UNRESOLVED_REFERENCE
UNSUPPORTED_IN_PROFILE
```

An invalid/unresolved operation must not silently evaluate with guessed values.

---

# 3. Acquisition context and landmark provenance

## GAUTH-007 — Capture condition is first-class metadata

When scan geometry influences authoring, the capture context SHALL be preserved when known.

At minimum support:

```text
weightBearingCondition
  NON_WEIGHT_BEARING
  PARTIAL_WEIGHT_BEARING
  FULL_WEIGHT_BEARING
  OTHER_NAMED
  UNKNOWN
```

Additional method/posture context may be profile-specific.

`UNKNOWN` is acceptable; inferred/assumed weight-bearing without provenance is not.

Rationale: scanning-method literature shows acquisition protocol and measured parameter affect reliability (`REF-CAD-002`, `REF-CAD-003`).

## GAUTH-008 — Landmark is more than a coordinate

A design-significant landmark SHALL preserve:

```text
landmarkId
semanticType
point
frameRef
side
sourceAcquisitionRef?
sourceMethod
  MANUAL_PALPATION_MARKER
  MANUAL_ON_SCAN
  DEVICE_PROVIDED
  ALGORITHM_DERIVED
  IMPORTED
  OTHER_NAMED
authorRef / algorithmRef
confidence?
reviewState
  UNREVIEWED
  REVIEWED_ACCEPTED
  REVIEWED_REJECTED
qualityFlags[]
```

This extends the logical meaning of the current `LandmarkSet` without forcing an immediate reference-schema migration.

## GAUTH-009 — Landmark uncertainty is not a geometry tolerance

Landmark identification uncertainty, registration residual and manufacturing tolerance are distinct quantities and SHALL NOT be merged into one generic `tolerance` field.

---

# 4. Placement/reference model

## GAUTH-010 — Placement uses a typed reference

A corrective feature SHALL not be positioned only by unlabelled global XYZ.

Supported P0 reference modes shall include at least:

```text
INTRINSIC_SQ
LANDMARK_RELATIVE_MM
LANDMARK_LINE_RELATIVE_MM
NORMALIZED_FOOT_LENGTH
ROI_RELATIVE
PRESSURE_TARGET_RELATIVE
CUSTOM_REGISTERED_REFERENCE
```

The chosen mode, reference IDs and frame are part of the operation meaning.

## GAUTH-011 — Intrinsic coordinates

Where `INTRINSIC_SQ` is used, semantics follow the frozen coordinate contract:

```text
s: heel -> distal
q: lateral -> medial
q > 0 = medial on both LEFT and RIGHT
```

Intrinsic coordinates do not replace metric anatomical coordinates; they are a stable placement mode for template-relative authoring.

## GAUTH-012 — Landmark-relative distance

A landmark-relative placement SHALL record:

```text
reference landmark/line
signed/unsigned convention
distance in mm
direction/frame
```

For metatarsal-pad placement this allows study/profile rules to be represented without converting them into a universal foot-coordinate constant (`REF-CAD-013`).

## GAUTH-013 — Normalized placement

Normalized placement SHALL record:

```text
normalization definition
reference length/axis
normalized value
source frame
```

Different normalization definitions are not assumed equivalent (`REF-CAD-014`).

## GAUTH-014 — Pressure-target placement

A pressure-derived placement SHALL preserve:

```text
source acquisition
metric/aggregation definition
ROI/version
threshold/selection rule
algorithm version
registration to CAD frame
```

A colored heatmap screenshot is not sufficient placement provenance.

---

# 5. Geometry dose model

## GAUTH-015 — Physical units are explicit

Geometry dose uses canonical physical units where applicable:

```text
mm
deg
mm²
```

Normalized values are permitted only with an explicit normalization definition.

## GAUTH-016 — Spatial extent is explicit

Local operations SHALL expose or derive an explicit support/influence region.

At minimum the semantic record can express:

```text
longitudinal extent
transverse extent
ROI/mask
boundary relation
falloff/transition definition
```

## GAUTH-017 — Transition is part of the prescription

Abrupt and smooth transitions are not equivalent.

A geometry operation SHALL identify a named transition/falloff mode and version when transition shape materially affects geometry.

## GAUTH-018 — Clamp/constraint is explicit

If an operation is clipped or altered by safety/manufacturing constraints, persistence SHALL distinguish:

```text
requested dose
realized/evaluated dose
constraint responsible
```

A silent clamp that changes clinical intent is prohibited.

---

# 6. Required P0 operation families

The P0 domain model SHALL be capable of expressing the following orthosis-specific operation families even if several eventually share the same low-level geometry primitive.

## GAUTH-019 — Template / outline / sizing

```text
TEMPLATE_MORPH
OUTLINE_EDIT
GLOBAL_SCALE
LENGTH_WIDTH_ADJUST
```

Persist template identity/version and any dimensional target used.

## GAUTH-020 — Arch

Arch authoring SHALL preserve at least:

```text
archType
side
start / peak / end references
peakHeight or target displacement
width/depth
curvature/roundness mode
transition
reference landmarks/frame
mechanicalProfileRef?
```

Medial and lateral arch remain distinct semantic operations.

## GAUTH-021 — Heel decomposition

The following are distinct semantic concepts:

```text
HEEL_CUP / containment
HEEL_RELIEF
HEEL_CAMBER
MEDIAL_HEEL_SKIVE
HEEL_MECHANICAL_REGION / plug
```

The engine may reuse primitives internally; persistence may not silently collapse the concepts.

## GAUTH-022 — Wedge/posting

Rearfoot and forefoot wedge prescriptions SHALL preserve:

```text
angle
direction
pivot/reference
extent
full/partial application
transition
```

The sign convention and mirror behavior are governed by side-aware anatomical semantics.

## GAUTH-023 — Corrective element

A corrective element SHALL retain:

```text
semantic element type
anatomical target
placement reference
rotation/orientation
scale/geometry dose
integration mode
transition
mechanical/material override if present
```

Generic imported geometry may be supported later, but named orthotic semantics remain the P0 path.

## GAUTH-024 — Offload feature

An offload operation SHALL preserve:

```text
targetROI
geometry dose
transition
mechanical/material dose
intended outcome metric
safetyRingROI?
remoteComparisonROIs[]
```

The feature is not judged only by local depression depth; outcome evaluation is a separate measured/predicted layer.

## GAUTH-025 — Sculpt / freeform

Freeform editing must be replayable.

Allowed semantic representations include:

```text
versioned brush-event sequence
OR
consolidated sparse displacement layer tied to persistent semantic coordinates/IDs
```

At minimum retain tool type, radius/influence, strength/dose convention, direction mode, source representation and algorithm version.

A baked mesh with no authoring lineage is permitted only in explicit `IMPORTED_LEGACY_GEOMETRY` authority mode.

## GAUTH-026 — Scan conform

A scan-conform operation SHALL preserve:

```text
sourceScanRef
registrationRef
ROI/mask
projection method/direction
strength/blend
maximum allowed displacement if used
residual/error metrics if computed
algorithm version
```

## GAUTH-027 — Height / thickness / DFM constraints

Clinical height edits and production minimum-thickness rules are separate operations/constraints.

No universal minimum thickness is defined here. Production minimums resolve through a qualified `ManufacturingProfile` and the numerical registry.

---

# 7. Bilateral semantics

## GAUTH-028 — Mirror is semantic, not just geometric

Mirroring RIGHT ↔ LEFT SHALL transform:

```text
geometry
side ownership
medial/lateral meaning
intrinsic q semantics
landmark references
ROI references
wedge/posting direction
corrective-element orientation where defined
```

A mirrored operation is a new side-owned operation/revision state, not a live alias to the contralateral project.

## GAUTH-029 — Mirror policy is operation-specific

Every operation family/preset/macro SHALL declare one of:

```text
MIRROR_SAFE_AUTOMATIC
MIRROR_WITH_PARAMETER_TRANSFORM
MIRROR_REQUIRES_REVIEW
NOT_MIRRORABLE
```

Clinical/material parameters that do not have a valid side transform must never be blindly copied.

---

# 8. Inspection contract

## GAUTH-030 — Section

The CAD SHALL support section inspection in an explicit frame/plane with repeatable source revision.

A section measurement identifies:

```text
DesignRevision
plane definition
representation measured
units
algorithm/version
```

## GAUTH-031 — Distance / height / angle

Measurements SHALL state their geometric definition rather than storing only a displayed scalar.

Examples:

```text
point-to-point distance
point-to-plane height
surface-normal distance
signed angle between named vectors/planes
```

## GAUTH-032 — Thickness

Thickness queries SHALL identify the thickness definition/method used. Normal-ray thickness, shortest surface distance and manufacturing-layer thickness are not assumed interchangeable.

## GAUTH-033 — Deviation map

Where CAD nominal geometry is compared with a scan/manufactured part, a deviation result SHALL preserve:

```text
source geometry identities
registration used
distance definition
sampling/algorithm version
units
summary statistics
map asset/reference
quality/uncertainty metadata where available
```

A deviation map is a measurement artifact, not a substitute for a qualified acceptance rule.

---

# 9. Upper clinical surface vs production realization

## GAUTH-034 — Clinical intent and production realization are separable

The logical model SHALL distinguish:

```text
clinical/contact surface intent
thickness field
lower/shoe-facing surface rule
sidewall/closure rule
manufacturing profile
```

This does not mandate a particular internal topology.

## GAUTH-035 — Production body is derived from a committed design

A manufacturing body/export SHALL reference the exact committed `DesignRevision` and `ManufacturingProfile` used.

Changing process-specific underside/closure rules creates a new manufacturing artifact/profile result, not a silent mutation of the historical clinical prescription.

---

# 10. Determinism and numerical behavior

## GAUTH-036 — Deterministic semantic replay

Given the same:

```text
base definition snapshots
ordered operations
source assets/registrations
algorithm versions
profile versions
```

the evaluator SHALL reproduce equivalent geometry within the declared algorithm/profile tolerance.

The tolerance itself is not defined here; it resolves through `18_numerical_qualification_registry.md`.

## GAUTH-037 — Ordering is explicit

Operation ordering materially affects geometry and SHALL be persisted.

Any dependency/reordering logic must be deterministic and visible in the expanded committed operation sequence.

## GAUTH-038 — Algorithm change does not rewrite history

If an operation algorithm changes, existing revisions remain bound to the historical algorithm/version or migration creates a new explicit revision/result.

---

# 11. Acceptance namespace

New architecture-independent acceptance family:

```text
GAUTH-001..040
```

Suggested allocation:

```text
GAUTH-001  operation envelope completeness
GAUTH-002  preview vs committed immutability
GAUTH-003  unknown capture condition preserved as UNKNOWN
GAUTH-004  landmark provenance completeness
GAUTH-005  intrinsic placement side semantics
GAUTH-006  landmark-relative placement retains reference + units
GAUTH-007  normalized placement retains normalization definition
GAUTH-008  pressure-target placement retains acquisition/ROI/algorithm
GAUTH-009  geometry/mechanical dose separation
GAUTH-010  requested vs constrained realized dose
GAUTH-011  arch start/peak/end semantics
GAUTH-012  heel semantic decomposition
GAUTH-013  wedge pivot/direction semantics
GAUTH-014  corrective-element semantic type survives geometry
GAUTH-015  offload target/safety/remote semantics
GAUTH-016  sculpt replay metadata
GAUTH-017  scan-conform source/registration provenance
GAUTH-018  minimum thickness resolves through manufacturing profile
GAUTH-019  right->left mirror preserves medial meaning
GAUTH-020  mirror review policy enforced
GAUTH-021  section plane/source revision reproducible
GAUTH-022  distance definition explicit
GAUTH-023  thickness method explicit
GAUTH-024  deviation-map provenance complete
GAUTH-025  clinical surface vs production realization separation
GAUTH-026  deterministic semantic replay
GAUTH-027  explicit operation ordering
GAUTH-028  historical algorithm version remains resolvable
GAUTH-029  invalid/unresolved operation cannot silently evaluate
GAUTH-030  legacy baked geometry uses explicit legacy authority mode
GAUTH-031..040 reserved for geometry fixtures discovered during implementation
```

These acceptance definitions are specification targets; `TD-CI-001` currently defers executable-CI trust but does not alter their meaning.

---

# 12. Relationship to older geometry documents

`03_geometry_operation_model.md`, `04_base_template.md` and `05_parametric_orthosis_geometry.md` are retained as architecture/math hypotheses.

Where they conflict with this document:

```text
16_geometry_authoring_contract.md wins for product/domain semantics
01_coordinate_registration.md wins for coordinates/side/transform semantics
18_numerical_qualification_registry.md wins for numeric-governance rules
```

No statement in this contract should be interpreted as freezing OpenSubdiv or any other geometry library.

---

# 13. Freeze record

The freeze criteria have been reviewed and are satisfied at documentation level:

1. all P0 operation families required by Functional v2 have a semantic envelope;
2. placement and physical dose are typed and unit-bearing;
3. bilateral/mirror behavior is explicit and side-aware;
4. capture condition and landmark provenance are represented;
5. section/distance/angle/thickness/deviation inspection semantics are explicit;
6. clinical/contact-surface intent is separated from production realization;
7. numerical limits resolve through the frozen numerical registry rather than hidden literals;
8. the representative P0 authoring acceptance catalog can be specified without selecting a geometry kernel.

Freeze evidence:

```text
docs/validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md
docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md
docs/validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md
docs/TRACEABILITY_MATRIX.md
```

**Change control:** normative semantic changes to this contract require an explicit superseding decision/version. Algorithm implementation, geometry-kernel selection, performance optimization and qualified numerical values may evolve without reopening this semantic freeze provided they continue to satisfy this contract.