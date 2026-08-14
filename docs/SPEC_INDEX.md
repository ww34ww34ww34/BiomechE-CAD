# BiomechE-CAD Specification Index

Markdown in this repository is the canonical specification source.

## Start / resume here

- [RESUME_HERE.md](RESUME_HERE.md) — current state, source hierarchy, audit status, DONE/TODO and exact restart point.
- [Architectural decisions](DECISIONS.md) — current baseline decisions and their status.
- [Research sources](research/SOURCES.md) — primary EasyCAD2 documents, market sources and scientific baseline.
- [EasyCAD2 primary reference pack](references/easycad2/README.md) — manual, validation plan and validation report with versions, source links, page map and evidence role.

## Current canonical specifications

| File | Status | Purpose |
|---|---|---|
| [BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | **Baseline / consolidated 2026-08-14** | Unified EasyCAD2-inspired product/clinical functional specification |
| [CAD_ENGINE_CAPABILITY_SPEC.md](spec/CAD_ENGINE_CAPABILITY_SPEC.md) | **v2 / current baseline** | OpenSubdiv-first orthosis CAD capability contract; general NURBS/B-Rep removed from P0 |
| [03_geometry_operation_model.md](spec/03_geometry_operation_model.md) | **Design baseline** | Canonical quad-dominant orthosis cage, stable IDs, intrinsic anatomical coordinates, mask/field engine, operation stack, OpenSubdiv adapter and production handoff |
| [05_parametric_orthosis_geometry.md](spec/05_parametric_orthosis_geometry.md) | **Math v0 / provisional** | Reference formulas and invariants for arch, wedge, heel/wrap/camber, elements, sculpt, scan conform, thickness and DFM fix |

## Common specifications still to freeze

| File | Status | Purpose |
|---|---|---|
| `spec/01_coordinate_registration.md` | **NEXT** | Coordinate spaces, units, LEFT/RIGHT semantics, pressure/scan/image/template registration and transforms |
| `spec/02_project_schema.md` | Planned | Versioned project schema, IDs, assets, operation history, migrations, hashes and persistence |
| `spec/04_base_template.md` | **NEXT after 01/02** | Concrete canonical cage topology, DIMA outline, L/W, template families, morphing and custom presets |
| `spec/06_corrective_elements.md` | Planned | Element library, placement, transforms, field/cage integration, custom elements and clinical semantics |
| `spec/07_sculpt_and_roi_deformation.md` | Planned | Sculpt, smoothing, ROI, falloff and deformation toward acquisition data |
| `spec/08_material_stiffness.md` | Planned | MaterialModifier, stiffness/density maps, transitions, physical properties and multi-material direction |
| `spec/09_analysis_qc_dfm.md` | Planned | Sections, heights, angles, thickness and manufacturing constraints |
| `spec/10_manufacturing.md` | Planned | Bridge/Straight/Oblique/Hybrid closure, STL/3MF/package export, manufacturing profiles and CAM boundary |
| `spec/11_biomeche_integration.md` | Planned | BiomechE pressure/result bridge, canonical units, provenance, ROI and pre/post outcome workflow |
| `spec/12_reporting_traceability.md` | Planned | Project/clinical/manufacturing reports, JSON/PDF and audit traceability |

## Validation specifications

| File | Status | Purpose |
|---|---|---|
| [easycad2_geometry_parity.md](validation/easycad2_geometry_parity.md) | **Baseline coverage gate** | Maps all 25 EasyCAD2 1.4 validation stories to the OpenSubdiv/control-cage architecture and identifies remaining algorithm gates |
| `validation_strategy.md` | Planned | Overall validation hierarchy |
| `geometry_invariants.md` | Planned | Numerical invariants for cage/limit/manufacturing geometry |
| `golden_geometry.md` | Planned | Golden fixture format and regression policy |
| `manufacturing_validation.md` | Planned | Watertightness, min thickness, orientation and production artifact validation |

The EasyCAD2 validation plan is the behavioral baseline. BiomechE-CAD must add quantitative geometry invariants and golden-geometry tests.

## Current geometry hypothesis

```text
Canonical Orthosis Cage
+ stable vertex IDs / intrinsic anatomical coordinates
+ OpenSubdiv limit-surface evaluator
+ versioned clinical deformation operations
+ mask/field composition
+ scan/query layer
+ orthosis-specific production-body generator
```

General-purpose NURBS/B-Rep, STEP/IGES, loft/sweep, arbitrary shell/offset and solid booleans are **not P0**. They remain adapter/future capabilities and must be justified by a concrete failing acceptance fixture.

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

Competitors should be audited against the same capability taxonomy so newly discovered features can be added without losing comparability.

## Documentation rules

1. Source evidence remains separate from engineering decisions.
2. New verified scientific/vendor claims must be added to a source ledger or dated research note.
3. User-provided implementation facts must be labeled separately when they are not present in public/primary documents.
4. Every P0 feature must become testable through acceptance criteria and/or invariants.
5. A library is added only to solve a named requirement/fixture; libraries must not redefine the product requirements retroactively.
6. Superseded architecture remains available through Git history and source evidence is not silently discarded.
7. Update `RESUME_HERE.md` after substantial work.
8. For third-party manuals/PDFs, keep exact source links, versions, page locators and evidence role in `docs/references/`. Binary copies should only be committed when repository rights/distribution policy explicitly allows it.
