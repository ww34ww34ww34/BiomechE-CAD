# BiomechE-CAD — Requirement Traceability Matrix

**Status:** CANONICAL TRACEABILITY BASELINE v0.2  
**Date:** 2026-08-15  
**Architecture:** kernel/runtime/storage independent  
**Functional authority:** `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`  
**Scientific authority:** `BIBLIOGRAPHY.md`  
**Executable-validation note:** CI debt is tracked separately in `TECHNICAL_DEBT.md`; semantic coverage is not blocked by `TD-CI-001`.

---

## 1. Purpose

For each major product requirement family this matrix records:

```text
WHY it exists
WHERE it is specified
HOW it is accepted
WHAT evidence constrains it
WHAT remains open
```

Detailed acceptance semantics stay in owning specs/catalogs; this file is the navigation/coverage layer.

Status vocabulary:

```text
FROZEN       product meaning stable
ACTIVE       usable baseline, refinements possible
DRAFT-FREEZE canonical P0 draft exists; cross-document review is next
QUALIFY      semantic contract exists; real device/process/profile evidence required
P1/P2        deliberately later
PARKED       downstream decision intentionally postponed
```

---

## 2. Product-level traceability

| Requirement family | Status | Canonical owner | Acceptance | Evidence/rationale | Remaining work |
|---|---|---|---|---|---|
| Product scope / vertical orthotic CAD | FROZEN | `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | cross-domain | EasyCAD2 + competitor + scientific evidence | none at inventory level |
| Project/revision/provenance | ACTIVE | `spec/02_project_schema.md` | `SCHEMA-*`, `XACC-*` | provenance/reproducibility doctrine | v0.2 materialization later |
| Schema v0.2 evolution | DRAFT-FREEZE | `spec/19_project_schema_v0_2_changeset.md` | migration/change-set review | new P0 authoring requirements | review, then JSON schema/migration later |
| Coordinate/laterality/registration | FROZEN | `spec/01_coordinate_registration.md` | `XACC-*` | BiomechE/ISB/anatomical context | numeric limits profile-owned |
| Scan capture context | DRAFT-FREEZE | `spec/16_geometry_authoring_contract.md` + schema v0.2 change-set | `GAUTH-*`, `AUTH-C07`, `AUTH-C09` | `REF-CAD-002`, `REF-CAD-003` | freeze + later schema materialization |
| Landmark provenance | DRAFT-FREEZE | authoring contract + schema v0.2 change-set | `GAUTH-*`, `AUTH-C10` | `REF-CAD-002`, `REF-CAD-003`, `REF-CAD-107` | freeze + UI details later |
| Base template / outline / sizing | DRAFT-FREEZE | `spec/16_geometry_authoring_contract.md` | `GAUTH-*` | EasyCAD2/market baseline | exact geometry implementation later |
| Arch authoring | DRAFT-FREEZE | `spec/16_geometry_authoring_contract.md` | `ARCH-*`, `GAUTH-*`, `AUTH-C01` | `REF-CAD-017`, `053`, `055`, `056` | no universal numeric default |
| Heel authoring | DRAFT-FREEZE | `spec/16_geometry_authoring_contract.md` | `HEEL-*`, `GAUTH-*`, `AUTH-C02` | `REF-CAD-018`, `058..067` | no universal cup/skive/relief dose |
| Rear/forefoot wedge/posting | DRAFT-FREEZE | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C03` | `REF-CAD-001`, `REF-CAD-015` | defaults profile-specific |
| Corrective elements | ACTIVE / authoring draft | `spec/06_corrective_elements.md` + `16` | `CE-*`, `GAUTH-*` | EasyCAD2 + market named corrections | kernel-specific realization later |
| Met-pad/reference-relative placement | DRAFT-FREEZE | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C04` | `REF-CAD-013`, `REF-CAD-014` | multiple placement modes preserved |
| Offloading / accommodation | ACTIVE | `spec/06_corrective_elements.md` + `16` | `OFF-*`, `GAUTH-*`, `AUTH-C05` | `REF-CAD-004`, `005`, `007`, `008` | real outcome loop requires qualified acquisition |
| Sculpt / local freeform | DRAFT-FREEZE | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C06` | EasyCAD2 + market | low-level representation later |
| Scan conform | DRAFT-FREEZE | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C07` | scan/registration evidence | exact algorithm/tolerance later |
| Requested vs realized constrained geometry | DRAFT-FREEZE | `16`, `18`, schema v0.2 change-set | `GAUTH-*`, `NREG-*`, `AUTH-C08` | prescription vs DFM separation | runtime evaluation model later |
| Inspection: section/distance/angle/thickness | DRAFT-FREEZE | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `AUTH-C11..13` | EasyCAD2 + market baseline | low-level query implementation later |
| CAD vs measured-part deviation | DRAFT-FREEZE / QUALIFY | `16`, `10`, `18` | `AUTH-C14`, `MAN-*`, `NREG-*` | `REF-CAD-106`; ISO/ASTM 52902 | process acceptance limits later |
| Minimum thickness / DFM | ACTIVE / QUALIFY | `09`, `10`, `18` | `MAN-*`, `NREG-*` | manufacturing standards/evidence | value ManufacturingProfile-owned |
| Material/stiffness/regional mechanics | ACTIVE / QUALIFY | `spec/08_material_stiffness.md` | `MAT-*` | `REF-CAD-098..105` | real profiles/process testing |
| Manufacturing run/artifact/physical part | ACTIVE / QUALIFY | `spec/10_manufacturing.md` | `MAN-*`, `XACC-*` | ISO/ASTM 52901/52902/52920; ISO 17295 | actual process qualification |
| Workflow preset/macro/history | DRAFT-FREEZE | `spec/17_workflow_preset_macro.md` | `WFLOW-*`, `AUTH-C15..18` | competitor convergence | schema/UI materialization later |
| Numerical/tolerance governance | DRAFT-FREEZE | `spec/18_numerical_qualification_registry.md` | `NREG-*`, `AUTH-C19..22` | literature + qualification standards | machine-readable registry later |
| BiomechE quantitative integration | FROZEN | `spec/11_biomeche_integration.md` | `BINT-*` | pinned upstream contract | follow future upstream freezes |
| Pressure acquisition qualification | FROZEN method / QUALIFY hardware | `spec/15_pressure_acquisition_qualification.md` | `PAQ-*` | `REF-CAD-108..110` | first physical FM12050 qualification |
| Pressure-informed outcome loop | ACTIVE | Functional v2 + `11` + `06` | `BINT-*`, `OFF-*` | `REF-CAD-004`, `005`, `069` | compatibility/device qualification |
| Measured vs predicted separation | FROZEN | Project Schema + Functional v2 | `SCHEMA-*`, `XACC-*` | scientific integrity | prediction models later |
| PROM/comfort/fit/adherence | ACTIVE | `spec/14_prom_comfort_adherence.md` | `PROM-*` | `REF-CAD-080..097` | exact instrument/licensing selection |
| Reporting / traceability | FROZEN | `spec/12_reporting_traceability.md` | `RPT-*` | PROV/FAIR/biomedical provenance | renderer/signing/archive later |
| Cloud/offline sync | P1/P2 | future sync spec | future | market signal | conflict/sync semantics open |
| Geometry kernel/runtime | PARKED | architecture docs | future scorecard/shoot-out | must satisfy authoring contracts | OpenSubdiv vs ON_SubD etc undecided |

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

## 4. Documentation gates before architecture selection

```text
GATE-DOC-01  traceability matrix current                         DONE v0.2
GATE-DOC-02  Geometry Authoring Contract written                 DONE draft; FREEZE NEXT
GATE-DOC-03  Workflow/Preset/Macro Contract written              DONE draft; FREEZE NEXT
GATE-DOC-04  Numerical/Qualification Registry written            DONE draft; FREEZE NEXT
GATE-DOC-05  P0 authoring acceptance catalog allocated           DONE v0.1
GATE-DOC-06  representative semantic fixture/test specs written  DONE — 22 scenarios
GATE-DOC-07  Project Schema v0.2 change-set documented           DONE design draft
GATE-DOC-08  cross-document contradiction/coverage audit         NEXT
GATE-DOC-09  16/17/18 promoted to FROZEN v1                     NEXT
GATE-DOC-10  geometry-engine evaluation scorecard                AFTER FREEZE
```

`TD-CI-001` is not part of these documentation gates. It must be closed before executable qualification is trusted again, not before specification freeze.

---

## 5. Maintenance rule

Whenever a P0 requirement changes, update this matrix with owner, acceptance direction, evidence/rationale and open/qualification state.

A requirement without an owner or acceptance direction is documentation debt.
