# BiomechE-CAD

Clinical CAD for custom foot orthoses/insoles, designed to integrate with the BiomechE biomechanics ecosystem.

BiomechE-CAD starts from a detailed EasyCAD2 behavioral baseline, but its target is broader: a versioned, auditable, non-destructive, scientifically traceable orthotic CAD with explicit acquisition, prescription, design, manufacturing, physical-part and outcome lineage.

## Start / resume here

Markdown under `docs/` is the canonical documentation source.

**If you are resuming this project after an interruption, always start with:**

- [RESUME HERE](docs/RESUME_HERE.md) — current mission, frozen decisions, DONE/TODO and exact restart point.

Current active visual checkpoint:

- [Visual Direction V2 — Surface-CAD Workstation](docs/ux/BIOMECHE_CAD_VISUAL_DIRECTION_V2_SURFACE_CAD_2026-08-17.md)
- [V2 mockup workspace / screen register](docs/ux/mockups/v2/README.md)
- [Visual V2 decision addendum](docs/DECISIONS_2026-08-17_VISUAL_V2_ADDENDUM.md)

Canonical product/architecture navigation:

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

## Current project state

```text
P0 written product documentation       COMPLETE / GO / 0 blockers
canonical bibliography                 NORMALIZED
V1 visual functional baseline          COMPLETE / browser-audited / reproducible
V2 visual aesthetic direction          ACTIVE / Surface-CAD workstation
V2-S01 Template / Modello              REVIEW — not yet approved
V2-S02..S05                            NOT GENERATED
Q0 geometry qualification harness      READY / parked during current visual refinement
geometry engine selection              OPEN / NO WINNER
Project Schema v0.2                    APPROVED / NOT MATERIALIZED
TD-CI-001                              DEFERRED / NON-BLOCKING
```

## Current visual direction

The preferred V2 look is a **high-level industrial surface-modeling CAD workstation**, not a medical dashboard and not a decorative sci-fi/Jarvis HUD.

Core traits:

```text
dominant geometry viewport
dark graphite neutral chrome
compact professional CAD tools
contextual properties
Scene/Layers hierarchy
surface curves/control points/section views when useful
restrained blue active states
amber/orange selected geometry
rich neutral clay/graphite orthosis rendering
minimal decorative glow
```

Visual work is produced and approved **one full-screen workspace at a time**:

```text
V2-S01 Template / Modello
V2-S02 Superficie / Edit Parametrico
V2-S03 Elementi
V2-S04 Scultura / Post Processing
V2-S05 Analisi / Produzione
```

The immediate restart point is V2-S01 review/refinement. Do not move to S02 before explicit approval.

## Product direction

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

Geometry-engine qualification is prepared but no engine has been selected.

Pinned Q0 candidates:

```text
OpenSubdiv v3_7_0 @ 9dab8a47bfbb1388ec8388fe61f5f916e6123f38
openNURBS 8.x   @ 00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
```

The executable Q0 harness is under `qualification/geometry-engine/q0/`.

Actual native/server/WASM candidate builds are still **NOT EXECUTED**. When visual work is paused/completed, continue Q0 from the existing harness; do not restart generic library research.

OpenSubdiv, openNURBS/ON_SubD, Manifold, OCCT or other geometry libraries must be judged against the frozen product/authoring contracts rather than driving those contracts.

## Documentation maintenance rule

Research evidence must not be silently rewritten when engineering or visual decisions evolve. Preserve historical baselines, make supersession explicit, and update at least:

```text
docs/RESUME_HERE.md
docs/SPEC_INDEX.md
docs/TRACEABILITY_MATRIX.md
docs/NEXT_CHAT_PROMPT.md
```

after substantial phase transitions.
