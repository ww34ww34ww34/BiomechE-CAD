# BiomechE-CAD — Product Workflow & Interaction Contract

**Version:** v1  
**Status:** **FROZEN v1**  
**Date:** 2026-08-16  
**Architecture/UI toolkit:** unspecified.  
**Purpose:** define end-to-end product state and interaction semantics without prescribing a specific desktop/web framework or final visual style.  
**Visual authority:** future `docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md` and versioned mockups may refine layout/interaction presentation but may not override semantic rules in this document.

---

## 0. Core interaction doctrine

BiomechE-CAD is a clinical/domain vertical CAD, not a generic mesh editor. Every interactive edit must preserve the distinction among:

```text
SOURCE EVIDENCE
SEMANTIC PRESCRIPTION
PREVIEWED REALIZATION
COMMITTED DESIGN REVISION
MANUFACTURING ARTIFACT
PHYSICAL ORTHOSIS
MEASURED OUTCOME
```

Frozen interaction rules:

```text
preview != commit
suggestion != confirmation
selection != semantic ownership
visual position != stored anatomical placement
undo/redo != mutation of committed history
warning != blocking error
hidden layer != deleted data
rendered color != quantitative authority
```

---

# 1. Canonical end-to-end workflow

```text
Patient / Case
  ↓
Acquire / Import
  ↓
Qualify input
  ↓
Register / landmarks
  ↓
Choose base/template
  ↓
Generate initial orthosis
  ↓
Parametric edits
  ↓
Corrective / offloading elements
  ↓
Free sculpt / local edits
  ↓
Material / mechanical prescription
  ↓
Inspect / measure
  ↓
BiomechE outcome comparison
  ↓
QC / DFM
  ↓
Manufacturing preparation
  ↓
Commit immutable DesignRevision
  ↓
Release manufacturing package
  ↓
Manufacture / inspect physical part
  ↓
Issue / service / outcome follow-up
```

The UI may allow non-linear navigation, but stage prerequisites and unresolved states remain explicit.

---

# 2. Workspace state model

A project workspace should expose at least:

```text
ProjectState
  currentCase
  activeSide
  activeDesignWorkingState
  lastCommittedDesignRevision

  visibleSources[]
  selectedSource?
  activeRegistration?
  activeLandmarkSet?
  activeROISet?

  activePrescriptionOperation?
  activeTool?
  selectionSet[]

  activeProfile(s)
  activeWorkflowApplication?
  activeMaterialPrescription?

  warnings[]
  blockers[]
  unresolvedItems[]

  dirtyState
  previewState
```

Transient UI state is not automatically persisted as clinical/product state.

---

# 3. Patient / case entry

The product should begin from a project/case context rather than an anonymous geometry scene.

Minimum visible context:

```text
case/project identity
patient/pseudonymous identity according to policy
side
active indication/use-case profile(s)
latest committed design revision
source-data status
manufacturing/outcome status when applicable
```

A geometry file may be opened for inspection/import, but creation of a clinically traceable design requires explicit case/side context before commitment.

---

# 4. Acquire / import interaction

Input workflow follows `20_input_scan_reference_data.md`.

The user must be able to distinguish:

```text
original source
processed source
registered source
reference-only geometry
physical-part scan
quantitative pressure/BiomechE data
```

Import UI should surface unresolved conditions such as:

```text
unknown units
unknown side
ambiguous orientation
missing capture metadata
unsupported file extensions/features
integrity failure
```

No import wizard silently guesses these states into validity.

---

# 5. Qualify input

Before authoring, the product may execute or display quality checks. Interaction state:

```text
VALID_FOR_DECLARED_USE
VALID_WITH_WARNINGS
UNRESOLVED
NOT_USABLE_FOR_DECLARED_USE
CORRUPT_OR_INTEGRITY_FAILURE
```

Warnings are actionable and traceable. The workflow/profile determines which states may proceed to which downstream actions.

A user override, where allowed, must record who/when/why and does not erase the original warning.

---

# 6. Registration and landmarks

The registration workspace must make visible:

```text
source side/frame
canonical target frame
landmarks + method/review state
registration method/version
residual/quality measurements
manual adjustments
review/confirmation state
```

Suggested automatic landmarks or alignment are visually distinguishable from reviewed/confirmed state.

Direct manipulation of a landmark updates its numeric/reference representation coherently; a numeric edit updates the viewport coherently.

---

# 7. Side context

LEFT/RIGHT must remain visible during authoring whenever ambiguity is possible.

Required behavior:

- current side is visible in primary workspace chrome or an equivalent persistent context area;
- side changes are explicit, not inferred from camera orientation;
- mirrored operations show semantic remapping before commit where clinically meaningful;
- a camera orbit/flip never changes anatomical side;
- a source with unknown/unconfirmed side cannot silently inherit the currently displayed side.

---

# 8. Base/template selection

A base/template is a versioned reusable definition, not a loose mesh preset.

The selection interaction should display as applicable:

```text
template identity/version
source/provenance
compatibility state
nominal size/dimensions
side policy
profile/workflow relevance
preview result
```

Applying a template creates/updates the working authoring state; it does not commit a new immutable DesignRevision until explicit commit.

Any geometry representation used to realize the template remains implementation infrastructure.

---

# 9. Authoring operation lifecycle

Every interactive semantic operation follows:

```text
SELECT / INVOKE
  ↓
EDIT PARAMETERS / DIRECT MANIPULATION
  ↓
PREVIEW
  ↓
INSPECT REQUESTED + REALIZED STATE
  ↓
APPLY TO WORKING STATE | CANCEL
  ↓
(optional further edits)
  ↓
COMMIT DESIGN REVISION
```

An operation may support continuous realtime preview, but preview is derived/transient and may be recomputed.

A parameter field must expose units. A direct handle and numeric field represent the same semantic parameter rather than separate hidden states.

---

# 10. Preview / apply / cancel / commit

## Preview

- non-authoritative derived geometry;
- may use lower rendering/tessellation quality;
- may be cancelled without history mutation;
- must not silently overwrite committed revision.

## Apply

- records semantic operation into the current working state;
- remains editable/undoable according to working-history policy;
- does not imply manufacturing release.

## Cancel

- restores prior working state for the active un-applied tool operation;
- cannot delete already committed historical evidence.

## Commit

Creates a new immutable `DesignRevision` snapshot/event lineage with exact source, operation, workflow/preset, algorithm/version and relevant profile provenance.

---

# 11. Undo / redo vs immutable history

Working-session undo/redo operates over uncommitted authoring state or creates a new inverse/replayable state according to implementation.

Once a DesignRevision is committed:

```text
undo historical revision
```

must mean creating or selecting another/new revision state, never rewriting the committed record in place.

The UI should visually distinguish:

```text
working history
committed revision history
manufacturing/release history
```

---

# 12. Parametric authoring

For arch, heel, wedge/post, size/outline and similar operations, interaction should expose:

```text
semantic operation name
anatomical/typed placement reference
requested parameters + units
realized/inspectable measurements where available
constraints/warnings
source preset/workflow if applicable
```

Implementation-specific control vertices or topology should remain hidden from normal clinical authoring unless an advanced engineering/debug mode is explicitly entered.

---

# 13. Corrective/offloading elements

Corrective element interaction follows `06_corrective_elements.md`.

Required visible semantics:

```text
element family
intended effect
target anatomy/ROI
placement reference
requested geometric dose
mechanical profile when assigned
realized geometry inspection
source preset/evidence context
```

Drag placement must update the same typed placement object used by numeric editing and reporting.

---

# 14. Sculpt / local editing

Freeform sculpt is allowed only as replayable semantic authoring state under `GAUTH`.

UI should expose:

```text
tool mode (raise/lower/smooth/etc.)
brush/reference radius + units
strength/dose + units/meaning
affected semantic region where available
protected/locked regions
stroke/application history
```

A sculpt result cannot collapse into an anonymous baked mesh with lost provenance.

---

# 15. Material / mechanical prescription

Material workspace must keep geometry and material dose separable.

Required interaction:

```text
select semantic material region/layer
assign exact MaterialDefinition revision
assign lot where production policy requires
assign nominal/effective property profile
show property source (nominal/measured/calibrated/modelled)
show stack order/interfaces
```

Changing material cannot silently change geometry unless an explicit coupled workflow says so and records both operations.

---

# 16. Visibility, isolation and selection

Objects/layers may be:

```text
VISIBLE
HIDDEN
ISOLATED
GHOSTED / REFERENCE
LOCKED
```

Visibility state does not change source validity, semantic existence or report lineage.

Selection should identify semantic objects when possible:

```text
source scan
landmark
ROI
orthosis surface
corrective element
material region
inspection definition
manufacturing artifact
physical-part measurement
```

Raw triangles/vertices may be available in advanced/debug contexts but are not the primary semantic selection model.

---

# 17. Linked 2D / 3D / quantitative views

Where multiple views exist, they should share semantic selection/reference state.

Examples:

```text
3D orthosis selection ↔ section view
ROI selection ↔ pressure map ↔ numeric metrics
landmark selection ↔ registration table
material region ↔ layer/stack inspector
inspection dimension ↔ numeric QC result
```

Linked views may have independent camera/zoom, but not independent contradictory domain state.

---

# 18. Inspection / measurement workflow

Every measurement is a reproducible inspection definition plus a result.

User interaction must distinguish:

```text
measurement definition
reference entities/landmarks/frame
method/version
current result
comparison target/limit if any
authority of target/limit
```

Dragging a measurement annotation is presentation-only unless the user explicitly edits the measurement definition.

---

# 19. BiomechE comparison workspace

BiomechE quantitative results remain authoritative according to `11_biomeche_integration.md`.

The CAD UI should support:

```text
BASELINE
OUTCOME
DELTA
```

with visible:

```text
metric definition
ROI/version
source protocol/device
compatibility/quality state
target + safety-ring/adjacent/remote regions where relevant
```

Heatmaps are views; numeric values/provenance remain accessible.

---

# 20. Warnings vs blockers

Canonical severity behavior:

```text
INFO
WARNING
BLOCKING
```

An interaction may also expose `UNRESOLVED` source/semantic state.

### INFO
Does not prevent progress; explanatory/provenance content.

### WARNING
Allows progress where policy permits, but remains visible/auditable.

### BLOCKING
Prevents the guarded transition until resolved or an explicitly authorized deviation policy is executed.

No color alone should be the only carrier of severity.

---

# 21. Workflow / preset invocation

A reusable workflow/preset may populate or propose operations, but the UI must preserve:

```text
source definition id/version/hash
inputs/defaults/overrides
expanded operations
compatibility warnings
suggested vs confirmed state
human confirmation when required
```

`one-click` workflow does not mean hidden semantics.

---

# 22. Save / autosave / recovery

The product may autosave working state, but autosave is not equivalent to committing a DesignRevision.

Suggested distinction:

```text
WORKING DRAFT SAVED
COMMITTED DESIGN REVISION
RELEASED FOR MANUFACTURING
```

Crash/session recovery should restore the latest recoverable working state without rewriting immutable committed revisions.

---

# 23. Manufacturing preparation and release

Before release, the UI should surface as applicable:

```text
committed design revision
manufacturing profile/revision
production geometry status
material/lot requirements
orientation/coordinate state
DFM checks
required QC plan
artifact/package hashes
warnings/blockers
```

`Generate` and `Release for manufacturing` are distinct actions where the product supports a release gate.

---

# 24. Physical-part QC and outcome follow-up

A physical orthosis workspace should resolve exact:

```text
physicalPartId
designRevision
manufacturingArtifact
manufacturingRun
material lots
QC status
service state
patient-experience/outcome data
```

A new physical copy of the same design is not the same physical entity.

---

# 25. Accessibility / high-density workstation principles

Without freezing a visual style, the interaction design should support:

- keyboard-accessible primary commands where feasible;
- visible focus state;
- text/icon labels or tooltips for non-obvious controls;
- no semantic status conveyed only by color;
- scalable text and high-DPI rendering;
- dense clinical workstation workflows without requiring mobile-style excessive paging;
- mouse/trackpad as primary desktop input, with touch support where the eventual platform supports it;
- confirmation dialogs reserved for genuinely destructive/release/high-risk transitions rather than routine edits.

Exact WCAG/desktop accessibility conformance target belongs to implementation/product release requirements and may be defined later.

---

# 26. Responsive / compact behavior

A compact/tablet/mobile view may support review, selection and limited edits, but capability parity is not assumed.

The UI must make unavailable capabilities explicit rather than hiding required state. Critical review/provenance/side information must remain accessible in compact layouts.

The visual reference package will define at least one compact canonical screen.

---

# 27. P0 acceptance tests

```text
UX-001 project/case/side context persists through authoring
UX-002 unknown-side source does not silently inherit active side
UX-003 import unresolved units/side/frame remains visibly unresolved
UX-004 automatic landmark suggestion visually differs from confirmed landmark
UX-005 direct manipulation and numeric field update one semantic parameter
UX-006 preview can be cancelled without changing committed revision
UX-007 apply changes working state but not immutable committed history
UX-008 commit creates new immutable DesignRevision
UX-009 undo/redo cannot rewrite a committed revision in place
UX-010 hidden/isolate does not delete semantic objects or provenance
UX-011 semantic mirror preserves side-aware meaning and presents remapped state
UX-012 corrective element drag retains typed anatomical placement
UX-013 sculpt stroke remains replayable/versioned
UX-014 material change does not silently alter geometry
UX-015 measurement annotation move does not alter definition unless explicitly editing it
UX-016 pressure heatmap selection resolves numeric metric/ROI/provenance
UX-017 warning and blocking states have distinct behavior and non-color cue
UX-018 suggested profile/preset/workflow != confirmed application
UX-019 generated manufacturing artifact != released manufacturing package
UX-020 physical-part QC resolves exact design/run/artifact identity
UX-021 autosave/recovery != DesignRevision commit
UX-022 compact view preserves critical side/warning/provenance access
```

---

# 28. Visual-reference requirements

The future canonical mockups SHALL cover at least:

```text
M01 Project / Patient / Case
M02 Import / Scan qualification
M03 Registration / Landmarks
M04 Base orthosis / Template
M05 Parametric authoring
M06 Corrective / Offloading elements
M07 Sculpt / Local editing
M08 Materials / mechanical prescription
M09 Inspection / Geometry QC
M10 BiomechE Before / After / Delta
M11 DFM / Manufacturing preparation
M12 Revision / Provenance / Report
M13 Physical-part QC / Outcome follow-up
M14 Responsive / compact view
```

Each screen must map back to relevant `UX-*` and product requirement IDs.

---

# 29. Frozen invariants

```text
preview != commit
working save != committed revision
commit != manufacturing release
suggestion != confirmation
camera orientation != anatomical side
hidden != deleted
render color != numeric authority
direct manipulation != untracked free geometry mutation
warning != blocker
physical copy != design revision
```

---

# 30. Product conclusion

A user should be able to move rapidly through the CAD while the system continuously answers:

```text
What am I editing?
Which side/case/source is authoritative?
Is this preview or committed state?
What semantic prescription does this control represent?
What value was requested and what was realized?
What is unresolved/warning/blocking?
Which evidence/profile/preset produced this state?
Which revision/artifact/physical part will this action affect?
```

This interaction contract is frozen independently of the final UI framework and geometry engine.
