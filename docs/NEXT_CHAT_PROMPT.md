# BiomechE-CAD — Next Chat Prompt

**Updated:** 2026-08-15  
**Purpose:** copy/paste this prompt into a new ChatGPT conversation to continue without reconstructing project context.

---

Continua il progetto **BiomechE-CAD** dal checkpoint documentale corrente.

Prima di qualsiasi modifica o nuova decisione, considera come documentazione canonica il repository:

`ww34ww34ww34/BiomechE-CAD`, branch `main`.

Leggi **in questo ordine**:

```text
docs/RESUME_HERE.md
docs/P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md
docs/SPEC_INDEX.md
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
docs/DECISIONS.md
docs/TECHNICAL_DEBT.md
docs/BIBLIOGRAPHY.md
```

## Stato da assumere

La fase di ricerca generale/funzionale e di progettazione semantica P0 è matura.

Sono già **FROZEN v1**:

```text
coordinate / registration semantics
BiomechE integration semantics
reporting / traceability semantics
pressure-acquisition qualification methodology
Geometry Authoring Contract
Workflow / Preset / Macro Contract
Numerical / Tolerance / Qualification Registry
P0 Authoring Acceptance Catalog — 22 semantic scenarios
```

Il cross-document audit ha trovato **0 contraddizioni semantiche bloccanti**.

`docs/spec/19_project_schema_v0_2_changeset.md` è **APPROVED CHANGE-SET / NOT MATERIALIZED**: non modificare ancora schema JSON, fixture o migrazioni salvo un task esplicito successivo.

## Debito tecnico CI — NON BLOCCANTE

`TD-CI-001` è deliberatamente differito dal project owner.

Non spendere tempo a riparare GitHub Actions, validator o fixture e non usare lo stato CI come gate per il lavoro corrente. Non dichiarare però `main` completamente qualificato. Quando il debito sarà riaperto, partire da `docs/TECHNICAL_DEBT.md`.

## Regole che NON devono essere riaperte senza una nuova evidenza/decisione

```text
EasyCAD2 = behavioral evidence, non verità scientifica
semantic prescription survives geometry
DesignRevision committed = immutable
capture context / landmark provenance = first class
placement = typed anatomical/reference semantics, non XYZ anonimo
geometry dose != mechanical/material dose
no hidden universal clinical default
OPEN means OPEN
algorithm tolerance != manufacturing tolerance != device limit != clinical threshold
CAD nominal != manufacturing artifact != physical accepted part
mirror is semantic and side-aware
workflow definitions use exact id/version/hash and preserve expanded historical operations
BiomechE remains quantitative KPI authority
architecture/kernel must satisfy the frozen contract, not redefine it
```

## Prossimo task principale

Procedi con **GEOMETRY ENGINE EVALUATION SCORECARD**.

Non scegliere subito una libreria.

Deriva prima una scorecard oggettiva direttamente dai contratti frozen e dai 22 casi `AUTH-C01..C22`.

Valuta almeno:

```text
product-owned clinical semantics isolation
stable/replayable geometry representation
SubD/surface quality
local parametric deformation
sculpt/freeform edit feasibility
mirror/bilateral support
surface point/normal/derivative queries
scan nearest-point / projection / conform support
section / distance / height / angle / thickness queries
deviation-map feasibility
production body / lower-surface / closure path
minimum-thickness/DFM support
determinism and numerical control
interactive performance and incremental invalidation
large scan handling
C++20 compatibility
single-core portability across desktop/server/web-WASM
web rendering/interoperability path
license
API stability
transitive dependency weight
serialization isolation
C#/.NET interoperability if useful
STL/3MF/CNC/manufacturing handoff
ability to satisfy each relevant frozen acceptance scenario
```

Principal candidates to start with:

```text
A. product-owned clinical layer + Pixar OpenSubdiv
B. product-owned clinical layer + openNURBS / ON_SubD
```

Considera OCCT, Manifold, CGAL, libigl, geometry-central o altre librerie **solo come componenti ausiliari** se un requisito frozen dimostra una necessità concreta. Non aggiungere dipendenze per capability teoriche.

Usa ricerca web aggiornata e **fonti primarie** per API, versioni, licenze, WASM, dipendenze e capability tecniche. Dove opportuno costruisci piccoli proof-of-concept/benchmark plan, ma prima definisci criteri, pesi, hard gate e scenari di confronto.

## Output richiesto nella nuova chat

1. audit rapido del checkpoint letto;
2. scorecard con hard gates vs weighted criteria;
3. mapping `GAUTH/WFLOW/NREG/AUTH-Cxx -> capability richiesta al geometry stack`;
4. confronto preliminare OpenSubdiv vs ON_SubD con fonti aggiornate;
5. lista delle incognite da verificare con PoC reali;
6. piano di benchmark/qualification dell'engine;
7. aggiornamento progressivo della documentazione nel repo;
8. sempre un riepilogo **DONE / TODO** e un handover aggiornato.

Non riaprire la ricerca generale sui CAD plantari salvo che emerga un gap concreto dalla scorecard.