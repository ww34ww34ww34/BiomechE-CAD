# BiomechE-CAD — Specification Index

**Status:** CANONICAL DOCUMENT MAP  
**Updated:** 2026-08-16

Markdown under `docs/` is the canonical documentation source.

---

## 1. Resume order

Read in this order before substantial work:

1. [RESUME_HERE.md](RESUME_HERE.md) — current mission, frozen state and exact restart point.
2. [P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md](P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md) — **ACTIVE WORK PLAN**, DOC-00..14 + VIS-01..04.
3. [P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md](P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md) — definitive P0 authoring freeze audit.
4. [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) — **canonical product scope**.
5. [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) — requirement → owner → acceptance → evidence → open state.
6. [spec/02_project_schema.md](spec/02_project_schema.md) — current persisted semantic baseline v0.1.
7. [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) — frozen coordinate/laterality/registration semantics.
8. [spec/16_geometry_authoring_contract.md](spec/16_geometry_authoring_contract.md) — **FROZEN v1** geometry-authoring semantics.
9. [spec/17_workflow_preset_macro.md](spec/17_workflow_preset_macro.md) — **FROZEN v1** reusable workflow/preset/macro semantics.
10. [spec/18_numerical_qualification_registry.md](spec/18_numerical_qualification_registry.md) — **FROZEN v1** numerical/tolerance/qualification governance.
11. [validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md](validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md) — **FROZEN semantic test-spec v1**, 22 scenarios.
12. [spec/19_project_schema_v0_2_changeset.md](spec/19_project_schema_v0_2_changeset.md) — **APPROVED CHANGE-SET / NOT MATERIALIZED**.
13. [validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md](validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md) — previous cross-document audit, 0 blockers.
14. [validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md](validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md) — frozen-authoring acceptance integration.
15. [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) — frozen BiomechE↔CAD quantitative contract.
16. [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) — frozen reporting/provenance contract.
17. [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) — frozen pressure-device qualification methodology.
18. [research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md](research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md) — architecture scorecard baseline; **no winner**.
19. [validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md](validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md) — Q0..Q7 architecture qualification plan, currently deferred by project priority.
20. [DECISIONS.md](DECISIONS.md) — cross-cutting decisions.
21. [TECHNICAL_DEBT.md](TECHNICAL_DEBT.md) — deferred engineering debt including `TD-CI-001`.
22. [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) — authoritative bibliography.
23. [NEXT_CHAT_PROMPT.md](NEXT_CHAT_PROMPT.md) — copy/paste continuation prompt.

`spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is historical/audit material and must not be mistaken for v2.

---

## 2. Current work order

```text
FUNCTIONALITY + EASYCAD2 + SCIENTIFIC EVIDENCE       DONE baseline
FUNCTIONAL SPEC v2                                   CANONICAL
COORDINATE / REGISTRATION                            FROZEN v1
BIOMECHE INTEGRATION                                 FROZEN v1
REPORTING / TRACEABILITY                             FROZEN v1
PRESSURE ACQUISITION QUALIFICATION METHOD            FROZEN v1
GEOMETRY AUTHORING CONTRACT                          FROZEN v1
WORKFLOW / PRESET / MACRO CONTRACT                   FROZEN v1
NUMERICAL / TOLERANCE / QUALIFICATION REGISTRY      FROZEN v1
P0 AUTHORING ACCEPTANCE CATALOG                      FROZEN semantic test-spec v1
PROJECT SCHEMA v0.2 CHANGE-SET                       APPROVED / NOT MATERIALIZED
P0 AUTHORING CROSS-DOCUMENT AUDIT                    DONE — 0 blockers
GEOMETRY ENGINE EVALUATION SCORECARD                 DONE baseline v0.1 — NO WINNER
GEOMETRY ENGINE POC/QUALIFICATION PLAN               DONE plan v0.1 — EXECUTION DEFERRED
P0 DOCUMENTATION CLOSURE PLAN                        ACTIVE — DOC-00 NEXT
CANONICAL VISUAL REFERENCE PACKAGE                   PLANNED AFTER WRITTEN CLOSURE
ARCHITECTURE SHOOT-OUT / FINAL SELECTION             DEFERRED UNTIL DOC/VIS CLOSURE OR OWNER REPRIORITIZATION
```

GitHub CI is **not** a current documentation gate. `TD-CI-001` remains deliberately deferred.

---

# 3. Canonical / frozen product specifications

| File | Status | Purpose |
|---|---|---|
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) | **CANONICAL v2** | Evidence-led product scope |
| [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) | **FROZEN v1** | Coordinate, laterality, intrinsic frame, transforms, registration |
| [spec/02_project_schema.md](spec/02_project_schema.md) | ACTIVE schema baseline v0.1 | Immutable revisions, definitions, acquisitions, outcomes, manufacturing/provenance |
| [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) | **FROZEN v1** | KPI/result provenance, quality, comparison, reanalysis |
| [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) | **FROZEN v1** | Immutable report/source-manifest semantics |
| [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) | **FROZEN methodology v1** | Intended-use-specific device/protocol qualification |
| [spec/16_geometry_authoring_contract.md](spec/16_geometry_authoring_contract.md) | **FROZEN v1** | Typed authoring operations, dose, placement, capture/landmark provenance, mirror, inspection, production boundary |
| [spec/17_workflow_preset_macro.md](spec/17_workflow_preset_macro.md) | **FROZEN v1** | Versioned reusable preset/macro/workflow semantics and human authority |
| [spec/18_numerical_qualification_registry.md](spec/18_numerical_qualification_registry.md) | **FROZEN v1** | Numeric authority classes, `OPEN` values, tolerance and qualification ownership |
| [spec/19_project_schema_v0_2_changeset.md](spec/19_project_schema_v0_2_changeset.md) | **APPROVED / NOT MATERIALIZED** | Additive schema direction; runtime/reference schema remains v0.1 |

---

# 4. Specifications to close in P0-DOC-CLOSURE

| File | Current status | Planned task |
|---|---|---|
| [spec/06_corrective_elements.md](spec/06_corrective_elements.md) | ACTIVE v0 | `DOC-01` — harmonize/freeze v1 |
| [spec/08_material_stiffness.md](spec/08_material_stiffness.md) | ACTIVE v0 | `DOC-02` — harmonize/freeze v1 |
| [spec/09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) | ACTIVE v0 | `DOC-03` — harmonize/freeze v1 |
| [spec/10_manufacturing.md](spec/10_manufacturing.md) | ACTIVE v0 | `DOC-04` — harmonize/freeze v1 |
| [spec/13_use_case_profiles.md](spec/13_use_case_profiles.md) | ACTIVE v0 | `DOC-05` — harmonize/freeze v1 |
| [spec/14_prom_comfort_adherence.md](spec/14_prom_comfort_adherence.md) | ACTIVE v0 | `DOC-06` — harmonize/freeze v1 |

The frozen `16/17/18` documents are authority where older active documents overlap authoring, workflow or numerical governance.

---

# 5. Provisional / historical specifications requiring disposition

| File | Status | Planned action |
|---|---|---|
| [spec/03_geometry_operation_model.md](spec/03_geometry_operation_model.md) | historical OpenSubdiv-first hypothesis | preserve as historical unless DOC-00 finds still-canonical material |
| [spec/04_base_template.md](spec/04_base_template.md) | candidate / not frozen | `DOC-07` definitive disposition |
| [spec/05_parametric_orthosis_geometry.md](spec/05_parametric_orthosis_geometry.md) | provisional math / not clinical authority | `DOC-07` definitive disposition |
| [spec/CAD_ENGINE_CAPABILITY_SPEC.md](spec/CAD_ENGINE_CAPABILITY_SPEC.md) | historical capability baseline | subordinate to current scorecard |
| [spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md](spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md) | parked pre-freeze checkpoint | historical |
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | historical product baseline | preserve for audit only |

The numbering gap between `06` and `08` is historical until DOC-00 determines otherwise. Do not invent a `07` solely to fill the sequence.

---

# 6. Planned new implementation-neutral contracts

The following names/paths are planned and may be adjusted by DOC-00 if evidence shows a better split:

| Planned file | Task | Purpose |
|---|---|---|
| `spec/20_input_scan_reference_data.md` | `DOC-08` | Input/scan/reference provenance and preprocessing contract |
| `spec/21_product_workflow_interaction.md` | `DOC-09` | End-to-end product workflow and interaction semantics |
| `spec/22_interchange_manufacturing_handoff.md` | `DOC-10` | Import/export/handoff, coordinate/unit/loss boundaries |
| `spec/23_realtime_performance_contract.md` | `DOC-11` | Candidate-neutral performance doctrine and metrics |
| `validation/VALIDATION_VERIFICATION_MASTER_PLAN.md` | `DOC-12` | Unified V&V evidence hierarchy |
| safety/governance package path to be chosen | `DOC-13` | Intended-use/risk/privacy/security boundary |

---

# 7. Visual reference package — planned canonical output

After written documentation closure:

```text
docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
docs/ux/mockups/v1/
```

The baseline mockup set is `M01..M14` and must cover the P0 workflow from project/case through scan, registration, orthosis authoring, corrective elements, materials, QC/BiomechE, manufacturing, revision/provenance and physical-part follow-up.

Prefer both editable/source-controlled mockup assets and rendered reference images where practical.

Authority rule:

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
MOCKUP = VISUAL / INTERACTION REFERENCE
```

Mockups must be versioned and mapped back to the relevant specifications/requirements.

---

# 8. Traceability / acceptance / validation

| File | Status | Purpose |
|---|---|---|
| [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) | **CANONICAL v0.5** | Requirement family → owner → acceptance → evidence → status |
| [validation/functional_acceptance_suite.md](validation/functional_acceptance_suite.md) | ACTIVE baseline | Existing acceptance baseline |
| [validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md](validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md) | **FROZEN v1** | `AUTH-C01..C22` |
| [validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md](validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md) | COMPLETE | Previous authoring cross-audit, 0 blockers |
| [validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md](validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md) | CANONICAL ADDENDUM v1 | Integrates `GAUTH/WFLOW/NREG` |
| [P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md](P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md) | COMPLETE / GO | P0 authoring freeze verdict |
| planned `validation/P0_DOCUMENTATION_CLOSURE_AUDIT_2026-08-16.md` | `DOC-00` NEXT | Whole-document inventory/authority/closure audit |
| planned final P0 documentation cross-audit | `DOC-14` | Documentation closure verdict |

Existing acceptance namespaces include:

```text
SCHEMA-*  OFF-*  CE-*  ARCH-*  HEEL-*  PROF-*  PROM-*  MAT-*  MAN-*
XACC-*    BINT-* RPT-* PAQ-*   GAUTH-* WFLOW-* NREG-* AUTH-C*
```

---

# 9. Research / evidence

Key research baselines remain:

- [research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md)
- `research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md`
- `research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md`
- `research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md`
- `research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md`
- `research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md`
- `research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md`
- `research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md`
- [research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md](research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md)
- [research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md](research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md)
- [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md)

Do not restart generic market research. New research should be driven by an identified closure gap or by the current-regulation requirements of DOC-13.

---

# 10. Architecture evaluation — preserved / execution deferred

| File | Status |
|---|---|
| [research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md](research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md) | ACTIVE BASELINE v0.1 — no winner |
| [validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md](validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md) | ACTIVE PLAN v0.1 — Q0..Q7 preserved |
| [research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md](research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md) | historical pre-scorecard architecture research |

Architecture PoC resumes only after documentation/visual closure or explicit owner reprioritization.

No geometry engine has been selected.

---

# 11. Pressure/device qualification package

| File | Status |
|---|---|
| [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) | methodology frozen |
| [research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md](research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md) | intake complete / not qualified |
| [validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md](validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md) | execution structure ready; limits not frozen |
| `qualification/templates/pressure-bench-result-0.1.json` | result template |

Real physical-unit qualification remains a separate future evidence stream.

---

# 12. Current exact next task

```text
DOC-00 — P0 Documentation Closure Audit
```

Create:

`docs/validation/P0_DOCUMENTATION_CLOSURE_AUDIT_2026-08-16.md`

Then execute `DOC-01..DOC-06`, followed by `DOC-07..DOC-14`, then `VIS-01..VIS-04`.

Only after that, unless explicitly reprioritized, resume geometry-engine `Q0..Q7`.
