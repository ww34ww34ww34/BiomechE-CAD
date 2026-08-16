# BiomechE-CAD — P0 Documentation Closure Audit

**Status:** COMPLETE BASELINE AUDIT v1  
**Date:** 2026-08-16  
**Phase:** `P0-DOC-CLOSURE / DOC-00`  
**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Architecture:** geometry-engine selection remains deferred; this audit is product/document authority only.

---

## 1. Purpose

This audit classifies the current BiomechE-CAD documentation before the remaining P0 documentation is frozen. It does not reopen frozen authoring semantics and does not materialize Project Schema v0.2.

The audit answers four questions:

1. which files are current product authority;
2. which files are mature enough for v1 freeze after harmonization;
3. which files are engineering hypotheses rather than product authority;
4. which missing cross-cutting contracts must still be created before documentation closure.

---

## 2. Authority hierarchy

When two documents overlap, authority resolves in this order for the current phase:

```text
BIOMECHE_CAD_FUNCTIONAL_SPEC_V2
        ↓
frozen domain contracts
  01 coordinate/registration
  11 BiomechE integration
  12 reporting/traceability
  15 pressure-acquisition qualification
  16 geometry authoring
  17 workflow/preset/macro
  18 numerical qualification registry
        ↓
P0 Authoring Acceptance Catalog + acceptance addendum
        ↓
remaining product specifications being closed in DOC-01..DOC-13
        ↓
architecture research / implementation hypotheses
```

Historical or provisional engineering files cannot override a frozen contract.

---

## 3. External evidence validation performed for DOC-00

The closure criteria were cross-checked against current scientific/guideline/standards evidence already registered in `docs/BIBLIOGRAPHY.md`, plus a current-source verification pass on 2026-08-16.

### 3.1 Corrective/offloading semantics

The current literature continues to support context-specific, measurable orthotic dose rather than anonymous geometry or a universal preset:

- `REF-CAD-011` — customized/bespoke orthotic treatment can reduce central-metatarsal plantar pressure in mechanical metatarsalgia, but the evidence does not justify one universal geometry/placement rule;
- `REF-CAD-012` — 2026 systematic review supports forefoot plantar-loading reduction while explicitly exposing an evidence gap for proposed posterior-chain mechanisms;
- `REF-CAD-013/014` — metatarsal-pad placement is a measurable intervention variable and published positions are population/protocol specific;
- `GUIDE-IWGDF-2023` — pressure-relieving therapeutic footwear is context-specific to diabetic-ulcer prevention/recurrence and active-ulcer offloading follows a distinct care pathway;
- `GUIDE-HEEL-PAIN-2023` — orthoses are not recommended as an isolated short-term treatment for plantar fasciitis, supporting profile-bound interpretation rather than a global therapeutic-success rule.

**Audit consequence:** `06_corrective_elements.md` is semantically mature; freeze must preserve explicit anatomical placement, target/adjacent ROI, requested/realized dose and evidence-profile context.

### 3.2 Material/mechanical semantics

Current registered evidence remains consistent with the existing `08` model:

- `REF-CAD-094` finds limited/heterogeneous evidence that several orthotic materials can reduce plantar pressure; no universal ranking follows;
- `REF-CAD-099` demonstrates load-dependent cushioning-stiffness optimization in a studied setting, supporting mechanical-dose/context metadata rather than a global stiffness default;
- `REF-CAD-095/096/100/101/103/105` support cyclic, thermal, service-aged and interface-dependent behavior;
- `STD-ISO-868-2003` explicitly treats Shore durometer hardness as an empirical control measurement with no simple universal relationship to a fundamental material property;
- `STD-ISO-3386-1-2025` defines compression stress/strain characterization for low-density flexible cellular materials.

**Audit consequence:** `08_material_stiffness.md` is mature enough for v1 freeze once its relationship to `NREG` and manufacturing is made explicit.

### 3.3 Manufacturing and QC semantics

Current standards verify the separation already adopted by the project:

- `STD-ISOASTM-52901-2017` distinguishes part definition, feedstock, final characteristics/properties, inspection and acceptance information;
- `STD-ISOASTM-52920-2023` defines process/site qualification principles for industrial AM;
- `STD-ISOASTM-52924-2023` separates mechanical, physical and geometrical classes for polymer-AM part properties;
- `STD-ISO-17295-2023` standardizes part positioning/orientation/coordinate reporting for AM;
- ISO/ASTM 52951:2026 now provides a data-package/digital-thread framework from design through acceptance. This is new supporting evidence for a product-owned manufacturing handoff package; it does not replace the internal clinical/design semantic model.

**Audit consequence:** `09_analysis_qc_dfm.md` and `10_manufacturing.md` are mature enough for v1 freeze. A separate DOC-10 interchange/handoff contract remains useful because file/data-package transport is not the same authority as the manufacturing lifecycle.

### 3.4 Profile and PROM semantics

Current guideline and measurement-methodology evidence validates the existing separation:

- `GUIDE-IWGDF-2023` requires condition-specific interpretation and separates prevention from active-ulcer offloading;
- `GUIDE-HEEL-PAIN-2023` supports multimodal interpretation for plantar heel pain;
- `GUIDE-COSMIN` requires clear construct definition and evidence-based selection of outcome measurement instruments using measurement properties and feasibility;
- `GUIDE-FDA-PRO-DEVICE-2022` requires PRO instruments to be fit for purpose for the intended device-evaluation context;
- `REF-CAD-091/092` support explicit adherence method and denominator rather than treating self-report, hours/day and exposure-normalized adherence as interchangeable.

**Audit consequence:** `13_use_case_profiles.md` and `14_prom_comfort_adherence.md` are mature enough for v1 freeze after explicit authority linkage.

### 3.5 Input/scan semantics

`REF-CAD-002` reports low-to-moderate evidence and variable accuracy/reliability when comparing 3D scanning with traditional morphology capture. `REF-CAD-003` identifies large variation in scanner specifications, weight-bearing, markers, number of scans, measurements and analysis protocols, and proposes a reporting checklist.

**Audit consequence:** the missing `20_input_scan_reference_data.md` is a real product contract, not an implementation detail. Capture conditions, original-vs-derived identity and processing provenance must be first-class.

---

## 4. Canonical document classification

| Document | DOC-00 classification | Authority / disposition |
|---|---|---|
| `spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` | **CANONICAL** | product-scope authority |
| `spec/01_coordinate_registration.md` | **FROZEN v1** | coordinate/laterality/registration authority |
| `spec/02_project_schema.md` | **CANONICAL ACTIVE v0.1** | persisted semantic baseline; v0.2 change-set is approved but not materialized |
| `spec/03_geometry_operation_model.md` | **HISTORICAL / SUPERSEDED IN PART** | pre-freeze OpenSubdiv-first architecture hypothesis; product semantics defer to `16` |
| `spec/04_base_template.md` | **QUALIFICATION-DEPENDENT ENGINEERING HYPOTHESIS** | `ORTHO_CAGE_41x17_V0`, Catmull-Clark and topology counts are not product authority; retain as candidate fixture only |
| `spec/05_parametric_orthosis_geometry.md` | **QUALIFICATION-DEPENDENT ENGINEERING REFERENCE** | candidate formulas only; semantic operator authority is `16`; numerical limits remain OPEN unless qualified |
| `spec/06_corrective_elements.md` | **READY FOR DOC-01 v1 FREEZE** | product semantic taxonomy and measurable prescription layer |
| `spec/08_material_stiffness.md` | **READY FOR DOC-02 v1 FREEZE** | material/mechanical-dose semantic authority |
| `spec/09_analysis_qc_dfm.md` | **READY FOR DOC-03 v1 FREEZE** | metric/QC/DFM semantic authority, subordinate to `NREG` for numerical authority classes |
| `spec/10_manufacturing.md` | **READY FOR DOC-04 v1 FREEZE** | manufacturing lifecycle/provenance authority |
| `spec/11_biomeche_integration.md` | **FROZEN v1** | BiomechE↔CAD quantitative contract |
| `spec/12_reporting_traceability.md` | **FROZEN v1** | immutable report/source-manifest authority |
| `spec/13_use_case_profiles.md` | **READY FOR DOC-05 v1 FREEZE** | evidence-context/non-transfer authority |
| `spec/14_prom_comfort_adherence.md` | **READY FOR DOC-06 v1 FREEZE** | PROM/comfort/fit/adherence authority |
| `spec/15_pressure_acquisition_qualification.md` | **FROZEN methodology v1** | pressure-device/protocol qualification method |
| `spec/16_geometry_authoring_contract.md` | **FROZEN v1** | geometry-authoring semantic authority |
| `spec/17_workflow_preset_macro.md` | **FROZEN v1** | reusable workflow/preset authority |
| `spec/18_numerical_qualification_registry.md` | **FROZEN v1** | numerical authority/tolerance/default lifecycle |
| `spec/19_project_schema_v0_2_changeset.md` | **APPROVED / NOT MATERIALIZED** | additive future schema direction only |
| `spec/CAD_ENGINE_CAPABILITY_SPEC.md` | **HISTORICAL** | superseded for current evaluation by geometry-engine scorecard |
| `spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md` | **HISTORICAL CHECKPOINT** | pre-freeze selection checkpoint |

There is intentionally no `spec/07_*`. The numbering gap is historical and is **not** filled solely for cosmetic continuity.

---

## 5. Remaining document gaps

The following are still required for full `P0-DOC-CLOSURE`:

| ID | Missing/remaining artifact | Why it remains necessary |
|---|---|---|
| DOC-01 | freeze `06_corrective_elements.md` | remove ACTIVE-v0 ambiguity and reconcile with `16/17/18` |
| DOC-02 | freeze `08_material_stiffness.md` | fix mechanical/numerical/manufacturing authority boundaries |
| DOC-03 | freeze `09_analysis_qc_dfm.md` | harmonize metric/QC/DFM acceptance and tolerance ownership |
| DOC-04 | freeze `10_manufacturing.md` | freeze artifact/run/physical-part lifecycle |
| DOC-05 | freeze `13_use_case_profiles.md` | freeze non-transfer/profile boundaries |
| DOC-06 | freeze `14_prom_comfort_adherence.md` | freeze measurement/instrument/adherence semantics |
| DOC-07 | explicit disposition headers for `04/05` | prevent implementation hypotheses becoming product doctrine |
| DOC-08 | `20_input_scan_reference_data.md` | original/processed/derived source contract |
| DOC-09 | `21_product_workflow_interaction.md` | end-to-end product state and interaction contract |
| DOC-10 | `22_interchange_manufacturing_handoff.md` | format/package/handoff loss and coordinate semantics |
| DOC-11 | `23_realtime_performance_contract.md` | product performance doctrine before engine qualification |
| DOC-12 | `24_validation_verification_master_plan.md` | one V&V authority over all acceptance namespaces |
| DOC-13 | intended-use/risk/privacy/security boundary | separate product safety/regulatory/security stream |
| DOC-14 | final cross-document closure audit | formal documentation freeze gate |
| VIS-01..04 | visual reference package | versioned visual/interaction baseline after semantic closure |

---

## 6. Freeze criteria for DOC-01..06

A document may move from `ACTIVE v0` to `FROZEN v1` only if all conditions below are satisfied:

1. no statement conflicts with `BIOMECHE_CAD_FUNCTIONAL_SPEC_V2` or frozen `01/11/12/15/16/17/18`;
2. no architecture library is required for the semantic contract;
3. all numerical values are either evidence/profile qualified or remain `OPEN`/illustrative;
4. clinical evidence is population/protocol contextualized;
5. manufacturing values are owned by ManufacturingProfile/QC requirements, not by clinical thresholds;
6. algorithm tolerances are owned by `NREG`, not inferred from device/manufacturing/clinical values;
7. acceptance namespace remains explicit and traceable;
8. report/provenance semantics point to exact design/manufacturing/physical/source revisions where applicable.

---

## 7. DOC-07 disposition decision

### `04_base_template.md`

**Decision:** retain, but classify as **ENGINEERING CANDIDATE / QUALIFICATION FIXTURE — NOT PRODUCT AUTHORITY**.

The following are implementation hypotheses and must not be frozen before architecture qualification:

```text
ORTHO_CAGE_41x17_V0
41 x 17 / 697 vertices / 640 quads
Catmull-Clark/OpenSubdiv evaluation
specific vertex-ID mapping
specific boundary interpolation / crease choices
specific candidate control spacing
```

The semantic requirement that a reusable base/template has exact identity/version/provenance and can be deterministically reconstructed remains valid, but its topology does not.

### `05_parametric_orthosis_geometry.md`

**Decision:** retain as **ENGINEERING MATHEMATICAL REFERENCE — INTENTIONALLY PROVISIONAL**.

The named operations and explicit units/directions/constraints remain useful. Exact bump functions, interpolation formulas, smoothing algorithms, projection algorithms and displacement-direction defaults are qualification hypotheses. `16_geometry_authoring_contract.md` owns the product semantics.

---

## 8. Risks found

### R-DOC-01 — accidental topology lock-in

`04` reads like an implementation-ready canonical cage and can be mistaken for a frozen product decision. DOC-07 must add a prominent non-authoritative status banner.

### R-DOC-02 — formula authority leakage

`05` contains deterministic formulas that are useful as test hypotheses but may be mistaken for validated clinical behavior. DOC-07 must explicitly subordinate them to `16` and `18`.

### R-DOC-03 — standards currency drift

Manufacturing standards continue to evolve. ISO/ASTM 52951:2026 is a material new source for design-to-acceptance data packages. Standards entries should therefore carry edition/status and periodic review rather than being treated as timeless constants.

### R-DOC-04 — visual specification lag

Without VIS-01..04, future UI implementation can satisfy text requirements while diverging in interaction density, state visibility and workflow coherence. The visual package remains part of documentation closure, but must be produced after written semantics stabilize.

---

## 9. DOC-00 verdict

```text
DOC-00 BASELINE INVENTORY              PASS
AUTHORITY HIERARCHY                    PASS
ACTIVE-v0 CANDIDATES IDENTIFIED        PASS
04/05 DISPOSITION                      DECIDED
MISSING CROSS-CUTTING CONTRACTS        IDENTIFIED
EXTERNAL EVIDENCE CONSISTENCY          PASS
BLOCKING CONTRADICTIONS                0 FOUND AT DOC-00 LEVEL
```

**Next authorized work:** execute DOC-01..06 harmonization/freeze, then add the DOC-07 status banners and proceed to DOC-08.

---

## 10. Evidence references

Canonical bibliography IDs used in this audit:

```text
GUIDE-IWGDF-2023
GUIDE-HEEL-PAIN-2023
GUIDE-COSMIN
GUIDE-FDA-PRO-DEVICE-2022
REF-CAD-002
REF-CAD-003
REF-CAD-011
REF-CAD-012
REF-CAD-013
REF-CAD-014
REF-CAD-091
REF-CAD-092
REF-CAD-094
REF-CAD-095
REF-CAD-096
REF-CAD-099
REF-CAD-100
REF-CAD-101
REF-CAD-103
REF-CAD-105
STD-ISO-868-2003
STD-ISO-3386-1-2025
STD-ISOASTM-52901-2017
STD-ISOASTM-52920-2023
STD-ISOASTM-52924-2023
STD-ISO-17295-2023
```

Current-source verification also consulted ISO/ASTM 52951:2026, *Additive manufacturing — Data — Data packages for AM parts*, official ISO publication 2026-06. It should be normalized into the canonical bibliography during the next bibliography-maintenance pass.
