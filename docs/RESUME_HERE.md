# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-16  
**Current phase:** **Q0 GEOMETRY ENGINE QUALIFICATION — HARNESS READY / REAL CANDIDATE BUILDS NEXT.**  
**Selection status:** **NO GEOMETRY ENGINE SELECTED.**  
**P0 product documentation:** COMPLETE / GO / 0 blockers.  
**Visual baseline:** source + browser audit COMPLETE; PNG repository archive remains packaging-only.

Project Schema v0.2 remains **APPROVED / NOT MATERIALIZED**. `TD-CI-001` remains deliberately deferred and non-blocking.

---

## 1. Read first

1. `docs/RESUME_HERE.md`
2. `docs/SPEC_INDEX.md`
3. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
4. `docs/TRACEABILITY_MATRIX.md`
5. `docs/DECISIONS.md`
6. `docs/DECISIONS_2026-08-16_CLOSURE_Q0_ADDENDUM.md`
7. `docs/spec/16_geometry_authoring_contract.md`
8. `docs/spec/17_workflow_preset_macro.md`
9. `docs/spec/18_numerical_qualification_registry.md`
10. `docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`
11. `docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md`
12. `docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`
13. `docs/research/architecture/GEOMETRY_ENGINE_Q0_EVIDENCE_UPDATE_2026-08-16.md`
14. `qualification/geometry-engine/q0/README.md`
15. `qualification/geometry-engine/q0/candidate-lock.json`
16. `qualification/geometry-engine/q0/results/Q0_EVIDENCE_STATUS_2026-08-16.md`
17. `qualification/geometry-engine/q0/results/Q0_HARNESS_VALIDATION_2026-08-16.md`
18. `docs/BIBLIOGRAPHY.md`
19. `docs/NEXT_CHAT_PROMPT.md`

Written/visual closure references remain available under `docs/validation/` and `docs/ux/` but are no longer the current execution point.

---

## 2. Frozen product principles

Do not reopen without explicit new evidence/decision:

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
geometry kernel must satisfy frozen contracts, never redefine them
```

---

## 3. Completed product / documentation / visual state

```text
DOC-00..DOC-14                               COMPLETE
written cross-document blockers             0
P0 documentation closure                    GO
canonical bibliography normalization        DONE
VIS-01 visual brief                         DONE
VIS-02 M01..M14 HTML source                 DONE
VIS-03 source/version archive               DONE
VIS-04 requirement↔screen traceability      DONE
VIS-03R-RUN 14/14 browser captures          DONE
VIS-04R browser/runtime/a11y audit          DONE — PASS WITH corrective items
VIS-03R-ARCHIVE PNG files in GitHub         OPEN — packaging only
```

Browser reference:

```text
Chromium 144.0.7559.96
M01..M13 1440×960
M14      1024×768
M07/M10  dark
runtime exceptions 0
```

Visual implementation corrections to preserve:

```text
VIS-A11Y-01 meaningful quantitative graphics need accessible naming/description or explicit decorative semantics + equivalent accessible numeric data
VIS-A11Y-02 interactive viewport tools must be semantic controls with keyboard/name/role/state
VIS-A11Y-03 explicit tested focus-visible treatment in light/dark
```

---

## 4. Q0 candidate locks

### OpenSubdiv

```text
tag       v3_7_0
commit    9dab8a47bfbb1388ec8388fe61f5f916e6123f38
```

### openNURBS / ON_SubD

```text
ref       8.x snapshot
commit    00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
```

These are qualification pins, not final production selections.

---

## 5. Q0 harness — READY

Implemented under:

`qualification/geometry-engine/q0/`

```text
candidate-lock.json
CMakeLists.txt
include/biomeche_q0/adapter.hpp
src/main.cpp
src/candidate_opensubdiv.cpp
src/candidate_opennurbs.cpp
cmake/CandidateOpenSubdiv.cmake
cmake/CandidateOpenNurbs.cmake
run_q0.py
results/Q0_EVIDENCE_STATUS_2026-08-16.md
results/Q0_HARNESS_VALIDATION_2026-08-16.md
```

Common rule:

```text
one product-owned C++20 adapter boundary
candidate-native types stay inside candidate implementation units
same headless smoke executable for native/server/WASM
no candidate-specific product semantics
```

Harness validation actually executed:

```text
Python runner syntax                    PASS
missing-Emscripten NOT_EXECUTED path    PASS
common C++20 adapter contract           PASS
candidate source-shape smoke            PASS
```

---

## 6. Q0 real candidate execution — NEXT

Current truth:

```text
OpenSubdiv native Release       NOT EXECUTED
OpenSubdiv headless/server      NOT EXECUTED
OpenSubdiv direct WASM          NOT EXECUTED
openNURBS native Release        NOT EXECUTED
openNURBS headless/server       NOT EXECUTED
openNURBS direct WASM           NOT EXECUTED
```

The chat execution environment has CMake/C++/Node but no Emscripten and no usable direct clone/DNS path for bringing the pinned upstream source trees into the local container. Therefore no candidate build PASS/FAIL is claimed here.

Exact runner:

```bash
python qualification/geometry-engine/q0/run_q0.py --candidate opensubdiv --source-root <OpenSubdiv-v3_7_0> --mode native --clean
python qualification/geometry-engine/q0/run_q0.py --candidate opensubdiv --source-root <OpenSubdiv-v3_7_0> --mode wasm --clean
python qualification/geometry-engine/q0/run_q0.py --candidate opennurbs --source-root <opennurbs-00bdd2ce> --mode native --clean
python qualification/geometry-engine/q0/run_q0.py --candidate opennurbs --source-root <opennurbs-00bdd2ce> --mode wasm --clean
```

Generated JSON results must be committed before any Q0 hard gate is promoted to PASS.

---

## 7. Current architecture-gate state

```text
HG-01 semantic isolation       POSITIVE STRUCTURAL EVIDENCE / BUILD CONFIRMATION PENDING
HG-10 native+server+WASM       UNKNOWN / EXECUTION REQUIRED
HG-13 license/distribution     UPSTREAM TERMS CAPTURED / FORMAL REVIEW REQUIRED
HG-14 dependency containment   PARTIAL POSITIVE EVIDENCE / BUILD CONFIRMATION PENDING
HG-15 full frozen acceptance   Q7 PENDING
```

No final weighted score and no winner are authorized.

Selection sequence remains:

```text
HARD GATES -> Q0..Q7 EXECUTED EVIDENCE -> WEIGHTED CRITERIA -> FINAL DECISION
```

---

## 8. Historical engineering documents remain subordinate

```text
04_base_template.md                 ENGINEERING CANDIDATE / QUALIFICATION FIXTURE
05_parametric_orthosis_geometry.md PROVISIONAL ENGINEERING MATHEMATICAL REFERENCE
```

`41×17`, Catmull-Clark/OpenSubdiv and provisional formulas/sample values are not frozen product requirements.

---

## 9. DONE

- [x] P0 written documentation closure / 0 blockers.
- [x] canonical bibliography normalized.
- [x] visual source M01..M14 + browser audit.
- [x] visual human-factors corrective items recorded.
- [x] Q0 exact upstream candidate pins.
- [x] Q0 product-owned C++20 adapter boundary.
- [x] Q0 native/WASM evidence runner.
- [x] Q0 harness validation.
- [x] no engine winner selected prematurely.

---

## 10. TODO — exact restart point

1. **Execute Q0 against the pinned upstream source trees** on a machine with native toolchain + Emscripten.
2. Commit generated JSON evidence and dependency/binary-size data.
3. Update HG-01/HG-10/HG-13/HG-14 strictly from executed evidence.
4. If Q0 passes sufficiently, proceed to Q1 common geometry/replay/query fixture.
5. Separately, when convenient, recreate/store the 14 PNG binaries under `docs/ux/mockups/v1/rendered/`; this is not an architecture blocker.

Do not restart generic CAD/library research.
