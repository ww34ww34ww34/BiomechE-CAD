# BiomechE-CAD — Geometry Operation Model & Canonical Orthosis Cage

**Status:** design baseline / OpenSubdiv-first hypothesis  
**Date:** 2026-08-14  
**Scope:** define the authoritative geometric model, the canonical orthosis control cage, operation-stack semantics, OpenSubdiv integration, field/mask engine and manufacturing handoff for a vertical foot-orthosis CAD.

> This document separates **source evidence**, **user-provided implementation fact**, **engineering inference** and **BiomechE-CAD decisions**. It does not claim to reverse-engineer EasyCAD2 internals.

---

## 1. Evidence baseline

### 1.1 Primary EasyCAD2 evidence

The EasyCAD2 manual 1.1.x.x and validation 1.4.x.x confirm a workflow centered on:

- editable DIMA outline and dimensions;
- 3D mesh editing and direct XYZ vertex editing;
- heel/wrap/camber, medial/lateral arch and wedge parameters;
- elements positioned/scaled/rotated on the orthosis mesh;
- `SOMMA` and `INTERSEZIONE` element integration modes described relative to upper/lower orthosis surfaces;
- custom element vertex editing;
- local sculpt by radius/strength;
- global deformation conforming the mesh to scan data;
- arbitrary section, distance, height and thickness checks;
- minimum-thickness correction;
- STL/GCODE production.

Source locators:

- `EasyCAD2 Manuale ITA 2.0.pdf`, software 1.1.x.x, 13/01/2024, especially DIMA pp. 14–18, MODIFICA pp. 23–30, ELEMENTI pp. 31–35, POST PROCESSING pp. 36–41, CONTROLLO pp. 42–44, PRODUCI pp. 44–50.
- `PdV0001_EasyCAD2 software validation plan.pdf`, 15/01/2026, US6–US24.
- `RdT001_Rapporto di Test ... 1.4xx.pdf`, 20/01/2026, US6–US24 PASS.

### 1.2 User-provided implementation fact

The project owner states with certainty that EasyCAD2 uses **OpenSubdiv**.

This is accepted as project context. It is not stated in the EasyCAD2 manual/validation documents, therefore the exact internal role of OpenSubdiv remains an inference until independently proven from binaries/build metadata/source provenance.

### 1.3 OpenSubdiv facts from official documentation

OpenSubdiv:

- evaluates subdivision surfaces at high performance on CPU/GPU;
- is optimized for deforming surfaces with static topology at interactive frame rates;
- receives mesh/cage data from the host application rather than creating assets itself;
- exposes subdivision surfaces as smooth limit surfaces over polygonal control cages;
- supports arbitrary topology, but regular quad-dominant regions are simpler and more predictable;
- explicitly warns that an arbitrary polygonal mesh is not automatically a good subdivision cage.

Reference:

- https://www.opensubdiv.org/docs/intro.html
- https://www.opensubdiv.org/docs/subdivision_surfaces.html

---

## 2. Architectural conclusion

BiomechE-CAD should not start from a general-purpose NURBS/B-Rep feature tree.

The preferred P0 model is:

```text
Canonical Orthosis Control Cage
        +
Persistent anatomical parameterization
        +
Versioned parametric deformation operations
        +
Mask / field engine
        +
OpenSubdiv limit-surface evaluation
        +
Scan/query/DFM modules
        +
Procedural production-solid generation
```

This is a **vertical orthosis CAD**, not a mechanical CAD.

NURBS/B-Rep/STEP remain optional adapter capabilities to be introduced only when a concrete use case requires them.

---

## 3. Authoritative representations

### 3.1 Clinical design geometry — P0

The authoritative clinical shape is a **control cage plus operation stack**, not the final tessellated STL.

```text
BaseCage + Operations + AlgorithmVersions = ClinicalDesignRevision
```

### 3.2 OpenSubdiv limit surface — derived P0

The smooth subdivision limit surface is derived deterministically from the evaluated cage and subdivision settings.

It is used for:

- interactive visualization;
- smooth surface queries where appropriate;
- high-quality tessellation;
- inspection/sections;
- manufacturing surface generation.

### 3.3 Acquisition mesh — independent authoritative evidence

A Scan3D STL is not converted into the control cage and does not become the design model.

It remains an acquisition asset with:

```text
source file
units
coordinate frame
registration transform
landmarks
quality/provenance
```

### 3.4 Production mesh/solid — derived artifact

The manufacturing body is derived from:

```text
Clinical limit surface
+ ThicknessField
+ ClosureProfile
+ MaterialRegion[]
+ ManufacturingProfile
```

STL/GCODE are export artifacts bound to an immutable project revision.

---

# 4. Canonical Orthosis Cage

## CAGE-001 — stable topology — P0

For a template family, topology SHOULD remain stable during ordinary clinical editing.

Stable means:

- same persistent vertex IDs;
- same face connectivity;
- same semantic vertex/face groups;
- modifications primarily alter control-point positions and attributes.

Topology-changing operations are exceptional and must be explicit/versioned.

## CAGE-002 — quad-dominant topology — P0

The canonical cage SHOULD be predominantly quad-based to align well with Catmull-Clark/OpenSubdiv.

Extraordinary vertices are allowed where necessary but should be:

- minimized;
- kept away from high-curvature/high-edit zones where practical;
- explicitly included in geometry regression fixtures.

## CAGE-003 — persistent IDs — P0

Every control vertex has a stable ID independent of its position:

```text
vertex_id
base_position
current_position
anatomical_uv
region_weights
flags
```

Persistent IDs enable:

- deterministic operations;
- template morphing;
- left/right mirroring;
- saved masks;
- clinical feature replay;
- regression testing;
- project migration.

## CAGE-004 — anatomical parameterization — P0

Each cage point shall have a topology-stable orthosis parameter coordinate:

```text
s ∈ [0,1]   heel -> distal/toe
q ∈ [-1,1] lateral -> medial
```

These coordinates are **intrinsic design coordinates**, not global XYZ and not sensor matrix indices.

They survive scale, mirror and ordinary deformation.

The exact relationship to global/anatomical coordinate frames is finalized in `01_coordinate_registration.md`.

## CAGE-005 — semantic regions — P0

Precompute reusable weights/masks such as:

```text
HEEL
REARFOOT
MIDFOOT
FOREFOOT
MEDIAL
LATERAL
MEDIAL_ARCH
LATERAL_ARCH
METATARSAL
HALLUX
FIFTH_MET
BOUNDARY
HEEL_BOUNDARY
FOREFOOT_BOUNDARY
```

A region can be crisp or weighted `[0,1]`.

## CAGE-006 — bilateral correspondence — P0

LEFT and RIGHT should share compatible topology and semantic IDs.

Mirror must transform:

- geometry;
- anatomical `q` sign;
- MEDIAL/LATERAL semantics;
- wedge/posting semantics;
- ROI and element placement.

## CAGE-007 — template family compatibility — target P0

SPORT, SANDALO, CLASSIC, COMFORT, DONNA-like templates should preferably use compatible cage topology and differ mainly by:

- control-point positions;
- outline/boundary target;
- semantic parameters;
- allowed production profiles.

If a template requires incompatible topology, it becomes a different `CageTopologyFamily` and cross-family morphing is not guaranteed.

## CAGE-008 — upper clinical surface vs production body — P0 decision

BiomechE-CAD will treat the **upper clinical surface cage** as the primary shape-authoring representation.

The lower surface and sidewalls are manufacturing geometry derived later from thickness/closure semantics.

Reason:

- most EasyCAD2 clinical operations describe shape of the contact/support surface;
- this maximizes topology stability;
- thickness and closure can vary by process without changing clinical prescription.

This is a BiomechE-CAD design decision, not a claim about EasyCAD2 internals.

---

# 5. OpenSubdiv integration contract

## OSD-001 — OpenSubdiv is evaluator, not domain model — P0

No project/business type shall expose OpenSubdiv types publicly.

```text
BiomechCage
 -> OpenSubdiv adapter
 -> LimitSurfaceEvaluator
```

## OSD-002 — subdivision scheme — P0

Initial target: Catmull-Clark for quad-dominant canonical cage.

Scheme/options must be serialized:

```text
scheme
boundary interpolation
crease rules
fvar rules if used
OpenSubdiv compatibility version
```

## OSD-003 — cage/limit separation — P0

UI and algorithms must explicitly distinguish:

- control cage;
- evaluated limit surface;
- tessellated display/manufacturing mesh.

Measurements must state which representation they use.

## OSD-004 — interactive invalidation — P0

If topology is unchanged, moving control points should invalidate only primvar/evaluation results, not rebuild the entire project model.

## OSD-005 — deterministic tessellation — P0

For a frozen project revision and manufacturing profile, tessellation must be reproducible within declared numerical tolerance.

## OSD-006 — derivatives — P1/P0 where needed

Expose limit-surface position and first derivatives/normals for:

- inspection;
- surface-normal displacement;
- section/measurement;
- local curvature-aware operations if later required.

---

# 6. Field / mask engine

The core abstraction for clinical shape modification is a scalar/vector field defined over intrinsic orthosis coordinates and/or cage vertices.

## FIELD-001 — scalar mask — P0

```text
Mask(v) -> [0,1]
```

Sources:

- semantic anatomical region;
- polygon ROI;
- circle/ellipse;
- brush radius;
- longitudinal interval;
- pressure ROI;
- scan-derived region;
- saved custom mask.

## FIELD-002 — displacement field — P0

```text
D(v) -> Vector3
```

An operation can displace by:

- global Z;
- current surface normal;
- anatomical axis;
- local frame;
- target projection delta.

The chosen direction is part of operation semantics and serialization.

## FIELD-003 — compact smooth falloff — P0

All local operations shall support smooth compact falloff to avoid discontinuities.

Baseline helper:

```text
smoothstep(x) = x²(3 - 2x), clamped to [0,1]
```

Higher-order alternatives may be added but algorithm version must be recorded.

## FIELD-004 — composition — P0

Field composition modes:

```text
ADD
MAX
MIN
MULTIPLY_MASK
TARGET
BLEND_TO_TARGET
CLAMP
```

Clinical operators should use named semantic modes rather than raw arbitrary booleans.

---

# 7. Operation stack

## OP-001 — immutable operation record — P0

Each operation stores at least:

```text
operation_id
type
side
enabled
parameters + units
intrinsic ROI/mask reference
source dataset reference [optional]
algorithm_id
algorithm_version
created_at
author
clinical rationale [optional]
```

## OP-002 — deterministic replay — P0

Rebuilding from the same base template + same operation list + same algorithm versions must produce geometrically equivalent output within tolerance.

## OP-003 — operation classes — P0

```text
TemplateMorphOperation
RigidTransformOperation
HeelWrapOperation
MedialArchOperation
LateralArchOperation
RearfootWedgeOperation
ForefootWedgeOperation
CorrectiveElementOperation
SculptOperation
SmoothOperation
ScanConformOperation
HeightConstraintOperation
ThicknessOperation
DFMFixOperation
MaterialModifierOperation
ProductionClosureOperation
```

## OP-004 — recommended evaluation stages — P0

```text
A. Base template / size / outline
B. Global foot/template morph
C. Heel/wrap/camber
D. Arch operators
E. Wedges/posting
F. Corrective elements
G. Sculpt/local ROI edits
H. Scan-conform operations
I. Geometry constraints / height fixes
J. Clinical limit-surface evaluation
K. Thickness + production closure
L. DFM checks/fixes
M. Manufacturing tessellation/export
```

An operation may declare its stage and dependencies. Reordering across incompatible stages is prohibited or explicitly resolved.

## OP-005 — non-destructive by default — P0

The operation stack, not a baked vertex array alone, is persisted as the primary design history.

A cached evaluated cage is allowed for performance but is disposable/rebuildable.

## OP-006 — local sculpt capture — P0

Sculpt must be replayable.

Two allowed representations:

1. compact brush-event sequence;
2. sparse persistent vertex displacement layer keyed by stable vertex IDs.

The second is preferred after stroke consolidation for deterministic compact replay.

---

# 8. Corrective elements without general-purpose B-Rep

## ELEM-001 — element model — P0

A corrective element is a clinically named modifier, not necessarily an independent CAD solid.

```text
CorrectiveElement
  id
  category
  canonical shape/field/cage
  position(s,q)
  rotation
  scale_x/y/z
  integration_mode
  material override [optional]
```

## ELEM-002 — preferred P0 representation

P0 elements should preferably be implemented as one of:

- analytic/parametric displacement fields;
- canonical element control cages sampled/projected onto the orthosis;
- compact height/support functions in intrinsic coordinates.

Arbitrary imported solid boolean is not a P0 requirement.

## ELEM-003 — EasyCAD2-style integration semantics — P0

EasyCAD2 documents `SOMMA` relative to upper-surface vertices and `INTERSEZIONE` relative to the lower-surface quota.

BiomechE-CAD therefore defines semantic modes:

```text
ADD_FROM_TOP
PLACE_FROM_BASE
```

The exact numeric formula is ours and versioned; it must reproduce clinically expected behavior and be validated against fixtures.

## ELEM-004 — custom element — P1

Custom element editing may manipulate the element cage vertices and save a reusable versioned preset.

---

# 9. Scan integration

OpenSubdiv does not replace scan processing.

P0 scan layer needs:

```text
STL import
triangle mesh
units
landmarks heel/1st/5th
rigid registration
manual fine alignment
BVH / nearest point
crop/trim
surface distance
projection target
```

ICP may be P1 if landmark + manual alignment is sufficient for initial parity.

`ScanConformOperation` stores:

```text
source_scan_id
ROI
strength
max_displacement
projection_direction/method
residual metrics
```

---

# 10. Production geometry

## PROD-001 — no general shell requirement in P0

P0 does not require arbitrary B-Rep shell/offset.

It requires an orthosis-specific production body:

```text
UpperClinicalSurface
+ ThicknessField
+ LowerSurfaceRule
+ Sidewall/ClosureRule
```

## PROD-002 — thickness field — P0

```text
t(s,q) >= manufacturing_minimum(s,q, profile)
```

Thickness is a semantic field, not merely the result of a generic normal offset.

## PROD-003 — closure profiles — P0

At minimum:

```text
BRIDGE
STRAIGHT
OBLIQUE
HYBRID_ADVANCED
```

Each profile defines lower-surface and sidewall construction rules explicitly.

## PROD-004 — manufacturing validation — P0

Before export:

- watertight output;
- consistent orientation;
- no degenerate triangles;
- minimum thickness satisfied;
- self-intersection checks where applicable;
- unit/orientation sanity;
- deterministic STL.

General-purpose B-Rep booleans remain optional unless a future production feature proves their need.

---

# 11. What is deliberately NOT P0

The following are removed from the minimum orthosis CAD kernel contract:

```text
full NURBS surface authoring
trimmed-surface B-Rep
STEP/IGES
wire/face/shell/solid feature tree
full sketch constraint solver
general loft/sweep/revolve
surface sew/stitch
general shell/offset
fillet/chamfer kernel
general solid primitive catalog
general-purpose B-Rep boolean engine
```

They may return as P1/P2 adapters only when justified by concrete workflow/interoperability requirements.

---

# 12. Canonical cage qualification suite

Before coding clinical operators, build a cage fixture and verify:

## CQ-001 — baseline limit surface

- cage valid;
- no unexpected ripples;
- acceptable limit-surface deviation from intended template.

## CQ-002 — mirror

DX↔SX mirror preserves topology/IDs and swaps medial/lateral semantics.

## CQ-003 — template morph

SPORT/CLASSIC/COMFORT/DONNA/SANDALO-like shapes can be represented without topology break inside the chosen topology family.

## CQ-004 — extreme L/W

Boundary remains valid at supported size/proportion limits.

## CQ-005 — heel wrap

Maximum supported heel operation does not fold/invert cage or limit surface.

## CQ-006 — arch extremes

Medial/lateral arch parameter envelope remains smooth and non-self-intersecting.

## CQ-007 — wedge

2°, 4°, 6° target wedge measured on evaluated surface within tolerance.

## CQ-008 — corrective element

Metatarsal-bar element integrates without topology change and with smooth transition.

## CQ-009 — sculpt

Repeated local sculpt remains stable and reproducible.

## CQ-010 — scan conform

ROI moves toward target scan while protected regions stay within displacement tolerance.

## CQ-011 — production closure

All closure modes produce watertight manufacturing output.

## CQ-012 — minimum thickness fix

A deliberate sub-threshold zone is detected and corrected without violating protected clinical regions more than allowed.

---

# 13. Open questions to resolve experimentally

1. Exact cage resolution and edge-loop layout.
2. Whether one topology family can cover all template categories.
3. Placement of extraordinary vertices.
4. Boundary interpolation/crease strategy in OpenSubdiv.
5. Whether arch/heel operators displace along global Z, cage normal or anatomical frame by default.
6. Element internal representation: field vs small cage vs sampled patch.
7. Best representation of sculpt history.
8. Scan-conform projection semantics.
9. Production lower-surface algorithm per closure profile.
10. Whether any real use case eventually requires Manifold/CGAL/OCCT.

---

# 14. Decision gate before adding another geometry kernel

Do **not** add OCCT, CGAL, Manifold, openNURBS or another geometry kernel to P0 merely for capability completeness.

Add a dependency only if a named acceptance test cannot be implemented robustly with:

```text
our cage/topology layer
+ OpenSubdiv
+ focused scan/query algorithms
+ procedural production mesh code
```

Any new dependency must document:

- exact unmet capability;
- fixture reproducing the need;
- robustness gain;
- license/platform/WASM cost;
- data-conversion cost;
- whether the dependency enters the authoritative model or remains an adapter.

---

# 15. DONE / TODO

## DONE

- [x] EasyCAD2 primary geometry behavior reviewed.
- [x] OpenSubdiv role reclassified from optional SubD to P0 surface evaluator based on project-owner implementation knowledge.
- [x] General-purpose NURBS/B-Rep removed from P0 hypothesis.
- [x] Canonical cage requirements defined.
- [x] Stable vertex-ID and intrinsic anatomical parameterization defined.
- [x] Field/mask engine defined.
- [x] Non-destructive operation stack defined.
- [x] Corrective-element semantic integration defined without forcing solid booleans.
- [x] Production-body separation defined.
- [x] Cage qualification suite defined.

## TODO

- [ ] Freeze coordinate/registration contract.
- [ ] Design first quad-dominant cage fixture.
- [ ] Define supported size/proportion envelope.
- [ ] Implement Catmull-Clark OpenSubdiv proof of concept.
- [ ] Implement intrinsic `(s,q)` generation.
- [ ] Implement medial arch reference operator.
- [ ] Implement lateral arch reference operator.
- [ ] Implement heel/wrap/camber reference operator.
- [ ] Implement rearfoot/forefoot wedge reference operator.
- [ ] Implement metatarsal-bar element reference fixture.
- [ ] Execute CQ-001..CQ-012.
- [ ] Re-evaluate need for a second geometry kernel after tests, not before.
