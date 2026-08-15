# BiomechE-CAD — Next Chat Prompt

**Updated:** 2026-08-15  
**Purpose:** copy/paste this prompt into a new ChatGPT conversation to continue without reconstructing project context.

---

Continua il progetto **BiomechE-CAD** dal checkpoint corrente.

Repository canonico:

`ww34ww34ww34/BiomechE-CAD`, branch `main`.

Prima di fare modifiche o prendere nuove decisioni, leggi almeno in questo ordine:

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
docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
docs/DECISIONS.md
docs/TECHNICAL_DEBT.md
docs/BIBLIOGRAPHY.md
```

## Stato da assumere

La ricerca generale/funzionale e la progettazione semantica P0 sono mature.

Sono **FROZEN v1**:

```text
coordinate / registration semantics
BiomechE integration semantics
reporting / traceability semantics
pressure-acquisition qualification methodology
Geometry Authoring Contract
Workflow / Preset / Macro Contract
Numerical / Tolerance / Qualification Registry
P0 Authoring Acceptance Catalog — AUTH-C01..C22
```

Il cross-document audit ha trovato **0 contraddizioni semantiche bloccanti**.

Project Schema v0.2 è **APPROVED CHANGE-SET / NOT MATERIALIZED**. Non modificare JSON Schema, fixture o migrazioni salvo task esplicito.

## Geometry Engine Evaluation — stato corrente

La **Geometry Engine Evaluation Scorecard v0.1 è stata completata**.

Sono stati definiti, prima di qualunque selezione:

```text
HG-01..HG-15 hard gates
16 weighted criteria = 100 punti
mapping GAUTH/WFLOW/NREG -> capability richiesta
mapping AUTH-C01..C22 -> architecture tests
PoC/benchmark uncertainties
candidate-neutral qualification plan Q0..Q7
```

**NON È STATO SELEZIONATO ALCUN ENGINE.**

Candidati principali invariati:

```text
A. product-owned clinical/domain layer + Pixar OpenSubdiv
B. product-owned clinical/domain layer + openNURBS / ON_SubD
```

Primary-source snapshot corrente:

- OpenSubdiv: evidenza forte per evaluator SubD focalizzato, deformazioni a topologia statica, limit/basis derivatives e core C++ con dipendenze minime;
- ON_SubD/openNURBS: evidenza forte per toolkit geometrico più ampio, limit/surface point, tangent/normal, cache/invalidation e interoperabilità 3DM;
- `rhino3dm 8.32.1`: evidenza concreta di famiglia openNURBS per .NET e JavaScript/WebAssembly, ma non prova la parità completa delle API authoring ON_SubD in WASM;
- nearest-point/projection, production body/closure/min-thickness/DFM, determinismo e workload performance restano selection-critical PoC per entrambi.

Non attribuire una capability perché “Rhino la sa fare”: usare soltanto API openNURBS/ON_SubD/rhino3dm realmente esposte o un PoC del nostro adapter.

## Regole che NON devono essere riaperte senza nuova evidenza/decisione

```text
semantic prescription survives geometry
committed DesignRevision = immutable
capture context / landmark provenance = first class
placement = typed anatomical/reference semantics, non XYZ anonimo
geometry dose != mechanical/material dose
no hidden universal clinical default
OPEN means OPEN
algorithm tolerance != manufacturing tolerance != device limit != clinical threshold
CAD nominal != ManufacturingArtifact != PhysicalOrthosis
mirror = semantic and side-aware
workflow/preset = exact id/version/hash + preserved historical expansion
BiomechE = quantitative KPI authority
the geometry kernel must satisfy the frozen contract, not redefine it
```

## Debito tecnico CI — NON BLOCCANTE

`TD-CI-001` resta deliberatamente differito.

Non spendere tempo a riparare GitHub Actions, validator o fixture. Non usare CI come gate della fase corrente e non dichiarare `main` completamente qualificato. Quando il debito sarà riaperto, partire da `docs/TECHNICAL_DEBT.md`.

## PROSSIMO TASK PRINCIPALE — Q0 Geometry Engine PoC Qualification

Procedi ora con la prima fase eseguibile del piano, **senza scegliere un vincitore e senza ottimizzare un candidato prima di aver costruito la stessa baseline per l'altro**.

### Q0-A — Native C++20 build / dependency audit

Per OpenSubdiv e openNURBS/ON_SubD:

```text
pin exact upstream tag + commit
build Release sul toolchain C++20 scelto
build headless/server
crea lo stesso narrow product-owned adapter/harness
cattura compiler/version/flags
cattura static/dynamic link graph
cattura transitive dependency manifest
cattura binary footprint
verifica che nessun tipo kernel diventi semantic persisted state
```

Baseline upstream da verificare nuovamente al momento dell'esecuzione:

```text
OpenSubdiv v3.7.0
openNURBS v8.32.26160.13001
rhino3dm 8.32.1 = interoperability evidence, non dependency obbligatoria
```

### Q0-B — Direct WebAssembly build

Compila lo **stesso product-owned C++ core/adapter** con Emscripten/WASM per entrambi.

Misura almeno:

```text
compile success/failure
WASM binary size
startup/init
baseline/peak heap
thread/SIMD configuration if used
surface query smoke test
native-vs-WASM numerical delta
render-buffer extraction path
```

Non dare OpenSubdiv/WASM per scontato solo perché è C++. Non dare ON_SubD authoring/WASM per scontato solo perché esiste rhino3dm.js.

### Dopo Q0 — Q1 shared canonical fixture

Se entrambi restano candidati, costruisci una sola candidate-neutral `FIX-GEOM-01` e prova:

```text
product-owned serialization -> kernel reconstruction
stable control/address mapping
limit point
Du/Dv or equivalent tangent data
normal
replay equivalence
explicit invalidation behavior
```

Solo dopo passare a local authoring/sculpt/mirror.

## Performance doctrine

Registra sempre performance e memoria, ma **non inventare soglie PASS**.

Finché non viene approvato un engineering profile `ARCH-PERF-*`, usare:

```text
MEASURED / NOT YET QUALIFIED
```

Raccogli almeno:

```text
min/p50/p95/p99/max/mean
sample count
cold vs steady state
peak memory/WASM heap
allocations where practical
control/faces/render triangles
scan tier if applicable
invalidation scope
compiler/toolchain/flags
candidate tag/commit
```

Replay epsilon deve essere un esplicito `ALGORITHM_NUMERICAL_TOLERANCE`; non deve mai usare una manufacturing acceptance tolerance.

## Auxiliary libraries

OCCT, Manifold, CGAL, libigl, geometry-central o altro entrano solo se un hard gate frozen + PoC dimostra un gap concreto.

Il trigger più probabile da testare è `HG-08`:

```text
production lower surface
offset/closure/watertight body
self-intersection / solid validation
minimum thickness / DFM
```

Non aggiungere un general-purpose CAD kernel preventivamente.

## Output richiesto

1. audit del checkpoint corrente;
2. esecuzione documentata di Q0 per entrambi i candidati, se il repo/tooling disponibile lo permette;
3. result manifest riproducibile per ciascun candidato;
4. confronto native/server/WASM e dependency footprint;
5. hard gates aggiornati `PASS/FAIL/UNKNOWN` con evidence grade;
6. nessuna selezione finché restano gate critici aperti;
7. aggiornamento progressivo di scorecard, qualification report, `TRACEABILITY_MATRIX.md`, `RESUME_HERE.md` e questo handover;
8. DONE/TODO sempre aggiornati.

Non ripartire dalla ricerca generale sui CAD plantari. La ricerca successiva deve essere esclusivamente guidata da un gap della scorecard/PoC.