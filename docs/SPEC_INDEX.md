# BiomechE-CAD — Specification Index

**Status:** CANONICAL DOCUMENT MAP  
**Updated:** 2026-08-15

Markdown under `docs/` is the canonical documentation source.

---

## 1. Resume order

Read in this order before substantial work:

1. [RESUME_HERE.md](RESUME_HERE.md) — current mission, state and exact restart point.
2. [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) — **canonical product scope**.
3. [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) — requirement → owner → acceptance → evidence → open state.
4. [spec/02_project_schema.md](spec/02_project_schema.md) — persisted semantic model.
5. [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) — frozen coordinate/laterality/registration semantics.
6. [spec/16_geometry_authoring_contract.md](spec/16_geometry_authoring_contract.md) — P0 geometry-authoring semantics, kernel independent.
7. [spec/17_workflow_preset_macro.md](spec/17_workflow_preset_macro.md) — P0 reusable workflow/preset/macro semantics.
8. [spec/18_numerical_qualification_registry.md](spec/18_numerical_qualification_registry.md) — numerical defaults/tolerances/qualification governance.
9. [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) — frozen BiomechE↔CAD quantitative contract.
10. [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) — frozen reporting/provenance contract.
11. [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) — frozen pressure-device qualification methodology.
12. [DECISIONS.md](DECISIONS.md) — cross-cutting decisions.
13. [TECHNICAL_DEBT.md](TECHNICAL_DEBT.md) — explicitly deferred engineering debt.
14. [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) — single authoritative bibliography.

`spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is historical/audit material and must not be mistaken for v2.

---

## 2. Current work order

```text
FUNCTIONALITY + EASYCAD2 + SCIENTIFIC EVIDENCE       DONE baseline
        ↓
FUNCTIONAL SPEC v2                                   CANONICAL
        ↓
PROJECT SCHEMA / PROVENANCE                          ACTIVE baseline
        ↓
COORDINATE / REGISTRATION                            FROZEN v1
        ↓
BIOMECHE INTEGRATION                                 FROZEN v1
        ↓
REPORTING / TRACEABILITY                             FROZEN v1
        ↓
PRESSURE ACQUISITION QUALIFICATION METHOD            FROZEN v1
        ↓
COMPETITOR + LITERATURE SECOND PASS                  DONE
        ↓
REQUIREMENT TRACEABILITY                             DONE v0.1
        ↓
GEOMETRY AUTHORING CONTRACT                          CANONICAL DRAFT / FREEZE NEXT
        ↓
WORKFLOW / PRESET / MACRO CONTRACT                   CANONICAL DRAFT / FREEZE NEXT
        ↓
NUMERICAL / TOLERANCE / QUALIFICATION REGISTRY      CANONICAL DRAFT / FREEZE NEXT
        ↓
P0 GEOMETRY ACCEPTANCE + REPRESENTATIVE FIXTURES     NEXT
        ↓
REAL DEVICE / MATERIAL / PROCESS QUALIFICATION       PARALLEL
        ↓
GEOMETRY ENGINE SHOOT-OUT                            LATER
```

GitHub CI is **not** a current documentation gate. See `TECHNICAL_DEBT.md`, `TD-CI-001`.

---

# 3. Canonical product specifications

| File | Status | Purpose |
|---|---|---|
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) | **CANONICAL v2** | Evidence-led P0/P1/P2 product scope |
| [spec/02_project_schema.md](spec/02_project_schema.md) | ACTIVE schema baseline v0 | Immutable revisions, definitions, acquisitions, outcomes, materials, manufacturing, provenance |
| [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) | **FROZEN v1** | CAD-ANAT-1, side, intrinsic coordinates, transforms, registration semantics |
| [spec/06_corrective_elements.md](spec/06_corrective_elements.md) | ACTIVE v0 | Corrective/offload taxonomy and semantics |
| [spec/08_material_stiffness.md](spec/08_material_stiffness.md) | ACTIVE v0 | Material identity, regions, effective/measured/service-aged mechanics |
| [spec/09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) | ACTIVE v0 | Quantitative analysis, QC and DFM semantics |
| [spec/10_manufacturing.md](spec/10_manufacturing.md) | ACTIVE v0 | Manufacturing profile/run/artifact/physical-part/QC lifecycle |
| [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) | **FROZEN v1** | KPI/result provenance, quality, comparison and reanalysis |
| [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) | **FROZEN v1** | Immutable report/source-manifest semantics |
| [spec/13_use_case_profiles.md](spec/13_use_case_profiles.md) | ACTIVE v0 | Evidence-context profiles and non-transfer rules |
| [spec/14_prom_comfort_adherence.md](spec/14_prom_comfort_adherence.md) | ACTIVE v0 | PROM/pain/function/comfort/fit/satisfaction/adherence separation |
| [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) | **FROZEN methodology v1** | Intended-use-specific device/protocol qualification |
| [spec/16_geometry_authoring_contract.md](spec/16_geometry_authoring_contract.md) | **CANONICAL DRAFT v0.1** | Typed authoring operations, dose, placement, capture/landmark provenance, mirror, inspection, production boundary |
| [spec/17_workflow_preset_macro.md](spec/17_workflow_preset_macro.md) | **CANONICAL DRAFT v0.1** | Versioned reusable preset/macro/workflow semantics and human authority |
| [spec/18_numerical_qualification_registry.md](spec/18_numerical_qualification_registry.md) | **CANONICAL DRAFT v0.1** | Numeric authority classes, OPEN values, tolerance and qualification ownership |

---

# 4. Traceability and governance

| File | Status | Purpose |
|---|---|---|
| [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) | **CANONICAL v0.1** | Product requirement family → canonical owner → acceptance → evidence → open gap |
| [DECISIONS.md](DECISIONS.md) | CANONICAL | Cross-cutting durable decisions |
| [TECHNICAL_DEBT.md](TECHNICAL_DEBT.md) | ACTIVE | Deferred engineering debt, including `TD-CI-001` |
| [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) | **CANONICAL** | Stable source IDs and source-role governance |

---

# 5. Acceptance families

Existing families:

```text
SCHEMA-001..030
OFF-001..009
CE-001..010
ARCH-001..014
HEEL-001..015
PROF-001..012
PROM-001..020
MAT-001..018
MAN-001..018
XACC-001..050
BINT-001..018
RPT-001..018
PAQ-001..020
```

New authoring-phase families defined by canonical drafts:

```text
GAUTH-001..040   geometry authoring
WFLOW-001..030   workflow/preset/macro
NREG-001..030    numerical/tolerance/qualification registry
```

The semantic definitions are authoritative even while `TD-CI-001` keeps executable GitHub validation temporarily outside the documentation gate.

---

# 6. Research / market evidence

| File | Status | Purpose |
|---|---|---|
| [research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md) | ACTIVE master matrix | feature ↔ scientific evidence ↔ requirement |
| [research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md](research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md) | complete | posting/metatarsal/arch/heel dose |
| [research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md](research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md) | complete | relief/offloading redistribution |
| [research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md](research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md) | complete | arch geometry/mechanics/context/outcome |
| [research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md](research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md) | complete | heel containment/relief/camber/material |
| [research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md](research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md) | complete | profile/population boundaries |
| [research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md](research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md) | complete | PROM/comfort/adherence governance |
| [research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md](research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md) | complete | material/process/QC/service evidence |
| [research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md](research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md) | baseline | EasyCAD2/OrthoCAD/Insolution/Voxelcare/Sharp Shape functional comparison |
| [research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md](research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md) | **second pass complete** | expanded competitor set + literature answers to authoring gaps |
| [research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md](research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md) | intake complete / not qualified | first Sensor Medica pressure-platform family intake |

---

# 7. Pressure/device qualification package

| File | Status |
|---|---|
| [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) | methodology frozen |
| [research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md](research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md) | nominal/source intake complete |
| [validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md](validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md) | execution structure ready, limits not frozen |
| [`qualification/templates/pressure-bench-result-0.1.json`](../qualification/templates/pressure-bench-result-0.1.json) | machine-readable result template |

Real physical-unit qualification remains pending and is independent of the documentation work now in progress.

---

# 8. Historical / architecture-hypothesis material

Preserve, but do not treat as current product authority:

| File | Status |
|---|---|
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | historical functional baseline |
| [spec/03_geometry_operation_model.md](spec/03_geometry_operation_model.md) | historical OpenSubdiv-first hypothesis; domain conflicts defer to `16_geometry_authoring_contract.md` |
| [spec/04_base_template.md](spec/04_base_template.md) | candidate / not frozen |
| [spec/05_parametric_orthosis_geometry.md](spec/05_parametric_orthosis_geometry.md) | provisional math / not clinical authority |
| [spec/CAD_ENGINE_CAPABILITY_SPEC.md](spec/CAD_ENGINE_CAPABILITY_SPEC.md) | engine capability baseline; architecture parked |
| [spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md](spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md) | parked architecture-selection checkpoint |
| [research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md](research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md) | archived library/portability research |

---

# 9. Current adopted conclusions

1. EasyCAD2 is behavioral evidence, not scientific truth.
2. BiomechE-CAD is a vertical orthotic CAD, not a generic modeler.
3. Semantic prescription survives final geometry.
4. Dose, placement, units, side, anatomical reference and source provenance are structured data.
5. Capture context and landmark provenance matter when scan geometry influences design.
6. Geometry dose and mechanical/material dose remain distinct.
7. Named orthotic operations remain domain concepts even if low-level geometry primitives are shared.
8. Workflow knowledge is P0 semantic infrastructure; advanced automation is later UX.
9. Presets/macros use exact version/hash and cannot rewrite historical revisions.
10. Numeric rules are typed by authority; `OPEN` remains `OPEN`.
11. Clinical thresholds are profile/population/protocol/ROI specific.
12. Manufacturing tolerance belongs to a qualified process/profile, not a global CAD constant.
13. CAD nominal geometry, manufactured artifact and measured physical part remain distinct.
14. BiomechE remains quantitative KPI authority.
15. Reports are immutable derivations from exact source entities.
16. Architecture selection remains downstream of frozen product/authoring contracts.
17. `TD-CI-001` is deferred and does not block documentation work.

---

# 10. Work queue — exact next documentation steps

1. Review/freeze `16_geometry_authoring_contract.md` as v1.
2. Review/freeze `17_workflow_preset_macro.md` as v1.
3. Review/freeze `18_numerical_qualification_registry.md` as v1.
4. Allocate representative geometry acceptance scenarios/fixtures for arch, heel, wedge, corrective element, mirror, section, thickness and deviation-map semantics.
5. Define schema-v0.2 change set required for capture context, richer landmark provenance and workflow applications — **documentation first, migration later**.
6. Continue real FM12050/material/process qualification in parallel when physical evidence is available.
7. Resume geometry-engine shoot-out only after the authoring/acceptance contracts are sufficiently frozen.

---

# 11. Documentation maintenance rules

1. `BIBLIOGRAPHY.md` remains the single bibliographic authority.
2. Vendor evidence establishes market capability, not efficacy.
3. Study-specific doses do not become universal defaults.
4. `OPEN` values are never filled by convenience.
5. Historical documents remain visibly historical.
6. Update `RESUME_HERE.md`, this index and `TRACEABILITY_MATRIX.md` after substantial work.
7. CI state is governed by `TECHNICAL_DEBT.md` while `TD-CI-001` is open.
