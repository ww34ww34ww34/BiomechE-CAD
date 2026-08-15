# BiomechE-CAD — Geometry Engine PoC / Qualification Plan

**Status:** ACTIVE PLAN v0.1 — not yet executed  
**Date:** 2026-08-15  
**Companion scorecard:** `docs/research/architecture/GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md`  
**Candidates:** product-owned layer + OpenSubdiv; product-owned layer + openNURBS/ON_SubD  
**Selection status:** undecided

---

## 1. Purpose

This plan converts the scorecard's `UNKNOWN` items into reproducible evidence.

It is intentionally **not** a general library demo. Each PoC must close a frozen-product question from `GAUTH`, `WFLOW`, `NREG` or `AUTH-C01..C22`.

Rules:

```text
same product-owned semantic fixture for both candidates
same requested operation parameters
same measurement harness
same native/WASM qualification metadata
no candidate-specific semantic shortcut
no hidden tolerance
no manufacturing limit reused as replay epsilon
no CI repair as part of this phase
```

`TD-CI-001` remains deferred. PoC evidence must be captured directly in result artifacts/reports; CI status is not the gate.

---

# 2. Qualification layers

The engine work maps to the frozen acceptance layering as follows:

```text
L0  persisted semantic/project state          product-owned; unchanged by candidate
L1  schema/contract                           product-owned; schema v0.2 still not materialized
L2  semantic operation evaluation             product-owned adapter/operator layer
L3  geometry realization and query            principal engine PoC layer
L4  numerical/performance qualification       engine + product-owned harness
L5  manufacturing/device acceptance           only when qualified profile/evidence exists
```

A library can score well at L3/L4 while still failing HG-01 if it forces L0/L1 semantics into kernel-native opaque state.

---

# 3. Reproducibility manifest — mandatory for every run

Every benchmark/result record must capture:

```text
candidateId
candidateVersion/tag
candidateCommit
candidateLicenseFileHash
buildTimestamp
hostPlatform
hostArchitecture
compilerId
compilerVersion
C++ standard
buildType
compilerFlags
linkMode
dependency manifest + versions
product adapter commit
fixtureId + fixtureHash
operation stack hash
algorithm bundle id/version/hash
numeric profile id/version/hash or OPEN status
thread count
CPU/GPU path if used
WASM toolchain/version/flags if applicable
result artifact hashes
```

No result without this manifest may be used for final weighted scoring.

---

# 4. Common canonical fixtures

Create candidate-neutral fixtures before implementation-specific optimization.

## FIX-GEOM-01 — Baseline orthosis control surface

Must contain:

- asymmetric left-foot template so mirror errors are observable;
- heel, midfoot arch and forefoot regions;
- sufficient curvature to exercise extraordinary vertices/crease/boundary handling;
- stable product-owned semantic region IDs independent of kernel IDs;
- explicit `mm` unit metadata and CAD-ANAT-1 frame.

## FIX-GEOM-02 — Local-dose fixture set

Operation cases:

```text
zero dose
small positive dose
large positive dose
bounded extent
short vs long transition
multiple partially overlapping edits
order-sensitive composition
```

Used by `AUTH-C01`, `C02`, `C03`, `C08`.

## FIX-GEOM-03 — Sculpt fixture

- at least 3 localized strokes/events;
- one stroke crosses a high-curvature region;
- replay from clean baseline;
- sparse/event representation stored in product-owned format;
- topology-change invalidation test.

Used by `AUTH-C06`.

## FIX-SCAN-01..03 — Registered scan tiers

Synthetic/reference scans with known geometry and exact registration transform:

```text
TIER-S   ~100k points/triangles
TIER-M   ~1M points/triangles
TIER-L   ~5M points/triangles or the largest size supported by the target product profile
```

Include known offsets/noise/outliers so nearest/projection residual correctness can be measured.

## FIX-PROD-01 — Production-body stress cases

At minimum:

```text
nominal smooth orthosis
thin local region
high curvature / offset difficulty
near-self-intersection case
open boundary requiring closure
asymmetric lower-surface condition
```

No hidden minimum thickness value is embedded in the fixture. The threshold is supplied by an explicit test ManufacturingProfile or remains OPEN depending on the case.

---

# 5. PoC execution sequence

## POC-01 — Native C++20 build and dependency audit

**Question:** Can the candidate be integrated behind the same C++20 adapter boundary with reproducible dependencies?

Run:

1. pin exact upstream tag/commit;
2. build Release on the primary desktop toolchain;
3. build headless/server target;
4. record build graph, static/dynamic libs and transitive dependencies;
5. record clean binary size and build time as descriptive metrics;
6. expose only a tiny product-owned C ABI/C++ facade to the harness.

**Gate links:** HG-01, HG-10, HG-13, HG-14.  
**Pass:** reproducible build + narrow adapter feasible; no semantic types leak upstream/downstream.  
**Fail:** candidate cannot be contained without making its object model part of the product semantic contract.

---

## POC-02 — WebAssembly same-core build

**Question:** Can the same product-owned C++ geometry adapter execute in browser/WASM without a second geometry implementation?

Measure:

```text
compile success
WASM binary size
compressed transfer size if packaging is tested
module initialization time
baseline heap
peak heap
single-thread and, if relevant, threaded/SIMD configuration
API surface required to render/query
native-vs-WASM numerical comparison
```

OpenSubdiv must be tested directly; do not infer WASM support from generic C++ portability. For the openNURBS family, rhino3dm is positive precedent but does not replace this product-authoring PoC.

**Gate links:** HG-10, HG-14; W-10.

---

## POC-03 — Canonical surface creation / serialization isolation

**Question:** Can a product-owned control representation and operation stack reconstruct candidate geometry without persisting opaque candidate state as authority?

Procedure:

1. construct `FIX-GEOM-01` from product-owned data;
2. hash semantic fixture;
3. build candidate control surface;
4. discard candidate instance;
5. reconstruct from product-owned fixture + exact versions;
6. compare sampled limit surface and control metadata under explicit algorithm-equivalence rule.

**Gate links:** HG-01, HG-02, HG-03, HG-14; AUTH-C01/C06/C15/C22.

---

## POC-04 — Limit point / derivatives / normals

For a deterministic grid plus extraordinary/boundary samples, record:

```text
position
Du/Dv or equivalent tangents
normal
second derivatives if exposed/used
candidate status/error
```

Cross-check finite-difference behavior for diagnostic purposes; finite differences are not automatically the canonical method.

**Gate links:** HG-04, HG-09; W-01/W-04.

---

## POC-05 — Local parametric authoring operators

Implement the same product-owned operator cases over `FIX-GEOM-02`:

```text
arch dose
heel modification
rear/forefoot wedge/posting
localized corrective/offload support geometry
transition/falloff variations
requested value exceeding a synthetic explicit constraint
```

Record:

```text
requested parameters
realized parameters
modified control elements / affected region
surface sample changes
invalidation scope
wall time p50/p95/p99
allocations/reallocations where measurable
```

**Gate links:** HG-03/HG-05/HG-09/HG-11; AUTH-C01/C02/C03/C05/C08.

---

## POC-06 — Sculpt replay and invalidation

Replay `FIX-GEOM-03` from clean state repeatedly.

Required tests:

- exact event/sparse record is product-owned;
- repeat produces equivalent geometry under replay rule;
- local edit invalidation is measured;
- unsupported topology change produces explicit invalid/unresolved state rather than silent remap;
- reload/replay does not depend on interactive editor memory.

**Gate links:** HG-02/HG-03/HG-05/HG-11; AUTH-C06.

---

## POC-07 — Semantic mirror / bilateral geometry

The product layer performs side-semantic mapping; candidate performs only the geometric work it is assigned.

Test:

```text
RIGHT operation -> LEFT mirrored operation
medial/lateral intrinsic meaning preserved
asymmetric fixture visibly swaps correctly
stable anchors/references remapped explicitly
mirror blocked when workflow child policy marks unsafe case
```

**Gate links:** HG-03/HG-05/HG-15; AUTH-C03/C18.

---

## POC-08 — Nearest point / projection / scan conform

For each `FIX-SCAN-*` tier:

1. build the candidate or product-owned spatial index;
2. project known scan points to the design surface;
3. record nearest point, normal, signed/unsigned residual as defined by the test method;
4. compare against synthetic ground truth;
5. run conform with explicit ROI, strength and algorithm version;
6. record residual before/after;
7. repeat for deterministic-equivalence analysis.

Metrics:

```text
index build time
projection throughput
p50/p95/p99 query latency where meaningful
peak memory
native vs WASM
error/residual distribution
outlier handling
```

**Gate links:** HG-06/HG-09/HG-12; AUTH-C07.

If neither candidate supplies an adequate primitive, this PoC may earn evaluation of one narrowly bounded BVH/spatial-query adjunct. That adjunct must then pass license/WASM/dependency/replay evaluation too.

---

## POC-09 — Reproducible inspection

### Section

- same revision + same section definition -> same section curve/sample set;
- include high-curvature and near-tangent planes.

### Distance / height / angle

- explicit reference entities and frames;
- verify units and sign conventions.

### Thickness

Exercise at least two explicitly named methods where meaningful, e.g.:

```text
normal-direction intersection
specified ray direction
nearest opposing-surface distance
```

The project must preserve method identity because different methods need not agree.

### Deviation map

- exact source/target revision/artifact IDs;
- sampling method and projection method explicit;
- report raw distribution before any acceptance threshold.

**Gate links:** HG-07/HG-09; AUTH-C11..C14.

---

## POC-10 — Production surface/body and DFM

This is a selection-critical experiment.

From an exact clinical/contact surface:

1. derive candidate lower surface using an explicit engineering fixture/profile;
2. construct side wall / closure as required;
3. generate production body;
4. detect self-intersection/non-manifold/open-boundary failures;
5. evaluate minimum thickness with explicit method;
6. preserve requested-vs-realized information when a synthetic explicit constraint changes geometry;
7. keep clinical/contact surface immutable.

Run all `FIX-PROD-01` cases.

**Gate links:** HG-08/HG-09; W-07; AUTH-C08/C13/C14/C19/C21/C22.

### Adjunct trigger

Only if this PoC establishes a real gap may a focused comparison of OCCT, Manifold, CGAL or another production-geometry component begin. Record the exact missing primitive first, e.g.:

```text
robust offset surface
watertight closure/boolean
self-intersection repair
solid classification
minimum wall/thickness acceleration
```

Do not add a general CAD kernel merely because POC-10 is difficult.

---

## POC-11 — Determinism / numerical control

Execute canonical operation stacks repeatedly:

```text
100 repeated runs same process where practical
fresh-process repeats
multiple thread settings if candidate supports them
native compiler/toolchain variants selected by project
native vs WASM
```

Report difference distributions at control and sampled limit surfaces.

The result is not PASS until an explicit `ALGORITHM_NUMERICAL_TOLERANCE` engineering profile is approved. Before that, status is:

```text
MEASURED / NOT YET QUALIFIED
```

Never use ManufacturingProfile tolerance as the replay epsilon.

**Gate links:** HG-02/HG-09; AUTH-C22.

---

## POC-12 — Incremental invalidation benchmark

Scenarios:

```text
single control element edit
small local region edit
multi-region edit
full-surface parameter change
topology-affecting change if supported
sculpt stroke sequence
```

Record separately:

```text
semantic operation evaluation
control-data update
candidate validation
cache invalidation/rebuild
limit evaluation
tessellation/render-mesh extraction
```

This decomposition is mandatory so a rendering bottleneck is not misattributed to the geometry kernel or vice versa.

**Gate links:** HG-11; W-08.

---

## POC-13 — Rendering interoperability

Native and web paths must consume derived render geometry without making the renderer the geometry authority.

Measure:

```text
limit-to-render mesh extraction time
vertex/index counts
copy count / bytes copied
update granularity
native GPU upload path
WASM -> JS/WebGL/WebGPU/Three.js-compatible buffer path as selected by implementation
```

The rendering path may differ by platform; the authoritative product-owned semantic/core geometry path must not.

**Gate links:** HG-10/HG-11; W-10.

---

## POC-14 — .NET boundary

Compare two bounded approaches where relevant:

```text
thin product C ABI + P/Invoke
candidate-family maintained .NET binding where available
```

Measure call/buffer overhead for realistic edit/query batches, not single trivial calls only.

Decision question: does a maintained binding materially reduce implementation risk without leaking candidate types into the product semantic model?

**Weight link:** W-15. Not independently a hard gate.

---

## POC-15 — Manufacturing neutral handoff

At minimum qualify:

```text
STL tessellation and explicit units policy
3MF export path or adapter strategy
watertight/manifold checks before handoff
normal/orientation consistency
ManufacturingArtifact hash/provenance separation
CNC/toolpath handoff boundary without making toolpath the CAD nominal state
```

A candidate is not required to be the CNC/CAM engine.

**Gate links:** HG-08/HG-14; W-16.

---

## POC-16 — Frozen acceptance architecture harness

Create an engine-backed harness mapping all `AUTH-C01..C22` to their relevant layers.

Expected distribution:

```text
C01..C14  L2/L3/L4 geometry, acquisition and inspection emphasis
C15..C18  L2 product workflow semantics + L3 geometry where invoked
C19..C22  L2/L4 governance and numerical falsification emphasis
```

The engine must not be forced to implement product governance that belongs above it; instead verify that the adapter boundary preserves the product test.

**Gate link:** HG-15.

---

# 6. Performance benchmark protocol

## 6.1 No hidden pass budget

The current frozen numerical registry does not define a universal engine performance threshold. Therefore the first benchmark pass produces **measurements**, not qualification claims.

A future explicit engineering-only profile should define, per target hardware/browser class:

```text
preview edit p95/p99 budget
full commit/rebuild budget
scan projection throughput budget
maximum supported scan tier
memory budget native
memory budget WASM
browser initialization/bundle budget if product-owned
render update budget
```

Until approved, report `OPEN` or `MEASURED / NOT YET QUALIFIED` as appropriate.

## 6.2 Statistics

For each timed case:

- warm-up documented;
- minimum 30 measured iterations for stable short operations where practical;
- report `min`, `p50`, `p95`, `p99`, `max`, `mean`;
- report sample count;
- retain raw result file for later audit;
- do not delete outliers without documented cause;
- separate cold-start from steady-state.

## 6.3 Memory

Report:

```text
baseline process/heap
post-fixture load
post-spatial-index
peak during operation
steady post-operation
WASM heap growth events
```

---

# 7. Evidence result template

Each PoC should produce a Markdown summary plus machine-readable result artifact later. Minimum Markdown fields:

```text
POC ID
candidate
version/tag/commit
fixture ID/hash
host/toolchain
status: PASS / FAIL / UNKNOWN / MEASURED-NOT-QUALIFIED
hard gates addressed
auth scenarios addressed
method
raw artifact refs/hashes
correctness observations
performance observations
memory observations
determinism observations
known confounders
new dependency introduced? yes/no
semantic contract change required? MUST be no unless explicit superseding decision exists
conclusion
next action
```

---

# 8. Initial candidate-specific hypotheses to falsify

These are deliberately phrased as hypotheses, not conclusions.

## OpenSubdiv hypotheses

- H-OSD-01: focused evaluator architecture yields lower integration/dependency cost.
- H-OSD-02: derivative/limit evaluation is sufficient to implement product inspection primitives above the kernel.
- H-OSD-03: static-topology deformation path provides superior incremental authoring performance.
- H-OSD-04: WASM compilation is practical despite no current project-specific upstream precedent captured here.
- H-OSD-05: missing spatial/production operations can be added as bounded product components without turning the stack into a fragmented multi-kernel architecture.

## ON_SubD hypotheses

- H-ON-01: broader geometry toolkit reduces inspection/interchange implementation cost.
- H-ON-02: public surface-point/tangent/normal and cache APIs are sufficient for stable authoring/query integration.
- H-ON-03: rhino3dm demonstrates a realistic family-level web/.NET path but full SubD authoring parity can still be delivered through our chosen adapter.
- H-ON-04: broader dependency/API footprint remains acceptable when isolated behind the product adapter.
- H-ON-05: ON_SubD incremental performance on orthosis workloads is competitive enough despite OpenSubdiv's explicit high-performance evaluator focus.

The PoCs should attempt to **falsify** these hypotheses rather than confirm preferences.

---

# 9. Execution order / stop conditions

Recommended order:

```text
PHASE Q0  POC-01 build/dependencies + POC-02 WASM
PHASE Q1  POC-03 canonical representation + POC-04 derivatives
PHASE Q2  POC-05 local authoring + POC-06 sculpt + POC-07 mirror
PHASE Q3  POC-08 scan/spatial + POC-09 inspection
PHASE Q4  POC-10 production/DFM
PHASE Q5  POC-11 determinism + POC-12 invalidation/performance
PHASE Q6  POC-13 rendering + POC-14 .NET + POC-15 manufacturing handoff
PHASE Q7  POC-16 AUTH-C01..C22 architecture harness + final weighted scoring
```

Stop a candidate early only on a demonstrated hard-gate failure that cannot be fixed behind a bounded adapter without changing frozen semantics.

Do **not** stop because another candidate looks faster in an early microbenchmark.

---

# 10. DONE / TODO

## DONE

- [x] Candidate-neutral qualification structure defined.
- [x] Common fixture families defined.
- [x] Build/WASM/replay/query/sculpt/mirror/scan/inspection/production/determinism/performance/interop tests specified.
- [x] Explicit adjunct-admission trigger defined.
- [x] Performance qualification kept separate from unapproved hidden budgets.
- [x] Frozen `AUTH-C01..C22` mapped into final engine harness phase.

## TODO

- [ ] Materialize the PoC harness in code on a dedicated architecture-evaluation branch/task.
- [ ] Pin toolchains and record candidate dependency manifests.
- [ ] Build `FIX-GEOM-*`, `FIX-SCAN-*`, `FIX-PROD-*` candidate-neutral fixtures.
- [ ] Execute Q0 for both candidates before candidate-specific optimization.
- [ ] Define/approve an engineering `ARCH-PERF-*` profile after baseline measurements.
- [ ] Run Q1..Q7 and update the scorecard with evidence grades.
- [ ] Perform legal review before closing HG-13.
- [ ] Keep Project Schema v0.2 unmaterialized unless separately authorized.
- [ ] Keep `TD-CI-001` deferred and out of this workstream.

---

# 11. Handover

**Next executable work:** create the smallest candidate-neutral C++20 harness and run **Q0** against the pinned OpenSubdiv and openNURBS baselines, including direct Emscripten/WASM build attempts. Capture failures as evidence; do not work around them by changing frozen semantics. After Q0, proceed to one shared canonical orthosis control fixture before any high-level operator implementation.