# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-16  
**Current phase:** **P0 WRITTEN DOCUMENTATION COMPLETE + CANONICAL VISUAL SOURCE BASELINE v1 COMPLETE.**  
**Outstanding visual evidence:** rendered/browser captures `VIS-03R/VIS-04R`.  
**Architecture status:** **NO GEOMETRY ENGINE SELECTED.** Q0..Q7 plan preserved.

The P0 product/semantic documentation has closed with **0 blocking cross-document contradictions**. A versioned navigable visual source containing M01..M14 is now saved in the repository and mapped to requirements. Pixel/browser golden captures remain pending because no connected render pipeline was available in the closure session.

Project Schema v0.2 remains **APPROVED / NOT MATERIALIZED**. `TD-CI-001` remains deliberately deferred and non-blocking.

---

## 1. Read these first

1. `docs/RESUME_HERE.md`
2. `docs/P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md`
3. `docs/validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md`
4. `docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md`
5. `docs/ux/mockups/v1/manifest.md`
6. `docs/ux/VISUAL_REFERENCE_CROSS_DOCUMENT_AUDIT_2026-08-16.md`
7. `docs/SPEC_INDEX.md`
8. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
9. `docs/TRACEABILITY_MATRIX.md`
10. `docs/spec/01_coordinate_registration.md`
11. `docs/spec/02_project_schema.md`
12. `docs/spec/06_corrective_elements.md`
13. `docs/spec/08_material_stiffness.md`
14. `docs/spec/09_analysis_qc_dfm.md`
15. `docs/spec/10_manufacturing.md`
16. `docs/spec/11_biomeche_integration.md`
17. `docs/spec/12_reporting_traceability.md`
18. `docs/spec/13_use_case_profiles.md`
19. `docs/spec/14_prom_comfort_adherence.md`
20. `docs/spec/15_pressure_acquisition_qualification.md`
21. `docs/spec/16_geometry_authoring_contract.md`
22. `docs/spec/17_workflow_preset_macro.md`
23. `docs/spec/18_numerical_qualification_registry.md`
24. `docs/spec/19_project_schema_v0_2_changeset.md`
25. `docs/spec/20_input_scan_reference_data.md`
26. `docs/spec/21_product_workflow_interaction.md`
27. `docs/spec/22_interchange_manufacturing_handoff.md`
28. `docs/spec/23_realtime_performance_contract.md`
29. `docs/validation/24_validation_verification_master_plan.md`
30. `docs/spec/25_intended_use_risk_privacy_security_boundary.md`
31. `docs/research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md`
32. `docs/research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md`
33. `docs/BIBLIOGRAPHY.md`
34. `docs/NEXT_CHAT_PROMPT.md`

`BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` remains the functional authority. Historical engine-first documents do not override the frozen product model.

---

## 2. Mission

BiomechE-CAD is a vertical CAD for custom foot orthoses combining mature orthotic-CAD productivity with stronger scientific/lifecycle semantics:

```text
acquisition provenance
+ semantic prescription
+ reproducible authoring
+ quantitative biomechanics
+ immutable design revision
+ material/manufacturing lineage
+ physical-part identity
+ measured outcome loop
+ reproducible reporting
```

The geometry engine is replaceable downstream infrastructure.

---

## 3. Frozen product principles

Do not reopen without explicit new evidence/decision:

- committed `DesignRevision` is immutable;
- original source != processed/registered/derived;
- capture context + landmark provenance are first-class;
- file coordinates != anatomical coordinates;
- placement is typed anatomical/reference semantics, not raw XYZ authority;
- requested dose != realized CAD dose;
- geometry dose != mechanical/material dose;
- semantic prescription survives geometry;
- mirror is semantic and side-aware;
- no hidden universal clinical default;
- `OPEN` remains `OPEN`;
- algorithm tolerance != device limit != manufacturing tolerance != clinical threshold != performance budget;
- pressure heatmap != quantitative source;
- BiomechE owns quantitative KPI/result definitions;
- profile != diagnosis;
- suggestion != confirmation;
- pain/function/comfort/fit/satisfaction/adherence remain distinct;
- `MeasuredOutcome != PredictedOutcome`;
- `DesignRevision != ManufacturingArtifact != ManufacturingRun != PhysicalOrthosis`;
- CAD nominal != measured manufactured geometry;
- file format != semantic authority;
- preview != apply/commit != manufacturing release;
- geometry kernel must satisfy frozen contracts, never redefine them.

Canonical units:

```text
mm, s, N, kPa, deg, mm²
```

---

## 4. Written documentation closure — COMPLETE

Final audit:

`docs/validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md`

```text
DOC-00 baseline inventory                    PASS
DOC-01 corrective elements                   FROZEN v1
DOC-02 material / stiffness                  FROZEN v1
DOC-03 analysis / QC / DFM                   FROZEN v1
DOC-04 manufacturing                         FROZEN v1
DOC-05 use-case profiles                     FROZEN v1
DOC-06 PROM / comfort / adherence            FROZEN v1
DOC-07 04/05 authority disposition           DONE
DOC-08 input / scan / reference              FROZEN v1
DOC-09 product workflow / interaction        FROZEN v1
DOC-10 interchange / handoff                 FROZEN v1
DOC-11 realtime / performance doctrine       FROZEN; budgets OPEN
DOC-12 V&V master plan                       CANONICAL v1
DOC-13 intended-use/risk/privacy/security    CANONICAL boundary; classification OPEN
DOC-14 final cross-document audit            PASS
BLOCKING CONTRADICTIONS                      0
WRITTEN DOCUMENTATION CLOSURE                GO
```

---

## 5. Historical/engineering documents — explicitly non-authoritative

### `spec/04_base_template.md`

Status:

```text
ENGINEERING CANDIDATE / QUALIFICATION FIXTURE
```

Therefore the following are **not** product requirements:

```text
41×17 topology
specific vertex/index layout
Catmull-Clark/OpenSubdiv realization
specific control spacing
```

### `spec/05_parametric_orthosis_geometry.md`

Status:

```text
ENGINEERING MATHEMATICAL REFERENCE — INTENTIONALLY PROVISIONAL
```

Exact arch/wedge/heel/sculpt/smooth/scan-conform formulas, directions and sample values remain algorithm PoC hypotheses.

---

## 6. Canonical visual reference — SOURCE BASELINE COMPLETE

Visual brief:

`docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md`

Editable/navigable source:

`docs/ux/mockups/v1/biomeche-cad-mockups-v1.html`

Manifest:

`docs/ux/mockups/v1/manifest.md`

Source-level audit:

`docs/ux/VISUAL_REFERENCE_CROSS_DOCUMENT_AUDIT_2026-08-16.md`

Current visual status:

```text
VIS-01 visual brief / design system           DONE
VIS-02 M01..M14 navigable source               DONE
VIS-03 source/version archive                  DONE
VIS-04 requirement ↔ screen mapping            DONE
VIS-03R rendered PNG archive                   PENDING
VIS-04R browser/pixel visual audit             PENDING
```

Authority:

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
HTML/MOCKUP            = VISUAL / INTERACTION REFERENCE
```

---

## 7. Canonical M01..M14 screens

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

Visual direction v1:

```text
premium medical-tech workstation
3D-first
high information density without legacy industrial-CAD chrome
light canonical baseline + dark representative screens
teal / blue / sage / restrained warm accents
no purple-dominant identity
persistent case / side / revision / profile context
semantic controls, not raw topology
requested vs realized values
status via text/icon/shape + color
quantitative palettes separated from process-status colors
provenance through progressive disclosure
```

---

## 8. Human-factors/accessibility evidence

Current visual evidence baseline:

`docs/research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md`

It maps current ISO 9241-210, IEC 62366-1, FDA human-factors and WCAG 2.2 principles into `HF-VIS-001..010`.

This is design guidance, not a conformity claim.

---

## 9. Current-source scientific/regulatory validation

Closure was revalidated using existing canonical papers/guidelines plus current official 2025/2026 sources recorded in:

`docs/research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md`

Important new sources awaiting stable IDs in the single canonical `BIBLIOGRAPHY.md` include:

```text
ISO/IEC 25422:2025 — 3MF
ISO/ASTM 52915:2020 — AMF
ISO/ASTM 52951:2026 — AM data packages
EU MDR current consolidated text
MDCG 2019-11 rev.1 (2025)
MDCG 2021-24 rev.1 (2026)
MDCG 2019-16 rev.1
MDCG 2021-3
GDPR
ISO 14971:2019
ISO 13485:2016
ISO 9241-210:2019
IEC 62366-1:2015+A1:2020
FDA HFE 2026
WCAG 2.2
```

Bibliography normalization is maintenance work; it does not reopen frozen semantics.

---

## 10. Acceptance / V&V

`TRACEABILITY_MATRIX.md` v0.6 and the V&V master plan own coverage/evidence semantics.

New closure namespaces:

```text
PROF-013..014
INPUT-001..020
UX-001..022
XCHG-001..018
PERF-001..016
VV-001..018
REG-001..016
VIS-001..020
```

`docs/validation/P0_DOCUMENTATION_CLOSURE_ACCEPTANCE_ADDENDUM_2026-08-16.md` registers the post-authoring namespaces.

`TD-CI-001` remains non-blocking; registered tests are specifications, not claims of CI execution.

---

## 11. Geometry engine — PRESERVED / NO WINNER

Still valid:

```text
Geometry Engine Evaluation Scorecard v0.1
HG-01..HG-15
100-point weighted criteria
candidate-neutral Q0..Q7 plan
```

Primary candidates remain:

```text
A. product-owned domain layer + Pixar OpenSubdiv
B. product-owned domain layer + openNURBS / ON_SubD
```

No new product/visual document closes an engine gate by appearance.

If architecture work is resumed, start at Q0; do not restart generic library research.

---

## 12. Project Schema v0.2 / CI — unchanged

```text
Project Schema v0.2    APPROVED / NOT MATERIALIZED
TD-CI-001               DEFERRED / NON-BLOCKING
```

Do not modify schemas/fixtures/migrations or CI unless explicitly requested.

---

## 13. Exact remaining documentation/visual tasks

### DOCUMENTATION MAINTENANCE

Normalize new 2025/2026 sources into stable IDs in `docs/BIBLIOGRAPHY.md` without changing source roles or frozen requirements.

Optionally fold the closure/visual decisions into `DECISIONS.md` in a dedicated maintenance pass.

### VIS-03R / VIS-04R

When browser/render tooling is available:

```text
capture M01..M13 at 1440×960
capture M14 at 1024×768
include dark M07/M10
verify no runtime/console errors
inspect overflow/clipping/density/status readability
archive captures under docs/ux/mockups/v1/rendered/
record hashes/browser/version in manifest
rerun visual audit
```

### AFTER / PARALLEL

Geometry-engine Q0 may now resume if owner chooses; render capture/bibliography maintenance do not require reopening semantics.

---

## 14. DONE

- [x] DOC-00..DOC-14.
- [x] Six former `ACTIVE v0` product specs frozen v1.
- [x] `04/05` explicitly de-authorized as product truth.
- [x] Input/scan/reference contract.
- [x] Product workflow/interaction contract.
- [x] Interchange/handoff contract.
- [x] Realtime/performance doctrine.
- [x] V&V master plan.
- [x] Intended-use/risk/privacy/security boundary.
- [x] Final written audit: 0 blockers / GO.
- [x] Current scientific/standards/regulatory verification supplement.
- [x] Human-factors visual evidence baseline.
- [x] VIS-01 visual reference.
- [x] VIS-02 M01..M14 navigable HTML source.
- [x] VIS-03 source/version archive.
- [x] VIS-04 source-level requirement mapping and audit.
- [x] No engine selected prematurely.

---

## 15. TODO

- [ ] canonical `BIBLIOGRAPHY.md` stable-ID normalization for new current sources;
- [ ] `VIS-03R` rendered captures;
- [ ] `VIS-04R` browser/pixel/accessibility review;
- [ ] optional `DECISIONS.md` maintenance;
- [ ] resume Q0 only when requested/appropriate.

---

## 16. New-chat handover

`docs/NEXT_CHAT_PROMPT.md` should resume from the remaining documentation/visual maintenance tasks, or from Q0 only if the owner explicitly changes priority.
