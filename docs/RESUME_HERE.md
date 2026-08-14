# BiomechE-CAD — RESUME HERE

> **Purpose:** first document to read when resuming BiomechE-CAD. It records the current source hierarchy, architecture baseline, decisions, validation state, open questions and exact next work.

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Canonical documentation:** Markdown under `docs/`  
**Current checkpoint:** 2026-08-14 — EasyCAD2 primary evidence consolidated; CAD capability baseline revised after OpenSubdiv evidence/context; canonical control-cage/operation model and EasyCAD2 25-story parity matrix added.

---

## 1. Product goal

BiomechE-CAD is a professional vertical CAD for custom foot orthoses/insoles integrated with BiomechE.

EasyCAD2 is the initial detailed behavioral benchmark, not the architectural ceiling.

Target product flow:

```text
Patient / Case
 -> OrthosisProject [LEFT/RIGHT]
 -> AcquisitionLayer[]
 -> Registration
 -> BaseTemplate / Canonical Cage
 -> Versioned Clinical Operations
 -> Corrective Elements
 -> Material Modifiers
 -> Analysis + DFM/QC
 -> Manufacturing Profile
 -> Export Artifacts
 -> Report
```

---

## 2. Primary EasyCAD2 evidence

### EC2-MANUAL-1.1

`EasyCAD2 Manuale ITA 2.0.pdf`  
software 1.1.x.x, 13/01/2024.

Detailed UI/geometry source for:

- DIMA;
- pressure/scan acquisition;
- MODIFICA;
- ELEMENTI;
- POST PROCESSING;
- CONTROLLO;
- PRODUCI;
- history/save/warnings.

### EC2-VAL-PLAN-1.4

`PdV0001_EasyCAD2 software validation plan.pdf`  
15/01/2026.

Defines 25 validation user stories.

### EC2-VAL-REPORT-1.4

`RdT001_Rapporto di Test di validazione software EasyCAD2 versione 14xx.pdf`  
20/01/2026.

Result:

```text
25 planned
25 executed
25 PASS
0 FAIL
0 BLOCKED
```

Reference links and page map live in `docs/references/easycad2/README.md`.

Do not commit the third-party PDF/screenshots to the public repo without explicit rights clearance.

---

## 3. EasyCAD2 geometry behavior confirmed by primary documents

Important confirmed behaviors:

- DX/SX mirror;
- DIMA templates SPORT/SANDALO/CLASSIC/COMFORT/DONNA;
- L/W/proportion editing;
- pressure `.bpe/.csv` registration;
- STL scan with heel/1st/5th landmarks and alignment;
- global thickness + flatten;
- heel/wrap/camber;
- medial/lateral arch with start/center/end/height/depth/curvature;
- rear/forefoot wedge in degrees, full/partial;
- corrective-element library;
- element position/rotation/XYZ scale;
- `SOMMA` / `INTERSEZIONE` integration described relative to upper/lower orthosis surfaces;
- direct XYZ element-vertex editing + CUSTOM preset;
- material/rigidity regions;
- local sculpt radius/strength;
- global deformation toward scan data;
- freehand/circle ROI deformation;
- section, height, ruler and fixed-height tools;
- minimum-thickness warning/fix;
- Bridge/Straight/Oblique/advanced production closure;
- STL/GCODE;
- PDF report;
- history/undo/redo/safe close.

The documents repeatedly use mesh/vertex semantics for core editing and validation.

---

## 4. New implementation-context fact

The project owner states with certainty that **EasyCAD2 uses OpenSubdiv**.

This fact is accepted as project context, but the EasyCAD2 manual/validation docs do not state how OpenSubdiv is internally used.

Therefore distinguish:

```text
USER-PROVIDED FACT:
EasyCAD2 uses OpenSubdiv.

ENGINEERING INFERENCE:
EasyCAD2 likely benefits from control-cage / subdivision-surface editing for at least part of the orthosis workflow.
```

Do not claim exact EasyCAD2 internal formulas/topology without independent evidence.

---

## 5. Official OpenSubdiv facts relevant to architecture

Official documentation states that OpenSubdiv:

- implements high-performance subdivision-surface evaluation;
- is optimized for deforming surfaces with static topology at interactive frame rates;
- works from polygonal control cages provided by the host application;
- exposes a smooth limit surface;
- supports arbitrary topology but regular quad-dominant regions are simpler/more predictable;
- warns that an arbitrary polygon mesh is not automatically a good subdivision cage.

References:

- `https://www.opensubdiv.org/docs/intro.html`
- `https://www.opensubdiv.org/docs/subdivision_surfaces.html`

---

## 6. Current geometry architecture baseline

The previous B-Rep/NURBS-heavy P0 hypothesis has been superseded.

Current baseline:

```text
Canonical Orthosis Control Cage
+ stable persistent vertex IDs
+ intrinsic anatomical coordinates
+ OpenSubdiv limit-surface evaluation
+ versioned parametric clinical operations
+ mask/field engine
+ scan/registration/query layer
+ orthosis-specific production-body generator
+ DFM validation
```

### Authoritative clinical model

```text
BaseCage + Operations + AlgorithmVersions
```

The final STL is derived, not authoritative.

### Canonical cage direction

- quad-dominant;
- stable topology during ordinary clinical edits;
- persistent vertex IDs;
- LEFT/RIGHT compatible topology;
- intrinsic coordinates:

```text
s ∈ [0,1]   heel -> toe
q ∈ [-1,1] lateral -> medial
```

- reusable anatomical region weights/masks;
- minimize extraordinary vertices in critical edit/high-curvature zones.

### OpenSubdiv role

OpenSubdiv is the expected P0 **surface evaluator**, not the business/domain model.

```text
BiomechCage
 -> OpenSubdiv adapter
 -> smooth limit surface
 -> display/query/tessellation
```

### Clinical operations

P0 operations include:

```text
TemplateMorph
HeelWrap
Camber
MedialArch
LateralArch
RearfootWedge
ForefootWedge
CorrectiveElement
Sculpt
Smooth
ScanConform
HeightConstraint
Thickness
DFMFix
MaterialModifier
ProductionClosure
```

Each operation is versioned, deterministic and replayable.

---

## 7. Current capability classification

### P0

```text
control-cage topology
stable IDs / adjacency / boundary
OpenSubdiv Catmull-Clark evaluation
intrinsic anatomical parameterization
template morph / L/W / mirror
clinical deformation fields
ROI/mask/falloff engine
corrective elements
vertex edit / sculpt / smooth
STL scan + landmarks + registration
BVH / closest-point / projection
section / distance / height / angle / thickness
orthosis-specific production body
Bridge/Straight/Oblique/Hybrid closure
watertight/min-thickness/DFM checks
versioned operation history
```

### P1

```text
utility B-spline curves
advanced custom-element cage editor
ICP
advanced mesh repair
local/adaptive production remeshing if needed
3MF/material-region export
curvature/geodesic helpers
positive mould
text emboss/deboss
```

### P2 / adapter / future

```text
NURBS surface authoring
trimmed B-Rep
STEP/IGES
Rhino exact interchange
general loft/sweep/revolve
general shell/offset
fillet/chamfer kernel
general solid boolean kernel
implicit/SDF
lattice/metamaterial
FEM
prediction/optimization/AI
```

General-purpose NURBS/B-Rep is therefore **not a P0 prerequisite**.

---

## 8. Important decisions

See `docs/DECISIONS.md`.

New decisions added:

- `D-CAD-011` — OpenSubdiv-first canonical control-cage architecture;
- `D-CAD-012` — general-purpose NURBS/B-Rep not P0;
- `D-CAD-013` — any additional geometry library must earn entry through a failing fixture;
- `D-CAD-014` — separate clinical upper surface from derived manufacturing body.

OCCT, CGAL, Manifold and openNURBS are **not selected dependencies** at this checkpoint.

---

## 9. New canonical documents

### Current capability baseline

`docs/spec/CAD_ENGINE_CAPABILITY_SPEC.md`

v2 replaces the old P0 classification. The previous version remains in Git history.

### Canonical cage and operation model

`docs/spec/03_geometry_operation_model.md`

Defines:

- authoritative representations;
- quad-dominant canonical cage;
- stable IDs;
- intrinsic `(s,q)`;
- anatomical masks;
- OpenSubdiv adapter contract;
- operation stack;
- field composition;
- corrective-element semantics;
- scan layer;
- production separation;
- CQ-001..CQ-012 cage qualification tests.

### Parametric geometry operators

`docs/spec/05_parametric_orthosis_geometry.md`

Defines a provisional deterministic math model for:

- smooth compact masks/falloffs;
- medial/lateral arch;
- rear/forefoot wedge;
- heel wrap/camber;
- thickness/flatten;
- corrective elements;
- sculpt;
- smooth;
- scan conform;
- height constraints;
- min-thickness fix.

These are BiomechE-CAD formulas, not claimed EasyCAD2 formulas.

### EasyCAD2 parity gate

`docs/validation/easycad2_geometry_parity.md`

All 25 EasyCAD2 1.4 validation stories have an implementation path in the proposed architecture.

This proves functional architecture coverage only; it does not prove the exact internal EasyCAD2 implementation.

---

## 10. Current mathematical direction

Use intrinsic field-based deformation over stable cage vertices.

Generic concept:

```text
Mask(v) -> [0,1]
Displacement(v) -> Vector3
P'(v) = P(v) + Mask(v) * Displacement(v)
```

Examples:

### Arch

```text
longitudinal start/center/end bump
× transverse medial/lateral profile
× anatomical mask
× target height
```

### Wedge

```text
h = tan(angle) * signed_distance_from_pivot_axis
× rearfoot/forefoot mask
× full/partial application mask
```

### Element

Prefer clinically named field/cage semantics:

```text
ADD_FROM_TOP
PLACE_FROM_BASE
```

rather than forcing general B-Rep booleans.

### Sculpt

```text
radius + strength + smooth compact falloff
```

with replay stored as sparse stable-vertex displacement layer or compact stroke history.

---

## 11. Clinical surface vs production body

Current BiomechE-CAD decision:

- canonical cage primarily authors the **upper clinical/contact surface**;
- thickness, lower surface and sidewalls are derived manufacturing semantics;
- production closure is orthosis-specific, not a generic CAD shell requirement.

Conceptually:

```text
UpperClinicalSurface
+ ThicknessField
+ LowerSurfaceRule
+ ClosureProfile
 -> ManufacturingBody
```

This separation still needs qualification against all production modes.

---

## 12. Geometry parity result against EasyCAD2

The proposed architecture covers:

```text
US6 mirror
US7 DIMA
US8 pressure registration
US9 Scan3D/Image2D alignment
US10 thickness/flatten
US11 heel
US12 arches
US13 wedges
US14 elements
US15 custom elements
US16 material modifiers
US17 sculpt
US18 scan conform
US19 section/fix heights
US20 ruler
US21 closure + STL/GCODE
US22 differentiated hardness
US24 minimum-thickness fix
```

Non-geometry stories US1–US5/US23/US25 are covered by project/settings/report/persistence layers.

No validated EasyCAD2 story currently forces general NURBS/B-Rep into P0.

---

## 13. Critical open questions

1. Final coordinate/registration contract.
2. Project Schema v0.
3. First concrete quad-dominant cage topology.
4. Cage vertex count/resolution and edge-loop layout.
5. Whether all template families share one topology family.
6. OpenSubdiv boundary/crease settings.
7. Arch displacement direction: anatomical vertical vs cage/limit normal.
8. Calibration of EasyCAD-like arch `roundness/depth/curvature` semantics.
9. Heel wrap/camber reference formula and limits.
10. Wedge pivot/reference axis fixture.
11. Corrective element representation: field vs small cage vs hybrid.
12. Exact `PLACE_FROM_BASE` semantics.
13. Scan-conform projection method.
14. Production lower-surface/closure algorithms.
15. Minimum-thickness repair policy.
16. Performance budget desktop + any WASM/server target.
17. Whether any fixture actually requires a second geometry library.

---

## 14. Exact restart point

**Do not evaluate OCCT/CGAL/Manifold first.**

Next work order:

```text
1. docs/spec/01_coordinate_registration.md
2. docs/spec/02_project_schema.md
3. docs/spec/04_base_template.md
   -> design first real canonical quad cage
4. create OpenSubdiv proof-of-concept fixture
5. implement intrinsic (s,q) mapping + semantic masks
6. implement reference operators:
   - medial arch
   - lateral arch
   - rearfoot/forefoot wedge
   - heel/wrap/camber
   - metatarsal bar/dome
7. execute CQ-001..CQ-012
8. only if a concrete test fails, evaluate a second geometry library
```

Parallel research may continue with ParoContour/DIERS and other competitors, but must not derail the geometry qualification sequence.

---

## 15. DONE

- [x] EasyCAD2 feature-by-feature research baseline.
- [x] EasyCAD2 manual 1.1 acquired and indexed.
- [x] EasyCAD2 validation plan/report 1.4 acquired and integrated.
- [x] 25/25 validation result recorded.
- [x] Unified product functional specification.
- [x] EasyCAD2 primary reference pack.
- [x] Initial generic CAD capability taxonomy.
- [x] Re-audit against actual EasyCAD2 geometry behavior.
- [x] OpenSubdiv-first architecture adopted as baseline.
- [x] General NURBS/B-Rep removed from P0.
- [x] Canonical cage/operation model written.
- [x] Provisional orthosis operator math written.
- [x] 25-story architecture parity matrix written.
- [x] Decision ledger updated.
- [x] Spec index updated.

---

## 16. TODO

### Geometry / architecture

- [ ] Freeze coordinate/registration specification.
- [ ] Freeze Project Schema v0.
- [ ] Design canonical cage fixture.
- [ ] Freeze base-template specification.
- [ ] Build OpenSubdiv proof of concept.
- [ ] Implement and test intrinsic anatomical coordinates.
- [ ] Implement CQ-001..CQ-012.
- [ ] Freeze reference operator versions after fixtures.
- [ ] Define production closure algorithms.
- [ ] Define geometry invariants/golden fixtures.
- [ ] Decide whether a second geometry library is actually needed.

### Clinical/manufacturing

- [ ] Complete corrective-element spec.
- [ ] Complete sculpt/ROI spec.
- [ ] Complete material/stiffness spec.
- [ ] Complete analysis/QC/DFM spec.
- [ ] Complete manufacturing spec.
- [ ] Complete BiomechE integration spec.
- [ ] Complete reporting/traceability spec.

### Research

- [ ] Deep audit ParoContour / DIERS.
- [ ] Audit FitFoot360.
- [ ] Audit Rodin4D/Neo.
- [ ] Audit Vorum/Canfit.
- [ ] Continue scientific source ledger.
- [ ] Add regulatory/privacy analysis.

---

## 17. Handover maintenance protocol

After substantial work:

1. update canonical specs;
2. preserve evidence provenance;
3. distinguish source facts from inference/decision;
4. update DONE/TODO;
5. update critical open questions;
6. state exact restart point;
7. keep superseded architecture in Git history rather than pretending it never existed;
8. do not leave a major decision only in chat.
