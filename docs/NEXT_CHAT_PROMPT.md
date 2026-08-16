# BiomechE-CAD — Next Chat Prompt

**Updated:** 2026-08-16  
**Purpose:** copy/paste this prompt into a new ChatGPT conversation to continue without reconstructing project context.

---

Continua il progetto **BiomechE-CAD** dal checkpoint corrente.

Repository canonico:

`ww34ww34ww34/BiomechE-CAD`, branch `main`.

## Leggi prima

```text
docs/RESUME_HERE.md
docs/P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md
docs/SPEC_INDEX.md
docs/P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md
docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md
docs/TRACEABILITY_MATRIX.md
docs/spec/01_coordinate_registration.md
docs/spec/02_project_schema.md
docs/spec/16_geometry_authoring_contract.md
docs/spec/17_workflow_preset_macro.md
docs/spec/18_numerical_qualification_registry.md
docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md
docs/spec/19_project_schema_v0_2_changeset.md
docs/validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md
docs/validation/P0_AUTHORING_ACCEPTANCE_INTEGRATION_ADDENDUM.md
docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
docs/DECISIONS.md
docs/TECHNICAL_DEBT.md
docs/BIBLIOGRAPHY.md
```

## Stato da assumere

Il nucleo P0 authoring è già maturo e frozen.

Sono authoritative/frozen:

```text
coordinate / registration
BiomechE integration
reporting / traceability
pressure-acquisition qualification methodology
Geometry Authoring Contract v1
Workflow / Preset / Macro Contract v1
Numerical / Tolerance / Qualification Registry v1
P0 Authoring Acceptance Catalog — AUTH-C01..C22
```

Il precedente cross-document audit ha trovato **0 contraddizioni semantiche bloccanti**.

Project Schema v0.2 è **APPROVED CHANGE-SET / NOT MATERIALIZED**. Non modificare JSON Schema, fixture o migrazioni salvo task esplicito.

`TD-CI-001` resta deliberatamente differito e non è un gate per questa fase.

## Priorità corrente: P0-DOC-CLOSURE

Il project owner ha deciso di continuare la documentazione **prima** di eseguire i PoC del geometry engine.

Il piano canonico è:

`docs/P0_DOCUMENTATION_CLOSURE_AND_VISUAL_REFERENCE_PLAN_2026-08-16.md`

Non ripartire da Q0, a meno che il project owner lo richieda esplicitamente.

## PROSSIMO TASK ESATTO — DOC-00

Esegui un audit completo della documentazione P0 e crea:

`docs/validation/P0_DOCUMENTATION_CLOSURE_AUDIT_2026-08-16.md`

L'audit deve:

1. inventariare tutti i documenti `docs/spec/*`;
2. classificarli come `FROZEN`, `CANONICAL ACTIVE`, `PROVISIONAL`, `HISTORICAL/SUPERSEDED`, `QUALIFICATION-DEPENDENT`;
3. verificare quale documento è authority per ciascun concetto;
4. identificare duplicazioni/semantiche pre-freeze che confliggono o sono superate da `16/17/18`;
5. confermare i veri gap documentali;
6. definire un criterio di chiusura/freeze per ogni documento non chiuso;
7. verificare la posizione di `04_base_template.md` e `05_parametric_orthosis_geometry.md`;
8. verificare l'anomalia di numerazione `06 -> 08` senza inventare un `07` solo per riempire il numero;
9. proporre eventuali correzioni al piano soltanto se l'audit trova evidenza concreta.

Non selezionare o implementare un geometry engine durante DOC-00.

## Ordine di lavoro dopo DOC-00

```text
DOC-01  06 corrective elements -> v1
DOC-02  08 material/stiffness -> v1
DOC-03  09 analysis/QC/DFM -> v1
DOC-04  10 manufacturing -> v1
DOC-05  13 use-case profiles -> v1
DOC-06  14 PROM/comfort/adherence -> v1
DOC-07  04/05 disposition
DOC-08  input/scan/reference data contract
DOC-09  product workflow & interaction contract
DOC-10  interchange/manufacturing handoff contract
DOC-11  realtime interaction & performance contract
DOC-12  validation & verification master plan
DOC-13  intended-use/risk/privacy/security package
DOC-14  final cross-document closure audit
```

Regulatory/security facts in DOC-13 devono essere verificati da fonti primarie correnti.

## Visual reference — parte obbligatoria del piano

Dopo la stabilizzazione della documentazione scritta, creare e salvare nel repository un **visual reference package v1**.

Proposed paths:

```text
docs/ux/BIOMECHE_CAD_VISUAL_REFERENCE_V1.md
docs/ux/mockups/v1/
```

Mockup minimi:

```text
M01 project/patient/case
M02 import/scan qualification
M03 registration/landmarks
M04 base orthosis/template
M05 parametric authoring
M06 corrective/offloading elements
M07 sculpt/local edit
M08 materials/regional mechanical prescription
M09 inspection/geometry QC
M10 BiomechE before/after/delta
M11 DFM/manufacturing preparation
M12 revision/provenance/report
M13 physical-part QC/outcome follow-up
M14 compact/responsive reference
```

Preferire, quando pratico:

```text
editable/source-controlled mockup (HTML/CSS, SVG o equivalente)
+
rendered reference image (PNG o equivalente)
```

Ogni mockup deve essere versionato e avere un manifest con mapping ai requisiti/spec.

Regola:

```text
WRITTEN SPECIFICATION = SEMANTIC AUTHORITY
MOCKUP = VISUAL / INTERACTION REFERENCE
```

## Principi frozen da non riaprire senza nuova evidenza/decisione

```text
semantic prescription survives geometry
committed DesignRevision immutable
capture context + landmark provenance first-class
placement typed anatomical/reference semantics, not raw XYZ
geometry dose != mechanical/material dose
no hidden universal clinical default
OPEN means OPEN
algorithm tolerance != manufacturing tolerance != device limit != clinical threshold
CAD nominal != ManufacturingArtifact != PhysicalOrthosis
mirror semantic + side-aware
workflow/preset exact id/version/hash, preserve historical expansion
BiomechE quantitative KPI authority
geometry kernel must satisfy frozen contract, not redefine it
```

## Geometry engine state — preserved, not cancelled

Scorecard and PoC plan remain valid. No winner is selected.

Candidates remain:

```text
A. product-owned domain layer + Pixar OpenSubdiv
B. product-owned domain layer + openNURBS / ON_SubD
```

Architecture qualification remains `Q0..Q7`, but is deferred until documentation/visual closure unless explicitly reprioritized.

## Performance doctrine

Performance remains central. DOC-11 must define a candidate-neutral product performance contract.

Do not invent PASS thresholds. Until an explicit `ARCH-PERF-*` budget is approved, results remain:

```text
MEASURED / NOT YET QUALIFIED
```

## Output richiesto per ogni task

- aggiornamento documentale nel repository;
- evidenza e rationale delle modifiche;
- nessun default universale inventato;
- cross-check con frozen contracts;
- aggiornamento di `TRACEABILITY_MATRIX.md`, `SPEC_INDEX.md`, `RESUME_HERE.md` e questo handover quando lo stato cambia;
- DONE/TODO sempre chiari.

Non ripartire dalla ricerca generale sui CAD plantari. Nuova ricerca solo se guidata da un gap reale della documentazione o da un requisito di DOC-13.