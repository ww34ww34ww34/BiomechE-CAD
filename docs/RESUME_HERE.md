# BiomechE-CAD — RESUME HERE

> **Purpose:** this is the first document to read when resuming BiomechE-CAD after any interruption. It records the current functional baseline, evidence hierarchy, audit state, decisions, open gaps and exact next work so a new conversation can continue without reconstructing context.

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Canonical documentation:** Markdown under `docs/`  
**Current checkpoint:** 2026-08-14 — EasyCAD2 manual + 1.4 validation consolidation completed and audited against the previous EasyCAD2 research.

---

## 1. Project goal

BiomechE-CAD is intended to become a professional vertical CAD for custom foot orthoses/insoles integrated with BiomechE.

The first product baseline deliberately uses EasyCAD2 as the most detailed behavioral reference currently available, while the architecture is intended to be more open, versionable, testable and scientifically traceable than a mesh-only commercial workflow.

Current target flow:

```text
Patient / Case
    -> OrthosisProject [LEFT/RIGHT]
    -> AcquisitionLayer[]
    -> Registration
    -> BaseTemplate
    -> ParametricOperation[]
    -> CorrectiveElement[]
    -> MaterialModifier[]
    -> SculptOperation[]
    -> Analysis + DFM/QC
    -> ManufacturingProfile
    -> ExportArtifact[]
    -> Report
```

---

## 2. Source-of-truth hierarchy

### Level A — primary EasyCAD2 evidence

1. `EasyCAD2 Manuale ITA 2.0.pdf` — internal software version 1.1.x.x.
2. `PdV0001_EasyCAD2 software validation plan.pdf` — validation baseline for EasyCAD2 1.4.x.x, 15/01/2026.
3. `RdT001_Rapporto di Test di validazione software EasyCAD2 versione 14xx.pdf` — final report, 20/01/2026.

The 1.1 manual is used for detailed UI/parameter behavior. The newer 1.4 validation documents are used to confirm that capabilities remained/currently existed in the later line even when the public manual is older.

### Level A2 — research and scientific evidence

Preserve:

- prior EasyCAD2 feature-by-feature research;
- EasyCAD/easyCAD lineage findings;
- vendor/market sources;
- peer-reviewed foot-orthosis literature;
- competitor research as it is added.

Useful scientific baseline currently includes Telfer 2013, Farhan 2021, Muir 2022, Cherni 2022, Xu 2019, Ruiz-Ramos 2024 and Allan 2023. Exact bibliographic details are in the consolidated specification and `research/SOURCES.md`.

### Level B — engineering decisions

Use `DECISIONS.md`. Source evidence must not silently become an engineering rule.

### Level C — current specification

The current canonical functional baseline is:

- `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md`

Future modular specifications should supersede or refine parts of it without deleting historical source evidence.

---

## 3. Provenance convention

Use these tags when origin matters:

```text
SOURCE / EASYCAD2-MANUAL
SOURCE / EASYCAD2-VALIDATION
SOURCE / EASYCAD-LEGACY
SOURCE / LITERATURE
SOURCE / MARKET
ENGINEERING DECISION
OPEN QUESTION
R&D CANDIDATE
```

Never invent a source locator or silently promote an inferred vendor behavior into a BiomechE-CAD requirement.

---

## 4. Current EasyCAD2 evidence baseline

### Confirmed workflow areas

```text
DATABASE / SETTINGS
DIMA
PRESSURE
SCAN3D
SCAN2D / IMAGE2D
MODIFICA
ELEMENTI
POST PROCESSING
CONTROLLO
PRODUCI
REPORT
TOOLBAR / HISTORY / SAVE
```

### Important capabilities now confirmed from primary documents

- patient database, search, edit/delete and project history;
- left/right project switching and project mirroring;
- DIMA templates `SPORT`, `SANDALO`, `CLASSIC`, `COMFORT`, `DONNA`;
- editable DIMA outline, L/W dimensions, shoe size and unlocked proportions;
- pressure import `.bpe/.csv` with X/Y/rotation/scale;
- Scan3D `.stl`, `heel`, `1st`, `5th` landmarks and alignment;
- Image/Scan2D calibration;
- global thickness and flatten;
- rearfoot heel/wrap + camber parameters;
- medial/lateral arch parameter sets including start/center/end, height, depth and curvature;
- rearfoot/forefoot wedges in degrees, full/partial application;
- element library by rearfoot/midfoot/forefoot/proprio/custom categories;
- metatarsal-bar family visible in the EasyCAD2 library/workflow;
- element position, rotation and XYZ scaling;
- custom element vertex editing + reusable preset;
- 3D-print modifier regions for differentiated rigidity;
- global/per-element five-level hardness workflow;
- local sculpt with radius/strength;
- global deformation toward loaded scan/pressure data;
- freehand/circle closed-region height deformation;
- cross-section, fixed-height controls, height visualization and ruler;
- minimum-thickness warning below 0.8 mm in the EasyCAD2 profile and automatic fix;
- production closure modes Bridge, Straight and Oblique plus advanced hybrid controls;
- STL, GCODE, project ZIP and print workflow;
- text in Slice3D;
- material/CNC/printer profiles;
- PDF report in the 1.4 validation baseline;
- undo/redo/action history;
- safe save on application close.

The EasyCAD2 1.4 validation report records 25/25 planned tests passed, 0 failed and 0 blocked.

---

## 5. Current architecture direction

### 5.1 Non-destructive operations

Where technically reasonable, preserve clinical/geometric operations as parameters instead of only baking them into a final mesh.

Conceptually:

```text
measurement/evidence
    -> prescription
    -> parametric operation
    -> evaluated geometry
    -> manufacturing artifact
```

An operation should be able to preserve:

```text
id
type
side
anatomical region
parameters + units
ROI/mask
source dataset
clinical rationale
author/time
algorithm version
before/after metrics
enabled state
```

### 5.2 Pressure is quantitative data

Pressure must remain a numeric, metric dataset with provenance and registration; it must not be reduced to an RGB background texture.

### 5.3 Coordinate semantics follow BiomechE

Canonical public units should remain aligned with BiomechE:

```text
distance = mm
angle = deg
pressure = kPa
force = N
area = mm2
```

Sensor/matrix orientation must not be confused with anatomical coordinates.

### 5.4 Materials are separate from geometry

A stiffness/density/material modifier is a first-class region, not merely an external print setting or forced geometric deformation.

### 5.5 CAM is downstream

GCODE/CNC post-processing belongs outside the core geometric model.

---

## 6. Current baseline decisions

The initial decision set is tracked in `DECISIONS.md` as `D-CAD-001` through `D-CAD-010`.

Core direction:

1. Markdown is canonical documentation.
2. EasyCAD2 is the initial behavioral benchmark, not the architectural ceiling.
3. Prefer versioned/non-destructive geometry operations.
4. Use BiomechE-compatible canonical physical units.
5. Acquisition provenance + registration transform are first-class data.
6. Pressure remains quantitative.
7. Material/stiffness regions are separate from pure geometry.
8. CAM/GCODE is separated from geometry core.
9. Exports bind to immutable project revisions.
10. Every P0 feature needs acceptance criteria/regression testing.

---

## 7. Audit status — previous EasyCAD2 research

**AUDIT COMPLETE for the current consolidation.**

The earlier EasyCAD2 feature inventory was checked against the new unified specification.

### Preserved

- all previously listed direct EasyCAD2 features;
- all earlier P0 requirements;
- scientific rationale for posting/wedges;
- numeric pressure/provenance requirement;
- scan provenance requirement;
- variable-stiffness/material-map direction;
- explainable future automation/AI;
- P0/P1/P2 prioritization.

### Earlier lineage/secondary findings promoted by the new primary documents

Now confirmed or substantially confirmed:

- controlateral mirror;
- arch start/center/end/curvature details;
- wedge angles in degrees;
- custom elements;
- metatarsal bars;
- proprioceptive element category;
- material/stiffness modifier regions;
- global/per-element hardness;
- global deformation from exam data;
- Bridge production closure;
- minimum-thickness DFM warning + fix;
- PDF report;
- history/undo/redo.

### Still open / not silently promoted

- exact mathematical formulas used internally by EasyCAD2;
- automatic DIMA generation specifically from Scan3D;
- cloud template library;
- wedge input directly in mm;
- automatic patient-name engraving rather than generic 3D text;
- exact toolpath/GCODE algorithm;
- 3MF/multi-material native export;
- OBJ/STEP support;
- SDK/API/plugin system;
- formal project schema/migration behavior;
- positive mould generation for thermoforming;
- exact regulatory/conformity report;
- general third-party hardware compatibility.

---

## 8. Copyright / source handling rule

The EasyCAD2 manual contains a copyright/reproduction restriction. Therefore:

- do not commit manual screenshots or the PDFs to this public repository without explicit rights clearance;
- keep page numbers, feature descriptions and source URLs in the research/specification documents;
- screenshots may be inspected for research but should not be redistributed automatically.

---

## 9. Current P0 functional envelope

### Workflow / persistence

- patient/case/project;
- LEFT/RIGHT;
- mirror;
- versioned project;
- undo/redo/history;
- autosave/crash-safe close.

### Acquisition

- BiomechE pressure;
- CSV pressure;
- STL scan;
- 2D image;
- registration;
- heel/1st/5th landmarks;
- source provenance.

### DIMA

- template library;
- L/W;
- outline edit;
- custom template.

### Parametric modification

- thickness/flatten;
- heel/wrap/camber;
- medial arch;
- lateral arch;
- rearfoot wedge;
- forefoot wedge;
- smooth.

### Elements / sculpt

- heel, arch, metatarsal and local offload/support elements;
- local raise/lower;
- ROI deform;
- deform toward scan.

### QC

- section;
- height;
- ruler;
- wedge angle;
- thickness map;
- minimum thickness;
- manifold/self-intersection/degenerate checks.

### Production

- STL;
- versioned project package;
- production closure;
- DFM report.

---

## 10. Critical open questions before kernel implementation

1. Coordinate and registration contract for pressure, Scan3D, Image2D, template and output mesh.
2. Project Schema v0 and migration/versioning rules.
3. BaseTemplate mathematical representation.
4. Operation Stack evaluation semantics and dependency graph.
5. Mathematical definition of heel/wrap/camber.
6. Mathematical definition of medial/lateral arch operators.
7. Mathematical definition of rearfoot/forefoot wedge and reference axis.
8. Local ROI deformation/falloff model.
9. Geometry kernel and mesh representation choice.
10. Thickness/offset strategy and robustness.
11. Boolean/element integration strategy.
12. Manufacturing closure semantics.
13. Material/stiffness physical property model.
14. Exact regression/golden geometry strategy.
15. API boundary between BiomechE and CAD.

---

## 11. Exact restart point

**Next specification work:**

```text
1. docs/spec/01_coordinate_registration.md
2. docs/spec/02_project_schema.md
3. docs/spec/03_geometry_operation_model.md
4. mathematical operators:
   - heel/camber
   - medial arch
   - lateral arch
   - rearfoot/forefoot wedge
5. geometry-kernel evaluation against those requirements
```

Do not start implementation by choosing a mesh library in isolation. The operator semantics, units, coordinate frames, persistence requirements and regression invariants should constrain the kernel choice.

After the common geometry baseline, continue the market audit using the EasyCAD2-derived feature matrix as a fixed comparison frame, starting with **ParoContour / DIERS**, then FitFoot360, Rodin4D/Neo, Vorum/Canfit and other relevant systems.

---

## 12. DONE

- [x] Broad CAD/orthosis research initiated.
- [x] EasyCAD2 feature-by-feature first audit completed.
- [x] EasyCAD2 Manual 1.1.x.x acquired and inspected.
- [x] EasyCAD2 Validation Plan 1.4.x.x acquired and inspected.
- [x] EasyCAD2 Validation Report 1.4.x.x acquired and inspected.
- [x] 25 validation user stories integrated.
- [x] Previous EasyCAD2 research audited for loss/coverage.
- [x] Unified functional specification created.
- [x] Specification committed to `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md`.
- [x] Dynamic handover initialized.
- [x] BiomechE documentation method adopted as the project documentation model.

---

## 13. TODO

- [ ] Finish competitor-by-competitor market research using the unified feature matrix.
- [ ] Deep audit ParoContour / DIERS.
- [ ] Audit FitFoot360.
- [ ] Audit Rodin4D/Neo.
- [ ] Audit Vorum/Canfit.
- [ ] Expand competitor list internationally.
- [ ] Create coordinate/registration specification.
- [ ] Create Project Schema v0.
- [ ] Create geometry operation model.
- [ ] Specify heel/arch/wedge mathematics.
- [ ] Evaluate geometry kernels.
- [ ] Define material/stiffness physical model.
- [ ] Define manufacturing/DFM profiles.
- [ ] Define validation/golden-mesh framework.
- [ ] Complete scientific reference ledger.
- [ ] Add regulatory/privacy analysis.
- [ ] Re-audit this handover after every substantial new research batch.

---

## 14. Handover maintenance protocol

At the end of every substantial work session:

1. update the relevant canonical spec/research document;
2. record important source provenance;
3. update DONE/TODO here;
4. update current open questions;
5. state the exact next restart point;
6. audit whether a newly verified source changes an older conclusion;
7. keep superseded source evidence rather than silently deleting it;
8. if material compaction/deletion is desirable, explicitly review it first;
9. do not leave a major decision only in chat — migrate it to Markdown;
10. keep this file short enough to resume efficiently but complete enough to recover the project state.
