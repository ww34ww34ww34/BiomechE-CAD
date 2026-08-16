# BiomechE-CAD — Specification Index

**Status:** **CANONICAL DOCUMENT MAP**  
**Updated:** 2026-08-16  
**Current phase:** **P0 written documentation complete + canonical visual source/browser baseline v1 complete**. Only repository packaging of PNG reference binaries remains; geometry-engine qualification is ready with no winner selected.

Markdown under `docs/` is the canonical documentation source.

---

## 1. Resume order

Read in this order before substantial work:

1. [RESUME_HERE.md](RESUME_HERE.md)
2. [P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md](P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md)
3. [validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md](validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md) — written closure **GO / 0 blockers**.
4. [ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md](ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md) — canonical visual/interaction reference.
5. [ux/mockups/v1/manifest.md](ux/mockups/v1/manifest.md) — M01..M14 requirement mapping.
6. [ux/VISUAL_REFERENCE_CROSS_DOCUMENT_AUDIT_2026-08-16.md](ux/VISUAL_REFERENCE_CROSS_DOCUMENT_AUDIT_2026-08-16.md) — source-level audit.
7. [ux/VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md](ux/VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md) — browser/runtime/accessibility audit.
8. [ux/mockups/v1/rendered/README.md](ux/mockups/v1/rendered/README.md) — binary render archive contract.
9. [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) — canonical product scope.
10. [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) — **canonical v0.8**.
11. [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) — FROZEN v1.
12. [spec/02_project_schema.md](spec/02_project_schema.md) — current persisted semantic baseline v0.1.
13. [spec/06_corrective_elements.md](spec/06_corrective_elements.md) — FROZEN v1.
14. [spec/08_material_stiffness.md](spec/08_material_stiffness.md) — FROZEN v1.
15. [spec/09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) — FROZEN v1.
16. [spec/10_manufacturing.md](spec/10_manufacturing.md) — FROZEN v1.
17. [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) — FROZEN v1.
18. [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) — FROZEN v1.
19. [spec/13_use_case_profiles.md](spec/13_use_case_profiles.md) — FROZEN v1.
20. [spec/14_prom_comfort_adherence.md](spec/14_prom_comfort_adherence.md) — FROZEN v1.
21. [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) — FROZEN methodology v1.
22. [spec/16_geometry_authoring_contract.md](spec/16_geometry_authoring_contract.md) — FROZEN v1.
23. [spec/17_workflow_preset_macro.md](spec/17_workflow_preset_macro.md) — FROZEN v1.
24. [spec/18_numerical_qualification_registry.md](spec/18_numerical_qualification_registry.md) — FROZEN v1.
25. [spec/19_project_schema_v0_2_changeset.md](spec/19_project_schema_v0_2_changeset.md) — APPROVED / NOT MATERIALIZED.
26. [spec/20_input_scan_reference_data.md](spec/20_input_scan_reference_data.md) — FROZEN v1.
27. [spec/21_product_workflow_interaction.md](spec/21_product_workflow_interaction.md) — FROZEN v1.
28. [spec/22_interchange_manufacturing_handoff.md](spec/22_interchange_manufacturing_handoff.md) — FROZEN v1.
29. [spec/23_realtime_performance_contract.md](spec/23_realtime_performance_contract.md) — FROZEN doctrine v1; budgets OPEN.
30. [validation/24_validation_verification_master_plan.md](validation/24_validation_verification_master_plan.md) — CANONICAL V&V v1.
31. [spec/25_intended_use_risk_privacy_security_boundary.md](spec/25_intended_use_risk_privacy_security_boundary.md) — CANONICAL boundary v1; regulatory classification OPEN.
32. [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) — **CANONICAL; normalized 2026-08-16**.
33. [research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md](research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md) — no winner.
34. [validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md](validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md) — Q0..Q7.
35. [DECISIONS.md](DECISIONS.md)
36. [TECHNICAL_DEBT.md](TECHNICAL_DEBT.md)
37. [NEXT_CHAT_PROMPT.md](NEXT_CHAT_PROMPT.md)

`spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` remains historical/audit material and must not be mistaken for v2.

---

## 2. Current work order

```text
FUNCTIONAL / SCIENTIFIC PRODUCT BASELINE              DONE
P0 WRITTEN DOCUMENTATION                              COMPLETE / GO / 0 blockers
P0 VISUAL BRIEF                                       DONE
M01..M14 NAVIGABLE VISUAL SOURCE                      DONE
REQUIREMENT ↔ SCREEN TRACEABILITY                     DONE
VISUAL SOURCE-LEVEL AUDIT                             DONE / 0 blockers
M01..M14 BROWSER RENDER EXECUTION                     DONE 14/14
BROWSER/RUNTIME/A11Y AUDIT                            DONE / PASS WITH corrective items
REPOSITORY PNG BINARY ARCHIVE                         OPEN — packaging only
CANONICAL BIBLIOGRAPHY NORMALIZATION                  DONE
PROJECT SCHEMA v0.2                                   APPROVED / NOT MATERIALIZED
GEOMETRY ENGINE SCORECARD + Q0..Q7 PLAN               READY / NO WINNER
CI TD-CI-001                                           DEFERRED / NON-BLOCKING
```

---

## 3. Canonical / frozen product specifications

| File | Status | Purpose |
|---|---|---|
| `BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | CANONICAL v2 | Product scope / P0-P2 |
| `01_coordinate_registration.md` | FROZEN v1 | Frames, laterality, transforms, registration |
| `02_project_schema.md` | CANONICAL ACTIVE v0.1 | Current persisted semantic baseline |
| `06_corrective_elements.md` | FROZEN v1 | Corrective/offloading prescription semantics |
| `08_material_stiffness.md` | FROZEN v1 | Material/mechanical-dose semantics |
| `09_analysis_qc_dfm.md` | FROZEN v1 | Outcome, inspection, QC and DFM semantics |
| `10_manufacturing.md` | FROZEN v1 | Manufacturing/run/artifact/physical-part lifecycle |
| `11_biomeche_integration.md` | FROZEN v1 | BiomechE quantitative integration |
| `12_reporting_traceability.md` | FROZEN v1 | Immutable reporting/source manifests |
| `13_use_case_profiles.md` | FROZEN v1 | Profile/context/non-transfer semantics |
| `14_prom_comfort_adherence.md` | FROZEN v1 | PROM/comfort/fit/satisfaction/adherence |
| `15_pressure_acquisition_qualification.md` | FROZEN methodology v1 | Device/protocol qualification method |
| `16_geometry_authoring_contract.md` | FROZEN v1 | Semantic authoring/replay/mirror/inspection |
| `17_workflow_preset_macro.md` | FROZEN v1 | Exact reusable knowledge/workflow definitions |
| `18_numerical_qualification_registry.md` | FROZEN v1 | Numeric authority/tolerance/default governance |
| `19_project_schema_v0_2_changeset.md` | APPROVED / NOT MATERIALIZED | Additive future schema direction |
| `20_input_scan_reference_data.md` | FROZEN v1 | Source/capture/processing/registration lineage |
| `21_product_workflow_interaction.md` | FROZEN v1 | End-to-end interaction/state semantics |
| `22_interchange_manufacturing_handoff.md` | FROZEN v1 | Format capability/loss/handoff/package semantics |
| `23_realtime_performance_contract.md` | FROZEN doctrine v1 | Performance measurement/qualification; budgets OPEN |
| `25_intended_use_risk_privacy_security_boundary.md` | CANONICAL boundary v1 | Intended-use/risk/privacy/security; final classification OPEN |

---

## 4. Engineering / historical material — non-authoritative

| File | Status | Rule |
|---|---|---|
| `03_geometry_operation_model.md` | historical | pre-freeze engine hypothesis |
| `04_base_template.md` | ENGINEERING CANDIDATE / QUALIFICATION FIXTURE | topology/counts/OpenSubdiv assumptions are not product requirements |
| `05_parametric_orthosis_geometry.md` | PROVISIONAL ENGINEERING MATHEMATICAL REFERENCE | formulas/directions/sample values are PoC hypotheses |
| `CAD_ENGINE_CAPABILITY_SPEC.md` | historical | current architecture authority is scorecard |
| `CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md` | historical checkpoint | no current selection authority |
| `BIOMECHE_CAD_FUNCTIONAL_SPEC.md` | historical functional baseline | v2 is current |

There is intentionally no `07_*`; the numbering gap is historical and has no product meaning.

---

## 5. Acceptance / visual traceability

Canonical coordination:

```text
TRACEABILITY_MATRIX.md                                 v0.8
validation/24_validation_verification_master_plan.md   v1
validation/P0_DOCUMENTATION_CLOSURE_ACCEPTANCE_ADDENDUM_2026-08-16.md
ux/mockups/v1/manifest.md
ux/VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md
```

Current namespaces include:

```text
SCHEMA-* OFF-* CE-* ARCH-* HEEL-* PROF-* PROM-* MAT-* AQ-* MAN-*
BINT-* RPT-* PAQ-* GAUTH-* WFLOW-* NREG-* AUTH-C* INPUT-* UX-*
XCHG-* PERF-* VV-* REG-* VIS-* XACC-* HG-01..15
```

Browser/a11y corrective items registered for implementation:

```text
VIS-A11Y-01 meaningful quantitative SVG alternative/name
VIS-A11Y-02 semantic controls for interactive viewport tools
VIS-A11Y-03 explicit tested focus-visible design rule
```

---

## 6. Canonical visual package

```text
docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
docs/ux/mockups/v1/README.md
docs/ux/mockups/v1/manifest.md
docs/ux/mockups/v1/biomeche-cad-mockups-v1.html
docs/ux/VISUAL_REFERENCE_CROSS_DOCUMENT_AUDIT_2026-08-16.md
docs/ux/VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md
docs/ux/mockups/v1/rendered/README.md
```

Status:

```text
VIS-01             DONE
VIS-02             DONE
VIS-03 source      DONE
VIS-04 source      DONE
VIS-03R-RUN        DONE — 14/14 captures executed
VIS-04R            DONE — Chromium audit / PASS WITH corrective items
VIS-03R-ARCHIVE    OPEN — PNG repository packaging only
```

Authority rule:

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
HTML SOURCE           = CANONICAL VISUAL / INTERACTION SOURCE
PNG                    = RENDERED REFERENCE ARTIFACT
```

---

## 7. Bibliography / current-source state

`BIBLIOGRAPHY.md` is the single canonical source authority and now contains stable IDs for the 2025/2026 additions, including current 3MF/AMF/data-package standards, MDR/MDCG/GDPR references, ISO 14971/13485, ISO 9241-210, IEC 62366-1, FDA HFE 2026 and WCAG/WCAG2ICT.

`research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md` and `research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md` remain research/audit ledgers, not parallel bibliography authorities.

---

## 8. Architecture evaluation — ready / no winner

Still valid:

```text
GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
HG-01..HG-15
Q0..Q7
NO WINNER
```

If engineering work resumes, start from Q0. Do not restart generic library research.

---

## 9. Remaining work

Only one visual maintenance item remains:

```text
store/recreate the 14 PNG binaries under docs/ux/mockups/v1/rendered/
record source blob/browser/viewport/hash/file size in the manifest
```

This is archival packaging, not a semantic or architecture-entry blocker.

Independent future qualification streams remain:

```text
geometry-engine Q0..Q7
Project Schema v0.2 implementation when authorized
physical pressure/material/manufacturing qualification
formal regulatory/QMS/privacy/security deployment assessment
actual UI implementation of VIS-A11Y-01..03
```
