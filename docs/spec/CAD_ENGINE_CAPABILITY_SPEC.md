# BiomechE-CAD — CAD Engine Capability Specification

**Version:** v2 — OpenSubdiv-first orthosis CAD  
**Status:** current capability baseline  
**Date:** 2026-08-14

> v2 supersedes the first B-Rep/NURBS-heavy capability draft. The earlier version remains preserved in Git history. The change is based on a direct EasyCAD2 functional audit plus the project-owner fact that EasyCAD2 uses OpenSubdiv.

---

## 0. Executive conclusion

BiomechE-CAD does **not** need the feature envelope of a general mechanical CAD to reproduce and improve the clinically relevant EasyCAD2 workflow.

The minimum geometry stack should be:

```text
CANONICAL ORTHOSIS CONTROL CAGE
+ OPENSUBDIV LIMIT-SURFACE EVALUATION
+ PARAMETRIC CLINICAL DEFORMATION ENGINE
+ MASK / FIELD ENGINE
+ SCAN / REGISTRATION / GEOMETRIC QUERIES
+ ORTHOSIS-SPECIFIC PRODUCTION BODY GENERATION
+ DFM / VALIDATION
```

The primary product object is:

```text
BaseCage + VersionedClinicalOperations
```

not:

```text
NURBS Faces + B-Rep Shell + General Feature Tree
```

and not merely:

```text
final STL triangle soup
```

---

# 1. Evidence and inference levels

## PRIMARY / EasyCAD2 documents

The EasyCAD2 manual and 1.4 validation confirm:

- DIMA 2D templates and editable dimensions;
- mesh/vertex editing;
- heel, arch and wedge modification;
- element placement/scale/rotation and custom element vertex editing;
- local sculpt and smoothing;
- scan-conforming deformation;
- sections, distances, heights, thickness checks;
- minimum-thickness correction;
- STL/GCODE production.

## USER-PROVIDED IMPLEMENTATION FACT

The project owner states that EasyCAD2 uses OpenSubdiv.

## OFFICIAL OPENSUBDIV FACTS

OpenSubdiv is a high-performance subdivision-surface evaluator designed for deforming surfaces with static topology at interactive frame rates. It works from polygonal control cages and exposes the smooth limit surface. It is not an asset/model creation application by itself.

Official references:

- https://www.opensubdiv.org/docs/intro.html
- https://www.opensubdiv.org/docs/subdivision_surfaces.html

## ENGINEERING INFERENCE

Combining the above makes a stable/mostly-stable control-cage architecture a strong hypothesis for this domain. This is an inference for BiomechE-CAD design, not a claim that EasyCAD2 uses exactly the same internal operation formulas.

---

# 2. P0 capabilities — required

## 2.1 Core math/types

```text
Point2/3
Vector2/3
Matrix/Transform
Frame/Plane
AABB/OBB
Ray/Segment
units and tolerances
```

## 2.2 Polygon/control-cage topology

```text
persistent vertices
edges
faces
quad-dominant cage
adjacency
boundary loops
stable IDs
semantic regions
crease/boundary attributes
```

P0 requirement is **editable control topology**, not general B-Rep topology.

## 2.3 OpenSubdiv integration

```text
Catmull-Clark
control-cage -> limit surface
boundary rules
creases where needed
position/normal/first derivative evaluation
deterministic tessellation
CPU implementation
GPU path where advantageous
```

## 2.4 Intrinsic anatomical parameterization

Each cage vertex must carry stable design coordinates independent of global XYZ:

```text
s : heel -> toe [0,1]
q : lateral -> medial [-1,1]
```

plus semantic region weights.

## 2.5 Template/DIMA operations

```text
template load
L/W scaling
unlocked proportions
outline/boundary adjustment
shoe-size mapping
custom template save
bilateral mirror
```

No NURBS requirement follows from this. A smooth 2D spline may be useful but can be local/internal.

## 2.6 Clinical parametric deformation

P0 named operations:

```text
HeelWrap
Camber
MedialArch
LateralArch
RearfootWedge
ForefootWedge
GlobalThickness
Flatten
```

Each is a deterministic field/constraint over the canonical cage, with units and algorithm version.

## 2.7 Mask/field engine

```text
anatomical masks
circle/ellipse/polygon ROI
saved custom ROI
longitudinal/transverse masks
smooth falloff
additive displacement
target displacement
blend-to-target
clamp/constraint
```

## 2.8 Corrective elements

P0 element semantics:

```text
clinical element library
position
rotation
scale X/Y/Z
ADD_FROM_TOP
PLACE_FROM_BASE
smooth integration
```

P0 does not require an arbitrary solid boolean engine.

## 2.9 Sculpt/edit

```text
vertex edit XYZ
brush raise/lower
radius
strength
falloff
local/global smooth
locked/protected regions
replayable sparse displacement layer
```

## 2.10 Scan/acquisition geometry

```text
STL triangle mesh import
unit handling
landmarks heel/1st/5th
rigid registration
manual fine alignment
crop
BVH/spatial index
closest point
ray/projection query
distance field/residuals
```

ICP is P1 unless P0 fixtures prove it necessary.

## 2.11 Geometric inspection

```text
cross-section by plane
diagonal/arbitrary section
point-point distance
local height
max/min height
wedge angle
arch height
surface distance
thickness query
height map
```

## 2.12 Production body

P0 needs an orthosis-specific production constructor:

```text
UpperClinicalSurface
+ ThicknessField
+ LowerSurfaceRule
+ SidewallRule
+ ClosureProfile
```

Closure profiles:

```text
BRIDGE
STRAIGHT
OBLIQUE
HYBRID_ADVANCED
```

This does not imply a general `Shell()` or arbitrary surface offset API.

## 2.13 DFM/mesh validation

```text
watertight output
consistent orientation
degenerate triangle detection
minimum thickness
self-intersection detection where applicable
unit/orientation sanity
reproducible STL
```

Targeted mesh repair can be implemented locally or delegated to a small auxiliary library if qualification tests prove the need.

## 2.14 Non-destructive project model

```text
versioned operations
undo/redo
stable IDs
algorithm versions
serialize/replay
immutable export revision
cache invalidation
```

---

# 3. P1 capabilities — useful but not initial blockers

```text
2D B-spline utility curves
advanced custom element cage editor
local topology refinement if actually needed
ICP registration
advanced mesh repair
adaptive tessellation/remeshing for production only
3MF
per-region material/stiffness export
surface curvature queries
geodesic brush distances
additional scan formats
positive mould generation
text emboss/deboss
```

A P1 capability may be provided by a focused library adapter without changing the authoritative control-cage model.

---

# 4. P2 / interoperability / R&D

```text
NURBS surface authoring
B-Rep
STEP/IGES
Rhino/3DM exact-surface interchange
trimmed surfaces
general loft/sweep/revolve
general shell/offset
fillet/chamfer kernel
general solid booleans
implicit/SDF modeling
lattice/metamaterials
multi-material geometric partitioning
FEM
pressure-outcome prediction
automatic optimization
AI-guided geometry
```

These capabilities should be added only against explicit use cases.

---

# 5. Explicit removals from the old P0

The first capability draft incorrectly promoted general-CAD functions to P0.

The following are now **removed from P0**:

```text
NURBS curves as mandatory domain primitive
NURBS surfaces
trimmed surfaces
B-Rep Vertex/Edge/Wire/Face/Shell/Solid model
join/sew of B-Rep faces
general trim/split surface modeling
general Boolean union/difference/intersection
general offset surface
general thicken/shell
loft/sweep/revolve/fill as product prerequisites
fillet/chamfer
STEP/IGES
large general-purpose primitive catalog
```

Reason: the validated EasyCAD2 user workflow can be covered without making them prerequisites, and OpenSubdiv strongly supports a control-cage/limit-surface architecture.

---

# 6. Primitive policy

Only retain primitives that directly support UI, selection, masks, measurements and tests.

## P0

```text
Point
Line/Segment
Polyline
Circle
Ellipse
Rectangle
Polygon
Plane
```

## Utility/P1

```text
Sphere/Capsule-like radial support function
Box/OBB for ROI and tests
```

Do not build a general solid primitive subsystem without a real product requirement.

---

# 7. Boolean policy

Do not equate EasyCAD2 `SOMMA` / `INTERSEZIONE` labels with general B-Rep booleans.

Manual evidence describes them relative to upper and lower orthosis surface vertices.

BiomechE-CAD P0 semantic operations are:

```text
ADD_FROM_TOP
PLACE_FROM_BASE
LOCAL_RELIEF
CLAMP_TO_REGION
```

A true mesh/solid boolean backend can be added later for imported arbitrary geometry, complex emboss/cut or production repair.

---

# 8. NURBS policy

## 8.1 Not required for clinical surface authority

The smooth surface authority is OpenSubdiv limit-surface semantics over a controlled cage.

## 8.2 B-spline utility curves may still be useful

For:

- DIMA outline interpolation;
- centerlines;
- profile/falloff curves;
- reporting/export helpers.

They do not justify a full NURBS CAD kernel.

## 8.3 Exact NURBS/B-Rep adapter trigger

Consider openNURBS/OCCT/etc. only if a requirement appears for:

```text
STEP/IGES
Rhino exact interoperability
industrial CAM requiring B-Rep
exact trimmed-surface exchange
external CAD round-trip
```

---

# 9. Candidate dependency policy

## OpenSubdiv

**P0 candidate / expected dependency.**

Role:

```text
subdivision topology refinement
limit-surface evaluation
normals/derivatives
interactive smooth surface
controlled tessellation
```

Not responsible for:

```text
clinical semantics
scan registration
project history
DFM rules
production closure
GCODE
```

## Second geometry library

**None by default.**

Manifold, CGAL, OCCT, openNURBS or alternatives must earn entry through a failing acceptance fixture.

---

# 10. Architecture acceptance suite

## A-001 Cage stability

Supported clinical edits preserve stable topology and IDs.

## A-002 Limit surface quality

No visible ripples/creases outside intentionally creased boundaries.

## A-003 Template envelope

Supported DIMA sizes/proportions remain valid.

## A-004 Mirror

DX↔SX geometry and semantics are equivalent.

## A-005 Heel extreme

No foldover/inversion.

## A-006 Arch extreme

No foldover/inversion; start/center/end metrics preserved.

## A-007 Wedge

2°, 4°, 6° measured within declared tolerance.

## A-008 Element integration

Metatarsal bar/dome integrates smoothly without topology change.

## A-009 Sculpt

Repeated brush operations remain deterministic.

## A-010 Scan conform

ROI converges toward target without violating protected regions.

## A-011 Production closure

Bridge/Straight/Oblique/Hybrid generate watertight output.

## A-012 Thickness fix

Sub-threshold fixture is detected and repaired.

## A-013 Round trip

Project save/load/replay reproduces cage/metrics within tolerance.

## A-014 Performance

Interactive cage editing + OpenSubdiv evaluation meets target frame/update budgets on supported hardware.

---

# 11. EasyCAD2 parity conclusion

The EasyCAD2 1.4 validation plan has 25 user stories. All 25 have an implementation path in the proposed architecture; geometry-heavy stories US6–US22/US24 do not require general B-Rep/NURBS as prerequisites.

See:

- `docs/validation/easycad2_geometry_parity.md`
- `docs/spec/03_geometry_operation_model.md`
- `docs/spec/05_parametric_orthosis_geometry.md`

This result is a **functional architecture parity**, not proof of EasyCAD2's internal implementation.

---

# 12. Final contract

The P0 CAD engine contract is now:

```text
CONTROL CAGE
+ STABLE IDS / ANATOMICAL UV
+ OPENSUBDIV LIMIT SURFACE
+ PARAMETRIC ORTHOSIS OPERATORS
+ MASK/FIELD COMPOSITION
+ CORRECTIVE ELEMENTS
+ SCULPT/SMOOTH
+ SCAN REGISTRATION/QUERIES
+ SECTION/DISTANCE/ANGLE/THICKNESS
+ PROCEDURAL PRODUCTION BODY
+ DFM/WATERTIGHT STL
+ VERSIONED DETERMINISTIC HISTORY
```

Everything else is optional until a concrete product feature proves otherwise.
