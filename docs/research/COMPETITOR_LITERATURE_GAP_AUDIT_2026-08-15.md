# BiomechE-CAD — Competitor + Literature Gap Audit — Second Pass

**Date:** 2026-08-15  
**Status:** SECOND-PASS EXTERNAL AUDIT / evidence intake for next specification freeze  
**Scope:** current orthotic CAD/CAM market workflows + scientific literature needed to answer remaining BiomechE-CAD specification questions.  
**Architecture:** intentionally out of scope; this audit does **not** select OpenSubdiv, ON_SubD, OCCT, Manifold or another geometry foundation.  
**Evidence rule:** vendor material proves public market capability only; scientific papers support/limit biomechanical or measurement claims; neither source type is allowed to create undocumented universal clinical defaults.

---

## 1. Why this second pass exists

The first competitor audit established the broad market baseline. This second pass asks the more implementation-relevant questions that remained open:

```text
Which operator-productivity capabilities are already normal in mature orthotic CAD systems?
Which anatomical/geometry parameters can be frozen semantically now?
Which parameters must remain profile/population/protocol specific?
Which acquisition facts materially alter orthosis design?
Which manufacturing tolerances can be generalized, and which cannot?
How much of the workflow should be deterministic/replayable before selecting a geometry kernel?
```

The strongest conclusion is that the remaining gap is no longer primarily a lack of feature ideas. It is the need to turn feature ideas into a reproducible **authoring contract** with explicit dose, anatomical reference, acquisition context, versioned workflow automation and measurable acceptance.

---

## 2. Additional current competitor systems reviewed

This pass extends the previous EasyCAD2 / OrthoCAD / Insolution / Voxelcare / Sharp Shape baseline with the following systems.

### FitFoot360 / FIT360

Current public product material documents:

```text
3/4 and full-foot rigid/soft orthoses
milled, 3D-printed and positive-mould workflows
clinical tools and reusable stored design ideas
single-button/replay-oriented design workflows
user-owned design knowledge / best-practice libraries
regional modifier models for variable infill/stiffness zones
```

Evidence intake:

- https://fit360ltd.com/FitFoot360.html
- https://fit360ltd.com/
- https://fit360ltd.com/FitPrint360.html

### paromed paro360 / paroContour

Current public material documents an integrated capture -> scan -> modelling -> two-sided milling workflow and, importantly, a mature concept of reusable `histories` / profiles:

```text
upper + lower surface design
orthopaedic markers
reusable histories / profiles
automatic placement of design elements from selected history
manual dose adjustment after placement
saved angle profiles
heel-cup defaults
bilateral copy/mirror workflow
soft-pad integration
both-side milling and exact underside/shoe realization
```

Evidence intake:

- https://paromed.de/en
- https://paromed.de/en/360-products/modelling/software
- https://paromed.de/en/blog/a/65/questions-and-answers-all-around-parocontour
- https://paromed.de/en/blog/a/120/custom-3d-brand-insoles
- https://paromed.de/en/TorsionFlex

### Qwadra Canfit / Rodin4D ecosystem

Current Canfit material documents:

```text
3D scan and/or manual measurements
anatomically-oriented modification tools
workflow macros
saved build-ups/reductions/trimlines with overlays
X-ray/photo/reference-line superposition
3D preview
measurement and clinical-correction capture
longitudinal patient-change tracking
```

Rodin4D/Qwadra continues to expose a broad scan -> rectification -> machining/3D-print ecosystem and a foot-orthosis-specific Arkad direction.

Evidence intake:

- https://qwadra.com/solution/canfit-design-software/
- https://qwadra.com/landing-page/
- https://www.rodin4d.com/

### Amfit Correct & Confirm

Current public material documents:

```text
prescription-based orthosis design
design templates
user-created reusable standard adjustments
corrective/supportive/offload adjustment libraries
multiple foot capture conditions including semi/full weight-bearing and seated
scanner -> CAD -> in-house mill / central fabrication
cloud data services and fabrication manifests
```

Evidence intake:

- https://amfit.com/solutions/correct-and-confirm-software/
- https://amfit.com/company/technology-overview/
- https://amfit.com/products/cadcam-mill/
- https://amfit.com/solutions/amfitcam-cnc-software/

### Sharp Shape AOMS — current feature evolution

Current public AOMS material shows that orthosis-specific named corrections continue to be product-level concepts rather than generic mesh editing. Recent published additions include Morton extension, UCBL, first-ray cutout, medial/lateral flanges, heel stabilizers, plantar fascial groove, navicular accommodation and medial clip, alongside long-standing CAD/CAM and cast-correction workflows.

Evidence intake:

- https://www.sharpshape.com/WhatIsNew.html
- https://www.sharpshape.com/download.html

### EasyCAD2 / easyCAD Insole — current official public baseline

Current Sensor Medica pages confirm the already-known baseline and make some workflow expectations particularly explicit:

```text
pressure / Scan2D / Scan3D inputs
template editing
heel / medial arch / lateral arch / wrap editing
corrective-object library
manual/freehand modifications
minimum thickness and wedge-angle inspection
contralateral symmetry
custom model/template generation
CNC G-code and STL production
```

Evidence intake:

- https://www.sensormedica.com/en/easycad-2/
- https://www.sensormedica.com/en/easycad-insole/

---

## 3. Revised market table stakes

After the expanded audit, the following capabilities should be treated as market baseline rather than differentiation:

```text
2D/3D foot acquisition
pressure integration in at least part of the market
orthosis-specific named corrections
prescription/template-driven authoring
reusable user/library design knowledge
local add/remove/relief operations
explicit heel/arch/posting/corrective-element controls
bilateral/mirror/copy assistance
inspection tools (sections, distances, angles, overlays)
upper/lower or clinical/production realization workflows
CNC and/or 3D-print output
patient/history/reorder workflow
some level of workflow automation
```

The important change from the first audit is that **workflow reuse is not a niche feature**. Canfit macros, FitFoot360 reusable design knowledge, paro360 histories/profiles, Amfit saved standard adjustments and EasyCAD model/template generation all point in the same direction.

Therefore `GAP-COMP-001` should be elevated:

```text
OLD: P1 product UX / semantic layer
NEW: P0 semantic infrastructure + P1 advanced automation/authoring UX
```

P0 does not mean hidden auto-prescription. It means the data model and operation system must be able to represent a named, versioned, inspectable and replayable multi-operation workflow from day one.

---

## 4. Scientific literature answering the remaining questions

### 4.1 Reproducible CAD authoring is itself a scientific/engineering requirement

**Source intake:** Wang JZ et al. *Computer-aided design methods for digitizing the foot and ankle orthoses manufacturing workflow: A scoping review.* Prosthet Orthot Int. 2025. PMID `41084107`; DOI `10.1097/PXR.0000000000000496`.

The review included 73 studies and found considerable variation in CAD workflows; 46.6% of included papers poorly described or did not describe design procedures sufficiently. It also found orthotic-specific CAD generally faster to operate than general-purpose CAD and proposed a checklist to improve standardization/reproducibility.

**BiomechE-CAD consequence:** the Geometry Authoring Contract is not documentation bureaucracy. It is a direct response to a known reproducibility problem in digital orthotics.

Every clinically/manufacturing meaningful operation should therefore preserve at least:

```text
operation type
side
anatomical target
reference landmark/frame
numerical dose + unit
spatial extent / influence region
material/mechanical state where relevant
source acquisition / registration
algorithm version
ordered predecessor context
preset/macro version
operator override/rationale where required
```

A screenshot or final mesh is not sufficient authoring provenance.

---

### 4.2 Weight-bearing condition must be first-class acquisition metadata

**Source intake:** Chhikara K et al. *Does Scanner Choice Matter for the Design of Foot Orthosis?* Sensors. 2025;25(3):869. PMID `39943509`; PMCID `PMC11820986`; DOI `10.3390/s25030869`.

In the studied workflow, scans differed among scanners, but orthosis designs did not significantly differ within the same weight-bearing condition; medial arch height and heel width changed significantly when weight-bearing condition changed.

**BiomechE-CAD consequence:** scanner identity/quality remains qualification metadata, but `weightBearingCondition` is mandatory semantic context for Scan3D-based design. A PWB/NWB/FWB acquisition must not silently substitute for another.

Recommended acquisition semantics:

```text
weightBearingCondition = NWB | PARTIAL | FULL | OTHER_NAMED
capturePosture
captureMethod
support/contact condition
operator/device provenance
```

Exact allowable substitutions remain profile-owned.

---

### 4.3 Landmark extraction must preserve provenance; automatic landmarks are not unquestioned truth

The wider scanning literature reports variable reliability/accuracy depending on the parameter being measured and the capture method.

**Source intake:**

- Farhan M et al. *Comparison of 3D scanning versus traditional methods of capturing foot and ankle morphology for the fabrication of orthoses: a systematic review.* 2021. PMID `33413570`.
- Potier C et al. *Toward subtalar joint axis-driven CAD/CAM foot orthoses: Reliability of a noninvasive clinical scanning protocol.* Prosthet Orthot Int. 2025;49(1):83-91. PMID `38517378`; DOI `10.1097/PXR.0000000000000343`.

**BiomechE-CAD consequence:** a landmark must carry how it was obtained:

```text
MANUAL_PALPATION_MARKER
MANUAL_ON_SCAN
DEVICE_PROVIDED
ALGORITHM_DERIVED
IMPORTED
```

and where appropriate:

```text
algorithm/version
operator
confidence/quality
source acquisition
review/confirmation state
```

Heel + first/fifth metatarsal-head landmarks remain a practical initial anatomical frame, but more advanced axes such as STJ-related constructs must be treated as optional profile/algorithm inputs, not universal truth.

---

### 4.4 Metatarsal-pad placement must support explicit reference modes; one global default is scientifically unsafe

**Source intake:** Hastings MK et al. *Effect of metatarsal pad placement on plantar pressure in people with diabetes mellitus and peripheral neuropathy.* Foot Ankle Int. 2007;28(1):84-88. PMID `17257544`; DOI `10.3113/FAI.2007.0015`.

In that specific diabetic-neuropathy/history-of-ulcer population, placement around 6.1–10.6 mm proximal to the metatarsal-head line consistently reduced pressure, while sufficiently distal placement could increase pressure.

**Additional source intake:** *Optimal placement of metatarsal pads for patients with hallux valgus based on plantar pressure measurement.* 2025/2026 publication record, PMID `40707294`. In that hallux-valgus crossover study, 76% foot-length placement reduced central metatarsal pressure.

These are not contradictory rules; they use different populations and reference constructs.

**BiomechE-CAD consequence:** metatarsal placement should support named reference semantics such as:

```text
DISTANCE_FROM_MET_HEAD_LINE_MM
NORMALIZED_FOOT_LENGTH
LANDMARK_RELATIVE
PRESSURE_TARGET_RELATIVE
CUSTOM_REGISTERED_REFERENCE
```

The design must preserve the chosen reference representation and outcome context. No single mm or percentage value becomes a universal preset.

---

### 4.5 Arch support is a dose with redistribution risk, not a single “more support” slider

Existing project evidence already shows arch geometry, stiffness/material and outcome must remain separate. The extended literature reinforces the need to treat arch height/support as a bounded dose because increasing support can alter pressure and internal tissue loading differently across regions.

**BiomechE-CAD consequence:** an arch operation needs, at minimum:

```text
height/dose
longitudinal position
medial/lateral extent
transition/blend extent
anatomical reference
material/mechanical region reference
side
profile/context
```

and pressure-informed evaluation should inspect target + adjacent/safety + remote regions. A higher arch is not automatically a better arch.

No universal maximum/minimum clinical height is frozen by this audit.

---

### 4.6 Heel cup, heel relief/plug and medial heel skive are different operations

The literature and mature commercial systems both support maintaining named heel operations instead of compressing them into generic sculpting.

A medial heel skive modifies rearfoot loading through a distinct geometric mechanism; heel cups alter containment/contact; local heel plugs/reliefs modify local cushioning/pressure behavior.

**BiomechE-CAD consequence:** retain separate semantic operation families:

```text
HeelCup / HeelContainment
HeelRelief / HeelPlug
HeelCamber
MedialHeelSkive / named posting operation
HeelMechanicalRegion
```

A generic brush may implement geometry internally, but it must not erase the named prescription meaning.

---

### 4.7 Geometry dose and mechanical/material dose must remain separate — and can vary regionally

Existing canonical `REF-CAD-099` already supports subject/load-dependent cushioning stiffness. Current FitFoot360 public material additionally demonstrates that regional modifier models / variable infill zones are already a commercial workflow concept.

**BiomechE-CAD consequence:** preserve at least:

```text
nominal geometric thickness
material identity
material lot where applicable
local mechanical region
manufacturing process/profile
predicted effective property
measured manufactured property
service-aged property
```

Variable infill/lattice/density is a manufacturing/mechanical realization of a prescription region, not merely another geometry brush.

Automatic pressure -> lattice optimization remains P1/P2 until validated for the specific process/material/use case.

---

### 4.8 Pressure-guided iterative redesign is sufficiently supported to be an architectural P0 capability

Existing project literature already includes pressure-informed orthosis studies and iterative/offloading evidence. The broader literature shows that subject-specific, pressure-guided optimization can outperform shape-only approaches in at least specific high-risk populations.

**BiomechE-CAD consequence:** P0 architecture must support the loop:

```text
baseline acquisition
 -> quantitative target/ROI
 -> DesignRevision
 -> manufactured PhysicalOrthosis
 -> outcome acquisition
 -> compatibility-gated comparison
 -> successor DesignRevision
```

This does **not** require automatic optimization in P0. It requires all identities, transformations and outcome semantics needed to make manual or later algorithmic iteration scientifically traceable.

Automatic/FE/data-driven optimization should remain an explicitly model-backed P1/P2 capability with model/version/uncertainty provenance.

---

### 4.9 No universal manufacturing dimensional tolerance can be taken from the literature

**Context source intake:** *Dimensional accuracy of ankle-foot orthoses constructed by rapid customization and manufacturing framework.* PMID `21328161` reported sub-2-mm results in a particular SLS AFO framework, with much smaller mean component discrepancies.

Existing canonical `REF-CAD-106` already shows that 3D-printed and traditionally fabricated foot orthoses can differ in actual width, arch dimensions and heel-cup height.

**BiomechE-CAD consequence:** do **not** introduce a global `2 mm` manufacturing tolerance.

Instead define:

```text
ManufacturingProfile
  -> process/material/machine
  -> feature or region
  -> inspection method
  -> qualified tolerance
  -> reference-equipment uncertainty
  -> pass/fail rule
```

A design-vs-manufactured difference map should be a first-class QC artifact, but the allowable deviation is profile/feature/process-specific.

---

## 5. Updated product-gap decisions

### GAP-COMP-001 — versioned workflow macro/preset orchestration

**Revised priority:** **P0 semantic infrastructure / P1 advanced UX automation**.

Minimum P0 contract:

```text
MacroDefinition id + version + hash
ordered semantic operations
parameter dependencies/defaults
explicit per-case overrides
preview before commit
expansion snapshot or exact resolvable definition
side/mirror policy
operator/rationale where required
historical immutability
```

A macro may suggest or instantiate operations, but disease/profile-specific clinical assumptions cannot activate invisibly.

### GAP-COMP-005 — bilateral authoring / safe transfer

**Priority:** P0 UX + semantic layer.

Competitor workflows make bilateral copy/mirror/reuse an operator-efficiency expectation. BiomechE-CAD already has frozen side semantics; the UI contract should now explicitly support:

```text
mirror entire design
copy selected operation/preset
transfer parameters without mirror
compare RIGHT/LEFT side-by-side
edit independently after transfer
```

Every action creates/updates target-side semantic state without mutating source history.

### GAP-COMP-006 — geometry inspection / difference-map workflow

**Priority:** P0 inspection infrastructure; measured manufacturing comparison becomes active once hardware/process qualification exists.

Required concepts:

```text
section
point distance
angle
local height/thickness
scan/design overlay
nominal/manufactured surface difference
thresholded QC regions
```

This aligns market practice with the existing project distinction between nominal design and measured physical geometry.

### GAP-COMP-007 — upper/lower realization and shoe-fit contract

**Priority:** P0 manufacturing realization semantics; P1 richer UX.

paromed and other systems show the operational importance of controlling both foot-facing and shoe-facing realization. BiomechE-CAD should explicitly preserve:

```text
clinical/top-surface prescription
shoe/last/interface constraints
lower-surface realization
closure/sidewall realization
material stack
manufacturing profile
```

Changing shoe-side realization must not silently rewrite the clinical prescription.

### GAP-COMP-008 — acquisition-context / landmark-authoring UX

**Priority:** P0.

The UX must make visible and editable where appropriate:

```text
weight-bearing state
side
scan/device/source
landmark source
landmark confidence/review state
registration quality
```

A user should never need to infer whether an arch was designed from a full-weight-bearing scan, partial-weight-bearing scan or manually edited geometry.

---

## 6. What can now be frozen before kernel selection

The following are sufficiently supported to enter a kernel-independent Geometry Authoring Contract:

```text
1. Every named correction is a semantic operation, not only final mesh displacement.
2. Operation dose/units/reference/extent/side/version survive commit.
3. Scan weight-bearing condition is first-class design context.
4. Landmark source/provenance survives; derived landmarks are reviewable/versioned.
5. Metatarsal placement supports multiple explicit anatomical/reference modes.
6. Arch geometry dose and mechanical dose remain distinct.
7. Heel cup, heel relief/plug, skive/posting and heel mechanical region remain distinct.
8. Bilateral mirror/copy/transfer is explicit and side-safe.
9. Multi-operation workflow macros/presets are versioned, inspectable and historically immutable.
10. Pressure-guided iteration is a native lifecycle workflow.
11. Nominal CAD geometry and measured manufactured geometry remain distinct and comparable.
12. Top/clinical geometry and lower/shoe/manufacturing realization remain semantically separable.
```

None of these decisions selects SubD, NURBS, B-Rep, mesh deformation or another mathematical implementation.

---

## 7. What must remain OPEN

The literature reviewed in this pass does **not** justify freezing universal values for:

```text
arch height limits
the “optimal” heel-cup height
one metatarsal-pad offset
one medial heel-skive depth
generic posting angle
generic scan accuracy requirement
generic registration tolerance
generic manufactured-part dimensional tolerance
one material hardness/stiffness
one infill/lattice density
one pressure-reduction target for all populations
one automatic-prescription algorithm
```

These belong to population/profile/protocol/process qualification or to user-visible presets with explicit provenance and non-transfer guards.

---

## 8. Documentation changes now justified

The next documentation phase should not be another broad feature survey. It should produce four linked contracts:

```text
A. REQUIREMENT TRACEABILITY MATRIX
   functional requirement -> owning spec -> acceptance -> fixture/HIL -> status

B. GEOMETRY AUTHORING CONTRACT P0
   template, thickness, arch, heel, wedge/posting, corrective element,
   relief/offload, sculpt, scan conform, section/measurement and bilateral semantics

C. WORKFLOW / PRESET / MACRO CONTRACT
   versioned reusable operations, parameter dependency, preview, override,
   side/mirror policy and historical reproducibility

D. NUMERICAL / QUALIFICATION REGISTRY
   computational tolerances != acquisition tolerances != manufacturing tolerances
```

The architecture shoot-out should remain parked until A-D provide enough executable numerical/semantic fixtures to compare candidate engines objectively.

---

## 9. Recommended acceptance additions

New/strengthened kernel-independent acceptance directions:

```text
XACC-WF-001  historical macro version remains reproducible after global macro edit
XACC-WF-002  macro expansion is inspectable before commit
XACC-WF-003  profile-incompatible macro target warns/blocks explicitly
XACC-LR-006  selected-operation transfer preserves target-side semantics
XACC-ACQ-014 weight-bearing mismatch cannot compare/apply silently
XACC-LM-001  algorithm-derived landmark stores algorithm/version + review state
XACC-MET-001 met-pad reference mode round-trips without conversion to anonymous XYZ
XACC-QC-051  nominal-vs-measured difference is a measurement artifact, not design mutation
XACC-MFG-052 lower-surface realization change does not mutate clinical prescription dose
```

Exact final IDs should be allocated during the acceptance-suite consolidation pass to avoid namespace collisions.

---

## 10. Competitive position after second pass

At the **specification** level, BiomechE-CAD already covers most publicly evidenced functional categories of mature orthotic CAD/CAM systems. The largest current gaps are not basic modelling capabilities; they are operator-productivity and authoring-contract details:

```text
workflow macros / reusable histories
bilateral transfer UX
inspection/difference maps
explicit top-vs-bottom realization workflow
acquisition/landmark provenance UX
```

Conversely, the existing BiomechE-CAD specification intentionally goes deeper than what is established on the reviewed public competitor pages in:

```text
immutable semantic DesignRevision history
explicit quantitative BiomechE KPI authority
protocol/device/ROI compatibility gates
measured != predicted
nominal != manufactured != physical accepted part
calibration/qualification provenance
machine-readable report source manifests
patient outcome loop
```

This is a **specification differentiation target**, not a claim that unreviewed competitor internals lack equivalent mechanisms and not a claim that BiomechE-CAD has already implemented them.

---

## 11. Source-governance note

The external sources introduced by this file are **research intake**. Before a frozen canonical specification relies on a newly introduced scientific or vendor claim, promote the source into `docs/BIBLIOGRAPHY.md` with a stable ID and truthful locator.

High-priority bibliography promotions from this pass are:

```text
Wang et al. 2025 CAD workflow scoping review — PMID 41084107
Chhikara et al. 2025 scanner / weight-bearing study — PMID 39943509
Farhan et al. 2021 3D scanning systematic review — PMID 33413570
Potier et al. 2025 STJ-axis digitization reliability — PMID 38517378
Hastings et al. 2007 metatarsal-pad placement — PMID 17257544
hallux-valgus met-pad placement study — PMID 40707294
AFO dimensional-accuracy context study — PMID 21328161
FitFoot360 current product pages
paromed paro360 current product/update pages
Qwadra Canfit current product page
Amfit Correct & Confirm current product page
Sharp Shape AOMS current update/download pages
```

Do not duplicate existing canonical sources such as `REF-CAD-099`, `REF-CAD-106` or the already-registered Sensor Medica / Voxelcare / Sharp Shape entries; enrich them where the source is the same.

---

## 12. Bottom line

The second-pass market and literature audit changes the next step from:

```text
“search for more CAD features”
```

to:

```text
freeze how P0 orthotic authoring is represented and replayed
        +
make workflow reuse a first-class versioned concept
        +
make acquisition context/landmarks explicit
        +
separate clinical geometry from mechanical and manufacturing realization
        +
turn these contracts into acceptance fixtures
```

The geometry kernel remains a downstream implementation choice to be judged against this contract.
