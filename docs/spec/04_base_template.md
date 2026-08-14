# BiomechE-CAD — Base Template & Canonical Cage v0

**Status:** concrete topology candidate / qualification fixture  
**Date:** 2026-08-14  
**Depends on:** `03_geometry_operation_model.md`; final frame semantics depend on `01_coordinate_registration.md`.

> This document defines the first **actual canonical orthosis cage candidate** to implement and test. It is a BiomechE-CAD engineering design, not a claim about EasyCAD2's exact topology.

---

## 1. Design goals

The cage must support the full EasyCAD2-like P0 editing envelope while keeping topology stable:

- DIMA L/W and template morphing;
- right/left mirror;
- heel wrap/camber;
- medial/lateral arches;
- rear/forefoot wedges;
- corrective elements;
- direct vertex edit;
- local sculpt/smooth;
- scan-conform deformation;
- sections and measurements;
- OpenSubdiv Catmull-Clark evaluation;
- production-body derivation.

It should avoid adding/removing faces during ordinary clinical editing.

---

# 2. Candidate topology: `ORTHO_CAGE_41x17_V0`

## 2.1 Dimensions

```text
longitudinal stations Ns = 41
transverse stations   Nq = 17
vertices              = 41 * 17 = 697
quad faces            = 40 * 16 = 640
```

Indexing:

```text
vertex(i,j)
  i = 0..40    longitudinal
  j = 0..16    transverse

vertex_id = i * 17 + j
```

Faces:

```text
quad(i,j) =
  v(i,   j)
  v(i+1, j)
  v(i+1, j+1)
  v(i,   j+1)
```

for:

```text
i = 0..39
j = 0..15
```

This gives a topological rectangular disk with one closed outer boundary.

---

## 2.2 Intrinsic coordinates

```text
s_i = i / 40
q_j = -1 + 2*j/16
```

Therefore:

- longitudinal sampling is exactly 2.5% of orthosis length;
- transverse sampling is 12.5% of normalized half-width span between `-1` and `+1` steps of `0.125`.

These coordinates are stable properties of vertex IDs and never change under geometric deformation.

---

# 3. Why 41 × 17

## 3.1 EasyCAD-compatible percentage controls

Arch controls use start/center/end percentages. A 41-row cage gives native 2.5% longitudinal stations while still allowing continuous interpolation between rows.

## 3.2 Physical control spacing

For a representative 260–300 mm orthosis:

```text
longitudinal control spacing ≈ 6.5–7.5 mm
```

For a 90–120 mm wide forefoot:

```text
transverse control spacing ≈ 5.5–7.5 mm near the widest region
```

This is fine enough for typical arch/heel/wedge deformation and a reasonable first target for local sculpt/element blending.

## 3.3 Performance

697 control vertices / 640 quads are trivial for CPU-side operation replay and small for OpenSubdiv.

The cost driver will be output tessellation/render resolution, not the authoring cage itself.

## 3.4 Qualification rather than dogma

If CQ tests show insufficient local feature control, increase topology in a **versioned topology family** rather than silently remeshing projects.

Candidate next family, only if proven necessary:

```text
ORTHO_CAGE_61x25_V1
```

Do not add it preemptively.

---

# 4. Boundary semantics

The structured grid has four topological boundary segments:

```text
HEEL_EDGE     i = 0
TOE_EDGE      i = 40
LATERAL_EDGE  j = 0
MEDIAL_EDGE   j = 16
```

Together they form one closed boundary loop.

## 4.1 Important caveat

The four grid corners are topology corners:

```text
(0,0)
(0,16)
(40,0)
(40,16)
```

They should be placed at natural high-turn regions of the outline:

- posterolateral heel;
- posteromedial heel;
- distal lateral toe boundary;
- distal medial toe boundary.

OpenSubdiv boundary behavior at these four points must be included in visual/curvature qualification. If artifacts are unacceptable, evaluate an alternative disk topology rather than forcing extra CAD machinery.

---

# 5. Base template representation

A template stores complete base positions, not only L/W scalars.

```text
BaseTemplate
  template_id
  topology_family = ORTHO_CAGE_41x17_V0
  side_reference
  nominal_size
  nominal_length_mm
  nominal_width_mm
  control_positions[697]
  semantic_metadata
  version
  author/provenance
```

Template categories may include EasyCAD2-like:

```text
SPORT
SANDALO
CLASSIC
COMFORT
DONNA
```

BiomechE-CAD template names can later be productized independently.

---

# 6. Shape parameterization

The full position array is authoritative for the base template, but generation/morphing uses semantic profiles.

## 6.1 Longitudinal centerline

Define:

```text
C(s) = centerline position in template plane
```

The cage does not require all vertices in a row to share identical global X. Individual row points may shift longitudinally to reproduce heel/toe curvature.

## 6.2 Lateral/medial half-widths

Use separate width profiles:

```text
W_lat(s) >= 0
W_med(s) >= 0
```

A simple planar seed position is:

```text
q <= 0:
  lateral_offset = q * W_lat(s)

q >= 0:
  medial_offset = q * W_med(s)
```

This captures asymmetry better than a single symmetric width.

## 6.3 Height seed

```text
Z0(s,q)
```

encodes the neutral clinical upper-surface shape before patient/project operations.

This may be represented directly by stored vertex Z or regenerated from a versioned template model.

---

# 7. L/W and DIMA morphing

## 7.1 Length

Length scaling must not be a naive global XYZ scale only.

Use intrinsic `s` and target longitudinal map:

```text
X_target(s) = LengthMap(s, L_target, template)
```

This allows heel and toe zones to scale differently if required by template behavior.

## 7.2 Width

Use:

```text
W_lat_target(s)
W_med_target(s)
```

so unlocked L/W proportions can alter width independently.

## 7.3 Shoe size

Shoe size is a UI/product input mapped through a versioned size table/profile to nominal L/W; the canonical geometry uses millimeters.

## 7.4 Outline edit

Boundary editing changes boundary control points and propagates displacement inward with a smooth transverse/longitudinal influence field.

Directly moving boundary points without interior compensation is allowed only in advanced edit mode.

---

# 8. Anatomical semantic bands

Intrinsic `s` provides stable bands. Initial non-clinical defaults for geometry organization only:

```text
HEEL        roughly proximal s range
REARFOOT    proximal quarter
MIDFOOT     central region
FOREFOOT    distal region
TOE/DISTAL  terminal region
```

**Do not freeze clinical percentages in this document.**

Exact thresholds must be linked to landmarks/prescription semantics in later clinical specs.

Instead, masks should be generated from:

```text
landmarks
normalized length
metatarsal line
heel reference
user-adjustable ROI
```

---

# 9. Medial/lateral semantics

With:

```text
q < 0 = lateral
q > 0 = medial
```

for the reference-side convention, LEFT/RIGHT mirror changes the geometric frame but the domain layer must preserve anatomical meaning.

Never infer anatomical medial/lateral directly from global X/Y sign after registration.

---

# 10. Semantic data attached to every vertex

Minimum generated data:

```text
vertex_id
s
q
is_boundary
boundary_segment
base_position
mirror_vertex_id
region_weights
```

Optional cached data:

```text
baseline_normal
current_cage_normal
limit_surface_param_ref
nearest_landmark_weights
pressure_mapping_ref
```

Caches must be rebuildable.

---

# 11. Mirror mapping

For structured cage:

```text
mirror(i,j) = (i, 16-j)
```

This gives an exact persistent ID correspondence.

Semantic mirror rules additionally swap:

```text
MEDIAL <-> MEDIAL anatomically
LATERAL <-> LATERAL anatomically
```

while geometric transverse sign changes.

Operations carrying side-specific direction/posting must use the anatomical frame, not merely negate a coordinate.

---

# 12. OpenSubdiv rules to qualify

Initial target:

```text
scheme = Catmull-Clark
```

Qualification must freeze:

- boundary interpolation mode;
- corner behavior;
- whether selected boundary edges need semi-sharp creases;
- whether production edge appearance should come from cage placement or crease weights;
- tessellation level/error policy.

Do not enable creases everywhere just to force the limit surface through the cage; that defeats smooth clinical shaping.

---

# 13. Cage vs limit-surface measurements

Define metric source explicitly:

### Cage metrics

Useful for:

- debugging;
- stable control-point constraints;
- operation regression.

### Limit-surface metrics

Preferred for:

- clinical height;
- local normals;
- section shape;
- visual inspection;
- production surface.

### Production-body metrics

Required for:

- actual thickness;
- min thickness;
- watertightness;
- manufacturing bounds.

Never compare metrics from different representations without labeling them.

---

# 14. Local feature resolution test

Before adopting the cage, test at least:

```text
heel cup edge transition
medial arch peak
lateral arch peak
metatarsal dome 20–30 mm class
metatarsal bar
5th-met support/offload
5–10 mm sculpt brush
wedge transition boundary
```

For each feature compare:

- intended analytic field;
- cage-sampled deformation;
- OpenSubdiv limit surface;
- tessellated manufacturing surface.

Measure peak attenuation and transition error.

If a small feature is too attenuated, options are evaluated in this order:

1. modify field/cage influence stencil;
2. allow local element cage overlay;
3. increase canonical topology family resolution;
4. only then evaluate hierarchical/local topology refinement.

---

# 15. Base-template fixture format

Proposed JSON metadata:

```json
{
  "schema": "BiomechE.CAD.BaseTemplate/1",
  "templateId": "neutral-41x17-v0",
  "topologyFamily": "ORTHO_CAGE_41x17_V0",
  "sideReference": "RIGHT",
  "vertexCount": 697,
  "faceCount": 640,
  "intrinsicGrid": { "Ns": 41, "Nq": 17 },
  "units": "mm",
  "positions": "external-or-packed-array",
  "algorithmVersion": "BaseTemplate/0"
}
```

The actual project schema may store arrays separately; this is only the geometry fixture contract.

---

# 16. Qualification tests for `ORTHO_CAGE_41x17_V0`

## BT-001 Topology

```text
697 vertices
640 quads
single connected component
single boundary loop
no duplicate vertices
no zero-area base quads
```

## BT-002 OpenSubdiv construction

TopologyRefiner/equivalent builds without error.

## BT-003 Neutral limit surface

No visible ripple; sections vary smoothly.

## BT-004 Boundary corners

No unacceptable heel/toe corner artifacts.

## BT-005 Mirror exactness

`mirror(mirror(v)) == v` and mirrored template geometric equivalence within tolerance.

## BT-006 L/W envelope

Supported L/W extremes remain non-inverted.

## BT-007 Heel operation

Max supported wrap/camber does not fold cage.

## BT-008 Arch operation

Medial/lateral high presets remain smooth.

## BT-009 Wedge

2/4/6° fixtures meet angle tolerance.

## BT-010 Element resolution

Reference metatarsal dome/bar preserves target peak/shape within tolerance.

## BT-011 Sculpt resolution

5/10/20 mm brush fixtures quantify attenuation and determine supported minimum brush radius.

## BT-012 Scan conform

Target projection does not create local inversion in supported max displacement.

## BT-013 Production body

All closure profiles produce valid watertight body from neutral + stressed fixtures.

---

# 17. Go / no-go rule

`ORTHO_CAGE_41x17_V0` becomes the frozen first topology family only if BT-001..BT-013 pass within defined tolerances.

If it fails, record the exact failure before changing topology.

Do not replace it because another library offers a more fashionable modeling representation.

---

# 18. Next implementation artifact

Create a small headless proof of concept:

```text
fixtures/cages/neutral_41x17.json
src/geometry/cage/
src/geometry/subdiv/
tests/geometry/cage/
```

Minimum proof:

1. generate/load the 41x17 cage;
2. evaluate OpenSubdiv limit surface;
3. render/export a sampled OBJ/STL for inspection;
4. apply one medial-arch field;
5. apply one 4° wedge;
6. verify mirror;
7. run BT-001/002/005/008/009 first.
