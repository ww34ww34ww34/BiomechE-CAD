# BiomechE-CAD — Requirement Traceability Matrix

**Status:** CANONICAL TRACEABILITY BASELINE v0.5  
**Date:** 2026-08-15  
**Architecture:** kernel/runtime/storage independent  
**Functional authority:** `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`  
**Scientific authority:** `BIBLIOGRAPHY.md`  
**Executable-validation note:** CI debt is tracked separately in `TECHNICAL_DEBT.md`; semantic coverage is not blocked by `TD-CI-001`.

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

Detailed acceptance semantics remain in their owning specs/catalogs. This file is the canonical navigation and coverage layer.

Status vocabulary:

```text
FROZEN       product meaning stable
ACTIVE       usable baseline; refinements possible
QUALIFY      semantic contract exists; real device/process/profile evidence required
P1/P2        deliberately later
PARKED       downstream decision intentionally postponed
APPROVED     documented change-set accepted but not yet materialized
EVALUATE     architecture candidate evaluation/qualification in progress
```

---

## 2. Product-level traceability

| Requirement family | Status | Canonical owner | Acceptance | Evidence/rationale | Remaining work |
|---|---|---|---|---|---|
| Product scope / vertical orthotic CAD | FROZEN | `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | cross-domain | EasyCAD2 + competitor + scientific evidence | none at inventory level |
| Project/revision/provenance | ACTIVE | `spec/02_project_schema.md` | `SCHEMA-*`, `XACC-*` | provenance/reproducibility doctrine | v0.2 materialization later |
| Schema v0.2 evolution | APPROVED / NOT MATERIALIZED | `spec/19_project_schema_v0_2_changeset.md` | migration/change-set review | frozen P0 authoring requirements | implementation task later |
| Coordinate/laterality/registration | FROZEN | `spec/01_coordinate_registration.md` | `XACC-*` | BiomechE/ISB/anatomical context | numeric limits profile-owned |
| Scan capture context | FROZEN | `spec/16_geometry_authoring_contract.md` + schema v0.2 change-set | `GAUTH-*`, `AUTH-C07`, `AUTH-C09` | `REF-CAD-002`, `REF-CAD-003` | schema/runtime materialization later |
| Landmark provenance | FROZEN | authoring contract + schema v0.2 change-set | `GAUTH-*`, `AUTH-C10` | `REF-CAD-002`, `REF-CAD-003`, `REF-CAD-107` | schema/UI materialization later |
| Base template / outline / sizing | FROZEN semantic | `spec/16_geometry_authoring_contract.md` | `GAUTH-*` | EasyCAD2/market baseline | exact geometry implementation under engine PoC |
| Arch authoring | FROZEN semantic | `spec/16_geometry_authoring_contract.md` | `ARCH-*`, `GAUTH-*`, `AUTH-C01` | `REF-CAD-017`, `053`, `055`, `056` | engine operator qualification; no universal numeric default |
| Heel authoring | FROZEN semantic | `spec/16_geometry_authoring_contract.md` | `HEEL-*`, `GAUTH-*`, `AUTH-C02` | `REF-CAD-018`, `058..067` | engine operator qualification; no universal cup/skive/relief dose |
| Rear/forefoot wedge/posting | FROZEN semantic | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C03` | `REF-CAD-001`, `REF-CAD-015` | engine mirror/operator qualification; defaults profile-specific |
| Corrective elements | ACTIVE + frozen authoring envelope | `spec/06_corrective_elements.md` + `16` | `CE-*`, `GAUTH-*` | EasyCAD2 + market named corrections | terminology harmonization later |
| Met-pad/reference-relative placement | FROZEN | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C04` | `REF-CAD-013`, `REF-CAD-014` | engine placement/query qualification + profile rules later |
| Offloading / accommodation | ACTIVE + frozen authoring envelope | `spec/06_corrective_elements.md` + `16` | `OFF-*`, `GAUTH-*`, `AUTH-C05` | `REF-CAD-004`, `005`, `007`, `008` | real outcome loop requires qualified acquisition |
| Sculpt / local freeform | FROZEN semantic | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C06` | EasyCAD2 + market | stable-addressing/replay PoC |
| Scan conform | FROZEN semantic | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C07` | scan/registration evidence | spatial-query/large-scan PoC; exact algorithm/tolerance later |
| Requested vs realized constrained geometry | FROZEN semantic | `16`, `18`, schema v0.2 change-set | `GAUTH-*`, `NREG-*`, `AUTH-C08` | prescription vs DFM separation | engine constraint/result PoC |
| Inspection: section/distance/angle/thickness | FROZEN semantic | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C11..13` | EasyCAD2 + market baseline | engine query qualification |
| CAD vs measured-part deviation | FROZEN semantic / QUALIFY acceptance | `16`, `10`, `18` | `AUTH-C14`, `MAN-*`, `NREG-*` | `REF-CAD-106`; ISO/ASTM 52902 | deviation PoC + process acceptance limits later |
| Minimum thickness / DFM | ACTIVE / QUALIFY | `09`, `10`, `18` | `MAN-*`, `NREG-*` | manufacturing standards/evidence | engine/adjunct PoC; value ManufacturingProfile-owned |
| Material/stiffness/regional mechanics | ACTIVE / QUALIFY | `spec/08_material_stiffness.md` | `MAT-*` | `REF-CAD-098..105` | real profiles/process testing |
| Manufacturing run/artifact/physical part | ACTIVE / QUALIFY | `spec/10_manufacturing.md` | `MAN-*`, `XACC-*` | ISO/ASTM 52901/52902/52920; ISO 17295 | production-body/handoff PoC + actual process qualification |
| Workflow preset/macro/history | FROZEN v1 | `spec/17_workflow_preset_macro.md` | `WFLOW-*`, `AUTH-C15..18` | competitor convergence | schema/UI materialization; kernel must remain workflow-independent |
| Numerical/tolerance governance | FROZEN v1 | `spec/18_numerical_qualification_registry.md` | `NREG-*`, `AUTH-C19..22` | literature + qualification standards | machine-readable registry later; engine numerical PoC now |
| BiomechE quantitative integration | FROZEN | `spec/11_biomeche_integration.md` | `BINT-*` | pinned upstream contract | follow future upstream freezes |
| Pressure acquisition qualification | FROZEN method / QUALIFY hardware | `spec/15_pressure_acquisition_qualification.md` | `PAQ-*` | `REF-CAD-108..110` | first physical FM12050 qualification |
| Pressure-informed outcome loop | ACTIVE | Functional v2 + `11` + `06` | `BINT-*`, `OFF-*` | `REF-CAD-004`, `005`, `069` | compatibility/device qualification |
| Measured vs predicted separation | FROZEN | Project Schema + Functional v2 | `SCHEMA-*`, `XACC-*` | scientific integrity | prediction models later |
| PROM/comfort/fit/adherence | ACTIVE | `spec/14_prom_comfort_adherence.md` | `PROM-*` | `REF-CAD-080..097` | exact instrument/licensing selection |
| Reporting / traceability | FROZEN | `spec/12_reporting_traceability.md` | `RPT-*` | PROV/FAIR/biomedical provenance | renderer/signing/archive later |
| Cloud/offline sync | P1/P2 | future sync spec | future | market signal | conflict/sync semantics open |
| Geometry kernel/runtime | **EVALUATE — SCORECARD v0.1 DONE / PoC NEXT** | `research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md` + frozen authoring package | hard gates `HG-01..15`, `AUTH-C01..C22`, PoC plan | candidate evidence must satisfy frozen contracts | OpenSubdiv vs ON_SubD undecided; Q0..Q7 qualification pending |

---

## 3. Evidence-derived product rules

### TRC-EVID-001 — Capture context survives into design provenance

A scan that influences geometry preserves capture condition; `UNKNOWN` is valid and silent assumption is not (`REF-CAD-002`, `REF-CAD-003`).

### TRC-EVID-002 — Landmark provenance is semantic state

A landmark includes source/method/frame/author-or-algorithm/quality/review semantics, not only coordinates.

### TRC-EVID-003 — Placement is typed

Supported semantics include landmark-relative metric placement, normalized placement, intrinsic coordinates, ROI/pressure-relative placement and custom registered references. Different references are not assumed equivalent (`REF-CAD-013`, `REF-CAD-014`).

### TRC-EVID-004 — Geometry dose and mechanical dose are separate

Height/depth/angle/extent do not substitute for thickness, material stiffness, cushioning, lattice/infill or service-aged mechanics.

### TRC-EVID-005 — Offloading is redistribution, not local depression

Target ROI, safety ring and remote regions survive into quantitative outcome evaluation (`REF-CAD-004`, `REF-CAD-005`).

### TRC-EVID-006 — Manufacturing acceptance is profile-owned

No project-wide hidden dimensional tolerance is allowed. ISO/ASTM 52901/52902 support explicit inspection/capability/acceptance semantics but not one universal orthosis tolerance.

### TRC-EVID-007 — Reusable workflow knowledge is product infrastructure

Competitor convergence around saved templates/adjustments/histories/workflows makes versioned reusable design knowledge a P0 semantic requirement; advanced automatic authoring remains P1+.

---

## 4. Documentation gates before / during architecture selection

```text
GATE-DOC-01  traceability matrix current                         DONE v0.5
GATE-DOC-02  Geometry Authoring Contract                         DONE — FROZEN v1
GATE-DOC-03  Workflow/Preset/Macro Contract                      DONE — FROZEN v1
GATE-DOC-04  Numerical/Qualification Registry                    DONE — FROZEN v1
GATE-DOC-05  P0 authoring acceptance catalog                     DONE — FROZEN semantic test-spec v1
GATE-DOC-06  representative semantic test specs                  DONE — 22 scenarios
GATE-DOC-07  Project Schema v0.2 change-set                      DONE — APPROVED / NOT MATERIALIZED
GATE-DOC-08  cross-document contradiction/coverage audit         DONE — 0 blockers
GATE-DOC-09  acceptance-suite integration                        DONE — canonical addendum v1
GATE-DOC-10  definitive P0 authoring freeze audit                DONE — architecture-entry GO
GATE-DOC-11  geometry-engine evaluation scorecard                DONE — baseline v0.1, no winner
GATE-DOC-12  geometry-engine PoC/qualification plan              DONE — plan v0.1
GATE-ARCH-01 Q0 native/WASM build + dependency evidence          NEXT
GATE-ARCH-02 Q1..Q7 candidate qualification                      PENDING
GATE-ARCH-03 final engine selection                              BLOCKED ON EVIDENCE
```

`TD-CI-001` is not part of these documentation/architecture-analysis gates. It must be closed before executable qualification infrastructure is later trusted as CI evidence; it is not a reason to delay direct PoC evidence collection now.

---

## 5. Architecture-entry / selection rule

Architecture evaluation is now active, but candidates are judged against the frozen contracts rather than feature marketing.

Canonical scorecard:

`docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md`

Canonical qualification plan:

`docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`

Evaluation order:

```text
HARD GATES -> WEIGHTED CRITERIA -> POC EVIDENCE -> FINAL SCORE
```

The scorecard maps:

```text
GAUTH -> required geometry/query/replay capability
WFLOW -> isolation/versioning/expansion implications
NREG  -> numerical-control/tolerance implications
AUTH-C01..C22 -> concrete candidate tests/PoCs
```

A candidate that requires changing frozen product semantics to look viable fails the architecture evaluation unless a new explicit evidence-backed product decision supersedes the freeze.

A candidate is not selected while a selection-critical hard gate remains `UNKNOWN`.

Auxiliary libraries are admitted only after a concrete frozen requirement + PoC demonstrates a bounded missing primitive. General capability breadth is not sufficient reason to add a dependency.

---

## 6. Current engine-evaluation traceability

| Frozen area | Scorecard gates / criteria | PoC phase | Key acceptance |
|---|---|---|---|
| semantic isolation / replay | HG-01/02/14 | Q0/Q1 | C01/C06/C15/C22 |
| stable authoring addressing | HG-03 | Q1/Q2 | C01/C03/C06 |
| surface points/derivatives/normals | HG-04; W-01/W-04 | Q1 | C01/C04/C11/C12 |
| local deformation / sculpt / mirror | HG-05; W-02/W-03 | Q2 | C01/C02/C03/C06/C08/C18 |
| scan conform / nearest projection | HG-06/HG-12; W-05/W-09 | Q3 | C07 |
| section/measurement/thickness/deviation | HG-07; W-06 | Q3 | C11..C14 |
| production body / minimum thickness / DFM | HG-08; W-07/W-16 | Q4/Q6 | C08/C13/C14/C19/C21/C22 |
| deterministic numerical control | HG-09; W-04/W-08 | Q5 | C08/C14/C16/C19..C22 |
| native/server/WASM one-core portability | HG-10; W-10/W-11 | Q0/Q6 | cross-cutting |
| interactive performance/invalidation | HG-11; W-08 | Q2/Q5 | authoring preview/commit path |
| license/API/dependency containment | HG-13/HG-14; W-12/W-13/W-14/W-15 | Q0/Q6 | provenance/replay boundary |
| all frozen scenarios | HG-15 | Q7 | C01..C22 |

---

## 7. Maintenance rule

Whenever a P0 requirement changes, update this matrix with owner, acceptance direction, evidence/rationale and open/qualification state.

A requirement without an owner or acceptance direction is documentation debt.

Normative changes to the frozen authoring package require an explicit superseding decision/version.