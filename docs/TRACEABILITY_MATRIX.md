# BiomechE-CAD — Requirement Traceability Matrix

**Status:** **CANONICAL TRACEABILITY BASELINE v0.11**  
**Date:** 2026-08-17  
**Functional authority:** `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`  
**V&V authority:** `validation/24_validation_verification_master_plan.md`  
**V1 visual evidence:** `ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md` + `ux/mockups/v1/manifest.md`  
**V2 active aesthetic direction:** `ux/BIOMECHE_CAD_VISUAL_DIRECTION_V2_SURFACE_CAD_2026-08-17.md`  
**Bibliographic authority:** `BIBLIOGRAPHY.md` — normalized 2026-08-16  
**Architecture qualification:** **Q0 READY / PARKED DURING V2 VISUAL REFINEMENT**  
**CI note:** `TD-CI-001` remains deferred/non-blocking.

---

## 1. Authority / status map

| Requirement family | Status | Canonical owner | Acceptance / qualification | Remaining |
|---|---|---|---|---|
| Product scope | FROZEN | `BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | cross-domain | implementation |
| Project/revision/provenance | CANONICAL v0.1 | `02_project_schema.md` | `SCHEMA-*`, `XACC-*` | v0.2 materialization |
| Schema v0.2 | APPROVED / NOT MATERIALIZED | `19_project_schema_v0_2_changeset.md` | change-set review | explicit future task |
| Coordinates/laterality/registration | FROZEN v1 | `01_coordinate_registration.md` | `GAUTH-*`, `INPUT-*` | implementation qualification |
| Input/scan/reference lineage | FROZEN v1 | `20_input_scan_reference_data.md` | `INPUT-001..020` | importer/runtime evidence |
| Geometry authoring semantics | FROZEN v1 | `16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C01..C14` | engine qualification |
| Corrective/offloading | FROZEN v1 | `06_corrective_elements.md` + `16` | `CE-*`, `OFF-*`, `AUTH-C04/C05` | measured outcome by profile |
| Materials/mechanics | FROZEN v1 / QUALIFY physical | `08_material_stiffness.md` | `MAT-*` | physical/process qualification |
| Analysis/QC/DFM | FROZEN v1 | `09_analysis_qc_dfm.md` | `AQ-*` | profile/process evidence |
| Manufacturing lifecycle | FROZEN v1 / QUALIFY physical | `10_manufacturing.md` | `MAN-*` | production qualification |
| BiomechE integration | FROZEN v1 | `11_biomeche_integration.md` | `BINT-*` | upstream contract monitoring |
| Reporting/provenance | FROZEN v1 | `12_reporting_traceability.md` | `RPT-*` | implementation/signing/archive later |
| Use-case profiles | FROZEN v1 | `13_use_case_profiles.md` | `PROF-*` | evidence-library maintenance |
| PROM/comfort/adherence | FROZEN v1 | `14_prom_comfort_adherence.md` | `PROM-*` | exact licensed instruments |
| Pressure acquisition qualification | FROZEN method / QUALIFY hardware | `15_pressure_acquisition_qualification.md` | `PAQ-*` | physical platform qualification |
| Workflow/preset/macro | FROZEN v1 | `17_workflow_preset_macro.md` | `WFLOW-*`, `AUTH-C15..18` | runtime materialization |
| Numerical governance | FROZEN v1 | `18_numerical_qualification_registry.md` | `NREG-*`, `AUTH-C19..22` | machine-readable registry later |
| Product interaction | FROZEN v1 | `21_product_workflow_interaction.md` | `UX-*` | executable UI |
| Interchange/handoff | FROZEN v1 | `22_interchange_manufacturing_handoff.md` | `XCHG-*` | exporter/importer qualification |
| Performance doctrine | FROZEN doctrine / budgets OPEN | `23_realtime_performance_contract.md` | `PERF-*` | `ARCH-PERF-*` later |
| V&V governance | CANONICAL v1 | `validation/24_validation_verification_master_plan.md` | `VV-*` | executable evidence grows with product |
| Intended use/risk/privacy/security | CANONICAL / classification OPEN | `25_intended_use_risk_privacy_security_boundary.md` | `REG-*` | formal deployment/regulatory work |
| Bibliography | CANONICAL / NORMALIZED | `BIBLIOGRAPHY.md` | stable IDs | maintenance only |
| Visual V1 baseline | CANONICAL FUNCTIONAL VISUAL EVIDENCE / BROWSER AUDITED / REPRODUCIBLE | `ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md` + `ux/mockups/v1/rendered/render_reference.py` | `VIS-*` + browser audit + generated SHA-256 manifest contract | actual UI implementation / optional PNG review cache |
| Visual V2 aesthetic/workspace | **ACTIVE / NOT FROZEN** | `ux/BIOMECHE_CAD_VISUAL_DIRECTION_V2_SURFACE_CAD_2026-08-17.md` + `ux/mockups/v2/README.md` | explicit per-screen user approval | V2-S01 approval then S02..S05 |
| Geometry engine | **Q0 READY / NO WINNER** | scorecard + PoC plan + `qualification/geometry-engine/q0/` | `HG-01..15`, Q0..Q7 | real native/WASM Q0 builds |

---

## 2. Historical engineering hypotheses — not product authority

```text
03_geometry_operation_model.md          HISTORICAL
04_base_template.md                     ENGINEERING CANDIDATE / QUALIFICATION FIXTURE
05_parametric_orthosis_geometry.md      PROVISIONAL ENGINEERING MATHEMATICAL REFERENCE
CAD_ENGINE_CAPABILITY_SPEC.md           HISTORICAL
CAD_ENGINE_ARCHITECTURE_STATUS_...      HISTORICAL
```

`41×17`, Catmull-Clark/OpenSubdiv realization and provisional formulas do not constrain final architecture unless independently qualified and explicitly adopted.

---

## 3. Documentation / visual gates

### V1 closure

```text
GATE-DOC-*             DONE — P0 written closure / 0 blockers
GATE-BIB-01            DONE — current-source stable-ID normalization
GATE-VIS-01            DONE — visual brief
GATE-VIS-02            DONE — M01..M14 navigable source
GATE-VIS-03            DONE — source/version archive
GATE-VIS-04            DONE — requirement↔screen mapping/source audit
GATE-VIS-03R-RUN       DONE — 14/14 browser captures executed
GATE-VIS-04R           DONE — browser/runtime/a11y audit PASS with corrective items
GATE-VIS-03R-REPRO     DONE — versioned Playwright/Chromium renderer + capture-manifest SHA-256 contract
PNG binary copies      OPTIONAL derived review cache; not a visual/documentation gate
```

Visual corrective items:

```text
VIS-A11Y-01 meaningful quantitative graphics need accessible naming/description or explicit decorative semantics + equivalent accessible numeric data
VIS-A11Y-02 interactive viewport tools must be semantic controls with keyboard/name/role/state
VIS-A11Y-03 explicit tested focus-visible treatment in light/dark
```

These are implementation obligations, not reasons to reopen frozen product semantics.

### V2 active design gate

V2 is deliberately **not frozen yet**.

```text
V2-S01 Template / Modello                 REVIEW
V2-S02 Superficie / Edit Parametrico      NOT GENERATED
V2-S03 Elementi                           NOT GENERATED
V2-S04 Scultura / Post Processing         NOT GENERATED
V2-S05 Analisi / Produzione               NOT GENERATED
```

Approval sequence:

```text
GENERATE -> REVIEW -> REVISE -> EXPLICIT USER APPROVAL -> PERSIST -> NEXT SCREEN
```

V2 changes aesthetic/workspace composition only. It cannot modify clinical, geometry-authority, manufacturing or provenance semantics.

---

## 4. Q0 architecture qualification state

Canonical Q0 evidence:

```text
qualification/geometry-engine/q0/README.md
qualification/geometry-engine/q0/candidate-lock.json
qualification/geometry-engine/q0/results/Q0_EVIDENCE_STATUS_2026-08-16.md
qualification/geometry-engine/q0/results/Q0_HARNESS_VALIDATION_2026-08-16.md
docs/research/architecture/GEOMETRY_ENGINE_Q0_EVIDENCE_UPDATE_2026-08-16.md
```

Pinned candidates:

```text
OpenSubdiv v3_7_0
  commit 9dab8a47bfbb1388ec8388fe61f5f916e6123f38

openNURBS 8.x snapshot
  commit 00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
```

BiomechE-owned Q0 infrastructure:

```text
common C++20 adapter interface       READY
common headless smoke executable     READY
OpenSubdiv smoke adapter             READY
openNURBS smoke adapter              READY
candidate CMake containment modules  READY
native/WASM evidence runner          READY
candidate lock manifest              READY
```

Harness validation actually executed:

```text
Python runner syntax                 PASS
missing-Emscripten truthfulness      PASS
common C++20 adapter contract        PASS
candidate source-shape smoke         PASS
```

Actual candidate builds:

```text
OpenSubdiv native                    NOT EXECUTED
OpenSubdiv headless/server           NOT EXECUTED
OpenSubdiv direct WASM               NOT EXECUTED
openNURBS native                     NOT EXECUTED
openNURBS headless/server            NOT EXECUTED
openNURBS direct WASM                NOT EXECUTED
```

Gate interpretation:

```text
HG-01 semantic isolation       POSITIVE STRUCTURAL EVIDENCE / BUILD CONFIRMATION PENDING
HG-10 native+server+WASM       UNKNOWN / EXECUTION REQUIRED
HG-13 license/distribution     TERMS CAPTURED / FORMAL REVIEW REQUIRED
HG-14 dependency containment   PARTIAL POSITIVE EVIDENCE / BUILD CONFIRMATION PENDING
HG-15 frozen acceptance        Q7 PENDING
```

No weighted final score and no engine winner is authorized yet.

---

## 5. Acceptance namespace registry

```text
SCHEMA-* OFF-* CE-* ARCH-* HEEL-* PROF-* PROM-* MAT-* AQ-* MAN-*
BINT-* RPT-* PAQ-* GAUTH-* WFLOW-* NREG-* AUTH-C* INPUT-* UX-*
XCHG-* PERF-* VV-* REG-* VIS-* XACC-* HG-01..15
```

A registered test ID is a specification, not a claim of CI execution.

---

## 6. Current OPEN / QUALIFY items

```text
V2-S01 explicit visual approval
V2-S02..S05 generation/approval
real Q0 candidate native/server/WASM builds
Q1..Q7 geometry/query/DFM/determinism/performance evidence
final geometry engine selection
exact topology/algorithm choices
algorithm tolerances and performance budgets
Project Schema v0.2 implementation
physical pressure/material/manufacturing qualification
formal regulatory/QMS/privacy/security deployment assessment
actual UI implementation of VIS-A11Y-01..03
optional materialized V1 PNG review copies when useful
```

---
