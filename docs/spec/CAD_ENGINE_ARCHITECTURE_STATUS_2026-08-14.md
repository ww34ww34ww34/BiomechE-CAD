# BiomechE-CAD — CAD Engine Architecture Status Addendum

**Date:** 2026-08-14  
**Status:** CURRENT OVERRIDE FOR ARCHITECTURE SELECTION

This addendum does **not** replace the functional capability requirements in `CAD_ENGINE_CAPABILITY_SPEC.md`. It overrides only the earlier implication that OpenSubdiv is already the expected/favored P0 dependency.

## Current state

Architecture selection is parked while the project completes the functional/scientific evidence baseline.

The product-level geometry contract remains approximately:

```text
patient-specific editable orthosis representation
+ stable semantic feature identity
+ smooth clinical surface
+ numerical prescription operations
+ anatomical placement/reference
+ scan/pressure registration and queries
+ local editing/sculpt
+ material/stiffness semantics
+ production body + QC/DFM
+ deterministic/versioned history
```

No current functional requirement chooses a specific geometry library.

## Deferred foundation shoot-out

When architecture work resumes, compare at least:

```text
A) Product-owned clinical/domain layer + OpenSubdiv
B) Product-owned clinical/domain layer + openNURBS / ON_SubD
```

Use the same orthosis fixtures and public/stable APIs only.

Required comparison includes:

- cage creation/editing;
- stable vertex/edge/face identity;
- boundary behavior;
- crease/semi-sharp behavior;
- extraordinary vertices;
- arbitrary limit-surface position/normal/derivatives required by product queries;
- deterministic tessellation;
- repeated-edit performance;
- native and Emscripten/WASM feasibility;
- memory and binary footprint.

P0 should not maintain both SubD representations in synchronization unless a future product requirement proves this necessary.

## Current active work

See:

- `docs/research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md`
- `docs/research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md`
- `docs/DECISIONS.md` (`D-CAD-015` onward)

The kernel shoot-out resumes only after functional evidence defines a sufficiently stable set of acceptance fixtures.
