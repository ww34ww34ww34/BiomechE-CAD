# BiomechE-CAD

Clinical CAD for custom foot orthoses/insoles, designed to integrate with the BiomechE biomechanics ecosystem.

The project starts from a detailed functional reconstruction of EasyCAD2 and expands it toward a versioned, auditable, non-destructive and scientifically traceable CAD architecture.

## Documentation source of truth

Markdown under `docs/` is the canonical documentation source.

**If you are resuming this project after an interruption, start with:**

- [RESUME HERE](docs/RESUME_HERE.md) — current state, sources, decisions, DONE/TODO, audit status and exact restart point.

Then use:

- [Specification index](docs/SPEC_INDEX.md)
- [Consolidated functional specification](docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md)
- [Architectural decisions](docs/DECISIONS.md)
- [Research source inventory](docs/research/SOURCES.md)

## Current baseline

The initial baseline is strongly inspired by EasyCAD2 and consolidates:

- EasyCAD2 manual 1.1.x.x;
- EasyCAD2 validation plan 1.4.x.x;
- EasyCAD2 validation report 1.4.x.x;
- prior EasyCAD/easyCAD2 market research;
- initial scientific literature on foot orthoses, plantar-pressure offloading, 3D scanning, posting and stiffness;
- architectural conventions inherited from the BiomechE documentation workflow.

## Architectural direction

```text
Patient / Case
    -> OrthosisProject [DX/SX]
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

The geometry history should remain non-destructive and versioned whenever technically reasonable. Clinical evidence, prescription parameters, geometry operations and manufacturing results must remain distinguishable.

## Documentation maintenance rule

Research evidence must not be silently rewritten when engineering decisions evolve. If older documentation appears obsolete or redundant enough to delete or materially compact, preserve the historical evidence or explicitly review it before removal.

`docs/RESUME_HERE.md` must be updated after every substantial research/specification session so another conversation can resume the project without reconstructing context from scratch.
