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
docs/validation/P0_DOCUMENTATION_CLOSURE_ACCEPTANCE_ADDENDUM_2026-08-16.md
docs/research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md
docs/research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md
docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
docs/DECISIONS.md
docs/TECHNICAL_DEBT.md
docs/BIBLIOGRAPHY.md
```

## Stato da assumere

Il lavoro di documentazione P0 è chiuso:

```text
DOC-00..DOC-14                   COMPLETE
WRITTEN DOCUMENTATION CLOSURE    GO
BLOCKING CONTRADICTIONS          0
```

È completata anche la baseline visuale **a livello sorgente**:

```text
VIS-01 visual reference/design system        DONE
VIS-02 M01..M14 navigable HTML source        DONE
VIS-03 editable/source archive               DONE
VIS-04 requirement ↔ screen mapping/audit    DONE
VIS-03R rendered PNG archive                 PENDING
VIS-04R browser/pixel/accessibility audit    PENDING
```

Artifact visuale canonico:

```text
docs/ux/mockups/v1/biomeche-cad-mockups-v1.html
```

Non dichiarare PNG/pixel golden già validati: il browser/render pass non è stato eseguito.

## Product semantics frozen

Non riaprire senza nuova evidenza/decisione:

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

`04_base_template.md` è **ENGINEERING CANDIDATE / QUALIFICATION FIXTURE**, non product authority.

`05_parametric_orthosis_geometry.md` è **PROVISIONAL ENGINEERING MATHEMATICAL REFERENCE**, non product authority.

Quindi `41×17`, Catmull-Clark/OpenSubdiv, formule di bump/smooth/wedge/scan-conform e sample values non sono requisiti frozen.

## Project Schema / CI

```text
Project Schema v0.2   APPROVED / NOT MATERIALIZED
TD-CI-001              DEFERRED / NON-BLOCKING
```

Non modificare schema JSON, fixture, migrazioni o CI salvo task esplicito.

## Fonti / bibliografia

La closure è stata validata con paper/guideline già canonici e con fonti ufficiali correnti 2025/2026 registrate in:

```text
docs/research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md
docs/research/VISUAL_HUMAN_FACTORS_EVIDENCE_2026-08-16.md
```

Resta manutenzione utile normalizzare in `BIBLIOGRAPHY.md` stable ID per:

```text
ISO/IEC 25422:2025 — 3MF
ISO/ASTM 52915:2020 — AMF
ISO/ASTM 52951:2026 — AM data packages
EU MDR
MDCG 2019-11 rev.1
MDCG 2021-24 rev.1
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

Questa normalizzazione non deve cambiare le semantiche frozen.

## Se l'obiettivo resta documentale/visuale

Procedi con:

### A. Bibliography normalization

Integra le nuove fonti correnti nel singolo `docs/BIBLIOGRAPHY.md`, mantenendo la tassonomia/ID governance esistente. Non creare una seconda bibliography authority.

### B. VIS-03R / VIS-04R quando hai un renderer/browser disponibile

```text
apri l'esatto HTML committed
cattura M01..M13 a 1440×960
cattura M14 a 1024×768
includi M07/M10 dark
verifica console/runtime
controlla clipping/overflow/density/status readability
verifica contrast/accessibility quanto richiesto
salva sotto docs/ux/mockups/v1/rendered/
registra browser/version/device-scale/hash in manifest
riesegui visual audit
```

## Se il proprietario decide di passare all'engineering

Riprendi **Q0 Geometry Engine Qualification**, senza una nuova ricerca generica sulle librerie.

Candidati ancora invariati:

```text
A. product-owned domain layer + Pixar OpenSubdiv
B. product-owned domain layer + openNURBS / ON_SubD
```

Nessun vincitore è selezionato.

Sequenza:

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

Performance deve sempre essere misurata secondo `23_realtime_performance_contract.md`; senza un budget esplicito usare `MEASURED / NOT YET QUALIFIED`.

## Visual authority

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
CANONICAL HTML/MOCKUP  = VISUAL / INTERACTION SOURCE REFERENCE
```

Se un mockup contraddice una spec frozen, correggere il mockup.

## Output richiesto a ogni cambio fase

Aggiornare:

```text
TRACEABILITY_MATRIX.md
SPEC_INDEX.md
RESUME_HERE.md
NEXT_CHAT_PROMPT.md
```

mantenendo DONE/TODO chiari e senza dichiarare evidenze non realmente eseguite.
