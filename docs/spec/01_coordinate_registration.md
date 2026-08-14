# 01 — Coordinate and Registration Contract

**Status:** FROZEN semantic baseline v1; real acquisition/registration tolerances remain explicitly `OPEN`  
**Date:** 2026-08-14  
**Scope:** kernel-independent coordinate, orientation, laterality, calibration and registration contract for BiomechE-CAD.  
**Depends on:** Functional Specification v2, Project Schema v0, Functional Acceptance Suite v0.  

> This specification freezes *meaning*, not a geometry-kernel implementation. OpenSubdiv vs openNURBS/ON_SubD remains parked.

---

## 1. Purpose

BiomechE-CAD consumes data whose array layout, device coordinates, anatomical meaning and CAD coordinates are not automatically the same thing. This contract prevents a numerically valid transform or plausible screen image from silently changing side, medial/lateral meaning, physical units or anatomical placement.

Normative rule:

```text
storage/index topology
    != physical sensor geometry
    != exam/device coordinates
    != anatomical coordinates
    != CAD coordinates
```

Every crossing between those domains SHALL be explicit and provenance-bearing.

The contract is deliberately compatible with the BiomechE distinction between matrix indexing, physical sensor geometry and `ExamFrame2D`; memory orientation SHALL NOT be used to infer physical orientation.

---

## 2. Normative language

`SHALL` / `MUST` = P0 contract.  
`SHOULD` = default unless a recorded reason exists.  
`MAY` = optional.  
`OPEN` = intentionally not yet qualified; no implementation may replace it with an undocumented constant.

---

## 3. Canonical units

BiomechE-CAD uses the already-frozen BiomechE physical units:

```text
distance  mm
time      s
force     N
pressure  kPa
angle     deg
area      mm²
```

Matrix indices are dimensionless indices, not millimetres. Pixel coordinates are pixels, not millimetres. A transform between two frames MUST state the units of both frames and any required scale/calibration explicitly.

Internally, trigonometric implementations MAY use radians, but persisted prescription angles remain `deg` unless a field explicitly says otherwise.

---

## 4. Coordinate-domain taxonomy

### 4.1 Matrix index frame

A pressure matrix address is the ordered pair:

```text
(row, column)
```

with integer topology only. The canonical convention is:

```text
row    increases with storage row index
column increases with storage column index
```

No anatomical direction is implied. `row + 1` does **not** mean anterior, posterior, medial, lateral, left or right unless an explicit physical mapping says so.

A source SHALL persist enough information to reconstruct its matrix topology, including width/height and stride/order where relevant.

### 4.2 Device/platform metric frame

A pressure platform SHALL expose physical sensor positions/represented areas or an equivalent explicit map. For a regular grid the map MAY be represented by:

```text
p_platform(row, column)
  = origin_center
  + column * column_step_vector
  + row    * row_step_vector
```

where vectors are in `mm` and carry the physical orientation. Irregular sensor layouts SHALL store sensor centres/areas explicitly rather than forcing them into a fictitious regular grid.

### 4.3 BiomechE exam frame

The current BiomechE 2D examination abstraction is treated as an explicit adapter frame. Its subject-centric metric basis is:

```text
+X_exam = posterior -> anterior
+Y_exam = subject RIGHT -> subject LEFT
```

BiomechE-CAD SHALL import the actual frame/geometry metadata associated with the acquisition, not assume that raw matrix X/Y equals these directions.

### 4.4 Source scan/image frames

A Scan3D or Image2D source MAY arrive in any vendor/device orientation. The source frame SHALL therefore be named and persisted before registration. Orientation is never inferred merely because a mesh or image appears visually upright.

### 4.5 Canonical CAD/anatomical 3D frame

`CAD-ANAT-1` is a **right-handed, subject-centric** frame used for both feet:

```text
+X = heel/posterior -> distal/anterior/forefoot
+Y = subject RIGHT -> subject LEFT
+Z = plantar/support-plane side -> dorsal/superior

X × Y = Z
```

The frame is intentionally the same handedness for LEFT and RIGHT objects. A left orthosis does not receive a left-handed Cartesian coordinate system.

The canonical origin SHALL be explicitly bound to the source used to establish the anatomical frame. For the initial H/M1/M5 landmark frame it is the posterior heel landmark `H`. If another qualified origin is used later, the frame receives a different `conventionVersion`; it is never silently substituted into `CAD-ANAT-1`.

---

## 5. LEFT / RIGHT ownership

`side` is the **patient/subject anatomical side**. It is not:

- screen left/right;
- matrix left/right;
- the sign of an arbitrary vendor coordinate;
- camera/view orientation;
- file naming convention.

P0 entities that have anatomical ownership SHALL carry or resolve an explicit side. At minimum this applies to orthosis projects, design revisions, side-specific acquisitions/frames/landmarks/ROIs, operations, manufacturing artifacts and physical orthoses where applicable.

A side mismatch SHALL be a validation failure unless an explicit bilateral/cross-side operation describes the relationship.

No function may infer side solely from a mesh centroid, pressure footprint location, filename, image appearance or sign of a coordinate.

---

## 6. Medial / lateral semantics

Because `+Y` is subject-left for **both** feet:

| Anatomical side | medial direction in `CAD-ANAT-1` | lateral direction |
|---|---:|---:|
| RIGHT | `+Y` | `-Y` |
| LEFT | `-Y` | `+Y` |

Therefore `MEDIAL` and `LATERAL` SHALL be stored as anatomical semantics, not as an unqualified Cartesian sign.

A parameter named only `yMedial` without side/frame context is invalid for persisted cross-side prescription semantics.

---

## 7. Foot-intrinsic `s/q` anatomical coordinates

BiomechE-CAD defines a side-normalized intrinsic 2D coordinate for anatomy-aware placement:

```text
s : longitudinal, 0 heel/posterior -> 1 distal/forefoot
q : transverse,  -1 lateral -> 0 centre -> +1 medial
```

`s/q` are semantic/anatomical coordinates. They are **not** a second Cartesian frame and are not assumed to be isometric or linear in physical millimetres.

Important consequence:

```text
RIGHT medial q > 0
LEFT  medial q > 0
```

while the Cartesian `Y` sign differs by side.

Any mapping `s/q <-> CAD mm` SHALL identify the template/foot-domain version and algorithm used. The historical geometry-hypothesis document is superseded wherever it implied that semantic mirroring must negate `q`.

---

## 8. Scan3D anatomical landmark frame

### 8.1 Initial landmark set

The first P0 Scan3D registration profile uses these semantic landmarks:

```text
H  = posterior heel/calcaneal landmark
M1 = first metatarsal-head landmark
M5 = fifth metatarsal-head landmark
F  = (M1 + M5) / 2
```

This landmark family is a practical anatomical registration baseline; a later richer foot model may add landmarks without silently changing this convention.

### 8.2 Frame construction

Given source-frame landmark coordinates:

```text
x0 = normalize(F - H)
```

Construct a subject-left transverse witness:

```text
RIGHT: y_candidate = M1 - M5
LEFT:  y_candidate = M5 - M1
```

Remove its component parallel to `x0`:

```text
y0 = normalize(y_candidate - dot(y_candidate, x0) * x0)
z0 = normalize(x0 × y0)
y0 = normalize(z0 × x0)
```

The origin is `H` and the resulting basis is right-handed.

### 8.3 Dorsal sign cannot be guessed

The three plantar/anatomical landmarks alone do not uniquely prove which normal points dorsally. A Scan3D import SHALL therefore provide an explicit dorsal/superior orientation witness, for example a device-axis declaration, an additional qualified landmark/normal or a source-frame contract.

If the witness conflicts with `z0`, the whole basis may be reoriented according to the documented algorithm, but the operation and source evidence SHALL be recorded.

If no trustworthy dorsal witness exists, orientation state is `UNRESOLVED`; the application SHALL ask for explicit resolution rather than choosing the visually convenient normal.

### 8.4 Degenerate geometry

Registration SHALL fail or become unresolved when landmarks are coincident or the transverse vector becomes numerically degenerate after orthogonalization. The minimum qualified separations/conditioning thresholds are currently `OPEN` and require scanner/landmark qualification; no clinical millimetre threshold is invented here.

---

## 9. Pressure indexing and physical axes

Pressure remains quantitative data in `kPa`; a heatmap is only a derived view.

A pressure import SHALL preserve, independently:

1. numeric samples;
2. matrix topology `(row,column)` and stride/order;
3. physical sensor centre/represented-area geometry in `mm`;
4. device/platform frame identity;
5. BiomechE/exam frame when available;
6. registration from the relevant physical/exam frame to the CAD/anatomical frame;
7. side and acquisition provenance.

A resampled heatmap or image SHALL NOT become the authoritative source for metric pressure analysis.

### 9.1 Pressure transform chain

The normal BiomechE bridge is:

```text
(row, column)
   -- explicit sensor geometry --> p_platform_mm
   -- device/exam transform ----> p_exam_mm
   -- registration -------------> p_CAD_mm
```

Any identity step MUST be an explicit identity by contract, not an omitted assumption.

The adapter for current BiomechE `ExamFrame2D` uses its explicit anterior and subject-left axes. BiomechE foot-local transverse semantics are lateral→medial on both feet, which is compatible with CAD intrinsic `q`; adapter code SHALL map by **meaning**, not by reusing a variable name from another algorithm.

---

## 10. Image2D calibration frame

An Image2D acquisition starts in pixel coordinates:

```text
u = column/pixel-x
v = row/pixel-y
```

Pixel origin/direction SHALL be recorded as source-image metadata. No physical size is implied until calibration exists.

For a qualified planar image the calibration may be represented as a homography:

```text
[x_mm, y_mm, w]^T = H_metric_from_pixel * [u, v, 1]^T
```

followed by division by `w`.

A simple scale + rotation + translation is permitted only when justified by the acquisition geometry. Perspective and lens distortion SHALL not be silently collapsed into a single mm-per-pixel scalar when they are material to the measurement.

The calibration record SHALL identify calibration method, source target/reference, timestamp/version where relevant, residual/error metrics when available and provenance.

Real calibration accuracy/tolerance is `OPEN` pending actual Image2D acquisition-system qualification.

---

## 11. Source -> target transform convention

### 11.1 Naming and direction

A transform is named:

```text
T_target_from_source
```

and means exactly:

```text
p_target = T_target_from_source * p_source
```

The Project Schema `Registration` fields bind the same direction:

```text
sourceFrameId -> targetFrameId
transformData.convention = "SOURCE_TO_TARGET"
```

A matrix without direction metadata is invalid persisted registration state.

### 11.2 Vector convention

BiomechE-CAD uses **column vectors** for normative transform algebra.

3D homogeneous point:

```text
p = [x, y, z, 1]^T
```

2D homogeneous point:

```text
p = [x, y, 1]^T
```

### 11.3 Composition

If:

```text
p_B = T_B_from_A * p_A
p_C = T_C_from_B * p_B
```

then:

```text
T_C_from_A = T_C_from_B * T_B_from_A
```

Code review/tests SHALL reject APIs whose multiplication order is ambiguous.

### 11.4 Inverse

For an invertible registration:

```text
T_source_from_target = inverse(T_target_from_source)
```

The inverse need not be separately persisted unless it has independent provenance; it SHOULD normally be derived from the authoritative source→target transform.

---

## 12. Matrix serialization

Normative algebra and textual array layout are separate concepts.

Persisted matrices use nested JSON arrays in **row-major textual order**:

```json
{
  "convention": "SOURCE_TO_TARGET",
  "vectorConvention": "COLUMN",
  "matrixLayout": "ROW_MAJOR_SERIALIZATION",
  "matrix4x4": [
    [1, 0, 0, 10],
    [0, 1, 0, -5],
    [0, 0, 1, 2],
    [0, 0, 0, 1]
  ],
  "units": "mm"
}
```

This example translates a column-vector point by `[10,-5,2] mm`. It does not define an in-memory C/C++/GPU layout. Bindings MAY store matrices differently internally, but serialization SHALL preserve the stated algebra exactly.

Rigid registration SHALL preserve distance and have rotation determinant `+1` within its computational validation tolerance. A determinant `-1` reflection is not a rigid registration.

Similarity/affine/projective transforms, when needed, SHALL be typed explicitly; they may not masquerade as rigid transforms.

---

## 13. Project Schema v0 binding

### `FrameDefinition`

At minimum persists:

```text
frameId
frameType
units
conventionVersion
side when anatomical/side-owned
human-readable description when needed
```

Vendor/device-specific axis metadata MAY live in extension payloads until promoted into the schema, but SHALL not be discarded.

### `Registration`

At minimum persists:

```text
registrationId
sourceFrameId
targetFrameId
transformType
transformData with SOURCE_TO_TARGET convention
method
algorithmRef when applicable
errorMetrics
qualityState
createdAt / createdBy
provenanceRecordId
```

### `Acquisition`

The acquisition SHALL reference the source physical frame and raw immutable evidence. Matrix index mapping may be stored in protocol/extension metadata while Project Schema v0 remains implementation-neutral.

---

## 14. Mirror semantics

### 14.1 Mirror is not registration

Bilateral mirror/copy is a **semantic design transformation** that creates a distinct target-side revision. It SHALL NOT be stored as though a reflected 4×4 matrix were an ordinary rigid registration.

### 14.2 Cartesian reflection

Under `CAD-ANAT-1`, the ideal bilateral Cartesian reflection is:

```text
x' =  x
y' = -y
z' =  z
```

Its linear determinant is `-1`; therefore it is a reflection, not a proper rigid-body rotation.

### 14.3 Intrinsic semantics

For a semantic RIGHT↔LEFT mirror:

```text
s' = s
q' = q
MEDIAL remains MEDIAL
LATERAL remains LATERAL
```

Side changes explicitly. Any side-qualified operation, ROI, landmark or prescription is remapped to the target side while preserving anatomical meaning.

### 14.4 Provenance/immutability

The source committed `DesignRevision` remains immutable. The mirror creates a distinct target-side revision/operation identity and records provenance linking source and result. Editing the mirrored copy never mutates the source revision.

A double semantic mirror SHALL reproduce the original semantic prescription modulo newly generated entity IDs/provenance timestamps.

---

## 15. Registration provenance

Every persisted registration SHALL make it possible to answer:

```text
what frames were related?
what exact direction?
which landmarks/calibration/source evidence were used?
who/what created it?
which algorithm/version?
when?
what residual/error/quality metrics were available?
was manual intervention involved?
```

Raw source evidence remains immutable/hash-addressable. Re-registration creates a new registration entity; it does not rewrite the old transform in place when that transform is already referenced by a committed revision/outcome.

---

## 16. No silent orientation inference

The following are explicitly forbidden as authoritative orientation rules:

- array row/column direction;
- image display orientation or EXIF alone;
- mesh bounding-box long axis alone;
- positive coordinate sign without frame metadata;
- filename containing `L`/`R`;
- visual pressure footprint position;
- UI camera/view orientation;
- whichever normal points toward the current camera.

If orientation, side or calibration is unknown, the state SHALL be represented as unknown/unresolved and surfaced for explicit resolution.

---

## 17. Tolerance classes

Tolerance is typed; there is no single universal `epsilon`.

### 17.1 Semantic/canonical exactness

The following are exact logical requirements:

- side identity;
- frame identity/version;
- transform direction convention;
- units labels;
- definition `id + version + hash` resolution;
- mirror preservation of intrinsic `s/q` meaning;
- revision/provenance links.

These are not fuzzy numerical comparisons.

### 17.2 Synthetic computational fixtures

`fixtures/acceptance/registration-known-transform.json` uses an analytically known rigid transform. Its `1e-12 mm` tolerance is a **computational fixture tolerance only** for simple double-precision arithmetic.

It SHALL NOT be copied into scanner, pressure-platform, landmark, Image2D or manufacturing acceptance criteria.

### 17.3 Real acquisition/registration tolerances

The following remain `OPEN` until justified by actual devices/protocols and qualification data:

```text
pressure sensor physical-position tolerance
pressure platform -> ExamFrame registration error
Scan3D landmark repeatability / registration residual
Image2D calibration error
automatic side/orientation classifier confidence, if one is ever allowed as suggestion
cross-modality pressure/scan registration tolerance
```

A future limit SHALL identify the acquisition system, protocol, metric, population/fixture where relevant and qualification evidence. A generic literature number is not sufficient to become a product acceptance constant.

### 17.4 Manufacturing coordinates

Manufacturing frame positioning and orientation are downstream provenance and SHALL be explicit. The project already records ISO 17295 as vocabulary context for AM positioning/orientation [STD-ISO-17295-2023, official Abstract/Scope]. Product-specific manufacturing dimensional tolerances remain part of manufacturing qualification, not this anatomical registration contract.

---

## 18. Round-trip invariants

### Registration

For a qualified invertible transform and points inside the qualified working domain:

```text
p_source
 -> T_target_from_source
 -> inverse(T_target_from_source)
 -> p_source_recovered
```

error SHALL be within the tolerance class declared for that fixture/system.

### Serialization

Serialize→parse SHALL preserve matrix numbers, frame IDs, direction, units and vector/layout conventions without transposition or implicit inversion.

### Mirror

RIGHT→LEFT→RIGHT SHALL preserve the source semantic prescription (`s`, `q`, medial/lateral role, dose, units and anatomical reference), while entity IDs/provenance may legitimately differ.

### Pressure mapping

Where an exact inverse mapping exists, matrix-address→physical-coordinate→matrix-address SHALL recover the same sensor address. For irregular geometry, nearest-sensor lookup is not automatically an inverse and SHALL have separately specified semantics.

---

## 19. Acceptance fixture binding

Current kernel-independent fixtures:

| Fixture | Contract exercised |
|---|---|
| `fixtures/acceptance/mirror-semantics.json` | side change, semantic medial/lateral preservation, `s/q`, immutable source |
| `fixtures/acceptance/registration-known-transform.json` | source→target direction, column-vector math, known transform |
| `fixtures/acceptance/roi-version-comparison.json` | frame-bound ROI version identity and no silent comparison |
| `fixtures/project/pressure-design-outcome-loop.json` | pressure index/metric/CAD frames, registration and measured outcome loop |

`tools/validate_fixtures.py` executes the schema-level and cross-domain checks that do not need final geometry.

---

## 20. BiomechE integration requirements carried forward

`docs/spec/11_biomeche_integration.md` SHALL define the concrete adapter from the BiomechE acquisition contract without duplicating biomechanical algorithms. It MUST preserve:

1. acquisition and device identity;
2. numeric pressure data and units;
3. matrix topology independently from physical sensor geometry;
4. `SensorGeometry`/equivalent physical centres and represented areas;
5. `ExamFrame2D` anterior/subject-left axes;
6. side/foot ownership;
7. source protocol and quality/provenance;
8. the exact registration used by a design/outcome revision;
9. compatibility rules for pre/post comparison.

No CAD code may assume that a BiomechE pressure matrix is already oriented like a CAD viewport.

---

## 21. OPEN items

The semantic coordinate contract is frozen, but these qualification items intentionally remain open:

- real Sensor Medica/BiomechE pressure hardware sensor-position and registration tolerances;
- selected Scan3D device coordinate declarations and landmark repeatability;
- selected Image2D calibration method/device tolerances;
- automatic landmark detection acceptance limits;
- cross-modality pressure↔scan registration limits;
- exact algorithm for mapping intrinsic `s/q` to each future template family;
- whether additional anatomical landmarks are mandatory for specific workflows;
- manufacturing-machine positioning tolerances per qualified process/profile.

These OPEN items do **not** reopen axis meaning, handedness, LEFT/RIGHT semantics, transform direction, mirror semantics or matrix-vs-physical separation.

---

## 22. Frozen decisions

1. `CAD-ANAT-1` is right-handed and subject-centric: `+X` heel→distal, `+Y` subject-right→subject-left, `+Z` plantar→dorsal.
2. LEFT/RIGHT is patient anatomical ownership, never display/storage orientation.
3. medial Cartesian sign is side-dependent; anatomical `MEDIAL/LATERAL` is explicit.
4. intrinsic `s` is heel→distal and intrinsic `q` is lateral→medial for **both** feet.
5. bilateral semantic mirror reflects canonical `Y` but preserves `s/q` anatomical meaning; mirror is not rigid registration.
6. pressure `(row,column)` is storage topology only; physical sensor geometry is explicit.
7. BiomechE pressure reaches CAD through explicit physical/exam frames and registration.
8. Scan3D H/M1/M5 defines the initial longitudinal/transverse anatomical basis, with an independent dorsal-orientation witness.
9. Image2D starts in pixel coordinates and becomes metric only through explicit calibration.
10. persisted transforms use `T_target_from_source`, column-vector algebra, row-major textual arrays and explicit composition order.
11. unknown orientation is represented as unknown; no silent inference.
12. real-world tolerances remain qualification-specific `OPEN` values until evidence exists.

---

## 23. Evidence / internal contract notes

- AM part positioning/orientation vocabulary: [STD-ISO-17295-2023, official Abstract/Scope].
- The BiomechE sibling repository is the authoritative integration-side implementation contract for matrix geometry, `ExamFrame2D` and current foot-axis semantics; `11_biomeche_integration.md` shall pin the exact BiomechE revision used by the adapter.
- ISB global-coordinate and foot-kinematics recommendations and the H/M1/M5 COP-registration literature were reviewed while freezing this contract; their canonical bibliography entries are added in the same checkpoint before being used for scientific claims.

This specification makes product choices explicit where interoperability requires a single convention. It does not claim that the chosen CAD axes are the only scientifically valid coordinate convention.
