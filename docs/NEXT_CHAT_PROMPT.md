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
docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
docs/DECISIONS.md
docs/TECHNICAL_DEBT.md
docs/BIBLIOGRAPHY.md
```

## Stato da assumere

**DOC-00..DOC-14 sono completati.**

Il final cross-document audit ha dato:

```text
WRITTEN DOCUMENTATION CLOSURE    GO
BLOCKING CONTRADICTIONS          0
```

Sono ora FROZEN/canonical anche:

```text
06 corrective/offloading elements
08 material/stiffness
09 analysis/QC/DFM
10 manufacturing lifecycle
13 use-case profiles
14 PROM/comfort/adherence
20 input/scan/reference data
21 product workflow/interaction
22 interchange/manufacturing handoff
23 realtime/performance doctrine (budget numerici OPEN)
24 V&V master plan
25 intended-use/risk/privacy/security boundary (classificazione normativa OPEN)
```

`04_base_template.md` e `05_parametric_orthosis_geometry.md` sono esplicitamente **engineering hypotheses / qualification references**, non product authority.

Project Schema v0.2 resta **APPROVED / NOT MATERIALIZED**. Non modificare JSON Schema, fixture o migrazioni salvo task esplicito.

`TD-CI-001` resta deliberatamente differito e non è un gate.

## PROSSIMO TASK ESATTO — VIS-01

Crea il canonical visual-reference brief:

```text
docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
```

Deve tradurre le specifiche frozen in una direzione visuale/interattiva coerente, senza inventare nuove regole cliniche.

Definisci almeno:

```text
visual principles
information architecture
workspace anatomy
navigation model
3D viewport anatomy
right/left + case/profile persistent context
inspector/property panels
quantitative/BiomechE panels
warning/blocking/unresolved states
requested vs realized presentation
source/provenance/revision presentation
material/mechanical presentation
manufacturing/QC state presentation
light/dark palette direction
typography/iconography density
responsive/compact policy
visual accessibility rules
```

Usa come interaction authority:

`docs/spec/21_product_workflow_interaction.md`.

## VIS-02 — canonical mockups

Poi genera e salva nel repo un set visuale coerente:

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

Target structure:

```text
docs/ux/mockups/v1/README.md
docs/ux/mockups/v1/manifest.md
source/editable assets
rendered canonical references
```

Quando pratico, conservare sia sorgente modificabile sia immagine/rendering di riferimento.

## VIS-03 — versioning

Ogni schermata deve avere:

```text
screen ID
version
status
viewport
theme
purpose
source asset
rendered asset
owning specs
acceptance IDs
limitations
supersedes/superseded-by
```

## VIS-04 — requirement ↔ screen traceability

Crea una matrice che colleghi ogni `Mxx` almeno a:

```text
21_product_workflow_interaction / UX-*
owning domain specs
INPUT/CE/MAT/AQ/MAN/BINT/RPT/REG as relevant
state/error/empty variants
```

Chiudi con un visual cross-document audit.

## Regola di authority visuale

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
MOCKUP = VISUAL / INTERACTION REFERENCE
```

Se un mockup sembra contraddire una specifica frozen, correggere il mockup; non cambiare automaticamente la specifica.

## Direzione estetica

Il visual reference deve essere professionale, medicale e premium, con alta densità informativa da workstation CAD ma senza look da CAD industriale anni 2000.

Preferire:

```text
pulito / contemporaneo
medical-tech
light + dark coerenti
superfici soft / moderatamente glass solo dove utile
3D al centro
comandi semantici chiari
sidebar/inspector ordinati
numeri/units/provenance facilmente leggibili
colori di stato non come unico segnale
```

Evita viola dominante. I mockup precedenti del progetto possono ispirare la direzione medical/pastello, ma le specifiche frozen decidono il contenuto.

## Principi frozen da non riaprire

```text
semantic prescription survives geometry
committed DesignRevision immutable
original source != processed/registered/derived
capture context + landmark provenance first-class
placement typed anatomical/reference, not raw XYZ
requested dose != realized dose
geometry dose != mechanical/material dose
no hidden universal clinical default
OPEN means OPEN
algorithm tolerance != manufacturing tolerance != device limit != clinical threshold != performance budget
CAD nominal != ManufacturingArtifact != ManufacturingRun != PhysicalOrthosis
mirror semantic + side-aware
workflow/preset exact id/version/hash
profile != diagnosis
suggestion != confirmation
BiomechE quantitative KPI authority
file format != semantic authority
preview != commit != manufacturing release
```

## Architecture state — preserved / deferred

No engine è selezionato.

Candidates remain:

```text
A. product-owned domain layer + Pixar OpenSubdiv
B. product-owned domain layer + openNURBS / ON_SubD
```

Q0..Q7 riparte soltanto dopo VIS closure salvo diversa priorità esplicita.

## Bibliography/source maintenance

`docs/research/CURRENT_SOURCE_SUPPLEMENT_2026-08-16.md` registra fonti correnti 2025/2026 ancora da normalizzare in `BIBLIOGRAPHY.md` (3MF/AMF/AM data packages, MDR/MDCG, GDPR, ISO 14971/13485).

Questa normalizzazione può essere fatta in parallelo al VIS ma non deve riaprire le specifiche.

## Output richiesto

- file visual-reference canonici nel repo;
- mockup realmente salvati/versionati;
- mapping requisiti↔screen;
- nessuna nuova regola clinica introdotta dalla grafica;
- aggiornamento di `TRACEABILITY_MATRIX.md`, `SPEC_INDEX.md`, `RESUME_HERE.md` e questo handover al cambio fase;
- DONE/TODO chiari.

Non ripartire dalla ricerca generale sui CAD plantari e non ripartire da DOC-00/Q0.
