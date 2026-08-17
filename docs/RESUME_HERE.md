# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint date:** 2026-08-17  
**Immediate continuation:** **VISUAL DIRECTION V2 — SURFACE-CAD WORKSTATION / V2-S01 REVIEW.**  
**Architecture phase:** **Q0 GEOMETRY ENGINE QUALIFICATION — READY / TEMPORARILY PARKED DURING VISUAL REFINEMENT.**  
**Selection status:** **NO GEOMETRY ENGINE SELECTED.**  
**P0 product documentation:** COMPLETE / GO / 0 blockers.  
**V1 visual baseline:** COMPLETE as functional/state/traceability evidence.  
**V2 visual direction:** ACTIVE / NOT YET FROZEN.

Project Schema v0.2 remains **APPROVED / NOT MATERIALIZED**. `TD-CI-001` remains deliberately deferred and non-blocking.

---

## 1. Read first

For the current visual continuation, read in this order:

1. `docs/RESUME_HERE.md`
2. `docs/ux/BIOMECHE_CAD_VISUAL_DIRECTION_V2_SURFACE_CAD_2026-08-17.md`
3. `docs/ux/mockups/v2/README.md`
4. `docs/DECISIONS_2026-08-17_VISUAL_V2_ADDENDUM.md`
5. `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`
6. `docs/TRACEABILITY_MATRIX.md`
7. `docs/SPEC_INDEX.md`
8. `docs/NEXT_CHAT_PROMPT.md`

When returning to architecture/Q0, additionally read:

9. `docs/DECISIONS_2026-08-16_CLOSURE_Q0_ADDENDUM.md`
10. `docs/spec/16_geometry_authoring_contract.md`
11. `docs/spec/17_workflow_preset_macro.md`
12. `docs/spec/18_numerical_qualification_registry.md`
13. `docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`
14. `docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md`
15. `docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`
16. `docs/research/architecture/GEOMETRY_ENGINE_Q0_EVIDENCE_UPDATE_2026-08-16.md`
17. `qualification/geometry-engine/q0/README.md`
18. `qualification/geometry-engine/q0/candidate-lock.json`
19. `qualification/geometry-engine/q0/results/Q0_EVIDENCE_STATUS_2026-08-16.md`
20. `qualification/geometry-engine/q0/results/Q0_HARNESS_VALIDATION_2026-08-16.md`
21. `docs/BIBLIOGRAPHY.md`

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

## 3. Product/documentation closure state

```text
DOC-00..DOC-14                               COMPLETE
written cross-document blockers             0
P0 documentation closure                    GO
canonical bibliography normalization        DONE
Project Schema v0.2                         APPROVED / NOT MATERIALIZED
TD-CI-001                                   DEFERRED / NON-BLOCKING
```

Historical engineering documents remain subordinate:

```text
04_base_template.md                 ENGINEERING CANDIDATE / QUALIFICATION FIXTURE
05_parametric_orthosis_geometry.md PROVISIONAL ENGINEERING MATHEMATICAL REFERENCE
```

`41×17`, Catmull-Clark/OpenSubdiv and provisional formulas/sample values are not frozen product requirements.

---

## 4. Visual V1 — retained functional baseline

V1 remains complete and useful for functional/state/traceability coverage:

```text
VIS-01 visual brief                         DONE
VIS-02 M01..M14 HTML source                 DONE
VIS-03 source/version archive               DONE
VIS-04 requirement↔screen traceability      DONE
VIS-03R-RUN 14/14 browser captures          DONE
VIS-04R browser/runtime/a11y audit          DONE — PASS WITH corrective items
VIS-03R-REPRODUCIBILITY                     DONE — versioned renderer + capture-manifest SHA-256 contract
materialized PNG copies                     OPTIONAL derived review cache
```

Canonical V1 reproducible renderer:

`docs/ux/mockups/v1/rendered/render_reference.py`

Visual implementation corrections to preserve:

```text
VIS-A11Y-01 meaningful quantitative graphics need accessible naming/description or explicit decorative semantics + equivalent accessible numeric data
VIS-A11Y-02 interactive viewport tools must be semantic controls with keyboard/name/role/state
VIS-A11Y-03 explicit tested focus-visible treatment in light/dark
```

V1 is **not** the preferred V2 aesthetic.

---

## 5. Visual V2 — current active direction

Canonical V2 direction document:

`docs/ux/BIOMECHE_CAD_VISUAL_DIRECTION_V2_SURFACE_CAD_2026-08-17.md`

Workspace register:

`docs/ux/mockups/v2/README.md`

Decision addendum:

`docs/DECISIONS_2026-08-17_VISUAL_V2_ADDENDUM.md`

Core aesthetic decision:

```text
HIGH-LEVEL INDUSTRIAL SURFACE CAD
not medical dashboard
not SaaS cards
not decorative Jarvis/HUD sci-fi
```

Visual grammar:

```text
dominant geometry viewport
dark graphite neutral chrome
compact monochrome CAD tools
contextual properties
Scene/Layers hierarchy
surface curves/control points/sections when relevant
restrained blue active state
amber/orange selected geometry
rich neutral geometry rendering
minimal decorative glow
orthotic data remains contextual, not dominant
```

Explicitly rejected directions:

```text
five-screen marketing collage as the actual screen design
KPI-dashboard visual identity
large medical cards
neon/circuit HUD decoration
rainbow heatmap everywhere
small geometry surrounded by UI chrome
consumer-app density
```

### V2 five-screen sequence

```text
V2-S01 Template / Modello                 REVIEW
V2-S02 Superficie / Edit Parametrico      NOT GENERATED
V2-S03 Elementi                           NOT GENERATED
V2-S04 Scultura / Post Processing         NOT GENERATED
V2-S05 Analisi / Produzione               NOT GENERATED
```

**Important:** generate/review **one full-screen image at a time**.

Approval protocol:

```text
GENERATE -> REVIEW -> REVISE -> EXPLICIT APPROVAL -> PERSIST -> NEXT SCREEN
```

The latest V2-S01 image generated on 2026-08-17 is a **candidate only**, not yet approved/frozen.

### Exact visual restart point

Resume by refining **V2-S01 Template / Modello only**.

The target should resemble a serious premium surface-modeling workstation:

- full application window, no poster framing;
- top mode tabs `MODELLO / SUPERFICIE / SCULTURA / ANALISI / PRODUZIONE`;
- compact CAD toolbar;
- central orthosis surface occupying most attention;
- neutral clay/graphite surface with selected reference curve/control points;
- metric dimensions;
- compact pressure/Scan2D/Scan3D references on the left;
- Scene/Layers and contextual base/template parameters on the right;
- optional small top/side/rear views;
- bottom units/grid/snap/status bar;
- no decorative neon/Jarvis effects.

Do not move to V2-S02 until the user explicitly approves S01.

---

## 6. Q0 candidate locks — preserved

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

## 7. Q0 harness — READY / parked

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

Actual candidate builds remain:

```text
OpenSubdiv native Release       NOT EXECUTED
OpenSubdiv headless/server      NOT EXECUTED
OpenSubdiv direct WASM          NOT EXECUTED
openNURBS native Release        NOT EXECUTED
openNURBS headless/server       NOT EXECUTED
openNURBS direct WASM           NOT EXECUTED
```

No final weighted score and no winner are authorized.

When visual work is paused/completed, the architecture restart point remains: execute Q0 against the exact pinned source trees on a machine with native toolchain + Emscripten, commit generated JSON evidence, then update HG-01/HG-10/HG-13/HG-14 strictly from executed evidence.

---

## 8. Current DONE

- [x] P0 written documentation closure / 0 blockers.
- [x] canonical bibliography normalized.
- [x] V1 visual functional/state baseline complete.
- [x] reproducible V1 renderer and audit.
- [x] V2 Surface-CAD visual doctrine captured.
- [x] V2 five-workspace sequence defined.
- [x] rejected visual directions documented.
- [x] V2-S01 current candidate state recorded as REVIEW, not approved.
- [x] Q0 exact candidate pins and harness preserved.
- [x] no engine winner selected prematurely.

---

## 9. Current TODO / exact restart

### Immediate

1. Refine **V2-S01 Template / Modello** only.
2. Get explicit user approval.
3. Persist the approved visual asset and mark `V2-S01 = APPROVED` in `docs/ux/mockups/v2/README.md`.
4. Then generate V2-S02.

### Architecture after visual checkpoint

5. Execute Q0 native + WASM against both exact pinned candidates.
6. Commit evidence and update gates.
7. If acceptable, proceed to Q1 geometry/replay/query fixture.

Do not restart generic CAD/library research and do not reinterpret V2 aesthetics as product/clinical semantics.
