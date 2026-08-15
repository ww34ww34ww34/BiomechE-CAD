# BiomechE-CAD — Project Schema v0.2 Change-Set Specification

**Status:** DESIGN CHANGE-SET / NOT YET MATERIALIZED  
**Date:** 2026-08-15  
**Parent schema:** `02_project_schema.md` / reference serialization `biomeche-cad-project-0.1`  
**Rule:** documentation first; do not modify schema JSON, fixtures or migrations until this change set is reviewed.

---

## 0. Purpose

The authoring-phase contracts introduced several semantic concepts that the current logical schema v0.1 only partially represents.

This document defines the intended **additive v0.2 schema evolution** without creating an implementation/CI dependency.

Primary drivers:

```text
Geometry Authoring Contract
Workflow / Preset / Macro Contract
Numerical / Qualification Registry
```

---

# 1. Compatibility doctrine

## SCHEMA02-001 — v0.2 should be additive where possible

Prefer additions over destructive field changes.

Existing v0.1 projects must remain importable through an explicit migration path.

## SCHEMA02-002 — missing new fields do not acquire guessed semantics

When importing v0.1:

```text
missing weight-bearing state -> UNKNOWN
missing landmark source detail -> legacy/unknown provenance state
missing workflow application -> operations remain valid standalone operations
missing numerical rule ref -> retain literal value and classify provenance as legacy/unclassified until reviewed
```

Migration must not fabricate clinical provenance.

## SCHEMA02-003 — v0.1 history remains historical truth

Migration may enrich representation, but must not claim that old projects contained information that was never recorded.

---

# 2. `ScanAcquisition` enrichment

Current v0.1 already contains optional `weightBearingCondition`.

v0.2 should formalize it and expand capture context:

```text
ScanAcquisition
  ...existing fields...

  captureContext
    weightBearingCondition
      NON_WEIGHT_BEARING
      PARTIAL_WEIGHT_BEARING
      FULL_WEIGHT_BEARING
      OTHER_NAMED
      UNKNOWN

    weightBearingDetail?
    posture?
    seatedStandingOther?
    supportCondition?
    captureMethod?
    protocolRef?
    notes?
```

### Rules

- `UNKNOWN` is explicit and valid.
- absence during migration maps to `UNKNOWN`, not a guessed state.
- free-text detail may supplement but not replace controlled state.

---

# 3. Landmark provenance enrichment

Replace/extend the current compact landmark entry:

```text
landmarkId
semanticType
point
confidence?
author/method
```

with an explicit provenance-capable structure:

```text
Landmark
  landmarkId
  semanticType
  point
  frameId
  side

  sourceAcquisitionRef?
  sourceMethod
    MANUAL_PALPATION_MARKER
    MANUAL_ON_SCAN
    DEVICE_PROVIDED
    ALGORITHM_DERIVED
    IMPORTED
    LEGACY_UNKNOWN
    OTHER_NAMED

  authorRef?
  algorithmRef?
  confidence?
  qualityFlags[]?

  reviewState
    UNREVIEWED
    REVIEWED_ACCEPTED
    REVIEWED_REJECTED
    LEGACY_UNKNOWN

  reviewedBy?
  reviewedAt?
  reviewNotes?
```

### Migration

If v0.1 has `author/method`, map truthfully where possible. Otherwise use `LEGACY_UNKNOWN` rather than inferring.

---

# 4. Workflow definitions

Extend:

```text
ProjectDefinitions
  ...
  presetDefinitions[]
```

with:

```text
workflowDefinitions[]
numericalRuleSnapshots[]?   // optional project-captured governed rules
```

## `WorkflowDefinition`

```text
WorkflowDefinition
  DefinitionHeader

  description?
  intendedContext?
  compatibilityRules
  inputs[]
  steps[]
  dependencies[]
  mirrorPolicy
```

Definitions remain immutable/versioned snapshots under the same exact-version/hash doctrine as templates and presets.

---

# 5. Workflow applications

Add root collection:

```text
workflowApplications[]
```

## `WorkflowApplication`

```text
WorkflowApplication
  applicationId
  workflowRef: VersionedRef

  orthosisProjectId
  designRevisionId?
  side

  appliedAt
  appliedBy

  inputBindings[]
  parameterOverrides[]
  expandedOperationIds[]

  compatibilityState
  reviewState
  warnings[]

  provenanceRecordId
```

The `designRevisionId` may be null during draft/preview application and becomes bound on committed historical state according to implementation lifecycle rules.

---

# 6. Operation links to workflow source

Extend `DesignOperation`:

```text
sourcePresetRef?
sourceWorkflowApplicationRef?
workflowStepId?
```

The operation remains independently meaningful after expansion.

This is critical: deleting/uninstalling a workflow library must not make historical operations uninterpretable.

---

# 7. Parameter overrides

Introduce:

```text
ParameterOverrideRecord
  overrideId
  workflowApplicationRef
  stepId
  parameterPath

  resolvedSource
    PRESET
    WORKFLOW_DEFAULT
    NUMERICAL_RULE
    PROFILE
    USER_INPUT
    OTHER

  sourceRuleRef?
  originalValue
  finalValue
  unit?

  overriddenBy
  overriddenAt
  rationale?
```

Rules:

- an override changes project/application state, not the source definition;
- before/after values remain historical evidence;
- unit compatibility must be validated.

---

# 8. Numerical rule references

Introduce a lightweight reference primitive:

```text
NumericalRuleRef
  ruleId
  version
  authorityClass
  contentHash?
  snapshotRef?
```

A project does not need to embed the complete global registry if it can resolve an immutable rule; committed revisions must still retain reproducible historical meaning.

Potential use sites:

```text
operation parameter default provenance
workflow default
manufacturing acceptance requirement
device qualification requirement
outcome interpretation rule
algorithm tolerance
```

Literal project values remain stored even when a rule ref explains where they came from.

---

# 9. Requested vs realized geometry state

For operations constrained by DFM/safety rules, add an optional evaluation record rather than rewriting requested parameters:

```text
OperationEvaluation
  evaluationId
  designRevisionId
  operationId

  requestedParametersSnapshot
  realizedParametersSnapshot?
  appliedConstraintRuleRefs[]

  state
    AS_REQUESTED
    CONSTRAINED
    REJECTED
    UNRESOLVED

  warnings[]
  algorithmRef
  createdAt
```

This may be stored under revision validation/evaluation results rather than inside the immutable operation itself; exact placement is an implementation-schema choice to finalize during v0.2 review.

---

# 10. Inspection measurements

Add a typed geometry-inspection result model, rather than storing only generic `designMetrics` scalars.

```text
GeometryInspection
  inspectionId
  designRevisionId
  side

  inspectionType
    SECTION
    DISTANCE
    HEIGHT
    ANGLE
    THICKNESS
    DEVIATION_MAP

  definition
  frameRef?
  sourceRefs[]
  value/series/mapRef
  units
  method
  algorithmRef
  uncertainty?
  qualityState
  createdAt
  provenanceRecordId
```

This supports reproducible measurements and avoids conflating display values with acceptance rules.

---

# 11. Manufacturing acceptance rule links

Extend relevant manufacturing/QC entities with explicit numerical rule refs where appropriate:

```text
QCRequirement
  ...
  acceptanceRuleRef?
  measurementMethodRef?
  uncertaintyPolicyRef?
```

The current literal-value representation may remain supported for compatibility.

No default global dimensional tolerance is introduced.

---

# 12. Acquisition compatibility semantics

Potential additive object:

```text
AcquisitionCompatibilityAssessment
  assessmentId
  acquisitionRefs[]
  intendedUse
  state
    COMPATIBLE
    COMPATIBLE_WITH_WARNINGS
    NOT_COMPARABLE
    INSUFFICIENT_DATA
  ruleRefs[]
  warnings[]
  algorithmRef?
  createdAt
```

This can generalize existing pressure/BiomechE compatibility gating to scan/capture contexts when needed, without forcing one universal comparison rule.

P0 implementation need should be reviewed before including it in the actual v0.2 JSON schema.

---

# 13. Root v0.2 conceptual additions

Proposed conceptual root additions:

```text
BiomechECADProject
  ...existing v0.1 collections...

  workflowApplications[]
  geometryInspections[]
  operationEvaluations[]?
  acquisitionCompatibilityAssessments[]?
```

Proposed `definitions` additions:

```text
workflowDefinitions[]
numericalRuleSnapshots[]?
```

---

# 14. Migration requirements

## SCHEMA02-004 — Deterministic migration

Migration from v0.1 to v0.2 SHALL be deterministic and versioned.

## SCHEMA02-005 — No provenance invention

Examples:

```text
missing scan weight-bearing -> UNKNOWN
old landmark method unavailable -> LEGACY_UNKNOWN
standalone operations -> no fabricated WorkflowApplication
literal parameter with no known rule -> no fabricated NumericalRuleRef
```

## SCHEMA02-006 — Preserve old hash/asset lineage

Migration creates migration provenance but does not rewrite raw asset bytes/hashes.

## SCHEMA02-007 — Historical design meaning must remain stable

A migrated v0.1 `DesignRevision` must represent the same authoring intent as before migration. New fields enrich known metadata or explicitly mark unknowns.

---

# 15. Deferred from v0.2 unless implementation proves need

Do not add merely for completeness:

```text
full cloud sync conflict model
multi-user CRDT state
general-purpose CAD feature tree
kernel-native topology objects
BRep/NURBS/SubD serialization
arbitrary workflow scripting language
automatic diagnosis/prescription objects
FE solver state
```

These remain separate future decisions.

---

# 16. Review checklist before materializing schema v0.2

1. Does each proposed field correspond to a frozen P0 requirement?
2. Can old v0.1 data map without invented provenance?
3. Are workflow definitions distinct from applications/expanded operations?
4. Are numerical rules references, not hidden code constants?
5. Can requested vs realized geometry be represented without mutating prescription intent?
6. Can geometry inspection results preserve method/revision/frame?
7. Are manufacturing tolerances still profile-owned?
8. Is any proposed object dependent on a specific geometry kernel? If yes, remove or redesign it.
9. Is the migration direction explicit before touching JSON Schema?

Only after this review should the reference serialization advance from `0.1` to `0.2`.
