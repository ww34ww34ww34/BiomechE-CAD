# BiomechE-CAD — P0 Authoring Acceptance Catalog

**Status:** CANONICAL TEST-SPEC BASELINE v0.1  
**Date:** 2026-08-15  
**Execution:** specification-only while `TD-CI-001` is deferred  
**Architecture:** geometry-kernel independent  
**Owners:** `spec/16_geometry_authoring_contract.md`, `spec/17_workflow_preset_macro.md`, `spec/18_numerical_qualification_registry.md`

---

## 0. Purpose

This catalog translates the new P0 authoring contracts into representative, executable-later scenarios **without choosing a geometry kernel**.

Synthetic values used in these scenarios exist only to make semantics testable. They are not clinical recommendations.

A future implementation may express these as JSON fixtures, unit tests, property tests or golden-geometry tests. The invariant is the behavior, not the test framework.

---

# 1. Test conventions

Use canonical frame semantics from `01_coordinate_registration.md`.

```text
RIGHT medial = +Y
LEFT  medial = -Y
intrinsic q > 0 = medial on both sides
```

Synthetic fixture quantities may use:

```text
mm
deg
normalized [0,1]
```

where explicitly identified.

Every scenario records:

```text
CASE ID
contract IDs
preconditions
input semantic state
action
expected persisted state
expected invariants
non-goals
```

---

# 2. Geometry authoring scenarios

## AUTH-C01 — Arch dose + placement survives commit

**Covers:** `GAUTH-001`, `GAUTH-004`, `GAUTH-015`, `GAUTH-016`, `GAUTH-020`, `GAUTH-036`.

Precondition:

- RIGHT orthosis project;
- registered scan exists;
- medial-arch landmarks/region are resolvable.

Synthetic authoring intent:

```text
operationType = MEDIAL_ARCH
placement = LANDMARK_RELATIVE_MM
peakHeight = 7.0 mm
start/peak/end refs explicitly named
transition = named/versioned
```

Expected:

1. committed operation retains type, side, placement mode/reference, dose/unit, transition and algorithm version;
2. final geometry cache may change format without losing those semantics;
3. replay from the exact revision inputs reproduces equivalent geometry within the future registered replay tolerance.

Non-goal: 7.0 mm is not a recommended clinical value.

---

## AUTH-C02 — Heel features remain semantically distinct

**Covers:** `GAUTH-021`.

Create separate operations for:

```text
HEEL_CUP
HEEL_RELIEF
HEEL_CAMBER
MEDIAL_HEEL_SKIVE
HEEL_MECHANICAL_REGION
```

Expected:

- operations remain distinguishable in persistence/history/reporting;
- disabling one does not implicitly disable another;
- implementation may share a primitive internally but may not serialize all five as one anonymous deformation.

---

## AUTH-C03 — Rearfoot wedge direction survives LEFT/RIGHT semantics

**Covers:** `GAUTH-022`, `GAUTH-028`, `GAUTH-029`.

Create a RIGHT rearfoot wedge with:

```text
angle = synthetic 4 deg
anatomical direction = MEDIAL_POSTING
pivot/reference explicitly named
```

Mirror to LEFT.

Expected:

- LEFT owns a new operation identity;
- anatomical intent remains `MEDIAL_POSTING`;
- global-axis sign transforms according to coordinate rules;
- mirror is not implemented as raw X/Y sign change without semantic transform.

---

## AUTH-C04 — Metatarsal placement reference modes remain non-equivalent

**Covers:** `GAUTH-010..014`, `NREG-006`, `NREG-013`.

Create two synthetic metatarsal-pad placements:

```text
A: LANDMARK_LINE_RELATIVE_MM, -8.0 mm from MTH line
B: NORMALIZED_FOOT_LENGTH, 0.76 using named normalization definition
```

Expected:

- A and B retain different placement modes and reference definitions;
- the system does not convert them into one unlabeled scalar;
- neither becomes a universal product default merely because literature contains similar study values.

---

## AUTH-C05 — Pressure-target offload preserves source semantics

**Covers:** `GAUTH-014`, `GAUTH-024`.

Precondition:

- pressure acquisition with exact protocol/device/calibration provenance;
- versioned target ROI;
- valid registration to CAD frame.

Create offload feature:

```text
placement = PRESSURE_TARGET_RELATIVE
targetROI = ROI-T
safetyRingROI = ROI-S
remoteComparisonROIs = [ROI-R1, ROI-R2]
geometry dose = synthetic
mechanical dose ref = optional named profile
```

Expected:

- source acquisition, ROI versions, registration and selection algorithm survive;
- heatmap pixels alone are insufficient provenance;
- measured outcome remains separate from design intent.

---

## AUTH-C06 — Sculpt replay is not a baked anonymous mesh

**Covers:** `GAUTH-025`, `GAUTH-036`, `GAUTH-038`.

Apply a synthetic sculpt stroke sequence or consolidated sparse displacement layer.

Expected committed state includes enough data to reproduce the edit:

```text
tool/mode
radius/influence
strength convention
direction mode
stroke/displacement representation
algorithm version
```

A project that retains only the resulting vertices fails unless authority mode is explicitly `IMPORTED_LEGACY_GEOMETRY`.

---

## AUTH-C07 — Scan conform records acquisition + registration

**Covers:** `GAUTH-007`, `GAUTH-026`.

Apply `SCAN_CONFORM` using a specific ScanAcquisition and Registration.

Expected:

- source scan and registration identities retained;
- weight-bearing condition remains the value captured on the acquisition, including `UNKNOWN` if unknown;
- projection method, ROI, strength/blend and algorithm version persisted;
- no later re-registration silently changes historical evaluation meaning.

---

## AUTH-C08 — Requested dose vs constrained realized dose

**Covers:** `GAUTH-018`, `GAUTH-027`, `NREG-017`.

Synthetic operation requests geometry that violates a manufacturing-profile constraint.

Expected persisted result distinguishes:

```text
requestedDose
realizedDose
constraintRuleRef
warning/failure state
```

The evaluator must not silently clamp and report the clamped value as if it were the original prescription.

---

# 3. Acquisition / landmark scenarios

## AUTH-C09 — Weight-bearing UNKNOWN remains UNKNOWN

**Covers:** `GAUTH-007`, `NREG-002` by analogy to unknown numeric state.

Import scan with no authoritative weight-bearing metadata.

Expected:

```text
weightBearingCondition = UNKNOWN
```

not `FULL_WEIGHT_BEARING` or another guessed convenience default.

---

## AUTH-C10 — Landmark provenance survives manual review

**Covers:** `GAUTH-008`, `GAUTH-009`.

Create algorithm-derived landmark, then user reviews/accepts it.

Expected historical semantics preserve:

```text
sourceMethod = ALGORITHM_DERIVED
algorithmRef = exact version
original quality/confidence if available
reviewState = REVIEWED_ACCEPTED
reviewing user/time
```

Review does not rewrite source method to `MANUAL_ON_SCAN`.

---

# 4. Inspection scenarios

## AUTH-C11 — Section is reproducible

**Covers:** `GAUTH-030`.

Define section plane from exact DesignRevision and frame.

Expected:

- plane definition, revision ID, representation/method and unit retained;
- reopening the same historical measurement does not silently use current revision geometry.

---

## AUTH-C12 — Distance definition is explicit

**Covers:** `GAUTH-031`.

Store two measurements with same numeric value but different definitions:

```text
POINT_TO_POINT
POINT_TO_PLANE_HEIGHT
```

Expected: they remain semantically different despite equal displayed values.

---

## AUTH-C13 — Thickness method is explicit

**Covers:** `GAUTH-032`, `NREG-020`.

Compare:

```text
NORMAL_RAY_THICKNESS
SHORTEST_SURFACE_DISTANCE
```

Expected: method identity is persisted; no automatic equivalence claim.

---

## AUTH-C14 — CAD vs measured-part deviation map

**Covers:** `GAUTH-033`, `NREG-021..025`.

Inputs:

```text
CAD nominal DesignRevision
measured physical-part scan
registration
named distance algorithm
```

Expected:

- identities/registration/method/map asset/summary retained;
- result does not automatically PASS/FAIL without a qualified ManufacturingProfile rule;
- unknown required uncertainty cannot be assumed zero.

---

# 5. Workflow / macro scenarios

## AUTH-C15 — Workflow expansion freezes exact version

**Covers:** `WFLOW-004..006`, `WFLOW-023..025`.

Apply `WorkflowDefinition W@1.2.0`, commit revision, then publish `W@1.3.0`.

Expected:

- old revision retains `W@1.2.0 + hash/snapshot`;
- expanded child operations remain inspectable;
- old revision does not resolve to 1.3.0;
- rerunning 1.3.0 creates a new application/revision identity.

---

## AUTH-C16 — Override is explicit

**Covers:** `WFLOW-008..010`, `NREG-026..027`.

Workflow resolves a synthetic default from registry rule; operator changes it before commit.

Expected:

```text
source rule/version
resolved default
final overridden value
author/time
```

all remain reconstructable.

The registry definition itself remains immutable.

---

## AUTH-C17 — Suggestion is not confirmation

**Covers:** `WFLOW-015..017`.

Future recommendation module suggests a workflow/profile.

Expected:

```text
SUGGESTED_NOT_CONFIRMED
```

until explicit user confirmation. The design cannot be reported as user-confirmed merely because a model suggested it.

---

## AUTH-C18 — Mirror policy blocks unsafe macro

**Covers:** `WFLOW-018..020`, `GAUTH-029`.

A workflow contains one mandatory step marked `NOT_MIRRORABLE`.

Expected:

- workflow cannot be `MIRROR_SAFE_AUTOMATIC`;
- automatic bilateral application is rejected or requires an explicitly reviewed alternative path.

---

# 6. Numerical registry scenarios

## AUTH-C19 — OPEN manufacturing tolerance stays OPEN

**Covers:** `NREG-002`, `NREG-009`, `NREG-021`.

ManufacturingProfile lacks a qualified dimensional acceptance rule.

Expected:

- deviation can be measured;
- no hidden `±1 mm`, `±2 mm` or other product constant appears;
- acceptance state is `NOT_QUALIFIED`/equivalent rather than guessed PASS.

---

## AUTH-C20 — UI default cannot satisfy a qualification limit

**Covers:** `NREG-004`, `NREG-008..012`.

Synthetic configuration contains:

```text
UI_CONVENIENCE_DEFAULT = 2.0 mm
required MANUFACTURING_ACCEPTANCE_LIMIT = OPEN
```

Expected: resolver refuses to use 2.0 mm as the manufacturing acceptance limit.

---

## AUTH-C21 — Evidence rule is profile-scoped

**Covers:** `NREG-006`, `NREG-010`, `NREG-013..016`.

Attach a diabetic-neuropathy metatarsal-pad evidence rule to a different unrelated use-case profile.

Expected:

- non-transfer guard prevents silent activation;
- evidence remains queryable but not active as a compatible rule.

---

## AUTH-C22 — Replay epsilon != part tolerance

**Covers:** `NREG-007`, `NREG-018`, `NREG-021`.

Define:

```text
algorithm replay equivalence epsilon
manufacturing dimensional acceptance tolerance
```

Expected: two distinct rule IDs/classes; changing one cannot change the other.

---

# 7. Minimum future geometry golden cases

When a geometry engine exists, add deterministic geometry fixtures for the semantic cases above.

At minimum each operation family should test:

```text
no-op / zero dose
positive representative dose
boundary/transition behavior
LEFT/RIGHT mirror
composition with adjacent operation
invalid/unresolved reference
requested-vs-realized constraint state
replay after serialization
```

The numerical values used for golden tests are engineering fixture values, not clinical defaults unless explicitly linked to a qualified registry rule.

---

# 8. Exit criteria for this catalog

This catalog is sufficient to unblock architecture evaluation when:

1. every major P0 geometry family has at least one representative semantic scenario;
2. mirror and provenance cases are present;
3. inspection semantics are testable;
4. workflow expansion/override behavior is testable;
5. `OPEN` numerical behavior is testable;
6. the cases can be implemented against competing geometry engines without changing their product meaning.

`TD-CI-001` affects where/how these are executed later, not the acceptance definitions themselves.
