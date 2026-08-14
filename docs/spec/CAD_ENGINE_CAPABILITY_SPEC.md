# BiomechE-CAD — CAD Engine Capability Specification

**Stato:** baseline capability specification  
**Data:** 2026-08-14  
**Scopo:** definire in un unico documento che cosa deve saper fare il motore CAD di BiomechE-CAD, indipendentemente dalla libreria/kernel che verrà scelto.  
**Relazione con la specifica prodotto:** questo documento completa `BIOMECHE_CAD_FUNCTIONAL_SPEC.md`: quella specifica descrive cosa deve poter fare l'utente clinicamente; questa descrive quali capacità geometriche/CAD deve possedere il motore per realizzarlo in modo robusto.

---

## 0. Executive summary

BiomechE-CAD non deve essere un semplice editor STL e non deve nemmeno trasformarsi in un CAD meccanico general purpose completo.

Il motore deve supportare quattro domini geometrici complementari:

1. **Geometria analitica e parametrica** — linee, archi, coniche, Bézier, B-spline e NURBS;
2. **Topologia CAD / B-Rep** — vertex, edge, wire, face, shell, solid, con join/sew/trim/split/boolean;
3. **Mesh polygonali** — scansioni 3D, sculpting, remeshing, repair, rendering e output manufacturing;
4. **Subdivision surfaces (SubD)** — opzionali, utili per freeform molto fluido e preview/rendering, ma non devono essere l'unica rappresentazione autorevole della geometria clinico-manifatturiera.

La regola guida è:

```text
PARAMETRIC / EXACT GEOMETRY
        +
TOPOLOGY / B-REP
        +
MESH / SCAN / SCULPT
        +
VERSIONED CLINICAL OPERATIONS
        =
BiomechE-CAD Geometry Engine
```

Per il plantare sono **P0** soprattutto:

- curve B-spline/NURBS;
- superfici B-spline/NURBS e trimmed surfaces;
- loft/sweep/ruled/fill;
- join/stitch/sew;
- trim/split/intersection;
- offset/thicken/shell;
- boolean union/difference/intersection;
- proiezione e closest-point;
- mesh repair/remesh/smooth;
- deformazioni locali/ROI;
- cross-section e thickness map;
- manifold/self-intersection validation;
- robust tolerance model;
- conversione controllata parametric surface → mesh.

SubD, fillet avanzati, variational surfacing, FEM, implicit/SDF modeling e feature mechanical-CAD complesse sono **P1/P2**, non prerequisiti per il primo MVP.

---

# 1. Principi architetturali

## CAD-ARCH-001 — Kernel-independent capability contract — P0

La specifica pubblica di BiomechE-CAD deve descrivere entità e operazioni proprie, non tipi specifici di una libreria.

Esempio:

```text
CadCurve3
CadNurbsCurve3
CadSurface
CadNurbsSurface
CadFace
CadShell
CadSolid
CadMesh
CadOperation
```

Il contratto applicativo non deve esporre direttamente tipi `TopoDS_*`, `CGAL::*`, `ON_*`, Eigen, OpenSubdiv o altri tipi di terze parti.

## CAD-ARCH-002 — Hybrid representation — P0

Il motore deve poter rappresentare contemporaneamente:

```text
analytic/parametric geometry
B-Rep topology
polygon mesh
point cloud / scan
optional SubD control cage
```

Una rappresentazione non deve essere forzata a sostituire le altre.

## CAD-ARCH-003 — Authoritative vs derived representations — P0

Ogni entità deve dichiarare quale forma è autorevole e quali sono derivate.

Esempio:

```text
NURBS surface        = authoritative
render triangle mesh = derived tessellation
STL export mesh      = derived manufacturing artifact
```

oppure:

```text
scanner triangle mesh = authoritative acquisition
smoothed preview mesh = derived
registered mesh       = derived + transform provenance
```

## CAD-ARCH-004 — Non-destructive clinical operation stack — P0

Operazioni cliniche ad alto livello devono restare ricostruibili:

```text
BaseTemplate
 + HeelOperation
 + MedialArchOperation
 + RearfootWedgeOperation
 + MetatarsalPadOperation
 + LocalReliefOperation
 -> evaluated geometry
```

Non devono ridursi immediatamente a modifiche irreversibili di triangoli.

## CAD-ARCH-005 — Deterministic evaluation — P0

Stesso input + stessi parametri + stessa versione algoritmo devono produrre geometria equivalente entro tolleranza dichiarata.

## CAD-ARCH-006 — Headless geometry core — P0

Le operazioni geometriche devono essere invocabili senza UI/rendering, per desktop, server, test automatici, batch processing ed eventuale WebAssembly o servizio remoto.

---

# 2. Modello geometrico canonico

## 2.1 Entità geometriche di base — P0

```text
Point2 / Point3
Vector2 / Vector3
Direction2 / Direction3
Axis / Frame / Plane
BoundingBox / OrientedBoundingBox
Transform / RigidTransform / AffineTransform
Ray / Line / Segment
```

## 2.2 Entità topologiche B-Rep — P0

Il motore deve poter modellare almeno:

```text
Vertex
Edge
Wire / Loop
Face
Shell
Solid / Body
Compound / Group
```

Semantica minima:

- un `Edge` lega una curva geometrica a un intervallo parametrico;
- un `Face` lega una superficie geometrica a uno o più loop di trimming;
- una `Shell` è un insieme connesso di face;
- un `Solid` è una shell chiusa/orientata o una struttura equivalente.

## 2.3 Identità stabile — P0

Entità e feature devono possedere ID persistenti quando possibile:

```text
geometry_id
topology_id
feature_id
operation_id
revision_id
```

---

# 3. Primitive 2D

## P0

- Point;
- Line;
- Segment;
- Polyline;
- Arc;
- Circle;
- Ellipse;
- Rectangle;
- oriented rectangle;
- Polygon;
- Bézier curve;
- B-spline curve;
- NURBS curve;
- closed spline;
- composite curve / polycurve.

## P1

- parabola;
- hyperbola;
- rounded rectangle;
- offset polyline con gestione join;
- clothoid/fair curve se utile a raccordi specifici.

---

# 4. Primitive 3D

## P0

- Plane;
- planar face from closed wire;
- Box;
- Cylinder;
- Cone / truncated cone;
- Sphere;
- Prism / generic extrusion;
- Wedge;
- ruled surface between two curves;
- extruded surface/solid.

## P1

- Torus;
- capsule;
- pipe/tube primitive;
- generic revolved solid.

Le primitive servono per costruire regioni, utensili booleani, supporti, tagli e fixture di test.

---

# 5. Curve parametriche, B-spline e NURBS

## CAD-CURVE-001 — B-spline curve — P0

Supporto almeno per:

```text
degree
control points / poles
knot vector
knot multiplicities
open / clamped
periodic / non-periodic
rational / non-rational
weights
parameter domain
```

## CAD-CURVE-002 — NURBS curve — P0

Una NURBS è una B-spline razionale; deve poter rappresentare curve coniche e curve freeform controllate.

## CAD-CURVE-003 — Evaluation — P0

Per parametro `u`:

```text
position
first derivative
second derivative
tangent
curvature
```

## CAD-CURVE-004 — Editing del control polygon — P0

- move control point;
- multi-select control points;
- weight edit per curve razionali;
- preserve endpoint opzionale;
- preserve tangent opzionale;
- local edit con falloff quando applicabile.

## CAD-CURVE-005 — Knot operations — P1

- knot insertion/refinement;
- knot removal entro tolleranza;
- degree elevation;
- degree reduction entro tolleranza.

## CAD-CURVE-006 — Split / trim / extend — P0

- split a parametro;
- trim a intervallo;
- reverse direction;
- extend tangent/curvature-aware quando definito.

## CAD-CURVE-007 — Join curves — P0

Join con controlli:

```text
G0 positional continuity
G1 tangent continuity
G2 curvature continuity [P1]
```

## CAD-CURVE-008 — Interpolation / approximation — P0

Creazione da punti interpolati o approssimati entro tolleranza, con eventuali tangent/endpoint constraints.

## CAD-CURVE-009 — Offset curve — P0

Offset 2D/planare con distance, side, join mode e gestione cusp/self-intersection.

## CAD-CURVE-010 — Projection / pullback — P0/P1

Proiezione di curve/punti su plane, surface e mesh.

## CAD-CURVE-011 — Closest point — P0

Closest point curve↔point e curve↔curve.

---

# 6. Superfici parametriche, B-spline e NURBS

## CAD-SURF-001 — Analytic surfaces — P0

- plane;
- cylinder;
- cone;
- sphere;
- ruled surface;
- extruded surface;
- revolved surface.

## CAD-SURF-002 — B-spline surface — P0

Supporto per:

```text
U degree / V degree
U/V knot vectors
U/V multiplicities
control net
rational weights
periodic/non-periodic U/V
parameter domains
```

## CAD-SURF-003 — NURBS surface — P0

La superficie NURBS deve essere nativa o semanticamente equivalente, non solo una tessellazione importata.

## CAD-SURF-004 — Surface evaluation — P0

Per `(u,v)`:

```text
position
partial derivatives
normal
principal curvatures [P1]
mean/Gaussian curvature [P1]
```

## CAD-SURF-005 — Iso-curves — P0

Estrarre curve `u = const` e `v = const`.

## CAD-SURF-006 — Trimmed surface — P0

Una face deve poter limitare una superficie mediante outer trim loop, inner loops/holes, orientamento e curve 2D/3D coerenti.

## CAD-SURF-007 — Surface split/trim — P0

Split mediante curve, plane, altra surface o body.

## CAD-SURF-008 — Surface extend — P1

## CAD-SURF-009 — Offset surface — P0

Offset lungo normale con distanza, tolleranza, gestione cusp/self-intersection e local failure reporting.

## CAD-SURF-010 — Surface closest point — P0

## CAD-SURF-011 — Intersections — P0

- curve/surface;
- surface/surface;
- surface/plane;
- surface/mesh quando necessario.

---

# 7. Costruzione di superfici

## P0

- Extrude;
- Loft / skin;
- Sweep;
- Ruled surface;
- Fill / patch semplice.

## P1

- Revolve;
- one/two rail sweep;
- fill con G1/G2 boundary constraints.

## P2

- network surface;
- variational/fair surface;
- advanced scattered-data fitting.

Loft deve gestire profile ordering, seam alignment, closed/open loft, parameterization e, P1, start/end tangent constraints.

---

# 8. Join, stitch, sew e continuità

## CAD-JOIN-001 — Join curve — P0

## CAD-JOIN-002 — Join edges/wires — P0

Creare wire chiusi o aperti con gestione gap entro tolerance.

## CAD-JOIN-003 — Stitch / sew faces — P0

Unire face lungo bordi coincidenti entro tolerance. Output:

```text
open shell
closed shell
solid when valid
unmatched edges list
healed gaps report
```

## CAD-JOIN-004 — Weld mesh vertices/edges — P0

## CAD-JOIN-005 — Continuity analyzer — P1

Verificare G0/G1/G2 con deviazioni numeriche.

---

# 9. Trim, split, cut e intersection

## P0

- trim curve by parameter/intersection;
- split curve/wire;
- trim surface by loop;
- split face by curve;
- split body by plane/surface;
- cut mesh by plane;
- compute section contours;
- curve/curve, curve/surface, surface/surface e mesh/mesh intersection.

Per il plantare le sezioni devono supportare misure di thickness, profile height, wedge angle, arch shape e heel cup.

---

# 10. Boolean operations

## P0

- Union / Fuse;
- Difference / Cut;
- Intersection / Common;
- boolean diagnostics.

In caso di fallimento restituire informazioni utili: self-intersection, non-manifold input, open shell, coplanar ambiguity, tolerance problem, degenerate result.

## P1

Robust fallback strategy, anche con backend mesh/implicit, purché il passaggio sia esplicito e il risultato validato.

---

# 11. Offset, thickness, shell e sidewalls

Questa è una delle aree più critiche per BiomechE-CAD.

## P0

- Offset curve;
- Offset surface;
- Thicken open surface;
- Variable thickness;
- Sidewall generation;
- Minimum thickness enforcement.

Il plantare deve supportare un thickness field concettuale:

```text
t(u,v)
or
t(x,y)
```

Sidewall modes minimi:

- vertical/straight;
- bevel/oblique;
- blended/bridge;
- local sidewall height/angle;
- smooth connection.

## P1

- shell/hollow general purpose.

---

# 12. Fillet, chamfer e blend

## P1

- constant-radius fillet;
- edge blend;
- chamfer;
- tangent surface blend.

## P2

- variable-radius fillet;
- advanced curvature-continuous blending.

Per BiomechE-CAD servono soprattutto su heel cup, sidewall, corrective elements e transition zones.

---

# 13. Transformazioni

## P0

- translation;
- rotation;
- uniform/non-uniform scale;
- mirror;
- transform by matrix;
- transform between coordinate frames;
- pivot/origin control.

## P1

- shear;
- taper;
- twist;
- bend.

`Mirror` DX↔SX deve convertire anche semantiche MEDIAL/LATERAL, LEFT/RIGHT e posting.

---

# 14. Freeform deformation

## P0

- control-point deformation;
- brush sculpt raise/lower;
- radius/strength/falloff;
- smooth;
- closed ROI deformation freehand/circle/polygon;
- additive raise/support;
- subtractive relief;
- deformation toward Scan3D/reference data.

## P1

- flatten/local planarize;
- cage/lattice Free Form Deformation;
- residual/deviation field during scan fitting.

## P2

- ARAP / shape-preserving deformation.

---

# 15. Mesh polygonali

## P0

- vertices/edges/faces;
- triangle/polygon mesh;
- adjacency;
- connected components;
- boundary loops;
- import polygon soup;
- triangulation;
- normals + orientation;
- repair;
- boundary stitch;
- isotropic remeshing;
- smoothing;
- clipping/slicing;
- mesh boolean o equivalente robusto;
- point/mesh e mesh/mesh distance;
- self-intersection detection.

Repair deve almeno gestire:

- isolated vertices;
- duplicate vertices/faces;
- degenerate triangles;
- zero-area faces;
- inconsistent orientation;
- holes;
- small disconnected components;
- non-manifold vertices/edges.

## P1

- adaptive remeshing;
- simplification/decimation;
- hole filling avanzato;
- Loop/Catmull-Clark subdivision;
- feature-preserving smoothing;
- Hausdorff distance.

---

# 16. Subdivision surfaces (SubD)

SubD è utile ma non deve diventare il fondamento unico del CAD.

## P1

- Catmull-Clark;
- creases/sharpness;
- limit-surface evaluation;
- adaptive tessellation;
- SubD ↔ mesh.

## P2

- SubD → NURBS/B-Rep conversion.

**Decisione proposta:** SubD è una capability aggiuntiva per freeform/rendering, non la source-of-truth del primo plantare parametrico.

---

# 17. Point cloud e scansioni 3D

## P0

- point-cloud container;
- import scan mesh/point cloud;
- crop;
- transform;
- unit metadata;
- landmarks;
- bounding box;
- closest point;
- distance-to-surface;
- registration transform provenance.

## P1

- normal estimation;
- outlier removal;
- downsampling;
- ICP;
- landmark-assisted ICP;
- plane fitting;
- local surface fitting;
- point-cloud-to-mesh reconstruction.

## P2

- Poisson/implicit reconstruction;
- uncertainty field.

---

# 18. Registration e coordinate geometry

## P0

- rigid transform;
- landmark registration;
- manual fine adjustment;
- coordinate-frame provenance;
- inverse transform when mathematically valid.

Landmark minimi per foot scan:

```text
heel
1st metatarsal
5th metatarsal
```

## P1

- similarity transform;
- ICP.

---

# 19. Geometric queries e measurements

## P0

- bounding box / OBB;
- length/perimeter;
- area/volume/centroid;
- surface normal;
- point-point, point-curve, point-surface, point-mesh distance;
- curve length;
- section thickness;
- min/max Z;
- angle between vectors/planes/sections;
- closest points;
- inside/outside solid;
- connected components.

## P1

- principal/mean/Gaussian curvature;
- geodesic distance;
- local feature size;
- shape diameter/thickness estimators;
- Hausdorff distance.

---

# 20. Spatial acceleration structures

## P0

- AABB tree / BVH equivalent;
- spatial search triangles;
- ray cast;
- nearest point;
- intersection acceleration;
- picking support.

## P1

- KD-tree point cloud;
- spatial hashing/grid for sculpt neighborhoods;
- incremental acceleration updates.

---

# 21. Tessellation e conversioni parametriche → mesh

## P0

NURBS/B-Rep → triangle mesh controllata da:

```text
chordal deviation
angular tolerance
maximum edge length
minimum edge length
boundary fidelity
normal deviation
```

Devono esistere profili separati:

```text
RenderMesh
ManufacturingMesh
AnalysisMesh
```

La manufacturing tessellation deve essere deterministica/versionata e rispettare trim/feature edges.

## P1

- adaptive tessellation basata su curvature/features.

---

# 22. Tolerance model e robustezza numerica

## P0

Canonical geometry unit: **mm**.

Tolleranze esplicite minime:

```text
linear_tolerance_mm
angular_tolerance_deg
join_tolerance_mm
intersection_tolerance_mm
tessellation_chord_tolerance_mm
```

Regole:

- nessuna tolerance escalation silenziosa;
- robust predicates per intersection/orientation/inside-outside;
- failure esplicito e diagnosticabile;
- no geometria corrotta per “far riuscire” un'operazione.

---

# 23. Validazione geometrica

## P0

- no NaN/Inf;
- closed boundary when required;
- manifoldness;
- orientation;
- degenerate element detection;
- self-intersection detection;
- minimum thickness;
- watertight manufacturing mesh;
- volume consistency;
- boundary gap report;
- geometric regression metrics.

Confronto versioni:

```text
max surface deviation
mean deviation
Hausdorff distance
volume delta
area delta
key section deviations
key clinical dimensions
```

---

# 24. Orthosis-specific geometric capabilities

## P0

- BaseTemplate/DIMA;
- closed editable 2D outline;
- length/width constraints;
- medial/lateral semantics;
- UpperSurface;
- LowerSurface;
- thickness field;
- heel cup / wrap;
- camber;
- medial arch;
- lateral arch;
- rearfoot wedge/posting in degrees;
- forefoot wedge/posting;
- metatarsal pad/bar;
- local raise/support;
- local depression/relief;
- corrective element library;
- element position/scale/rotation/integration;
- mirror DX/SX semantic;
- cross-section inspector;
- height map;
- thickness map;
- minimum thickness repair;
- production closure profiles.

## P1

- template morphing;
- deform toward Scan3D;
- pressure-driven target ROI;
- material/stiffness regions.

---

# 25. Join primitive e feature workflow

Il motore deve costruire forme complesse come composizione di primitive/feature senza perdere la storia.

Esempio:

```text
Base orthosis surface
 + medial arch feature
 + heel cup feature
 + metatarsal pad primitive
 - heel relief primitive
 + sidewall closure
 -> solid
```

Ogni feature dovrebbe poter essere enabled/disabled, edited, mirrored, copied, versioned e inspected.

Integrazione possibili:

- union;
- subtraction;
- intersection;
- smooth/blended union [P1/P2];
- deformation field;
- height-field composition.

---

# 26. Feature history / dependency graph

## P0

- ordered operation stack;
- explicit dependencies;
- dirty propagation;
- incremental recompute when possible;
- undo/redo;
- suppress/unsuppress;
- edit parameters;
- clone feature;
- side-specific feature;
- provenance.

## P1

- branching design alternatives;
- compare revisions;
- feature groups;
- reusable presets;
- partial recompute/cache.

## P2

- DAG complesso;
- parametric expressions between features.

---

# 27. Constraints e relazioni parametriche

## P0

- fixed distance;
- fixed angle;
- symmetry/mirror relation;
- aligned landmarks;
- preserve min thickness;
- preserve outline region;
- preserve endpoint/tangent for curves.

## P1

- equal lengths;
- tangent constraints;
- curvature continuity;
- relative dimension expressions;
- parametric formulas.

Non serve replicare un full parametric mechanical sketcher: servono constraint utili al dominio ortesico.

---

# 28. Rendering-facing geometry services

Il geometry core non renderizza, ma deve fornire:

## P0

- render tessellation;
- normals;
- edge/wire geometry;
- selection IDs;
- picking acceleration;
- clipping/section geometry;
- bounding boxes;
- layer visibility;
- scalar fields per height/thickness/pressure/deviation;
- transform matrices;
- incremental mesh update.

## P1

- curvature/deviation heatmap;
- LOD;
- GPU-friendly patch/tessellation data.

---

# 29. Import / export geometric formats

## P0

Input/output:

- STL;
- project-native format/package;
- JSON manifest/report.

## P1

- OBJ;
- 3MF;
- PLY;
- STEP se B-Rep/NURBS interoperability diventa utile;
- IGES solo se un workflow reale lo richiede;
- 3DM se Rhino interoperability è strategica.

## P2

- glTF;
- USD;
- specialized CAM exchange.

Un formato non deve diventare automaticamente la source-of-truth interna.

---

# 30. Manufacturing geometry

## P0

- watertight solid/mesh;
- minimum wall/thickness;
- controlled tessellation.

## P1

- build orientation metadata;
- additive overhang analysis;
- CNC stock bounds;
- engraving/emboss geometry;
- material region masks.

## P2

- cutter reach/undercut analysis;
- multi-material partition.

---

# 31. Implicit / SDF / voxel geometry

Non è necessaria come base, ma può essere backend complementare.

## P2 / alcuni P1

- signed distance field;
- voxelization;
- robust implicit union/difference;
- smooth union;
- offset via level set;
- lattice generation;
- scan cleanup;
- topology-insensitive local relief.

Ogni conversione B-Rep/mesh ↔ SDF deve dichiarare la perdita/tolleranza introdotta.

---

# 32. Curvature fairness e surface quality

## P1

- curvature display;
- zebra/continuity visualization;
- fair curve/surface;
- energy smoothing;
- local oscillation detection;
- tangent continuity repair.

---

# 33. Performance requirements

## P0

- cancellable heavy operations;
- no UI freeze;
- incremental re-evaluation;
- spatial acceleration caches;
- multi-threading quando sicuro;
- render tessellation separata dal manufacturing.

Target iniziali da validare:

```text
camera/render: 60 fps preferred
interactive deformation: >= 30 fps target
parameter update preview: < 100 ms preferred for common operations
heavy exact boolean/remesh: cancellable + progress
```

---

# 34. Precisione numerica

## P0

Usare **double precision** per coordinate, parametri e misure autorevoli salvo motivazione specifica.

Float è accettabile per render buffers/GPU preview, ma non come unica copia autorevole della geometria CAD.

---

# 35. Threading, reentrancy e cancellation

## P0

Ogni backend deve essere auditato per:

- thread safety;
- reentrancy;
- cancellation/progress;
- deterministic behavior;
- global state;
- allocator assumptions.

---

# 36. Serialization e project persistence

## P0

Il project format deve serializzare semantica, non solo mesh finale:

```text
project metadata
coordinate frames
source acquisitions
base template
curve/surface definitions when authoritative
operation stack
corrective elements
ROI/masks
material regions
manufacturing profile
export provenance
```

Asset pesanti possono essere embedded o esterni con hash.

## P1

- schema migrations;
- delta revisions;
- cache invalidation/versioning;
- portable project package.

---

# 37. API funzionale minima del geometry engine

Esempio concettuale:

```text
CreateCurve(...)
CreateNurbsCurve(...)
CreateNurbsSurface(...)
CreateFaceFromSurface(...)
CreateSolidFromShell(...)

InterpolateCurve(...)
ApproximateCurve(...)
Loft(...)
Sweep(...)
Extrude(...)
Fill(...)

Join(...)
Sew(...)
Trim(...)
Split(...)
Intersect(...)
Offset(...)
Thicken(...)

BooleanUnion(...)
BooleanDifference(...)
BooleanIntersection(...)

Tessellate(...)
Remesh(...)
RepairMesh(...)
SmoothMesh(...)

ClosestPoint(...)
Project(...)
Measure(...)
Section(...)
ComputeThickness(...)
Validate(...)
```

Sopra questo livello:

```text
ApplyMedialArch(...)
ApplyHeelCup(...)
ApplyRearfootWedge(...)
ApplyMetatarsalPad(...)
ApplyLocalRelief(...)
```

---

# 38. Capability priority matrix

## P0 — indispensabile

### Geometry/topology

- analytic primitives;
- B-spline/NURBS curves;
- B-spline/NURBS surfaces;
- trimmed surfaces;
- B-Rep vertex/edge/wire/face/shell/solid;
- transforms;
- join/sew;
- split/trim/intersection;
- loft/sweep/extrude/ruled/fill;
- offset/thicken/variable thickness;
- booleans.

### Mesh

- import;
- adjacency;
- normals;
- repair;
- remesh;
- smoothing;
- clipping/slicing;
- mesh boolean or equivalent;
- manifold/self-intersection checks;
- tessellation.

### Queries

- closest point;
- projection;
- distance;
- section;
- area/volume;
- height/thickness;
- angles;
- inside/outside.

### Domain

- DIMA;
- heel cup/camber;
- medial/lateral arch;
- rear/forefoot wedge;
- metatarsal bar/pad;
- local relief/support;
- scan fitting;
- mirror DX/SX;
- DFM validation.

## P1 — molto utile

- fillet/chamfer;
- G2 continuity tools;
- advanced knot operations;
- rail sweep;
- advanced fill;
- adaptive remeshing;
- decimation;
- curvature analysis;
- ICP;
- SubD Catmull-Clark;
- adaptive SubD tessellation;
- material/stiffness regions;
- 3MF;
- STEP interoperability;
- richer manufacturing checks;
- feature-preserving deformation;
- project comparison.

## P2 — R&D / advanced

- full SubD modeling;
- SubD→NURBS conversion;
- variational surfacing;
- ARAP;
- implicit/SDF;
- lattice/metamaterials;
- multi-material;
- FEM;
- generative optimization;
- pressure outcome prediction;
- AI-guided geometry;
- full mechanical sketch constraints.

---

# 39. Cosa NON serve replicare subito

Non sono P0:

- assemblies meccanici complessi;
- gears/fasteners;
- sheet metal;
- CAM multi-axis general purpose;
- drafting 2D general purpose;
- GD&T completo;
- PCB/electrical CAD;
- BIM;
- full enterprise mechanical history tree.

---

# 40. Conseguenze per la scelta del kernel/librerie

Questo documento non sceglie lo stack. Ogni candidato va confrontato su:

```text
NURBS curve/surface native support
trimmed surfaces
B-Rep/topology
join/sew
boolean robustness
offset/thicken robustness
loft/sweep/fill
mesh interoperability
mesh repair/remesh
scan fitting
tessellation control
threading
license
platform portability
WASM/server feasibility
serialization
performance
dependency weight
```

Famiglie già studiate:

- **Open CASCADE / OCCT**: riferimento per set B-Rep + curve/surface + modeling algorithms; non implica adozione automatica.
- **CGAL Polygon Mesh Processing**: riferimento per boolean/remeshing/repair/intersection/distance su mesh; licenze e moduli vanno valutati.
- **openNURBS**: utile per NURBS evaluation/interchange/3DM, non equivalente a un full solid-modeling kernel.
- **OpenSubdiv**: utile per subdivision evaluation/tessellation interattiva, non sostituisce B-Rep/trim/boolean/offset/manufacturing.

La decisione deve essere **capability-driven**, non library-driven.

---

# 41. CAD Kernel Qualification Suite

Prima di adottare uno stack, creare fixture automatiche.

## KQ-001 — NURBS curve

Create/evaluate/split/join/offset/serialize.

## KQ-002 — NURBS surface

Create/evaluate UV/normal/trim/section/tessellate.

## KQ-003 — Loft orthosis

Loft tra profili ortesici senza fold/self-intersection.

## KQ-004 — Variable thickness

Genera volume con thickness variabile e misura errore.

## KQ-005 — Heel cup

Heel wrap smooth, senza self-intersection.

## KQ-006 — Medial arch

Start/center/end + height riproducibili.

## KQ-007 — Wedge

Rearfoot wedge 2°, 4°, 6°: misura risultante entro tolleranza.

## KQ-008 — Element union

Metatarsal pad integrato senza non-manifold edges.

## KQ-009 — Relief subtraction

Sottrazione locale con volume valido.

## KQ-010 — Scan deform

Deformazione verso scan preservando contorno protetto.

## KQ-011 — Mesh repair

Fixture con holes, flipped normals, degenerate faces, duplicate vertices, small components.

## KQ-012 — Boolean stress

Near-coplanar, tangent contact, tiny feature, nested body, invalid self-intersecting input.

## KQ-013 — Offset stress

Curvature alte: failure diagnostics e local minimum radius.

## KQ-014 — Tessellation

Verifica chordal deviation e manifold output.

## KQ-015 — Round-trip

Serialize → reload → regenerate → geometric equivalence.

---

# 42. Relazione con EasyCAD2

Le capability generalizzano i moduli EasyCAD2:

```text
DIMA                 -> curve/splines + constraints
MODIFICA              -> parametric/freeform surface operations
ELEMENTI              -> primitives/features + boolean/integration
POST PROCESSING       -> mesh/freeform deformation + smoothing
CONTROLLO             -> section/distance/height/thickness/angle queries
PRODUCI               -> solid closure + tessellation + manufacturing validation
Mirror DX/SX          -> transform + anatomical semantics
Material modifiers    -> region/mask + manufacturing properties
```

---

# 43. Reference sources

## Project references

- `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md`
- `docs/references/easycad2/README.md`
- `docs/research/SOURCES.md`
- `docs/DECISIONS.md`
- `docs/RESUME_HERE.md`

## Geometry/CAD references

### Open CASCADE Technology

Official documentation describes B-Rep as topology binding mathematical geometry such as analytic curves/surfaces, Bézier and NURBS, and documents booleans, filling, pipe/sweep and B-spline construction.

- https://dev.opencascade.org/doc/overview/html/
- https://dev.opencascade.org/doc/overview/html/occt_user_guides__modeling_algos.html
- https://dev.opencascade.org/doc/refman/html/class_geom___b_spline_curve.html
- https://dev.opencascade.org/doc/refman/html/class_geom___b_spline_surface.html

### CGAL Polygon Mesh Processing

Official CGAL documentation covers polygon mesh processing, boolean operations, clipping/splitting/slicing, remeshing, simplification, smoothing, repair, boundary stitching, degeneracy and non-manifold detection.

- https://doc.cgal.org/latest/Polygon_mesh_processing/
- https://doc.cgal.org/latest/Manual/packages.html

### openNURBS

McNeel's openNURBS toolkit provides 3DM interchange, NURBS evaluation tools and elementary geometry/view utilities. It is useful evidence for NURBS/interchange capability but is not treated here as a complete solid-modeling kernel.

- https://github.com/mcneel/opennurbs

### OpenSubdiv

Pixar OpenSubdiv provides high-performance subdivision surface evaluation and adaptive CPU/GPU workflows.

- https://opensubdiv.org/
- https://opensubdiv.org/docs/osd_overview.html

---

# 44. DONE / TODO

## DONE

- [x] Functional EasyCAD2-derived product specification exists.
- [x] CAD geometric capability taxonomy defined.
- [x] NURBS/B-spline curve/surface requirements defined.
- [x] B-Rep topology requirements defined.
- [x] Primitive and join/stitch/sew requirements defined.
- [x] Trim/split/intersection/boolean requirements defined.
- [x] Offset/thicken/shell requirements defined.
- [x] Loft/sweep/fill requirements defined.
- [x] Mesh processing requirements defined.
- [x] SubD role classified.
- [x] Point-cloud/scan and registration capabilities defined.
- [x] Geometric queries/tessellation/tolerance/validation defined.
- [x] Orthosis-specific geometry mapped onto CAD capabilities.
- [x] Kernel qualification test suite outlined.

## TODO

- [ ] Freeze `01_coordinate_registration.md`.
- [ ] Freeze Project Schema v0.
- [ ] Freeze geometry operation stack semantics.
- [ ] Define mathematical DIMA model.
- [ ] Define heel/wrap/camber operator.
- [ ] Define medial/lateral arch operators.
- [ ] Define rearfoot/forefoot wedge operator.
- [ ] Define variable thickness field semantics.
- [ ] Define corrective-element integration semantics.
- [ ] Implement CAD Kernel Qualification Suite fixtures.
- [ ] Score candidate stacks against P0/P1/P2 capabilities.
- [ ] Decide exact/mesh/SubD backend composition.
- [ ] Decide whether OCCT is needed, optional or excessive after scoring.
- [ ] Evaluate NURBS-focused alternatives and lightweight stacks.
- [ ] Evaluate web/WASM/server portability for finalists.

---

# 45. Final product requirement

BiomechE-CAD deve costruire e modificare il plantare come **modello geometrico clinicamente parametrico**, non come semplice STL scolpito.

In sintesi il CAD engine deve saper fare:

```text
PRIMITIVES
+ CURVES
+ B-SPLINE / NURBS
+ SURFACES
+ TRIMMED SURFACES
+ B-REP TOPOLOGY
+ JOIN / SEW / STITCH
+ TRIM / SPLIT / INTERSECTION
+ EXTRUDE / LOFT / SWEEP / FILL
+ OFFSET / THICKEN / SHELL
+ BOOLEAN UNION / CUT / INTERSECTION
+ FREEFORM DEFORMATION
+ MESH REPAIR / REMESH / SMOOTH
+ SCAN REGISTRATION / FITTING
+ SECTIONS / DISTANCES / ANGLES / THICKNESS
+ ROBUST TOLERANCES / VALIDATION
+ CONTROLLED TESSELLATION
+ VERSIONED CLINICAL FEATURE HISTORY
```

Questo è il contratto minimo di capacità che deve guidare la scelta della libreria e l'architettura del geometry core.
