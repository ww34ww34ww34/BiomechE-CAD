# BiomechE-CAD — Next Chat Prompt

**Updated:** 2026-08-16  
**Purpose:** copy/paste into a new ChatGPT conversation to continue from the current checkpoint.

---

Continua il progetto **BiomechE-CAD** dal checkpoint corrente.

Repository canonico: `ww34ww34ww34/BiomechE-CAD`, branch `main`.

## Leggi prima

```text
docs/RESUME_HERE.md
docs/SPEC_INDEX.md
docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md
docs/TRACEABILITY_MATRIX.md
docs/DECISIONS.md
docs/DECISIONS_2026-08-16_CLOSURE_Q0_ADDENDUM.md
docs/spec/16_geometry_authoring_contract.md
docs/spec/17_workflow_preset_macro.md
docs/spec/18_numerical_qualification_registry.md
docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md
docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
docs/research/architecture/GEOMETRY_ENGINE_Q0_EVIDENCE_UPDATE_2026-08-16.md
qualification/geometry-engine/q0/README.md
qualification/geometry-engine/q0/candidate-lock.json
qualification/geometry-engine/q0/results/Q0_EVIDENCE_STATUS_2026-08-16.md
qualification/geometry-engine/q0/results/Q0_HARNESS_VALIDATION_2026-08-16.md
docs/BIBLIOGRAPHY.md
```

## Stato da assumere

La parte documentale/visuale P0 è chiusa:

```text
DOC-00..DOC-14                    COMPLETE
written blockers                  0
P0 documentation closure          GO
bibliography normalization        DONE
M01..M14 visual source            DONE
browser renders                   14/14 DONE
browser/runtime/a11y audit        DONE — PASS WITH corrective items
PNG binary archive in GitHub      OPEN — packaging only / NON-BLOCKING
```

Project Schema v0.2 = **APPROVED / NOT MATERIALIZED**.

`TD-CI-001` = **DEFERRED / NON-BLOCKING**.

Non modificare schema JSON/fixture/migrazioni o CI salvo task esplicito.

## Principi frozen

```text
committed DesignRevision immutable
original source != processed/registered/derived
capture context + landmark provenance first-class
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
MeasuredOutcome != PredictedOutcome
DesignRevision != ManufacturingArtifact != ManufacturingRun != PhysicalOrthosis
CAD nominal != measured manufactured geometry
file format != semantic authority
preview != commit != manufacturing release
geometry kernel satisfies frozen contract, never redefines it
```

`04_base_template.md` e `05_parametric_orthosis_geometry.md` restano engineering hypotheses/qualification references, non product authority.

## Current phase — Q0 Geometry Engine Qualification

No winner è selezionato.

Exact candidate locks:

```text
OpenSubdiv
  tag       v3_7_0
  commit    9dab8a47bfbb1388ec8388fe61f5f916e6123f38

openNURBS / ON_SubD
  ref       8.x snapshot
  commit    00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
```

Q0 executable harness is already in:

`qualification/geometry-engine/q0/`

Implemented:

```text
candidate lock manifest
common C++20 adapter.hpp
common headless smoke main
OpenSubdiv smoke adapter
openNURBS smoke adapter
candidate-specific CMake containment modules
native/WASM evidence runner run_q0.py
Q0 evidence ledger
Q0 harness validation report
```

Harness validation actually executed:

```text
Python runner syntax                         PASS
missing-Emscripten NOT_EXECUTED semantics    PASS
common C++20 adapter contract                PASS
candidate source-shape smoke                 PASS
```

Actual candidate builds are still:

```text
OpenSubdiv native       NOT EXECUTED
OpenSubdiv server       NOT EXECUTED
OpenSubdiv direct WASM  NOT EXECUTED
openNURBS native        NOT EXECUTED
openNURBS server        NOT EXECUTED
openNURBS direct WASM   NOT EXECUTED
```

Do not convert API/source inspection into build PASS.

## PROSSIMO TASK ESATTO

Execute Q0 on a machine/environment that has the exact pinned source trees and Emscripten/native toolchains.

Use:

```bash
python qualification/geometry-engine/q0/run_q0.py --candidate opensubdiv --source-root <OpenSubdiv-v3_7_0> --mode native --clean
python qualification/geometry-engine/q0/run_q0.py --candidate opensubdiv --source-root <OpenSubdiv-v3_7_0> --mode wasm --clean
python qualification/geometry-engine/q0/run_q0.py --candidate opennurbs --source-root <opennurbs-00bdd2ce> --mode native --clean
python qualification/geometry-engine/q0/run_q0.py --candidate opennurbs --source-root <opennurbs-00bdd2ce> --mode wasm --clean
```

Collect/commit:

```text
configure/build/runtime exit
compiler/CMake/Emscripten versions
flags
build duration
static/dynamic dependency evidence
binary/WASM size
artifact SHA-256
stdout/stderr
```

Only then update:

```text
HG-01 semantic isolation
HG-10 one-core native/server/WASM
HG-13 license/distribution review state
HG-14 dependency containment
```

If Q0 is acceptable, proceed to Q1 common geometry/replay/query fixture. Do not restart generic library research.

## Performance doctrine

Performance remains central and must be measured under `docs/spec/23_realtime_performance_contract.md`.

Until explicit `ARCH-PERF-*` budgets exist:

```text
MEASURED / NOT YET QUALIFIED
```

## Visual residual

When a persistent binary-transfer path is available, recreate/store the 14 PNGs under:

`docs/ux/mockups/v1/rendered/`

following `rendered/README.md`. This is archival packaging, not a Q0 blocker.

## At each phase transition

Update:

```text
docs/TRACEABILITY_MATRIX.md
docs/SPEC_INDEX.md
docs/RESUME_HERE.md
docs/NEXT_CHAT_PROMPT.md
```

Keep DONE/TODO explicit and never claim unexecuted evidence.
