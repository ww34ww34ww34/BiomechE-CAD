# BiomechE-CAD — Specification Index

**Status:** CANONICAL DOCUMENT MAP  
**Updated:** 2026-08-17  
**Immediate continuation:** **Visual Direction V2 — Surface-CAD Workstation / V2-S01 review.**  
**Architecture phase:** **Q0 Geometry Engine Qualification — harness/pins ready, execution parked during visual refinement.**  
**Selection:** **NO WINNER**.

---

## 1. Resume order

### Current visual continuation

1. `RESUME_HERE.md`
2. `ux/BIOMECHE_CAD_VISUAL_DIRECTION_V2_SURFACE_CAD_2026-08-17.md`
3. `ux/mockups/v2/README.md`
4. `DECISIONS_2026-08-17_VISUAL_V2_ADDENDUM.md`
5. `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
6. `TRACEABILITY_MATRIX.md` — **v0.10**
7. `NEXT_CHAT_PROMPT.md`

### Architecture/Q0 continuation

8. `DECISIONS.md`
9. `DECISIONS_2026-08-16_CLOSURE_Q0_ADDENDUM.md`
10. `spec/01_coordinate_registration.md`
11. `spec/02_project_schema.md`
12. `spec/16_geometry_authoring_contract.md`
13. `spec/17_workflow_preset_macro.md`
14. `spec/18_numerical_qualification_registry.md`
15. `validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`
16. `research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md`
17. `validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`
18. `research/architecture/GEOMETRY_ENGINE_Q0_EVIDENCE_UPDATE_2026-08-16.md`
19. `../qualification/geometry-engine/q0/README.md`
20. `../qualification/geometry-engine/q0/candidate-lock.json`
21. `../qualification/geometry-engine/q0/results/Q0_EVIDENCE_STATUS_2026-08-16.md`
22. `../qualification/geometry-engine/q0/results/Q0_HARNESS_VALIDATION_2026-08-16.md`
23. `BIBLIOGRAPHY.md`

---

## 2. Frozen/canonical product package

```text
BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md                  CANONICAL v2
01_coordinate_registration.md                      FROZEN v1
02_project_schema.md                                CANONICAL ACTIVE v0.1
06_corrective_elements.md                           FROZEN v1
08_material_stiffness.md                            FROZEN v1
09_analysis_qc_dfm.md                               FROZEN v1
10_manufacturing.md                                 FROZEN v1
11_biomeche_integration.md                          FROZEN v1
12_reporting_traceability.md                        FROZEN v1
13_use_case_profiles.md                             FROZEN v1
14_prom_comfort_adherence.md                        FROZEN v1
15_pressure_acquisition_qualification.md            FROZEN methodology v1
16_geometry_authoring_contract.md                   FROZEN v1
17_workflow_preset_macro.md                         FROZEN v1
18_numerical_qualification_registry.md              FROZEN v1
19_project_schema_v0_2_changeset.md                 APPROVED / NOT MATERIALIZED
20_input_scan_reference_data.md                     FROZEN v1
21_product_workflow_interaction.md                  FROZEN v1
22_interchange_manufacturing_handoff.md             FROZEN v1
23_realtime_performance_contract.md                 FROZEN doctrine v1 / budgets OPEN
validation/24_validation_verification_master_plan.md CANONICAL v1
25_intended_use_risk_privacy_security_boundary.md   CANONICAL boundary v1 / classification OPEN
```

Written P0 closure: **GO / 0 blockers**.

---

## 3. Historical / engineering-only documents

```text
03_geometry_operation_model.md                 HISTORICAL
04_base_template.md                            ENGINEERING CANDIDATE / QUALIFICATION FIXTURE
05_parametric_orthosis_geometry.md             PROVISIONAL ENGINEERING MATHEMATICAL REFERENCE
CAD_ENGINE_CAPABILITY_SPEC.md                  HISTORICAL
CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md   HISTORICAL
BIOMECHE_CAD_FUNCTIONAL_SPEC.md                HISTORICAL
```

They cannot override the frozen product contracts.

---

## 4. Visual-reference packages

### V1 — functional/state/traceability baseline

```text
ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
ux/mockups/v1/README.md
ux/mockups/v1/manifest.md
ux/mockups/v1/biomeche-cad-mockups-v1.html
ux/VISUAL_REFERENCE_CROSS_DOCUMENT_AUDIT_2026-08-16.md
ux/VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md
ux/mockups/v1/rendered/README.md
ux/mockups/v1/rendered/render_reference.py
```

Status:

```text
VIS-01                    DONE
VIS-02                    DONE
VIS-03 source             DONE
VIS-04 source             DONE
VIS-03R-RUN               DONE — 14/14 captures executed
VIS-04R                   DONE — PASS WITH corrective items
VIS-03R-REPRODUCIBILITY   DONE — versioned Chromium/Playwright renderer + SHA-256 manifest generation
PNG MATERIALIZATION       OPTIONAL derived cache
```

V1 remains useful evidence but **is not the preferred current aesthetic**.

### V2 — active Surface-CAD workstation direction

```text
ux/BIOMECHE_CAD_VISUAL_DIRECTION_V2_SURFACE_CAD_2026-08-17.md
ux/mockups/v2/README.md
DECISIONS_2026-08-17_VISUAL_V2_ADDENDUM.md
```

Status:

```text
V2 doctrine              CAPTURED / ACTIVE
V2-S01 Template/Modello  REVIEW — generated candidate, not approved
V2-S02                    NOT GENERATED
V2-S03                    NOT GENERATED
V2-S04                    NOT GENERATED
V2-S05                    NOT GENERATED
```

V2 aesthetic doctrine:

```text
high-level industrial surface CAD
geometry-first workstation
dark graphite neutral chrome
compact contextual controls
Scene/Layers + properties
restrained blue active state
amber/orange selected geometry
no decorative Jarvis/neon HUD
```

Generate and approve one full-screen workspace at a time.

Visual corrective items from V1 still apply: `VIS-A11Y-01..03` in `TRACEABILITY_MATRIX.md`.

---

## 5. Bibliography

`BIBLIOGRAPHY.md` is the single canonical bibliography and was normalized on 2026-08-16 with stable IDs for current AM/interchange, MDR/MDCG/GDPR, ISO risk/QMS and HFE/accessibility sources.

Research supplements remain intake/audit ledgers only.

---

## 6. Q0 geometry-engine qualification — READY / PARKED

Canonical plan/scorecard:

```text
research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
research/architecture/GEOMETRY_ENGINE_Q0_EVIDENCE_UPDATE_2026-08-16.md
```

Executable harness:

```text
qualification/geometry-engine/q0/README.md
qualification/geometry-engine/q0/candidate-lock.json
qualification/geometry-engine/q0/CMakeLists.txt
qualification/geometry-engine/q0/include/biomeche_q0/adapter.hpp
qualification/geometry-engine/q0/src/main.cpp
qualification/geometry-engine/q0/src/candidate_opensubdiv.cpp
qualification/geometry-engine/q0/src/candidate_opennurbs.cpp
qualification/geometry-engine/q0/cmake/CandidateOpenSubdiv.cmake
qualification/geometry-engine/q0/cmake/CandidateOpenNurbs.cmake
qualification/geometry-engine/q0/run_q0.py
qualification/geometry-engine/q0/results/Q0_EVIDENCE_STATUS_2026-08-16.md
qualification/geometry-engine/q0/results/Q0_HARNESS_VALIDATION_2026-08-16.md
```

Candidate locks:

```text
OpenSubdiv v3_7_0 @ 9dab8a47bfbb1388ec8388fe61f5f916e6123f38
openNURBS 8.x   @ 00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
```

Harness status:

```text
product-owned C++20 adapter boundary      READY
common headless smoke executable          READY
candidate source adapters                 READY
native/WASM evidence runner               READY
runner/common/source-shape validation     PASS
```

Actual candidate build cells remain **NOT EXECUTED** until run against the pinned source trees/toolchains.

No winner is selected.

---

## 7. Current exact next task

### Immediate visual task

Refine **V2-S01 Template / Modello** only using the Surface-CAD direction. Obtain explicit approval before moving to V2-S02.

### Architecture task after visual checkpoint

Execute Q0 native + direct Emscripten/WASM runs for both exact pinned candidates using `qualification/geometry-engine/q0/run_q0.py`. Commit generated JSON evidence before promoting any hard gate. If Q0 qualifies both/sufficient candidates, proceed to Q1 common geometry/replay/query fixture.

---

## 8. Deferred/non-blocking

```text
Project Schema v0.2 materialization    DEFERRED until explicit task
TD-CI-001                              DEFERRED / NON-BLOCKING
physical pressure qualification       FUTURE evidence stream
material/manufacturing qualification  FUTURE evidence stream
formal regulatory/QMS deployment      FUTURE assessment
materialized V1 visual PNG copies     OPTIONAL review cache
```
