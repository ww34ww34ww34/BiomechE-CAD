# BiomechE-CAD — Canonical Visual Reference v1

**Status:** **CANONICAL VISUAL / INTERACTION REFERENCE v1 — VIS-01 COMPLETE**  
**Date:** 2026-08-16  
**Semantic authority:** written frozen/canonical product specifications.  
**Interaction authority:** `docs/spec/21_product_workflow_interaction.md`.  
**Human-factors evidence:** `docs/research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md`.  
**Architecture:** UI framework and geometry engine deliberately unspecified.

---

## 0. Authority rule

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
THIS DOCUMENT         = VISUAL / INTERACTION REFERENCE
MOCKUP                = SCREEN-LEVEL GOLDEN INTENT
IMPLEMENTATION        = MUST SATISFY BOTH, THEN BE VALIDATED
```

If a mockup appears to contradict a frozen semantic contract, fix the mockup. Do not silently weaken the product specification to preserve appearance.

---

# 1. Visual mission

BiomechE-CAD should feel like a **modern clinical engineering workstation**:

```text
precise
calm
high information density
premium but restrained
medical-tech rather than generic enterprise
fast to scan
obvious side/revision/state
3D-first
quantitative when data exist
provenance available without clutter
```

Avoid:

```text
legacy industrial-CAD chrome
large empty marketing-style cards inside expert workflows
excessive gradients/glow
purple-dominant identity
status conveyed by color alone
hidden clinical state behind decorative icons
raw topology/mesh terminology in ordinary clinical workflows
```

---

# 2. Design principles

## VR-01 — Context is persistent

The active:

```text
case
side
working/committed revision state
profile context
critical warning/blocking state
```

must remain perceptible through authoring screens.

## VR-02 — 3D is the work surface, not decoration

On authoring screens the central viewport gets the largest continuous region. Controls frame the model rather than fragment it into unrelated cards.

## VR-03 — Semantic controls before geometric internals

Normal UI vocabulary is:

```text
Arch height
Heel cup
Rearfoot post
Metatarsal dome
Material region
Target ROI
Requested / Realized
```

not:

```text
vertex 431
face set 7
control cage row 18
```

Engineering/debug views may expose internals separately.

## VR-04 — Direct + numeric editing are peers

A handle/drag operation and the inspector quantity field edit the same semantic parameter. Neither becomes hidden secondary state.

## VR-05 — Requested vs realized is visible where consequential

When constraints/realization can change dose, use paired display:

```text
Requested   5.0 mm
Realized    4.6 mm
Delta      -0.4 mm   [reason]
```

Illustrative only; values are not defaults.

## VR-06 — Provenance uses progressive disclosure

Primary workspace shows only critical provenance:

```text
source identity short label
review state
revision
algorithm/profile/preset badge when relevant
```

Full version/hash/capture lineage is one click away in a drawer/inspector.

## VR-07 — State uses redundant cues

For `VALID`, `WARNING`, `BLOCKING`, `UNRESOLVED`, `SUGGESTED`, `CONFIRMED`, `PREVIEW`, `COMMITTED`, `RELEASED` use text + icon/shape/border and optionally color.

## VR-08 — Quantitative colors are not status colors

Pressure/deviation maps have their own legend and units. The same red/green vocabulary is not reused ambiguously for process status.

## VR-09 — High density through hierarchy

Use compact toolbars, grouped inspector sections, aligned quantity rows, disclosure panels and split views. Do not achieve density by making text/targets illegibly small.

## VR-10 — High-consequence actions are visually distinct

```text
Apply
Commit revision
Generate manufacturing artifact
Release manufacturing package
Accept physical part
```

must not look interchangeable.

---

# 3. Human-factors constraints

Visual design adopts `HF-VIS-001..010` from the evidence baseline.

Key implementation consequences:

- color is not the sole status cue;
- focus/selection/active tool/active side are visibly distinct;
- drag-based edits have numeric or equivalent non-drag paths where meaningful;
- critical action result is followed by explicit feedback;
- high-risk release/acceptance transitions receive stronger confirmation;
- asynchronous computation states expose `calculating`, `stale`, `ready`, `failed` rather than silently leaving the last image visible as if current.

This is design evidence, not an IEC/FDA/WCAG conformity claim.

---

# 4. Information architecture

Primary product areas:

```text
CASE
  Overview
  Sources
  Registration
  Outcomes

DESIGN
  Base
  Parametric
  Corrections
  Sculpt
  Materials
  Inspect

BIOMECHANICS
  BiomechE
  Compare

PRODUCTION
  DFM
  Manufacturing
  QC / Physical Part

HISTORY
  Revisions
  Reports
  Provenance
```

The navigation may collapse by workflow stage but must preserve direct expert access.

---

# 5. Canonical workstation anatomy

Desktop reference viewport: **1440×960** for mockup v1. This is a visual design fixture, not a minimum supported display.

```text
┌──────────────────────────────────────────────────────────────┐
│ A. Global Context Bar                                       │
├──────┬─────────────────────────────────────┬─────────────────┤
│ B.   │                                     │ D. Inspector    │
│ Nav  │ C. Main 3D / primary work surface   │ / Properties    │
│ Rail │                                     │                 │
│      │                                     │                 │
├──────┴─────────────────────────────────────┴─────────────────┤
│ E. Context strip / measurements / timeline / results        │
└──────────────────────────────────────────────────────────────┘
```

### A — Global Context Bar

Always capable of showing:

```text
BiomechE-CAD
case / patient short identity
LEFT / RIGHT
active profile
working vs committed state
revision short ID
source/quality blocker count
save/recovery state
primary contextual action
```

### B — Navigation Rail

Compact icon + text labels. Current section clearly marked. Can collapse but labels remain available through tooltip/expanded mode.

### C — Main Work Surface

Usually 3D viewport; may become compare, table, report or workflow canvas on non-authoring screens.

### D — Inspector

Semantic properties, numeric inputs, source/preset/evidence context, warnings and requested/realized values.

### E — Context Strip

Screen-dependent:

```text
operation timeline
section plots
BiomechE metrics
comparison table
manufacturing checks
physical-part QC
```

May expand into a bottom panel.

---

# 6. Layout density

Reference desktop dimensions:

```text
Global Context Bar     56–64 px visual target
Nav Rail               64 px collapsed / ~188–220 expanded
Inspector               ~320–360 px
Bottom context strip   ~180–260 px expanded
```

These are visual-reference dimensions, not hard product constraints.

The central viewport should remain dominant at typical workstation widths.

---

# 7. Typography

Preferred style:

```text
neutral modern grotesk / UI sans
open counters
good small-size legibility
tabular numerals available
clear distinction 0/O and 1/l/I
```

Reference scale:

```text
Page/workspace title    18–20
Section title           14–16
Body                    13–14
Dense labels            12–13
Metadata/provenance     11–12
Critical numeric value  14–18 with tabular numerals
```

Avoid oversized headings that consume CAD workspace.

Quantity fields align decimal/numeric values and keep units visible.

---

# 8. Canonical color direction

## Light

```text
Canvas/background       #F3F6F7
Primary surface         #FFFFFF
Secondary surface       #F8FAFA
Raised/selected         #EDF5F4
Border                  #D7E1E3
Strong text             #172429
Body text               #314047
Muted text              #6E7D84
Primary teal            #167C7D
Primary hover           #11696A
Soft teal               #DCEFED
Secondary blue          #3C7895
Sage accent             #6F927B
Warm accent             #B9785B
```

## Dark

```text
Canvas/background       #0F171A
Primary surface         #162126
Secondary surface       #1B282D
Raised/selected         #203437
Border                  #2E4147
Strong text             #F0F5F5
Body text               #CFDADC
Muted text              #91A1A6
Primary teal            #55B8B2
Secondary blue          #79B2CE
Sage accent             #95B49C
Warm accent             #D49A7D
```

No dominant purple. If violet ever appears in quantitative data, it is part of a labeled data palette, not the brand/status accent.

---

# 9. Status palette

Reference only; every state has icon + label.

```text
VALID / READY          green-teal family + check icon + text
INFO                   blue family + info icon + text
WARNING                amber family + triangle icon + text
BLOCKING / ERROR       red family + octagon/error icon + text
UNRESOLVED             neutral/amber dashed treatment + ? icon + text
SUGGESTED              blue dashed/pill + sparkle/suggestion icon + text
CONFIRMED              solid neutral/teal + confirmation icon + text
PREVIEW                blue/teal outline + PREVIEW text
COMMITTED              solid revision badge + lock/check semantics
RELEASED               distinct production badge + release icon
STALE                   muted warning treatment + refresh icon + text
```

Status palettes must be checked for contrast in implementation.

---

# 10. Quantitative palettes

Pressure, deviation and other scalar maps use separate perceptually ordered palettes with:

```text
visible legend
units
min/max or threshold markers where defined
missing/unavailable treatment
source/metric/ROI label
```

Do not encode `good/bad` merely by green/red unless the owning interpretation rule explicitly defines it and the UI also states the rule textually.

---

# 11. Core component vocabulary

## `ContextChip`

Compact case/side/profile/revision state.

## `StatusBadge`

Icon + text + color/border.

## `QuantityField`

```text
label | numeric value | unit | optional slider/stepper
```

Supports direct numeric input and visible constraints/source.

## `RequestedRealizedRow`

Paired requested/realized values + delta/reason.

## `SemanticToolCard`

Named operation with short clinical/engineering meaning, icon and state.

## `SourceCard`

Source type, side, original/derived badge, quality state, short hash/ID, capture context drill-down.

## `ProvenancePill`

Compact exact version/profile/preset/algorithm indicator opening detail drawer.

## `EvidenceLink`

Opens evidence/profile source; does not imply recommendation strength by icon alone.

## `LayerRow`

Visibility/isolation/lock + semantic type + source/revision state.

## `MetricTile`

Metric + value + unit + ROI + source/quality. Tiles are dense and comparable, not marketing KPI cards.

## `ComparisonRow`

Baseline / outcome / absolute delta / relative delta / compatibility state.

## `CheckRow`

DFM/QC requirement + result + method + authority + blocker state.

## `RevisionNode`

Immutable revision timeline node with author/time/source summary.

## `ActionBar`

Routine actions left/neutral, primary reversible action emphasized, high-consequence release/accept actions separated and labelled.

---

# 12. 3D viewport grammar

Viewport overlays may include:

```text
orientation triad
LEFT/RIGHT anatomical side flag
scale/units
view preset control
visibility/layer control
active tool state
selection label
cursor/brush size preview
measurement labels
quantitative overlay legend
preview/stale/calculating badge
```

Avoid permanent clutter with all provenance hashes or all landmarks when irrelevant.

Selection outline/halo must be distinguishable from quantitative heatmap colors.

---

# 13. Side/laterality presentation

Persistent side indicator uses:

```text
LEFT  /  RIGHT
```

as text, optionally with a small anatomical-foot glyph.

Do not rely on red/blue conventions alone.

When mirroring:

```text
Source: RIGHT revision R12
Target: LEFT working copy
Semantic remap: medial↔medial, lateral↔lateral
```

is previewable before commit.

---

# 14. Working / preview / commit presentation

Canonical visual hierarchy:

### Working / Preview

```text
PREVIEW badge
editable parameters
Cancel / Apply
optional stale/calculating state
```

### Working applied

```text
Working changes • not committed
Undo / Redo
Commit revision
```

### Committed

```text
Revision Rxx • Committed
immutable badge
Create successor / Compare / Manufacture
```

Manufacturing release is a separate step and should not reuse the same primary button label/color.

---

# 15. Warning / blocking language

Messages have:

```text
severity
short title
affected object
why it matters
recommended resolution/action
provenance/details link
```

Example form:

```text
[BLOCKING] Side unresolved
This scan cannot be committed into a side-specific design until laterality is confirmed.
[Review source] [Confirm side…]
```

No generic `Something went wrong` for actionable domain states.

---

# 16. Empty / loading / stale states

## Empty

Explain the next domain action, e.g. `Import a foot scan or choose a reference template` rather than displaying a blank viewport.

## Loading/calculating

Show which result is computing and retain an explicit stale-state marker if the prior visualization remains visible.

## Failure

Keep the last valid state identifiable and do not present failed/incomplete computation as current.

---

# 17. Light / dark policy

Both themes preserve:

```text
same information hierarchy
same semantic icons
same status labels
same component geometry
comparable contrast
```

Dark mode is not achieved by simple inversion; quantitative maps/3D material shading require theme-specific validation.

The visual golden baseline v1 uses **light mode as primary** and includes a dark-mode reference for representative authoring/quantitative screens.

---

# 18. Responsive / compact policy

Reference compact viewport for M14: **1024×768** or tablet-class landscape.

Strategy:

```text
nav collapses to icon rail
details inspector becomes drawer/tab
bottom analysis panel becomes switchable sheet
context bar retains case + side + state
critical warning/blocking remains accessible
3D remains interactive
high-consequence actions never disappear into ambiguous overflow
```

Phone portrait is not assumed to support full authoring parity. Review/approval/read-only subsets may be defined later.

---

# 19. Screen briefs M01..M14

## M01 — Project / Patient / Case

**Goal:** choose/resume correct case and understand state before geometry work.

Primary regions:

```text
recent/open cases
case summary
LEFT/RIGHT design cards
active profiles
latest revision / manufacturing / outcome state
source completeness
```

Must surface: wrong-case prevention, side, current revision, unresolved inputs.

---

## M02 — Import / Scan Qualification

**Goal:** make original source and unresolved capture/geometry state obvious.

Primary layout:

```text
left: sources list
center: 3D/2D source preview
right: Source inspector
bottom: quality + processing lineage
```

Show:

```text
ORIGINAL / PROCESSED / REGISTERED badges
units
side + provenance
capture condition
scanner/device
mesh quality warnings
processing operations
```

---

## M03 — Registration / Landmarks

**Goal:** review landmarks and source→anatomical registration.

Primary layout:

```text
center 3D scan + landmarks
right landmark table / registration properties
bottom residual/quality summary
```

Suggested landmarks visually differ from confirmed ones.

---

## M04 — Base Orthosis / Template

**Goal:** choose versioned semantic base/template and establish initial fit/size.

Show:

```text
template gallery/list
version/source
compatibility
nominal dimensions
side policy
preview orthosis over scan
size/length/width controls
```

No control-cage topology shown in normal mode.

---

## M05 — Parametric Authoring

**Goal:** efficient arch/heel/wedge/outline authoring.

Center 3D model; left tool family; right semantic inspector.

Inspector example groups:

```text
Medial Arch
  Placement/reference
  Height
  Start / Center / End
  Shape
  Requested / Realized
  Preset/source
```

Bottom strip: operation stack + key measurements.

---

## M06 — Corrective / Offloading Elements

**Goal:** place named element with anatomical/evidence context.

Show:

```text
element library by semantic family
target ROI/anatomy
landmark-relative placement
requested dose
mechanical profile
source preset/evidence
before/after outcome hook if available
```

Target + safety-ring regions can be overlaid.

---

## M07 — Sculpt / Local Editing

**Goal:** freeform refinement while preserving replayability.

Show:

```text
raise/lower/smooth
radius
strength/dose
direction/reference
protected regions
stroke/history state
```

Viewport has visible brush footprint and preview badge.

---

## M08 — Materials / Mechanical Prescription

**Goal:** assign material/mechanical state without confusing it with geometry.

Layout:

```text
center 3D material-region overlay
right material definition + property source
bottom layer stack / interfaces
```

Visually differentiate:

```text
NOMINAL
MEASURED
CALIBRATED EFFECTIVE
MODELLED
SERVICE-MEASURED
```

---

## M09 — Inspection / Geometry QC

**Goal:** reproduce/inspect geometric realization.

Show:

```text
section view
length/width/height/angle/thickness measurements
requested/realized comparisons
inspection definition reference
quality/DFM checks
```

Measurement labels contain units and reference context.

---

## M10 — BiomechE Before / After / Delta

**Goal:** quantitative comparison without hiding protocol compatibility.

Layout:

```text
three coordinated maps: BASELINE / OUTCOME / DELTA
metric/ROI selector
comparison table
protocol compatibility
quality warnings
target + safety-ring + remote region metrics
```

Heatmaps have explicit legend/units and numeric drill-down.

---

## M11 — DFM / Manufacturing Preparation

**Goal:** understand if a committed design is ready to produce and under which profile.

Show:

```text
ManufacturingProfile + revision
production geometry preview
orientation/units
materials/lots requirements
DFM check list
required QC plan
artifact/package state
Generate artifact
Release manufacturing package [separate]
```

Blocking states are prominent and specific.

---

## M12 — Revision / Provenance / Report

**Goal:** make immutable history/source chain legible.

Layout:

```text
revision timeline/graph
selected revision summary
source/operation/preset/workflow lineage
report artifacts
exact versions/hashes in expandable detail
```

`Working` and `Committed` states visibly differ.

---

## M13 — Physical-Part QC / Outcome Follow-up

**Goal:** link actual produced part to design/run/QC/service/outcome.

Show:

```text
PhysicalOrthosis ID
DesignRevision
ManufacturingArtifact/Run
material lots
QC result
physical scan/deviation
issued/in-service state
PROM/comfort/adherence/outcome timeline
```

A second copy from the same design appears as a distinct physical-part record.

---

## M14 — Responsive / Compact Reference

**Goal:** prove critical state survives a constrained layout.

Use representative authoring screen with:

```text
collapsed nav
3D viewport
persistent case + LEFT/RIGHT + Working/Preview state
inspector drawer
bottom metrics sheet
visible warning
```

Do not claim mobile feature parity.

---

# 20. Screen-state variants required across the set

The M01..M14 package collectively must include examples of:

```text
EMPTY
NORMAL
SELECTED
PREVIEW
CALCULATING
STALE
WARNING
BLOCKING
UNRESOLVED
SUGGESTED
CONFIRMED
COMMITTED
RELEASED
NOT_COMPARABLE
```

Not every screen needs every state.

---

# 21. Mockup asset structure

```text
docs/ux/mockups/v1/
  README.md
  manifest.md
  biomeche-cad-mockups-v1.html
  assets/
    (optional local vector/raster assets)
  rendered/
    M01_...png
    ...
    M14_...png
```

`biomeche-cad-mockups-v1.html` is the preferred editable/source-controlled visual artifact for v1.

Rendered references are generated from that source when rendering tooling is available and recorded in the manifest.

---

# 22. Visual acceptance namespace

Define `VIS-*` for the visual package:

```text
VIS-001 persistent case + side context
VIS-002 working/preview/committed/released states distinguishable
VIS-003 warning/blocking/unresolved redundant cues
VIS-004 requested/realized presentation where applicable
VIS-005 numeric values show units and readable alignment
VIS-006 direct manipulation has visible numeric/semantic counterpart
VIS-007 provenance available by progressive disclosure
VIS-008 quantitative map has legend/units/source context
VIS-009 heatmap status does not replace numeric authority
VIS-010 semantic selection distinct from quantitative overlay
VIS-011 high-consequence actions visually separated
VIS-012 suggested vs confirmed visually distinct
VIS-013 original/processed/registered source visually distinct
VIS-014 material property source visually distinguishable
VIS-015 physical part distinct from design/artifact/run
VIS-016 focus/selection/active tool/side states do not collapse
VIS-017 light/dark preserve hierarchy/state meaning
VIS-018 compact layout preserves critical case/side/warning/provenance
VIS-019 M01..M14 each maps to owning requirements
VIS-020 mockup source/version/viewport/theme/status recorded
```

---

# 23. VIS-01 verdict

```text
VISUAL PRINCIPLES                DEFINED
INFORMATION ARCHITECTURE         DEFINED
WORKSPACE ANATOMY                DEFINED
COMPONENT VOCABULARY             DEFINED
LIGHT/DARK DIRECTION             DEFINED
STATE LANGUAGE                   DEFINED
RESPONSIVE POLICY                DEFINED
HUMAN-FACTORS CONSTRAINTS        MAPPED
M01..M14 BRIEFS                  DEFINED
VIS ACCEPTANCE IDS               VIS-001..020
ACTUAL MOCKUP ASSETS             NEXT — VIS-02
```

No geometry engine, clinical default, manufacturing tolerance or regulatory classification was introduced by this visual reference.
