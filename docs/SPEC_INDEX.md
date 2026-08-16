# BiomechE-CAD — Specification Index

**Status:** **CANONICAL DOCUMENT MAP**  
**Updated:** 2026-08-16  
**Current phase:** written P0 documentation closure **GO**; canonical visual-reference package **NEXT**.

Markdown under `docs/` is the canonical documentation source.

---

## 1. Resume order

Read in this order before substantial work:

1. [RESUME_HERE.md](RESUME_HERE.md) — mission, frozen state and exact restart point.
2. [P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md](P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md) — DOC-00..14 + VIS-01..04 work plan.
3. [validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md](validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md) — **WRITTEN DOCUMENTATION CLOSURE GO**, 0 blockers.
4. [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) — **canonical product scope**.
5. [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) — **CANONICAL v0.6**, requirement→owner→acceptance→evidence→open state.
6. [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) — frozen coordinates/laterality/registration.
7. [spec/02_project_schema.md](spec/02_project_schema.md) — persisted semantic baseline v0.1.
8. [spec/06_corrective_elements.md](spec/06_corrective_elements.md) — **FROZEN v1**.
9. [spec/08_material_stiffness.md](spec/08_material_stiffness.md) — **FROZEN v1**.
10. [spec/09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) — **FROZEN v1**.
11. [spec/10_manufacturing.md](spec/10_manufacturing.md) — **FROZEN v1**.
12. [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) — **FROZEN v1**.
13. [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) — **FROZEN v1**.
14. [spec/13_use_case_profiles.md](spec/13_use_case_profiles.md) — **FROZEN v1**.
15. [spec/14_prom_comfort_adherence.md](spec/14_prom_comfort_adherence.md) — **FROZEN v1**.
16. [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) — **FROZEN methodology v1**.
17. [spec/16_geometry_authoring_contract.md](spec/16_geometry_authoring_contract.md) — **FROZEN v1**.
18. [spec/17_workflow_preset_macro.md](spec/17_workflow_preset_macro.md) — **FROZEN v1**.
19. [spec/18_numerical_qualification_registry.md](spec/18_numerical_qualification_registry.md) — **FROZEN v1**.
20. [spec/19_project_schema_v0_2_changeset.md](spec/19_project_schema_v0_2_changeset.md) — **APPROVED / NOT MATERIALIZED**.
21. [spec/20_input_scan_reference_data.md](spec/20_input_scan_reference_data.md) — **FROZEN v1**.
22. [spec/21_product_workflow_interaction.md](spec/21_product_workflow_interaction.md) — **FROZEN v1**.
23. [spec/22_interchange_manufacturing_handoff.md](spec/22_interchange_manufacturing_handoff.md) — **FROZEN v1**.
24. [spec/23_realtime_performance_contract.md](spec/23_realtime_performance_contract.md) — **FROZEN doctrine v1; budgets OPEN**.
25. [validation/24_validation_verification_master_plan.md](validation/24_validation_verification_master_plan.md) — **CANONICAL V&V v1**.
26. [spec/25_intended_use_risk_privacy_security_boundary.md](spec/25_intended_use_risk_privacy_security_boundary.md) — **CANONICAL boundary v1; regulatory classification OPEN**.
27. [validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md](validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md) — frozen `AUTH-C01..C22`.
28. [P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md](P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md) — previous authoring freeze audit.
29. [research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md](research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md) — scorecard; **no winner**.
30. [validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md](validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md) — Q0..Q7 preserved / execution deferred.
31. [DECISIONS.md](DECISIONS.md)
32. [TECHNICAL_DEBT.md](TECHNICAL_DEBT.md)
33. [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md)
34. [NEXT_CHAT_PROMPT.md](NEXT_CHAT_PROMPT.md)

`spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` remains historical/audit material.

---

## 2. Current work order

```text
FUNCTIONALITY + EASYCAD2 + SCIENTIFIC EVIDENCE       DONE baseline
FUNCTIONAL SPEC v2                                   CANONICAL
COORDINATE / REGISTRATION                            FROZEN v1
CORRECTIVE / OFFLOADING ELEMENTS                     FROZEN v1
MATERIAL / STIFFNESS                                 FROZEN v1
ANALYSIS / QC / DFM                                  FROZEN v1
MANUFACTURING LIFECYCLE                              FROZEN v1
BIOMECHE INTEGRATION                                 FROZEN v1
REPORTING / TRACEABILITY                             FROZEN v1
USE-CASE PROFILES                                    FROZEN v1
PROM / COMFORT / ADHERENCE                          FROZEN v1
PRESSURE ACQUISITION QUALIFICATION METHOD            FROZEN v1
GEOMETRY AUTHORING CONTRACT                          FROZEN v1
WORKFLOW / PRESET / MACRO CONTRACT                   FROZEN v1
NUMERICAL / TOLERANCE / QUALIFICATION REGISTRY      FROZEN v1
INPUT / SCAN / REFERENCE DATA                        FROZEN v1
PRODUCT WORKFLOW / INTERACTION                       FROZEN v1
INTERCHANGE / MANUFACTURING HANDOFF                  FROZEN v1
REALTIME / PERFORMANCE DOCTRINE                      FROZEN v1 — budgets OPEN
V&V MASTER PLAN                                      CANONICAL v1
INTENDED USE / RISK / PRIVACY / SECURITY BOUNDARY   CANONICAL v1 — regulatory classification OPEN
PROJECT SCHEMA v0.2 CHANGE-SET                       APPROVED / NOT MATERIALIZED
P0 WRITTEN DOCUMENTATION FINAL AUDIT                 DONE — 0 blockers / GO
VISUAL REFERENCE BRIEF                               NEXT
CANONICAL MOCKUPS                                    PENDING VIS-02
REQUIREMENT ↔ SCREEN TRACEABILITY                    PENDING VIS-04
GEOMETRY ENGINE POC / FINAL SELECTION                DEFERRED; no winner
```

GitHub CI remains non-blocking for this documentation/visual phase under `TD-CI-001`.

---

# 3. Frozen / canonical product specifications

| File | Status | Purpose |
|---|---|---|
| `BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | **CANONICAL v2** | Product scope/P0-P2 |
| `01_coordinate_registration.md` | **FROZEN v1** | Frames, side, transforms, registration |
| `02_project_schema.md` | CANONICAL ACTIVE v0.1 | Current persisted semantic baseline |
| `06_corrective_elements.md` | **FROZEN v1** | Named corrective/offload prescription, typed placement, requested/realized dose |
| `08_material_stiffness.md` | **FROZEN v1** | Material identity, regions/stacks, measured/effective/service mechanics |
| `09_analysis_qc_dfm.md` | **FROZEN v1** | Quantitative outcome, geometric QC and DFM semantics |
| `10_manufacturing.md` | **FROZEN v1** | Profile/run/artifact/physical-part/QC lifecycle |
| `11_biomeche_integration.md` | **FROZEN v1** | BiomechE quantitative contract |
| `12_reporting_traceability.md` | **FROZEN v1** | Report/source-manifest reproducibility |
| `13_use_case_profiles.md` | **FROZEN v1** | Context/profile non-transfer rules |
| `14_prom_comfort_adherence.md` | **FROZEN v1** | Construct/instrument/comfort/fit/satisfaction/adherence separation |
| `15_pressure_acquisition_qualification.md` | **FROZEN methodology v1** | Device/protocol qualification method |
| `16_geometry_authoring_contract.md` | **FROZEN v1** | Semantic authoring/replay/mirror/inspection/production boundary |
| `17_workflow_preset_macro.md` | **FROZEN v1** | Exact reusable knowledge definitions and human authority |
| `18_numerical_qualification_registry.md` | **FROZEN v1** | `OPEN`, authority classes, tolerance/default governance |
| `19_project_schema_v0_2_changeset.md` | **APPROVED / NOT MATERIALIZED** | Future additive persisted representation |
| `20_input_scan_reference_data.md` | **FROZEN v1** | Original/processed/registered/derived source lineage |
| `21_product_workflow_interaction.md` | **FROZEN v1** | End-to-end interaction/state semantics |
| `22_interchange_manufacturing_handoff.md` | **FROZEN v1** | Format capability/loss/units/frame/package semantics |
| `23_realtime_performance_contract.md` | **FROZEN doctrine v1** | Performance measurement/qualification, budgets OPEN |
| `25_intended_use_risk_privacy_security_boundary.md` | **CANONICAL v1** | Regulatory/privacy/security boundary; final classification OPEN |

---

# 4. Engineering / historical material — non-authoritative

| File | Status | Rule |
|---|---|---|
| `03_geometry_operation_model.md` | historical OpenSubdiv-first hypothesis | does not override `16` |
| `04_base_template.md` | **ENGINEERING CANDIDATE / QUALIFICATION FIXTURE** | `41x17`, Catmull-Clark etc. are hypotheses, not product requirements |
| `05_parametric_orthosis_geometry.md` | **PROVISIONAL ENGINEERING MATHEMATICAL REFERENCE** | formulas/directions/fixture values are PoC hypotheses |
| `CAD_ENGINE_CAPABILITY_SPEC.md` | historical | current authority is scorecard |
| `CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md` | historical checkpoint | no current selection authority |
| `BIOMECHE_CAD_FUNCTIONAL_SPEC.md` | historical v1 product baseline | v2 is current |

There is intentionally no `07_*`; the numbering gap is historical and has no semantic meaning.

---

# 5. Traceability / acceptance / V&V

| File | Status | Purpose |
|---|---|---|
| `TRACEABILITY_MATRIX.md` | **CANONICAL v0.6** | Current product/acceptance/open-state map |
| `validation/functional_acceptance_suite.md` | ACTIVE historical/integration baseline | Existing XACC and broad acceptance; subordinate ranges to owning specs/master plan |
| `validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md` | **FROZEN v1** | `AUTH-C01..C22` |
| `validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md` | CANONICAL authoring addendum | `GAUTH/WFLOW/NREG` integration |
| `validation/P0_DOCUMENTATION_CLOSURE_AUDIT_2026-08-16.md` | COMPLETE | DOC-00 authority/inventory audit |
| `validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md` | **COMPLETE / GO** | DOC-14 written closure audit, 0 blockers |
| `validation/24_validation_verification_master_plan.md` | **CANONICAL v1** | Evidence layers/result states/requalification/release evidence |

Current acceptance namespaces:

```text
SCHEMA-*  OFF-*   CE-*    ARCH-*  HEEL-*  PROF-*  PROM-*  MAT-*
AQ-*      MAN-*   BINT-*  RPT-*   PAQ-*   GAUTH-* WFLOW-* NREG-*
AUTH-C*   INPUT-* UX-*    XCHG-*  PERF-*  VV-*    REG-*   XACC-*
HG-01..15
```

---

# 6. Research / scientific evidence

Canonical evidence remains in:

```text
BIBLIOGRAPHY.md
research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md
research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md
research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md
research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md
research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md
research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md
research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md
research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md
research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md
research/COMPETITOR_LITERATURE_GAP_AUDIT_2026-08-15.md
```

The 2026 closure pass additionally verified current official standards/regulatory sources for 3MF/AMF/data packages, MDR/MDCG, GDPR, ISO 14971/13485. These must be normalized into canonical bibliography IDs in a dedicated maintenance pass; until then new documents mark them explicitly as current-source supplements.

Do not restart generic CAD market research. Future research is gap-driven.

---

# 7. Architecture evaluation — preserved / deferred

| File | Status |
|---|---|
| `research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md` | baseline v0.1 — **NO WINNER** |
| `validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md` | Q0..Q7 plan preserved |
| `research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md` | historical pre-scorecard research |

Architecture resumes only after visual-reference closure or explicit reprioritization.

No engine selection is implied by `04/05`, by mockups, or by any new product contract.

---

# 8. Physical qualification streams — still separate

Pressure-device package:

```text
spec/15_pressure_acquisition_qualification.md
research/SENSORMEDICA_FM12050_QUALIFICATION_INTAKE_2026-08-15.md
validation/FM12050_PFM2120_BENCH_QUALIFICATION_PROTOCOL_DRAFT.md
qualification/templates/pressure-bench-result-0.1.json
```

Real material/process/manufacturing qualification likewise requires physical evidence and is not implied by written-spec freeze.

---

# 9. Visual reference package — NEXT

Canonical target paths:

```text
docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
docs/ux/mockups/v1/README.md
docs/ux/mockups/v1/manifest.md
```

Required baseline screens:

```text
M01 Project / Patient / Case
M02 Import / Scan qualification
M03 Registration / Landmarks
M04 Base orthosis / Template
M05 Parametric authoring
M06 Corrective / Offloading elements
M07 Sculpt / Local editing
M08 Materials / mechanical prescription
M09 Inspection / Geometry QC
M10 BiomechE Before / After / Delta
M11 DFM / Manufacturing preparation
M12 Revision / Provenance / Report
M13 Physical-part QC / Outcome follow-up
M14 Responsive / compact view
```

Authority rule:

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
MOCKUP = VISUAL / INTERACTION REFERENCE
```

Each mockup must be versioned and map to owning specs + acceptance IDs.

---

# 10. Current exact next task

```text
VIS-01  create canonical visual brief / design system direction
VIS-02  generate/save M01..M14 canonical mockups
VIS-03  version/archive editable source + rendered references
VIS-04  build requirement ↔ screen traceability and visual-closure audit
```

A bibliography-normalization pass for the new 2025/2026 sources may be done immediately before or alongside VIS-01 because it does not reopen product semantics.

After VIS closure, resume geometry-engine Q0 unless project owner reprioritizes.
