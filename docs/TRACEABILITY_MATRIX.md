# BiomechE-CAD — Requirement Traceability Matrix

**Status:** CANONICAL TRACEABILITY BASELINE v0.1  
**Date:** 2026-08-15  
**Architecture:** kernel/runtime/storage independent  
**Functional authority:** `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`  
**Scientific authority:** `BIBLIOGRAPHY.md`  
**Executable-validation note:** current CI debt is tracked separately in `TECHNICAL_DEBT.md`; semantic coverage in this matrix is not blocked by `TD-CI-001`.

---

## 1. Purpose

This matrix answers, for every major product requirement family:

```text
WHY does it exist?
WHERE is it specified?
HOW is it accepted?
WHAT evidence constrains it?
WHAT remains open?
```

The matrix is deliberately **family-level** rather than a duplicate of every acceptance ID. Detailed numerical/behavioral checks remain in their owning specs and acceptance suite.

Status vocabulary:

```text
FROZEN       semantic contract may be implemented without reopening product intent
ACTIVE       sufficiently specified to work from, but refinements are expected
P0-NEXT      required before architecture shoot-out / implementation freeze
QUALIFY      semantic model exists; real device/process/profile evidence still required
P1/P2        deliberately later
HISTORICAL   retained for audit, not current authority
```

---

## 2. Product-level traceability

| Requirement family | Priority/status | Canonical owner | Acceptance family | Evidence / rationale | Current gap |
|---|---|---|---|---|---|
| Product scope / vertical orthotic CAD | FROZEN | `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | cross-domain | EasyCAD2 behavioral baseline + market audit + scientific batches | none at feature-inventory level |
| Project/revision/provenance model | ACTIVE | `spec/02_project_schema.md` | `SCHEMA-*`, `XACC-*` | W3C PROV, FAIR, reproducibility doctrine | schema evolution for new macro/acquisition details to be materialized later |
| Coordinate, side, mirror, registration | FROZEN | `spec/01_coordinate_registration.md` | `XACC-*` + registration cases | ISB context; BiomechE frame contract; anatomy/landmark evidence | numeric registration tolerances remain profile/device owned |
| Scan 3D / capture context | P0-NEXT | Functional v2 + Project Schema + `spec/16_geometry_authoring_contract.md` | `GAUTH-*` | `REF-CAD-002`, `REF-CAD-003`; acquisition-condition literature | formal capture-context compatibility rules |
| Landmark provenance | P0-NEXT | `spec/16_geometry_authoring_contract.md` | `GAUTH-*` | `REF-CAD-002`, `REF-CAD-003`, `REF-CAD-107` | schema materialization + UI review states |
| Base template / outline / sizing | P0-NEXT | Functional v2 + `spec/16_geometry_authoring_contract.md` | `GAUTH-*` | EasyCAD2 US/DIMA evidence; market table stakes | exact template-family geometry rules remain implementation-specific |
| Arch authoring | ACTIVE -> P0 freeze | `spec/16_geometry_authoring_contract.md` + existing arch research | `ARCH-*`, `GAUTH-*` | `REF-CAD-017`, `REF-CAD-053`, `REF-CAD-055`, `REF-CAD-056` | numerical defaults must stay profile/context specific |
| Heel authoring | ACTIVE -> P0 freeze | `spec/16_geometry_authoring_contract.md` + existing heel research | `HEEL-*`, `GAUTH-*` | `REF-CAD-018`, `REF-CAD-058..067` | no universal cup/skive/relief dose |
| Rear/forefoot wedge/posting | ACTIVE -> P0 freeze | `spec/16_geometry_authoring_contract.md` | `GAUTH-*` + existing dose acceptance | `REF-CAD-001`, `REF-CAD-015` | default dose/profile rules remain indication specific |
| Corrective elements | ACTIVE | `spec/06_corrective_elements.md` + authoring contract | `CE-*`, `GAUTH-*` | EasyCAD2 + market named-correction workflows | exact geometric implementation remains kernel independent/open |
| Metatarsal pad / landmark-relative placement | P0-NEXT | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `CE-*` | `REF-CAD-013`, `REF-CAD-014` | placement must support multiple reference modes; no universal position |
| Offloading / accommodation | ACTIVE | `spec/06_corrective_elements.md` + Functional v2 | `OFF-*`, `XACC-*` | `REF-CAD-004`, `REF-CAD-005`, `REF-CAD-007`, `REF-CAD-008` | quantitative closed loop requires qualified acquisition/profile |
| Sculpt / local freeform | P0-NEXT | `spec/16_geometry_authoring_contract.md` | `GAUTH-*` | EasyCAD2 validated behavior + market baseline | representation chosen later; semantic replay must survive |
| Scan conform / target projection | P0-NEXT | `spec/16_geometry_authoring_contract.md` | `GAUTH-*` | acquisition/registration evidence | exact projection algorithm and tolerances remain algorithm-owned |
| Inspection: section, distance, angle, height, thickness | P0-NEXT | `spec/16_geometry_authoring_contract.md` | `GAUTH-*`, `XACC-*` | EasyCAD2 control workflow + competitor table stakes | measurement representation/tolerance registry required |
| Minimum thickness / DFM | ACTIVE | `spec/09_analysis_qc_dfm.md`, `spec/10_manufacturing.md`, `spec/18_numerical_qualification_registry.md` | `MAN-*`, `XACC-*`, `NREG-*` | manufacturing standards + process evidence | numeric minimum is ManufacturingProfile-owned |
| Material identity / stiffness / regional mechanics | ACTIVE | `spec/08_material_stiffness.md` | `MAT-*` | `REF-CAD-098..105`, ISO material test semantics | actual qualified material/process profiles needed |
| Variable density / lattice / structural regions | ACTIVE P0 semantic / P1 advanced | `spec/08_material_stiffness.md`, authoring contract | `MAT-*`, `GAUTH-*` | `REF-CAD-098`, `REF-CAD-099` | printer/process realization later |
| Manufacturing run / artifact / physical part | ACTIVE | `spec/10_manufacturing.md` | `MAN-*`, `XACC-*` | ISO/ASTM 52901, 52902, 52920, ISO 17295 | actual machine/process qualification pending |
| CAD nominal vs manufactured measured geometry | P0 semantic / QUALIFY | `spec/10_manufacturing.md` + numerical registry | `MAN-*`, `NREG-*` | `REF-CAD-106`; ISO/ASTM 52902 | no universal dimensional tolerance |
| Workflow preset / macro / history | P0-NEXT | `spec/17_workflow_preset_macro.md` | `WFLOW-*` | competitor convergence: EasyCAD2 templates, Canfit macros, paro360 histories, FitFoot360 reusable design knowledge, Amfit adjustments | schema/UI materialization later |
| Bilateral copy/mirror of workflow | P0-NEXT | coordinate spec + workflow spec + authoring contract | `WFLOW-*`, `GAUTH-*`, `XACC-*` | market baseline + side semantic safety | per-operation mirror policy must be explicit |
| BiomechE quantitative integration | FROZEN | `spec/11_biomeche_integration.md` | `BINT-*` | pinned BiomechE contract + provenance evidence | new upstream DYN capabilities only after upstream freeze |
| Pressure acquisition qualification | FROZEN methodology / QUALIFY hardware | `spec/15_pressure_acquisition_qualification.md` | `PAQ-*` | `REF-CAD-108..110` | first physical FM12050 unit and real bench evidence |
| Pressure-informed outcome loop | ACTIVE P0 | Functional v2 + BiomechE integration | `BINT-*`, `OFF-*`, `XACC-*` | `REF-CAD-004`, `REF-CAD-005`, `REF-CAD-069` | profile/device comparability qualification |
| Measured vs predicted outcome separation | FROZEN principle | Project Schema + Functional v2 | `SCHEMA-*`, `XACC-*` | scientific integrity / provenance | prediction models later |
| PROM / comfort / fit / adherence | ACTIVE | `spec/14_prom_comfort_adherence.md` | `PROM-*` | `REF-CAD-080..097` | exact instruments/licensing/population selection |
| Reporting / traceability | FROZEN | `spec/12_reporting_traceability.md` | `RPT-*` | W3C PROV / FAIR / biomedical provenance | renderer/signing/archive profile later |
| Cloud/offline portability | P1 | schema principles + future sync spec | future | market signal from cloud ecosystems | conflict/sync contract not yet frozen |
| Geometry kernel/runtime | PARKED | architecture status docs | future shoot-out | must satisfy all above contracts | OpenSubdiv vs ON_SubD etc intentionally undecided |

---

## 3. Evidence-derived rules now considered product requirements

### TRC-EVID-001 — Capture context survives into design provenance

A scan used to influence geometry SHALL preserve capture condition, including weight-bearing state when known. `UNKNOWN` is valid; silently assuming a state is not.

Evidence role: 3D scanning methodology/reliability and reporting (`REF-CAD-002`, `REF-CAD-003`).

### TRC-EVID-002 — Landmark coordinates require source/method provenance

A landmark is not just a point. Its source, method, frame, author/algorithm and quality/review status are part of its meaning.

### TRC-EVID-003 — Placement is a typed reference, not an unlabelled XYZ

Corrective elements SHALL support explicit placement semantics such as:

```text
LANDMARK_RELATIVE_MM
LANDMARK_LINE_RELATIVE_MM
NORMALIZED_FOOT_LENGTH
INTRINSIC_SQ
ROI_RELATIVE
PRESSURE_TARGET_RELATIVE
CUSTOM_REGISTERED_REFERENCE
```

The metatarsal-pad literature demonstrates why different populations/reference definitions cannot be collapsed into one universal coordinate (`REF-CAD-013`, `REF-CAD-014`).

### TRC-EVID-004 — Geometry dose and mechanical dose remain separate

Height/depth/angle/extent do not substitute for material stiffness, thickness, lattice/infill, cushioning or effective structural response.

### TRC-EVID-005 — Improvement in one ROI is not sufficient evidence of global success

Offloading evaluation SHALL preserve target ROI, safety-ring and remote-region comparison semantics (`REF-CAD-004`, `REF-CAD-005`).

### TRC-EVID-006 — Manufacturing acceptance belongs to a qualified profile

No project-wide hidden dimensional tolerance is permitted. Acceptance requires method + machine/process/material/profile + feature class + uncertainty where relevant. ISO/ASTM 52901 and 52902 support part-definition/inspection/capability semantics but do not prescribe one universal orthosis tolerance.

---

## 4. Documentation gates before architecture selection

The following are now the documentation gates for resuming the geometry-engine shoot-out:

```text
GATE-DOC-01  Traceability matrix exists and remains current              DONE v0.1
GATE-DOC-02  Geometry Authoring Contract P0 frozen                       NEXT
GATE-DOC-03  Workflow/Preset/Macro semantic contract frozen              NEXT
GATE-DOC-04  Numerical/Qualification Registry rules frozen               NEXT
GATE-DOC-05  P0 geometry-dependent acceptance catalog allocated          NEXT
GATE-DOC-06  first representative geometry fixtures specified            NEXT
```

`TD-CI-001` is **not** part of these documentation gates. It must be closed before executable qualification is trusted again, but it does not prevent specification work.

---

## 5. Maintenance rule

Whenever a P0 requirement is added or materially changed, update this matrix in the same documentation session with:

```text
requirement family
canonical owner
acceptance family
evidence/rationale
qualification/open state
```

A requirement without an owner or acceptance direction is incomplete documentation debt.
