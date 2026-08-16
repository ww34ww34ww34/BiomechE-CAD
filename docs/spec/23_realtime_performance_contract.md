# BiomechE-CAD — Realtime Interaction & Performance Contract

**Version:** v1  
**Status:** **FROZEN PERFORMANCE DOCTRINE v1 — NUMERICAL BUDGETS OPEN**  
**Date:** 2026-08-16  
**Architecture:** engine-neutral; applies to native desktop, headless/server and web/WASM targets where supported.  
**Numerical authority:** `18_numerical_qualification_registry.md`.  
**Architecture qualification:** `validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`.

---

## 0. Purpose

Define **how BiomechE-CAD performance is measured, reported and qualified** before selecting a geometry engine or hardcoding performance thresholds.

Performance is a product requirement because authoring productivity depends on interactive feedback, but unsupported numbers are not requirements.

Core doctrine:

```text
MEASURE FIRST
PROFILE THE PIPELINE
OPTIMIZE PROVEN BOTTLENECKS
RE-MEASURE
```

and:

```text
MEASURED
!= QUALIFIED
```

Until an explicit performance profile owns a limit, results remain:

```text
MEASURED / NOT YET QUALIFIED
```

---

# 1. What performance means

BiomechE-CAD performance includes more than render FPS:

```text
interaction latency
geometry update latency
inspection/query latency
source/scan handling latency
commit/replay latency
manufacturing-geometry generation latency
render/presentation latency
memory footprint
allocation/churn
startup/load time
serialization/import/export time
WASM startup/heap/transfer where applicable
```

A high frame rate with delayed geometry or stale semantic state is not considered good interactive performance.

---

# 2. Performance authority model

```text
EngineeringPerformanceProfile
  profileId
  version
  targetPlatform
  workloadClass
  metricBudgets[]
  testEnvironmentRequirements
  evidence/decisionRef
  lifecycle
    OPEN
    PROVISIONAL
    QUALIFIED
    DEPRECATED
```

Performance budgets are engineering/product limits, not clinical thresholds, manufacturing tolerances or algorithm epsilons.

No fallback across these authority classes is allowed.

---

# 3. Required timing statistics

For steady-state timing distributions report at least:

```text
sampleCount
min
p50
p95
p99
max
mean
```

Also report where relevant:

```text
standard deviation / dispersion
warmup count
cold-start sample(s)
steady-state window
excluded sample rule
```

A single average is insufficient for interactive performance qualification.

---

# 4. Environment manifest

Every benchmark/qualification result records enough environment state to be reproducible:

```text
BenchmarkEnvironment
  platform/OS
  CPU model
  logical/physical core info where relevant
  RAM
  GPU + driver when used
  browser/runtime when WASM/web
  compiler/version
  build configuration
  optimization flags
  sanitizer/instrumentation state
  thread count / scheduling mode
  SIMD/GPU backend state
  geometry-engine tag/commit
  adapter/product commit
  dataset/fixture hashes
```

Results without environment/build provenance are exploratory only.

---

# 5. Workload tiers

Define benchmark workload tiers by **actual semantic workload and data size**, not arbitrary marketing labels.

Candidate tier dimensions:

```text
control/authoring element count
surface/face/triangle count
scan point/triangle count
number of visible sources
number of corrective elements
material region count
ROI/landmark count
inspection query count
pressure/result dataset size
history/replay operation count
```

Exact `SMALL/MEDIUM/LARGE` boundaries remain OPEN until representative project datasets are selected.

---

# 6. Interaction latency classes

Measure separately:

```text
INPUT_TO_PREVIEW
PARAMETER_TO_GEOMETRY
DIRECT_MANIPULATION_TO_GEOMETRY
GEOMETRY_TO_RENDER_BUFFER
RENDER_BUFFER_TO_PRESENTATION [when measurable]
APPLY_OPERATION
COMMIT_REVISION
UNDO_REDO_WORKING_STATE
```

End-to-end latency and internal stage timings should both be available during qualification so bottlenecks are not guessed.

---

# 7. Preview vs committed quality

BiomechE-CAD may use a lower-cost preview representation provided:

```text
semantic requested state is identical
preview quality state is visible/defined
commit/rebuild produces the qualified representation
preview does not become immutable source evidence
```

Performance optimization may reduce tessellation/render detail but may not silently change semantic dose or clinical/reference placement.

---

# 8. Incremental recomputation doctrine

The implementation SHOULD avoid recomputing unaffected work.

Measure:

```text
invalidated semantic operations
invalidated geometry region
recomputed control/surface elements
recomputed render elements
recomputed inspections
recomputed spatial index portions
```

If a local edit triggers full-scene rebuild, report it explicitly rather than hiding it behind aggregate timing.

Incremental caching is permitted only when caches are invalidated deterministically and remain rebuildable.

---

# 9. Allocation and memory doctrine

Measure where practical:

```text
steady-state allocations per operation/frame
bytes allocated
peak resident memory
geometry memory
scan/index memory
render-buffer memory
WASM heap baseline/peak
cache memory
```

Avoiding unnecessary allocation/copy is a preferred engineering direction, but no implementation technique is frozen before profiling.

Memory reduction must not discard source evidence/provenance required by committed projects.

---

# 10. Large scan handling

Large source scans are a first-class workload.

Measure independently:

```text
import/decode
quality analysis
processing/decimation
registration
spatial-index build
nearest/projection queries
visibility/render upload
memory peak
```

The product may use derived LOD/decimated copies for interaction, but the original source identity/hash and processing provenance remain intact under `20_input_scan_reference_data.md`.

---

# 11. Spatial-query performance

Operations such as conform, deviation, closest-point mapping and inspection may depend on spatial acceleration.

Measure:

```text
index build time
index memory
query batch size
query throughput
p50/p95/p99 query batch latency
incremental rebuild/update cost
accuracy/residual state
```

A faster approximate query path must be explicitly labelled/versioned and qualified for its intended use; performance cannot silently weaken geometric accuracy.

---

# 12. Inspection / deviation workloads

Benchmark:

```text
section generation
distance/height/angle inspection
thickness query
deviation map
manufactured-part comparison
```

Measure algorithm time separately from visualization/color-map generation.

---

# 13. Determinism vs performance

Optimization, parallelism, SIMD or GPU execution must not silently violate deterministic/version-bound replay requirements.

Qualification distinguishes:

```text
BYTE IDENTITY
GEOMETRIC EQUIVALENCE
SEMANTIC REPLAY EQUIVALENCE
```

Any tolerated numerical delta uses an explicit `ALGORITHM_NUMERICAL_TOLERANCE` from NREG, never a manufacturing or clinical limit.

---

# 14. Native desktop performance

Native qualification should record:

```text
cold startup
project load
steady interaction
CPU/GPU backend state
memory
threading
headless geometry path
render path separately where possible
```

No desktop-specific acceleration may become semantic authority.

---

# 15. Headless/server performance

The same product-owned semantic/core pipeline should be measurable without GUI presentation for operations such as:

```text
replay/rebuild
inspection
scan mapping
manufacturing geometry generation
import/export validation
```

This separates core geometry cost from UI/rendering cost and supports server deployment where selected.

---

# 16. Web/WASM performance

Where web/WASM is a supported target, measure:

```text
WASM/module download or package size [as deployment context]
initialization/startup
baseline heap
peak heap
JS↔WASM boundary calls
bulk data transfer/copy cost
geometry/core operation timings
render-buffer handoff
thread/SIMD configuration
native-vs-WASM numerical equivalence
```

WASM capability is not assumed because a library is C++; it must be built and measured.

---

# 17. Rendering performance

Render benchmarks distinguish:

```text
scene preparation
CPU transform/update
GPU/buffer upload
raster/presentation
UI overlay/layout
```

Report at least frame time distribution rather than FPS alone when frame pacing matters.

A render optimization may use LOD, culling or cached buffers provided quantitative/semantic source state remains exact and inspectable.

---

# 18. Latest-state-wins interaction

For continuous pointer/slider interaction, implementations may coalesce intermediate preview requests when generation rate exceeds display/update capacity, provided:

```text
latest requested semantic state wins
commit uses exact current requested state
no stale preview is presented as current
coalescing is measurable during performance tests
```

Queueing every obsolete intermediate preview is not a product requirement.

---

# 19. Benchmark fixture governance

Every benchmark fixture has:

```text
fixtureId/version
semantic purpose
source hashes
expected geometry/data scale
operation sequence
result correctness checks
benchmark-only vs acceptance role
```

Candidate-neutral fixtures are required for geometry-engine comparison before candidate-specific optimization.

Architecture qualification already reserves fixtures such as:

```text
FIX-GEOM-01
FIX-SCAN-01
FIX-ORTH-01
FIX-PROD-01
FIX-MIRROR-01
FIX-DEV-01
```

---

# 20. Correctness gate before performance comparison

A timing result is not comparable if candidates/versions perform materially different work.

Before comparing performance verify:

```text
same semantic input
same output/inspection requirement
same accepted approximation/quality level
same fixture
same validation state
```

If quality differs, report separate quality-performance points rather than claiming a single winner.

---

# 21. Profiling doctrine

When performance misses a qualified or desired target:

1. capture end-to-end timing;
2. instrument major pipeline stages;
3. identify dominant measured cost;
4. change the smallest relevant layer;
5. rerun correctness + benchmark;
6. record before/after evidence.

Do not introduce caches, threads, retained native state or new dependencies purely from intuition if profiling can identify the bottleneck first.

---

# 22. Regression policy

A qualified performance profile should define allowed regression policy per workload/metric.

Until that policy exists, store historical benchmark results and surface statistically/materially notable regressions without automatic PASS/FAIL.

Performance changes that alter geometry/numerical results require correctness requalification as well as benchmark review.

---

# 23. Result state vocabulary

```text
NOT_MEASURED
MEASURED_NOT_QUALIFIED
PASS
FAIL
INDETERMINATE
NOT_COMPARABLE
```

`PASS/FAIL` requires an explicit EngineeringPerformanceProfile budget.

---

# 24. P0 acceptance / qualification tests

```text
PERF-001 timing report includes sample count + min/p50/p95/p99/max/mean
PERF-002 benchmark records exact environment/build/candidate/fixture versions
PERF-003 cold-start and steady-state are not silently mixed
PERF-004 render and core geometry time can be separated where applicable
PERF-005 local edit reports invalidation/recomputation scope
PERF-006 memory/peak memory reported for large scan workloads
PERF-007 source LOD/decimation does not replace original source lineage
PERF-008 spatial-query speed test also checks geometric correctness/residual
PERF-009 native-vs-WASM comparison reports numerical equivalence state
PERF-010 candidate comparison performs equivalent semantic work/quality
PERF-011 optimization benchmark includes before/after correctness evidence
PERF-012 no PASS/FAIL without explicit performance budget profile
PERF-013 algorithm epsilon remains separate from performance budget
PERF-014 commit uses exact latest requested semantic state after preview coalescing
PERF-015 caches are rebuildable and deterministic invalidation is testable
PERF-016 performance regression result preserves historical benchmark provenance
```

---

# 25. Open performance budgets

As of this freeze, numerical budgets for the following remain **OPEN**:

```text
interactive p95 latency
frame-time target
local rebuild p95
full replay time
scan import/registration time
spatial query throughput
memory ceiling
WASM startup/heap ceiling
manufacturing generation time
```

They must be established from representative hardware/workloads and product requirements, then versioned as `ARCH-PERF-*` or equivalent EngineeringPerformanceProfiles.

No value from a geometry library benchmark, manufacturing tolerance, display refresh rate or clinical literature automatically becomes a product limit.

---

# 26. Frozen invariants

```text
average alone != latency qualification
FPS alone != interactive performance
measured != qualified
preview quality reduction != semantic dose reduction
cache != source authority
faster approximate result != qualified equivalent result
algorithm tolerance != performance budget
native result != assumed WASM result
optimization intuition != profiling evidence
```

---

# 27. Product conclusion

BiomechE-CAD performance work must always answer:

```text
What exact semantic workload was measured?
On which build/hardware/runtime?
What does the latency distribution look like?
Where did the time/memory go?
What was invalidated/recomputed?
Did correctness remain equivalent?
Was this merely measured, or against an approved budget?
```

This doctrine is frozen before geometry-engine selection so the engine is judged against the product rather than the product being retrofitted to the engine.
