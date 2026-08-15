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
4. [spec/02_project_schema.md](spec/02_project_schema.md) — current persisted semantic baseline.
5. [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) — frozen coordinate/laterality/registration semantics.
6. [spec/16_geometry_authoring_contract.md](spec/16_geometry_authoring_contract.md) — P0 geometry-authoring semantics, kernel independent.
7. [spec/17_workflow_preset_macro.md](spec/17_workflow_preset_macro.md) — P0 reusable workflow/preset/macro semantics.
8. [spec/18_numerical_qualification_registry.md](spec/18_numerical_qualification_registry.md) — numerical/tolerance/qualification governance.
9. [validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md](validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md) — 22 representative architecture-independent P0 scenarios.
10. [validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md](validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md) — cross-document consistency audit, 0 blocking contradictions.
11. [validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md](validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md) — integrates `GAUTH/WFLOW/NREG` into the older acceptance baseline.
12. [spec/19_project_schema_v0_2_changeset.md](spec/19_project_schema_v0_2_changeset.md) — documented schema evolution; **not yet materialized**.
13. [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) — frozen BiomechE↔CAD quantitative contract.
14. [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) — frozen reporting/provenance contract.
15. [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) — frozen pressure-device qualification methodology.
16. [DECISIONS.md](DECISIONS.md) — cross-cutting decisions.
17. [TECHNICAL_DEBT.md](TECHNICAL_DEBT.md) — explicitly deferred engineering debt.
18. [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) — single authoritative bibliography.

`spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is historical/audit material and must not be mistaken for v2.

---

## 2. Current work order

```text
FUNCTIONALITY + EASYCAD2 + SCIENTIFIC EVIDENCE       DONE baseline
FUNCTIONAL SPEC v2                                   CANONICAL
PROJECT SCHEMA / PROVENANCE                          ACTIVE baseline
COORDINATE / REGISTRATION                            FROZEN v1
BIOMECHE INTEGRATION                                 FROZEN v1
REPORTING / TRACEABILITY                             FROZEN v1
PRESSURE ACQUISITION QUALIFICATION METHOD            FROZEN v1
COMPETITOR + LITERATURE SECOND PASS                  DONE
REQUIREMENT TRACEABILITY                             DONE v0.3
GEOMETRY AUTHORING CONTRACT                          CANONICAL DRAFT v0.1
WORKFLOW / PRESET / MACRO CONTRACT                   CANONICAL DRAFT v0.1
NUMERICAL / TOLERANCE / QUALIFICATION REGISTRY      CANONICAL DRAFT v0.1
P0 AUTHORING ACCEPTANCE CATALOG                      DONE — 22 scenarios
PROJECT SCHEMA v0.2 CHANGE-SET                       DONE design draft / not materialized
CROSS-DOCUMENT AUDIT                                 DONE — 0 blockers
ACCEPTANCE SUITE INTEGRATION                         DONE — addendum v1
FINAL STATUS NORMALIZATION / FREEZE                  NEXT
GEOMETRY ENGINE SCORECARD + SHOOT-OUT                AFTER FREEZE
```

GitHub CI is **not** a current documentation gate. See `TECHNICAL_DEBT.md`, `TD-CI-001`.

---

# 3. Canonical product specifications

| File | Status | Purpose |
|---|---|---|
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) | **CANONICAL v2** | Evidence-led P0/P1/P2 product scope |
| [spec/02_project_schema.md](spec/02_project_schema.md) | ACTIVE schema baseline v0.1 | Immutable revisions, definitions, acquisitions, outcomes, materials, manufacturing, provenance |
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
| [spec/18_numerical_qualification_registry.md](spec/18_numerical_qualification_registry.md) | **CANONICAL DRAFT v0.1** | Numeric authority classes, `OPEN` values, tolerance and qualification ownership |
| [spec/19_project_schema_v0_2_changeset.md](spec/19_project_schema_v0_2_changeset.md) | DESIGN CHANGE-SET | Additive schema v0.2 direction; no JSON/schema migration yet |

---

# 4. Traceability / acceptance / governance

| File | Status | Purpose |
|---|---|---|
| [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) | **CANONICAL v0.3** | Product family → owner → acceptance → evidence → open gap |
| [validation/functional_acceptance_suite.md](validation/functional_acceptance_suite.md) | ACTIVE baseline | Existing pre-authoring acceptance families; current-state wording supplemented by addendum |
| [validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md](validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md) | **CANONICAL TEST-SPEC v0.1** | 22 representative authoring/workflow/numerical scenarios |
| [validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md](validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md) | COMPLETE | 0 blocking semantic contradictions; 5 non-blocking harmonizations |
| [validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md](validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md) | **CANONICAL ADDENDUM v1** | Registers `GAUTH/WFLOW/NREG` and current precedence without depending on CI |
| [DECISIONS.md](DECISIONS.md) | CANONICAL | Cross-cutting durable decisions |
| [TECHNICAL_DEBT.md](TECHNICAL_DEBT.md) | ACTIVE | Deferred engineering debt, including `TD-CI-001` |
| [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) | **CANONICAL** | Stable source IDs and source-role governance |

Existing acceptance namespaces remain:

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

New authoring-phase namespaces:

```text
GAUTH-001..040
WFLOW-001..030
NREG-001..030
```

---

# 5. Research / market evidence

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
| [research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md](research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md) | baseline | first market comparison |
| [research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md](research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md) | **second pass complete** | expanded competitor set + literature answers to authoring gaps |
| [research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md](research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md) | intake complete / not qualified | first Sensor Medica pressure-platform family intake |

---

# 6. Pressure/device qualification package

| File | Status |
|---|---|
| [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) | methodology frozen |
| [research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md](research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md) | nominal/source intake complete |
| [validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md](validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md) | execution structure ready; limits not frozen |
| [`qualification/templates/pressure-bench-result-0.1.json`](../qualification/templates/pressure-bench-result-0.1.json) | machine-readable result template |

Real physical-unit qualification remains pending and is independent of the current documentation freeze.

---

# 7. Historical / architecture-hypothesis material

Preserve, but do not treat as current product authority:

| File | Status |
|---|---|
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | historical functional baseline |
| [spec/03_geometry_operation_model.md](spec/03_geometry_operation_model.md) | historical OpenSubdiv-first hypothesis; product semantics defer to `16_geometry_authoring_contract.md` |
| [spec/04_base_template.md](spec/04_base_template.md) | candidate / not frozen |
| [spec/05_parametric_orthosis_geometry.md](spec/05_parametric_orthosis_geometry.md) | provisional math / not clinical authority |
| [spec/CAD_ENGINE_CAPABILITY_SPEC.md](spec/CAD_ENGINE_CAPABILITY_SPEC.md) | engine capability baseline; architecture parked |
| [spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md](spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md) | parked architecture-selection checkpoint |
| [research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md](research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md) | archived library/portability research |

---

# 8. Current adopted conclusions

1. EasyCAD2 is behavioral evidence, not scientific truth.
2. Semantic prescription survives final geometry.
3. Capture context and landmark provenance are P0 when they influence design.
4. Placement is a typed reference; study-specific locations are not universal coordinates.
5. Geometry dose and material/mechanical dose remain distinct.
6. Named orthotic operations remain domain concepts even if low-level geometry primitives are shared.
7. Workflow knowledge is P0 semantic infrastructure; advanced automation is P1+.
8. Presets/macros use exact version/hash and freeze their expanded historical meaning.
9. Numeric rules are classified by authority; `OPEN` remains `OPEN`.
10. Manufacturing/device/clinical limits are profile-owned; no global hidden tolerance.
11. CAD nominal geometry, manufacturing artifact and measured physical part remain distinct.
12. Cross-document audit found no blocking semantic contradiction in the P0 authoring package.
13. Architecture selection remains downstream of authoring/acceptance contracts.
14. `TD-CI-001` is deferred and does not block documentation work.

---

# 9. Exact next documentation work

1. Normalize status headers/cross-references and freeze `16`, `17`, `18` as v1.
2. Promote the P0 authoring catalog to frozen semantic test-spec v1 and the schema v0.2 document to approved change-set/not materialized.
3. Derive a geometry-engine evaluation scorecard directly from `GAUTH/WFLOW/NREG` plus the 22 representative scenarios.
4. Only then resume OpenSubdiv vs openNURBS/ON_SubD evaluation.

Parallel real-device/material/process qualification may continue whenever physical evidence is available.

---

# 10. Documentation maintenance rules

1. `BIBLIOGRAPHY.md` remains the single bibliographic authority.
2. Vendor evidence establishes market capability, not efficacy.
3. Study-specific doses do not become universal defaults.
4. `OPEN` values are never filled by convenience.
5. Historical documents remain visibly historical.
6. Update `RESUME_HERE.md`, this index and `TRACEABILITY_MATRIX.md` after substantial work.
7. CI state is governed by `TECHNICAL_DEBT.md` while `TD-CI-001` is open.
