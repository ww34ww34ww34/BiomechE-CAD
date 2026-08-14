# BiomechE-CAD Specification Index

Markdown in this repository is the canonical specification source.

## Start / resume here

- [RESUME_HERE.md](RESUME_HERE.md) — current state, source hierarchy, audit status, DONE/TODO and exact restart point.
- [Architectural decisions](DECISIONS.md) — current baseline decisions and their status.
- [Research sources](research/SOURCES.md) — primary EasyCAD2 documents, market sources and scientific baseline.

## Current canonical functional specification

| File | Status | Purpose |
|---|---|---|
| [BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | **Baseline / consolidated 2026-08-14** | Unified EasyCAD2-inspired functional specification, P0/P1/P2, scientific rationale, validation approach and loss-audit against the previous research |

## Planned common specifications

| File | Status | Purpose |
|---|---|---|
| `spec/01_coordinate_registration.md` | **NEXT** | CAD coordinate spaces, units, LEFT/RIGHT semantics, pressure/scan/image/template registration and transforms |
| `spec/02_project_schema.md` | Planned | Versioned project schema, IDs, assets, operation history, migrations, hashes and persistence |
| `spec/03_geometry_operation_model.md` | Planned | Non-destructive operation stack, dependency/evaluation semantics, undo/redo and determinism |
| `spec/04_base_template.md` | Planned | DIMA representation, outline constraints, L/W, template morphing and custom presets |
| `spec/05_parametric_orthosis_geometry.md` | Planned | Heel/wrap/camber, medial/lateral arch and wedge mathematical operators |
| `spec/06_corrective_elements.md` | Planned | Element library, placement, transforms, booleans, custom elements and clinical semantics |
| `spec/07_sculpt_and_roi_deformation.md` | Planned | Sculpt, smoothing, freehand/circle ROI, falloff and deformation toward acquisition data |
| `spec/08_material_stiffness.md` | Planned | MaterialModifier, stiffness/density maps, transitions, physical properties and multi-material direction |
| `spec/09_analysis_qc_dfm.md` | Planned | Sections, heights, angles, thickness, manifold/self-intersection checks and manufacturing constraints |
| `spec/10_manufacturing.md` | Planned | Closure profiles, STL/3MF/package export, manufacturing profiles and CAM boundary |
| `spec/11_biomeche_integration.md` | Planned | BiomechE pressure/result bridge, canonical units, provenance, ROI and pre/post outcome workflow |
| `spec/12_reporting_traceability.md` | Planned | Project/clinical/manufacturing reports, JSON/PDF and audit traceability |

## Planned validation specifications

```text
docs/validation/
  validation_strategy.md
  geometry_invariants.md
  golden_geometry.md
  easycad2_parity_user_stories.md
  manufacturing_validation.md
```

The EasyCAD2 1.4 validation plan provides a useful behavioral baseline, but BiomechE-CAD must add quantitative geometry invariants and golden-geometry regression tests.

## Planned competitor research

```text
docs/research/competitors/
  easycad2.md
  parocontour_diers.md
  fitfoot360.md
  rodin4d_neo.md
  vorum_canfit.md
  ...
```

Competitors should be audited against the same capability taxonomy defined by the consolidated specification so newly discovered features can be added without losing comparability.

## Documentation rules

1. Source evidence remains separate from engineering decisions.
2. New verified scientific/vendor claims must be added to a source ledger or dated research note.
3. Every P0 feature must become testable through acceptance criteria and/or invariants.
4. When a modular spec supersedes part of the consolidated baseline, preserve the baseline as historical provenance until an explicit compaction review.
5. Update `RESUME_HERE.md` after substantial work.
6. Do not commit third-party manual screenshots/PDFs to this public repository without rights clearance; store citations, page locators and descriptions instead.
