# BiomechE-CAD — Requirement Traceability Matrix

**Status:** **CANONICAL TRACEABILITY BASELINE v0.7**  
**Date:** 2026-08-16  
**Functional authority:** `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`  
**V&V authority:** `validation/24_validation_verification_master_plan.md`  
**Visual authority:** `ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md` + `ux/mockups/v1/manifest.md`  
**CI note:** `TD-CI-001` remains deferred/non-blocking.

---

## 1. Purpose

For every major product family this matrix records:

```text
WHY it exists
WHERE it is specified
HOW it is accepted
WHICH evidence constrains it
WHAT remains open
WHICH visual screen(s) represent it
```

Status vocabulary:

```text
FROZEN       product meaning stable
CANONICAL    current governance/coordination authority
QUALIFY      contract exists; execution/physical evidence required
OPEN         deliberately unresolved
HISTORICAL   preserved but non-authoritative
APPROVED     change-set accepted but not materialized
DEFERRED     planned but not current gate
```

---

## 2. Product-level traceability

| Requirement family | Status | Owner | Acceptance / evidence | Visual | Remaining |
|---|---|---|---|---|---|
| Product scope | **FROZEN** | `BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | cross-domain | M01..M14 | implementation |
| Project/revision/provenance | CANONICAL v0.1 | `02_project_schema.md` | `SCHEMA-*`, `XACC-*` | M01,M12,M13 | v0.2 materialization |
| Schema v0.2 evolution | **APPROVED / NOT MATERIALIZED** | `19_project_schema_v0_2_changeset.md` | change-set review | n/a | explicit future task |
| Coordinates/laterality/registration | **FROZEN v1** | `01_coordinate_registration.md` | `GAUTH-*`, `INPUT-*` | M02,M03,M14 | implementation qualification |
| Input/scan/reference lineage | **FROZEN v1** | `20_input_scan_reference_data.md` | `INPUT-001..020`, scan reviews | M02,M03 | importer/runtime evidence |
| Landmark provenance | **FROZEN** | `20` + `16` | `INPUT-010`, `AUTH-C10` | M03 | algorithm/UI evidence |
| Base/template semantics | **FROZEN semantic** | `16` + `17` | `GAUTH-*`, `UX-*` | M04 | engine realization |
| `04` topology candidate | **HISTORICAL/ENGINEERING** | `04_base_template.md` | PoC fixture only | deliberately hidden | no product lock-in |
| `05` formulas | **HISTORICAL/PROVISIONAL ENGINEERING** | `05_parametric_orthosis_geometry.md` | algorithm PoC only | semantic UI only | formulas/tolerances open |
| Parametric authoring | **FROZEN semantic** | `16` | `GAUTH-*`, `AUTH-C01..03/C08` | M05 | engine qualification |
| Corrective/offloading elements | **FROZEN v1** | `06_corrective_elements.md` + `16` | `CE-*`, `OFF-*`, `AUTH-C04/C05` | M06 | outcome evidence by profile |
| Sculpt/local freeform | **FROZEN semantic** | `16` | `AUTH-C06`, `UX-013` | M07 | replay/performance PoC |
| Material/mechanical prescription | **FROZEN v1 / QUALIFY physical** | `08_material_stiffness.md` | `MAT-001..018` + material evidence | M08 | material/process qualification |
| Analysis/outcome/QC/DFM | **FROZEN v1** | `09_analysis_qc_dfm.md` | `AQ-001..010` | M09,M10,M11 | profile limits/physical evidence |
| BiomechE integration | **FROZEN v1** | `11_biomeche_integration.md` | `BINT-*` | M10 | upstream contract monitoring |
| Pressure acquisition qualification | FROZEN method / **QUALIFY hardware** | `15_pressure_acquisition_qualification.md` | `PAQ-*` | M02,M10 | physical platform qualification |
| Use-case profiles | **FROZEN v1** | `13_use_case_profiles.md` | `PROF-001..014` | M01,M06,M10 | versioned evidence updates |
| PROM/comfort/fit/adherence | **FROZEN v1** | `14_prom_comfort_adherence.md` | `PROM-001..020` | M13 | exact instrument/license choices |
| Workflow/preset/macro | **FROZEN v1** | `17_workflow_preset_macro.md` | `WFLOW-*`, `AUTH-C15..18` | M04,M05,M06,M12 | runtime/schema materialization |
| Numerical governance | **FROZEN v1** | `18_numerical_qualification_registry.md` | `NREG-*`, `AUTH-C19..22` | M05,M09,M10,M11 | machine-readable registry later |
| Product interaction/state | **FROZEN v1** | `21_product_workflow_interaction.md` | `UX-001..022` | M01..M14 | executable UI validation |
| Interchange/handoff | **FROZEN v1** | `22_interchange_manufacturing_handoff.md` | `XCHG-001..018` | M11,M12,M13 | exporter/importer conformance |
| Manufacturing lifecycle | **FROZEN v1 / QUALIFY physical** | `10_manufacturing.md` | `MAN-001..018` | M11,M12,M13 | process/part qualification |
| Reporting/traceability | **FROZEN v1** | `12_reporting_traceability.md` | `RPT-*` | M12,M13 | renderer/signing/archive implementation |
| Performance doctrine | **FROZEN doctrine / budgets OPEN** | `23_realtime_performance_contract.md` | `PERF-001..016` | M07,M10,M14 | `ARCH-PERF-*` profiles later |
| V&V governance | **CANONICAL v1** | `validation/24_validation_verification_master_plan.md` | `VV-001..018` | all | executable evidence grows with product |
| Intended use/risk/privacy/security boundary | **CANONICAL / classification OPEN** | `25_intended_use_risk_privacy_security_boundary.md` | `REG-001..016` | M01,M11,M12,M13 | formal regulatory/QMS/deployment decisions |
| Canonical visual reference | **CANONICAL SOURCE v1** | `ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md` | `VIS-001..020`, visual audit | M01..M14 | rendered/browser goldens pending |
| Geometry engine | **DEFERRED / NO WINNER** | scorecard + Q0..Q7 plan | `HG-01..15`, Q0..Q7 | none selects engine | architecture qualification |

---

## 3. Evidence-derived frozen rules

```text
TRC-EVID-001 capture context survives into design provenance
TRC-EVID-002 landmark provenance is semantic state
TRC-EVID-003 placement is typed/anatomical/reference-based
TRC-EVID-004 geometry and mechanical dose remain separate
TRC-EVID-005 offloading outcome includes redistribution
TRC-EVID-006 manufacturing acceptance is profile-owned
TRC-EVID-007 workflow knowledge is exact/versioned
TRC-EVID-008 original source is not replaced by processed convenience data
TRC-EVID-009 file format is not semantic authority
TRC-EVID-010 performance is measured before qualification
TRC-EVID-011 regulatory status follows intended purpose/formal assessment
TRC-EVID-012 visual mockup cannot create semantic authority
```

---

## 4. Documentation / visual gates

```text
GATE-DOC-01..19     DONE — written closure / 0 blockers
GATE-VIS-01         DONE — visual brief v1
GATE-VIS-02         DONE — navigable M01..M14 HTML source
GATE-VIS-03         DONE — source/version archive
GATE-VIS-04         DONE — requirement↔screen traceability/source audit
GATE-VIS-03R        PENDING — rendered PNG archive
GATE-VIS-04R        PENDING — browser/pixel/accessibility visual review
```

`TD-CI-001` is not a documentation/visual gate.

---

## 5. Acceptance namespace registry

```text
SCHEMA-001..030
OFF-001..009
CE-001..010
ARCH-001..014
HEEL-001..015
PROF-001..014
PROM-001..020
MAT-001..018
AQ-001..010
MAN-001..018
BINT-001..018
RPT-001..018
PAQ-001..020
GAUTH-001..040
WFLOW-001..030
NREG-001..030
AUTH-C01..C22
INPUT-001..020
UX-001..022
XCHG-001..018
PERF-001..016
VV-001..018
REG-001..016
VIS-001..020
XACC-* cross-domain scenarios
HG-01..HG-15 architecture gates
```

The closure addendum registers new post-authoring namespaces without claiming current CI execution.

---

## 6. VIS mapping summary

```text
M01 case/context                         UX / PROF / INPUT / schema
M02 input/scan qualification            INPUT / UX / registration
M03 registration/landmarks              INPUT / GAUTH / UX
M04 base/template                       GAUTH / WFLOW / UX
M05 parametric authoring                GAUTH / NREG / UX
M06 corrective/offloading               CE / OFF / PROF / GAUTH
M07 sculpt                              GAUTH / PERF / UX
M08 materials                           MAT / MAN / UX
M09 inspection/QC                       AQ / GAUTH / NREG
M10 BiomechE compare                    BINT / AQ / PAQ / OFF
M11 DFM/manufacturing prep              MAN / AQ / XCHG / NREG
M12 revision/provenance/report          RPT / schema / WFLOW / UX
M13 physical part/outcome               MAN / MAT / PROM / RPT
M14 compact                             UX / VIS / human-factors evidence
```

Full mapping: `docs/ux/mockups/v1/manifest.md`.

---

## 7. Open items that are not contradictions

```text
BIBLIOGRAPHY stable-ID normalization for newly verified 2025/2026 sources
rendered M01..M14 captures + browser visual audit
Project Schema v0.2 implementation
geometry engine Q0..Q7 + selection
exact geometry algorithms/topology
algorithm tolerances
performance budgets
physical pressure/material/manufacturing qualification
formal software MDR classification/QMS/DPIA/security architecture
exact PROM licensing/selection per deployment
```

---

## 8. Architecture selection rule — unchanged

When resumed:

```text
HARD GATES -> Q0..Q7 EVIDENCE -> WEIGHTED CRITERIA -> FINAL DECISION
```

A candidate cannot win by forcing weaker frozen semantics or by matching a mockup visually.

---

## 9. Maintenance rule

Whenever a P0 requirement changes, update:

```text
owner
acceptance IDs
evidence/source role
OPEN/QUALIFY state
visual Mxx mapping
change/requalification impact
```

A requirement without owner, acceptance direction or explicit deferral is documentation debt.
