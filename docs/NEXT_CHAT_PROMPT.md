# BiomechE-CAD — Next Chat Prompt

**Updated:** 2026-08-16  
**Purpose:** copy/paste into a new ChatGPT conversation to continue from the current checkpoint.

---

Continua il progetto **BiomechE-CAD** dal checkpoint corrente.

Repository canonico:

`ww34ww34ww34/BiomechE-CAD`, branch `main`.

## Leggi prima

```text
docs/RESUME_HERE.md
docs/P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md
docs/validation/P0_DOCUMENTATION_FINAL_CROSS_DOCUMENT_AUDIT_2026-08-16.md
docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
docs/ux/mockups/v1/manifest.md
docs/ux/VISUAL_REFERENCE_CROSS_DOCUMENT_AUDIT_2026-08-16.md
docs/ux/VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md
docs/ux/mockups/v1/rendered/README.md
docs/SPEC_INDEX.md
docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md
docs/TRACEABILITY_MATRIX.md
docs/spec/01_coordinate_registration.md
docs/spec/02_project_schema.md
docs/spec/06_corrective_elements.md
docs/spec/08_material_stiffness.md
docs/spec/09_analysis_qc_dfm.md
docs/spec/10_manufacturing.md
docs/spec/11_biomeche_integration.md
docs/spec/12_reporting_traceability.md
docs/spec/13_use_case_profiles.md
docs/spec/14_prom_comfort_adherence.md
docs/spec/15_pressure_acquisition_qualification.md
docs/spec/16_geometry_authoring_contract.md
docs/spec/17_workflow_preset_macro.md
docs/spec/18_numerical_qualification_registry.md
docs/spec/19_project_schema_v0_2_changeset.md
docs/spec/20_input_scan_reference_data.md
docs/spec/21_product_workflow_interaction.md
docs/spec/22_interchange_manufacturing_handoff.md
docs/spec/23_realtime_performance_contract.md
docs/validation/24_validation_verification_master_plan.md
docs/spec/25_intended_use_risk_privacy_security_boundary.md
docs/BIBLIOGRAPHY.md
docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
docs/DECISIONS.md
docs/TECHNICAL_DEBT.md
```

## Stato da assumere

La documentazione P0 è chiusa:

```text
DOC-00..DOC-14                   COMPLETE
WRITTEN DOCUMENTATION CLOSURE    GO
BLOCKING CONTRADICTIONS          0
```

La baseline visuale è chiusa a livello sorgente e browser:

```text
VIS-01 visual reference/design system        DONE
VIS-02 M01..M14 navigable HTML source        DONE
VIS-03 editable/source archive               DONE
VIS-04 requirement↔screen mapping/audit      DONE
VIS-03R-RUN 14/14 browser captures           DONE
VIS-04R browser/runtime/a11y audit           DONE — PASS WITH CORRECTIVE ITEMS
VIS-03R-ARCH repository PNG binaries         OPEN — packaging only
```

Browser audit:

```text
Chromium 144.0.7559.96
M01..M13 1440×960
M14      1024×768
M07/M10  dark
runtime exceptions 0
```

Canonical visual source:

`docs/ux/mockups/v1/biomeche-cad-mockups-v1.html`

Canonical browser audit:

`docs/ux/VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md`

The 14 PNGs were generated during the browser pass but the transient sandbox reset before binary transfer to GitHub. Do **not** claim that the PNG binary archive already exists. The destination/metadata contract is `docs/ux/mockups/v1/rendered/README.md`.

## Browser/a11y corrective items

Preserve into production implementation:

```text
VIS-A11Y-01
Meaningful M10 quantitative SVGs need accessible name/description,
or explicit decorative semantics only when equivalent accessible numeric data are adjacent.

VIS-A11Y-02
If viewport tool stand-ins become interactive, implement them as semantic controls
with keyboard support and programmatic name/role/state.

VIS-A11Y-03
Freeze and test an explicit visible focus treatment in light and dark modes.
```

These are implementation/presentation corrections, not changes to the frozen clinical/domain model.

## Bibliography

`docs/BIBLIOGRAPHY.md` is the single canonical authority and is now normalized as of 2026-08-16.

Stable IDs now cover the new current-source set, including:

```text
STD-ISOIEC-25422-2025
STD-ISOASTM-52915-2020
STD-ISOASTM-52951-2026
STD-ISO-14971-2019
STD-ISO-13485-2016
STD-ISO-9241-210-2019
STD-IEC-62366-1-2015-A1-2020
STD-W3C-WCAG-2.2
GUIDE-W3C-WCAG2ICT-2.2
REG-EU-MDR-2017-745
GUIDE-MDCG-2019-11-REV1-2025
GUIDE-MDCG-2021-24-REV1-2026
GUIDE-MDCG-2019-16-REV1
GUIDE-MDCG-2021-3
REG-EU-GDPR-2016-679
GUIDE-FDA-HFE-2026
```

Do not turn a standards/guidance entry into automatic conformance, certification, legal classification or a clinical threshold.

## Product semantics frozen

Do not reopen without new evidence/decision:

```text
committed DesignRevision immutable
original source != processed/registered/derived
capture context + landmark provenance first-class
file coordinates != anatomical coordinates
placement typed anatomical/reference, not raw XYZ authority
requested dose != realized CAD dose
geometry dose != mechanical/material dose
semantic prescription survives geometry
mirror semantic + side-aware
no hidden universal clinical default
OPEN means OPEN
algorithm tolerance != device limit != manufacturing tolerance != clinical threshold != performance budget
pressure heatmap != quantitative authority
BiomechE quantitative KPI authority
profile != diagnosis
suggestion != confirmation
pain/function/comfort/fit/satisfaction/adherence distinct
MeasuredOutcome != PredictedOutcome
DesignRevision != ManufacturingArtifact != ManufacturingRun != PhysicalOrthosis
CAD nominal != measured manufactured geometry
file format != semantic authority
preview != commit != manufacturing release
```

## Historical engineering docs

`04_base_template.md` = ENGINEERING CANDIDATE / QUALIFICATION FIXTURE.

`05_parametric_orthosis_geometry.md` = PROVISIONAL ENGINEERING MATHEMATICAL REFERENCE.

`41×17`, Catmull-Clark/OpenSubdiv, specific formulas/sample values are not frozen product requirements.

## Project Schema / CI

```text
Project Schema v0.2   APPROVED / NOT MATERIALIZED
TD-CI-001              DEFERRED / NON-BLOCKING
```

Do not modify schema JSON, fixtures, migrations or CI unless explicitly tasked.

## Preferred next task — engineering

The written + browser visual baseline is now sufficient to resume:

```text
Q0 — Geometry Engine Qualification
```

Do not restart generic library research.

Candidates remain:

```text
A. product-owned domain layer + Pixar OpenSubdiv
B. product-owned domain layer + openNURBS / ON_SubD
```

No winner selected.

Qualification sequence:

```text
Q0 native/server/WASM build + dependency audit
Q1 candidate-neutral geometry/replay/query fixture
Q2 local authoring/sculpt/mirror
Q3 scan/spatial queries/inspection
Q4 production body/DFM
Q5 determinism/incremental/performance
Q6 interop/.NET/manufacturing handoff
Q7 AUTH-C01..C22 engine-backed qualification
```

Performance must always be measured under `23_realtime_performance_contract.md`; without approved `ARCH-PERF-*` budgets use `MEASURED / NOT YET QUALIFIED`.

## Optional mechanical visual packaging

If a persistent binary-transfer/render path is available, recreate/store:

```text
docs/ux/mockups/v1/rendered/M01-case-1440x960.png
...
docs/ux/mockups/v1/rendered/M14-compact-1024x768.png
```

and record source blob/browser/version/viewport/device-scale/hash/file size. This is archival packaging, not an architecture-entry blocker.

## Output at every phase transition

Update:

```text
TRACEABILITY_MATRIX.md
SPEC_INDEX.md
RESUME_HERE.md
NEXT_CHAT_PROMPT.md
```

Keep DONE/TODO explicit and never claim evidence that was not actually executed.
