# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-16  
**Current phase:** **WRITTEN P0 DOCUMENTATION CLOSURE GO — VISUAL REFERENCE PACKAGE NEXT.**  
**Architecture status:** **NO GEOMETRY ENGINE SELECTED. Q0..Q7 plan preserved / execution deferred until VIS closure or explicit reprioritization.**

The written P0 product/semantic documentation has now completed `DOC-00..DOC-14` with **0 blocking cross-document contradictions**. The next work is `VIS-01..VIS-04`: create, save and trace a canonical visual reference/mockup package without changing the frozen product semantics.

Project Schema v0.2 remains **APPROVED / NOT MATERIALIZED**. `TD-CI-001` remains deliberately deferred and non-blocking.

---

## 1. Read these first

1. `docs/RESUME_HERE.md`
2. `docs/P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md`
3. `docs/validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md`
4. `docs/SPEC_INDEX.md`
5. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
6. `docs/TRACEABILITY_MATRIX.md`
7. `docs/spec/01_coordinate_registration.md`
8. `docs/spec/02_project_schema.md`
9. `docs/spec/06_corrective_elements.md`
10. `docs/spec/08_material_stiffness.md`
11. `docs/spec/09_analysis_qc_dfm.md`
12. `docs/spec/10_manufacturing.md`
13. `docs/spec/11_biomeche_integration.md`
14. `docs/spec/12_reporting_traceability.md`
15. `docs/spec/13_use_case_profiles.md`
16. `docs/spec/14_prom_comfort_adherence.md`
17. `docs/spec/15_pressure_acquisition_qualification.md`
18. `docs/spec/16_geometry_authoring_contract.md`
19. `docs/spec/17_workflow_preset_macro.md`
20. `docs/spec/18_numerical_qualification_registry.md`
21. `docs/spec/19_project_schema_v0_2_changeset.md`
22. `docs/spec/20_input_scan_reference_data.md`
23. `docs/spec/21_product_workflow_interaction.md`
24. `docs/spec/22_interchange_manufacturing_handoff.md`
25. `docs/spec/23_realtime_performance_contract.md`
26. `docs/validation/24_validation_verification_master_plan.md`
27. `docs/spec/25_intended_use_risk_privacy_security_boundary.md`
28. `docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`
29. `docs/research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md`
30. `docs/BIBLIOGRAPHY.md`
31. `docs/NEXT_CHAT_PROMPT.md`

`BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` remains the functional authority. The old functional spec and the old engine-first documents are historical/reference material only.

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

The geometry engine is downstream infrastructure and cannot become domain authority.

---

## 3. Frozen product principles — do not reopen without new evidence/decision

- EasyCAD2 is behavioral evidence, not scientific truth.
- A committed `DesignRevision` is immutable.
- Semantic prescription survives final geometry.
- Original source evidence survives processing/registration.
- Capture context and landmark provenance are first-class.
- Placement is typed anatomical/reference semantics, not raw XYZ authority.
- Requested dose and realized geometry remain distinct.
- Geometry dose and mechanical/material dose are distinct.
- Mirror is semantic and side-aware.
- Reusable definitions resolve exact `id + version + hash/snapshot` and preserve historical expansion.
- Pressure is quantitative; heatmaps are derived views.
- Offloading is target + safety ring/adjacent + remote redistribution.
- Profiles are context, not diagnoses.
- PROM/function/comfort/fit/satisfaction/adherence remain distinct.
- `MeasuredOutcome != PredictedOutcome`.
- `UNAVAILABLE`/`MISSING`/`NOT_COMPARABLE` are never zero.
- `OPEN` remains `OPEN`.
- Algorithm tolerance, device limit, manufacturing tolerance, clinical threshold and performance budget are separate authorities.
- BiomechE is quantitative KPI authority; CAD owns prescription/design/lifecycle semantics.
- `DesignRevision != ManufacturingArtifact != ManufacturingRun != PhysicalOrthosis`.
- CAD nominal geometry != measured manufactured geometry.
- File format != product semantic authority.
- Preview != commit != manufacturing release.
- Suggestion != human confirmation.
- The geometry kernel must satisfy frozen contracts, never redefine them.

Canonical units remain:

```text
mm, s, N, kPa, deg, mm²
```

---

## 4. Written documentation closure — COMPLETE

Canonical final audit:

`docs/validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md`

Verdict:

```text
DOC-00 baseline inventory                    PASS
DOC-01 corrective elements v1               FROZEN
DOC-02 material & stiffness v1               FROZEN
DOC-03 analysis/QC/DFM v1                    FROZEN
DOC-04 manufacturing v1                     FROZEN
DOC-05 use-case profiles v1                  FROZEN
DOC-06 PROM/comfort/adherence v1             FROZEN
DOC-07 04/05 engineering disposition         DONE
DOC-08 input/scan/reference                  FROZEN
DOC-09 product workflow/interaction          FROZEN
DOC-10 interchange/handoff                   FROZEN
DOC-11 realtime/performance doctrine         FROZEN; budgets OPEN
DOC-12 V&V master plan                       CANONICAL
DOC-13 intended-use/risk/privacy/security    CANONICAL boundary; regulatory decision OPEN
DOC-14 final cross-document audit            PASS
BLOCKING CONTRADICTIONS                      0
WRITTEN DOCUMENTATION CLOSURE                GO
```

---

## 5. New frozen/canonical contracts

### `06_corrective_elements.md` — FROZEN v1

```text
named corrective element
+ typed anatomical placement
+ requested/realized dose
+ mechanical profile separation
+ target/safety-ring/remote outcome semantics
+ side-aware mirror
```

No literature placement becomes a universal hidden preset.

### `08_material_stiffness.md` — FROZEN v1

```text
material family != supplier formulation
hardness != modulus
nominal != measured/effective/service-aged property
base material != lattice/structural effective property
```

### `09_analysis_qc_dfm.md` — FROZEN v1

```text
GEOMETRIC QC != BIOMECHANICAL OUTCOME != ACQUISITION QUALITY != DFM QC
```

### `10_manufacturing.md` — FROZEN v1

```text
DesignRevision
!= ManufacturingGeometry/Artifact
!= ManufacturingRun
!= PhysicalOrthosis
!= Accepted PhysicalOrthosis
```

### `13_use_case_profiles.md` — FROZEN v1

Profile is contextual interpretation, not diagnosis or automatic prescription. Active diabetic-ulcer treatment is not silently conflated with recurrence-prevention footwear/insole workflow.

### `14_prom_comfort_adherence.md` — FROZEN v1

Construct-before-instrument, exact version/language/scoring/license context, multidimensional outcomes, explicit adherence denominator/method.

### `20_input_scan_reference_data.md` — FROZEN v1

```text
ORIGINAL != PROCESSED != REGISTERED != DERIVED
```

Units, side, frame, capture conditions, processing, landmarks, ROI and registration are provenance.

### `21_product_workflow_interaction.md` — FROZEN v1

End-to-end state/interaction contract; visual implementation still open.

### `22_interchange_manufacturing_handoff.md` — FROZEN v1

Format capability/loss manifests, explicit units/frame/orientation and product-owned manufacturing package.

### `23_realtime_performance_contract.md` — FROZEN doctrine v1

Performance is always measured; no invented budgets. Until explicit EngineeringPerformanceProfile exists:

```text
MEASURED / NOT YET QUALIFIED
```

### `validation/24_validation_verification_master_plan.md` — CANONICAL v1

One evidence hierarchy/result-state model across semantic, numerical, UI, performance, hardware, manufacturing and outcome evidence.

### `25_intended_use_risk_privacy_security_boundary.md` — CANONICAL boundary v1

Final MDR software qualification/classification, QMS scope, DPIA/security architecture and future AI Act applicability remain deliberately OPEN pending formal intended-purpose/deployment assessment.

---

## 6. Engineering hypotheses — explicitly not product authority

### `04_base_template.md`

```text
41x17 topology
Catmull-Clark/OpenSubdiv choice
vertex/index mapping
specific control spacing
```

are **qualification fixtures/hypotheses**, not frozen requirements.

### `05_parametric_orthosis_geometry.md`

Exact bump/smooth/wedge/arch/scan-conform formulas, displacement directions, sample angles and numerical bounds are **algorithm hypotheses**, not clinical/product authority.

---

## 7. Current source verification / bibliography

Closure was validated against existing canonical papers/guidelines and current official standards/regulatory sources.

Temporary source record:

`docs/research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md`

New current sources still to normalize into stable `BIBLIOGRAPHY.md` IDs include:

```text
ISO/IEC 25422:2025 — 3MF
ISO/ASTM 52915:2020 — AMF v1.2
ISO/ASTM 52951:2026 — AM data packages
EU MDR current consolidated text
MDCG 2019-11 rev.1 (2025)
MDCG 2021-24 rev.1 (2026)
MDCG 2019-16 rev.1
MDCG 2021-3
GDPR
ISO 14971:2019
ISO 13485:2016
```

This normalization is maintenance work and does not block VIS.

---

## 8. Acceptance / V&V

`TRACEABILITY_MATRIX.md` is now canonical v0.6.

New namespaces:

```text
PROF-013..014
INPUT-001..020
UX-001..022
XCHG-001..018
PERF-001..016
VV-001..018
REG-001..016
```

Registered by:

`docs/validation/P0_DOCUMENTATION_CLOSURE_ACCEPTANCE_ADDENDUM_2026-08-16.md`

The older `functional_acceptance_suite.md` remains useful for historical/integration scenarios but its old namespace ranges do not override owning frozen specs or the V&V master plan.

---

## 9. Visual reference package — EXACT NEXT PHASE

Owner requirement: save a versioned visual reference after written semantics are stable.

Target:

```text
docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
docs/ux/mockups/v1/README.md
docs/ux/mockups/v1/manifest.md
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
M14 Responsive / compact view
```

Prefer both editable/source-controlled assets and rendered references where practical.

Authority rule:

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
MOCKUP = VISUAL / INTERACTION REFERENCE
```

---

## 10. Geometry engine evaluation — preserved / deferred

Still valid:

```text
Geometry Engine Evaluation Scorecard v0.1
HG-01..HG-15
100-point weighted criteria
candidate-neutral Q0..Q7 plan
OpenSubdiv vs openNURBS/ON_SubD primary candidates
NO WINNER
```

Architecture execution resumes after VIS closure unless owner explicitly reprioritizes.

No library enters merely because a mockup appears to need a feature.

---

## 11. Project Schema v0.2 / CI — unchanged

```text
Project Schema v0.2   APPROVED / NOT MATERIALIZED
TD-CI-001              DEFERRED / NON-BLOCKING
```

Do not modify schemas/fixtures/migrations or repair CI during VIS unless explicitly requested.

---

## 12. DONE

- [x] DOC-00..DOC-14 written closure.
- [x] Six former ACTIVE-v0 product specs frozen v1.
- [x] `04/05` de-authorized as engineering hypotheses.
- [x] Input/scan/reference contract.
- [x] Product workflow/interaction contract.
- [x] Interchange/manufacturing-handoff contract.
- [x] Realtime/performance doctrine.
- [x] V&V Master Plan.
- [x] Intended-use/risk/privacy/security boundary.
- [x] Final cross-document audit: 0 blockers / GO.
- [x] Traceability v0.6.
- [x] New acceptance namespaces registered.
- [x] 2026 source-verification supplement recorded.
- [x] No engine selected prematurely.

---

## 13. TODO — exact restart point

### NEXT — VIS-01

Create:

`docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md`

It must define:

```text
visual principles
information architecture
workspace anatomy
component vocabulary
state/warning/blocking language
side/profile/provenance visibility
3D viewport + inspectors + quantitative panels
light/dark/medical palette direction
responsive/compact policy
M01..M14 screen briefs
```

### THEN — VIS-02

Generate/save the M01..M14 canonical mockups.

### THEN — VIS-03

Archive editable/source assets + rendered references with manifest/version/status.

### THEN — VIS-04

Map each screen to relevant specs/acceptance IDs and perform visual-closure audit.

### PARALLEL OPTIONAL

Normalize new 2025/2026 sources into stable `BIBLIOGRAPHY.md` IDs.

### AFTER VIS CLOSURE

Resume geometry engine Q0 unless owner reprioritizes.

---

## 14. New-chat handover

`docs/NEXT_CHAT_PROMPT.md` must resume from **VIS-01 canonical visual reference brief**, not from DOC-00 and not from geometry-engine Q0.
