# BiomechE-CAD — Requirement Traceability Matrix

**Status:** **CANONICAL TRACEABILITY BASELINE v0.6**  
**Date:** 2026-08-16  
**Architecture:** kernel/runtime/storage independent  
**Functional authority:** `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`  
**Scientific authority:** `BIBLIOGRAPHY.md` + explicitly identified current-source supplements pending normalization  
**V&V authority:** `validation/24_validation_verification_master_plan.md`  
**CI note:** `TD-CI-001` remains separately deferred; semantic coverage is not defined by CI state.

---

## 1. Purpose

For every major product-requirement family this matrix records:

```text
WHY it exists
WHERE it is specified
HOW it is accepted
WHAT evidence constrains it
WHAT remains open
```

Detailed acceptance semantics remain in their owning contracts/catalogs. This file is the canonical navigation and coverage layer.

Status vocabulary:

```text
FROZEN       product meaning stable
CANONICAL    current governance/coordination authority
QUALIFY      semantic contract exists; physical/device/process evidence required
OPEN         deliberately unresolved, must not receive a hidden default
P1/P2        deliberately later
HISTORICAL   preserved audit/reference only
APPROVED     documented change-set accepted but not materialized
DEFERRED     valid planned work not current priority
```

---

## 2. Product-level traceability

| Requirement family | Status | Canonical owner | Acceptance / evidence | Remaining work |
|---|---|---|---|---|
| Product scope / vertical orthotic CAD | **FROZEN** | `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | cross-domain; EasyCAD2 + competitor + scientific evidence | none at written-scope level |
| Project/revision/provenance | CANONICAL ACTIVE v0.1 | `spec/02_project_schema.md` | `SCHEMA-*`, `XACC-*` | schema v0.2 materialization later |
| Schema v0.2 evolution | **APPROVED / NOT MATERIALIZED** | `spec/19_project_schema_v0_2_changeset.md` | change-set review | explicit implementation task only |
| Coordinate/laterality/registration | **FROZEN v1** | `spec/01_coordinate_registration.md` | `GAUTH-*`, `INPUT-*`, `XACC-*` | numerical qualification where applicable |
| Input / scan / reference data | **FROZEN v1** | `spec/20_input_scan_reference_data.md` | `INPUT-001..020`; `REF-CAD-002/003` | runtime/schema/importer implementation |
| Scan capture context | **FROZEN** | `20` + `16` | `INPUT-*`, `GAUTH-*`, `AUTH-C07/C09` | device-specific metadata/qualification adapters |
| Landmark provenance | **FROZEN** | `20` + `16` | `INPUT-010`, `GAUTH-*`, `AUTH-C10` | UI/algorithm qualification |
| Base template / outline / sizing semantics | **FROZEN semantic** | `16` | `GAUTH-*`, `UX-*` | exact representation under engine qualification |
| Base topology candidate `04` | **HISTORICAL/ENGINEERING CANDIDATE** | `spec/04_base_template.md` | future architecture fixture only | no product lock-in |
| Parametric formula reference `05` | **HISTORICAL/PROVISIONAL ENGINEERING** | `spec/05_parametric_orthosis_geometry.md` | future algorithm PoC only | no semantic/numeric authority |
| Arch authoring | **FROZEN semantic** | `16` | `ARCH-*`, `GAUTH-*`, `AUTH-C01` | engine operator qualification; defaults profile-specific/OPEN |
| Heel authoring | **FROZEN semantic** | `16` | `HEEL-*`, `GAUTH-*`, `AUTH-C02` | engine operator qualification |
| Rear/forefoot wedge/posting | **FROZEN semantic** | `16` | `GAUTH-*`, `AUTH-C03` | mirror/realization qualification |
| Corrective / offloading elements | **FROZEN v1** | `spec/06_corrective_elements.md` + `16` | `CE-001..010`, `OFF-*`, `GAUTH-*` | real outcome loop depends on qualified acquisition |
| Met-pad/reference-relative placement | **FROZEN** | `06` + `16` | `CE-*`, `AUTH-C04`; `REF-CAD-013/014` | engine query/placement qualification |
| Sculpt / local freeform | **FROZEN semantic** | `16` | `GAUTH-*`, `AUTH-C06`, `UX-013` | stable-addressing/replay PoC |
| Scan conform | **FROZEN semantic** | `16` + `20` | `GAUTH-*`, `AUTH-C07`, `INPUT-*` | spatial-query/large-scan PoC |
| Requested vs realized geometry | **FROZEN** | `16` + `18` | `GAUTH-*`, `NREG-*`, `AUTH-C08` | engine realization/inspection evidence |
| Inspection / section / distance / angle / thickness | **FROZEN semantic** | `16` + `09` | `GAUTH-*`, `AQ-*`, `AUTH-C11..13` | engine query qualification |
| Analysis / outcome / QC / DFM semantics | **FROZEN v1** | `spec/09_analysis_qc_dfm.md` | `AQ-001..010`; literature/device/manufacturing evidence | actual limits/profile evidence |
| CAD vs measured-part deviation | FROZEN semantic / **QUALIFY physical** | `09` + `10` + `16` + `18` | `AUTH-C14`, `MAN-*` | deviation PoC + process acceptance limits |
| Minimum thickness / DFM | FROZEN semantic / **QUALIFY** | `09` + `10` + `18` | `AQ-*`, `MAN-*`, `NREG-*` | algorithm and ManufacturingProfile limits |
| Material/stiffness/regional mechanics | **FROZEN v1 / QUALIFY physical** | `spec/08_material_stiffness.md` | `MAT-001..018`; `REF-CAD-094..105`; ISO material tests | actual material/process profiles |
| Manufacturing run/artifact/physical part | **FROZEN v1 / QUALIFY physical** | `spec/10_manufacturing.md` | `MAN-001..018`, `XACC-*` | production-body/process/part qualification |
| Interchange / manufacturing handoff | **FROZEN v1** | `spec/22_interchange_manufacturing_handoff.md` | `XCHG-001..018`; ISO/3MF/AMF current-source evidence | implementation capability profiles/conformance tests |
| Workflow preset/macro/history | **FROZEN v1** | `spec/17_workflow_preset_macro.md` | `WFLOW-*`, `AUTH-C15..18` | schema/UI materialization |
| Product workflow / interaction | **FROZEN v1** | `spec/21_product_workflow_interaction.md` | `UX-001..022` | visual reference + executable UI tests |
| Numerical/tolerance governance | **FROZEN v1** | `spec/18_numerical_qualification_registry.md` | `NREG-*`, `AUTH-C19..22` | machine-readable registry later; additive perf terminology harmonization candidate |
| Realtime/performance doctrine | **FROZEN doctrine / BUDGETS OPEN** | `spec/23_realtime_performance_contract.md` | `PERF-001..016` | define/qualify `ARCH-PERF-*` budgets from representative workloads |
| BiomechE quantitative integration | **FROZEN v1** | `spec/11_biomeche_integration.md` | `BINT-*` | track upstream contract changes |
| Pressure acquisition qualification | FROZEN method / **QUALIFY hardware** | `spec/15_pressure_acquisition_qualification.md` | `PAQ-*`; `REF-CAD-108..110` | first physical FM12050 qualification |
| Pressure-informed outcome loop | FROZEN semantics / QUALIFY acquisition | `06` + `09` + `11` + `15` | `BINT-*`, `CE/OFF-*`, `AQ-*` | qualified compatible datasets |
| Measured vs predicted separation | **FROZEN** | Functional v2 + schema + `09` | `SCHEMA-*`, `AQ-*`, `XACC-*` | prediction models later |
| Indication/use-case profiles | **FROZEN v1** | `spec/13_use_case_profiles.md` | `PROF-001..014` | future profile library/evidence updates versioned |
| PROM/comfort/fit/adherence | **FROZEN v1** | `spec/14_prom_comfort_adherence.md` | `PROM-001..020`; COSMIN/FDA + literature | exact instrument/licensing decisions per deployment |
| Reporting / traceability | **FROZEN v1** | `spec/12_reporting_traceability.md` | `RPT-*` | renderer/signing/archive implementation |
| Intended-use / risk / privacy / security boundary | **CANONICAL v1 / REGULATORY CLASSIFICATION OPEN** | `spec/25_intended_use_risk_privacy_security_boundary.md` | `REG-001..016`; MDR/GDPR/ISO current-source baseline | formal intended-purpose/classification/QMS/DPIA/security decisions |
| Validation & verification governance | **CANONICAL v1** | `validation/24_validation_verification_master_plan.md` | `VV-001..018` | executable evidence grows with implementation |
| Visual reference / canonical mockups | **NEXT** | future `docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md` | `VIS-*` + `UX-*` mapping | VIS-01..04 |
| Cloud/offline sync | P1/P2 | future sync spec | future | conflict/sync semantics open |
| Geometry kernel/runtime | **DEFERRED — SCORECARD/PLAN READY, NO WINNER** | geometry scorecard + PoC plan | `HG-01..15`, `AUTH-C01..C22`, Q0..Q7 | resume after VIS closure or owner reprioritization |

---

## 3. Frozen evidence-derived product rules

### TRC-EVID-001 — Capture context survives into design provenance
A scan influencing geometry preserves capture condition; `UNKNOWN` remains valid and silent assumptions are forbidden (`REF-CAD-002`, `REF-CAD-003`).

### TRC-EVID-002 — Landmark provenance is semantic state
Landmarks include source/method/frame/author-or-algorithm/quality/review semantics, not coordinates only.

### TRC-EVID-003 — Placement is typed
Landmark-relative metric placement, normalized placement, intrinsic/surface references, ROI/pressure-relative placement and custom registered references are distinct semantics.

### TRC-EVID-004 — Geometry and mechanical dose are separate
Height/depth/angle/extent do not substitute for material, stiffness, cushioning, lattice/structure or service-aged mechanics.

### TRC-EVID-005 — Offloading is redistribution
Target ROI, safety ring/adjacent and remote regions remain visible in outcome evaluation.

### TRC-EVID-006 — Manufacturing acceptance is profile-owned
No project-wide hidden dimensional tolerance is allowed.

### TRC-EVID-007 — Workflow knowledge is versioned product infrastructure
Definitions resolve exact identity/version/hash and preserve historical expansion.

### TRC-EVID-008 — Original source is never replaced by processed convenience data
Original/processed/registered/derived assets retain explicit lineage.

### TRC-EVID-009 — File format is not semantic authority
STL/3MF/AMF/other carriers have explicit capability and loss semantics; product/manufacturing manifests preserve missing context.

### TRC-EVID-010 — Performance is evidence-led
`MEASURED != QUALIFIED`; budgets remain OPEN until an explicit engineering profile owns them.

### TRC-EVID-011 — Regulatory status follows intended purpose
Capability or patient-specific geometry alone does not establish software/device/custom-made regulatory classification.

---

## 4. Documentation closure gates

```text
GATE-DOC-01  traceability baseline                                  DONE v0.6
GATE-DOC-02  Geometry Authoring Contract                            DONE — FROZEN v1
GATE-DOC-03  Workflow/Preset/Macro Contract                         DONE — FROZEN v1
GATE-DOC-04  Numerical/Qualification Registry                       DONE — FROZEN v1
GATE-DOC-05  P0 Authoring Acceptance Catalog                        DONE — FROZEN v1
GATE-DOC-06  Project Schema v0.2 change-set                         DONE — APPROVED / NOT MATERIALIZED
GATE-DOC-07  P0 authoring cross-document audit                      DONE — 0 blockers
GATE-DOC-08  geometry-engine scorecard                              DONE — no winner
GATE-DOC-09  geometry-engine qualification plan                     DONE — execution deferred
GATE-DOC-10  DOC-00 closure inventory                               DONE
GATE-DOC-11  DOC-01..06 ACTIVE-v0 product specs                     DONE — FROZEN v1
GATE-DOC-12  DOC-07 engineering-hypothesis disposition              DONE
GATE-DOC-13  DOC-08 Input/Scan/Reference Contract                   DONE — FROZEN v1
GATE-DOC-14  DOC-09 Product Workflow/Interaction                    DONE — FROZEN v1
GATE-DOC-15  DOC-10 Interchange/Handoff                             DONE — FROZEN v1
GATE-DOC-16  DOC-11 Realtime/Performance                            DONE — doctrine frozen, budgets OPEN
GATE-DOC-17  DOC-12 V&V Master Plan                                 DONE — CANONICAL v1
GATE-DOC-18  DOC-13 Intended-use/Risk/Privacy/Security boundary     DONE — regulatory decision OPEN
GATE-DOC-19  DOC-14 final cross-document audit                      DONE — 0 blockers / WRITTEN CLOSURE GO
GATE-VIS-01  visual reference brief                                 NEXT
GATE-VIS-02  canonical mockup set                                   PENDING
GATE-VIS-03  visual package versioning/archive                      PENDING
GATE-VIS-04  requirement ↔ screen traceability                      PENDING
```

`TD-CI-001` is not part of documentation/visual closure gates.

---

## 5. Current acceptance namespace registry

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
XACC-* cross-domain scenarios
HG-01..HG-15 architecture gates
```

The older `validation/functional_acceptance_suite.md` is retained as an active baseline and requires namespace/index synchronization through the closure addendum/master plan; its older ranges do not override the owning frozen specs.

---

## 6. Open items that are NOT documentation contradictions

```text
Project Schema v0.2 implementation
geometry engine Q0..Q7 + selection
specific geometry algorithms/topology
algorithm numerical tolerances
performance budgets
real pressure-device qualification
material/process/physical manufacturing qualification
final software MDR qualification/classification
QMS/DPIA/deployment security decisions
exact PROM licensing/selection
visual mockups
```

`OPEN` must remain visible rather than receiving guessed defaults.

---

## 7. Architecture selection rule — unchanged

When resumed:

```text
HARD GATES -> Q0..Q7 EVIDENCE -> WEIGHTED CRITERIA -> FINAL DECISION
```

A candidate fails if it requires weakening frozen product semantics. Auxiliary libraries enter only after a concrete frozen requirement + evidence demonstrates a bounded gap.

The current project priority is VIS closure, not Q0.

---

## 8. Maintenance rule

Whenever a P0 requirement changes, update:

```text
owner
acceptance IDs
evidence basis
OPEN/QUALIFY state
visual mapping when applicable
change/requalification impact
```

A requirement without an owner, acceptance direction or explicit deferral is documentation debt.
