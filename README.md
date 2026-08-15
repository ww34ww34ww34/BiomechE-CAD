# BiomechE-CAD

Clinical CAD for custom foot orthoses/insoles, designed to integrate with the BiomechE biomechanics ecosystem.

BiomechE-CAD starts from a detailed EasyCAD2 behavioral baseline, but its target is broader: a versioned, auditable, non-destructive, scientifically traceable orthotic CAD with explicit acquisition, prescription, design, manufacturing, physical-part and outcome lineage.

## Documentation source of truth

Markdown under `docs/` is the canonical documentation source.

**If you are resuming this project after an interruption, start with:**

- [RESUME HERE](docs/RESUME_HERE.md) — current mission, frozen decisions, DONE/TODO and exact restart point.

Then use:

- [Specification index](docs/SPEC_INDEX.md)
- [Canonical Functional Specification v2](docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md)
- [Requirement Traceability Matrix](docs/TRACEABILITY_MATRIX.md)
- [Geometry Authoring Contract](docs/spec/16_geometry_authoring_contract.md)
- [Workflow / Preset / Macro Contract](docs/spec/17_workflow_preset_macro.md)
- [Numerical / Tolerance / Qualification Registry](docs/spec/18_numerical_qualification_registry.md)
- [Architectural decisions](docs/DECISIONS.md)
- [Technical debt register](docs/TECHNICAL_DEBT.md)
- [Canonical bibliography](docs/BIBLIOGRAPHY.md)

`docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is the preserved historical/audit baseline; it is **not** the current functional authority.

## Current product direction

```text
Patient / Case
    -> Acquisition + provenance
    -> Registration + landmarks
    -> OrthosisProject [LEFT / RIGHT]
    -> BaseTemplate
    -> Versioned semantic authoring operations
    -> Corrective / offload features
    -> Material / mechanical prescription
    -> Inspection + analysis + DFM/QC
    -> ManufacturingProfile
    -> ManufacturingArtifact
    -> PhysicalOrthosis
    -> Measured outcome / follow-up
    -> Reproducible report
```

The design history is semantic and versioned. Dose, placement, units, anatomical reference, source acquisition, algorithm version and material/mechanical intent must survive into committed revisions.

## Architecture status

The geometry-engine shoot-out is intentionally parked.

OpenSubdiv, openNURBS/ON_SubD, Manifold, OCCT or other geometry libraries must be judged against the frozen product/authoring contracts rather than driving those contracts.

## Current documentation priority

```text
traceability                         baseline DONE
geometry authoring semantics         canonical draft / freeze next
workflow/preset/macro semantics      canonical draft / freeze next
numerical/tolerance governance       canonical draft / freeze next
representative geometry acceptance   next
real device/process qualification    parallel
geometry-engine selection            later
```

GitHub Actions / fixture-validation reliability is currently an explicitly deferred technical debt item (`TD-CI-001`). It does not block documentation progress and current CI status must not be used as proof that `main` is fully qualified.

## Documentation maintenance rule

Research evidence must not be silently rewritten when engineering decisions evolve. Preserve historical baselines, make supersession explicit, and update `docs/RESUME_HERE.md`, `docs/SPEC_INDEX.md` and `docs/TRACEABILITY_MATRIX.md` after substantial specification work.
