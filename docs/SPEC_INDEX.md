# BiomechE-CAD — Specification Index

**Status:** **CANONICAL DOCUMENT MAP**  
**Updated:** 2026-08-16  
**Current phase:** **P0 written documentation complete + canonical visual source baseline v1 complete**. Render/browser captures remain pending; geometry-engine qualification remains preserved with no winner selected.

Markdown under `docs/` is the canonical documentation source.

---

## 1. Resume order

Read in this order before substantial work:

1. [RESUME_HERE.md](RESUME_HERE.md) — current mission, frozen state and exact restart point.
2. [P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md](P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md) — closure/visual plan and current status.
3. [validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md](validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md) — **written closure GO / 0 blockers**.
4. [ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md](ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md) — **canonical visual/interaction reference v1**.
5. [ux/mockups/v1/manifest.md](ux/mockups/v1/manifest.md) — M01..M14 requirement mapping.
6. [ux/VISUAL_REFERENCE_CROSS_DOCUMENT_AUDIT_2026-08-16.md](ux/VISUAL_REFERENCE_CROSS_DOCUMENT_AUDIT_2026-08-16.md) — source-level visual audit; render capture pending.
7. [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) — **canonical product scope**.
8. [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) — **canonical v0.7**.
9. [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) — **FROZEN v1**.
10. [spec/02_project_schema.md](spec/02_project_schema.md) — current persisted semantic baseline v0.1.
11. [spec/06_corrective_elements.md](spec/06_corrective_elements.md) — **FROZEN v1**.
12. [spec/08_material_stiffness.md](spec/08_material_stiffness.md) — **FROZEN v1**.
13. [spec/09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) — **FROZEN v1**.
14. [spec/10_manufacturing.md](spec/10_manufacturing.md) — **FROZEN v1**.
15. [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) — **FROZEN v1**.
16. [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) — **FROZEN v1**.
17. [spec/13_use_case_profiles.md](spec/13_use_case_profiles.md) — **FROZEN v1**.
18. [spec/14_prom_comfort_adherence.md](spec/14_prom_comfort_adherence.md) — **FROZEN v1**.
19. [spec/15_pressure_acquisition_qualification.md](spec/15_pressure_acquisition_qualification.md) — **FROZEN methodology v1**.
20. [spec/16_geometry_authoring_contract.md](spec/16_geometry_authoring_contract.md) — **FROZEN v1**.
21. [spec/17_workflow_preset_macro.md](spec/17_workflow_preset_macro.md) — **FROZEN v1**.
22. [spec/18_numerical_qualification_registry.md](spec/18_numerical_qualification_registry.md) — **FROZEN v1**.
23. [spec/19_project_schema_v0_2_changeset.md](spec/19_project_schema_v0_2_changeset.md) — **APPROVED / NOT MATERIALIZED**.
24. [spec/20_input_scan_reference_data.md](spec/20_input_scan_reference_data.md) — **FROZEN v1**.
25. [spec/21_product_workflow_interaction.md](spec/21_product_workflow_interaction.md) — **FROZEN v1**.
26. [spec/22_interchange_manufacturing_handoff.md](spec/22_interchange_manufacturing_handoff.md) — **FROZEN v1**.
27. [spec/23_realtime_performance_contract.md](spec/23_realtime_performance_contract.md) — **FROZEN doctrine v1; budgets OPEN**.
28. [validation/24_validation_verification_master_plan.md](validation/24_validation_verification_master_plan.md) — **CANONICAL V&V v1**.
29. [spec/25_intended_use_risk_privacy_security_boundary.md](spec/25_intended_use_risk_privacy_security_boundary.md) — **CANONICAL boundary v1; regulatory classification OPEN**.
30. [validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md](validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md) — frozen `AUTH-C01..C22`.
31. [validation/P0_DOCUMENTATION_CLOSURE_ACCEPTANCE_ADDENDUM_2026-08-16.md](validation/P0_DOCUMENTATION_CLOSURE_ACCEPTANCE_ADDENDUM_2026-08-16.md) — post-authoring namespace registration.
32. [research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md](research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md) — current 2025/2026 source verification pending bibliography-ID normalization.
33. [research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md](research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md) — human-factors/accessibility evidence for visual baseline.
34. [research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md](research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md) — **no winner**.
35. [validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md](validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md) — Q0..Q7 preserved.
36. [DECISIONS.md](DECISIONS.md)
37. [TECHNICAL_DEBT.md](TECHNICAL_DEBT.md)
38. [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md)
39. [NEXT_CHAT_PROMPT.md](NEXT_CHAT_PROMPT.md)

`spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` remains historical/audit material and must not be mistaken for v2.

---

## 2. Current work order

```text
FUNCTIONAL / SCIENTIFIC PRODUCT BASELINE              DONE
P0 WRITTEN DOCUMENTATION                              COMPLETE / GO / 0 blockers
P0 VISUAL BRIEF                                       DONE
M01..M14 NAVIGABLE VISUAL SOURCE                      DONE
REQUIREMENT ↔ SCREEN TRACEABILITY                     DONE
VISUAL SOURCE-LEVEL CROSS-DOC AUDIT                   DONE / 0 blockers
RENDERED PNG/BROWSER GOLDENS                          PENDING VIS-03R/VIS-04R
CURRENT 2025/2026 SOURCE VERIFICATION                 DONE supplement
CANONICAL BIBLIOGRAPHY STABLE-ID NORMALIZATION        MAINTENANCE TODO
PROJECT SCHEMA v0.2                                   APPROVED / NOT MATERIALIZED
GEOMETRY ENGINE SCORECARD + Q0..Q7 PLAN               READY / NO WINNER
GEOMETRY ENGINE EXECUTION / FINAL SELECTION           DEFERRED UNTIL REPRIORITIZED
CI TD-CI-001                                           DEFERRED / NON-BLOCKING
```

---

## 3. Canonical / frozen product specifications

| File | Status | Purpose |
|---|---|---|
| `BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | **CANONICAL v2** | Product scope / P0-P2 |
| `01_coordinate_registration.md` | **FROZEN v1** | Frames, laterality, transforms, registration |
| `02_project_schema.md` | CANONICAL ACTIVE v0.1 | Current persisted semantic baseline |
| `06_corrective_elements.md` | **FROZEN v1** | Corrective/offloading prescription semantics |
| `08_material_stiffness.md` | **FROZEN v1** | Material/mechanical-dose semantics |
| `09_analysis_qc_dfm.md` | **FROZEN v1** | Outcome, inspection, QC and DFM semantics |
| `10_manufacturing.md` | **FROZEN v1** | Manufacturing/run/artifact/physical-part lifecycle |
| `11_biomeche_integration.md` | **FROZEN v1** | BiomechE quantitative integration |
| `12_reporting_traceability.md` | **FROZEN v1** | Immutable reporting/source manifests |
| `13_use_case_profiles.md` | **FROZEN v1** | Profile/context/non-transfer semantics |
| `14_prom_comfort_adherence.md` | **FROZEN v1** | PROM/comfort/fit/satisfaction/adherence |
| `15_pressure_acquisition_qualification.md` | **FROZEN methodology v1** | Device/protocol qualification method |
| `16_geometry_authoring_contract.md` | **FROZEN v1** | Semantic authoring/replay/mirror/inspection |
| `17_workflow_preset_macro.md` | **FROZEN v1** | Exact reusable knowledge/workflow definitions |
| `18_numerical_qualification_registry.md` | **FROZEN v1** | Numeric authority/tolerance/default governance |
| `19_project_schema_v0_2_changeset.md` | **APPROVED / NOT MATERIALIZED** | Additive future schema direction |
| `20_input_scan_reference_data.md` | **FROZEN v1** | Source/capture/processing/registration lineage |
| `21_product_workflow_interaction.md` | **FROZEN v1** | End-to-end interaction/state semantics |
| `22_interchange_manufacturing_handoff.md` | **FROZEN v1** | Format capability/loss/handoff/package semantics |
| `23_realtime_performance_contract.md` | **FROZEN doctrine v1** | Performance measurement/qualification; budgets OPEN |
| `25_intended_use_risk_privacy_security_boundary.md` | **CANONICAL boundary v1** | Intended-use/risk/privacy/security; final classification OPEN |

---

## 4. Engineering / historical material — non-authoritative

| File | Status | Rule |
|---|---|---|
| `03_geometry_operation_model.md` | historical | pre-freeze OpenSubdiv-first hypothesis |
| `04_base_template.md` | **ENGINEERING CANDIDATE / QUALIFICATION FIXTURE** | topology/counts/OpenSubdiv assumptions are not product requirements |
| `05_parametric_orthosis_geometry.md` | **PROVISIONAL ENGINEERING MATHEMATICAL REFERENCE** | formulas/directions/sample values are PoC hypotheses |
| `CAD_ENGINE_CAPABILITY_SPEC.md` | historical | current architecture authority is scorecard |
| `CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md` | historical checkpoint | no current selection authority |
| `BIOMECHE_CAD_FUNCTIONAL_SPEC.md` | historical functional baseline | v2 is current |

There is intentionally no `07_*`; the numbering gap is historical and has no product meaning.

---

## 5. Acceptance / V&V / traceability

Canonical coordination:

```text
TRACEABILITY_MATRIX.md                         v0.7
validation/24_validation_verification_master_plan.md   v1
validation/P0_DOCUMENTATION_CLOSURE_ACCEPTANCE_ADDENDUM_2026-08-16.md
```

Current namespaces include:

```text
SCHEMA-* OFF-* CE-* ARCH-* HEEL-* PROF-* PROM-* MAT-* AQ-* MAN-*
BINT-* RPT-* PAQ-* GAUTH-* WFLOW-* NREG-* AUTH-C* INPUT-* UX-*
XCHG-* PERF-* VV-* REG-* VIS-* XACC-* HG-01..15
```

A registered acceptance ID means a test specification exists; it does not claim current CI execution.

---

## 6. Canonical visual package

Visual authority:

```text
docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
docs/ux/mockups/v1/README.md
docs/ux/mockups/v1/manifest.md
docs/ux/mockups/v1/biomeche-cad-mockups-v1.html
```

Canonical screens:

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
M14 Responsive / compact reference
```

Status:

```text
VIS-01   DONE — design/visual brief
VIS-02   DONE — navigable source M01..M14
VIS-03   DONE — editable/source archive
VIS-04   DONE — source-level requirement mapping/audit
VIS-03R  PENDING — rendered image archive
VIS-04R  PENDING — browser/pixel/accessibility review
```

Authority rule:

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
MOCKUP/HTML            = VISUAL / INTERACTION REFERENCE
```

---

## 7. Research / bibliography

The canonical bibliography remains `BIBLIOGRAPHY.md`.

Current-source verification performed during closure is preserved in:

```text
research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md
research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md
```

New verified 2025/2026 sources still needing stable IDs in `BIBLIOGRAPHY.md` include current 3MF/AMF/AM data-package standards, MDR/MDCG/GDPR sources, ISO 14971/13485 and visual/human-factors sources (ISO 9241-210, IEC 62366-1, FDA HFE, WCAG 2.2).

This normalization is maintenance only; it must not change frozen requirement semantics.

---

## 8. Architecture evaluation — preserved

Still valid:

```text
GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
HG-01..HG-15
Q0..Q7
NO WINNER
```

No visual mockup or historical engineering file selects a geometry engine.

If/when engineering work resumes, start from Q0 and use the frozen product + visual contracts as qualification inputs.

---

## 9. Physical qualification streams — separate

Still pending external/physical evidence:

```text
FM12050 / pressure-hardware qualification
material/coupon qualification
manufacturing process qualification
physical-part dimensional/material/QC qualification
```

Written-spec freeze does not imply physical qualification.

---

## 10. Exact remaining tasks

### Documentation maintenance

1. normalize new 2025/2026 official sources into stable IDs in `BIBLIOGRAPHY.md`;
2. optionally consolidate closure/visual decisions in `DECISIONS.md`.

### Visual render evidence

When browser/render tooling is available:

```text
capture M01..M13 at 1440×960
capture M14 at 1024×768
include dark M07/M10 captures
verify runtime/console behavior
inspect clipping/overflow/density/status readability
measure contrast/accessibility where required
archive captures under docs/ux/mockups/v1/rendered/
record hashes/browser/version in manifest
rerun VIS-04R audit
```

### Engineering

Resume geometry-engine Q0 only when the project owner chooses to switch from documentation/visual maintenance to architecture execution.
