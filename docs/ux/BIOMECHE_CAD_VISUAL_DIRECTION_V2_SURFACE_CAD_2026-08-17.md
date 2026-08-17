# BiomechE-CAD — Visual Direction V2: Surface-CAD Workstation

**Date:** 2026-08-17  
**Status:** **ACTIVE VISUAL DIRECTION / NOT YET FROZEN**  
**Scope:** look-and-feel, workspace composition, interaction density and screen-by-screen visual reference.  
**Semantic authority remains:** frozen written specifications and acceptance contracts.  
**Previous visual package:** `BIOMECHE_CAD_VISUAL_REFERENCE_V1.md` + `mockups/v1/` remain valid for functional coverage/traceability, but **do not define the preferred V2 aesthetic**.

---

## 1. Why V2 exists

The first visual baseline successfully covered product states, provenance, warnings, BiomechE integration and manufacturing boundaries, but subsequent visual exploration showed that it reads too much like a medical dashboard/application and not enough like a **high-level professional CAD workstation**.

The preferred direction is now a surface-modeling CAD aesthetic inspired by the structural language of high-end industrial surfacing tools:

- one dominant geometry viewport;
- dark neutral workstation chrome;
- precise, quiet typography;
- compact monochrome toolbars;
- contextual property panels rather than large dashboard cards;
- scene/layer hierarchy;
- curve/control-point/surface editing visible in the viewport;
- orthographic mini-views where useful;
- thin blue active-state accents;
- orange/amber reserved primarily for selected geometry/edges;
- minimal decorative glow;
- visually rich geometry, visually restrained interface.

The goal is **not** to imitate a specific commercial product pixel-for-pixel. The goal is to adopt the interaction grammar and visual hierarchy of serious surface CAD while preserving BiomechE-CAD semantics.

---

## 2. Style fingerprint

### 2.1 Overall character

```text
professional industrial surface CAD
premium desktop workstation
immediate and dense, but not cluttered
technical rather than medical-dashboard
futuristic through precision, not through sci-fi decoration
geometry first
controls second
status/provenance available but visually subordinate
```

### 2.2 Palette doctrine

Approximate direction, not frozen tokens:

```text
application background      graphite / near-black
workspace chrome            dark neutral charcoal
panel separators            low-contrast cool gray
primary text                soft white / light gray
secondary text              desaturated gray
active tab/tool             restrained blue
reference curves/points     cyan / cool blue
selected geometry/edge      amber/orange
success/ready               restrained green
warnings                    amber
errors/blocking             red only when necessary
```

Avoid dominant purple and avoid large neon cyan glows.

### 2.3 Geometry rendering

Preferred:

- physically plausible smooth orthosis surface;
- graphite, clay, pearl-gray or neutral semitransparent material;
- soft studio lighting;
- subtle reflection and contact shadow;
- selected borders/curves visibly overlaid;
- control cage, control points, section curves and reference curves only when contextually relevant;
- optional wireframe/curvature/zebra/analysis overlay modes;
- no default rainbow heatmap on ordinary authoring screens.

Quantitative heatmaps remain available for analysis and local sculpt/inspection contexts, but must not become the generic visual identity of the CAD.

---

## 3. Canonical workstation anatomy for V2

A normal full-screen CAD workspace should generally contain:

```text
TOP APPLICATION BAR
  project/case name, undo/redo/save, global status, help/settings

PRIMARY MODE TABS
  MODELLO | SUPERFICIE | SCULTURA | ANALISI | PRODUZIONE

CONTEXT TOOLBAR
  compact operation icons relevant to current mode

LEFT TOOL RAIL / CONTEXT PANEL
  selection/edit tools or source/reference tools

CENTRAL VIEWPORT
  dominant geometry workspace; approximately 60–75% of usable visual attention

RIGHT CONTEXT STACK
  SCENE / LAYERS
  contextual PARAMETERS / PROPERTIES
  MATERIALS only where relevant

OPTIONAL FLOATING MINI-VIEWS
  top/front/side/perspective or local section views

BOTTOM STATUS BAR
  units, grid, snap, active mode, optional performance/status readout
```

Not every screen must show every panel. Panels should collapse when not relevant.

---

## 4. What to preserve from EasyCAD2 / orthotic-specific workflow

The V2 workstation must still make the orthotic CAD workflow immediately recognizable. The key domain stages remain:

1. source/template/base geometry;
2. parametric edit of heel, medial/lateral arch, forefoot/outline/thickness;
3. corrective/support elements;
4. local sculpt/post-processing;
5. geometric inspection and production preparation.

Source context may include pressure exam, 2D scan and 3D scan, but these should appear as **reference data feeding the CAD**, not as the main application identity.

Corrective elements remain named orthotic objects with placement/size/mechanical properties rather than generic CAD primitives alone.

---

## 5. Explicit anti-patterns from the visual exploration

Do **not** return to these directions unless explicitly requested:

```text
five-screen marketing poster as the main design artifact
medical dashboard cards dominating the workspace
large KPI rings/scores as the primary CAD view
excessive cyan neon / Jarvis HUD decoration
sci-fi grids, circuit borders and ornamental holographic UI
rainbow heatmap on every screen
huge labeled panels with little geometry
large empty margins around small CAD objects
fake low-density consumer-app UI
visual language closer to patient management than to geometry authoring
```

The user explicitly rejected earlier iterations as being too far from a real high-level CAD and insufficiently contextual.

---

## 6. Five V2 canonical workspaces

These replace the earlier idea of designing all screens as a collage. **Generate and review one full-screen image at a time.**

### V2-S01 — Template / Modello

**Status:** ACTIVE — latest candidate exists from 2026-08-17 conversation, **not yet approved/frozen**.

Purpose:

- establish/reference the base orthosis geometry;
- show source context without becoming an import dashboard;
- manipulate outline/reference curves/control points;
- expose dimensions and base/support parameters;
- set the visual grammar for every later screen.

Must contain:

- `MODELLO` active in primary mode tabs;
- compact CAD operation toolbar;
- dominant 3D orthosis viewport;
- neutral clay/graphite orthosis surface;
- selected outline/reference curve with sparse control points;
- dimension annotations in mm;
- source/reference context for pressure / Scan2D / Scan3D in a compact panel;
- Scene/Layers on the right;
- contextual Template/Base parameters on right;
- optional small top/side/rear views;
- bottom status bar with units/grid/snap.

The screen should look usable for several hours of professional CAD work, not like a presentation slide.

### V2-S02 — Superficie / Edit Parametrico

Purpose:

- modify heel cup, medial arch, lateral arch, forefoot wrap/shape, posting, outline and thickness using semantic parameters plus direct manipulation.

Must emphasize:

- full 3D surface;
- surface curves/control cage only where useful;
- contextual parametric tree/panel;
- requested vs realized value where required by frozen contract;
- section/orthographic mini-views;
- direct manipulation + numeric input.

### V2-S03 — Elementi

Purpose:

- add and position met pad, heel lift, medial/lateral wedge, arch support, cut-out/relief and other semantic corrective objects.

Must emphasize:

- element library as compact object palette;
- actual 3D element selected on orthosis;
- transform manipulator;
- typed anatomical/reference placement;
- dimensions/position values;
- Scene/Layers showing each element as an object;
- property inspector for selected element.

### V2-S04 — Scultura / Post Processing

Purpose:

- local freeform refinement while preserving replay/provenance and protected regions.

Must emphasize:

- large sculpt viewport;
- brush cursor/footprint;
- Raise/Lower/Smooth/Flatten/Pinch/Mask/Protect semantics;
- optional local thickness/curvature/deviation overlay;
- protected regions/layers;
- brush radius/intensity/falloff;
- local section profile at bottom.

### V2-S05 — Analisi / Produzione

Purpose:

- geometry inspection, sections, thickness/curvature/deviation, DFM and manufacturing release preparation.

Must emphasize:

- orthosis geometry remains dominant;
- selected analysis mode (thickness/curvature/deviation);
- reproducible section cuts;
- explicit DFM checks;
- STL/3MF and CNC/manufacturing handoff as contextual production panel;
- artifact generation remains distinct from manufacturing release.

BiomechE pressure comparison may be linked/opened contextually, but this screen should still read first as **CAD inspection/manufacturing**, not a clinical analytics dashboard.

---

## 7. V2-S01 generation brief — exact restart point

When resuming visual work, do not generate a new five-screen collage. Generate **one V2-S01 full-screen workstation image only**.

Recommended image framing:

```text
standard desktop CAD screen
16:9 or workstation-wide aspect
single application window filling image
no external title/poster framing
no presentation-board labels
```

Composition priority:

```text
1. central orthosis surface viewport
2. professional top CAD mode/tool bars
3. right Scene/Layers + contextual parameters
4. compact left source/reference + tool rail
5. mini orthographic views and status bar
```

Visual target:

> High-end industrial surface-modeling CAD adapted to orthotic insoles: dark graphite UI, calm precision, dense compact controls, professional surface viewport, control curves and dimensions, minimal blue highlights, amber selection, no decorative Jarvis glow.

---

## 8. Approval protocol

For each V2 screen:

```text
GENERATE -> REVIEW WITH USER -> REVISE -> APPROVE -> SAVE AS CANONICAL V2 SCREEN -> NEXT SCREEN
```

Do not infer approval from generation alone.

Screen status values:

```text
DRAFT
REVIEW
APPROVED
SUPERSEDED
```

Only `APPROVED` visual assets become V2 visual references.

---

## 9. Relationship with V1

V1 remains useful and must not be deleted because it captures:

- semantic requirement coverage;
- state coverage;
- accessibility findings;
- provenance/workflow examples;
- reproducible rendering infrastructure.

V2 changes **visual grammar and workspace composition**, not the frozen domain semantics.

Therefore:

```text
V1 = functional/traceability visual baseline
V2 = active high-level CAD aesthetic/workstation baseline
written specs = semantic authority
```

---

## 10. Current restart status

```text
V2 style doctrine             CAPTURED
five CAD workspaces           DEFINED
V2-S01 latest candidate       GENERATED IN 2026-08-17 SESSION / NOT APPROVED
V2-S02                        NOT GENERATED
V2-S03                        NOT GENERATED
V2-S04                        NOT GENERATED
V2-S05                        NOT GENERATED
Q0 geometry qualification     READY / PARKED WHILE VISUAL V2 IS BEING REFINED
geometry engine winner        NONE
```

Next visual action: **review/refine V2-S01 only** until approved, then persist it as the canonical first V2 screen and move to V2-S02.
