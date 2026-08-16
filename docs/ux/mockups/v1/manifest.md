# BiomechE-CAD — Mockup Manifest v1

**Status:** CANONICAL VISUAL PACKAGE MANIFEST v1  
**Date:** 2026-08-16  
**Visual spec:** `../../BIOMECHE_CAD_VISUAL_REFERENCE_V1.md`

---

## Package assets

| Asset | Role | Status |
|---|---|---|
| `biomeche-cad-mockups-v1.html` | Self-contained editable/navigable mockup source | VIS-02 target |
| `README.md` | Package/readme/version policy | DONE |
| `manifest.md` | Screen → specification/acceptance map | ACTIVE |
| `rendered/M01...M14.png` | Canonical rendered captures | generate when render tooling is available |

Primary reference viewport is 1440×960 unless a screen states otherwise. M14 uses compact landscape reference.

---

## Common requirements applied to all screens

```text
VR-01..VR-10
HF-VIS-001..010
VIS-001 case+side context where clinically relevant
VIS-002 preview/working/committed/released distinction where applicable
VIS-003 redundant warning/blocking/unresolved cues
VIS-005 numeric units/legibility
VIS-007 provenance progressive disclosure
VIS-016 focus/selection/active-tool/side distinction
VIS-019 requirement mapping
VIS-020 asset metadata/versioning
```

---

## M01 — Project / Patient / Case

```text
ID: M01
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: choose/resume correct case and expose side/profile/revision/source state before authoring
```

Owning specs / acceptance:

```text
21_product_workflow_interaction: UX-001, UX-002, UX-021
13_use_case_profiles: PROF-001, PROF-005, PROF-011
20_input_scan_reference_data: INPUT-005, INPUT-019
02_project_schema / 12_reporting_traceability
VIS-001, VIS-002, VIS-003, VIS-012, VIS-019, VIS-020
HF-VIS-001, HF-VIS-002
```

Must depict: case list, LEFT/RIGHT design cards, profile badges, latest committed revision, unresolved source/warning count.

---

## M02 — Import / Scan Qualification

```text
ID: M02
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: distinguish original/processed/registered sources and expose unresolved capture/geometry state
```

Owning specs / acceptance:

```text
20_input_scan_reference_data: INPUT-001..009, INPUT-018..020
21_product_workflow_interaction: UX-002, UX-003, UX-017
01_coordinate_registration
15_pressure_acquisition_qualification where pressure source is shown
VIS-003, VIS-007, VIS-013
HF-VIS-001, HF-VIS-002, HF-VIS-005
```

Must depict: source list, original/derived badges, unit state, side provenance, capture condition, scanner/device context, mesh-quality warning, processing lineage.

---

## M03 — Registration / Landmarks

```text
ID: M03
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: review suggested/confirmed landmarks and source→anatomical registration
```

Owning specs / acceptance:

```text
01_coordinate_registration
20_input_scan_reference_data: INPUT-010..013
16_geometry_authoring_contract: GAUTH acquisition/landmark/registration family
21_product_workflow_interaction: UX-004, UX-005
AUTH-C09, AUTH-C10
VIS-003, VIS-006, VIS-007, VIS-012, VIS-016
```

Must depict: 3D scan, landmarks, landmark table, suggested vs confirmed state, residual/quality summary, registration method/provenance.

---

## M04 — Base Orthosis / Template

```text
ID: M04
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: choose exact template definition and size/fit without exposing candidate engine topology as product semantics
```

Owning specs / acceptance:

```text
16_geometry_authoring_contract
17_workflow_preset_macro
21_product_workflow_interaction: UX-005, UX-006, UX-007
GAUTH-* relevant base/template authoring
VIS-002, VIS-005, VIS-006, VIS-007
```

Must depict: versioned template gallery/list, compatibility/source, preview over scan, metric size/length/width controls, Preview/Apply/Cancel.

Explicit limitation: no `41×17`/OpenSubdiv control cage is shown as clinical UI authority.

---

## M05 — Parametric Authoring

```text
ID: M05
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: fast semantic arch/heel/post/outline editing with direct+numeric control
```

Owning specs / acceptance:

```text
16_geometry_authoring_contract: GAUTH-* / AUTH-C01..03, C08
21_product_workflow_interaction: UX-005..009
18_numerical_qualification_registry
ARCH-* / HEEL-*
VIS-002, VIS-004, VIS-005, VIS-006, VIS-011, VIS-016
HF-VIS-003, HF-VIS-004, HF-VIS-005
```

Must depict: dominant 3D viewport, semantic tool family, numeric inspector, requested/realized pair, operation stack, Apply/Cancel then Commit separate.

---

## M06 — Corrective / Offloading Elements

```text
ID: M06
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: place a named corrective element relative to anatomy/ROI with evidence/profile context
```

Owning specs / acceptance:

```text
06_corrective_elements: CE-001..010
16_geometry_authoring_contract: AUTH-C04/C05
13_use_case_profiles
21_product_workflow_interaction: UX-005, UX-012, UX-018
09_analysis_qc_dfm target+safety-ring semantics
VIS-004, VIS-005, VIS-006, VIS-007, VIS-012
```

Must depict: element family, target, typed/landmark-relative placement, requested dose, mechanical profile, preset/evidence provenance, target+safety-ring overlay.

---

## M07 — Sculpt / Local Editing

```text
ID: M07
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: DARK REPRESENTATIVE
Purpose: freeform refinement with replayable brush semantics and protected regions
```

Owning specs / acceptance:

```text
16_geometry_authoring_contract: AUTH-C06, GAUTH sculpt/replay
21_product_workflow_interaction: UX-013
23_realtime_performance_contract: PERF-005, PERF-014, PERF-015
VIS-002, VIS-005, VIS-006, VIS-016, VIS-017
HF-VIS-003, HF-VIS-005
```

Must depict: brush footprint, raise/lower/smooth, radius, strength, direction/reference, protected regions, preview/calculating state, compact operation history.

---

## M08 — Materials / Mechanical Prescription

```text
ID: M08
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: assign regional material/mechanical dose independently of geometry
```

Owning specs / acceptance:

```text
08_material_stiffness: MAT-001..018
21_product_workflow_interaction: UX-014
10_manufacturing material/lot linkage
18_numerical_qualification_registry
VIS-005, VIS-007, VIS-014
```

Must depict: 3D material region overlay, exact MaterialDefinition revision, property source, layer stack, interfaces, nominal/measured/calibrated/modelled labels.

---

## M09 — Inspection / Geometry QC

```text
ID: M09
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: reproducible geometry inspection with units/reference/method and requested-vs-realized values
```

Owning specs / acceptance:

```text
09_analysis_qc_dfm: AQ-009/AQ-010 and geometric QC
16_geometry_authoring_contract: AUTH-C11..C14
21_product_workflow_interaction: UX-015
18_numerical_qualification_registry
VIS-004, VIS-005, VIS-007
```

Must depict: linked 3D + section, measurement list, thickness/deviation state, measurement definition provenance, no tolerance without authority.

---

## M10 — BiomechE Before / After / Delta

```text
ID: M10
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: DARK REPRESENTATIVE
Purpose: quantitative biomechanical comparison with visible protocol compatibility
```

Owning specs / acceptance:

```text
11_biomeche_integration: BINT-*
09_analysis_qc_dfm: AQ-001..009
15_pressure_acquisition_qualification
06_corrective_elements target/safety-ring outcome
21_product_workflow_interaction: UX-016
VIS-003, VIS-005, VIS-008, VIS-009, VIS-010, VIS-017
```

Must depict: BASELINE/OUTCOME/DELTA maps, legend+units, metric/ROI selector, numeric comparison table, compatibility state, target+safety-ring/remote metrics.

---

## M11 — DFM / Manufacturing Preparation

```text
ID: M11
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: distinguish design readiness, artifact generation and manufacturing release
```

Owning specs / acceptance:

```text
10_manufacturing: MAN-001..018
09_analysis_qc_dfm DFM
22_interchange_manufacturing_handoff: XCHG-*
21_product_workflow_interaction: UX-017, UX-019
18_numerical_qualification_registry
VIS-002, VIS-003, VIS-005, VIS-007, VIS-011
HF-VIS-004, HF-VIS-006
```

Must depict: profile/revision, production geometry preview, orientation/units, DFM check rows, QC plan, generated artifact state, separate high-consequence Release action.

---

## M12 — Revision / Provenance / Report

```text
ID: M12
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: inspect immutable revision history and complete provenance/report lineage
```

Owning specs / acceptance:

```text
12_reporting_traceability: RPT-*
02_project_schema
17_workflow_preset_macro
21_product_workflow_interaction: UX-008, UX-009, UX-021
VIS-002, VIS-007
```

Must depict: revision timeline/graph, working vs committed, selected revision summary, source/operation/preset/workflow lineage, report artifacts, expandable exact hashes.

---

## M13 — Physical-Part QC / Outcome Follow-up

```text
ID: M13
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1440×960
Theme: LIGHT
Purpose: distinguish the actual physical part from design/artifact/run and connect QC/service/outcomes
```

Owning specs / acceptance:

```text
10_manufacturing: MAN-* physical-part lifecycle
08_material_stiffness service state
14_prom_comfort_adherence: PROM-*
09_analysis_qc_dfm
21_product_workflow_interaction: UX-020
12_reporting_traceability
VIS-003, VIS-005, VIS-007, VIS-015
```

Must depict: PhysicalOrthosis identity, design/artifact/run/material lots, QC result, physical scan/deviation, issue/service state, multidimensional patient-experience timeline.

---

## M14 — Responsive / Compact Reference

```text
ID: M14
Version: 1.0
Status: CANONICAL MOCKUP TARGET
Viewport: 1024×768
Theme: LIGHT
Purpose: demonstrate preservation of critical context in constrained landscape layout
```

Owning specs / acceptance:

```text
21_product_workflow_interaction: UX-022
VIS-001, VIS-002, VIS-003, VIS-005, VIS-016, VIS-018
WCAG/HF-VIS evidence baseline
```

Must depict: collapsed nav, dominant viewport, persistent case+side+state, inspector drawer affordance, bottom metric sheet, visible warning. Does not claim phone/full authoring parity.

---

## Required state coverage across package

| State | At least one screen |
|---|---|
| EMPTY | M01/M02 |
| NORMAL | all |
| SELECTED | M03/M05/M06/M08/M09 |
| PREVIEW | M04/M05/M07 |
| CALCULATING | M07/M10 |
| STALE | M10 |
| WARNING | M02/M10/M11/M14 |
| BLOCKING | M02/M11 |
| UNRESOLVED | M01/M02/M03 |
| SUGGESTED | M03/M06 |
| CONFIRMED | M03/M06 |
| COMMITTED | M01/M12 |
| RELEASED | M11/M12/M13 |
| NOT_COMPARABLE | M10 |

---

## Visual-closure rule

VIS-04 may close only when:

1. the editable mockup contains all M01..M14 screens;
2. every screen can be reached from its screen navigator;
3. manifest entries match actual screen content;
4. no mockup introduces an unsupported clinical/manufacturing numerical default;
5. high-risk state/action distinctions remain visible;
6. requirement ↔ screen mapping is complete;
7. rendered captures are archived where the available rendering toolchain permits it.
