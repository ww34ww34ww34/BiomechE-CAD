# BiomechE-CAD — Geometry Engine Evaluation Scorecard

**Status:** ACTIVE BASELINE v0.1 — scorecard defined, candidates not selected  
**Date:** 2026-08-15  
**Scope:** geometry-engine architecture evaluation after P0 authoring freeze  
**Canonical branch at evaluation start:** `main` @ `4d61ed5e655a4c2893194c9ead8e5857181036bc`  
**Primary candidates:**

```text
A. product-owned clinical/domain layer + Pixar OpenSubdiv
B. product-owned clinical/domain layer + openNURBS / ON_SubD
```

**Decision status:** **NO WINNER SELECTED.** This document defines how candidates are allowed to compete.

---

## 1. Checkpoint audit

The architecture evaluation starts only after the following product semantics have been frozen independently of any geometry library:

- `spec/01_coordinate_registration.md` — coordinate/laterality/registration semantics;
- `spec/16_geometry_authoring_contract.md` — Geometry Authoring Contract (`GAUTH-*`);
- `spec/17_workflow_preset_macro.md` — Workflow/Preset/Macro Contract (`WFLOW-*`);
- `spec/18_numerical_qualification_registry.md` — Numerical/Tolerance/Qualification Registry (`NREG-*`);
- `validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md` — `AUTH-C01..C22`;
- `validation/P0_AUTHORING_CROSS_DOCUMENT_AUDIT_2026-08-15.md` — 0 blocking semantic contradictions;
- `P0_AUTHORING_FREEZE_AUDIT_2026-08-15.md` — architecture-entry GO.

The Project Schema v0.2 change-set remains **APPROVED / NOT MATERIALIZED**. This scorecard does not authorize JSON Schema, fixture or migration changes.

`TD-CI-001` remains deliberately deferred. GitHub CI is not a gate for this architecture-analysis phase and a green workflow must not be presented as proof that `main` is fully qualified.

### 1.1 Architecture doctrine

The engine is a replaceable implementation component below product-owned semantics.

The following are therefore **not** negotiable candidate preferences:

```text
semantic prescription survives geometry
committed DesignRevision is immutable
capture context and landmark provenance are first-class
placement is typed anatomical/reference semantics
geometry dose != mechanical/material dose
no hidden universal clinical default
OPEN means OPEN
algorithm tolerance != manufacturing tolerance != device limit != clinical threshold
CAD nominal != ManufacturingArtifact != PhysicalOrthosis
mirror is semantic and side-aware
workflow/preset exact id/version/hash and historical expansion survive
BiomechE remains quantitative KPI authority
```

A library that is attractive only if one of these rules is weakened fails the architecture evaluation.

---

# 2. Evaluation method

The evaluation has three layers, in this order:

1. **HARD GATES** — pass/fail/unknown. A true fail removes a candidate. `UNKNOWN` requires a PoC and cannot be silently treated as pass.
2. **WEIGHTED CRITERIA** — used only after the relevant hard gates have passed or have an approved bounded implementation path.
3. **POC/BENCHMARK UNCERTAINTIES** — claims not established by current primary evidence are converted into executable experiments.

The scorecard deliberately separates **what the product must own** from **what the geometry library must natively provide**. A capability may be satisfied by a small product-owned adapter or accelerator if that boundary is explicit, deterministic, testable and does not reintroduce a second geometry authority.

## 2.1 Candidate score scale

Weighted criteria use a 0–5 score:

| Score | Meaning |
|---:|---|
| 0 | absent or architecture blocker |
| 1 | feasible only through major rearchitecture / large unproven adjunct |
| 2 | partial capability; high integration or qualification risk |
| 3 | adequate through a bounded product-owned adapter |
| 4 | strong direct capability with current primary evidence |
| 5 | exceptional direct capability plus mature qualification evidence |

A numerical score must carry an evidence grade:

| Grade | Evidence |
|---|---|
| A | current primary source **and** project PoC/benchmark |
| B | current primary source/API/source code, no project PoC yet |
| C | reasoned inference or indirect upstream evidence |
| U | unknown / not demonstrated |

**Selection rule:** no candidate may receive the final selection recommendation while any selection-critical hard gate remains `UNKNOWN`, and no `5` may be assigned without project-owned qualification evidence.

---

# 3. HARD GATES

| Gate | Requirement | Frozen source / acceptance | Pass condition | Failure condition |
|---|---|---|---|---|
| **HG-01 Product-owned semantics isolation** | Clinical/domain/workflow/numerical semantics remain outside the kernel. Kernel objects are never the authoritative persisted prescription. | GAUTH-001/004/005; WFLOW; schema doctrine; AUTH-C01/C15/C19..22 | semantic operations can reconstruct geometry through a narrow adapter; kernel serialization is optional/derived | product meaning must be encoded only in opaque library state or kernel-native history |
| **HG-02 Replayable derived geometry** | Exact revision + exact operation stack + exact algorithm bundle can reconstruct derived geometry. | GAUTH-004/036/037/038; NREG; AUTH-C01/C06/C15/C22 | deterministic reconstruction within explicitly named algorithm qualification tolerance | hidden mutable history/state makes exact historical reconstruction impossible |
| **HG-03 Stable authoring coordinates / IDs** | Local operations and sculpt records can bind to persistent semantic coordinates or stable component identity with explicit invalidation on topology change. | GAUTH-010/025/028/036; AUTH-C03/C06 | topology/control representation can support stable addressing or a deterministic product-owned correspondence layer | authoring requires anonymous baked mesh edits that destroy replay semantics |
| **HG-04 Limit/surface differential queries** | Evaluate surface position and sufficient first-order differential information for tangent/normal construction at reproducible surface coordinates. | GAUTH-010/030/031/036; AUTH-C01/C04/C11/C12 | point + tangent/derivative + normal path is reproducible and numerically controlled | only display tessellation is available and authoring/inspection cannot query the underlying surface reproducibly |
| **HG-05 Local deformation, sculpt and semantic mirror feasibility** | Bounded local parametric edits, freeform sculpt replay and side-aware mirror can be implemented without changing product semantics. | GAUTH-015..018/025/028; AUTH-C01/C03/C06/C08/C18 | edits can be expressed/replayed and mirror produces a new side-owned semantic result | required operations force destructive mesh-only history or side-agnostic coordinate mirroring |
| **HG-06 Spatial query / scan-conform path** | Nearest point, projection and scan conform can be implemented with adequate correctness and scalable acceleration. Native kernel API is not mandatory; a single bounded product-owned spatial-query component is acceptable. | GAUTH-026; registration spec; AUTH-C07 | PoC proves registered scan→surface projection/residual path at required sizes | no practical deterministic path exists without introducing a competing geometry authority |
| **HG-07 Reproducible inspection path** | Section, distance, height, angle, thickness and deviation definitions can be calculated from exact revision/provenance. | GAUTH-030..033; AUTH-C11..C14 | each inspection has an explicit method and reproduces within named numerical tolerance | results depend on view/display mesh or undocumented library defaults |
| **HG-08 Production realization / DFM path** | Exact clinical/contact surface can feed lower surface, closure, production body and minimum-thickness/DFM checks while keeping clinical intent separate. | GAUTH-034/035; manufacturing specs; AUTH-C14/C19/C21 | bounded production pipeline can produce/validate manufacturable geometry from exact revision + ManufacturingProfile | candidate requires conflating clinical surface with production body or cannot support an earned production adjunct |
| **HG-09 Explicit numerical control** | Algorithm tolerances are explicit, scoped and versioned; no hidden project-wide clinical/manufacturing tolerance is introduced by the engine. | NREG-001..030; GAUTH-036; AUTH-C08/C14/C16/C19..22 | tolerances/defaults can be surfaced, classified and captured in algorithm/profile provenance | correctness depends on uncontrollable hidden tolerance/default with semantic effect |
| **HG-10 One C++ core across native + server + web-WASM** | Product-owned geometry semantics/evaluation core is one C++20 codebase deployable desktop/server and compilable for web-WASM; renderer may differ. | architecture constraint | same core/adapter contracts compile and execute in native and WASM qualification fixtures | web requires a second independently evolving product geometry implementation |
| **HG-11 Interactive/incremental feasibility** | Authoring updates and invalidation are fast enough for interactive editing on the target profile. | GAUTH preview/commit model; user product requirement | qualification profile passes p50/p95/p99 edit/update budgets once those engineering budgets are explicitly approved | measured performance fails approved product budgets after bounded optimization |
| **HG-12 Large-scan feasibility** | Registered scan/point-cloud/mesh sizes can be handled without pathological memory/time behavior. | GAUTH-007/026; AUTH-C07 | benchmark profile passes memory/throughput budgets once approved | candidate architecture intrinsically forces unacceptable duplication/rebuild behavior |
| **HG-13 License / distribution acceptability** | Commercial desktop/server/web distribution and modification/use terms are approved for the product. | product legal gate | primary license text + dependency notices reviewed and accepted | legal review rejects terms or required redistribution model |
| **HG-14 API/dependency containment** | Upstream changes do not leak into semantic schema/history; exact upstream version and dependency graph can be pinned/reproduced. | GAUTH-038; WFLOW exact-version doctrine; provenance | narrow adapter + reproducible build + dependency manifest | upstream object model becomes persisted semantic contract or unpinnable dependency |
| **HG-15 Frozen acceptance coverage** | Architecture can satisfy all `AUTH-C01..C22` at their relevant layers without semantic exceptions. | P0 Authoring Acceptance Catalog | no scenario requires changing frozen meaning; geometry scenarios have L3/L4 test path | any frozen scenario can pass only by weakening/reinterpreting the product contract |

### 3.1 Important interpretation

`AUTH-C17`, `C19`, `C20` and `C21` are mainly product/governance tests, not geometry-algorithm differentiators. They still participate in **HG-01/HG-09/HG-15** because the selected stack must not make them impossible, but a library does not earn weighted points merely for not owning clinical authority.

Similarly, direct `.NET`, STL, 3MF or CNC APIs are not hard gates if the product-owned C++ adapter and manufacturing handoff can provide them safely. They are integration-cost criteria.

---

# 4. WEIGHTED CRITERIA — 100 points

Weights are applied only after hard-gate compatibility is established.

| ID | Criterion | Weight | What is actually scored |
|---|---|---:|---|
| W-01 | SubD / limit-surface quality and artifact control | 10 | surface quality, crease/boundary handling, stable limit evaluation, artifact resistance |
| W-02 | Local parametric deformation ergonomics | 8 | bounded local deformation implementation cost, stable addressing, falloff/transition support |
| W-03 | Sculpt/freeform editing | 7 | sparse/event replay feasibility, incremental updates, topology-change handling |
| W-04 | Surface differential/query primitives | 7 | point/tangent/normal/derivative access and precision/control |
| W-05 | Nearest-point / projection / spatial acceleration | 8 | direct primitives or clean product-owned BVH path; correctness and integration cost |
| W-06 | Inspection and deviation primitives | 6 | section/intersection, measurements, thickness, deviation-map building blocks |
| W-07 | Production body / minimum-thickness / DFM integration | 12 | lower surface, offsets/closure/solid validation path; need/cost of earned adjunct |
| W-08 | Interactive performance / incremental invalidation | 11 | edit p50/p95/p99, rebuild granularity, cache invalidation, allocation behavior |
| W-09 | Large scan memory/throughput | 7 | scan projection throughput, memory scaling, zero/low-copy options |
| W-10 | Web-WASM + rendering interoperability maturity | 8 | build feasibility, binary size/startup, mesh/point transfer, browser rendering path |
| W-11 | Native C++20 / desktop / server integration | 4 | build simplicity, compiler/platform coverage, headless execution |
| W-12 | API lifecycle / upstream stability | 3 | release/version discipline, public/private API boundary, migration risk |
| W-13 | Dependency/build footprint | 3 | transitive dependencies, optionality, supply-chain/build complexity |
| W-14 | Serialization/interchange isolation | 2 | ease of product-owned replay serialization and optional neutral/native interchange |
| W-15 | .NET/C# interoperability | 2 | maintained binding path without making .NET the geometry authority |
| W-16 | Manufacturing handoff: STL / 3MF / CNC path | 2 | reliable neutral export/handoff; direct CNC kernel API is not required |

**Total: 100**

License is intentionally excluded from weighting because unacceptable licensing is a hard failure, not a trade-off to be compensated by geometry features.

---

# 5. Frozen-contract → required stack capability mapping

| Frozen rule(s) | Product meaning | Geometry-stack capability demanded | Main qualification scenarios |
|---|---|---|---|
| GAUTH-001/004/005/036/037/038 | semantic operation authoritative; preview/commit separation; deterministic version-bound replay | narrow kernel adapter; deterministic rebuild; explicit operation order; version pinning | C01, C06, C15, C22 |
| GAUTH-007/008/010 + coordinate spec | capture/landmark provenance and typed placement survive | registered transforms + stable surface query coordinates; **provenance itself stays product-owned** | C04, C05, C07, C09, C10 |
| GAUTH-015/016/017/018 | units, extent, transition and requested-vs-realized are explicit | parameterized local deformation; explicit constraint/result reporting | C01, C08 |
| GAUTH-025 | sculpt is replayable semantic history, not anonymous final mesh | stable control/surface addressing; sparse displacement or event replay; local invalidation | C06 |
| GAUTH-026 | scan conform records source, registration, ROI, projection method, strength, residual, algorithm version | nearest-point/projection accelerator; residual calculation; scalable scan access | C07 |
| GAUTH-028 + side/coordinate freeze | mirror is semantic and side-aware | deterministic geometric transform/correspondence while product layer remaps side-owned semantics | C03, C18 |
| GAUTH-030/031 | reproducible section/distance/height/angle | surface intersection/sampling and exact measurement definitions | C11, C12 |
| GAUTH-032 | thickness has explicit method | opposing-surface/ray/normal/nearest-point method selectable and provenance-bound | C13 |
| GAUTH-033 | deviation map is provenance-bearing measurement | closest/projection mapping + signed/unsigned distance field over explicit source/target | C14 |
| GAUTH-034/035 | clinical/contact surface != production realization | exact surface export into lower-surface/closure/solid/DFM pipeline | C14, C19, C21 |
| WFLOW-001..030 | exact reusable definition, expansion, override, inspection and mirror policies | geometry kernel must be callable as deterministic stateless-ish service; no workflow state inside kernel | C15..C18 |
| NREG-001..030 | numeric authority classes, OPEN lifecycle, no silent fallback | explicit algorithm tolerance/profile injection and observed metric reporting | C08, C14, C16, C19..C22 |

---

# 6. `AUTH-C01..C22` → architecture test mapping

| Scenario | Architecture implication / test |
|---|---|
| C01 Arch dose + placement + replay | replay same typed operation and compare control/limit outputs under explicit geometry-equivalence rule |
| C02 Heel semantic distinction | verify distinct heel operation semantics can share low-level primitives without collapsing into one opaque kernel edit |
| C03 Side-aware wedge mirror | mirror geometry and semantic side mapping; verify intrinsic medial/lateral meaning survives |
| C04 Met-pad non-equivalent references | evaluate two placement-reference modes that resolve to different locations; kernel must not normalize away reference semantics |
| C05 Pressure-target offload provenance | pressure/ROI provenance remains outside kernel; kernel consumes resolved registered target geometry only |
| C06 Sculpt replay | replay event/sparse-displacement record; compare output and stable addressing after reload |
| C07 Scan conform | benchmark registered scan projection/conform + residuals + deterministic repeat |
| C08 Requested vs realized | constraint path returns both requested and realized values; no silent clamping |
| C09 Weight-bearing UNKNOWN | kernel receives geometry without inventing missing capture semantics |
| C10 Landmark provenance | geometry consumes resolved landmark/reference but cannot erase/replace provenance record |
| C11 Section | identical section definition over identical revision reproduces curve/measurements |
| C12 Distance/height/angle | named measurement method reproduces values and units |
| C13 Thickness method | compare at least two explicit thickness methods where they differ; preserve method identity |
| C14 CAD-vs-part deviation | build deviation mapping but refuse qualified PASS if ManufacturingProfile rule is absent/OPEN |
| C15 Workflow version + expanded children | exact workflow expansion generates same operation sequence; kernel has no hidden workflow version state |
| C16 Override + registry rule | altered governed parameter is explicit in override/numerical rule provenance |
| C17 Suggestion != confirmation | architecture cannot auto-promote generated geometry suggestion to committed clinical confirmation |
| C18 Unsafe child blocks mirror | product policy can reject mirror before/during geometry application; kernel mirror primitive is not authority |
| C19 OPEN manufacturing tolerance | production/inspection path returns measurement; qualification remains OPEN rather than inventing PASS limit |
| C20 UI default != qualification | visual/editor default never becomes hidden kernel tolerance/clinical rule |
| C21 Evidence rule profile-scoped | measurement engine accepts explicit profile/rule selection and does not own universal threshold |
| C22 Replay epsilon != part tolerance | separate geometry-replay equivalence from manufacturing acceptance comparison |

---

# 7. Current primary-source evidence snapshot

The purpose of this section is **capability evidence**, not selection.

## 7.1 Pixar OpenSubdiv

Pinned evaluation baseline: **v3.7.0** (`9dab8a47...` upstream tag observed 2026-08-15).

Primary evidence:

- upstream describes OpenSubdiv as high-performance subdivision evaluation on parallel CPU/GPU and specifically optimized for deforming subdivision surfaces with **static topology** at interactive frame rates;
- the core C++ libraries state no dependency beyond the C++ standard library; optional `Osd` paths use APIs such as OpenGL, Metal, CUDA, TBB, OpenCL and DirectX;
- `Far::PatchTable::EvaluateBasis()` exposes basis evaluation with optional first derivatives (`Du`, `Dv`) and second derivatives (`Duu`, `Duv`, `Dvv`), which is strong evidence for a point/tangent/normal differential-evaluation pipeline;
- OpenSubdiv's public architecture is focused on subdivision representation/evaluation, not on full CAD production-body or scan-processing functionality.

Primary URLs:

```text
https://github.com/PixarAnimationStudios/OpenSubdiv
https://github.com/PixarAnimationStudios/OpenSubdiv/blob/v3_7_0/README.md
https://github.com/PixarAnimationStudios/OpenSubdiv/blob/v3_7_0/opensubdiv/far/patchTable.h
https://github.com/PixarAnimationStudios/OpenSubdiv/blob/v3_7_0/LICENSE.txt
```

License baseline: upstream `LICENSE.txt` is the **Tomorrow Open Source Technology License 1.0**. Treat commercial/product acceptability as **HG-13 legal-review OPEN**, not as an engineering assumption.

### Evidence-led preliminary characterization

**Strong/current evidence:**

```text
SubD limit evaluation
first/second derivative basis evaluation
static-topology deforming-surface performance focus
lean core dependency graph
CPU/GPU evaluation options
```

**Not demonstrated by current primary evidence and therefore PoC/adapter territory:**

```text
browser/WASM build and product bundle characteristics
nearest-point / closest-point query
large scan BVH / projection
section/thickness/deviation toolchain
production lower surface / closure / watertight solid
minimum-thickness/DFM
.NET binding
STL/3MF/CNC handoff
```

Absence from this evidence set is **not** a claim that a task is impossible; it means the scorecard will not credit it until demonstrated.

## 7.2 openNURBS / `ON_SubD`

Pinned evaluation baseline: **openNURBS v8.32.26160.13001** (`00bdd2ce...` upstream tag observed 2026-08-15).

Primary evidence:

- openNURBS is a broader C++ geometry/file toolkit centered on the 3DM model and includes NURBS evaluation and elementary geometry utilities;
- public `ON_SubD` headers expose surface/limit-point concepts, tangent/normal data and component evaluation caches/invalidation operations;
- public SubD mesh-fragment structures expose tessellated surface points/normals useful for rendering/inspection adapters;
- the Windows static-library path in `opennurbs_public.h` brings bundled/linked dependencies including zlib and FreeType plus system libraries, so its baseline footprint is broader than OpenSubdiv core;
- current inspection of the public `opennurbs_subd.h` did **not** establish a direct `ON_SubD::ClosestPoint`-style primitive. Nearest-point/projection therefore remains a PoC/adapter question rather than a credited native capability.

Primary URLs:

```text
https://github.com/mcneel/opennurbs
https://github.com/mcneel/opennurbs/blob/v8.32.26160.13001/README.md
https://github.com/mcneel/opennurbs/blob/v8.32.26160.13001/opennurbs_subd.h
https://github.com/mcneel/opennurbs/blob/v8.32.26160.13001/opennurbs_public.h
https://github.com/mcneel/opennurbs/blob/v8.32.26160.13001/LICENSE
```

License baseline: use the current upstream openNURBS license text and bundled notices as **HG-13 legal-review OPEN**. Do not infer product approval from the project name or historical summaries.

## 7.3 `rhino3dm` as interoperability evidence, not automatic dependency

Pinned evidence snapshot: **rhino3dm 8.32.1** (2026-07-29).

McNeel's current `rhino3dm` project demonstrates that openNURBS-derived C++ can be delivered through:

```text
.NET
Python
JavaScript + WebAssembly
Windows / macOS / Linux
```

The official JavaScript documentation states that `rhino3dm.js` is openNURBS plus C++→JavaScript bindings compiled to WebAssembly and runs in major browsers/Node.js. Version `8.32.0` added a JS/Python **SubD read API** exposing control-net points, surface points, tags and connectivity; `8.32.1` followed on 2026-07-29.

This is **positive portability/interoperability evidence for the openNURBS family**, but it does **not** prove that every native `ON_SubD` authoring capability is exposed in WebAssembly or that `rhino3dm` should be adopted as a product runtime dependency. Full authoring parity is a PoC item.

Primary URLs:

```text
https://github.com/mcneel/rhino3dm
https://github.com/mcneel/rhino3dm/blob/8.x/docs/javascript/RHINO3DM.JS.md
https://github.com/mcneel/rhino3dm/blob/8.x/CHANGELOG.md
```

---

# 8. Preliminary comparison — evidence only, no winner

Legend: `+` current positive primary evidence; `?` needs project PoC/benchmark; `A` likely bounded adapter/adjunct; `—` not credited by current evidence.

| Capability | OpenSubdiv | openNURBS / ON_SubD | Current interpretation |
|---|---|---|---|
| Product-owned clinical isolation | + | + | both can sit below a product-owned semantic layer; must be enforced by our adapter |
| Stable SubD control/limit representation | + | + | both plausible; persistent authoring addressing still needs PoC |
| Limit/surface point + derivatives/normals | + | + | OpenSubdiv derivative basis is explicit; ON_SubD surface-point/tangent/normal APIs exist |
| Static-topology interactive deformation focus | + | ? | explicit OpenSubdiv design target; ON_SubD needs our benchmark |
| Local parametric orthosis deformation | A/? | A/? | product-owned operator layer required for both |
| Sculpt replay | A/? | A/? | neither earns credit until stable-addressing/invalidation PoC |
| Semantic mirror | A | A | semantics remain product-owned; geometry transform/correspondence must be proven |
| Nearest point / projection | ?/A | ?/A | no candidate is currently credited with a verified direct SubD closest-point path |
| Large scan acceleration | ?/A | ?/A | gap-driven BVH component may be justified after PoC |
| Section/thickness/deviation | ?/A | ?/A | broader openNURBS geometry may reduce adapter cost, but must be verified against public APIs |
| Production body / closure / minimum thickness | ?/A | ?/A | critical unresolved area for both; likely trigger for narrowly earned auxiliary library evaluation |
| Lean core dependencies | + | lower | OpenSubdiv core explicitly stdlib-only; openNURBS static path is broader |
| Web/WASM precedent | ? | + | rhino3dm is concrete family-level evidence; OpenSubdiv still requires direct Emscripten PoC |
| .NET precedent | ?/A | + | Rhino3dm.NET is maintained evidence; still optional to product architecture |
| Neutral/manufacturing handoff | A/? | +/A | openNURBS has 3DM ecosystem breadth; product still needs STL/3MF/CNC-specific handoff qualification |
| Determinism / cross-platform equivalence | ? | ? | must be measured for exact product workloads and qualification tolerance |

### 8.1 Evidence lead, not selection lead

At this checkpoint:

- **OpenSubdiv has the clearer evidence lead for a small, focused, high-performance SubD evaluator with explicit derivative evaluation and lean core dependencies.**
- **openNURBS/ON_SubD has the clearer evidence lead for geometry-toolkit breadth and an already demonstrated .NET/WebAssembly interoperability family through rhino3dm.**
- **Neither candidate currently has enough evidence on spatial queries, orthosis production realization, minimum-thickness/DFM and full frozen acceptance coverage to be selected.**

This is exactly why weighted scoring is intentionally not finalized yet.

---

# 9. Uncertainties that MUST become PoCs / benchmarks

| ID | Uncertainty | Why documentation alone is insufficient | Candidate(s) |
|---|---|---|---|
| POC-01 | native C++20 reproducible build footprint | actual compiler flags, binary/dependency graph and integration friction are product-specific | both |
| POC-02 | WASM same-core feasibility | browser compile, exceptions/RTTI/threading/SIMD, binary size, startup and API exposure must be measured | both; especially OpenSubdiv |
| POC-03 | stable authoring addressing | sculpt/local ops need IDs/param coords robust to supported edits | both |
| POC-04 | limit point/tangent/normal equivalence | verify exact APIs and numerical behavior on canonical orthosis patches | both |
| POC-05 | local deformation update cost | orthosis operators are product-specific and invalidate local regions differently | both |
| POC-06 | sculpt event/sparse-displacement replay | persistence + incremental edit behavior cannot be inferred from generic SubD APIs | both |
| POC-07 | side-aware mirror correspondence | must preserve left/right intrinsic semantics and stable operation anchors | both |
| POC-08 | closest point / scan projection | direct ON_SubD primitive not established; OpenSubdiv is evaluator-focused | both |
| POC-09 | large scan throughput/memory | product scan sizes and browser/native memory characteristics matter | both |
| POC-10 | reproducible section/intersection | exact section curves and measurement tolerance must be observed | both |
| POC-11 | thickness method(s) | normal/ray/nearest methods can diverge; method identity is frozen semantic state | both |
| POC-12 | deviation map | spatial acceleration, sign convention, sampling and residual behavior need fixtures | both |
| POC-13 | lower surface / offset / closure / watertight body | likely decisive capability gap; may justify a narrowly scoped adjunct | both |
| POC-14 | minimum-thickness / DFM | must detect violations against explicit ManufacturingProfile rule without hidden limit | both |
| POC-15 | deterministic replay | repeat/process/platform/WASM equivalence must be measured under explicit algorithm tolerance | both |
| POC-16 | incremental invalidation | compare control-point edits, cache invalidation, partial vs full rebuild | both |
| POC-17 | render interop | extract render mesh/attributes without avoidable copies on native and web | both |
| POC-18 | .NET boundary cost | confirm whether thin C ABI/PInvoke is enough vs family binding value | both |
| POC-19 | STL/3MF handoff | verify neutral tessellation, units, normals/watertightness and metadata strategy | both |
| POC-20 | AUTH-C01..C22 architecture harness | final selection needs candidate-backed evidence, not feature-name matching | both |

---

# 10. Rules for admitting auxiliary libraries

OCCT, Manifold, CGAL, libigl, geometry-central or another library is **not** added because it is generally capable.

An adjunct enters evaluation only when all are true:

1. a frozen hard gate/PoC demonstrates a concrete missing capability;
2. the missing capability cannot be implemented reasonably inside the product-owned layer;
3. the adjunct has one sharply bounded responsibility;
4. it does not become a second semantic geometry authority;
5. serialization/replay remains product-owned;
6. license, WASM/native portability, dependency and performance impacts are scored;
7. removal/replacement remains possible behind an adapter.

The first likely trigger is **HG-08 / POC-13..14** (production body, closure, robust offset/minimum-thickness/DFM), but this is a hypothesis to test, not permission to add OCCT/CGAL/Manifold now.

---

# 11. Performance and numerical qualification rule

No hidden engineering budget is invented by this scorecard.

For the first benchmark pass, record at least:

```text
wall time p50 / p95 / p99 / max
CPU time where practical
peak working memory / WASM heap
allocation/reallocation counts where practical
control vertices / faces / rendered triangles
scan point/triangle count
number of modified control elements
cache rebuild / invalidation scope
native compiler/version/flags
WASM toolchain/version/flags
candidate tag/commit
```

Final PASS/FAIL for performance requires an explicitly approved engineering qualification profile (for example a future `ARCH-PERF-*` profile). Until those budgets are approved, performance results are `MEASURED / NOT YET QUALIFIED`, not silently PASS.

Likewise, replay/equivalence epsilon must be a named **algorithm numerical tolerance**, never borrowed from a manufacturing acceptance limit.

---

# 12. Selection decision rule

A candidate may be recommended only when:

```text
all selection-critical hard gates = PASS
HG-13 license = reviewed/accepted
WASM/native single-core path = demonstrated
spatial-query/scan-conform path = demonstrated
production realization path = demonstrated or bounded adjunct formally earned
numerical/replay qualification = demonstrated
AUTH-C01..C22 architecture coverage = no semantic exception
weighted score = evidence-backed, with uncertainty/confidence recorded
```

A smaller weighted-score advantage is not enough to override a hard-gate failure.

---

# 13. DONE / TODO

## DONE

- [x] Checkpoint audited against P0 frozen documents.
- [x] Hard gates defined before library scoring.
- [x] Weighted criteria defined independently of candidate marketing.
- [x] `GAUTH/WFLOW/NREG` mapped to geometry-stack capability.
- [x] `AUTH-C01..C22` mapped to architecture tests.
- [x] Current primary-source evidence captured for OpenSubdiv, openNURBS/ON_SubD and rhino3dm interoperability precedent.
- [x] Candidate unknowns converted into explicit PoCs rather than assumptions.
- [x] No geometry engine selected.

## TODO

- [ ] Execute POC-01..20 in the qualification plan.
- [ ] Approve explicit engineering performance profile before declaring performance PASS/FAIL.
- [ ] Perform product legal review for candidate licenses/dependency notices.
- [ ] Determine whether HG-08 requires an auxiliary production-solid/DFM component.
- [ ] Fill evidence-graded weighted scores only after PoCs.
- [ ] Produce final architecture shoot-out and selection decision only after hard gates close.
- [ ] Keep `TD-CI-001` deferred; do not spend this phase repairing CI.

---

# 14. Handover

**Exact restart point:** execute the companion `docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`, beginning with build/reproducibility and canonical geometry fixtures for **both** candidates. Do not optimize one candidate before the other has the same fixture and measurement harness. Do not select a winner from this v0.1 evidence snapshot.