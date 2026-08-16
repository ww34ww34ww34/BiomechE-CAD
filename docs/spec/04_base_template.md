# BiomechE-CAD — Base Template & Canonical Cage v0

**Status:** **ENGINEERING CANDIDATE / QUALIFICATION FIXTURE — NOT PRODUCT AUTHORITY**  
**Date:** 2026-08-16 status clarification; engineering proposal originally 2026-08-14  
**Authority:** product semantics are governed by `16_geometry_authoring_contract.md`, `17_workflow_preset_macro.md` and `18_numerical_qualification_registry.md`.  
**Architecture status:** no geometry engine or canonical topology has been selected.

> **NON-AUTHORITATIVE ENGINEERING HYPOTHESIS.** This document preserves a concrete topology candidate for future PoC/qualification. `ORTHO_CAGE_41x17_V0`, its counts/indexing, Catmull-Clark/OpenSubdiv choices, spacing and boundary behavior are **not frozen product requirements**. A future geometry stack may satisfy the frozen semantic authoring contract with a different representation. Only evidence from architecture qualification may promote a topology family.

> This document defines the first **actual canonical orthosis cage candidate** to implement and test. It is a BiomechE-CAD engineering design, not a claim about EasyCAD2's exact topology.

---

## 1. Design goals

The candidate cage is intended to test whether a stable-topology representation can support the EasyCAD2-like P0 editing envelope while preserving the frozen BiomechE-CAD semantics:

- DIMA L/W and template morphing;
- right/left semantic mirror;
- heel wrap/camber;
- medial/lateral arches;
- rear/forefoot wedges;
- corrective elements;
- direct local edit;
- local sculpt/smooth;
- scan-conform deformation;
- sections and measurements;
- candidate SubD evaluation;
- production-body derivation.

These are qualification objectives, not proof that ordinary authoring must use one fixed cage topology.

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

All values in this section are candidate-fixture values only.

---

## 2.2 Intrinsic coordinates

Candidate mapping:

```text
s_i = i / 40
q_j = -1 + 2*j/16
```

Therefore in this fixture:

- longitudinal sampling is exactly 2.5% of candidate orthosis length;
- transverse sampling is 12.5% of normalized half-width span between `-1` and `+1`.

Stable semantic placement does **not** depend on adopting this discrete grid; the frozen authoring contract requires typed anatomical/reference placement independently of engine representation.

---

# 3. Why 41 × 17 was proposed

## 3.1 EasyCAD-compatible percentage controls

Arch controls use start/center/end percentages. A 41-row candidate cage gives native 2.5% longitudinal stations while still allowing continuous interpolation between rows.

## 3.2 Candidate physical control spacing

For a representative 260–300 mm orthosis the proposed topology gives longitudinal spacing of roughly 6.5–7.5 mm. For a 90–120 mm wide forefoot the candidate transverse spacing is roughly 5.5–7.5 mm near the widest region.

These are engineering observations, not validated minimum feature sizes or clinical requirements.

## 3.3 Performance hypothesis

697 control vertices / 640 quads are expected to be inexpensive for CPU-side operation replay and SubD evaluation, but this remains a PoC/benchmark hypothesis. Actual performance authority belongs to the future realtime/performance contract and architecture qualification.

## 3.4 Qualification rather than dogma

If qualification shows insufficient local feature control, topology may change in a **versioned topology family** or the representation may change entirely. A previously suggested candidate such as `ORTHO_CAGE_61x25_V1` has no product-authority status until tested.

---

# 4. Boundary semantics — candidate fixture

The structured grid has four candidate topological boundary segments:

```text
HEEL_EDGE     i = 0
TOE_EDGE      i = 40
LATERAL_EDGE  j = 0
MEDIAL_EDGE   j = 16
```

Together they form one closed boundary loop.

The four grid corners are topology corners. Their exact placement and any SubD corner/boundary interpolation behavior are architecture-qualification questions, not clinical semantics.

---

# 5. Base template product semantics vs candidate representation

The **product-level** requirement is that a reusable base/template have exact identity/version/provenance and support deterministic reconstruction under the selected engine. A candidate engineering representation is:

```text
BaseTemplate
  template_id
  representation/topology_family
  side_reference
  nominal_size
  nominal_length_mm
  nominal_width_mm
  control_data
  semantic_metadata
  version
  author/provenance
```

The exact `control_data` representation is intentionally not frozen here.

Template categories may include EasyCAD2-like behavioral references such as:

```text
SPORT
SANDALO
CLASSIC
COMFORT
DONNA
```

but product naming/taxonomy remains a separate product decision and must not imply clinical evidence.

---

# 6. Candidate shape parameterization

The original engineering proposal used a complete position array plus semantic profiles such as a longitudinal centerline, separate medial/lateral half-width functions and a height seed. These remain useful PoC constructs:

```text
C(s)
W_lat(s)
W_med(s)
Z0(s,q)
```

No particular basis, interpolation family or control sampling is frozen by this document.

---

# 7. L/W and DIMA morphing — semantic requirement and hypothesis

Product semantics require length/width/size edits to be unit-explicit, replayable, inspectable and side-aware. The candidate proposes intrinsic-coordinate maps rather than only global XYZ scaling:

```text
X_target(s) = LengthMap(s, L_target, template)
W_lat_target(s)
W_med_target(s)
```

The exact maps are engineering hypotheses. Shoe size remains a UI/product input mapped through a versioned size/profile table to metric geometry.

---

# 8. Anatomical semantic bands

No clinical percentage bands are frozen here.

Masks/regions should ultimately derive from the frozen product semantics:

```text
landmarks
normalized anatomical references
metatarsal line
heel reference
user-defined ROI
```

A topology coordinate such as candidate `s/q` may assist implementation but cannot replace typed anatomical placement/provenance.

---

# 9. Medial/lateral semantics

Anatomical medial/lateral meaning belongs to `01_coordinate_registration.md` and the side-aware authoring contract. It must never be inferred solely from a global coordinate sign or this candidate grid convention.

---

# 10. Candidate vertex metadata

If a structured cage is used, candidate rebuildable metadata may include:

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

Caches such as normals, limit-surface references, landmark weights or pressure mappings must remain rebuildable and non-authoritative.

---

# 11. Mirror mapping — candidate only

For this candidate structured cage:

```text
mirror(i,j) = (i, 16-j)
```

The **frozen product requirement** is stronger and representation-independent: mirror is semantic and side-aware. Exact vertex correspondence is optional implementation infrastructure, not domain authority.

---

# 12. SubD/OpenSubdiv rules to qualify

The original candidate target was Catmull-Clark/OpenSubdiv. Boundary interpolation, corner behavior, creases and tessellation remain explicit PoC questions.

This section must not be read as selecting OpenSubdiv. Current architecture scorecard still compares multiple candidate approaches and requires evidence before selection.

---

# 13. Representation-specific measurements

If a cage/limit/production-body architecture is selected, measurements must label their source representation, for example:

```text
control/cage metric
clinical/limit-surface metric
production-body metric
measured physical-part metric
```

The frozen invariant is that requested prescription, realized CAD geometry, manufacturing artifact and measured physical part are not silently conflated.

---

# 14. Local feature resolution qualification

A candidate representation should be tested on representative features such as heel transition, arches, metatarsal elements, sculpt brushes and wedge transitions. Exact dimensions previously proposed in this file are **qualification fixtures**, not universal minimum feature sizes or clinical defaults.

Measure at least:

```text
requested dose
realized CAD dose
surface smoothness / artifact state
local attenuation/error
invalidation scope
performance/memory
```

Only qualification evidence may establish a supported envelope.

---

# 15. Candidate fixture metadata

A future candidate fixture may retain metadata similar to:

```json
{
  "schema": "BiomechE.CAD.BaseTemplateCandidate/1",
  "templateId": "neutral-41x17-v0",
  "representationCandidate": "ORTHO_CAGE_41x17_V0",
  "sideReference": "RIGHT",
  "units": "mm",
  "algorithmVersion": "BaseTemplateCandidate/0"
}
```

This is not Project Schema v0.2 materialization.

---

# 16. Candidate qualification tests

The historical BT-001..BT-013 suite remains useful as an architecture fixture family if this representation is implemented:

```text
BT-001 topology validity
BT-002 candidate SubD construction
BT-003 neutral surface quality
BT-004 boundary/corner quality
BT-005 mirror equivalence
BT-006 L/W supported envelope
BT-007 heel operation
BT-008 arch operation
BT-009 wedge realization
BT-010 element resolution
BT-011 sculpt resolution
BT-012 scan conform stability
BT-013 production body validity
```

Numerical tolerances are not defined here. They must be explicit `ALGORITHM_NUMERICAL_TOLERANCE` or other appropriate NREG entries and qualified before PASS/FAIL.

---

# 17. Go / no-go rule

`ORTHO_CAGE_41x17_V0` becomes a selected topology family **only** if the future architecture qualification demonstrates that it satisfies the frozen product contract and the approved performance/quality profiles. Failure must be recorded before changing representation.

A different engine/representation is fully acceptable if it satisfies the same frozen product semantics more effectively.

---

# 18. Final disposition

```text
PRODUCT SEMANTICS            authoritative elsewhere — frozen contracts
41x17 topology               engineering hypothesis
OpenSubdiv/Catmull-Clark     engineering hypothesis
vertex/index mapping         engineering hypothesis
specific control spacing     engineering hypothesis
BT-* tests                   reusable qualification ideas
clinical defaults            NONE frozen here
manufacturing tolerances     NONE frozen here
```

This document is preserved for engineering continuity and future PoC work; it is **not** a reason to select a geometry engine or lock product data to this topology.
