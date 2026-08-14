# BiomechE-CAD — Geometry Stack Deep Research (validated)

**Date:** 2026-08-14  
**Status:** VALIDATED WITH MINOR CORRECTIONS  
**Source:** user-supplied `deep-research-report_BiomechE-CAD.md`  
**Purpose:** archive the deeper library/portability/stack analysis after checking it against the current BiomechE-CAD v2 capability baseline and current primary upstream documentation.

---

## 1. Validation verdict

The research is **architecturally coherent with the current BiomechE-CAD baseline**.

The main conclusion is retained:

```text
BiomechCore = product-owned geometry/domain core

P0 expected external geometry dependency:
    OpenSubdiv

First conditional second dependency:
    Manifold

Adapters only when a real requirement appears:
    openNURBS / rhino3dm  -> .3dm / Rhino / NURBS interoperability
    OCCT                  -> STEP / IGES / exact B-Rep / general CAD
```

This matches the project decisions already recorded in `docs/DECISIONS.md`:

- `D-CAD-011` — OpenSubdiv-first control-cage architecture;
- `D-CAD-012` — general NURBS/B-Rep is not a P0 prerequisite;
- `D-CAD-013` — additional geometry libraries must earn entry through a failing fixture;
- `D-CAD-014` — clinical upper surface and manufacturing body are separate layers.

The report is therefore archived as **research evidence and implementation guidance**, not as an automatic freeze of every proposed technology.

---

## 2. Important distinction preserved

The most useful architectural statement in the research is:

> A single geometry core does not mean one binary artifact. It means one authoritative model, one semantic contract, one source implementation and one API boundary, compiled for the required targets.

The candidate implementation shape is:

```text
                   BiomechCore C++20
                         │
              ┌──────────┴──────────┐
              │                     │
        OpenSubdiv               Product-owned
        evaluator                domain algorithms
              │                     │
              └──────────┬──────────┘
                         │
                    C ABI candidate
                         │
               ┌─────────┴─────────┐
               │                   │
            WebAssembly         native server
```

`C++20`, a small `C ABI`, and FlatBuffers are **recommended candidates** from this research. They are not yet frozen project decisions and still require implementation spikes.

---

## 3. Upstream facts revalidated on 2026-08-14

### 3.1 OpenSubdiv

**Validated version:** `3.7.0`.

Official OpenSubdiv release notes identify 3.7.0 as the October 2025 release. Official documentation states that the library implements high-performance subdivision-surface evaluation and is optimized for deforming surfaces with static topology at interactive frame rates.

The core libraries are C++ and have no mandatory dependency beyond the C++ standard library. Optional `Osd` backends cover CPU/GPU APIs including TBB, CUDA, OpenCL, OpenGL/DX11/Metal-related paths depending on build configuration.

Official sources:

- https://opensubdiv.org/docs/release_notes.html
- https://opensubdiv.org/
- https://opensubdiv.org/docs/osd_overview.html
- https://opensubdiv.org/docs/cmake_build.html
- https://github.com/PixarAnimationStudios/OpenSubdiv

**BiomechE-CAD consequence:** OpenSubdiv remains the strongest P0 candidate for evaluating the clinical control cage / smooth limit surface.

**Important caveat:** Pixar does not publish an official browser package equivalent to `rhino3dm.wasm` or Manifold's packaged WASM binding. A BiomechE WebAssembly build is therefore a project qualification task, not an upstream-guaranteed product artifact.

---

### 3.2 Manifold

**Validated version:** `3.5.2`, released 2026-06-27.

Official upstream describes Manifold as a geometry library for manifold triangle meshes, with reliability/manifold output as its primary goal. Current upstream documentation states that there are no mandatory external dependencies; TBB, Emscripten, Nanobind and others are optional depending on enabled features.

The repository contains C, Python and JS/TS/WASM binding paths. Official build documentation explicitly warns that although recent Emscripten builds can enable `MANIFOLD_PAR=ON`, parallel WASM is not currently recommended because potential memory-corruption problems may occur.

Official sources:

- https://github.com/elalish/manifold
- https://github.com/elalish/manifold/releases

**BiomechE-CAD consequence:** Manifold remains the most plausible **conditional second geometry library** when production fixtures demonstrate a need for robust solid-mesh boolean/solid operations or production-body robustness.

It is **not** promoted to mandatory P0 merely because it is useful.

Recommended initial WASM qualification stance:

```text
MANIFOLD_PAR = OFF
```

until an explicit multithreaded WASM qualification is performed.

---

### 3.3 rhino3dm / openNURBS

The research's version distinction is valid:

- rhino3dm changelog: `8.32.1` on 2026-07-29;
- npm `rhino3dm`: `8.32.1`;
- NuGet `Rhino3dm`: `8.32.0` at the validation date.

The 8.32 line added richer JS/Python SubD access including control-net/connectivity information; 8.32.1 added a point-cloud typed-array export path.

Official sources:

- https://github.com/mcneel/rhino3dm
- https://github.com/mcneel/rhino3dm/blob/8.x/CHANGELOG.md
- https://www.npmjs.com/package/rhino3dm
- https://www.nuget.org/packages/Rhino3dm
- https://github.com/mcneel/opennurbs

rhino3dm officially exposes geometry based on openNURBS to .NET, Python and JavaScript/WASM and supports `.3dm`, NURBS, B-Reps as data structures, meshes and SubD.

**BiomechE-CAD consequence:** useful adapter if exact `.3dm` / Rhino interoperability becomes a requirement. It is not a reason to replace OpenSubdiv in P0 without a measured evaluation benchmark.

openNURBS itself should be pinned to an exact commit/version lineage rather than treated as a conventional independent SemVer release stream.

---

### 3.4 Open CASCADE Technology (OCCT)

The broad capability assessment is correct: OCCT is a full CAD/CAM/CAE kernel family with B-Rep, modeling algorithms and industrial data exchange, including STEP and IGES.

Official 8.0 documentation requires C++17 and documents supported Web/Emscripten builds in addition to desktop/mobile platforms.

**Correction to the wording of the original research:**

`8.0.0.p1` was officially announced by Open Cascade on 2026-06-17 as a hot patch on top of 8.0.0. GitHub's ordinary Releases page still exposes `V8_0_0` as the latest standard release entry. Therefore the archived wording should be:

```text
OCCT 8.0.0.p1 = official 8.0.0 hot patch announcement
```

rather than implying that it appears identically as the normal GitHub `Latest` release artifact.

Official sources:

- https://dev.opencascade.org/doc/overview/html/index.html
- https://dev.opencascade.org/doc/overview/html/build_upgrade__building_occt.html
- https://dev.opencascade.org/about/data_exchange
- https://github.com/Open-Cascade-SAS/OCCT
- https://github.com/Open-Cascade-SAS/OCCT/discussions/1316

**BiomechE-CAD consequence:** OCCT remains a feature-triggered adapter candidate for exact B-Rep / STEP / IGES / industrial CAD round-trip. Current P0 orthosis behavior does not justify making it a foundation dependency.

---

### 3.5 FlatBuffers

The research's basic assessment is valid.

Base release line verified: `25.12.19`, with a later hotfix-style tag `v25.12.19-2026-02-06-03fffb2`.

Official FlatBuffers documentation supports C++, C#, JavaScript/TypeScript and many other languages and allows direct reading of serialized buffers without a mandatory full unpack step.

Official sources:

- https://github.com/google/flatbuffers
- https://github.com/google/flatbuffers/releases
- https://flatbuffers.dev/support/

**BiomechE-CAD consequence:** FlatBuffers is a strong candidate for project/document/IPC serialization, but should not be placed in the pointer-drag/render hot path simply because it is efficient.

The recommended separation remains:

```text
Document / commands / persistence -> schema-based serialization
Realtime geometry buffers          -> direct memory / typed arrays
```

---

### 3.6 geometry3Sharp

The report correctly distinguishes the old stable package from renewed development:

- NuGet stable package: `1.0.324`, last updated in 2019;
- upstream README, updated in 2026, states active work has resumed on a modern `.NET 8` branch.

The library contains `DMesh3`, remeshing, spatial queries, SDF/implicit tools and Marching Cubes.

Official sources:

- https://github.com/gradientspace/geometry3Sharp
- https://www.nuget.org/packages/geometry3Sharp

**BiomechE-CAD consequence:** useful algorithmic reference and possible host-side utility, but adding it as a second authoritative geometry ecosystem would conflict with the single-core goal unless a very specific use case justifies it.

---

### 3.7 TinySpline

NuGet `tinyspline 0.6.0.1` is verified. The package describes an ANSI C core for NURBS/B-spline/Bézier curves with multiple generated bindings.

Official/package source:

- https://www.nuget.org/packages/tinyspline
- https://github.com/msteinbeck/tinyspline

**BiomechE-CAD consequence:** a reasonable small utility candidate if P1 spline-curve requirements grow; not a surface/solid kernel.

---

### 3.8 Verb

The caution in the research is justified. The official repository still has open issues involving modern Haxe dependency/toolchain compatibility and other NURBS behavior.

Official source:

- https://github.com/pboyer/verb

**BiomechE-CAD consequence:** no current advantage strong enough to make Verb part of the new C++-centric universal geometry core.

---

## 4. Architecture conclusions accepted from the research

### 4.1 Product-owned core, not library-owned document model

No third-party internal type should become the canonical project schema.

Do not persist or expose as product-level identities:

```text
Far::TopologyRefiner
manifold::Manifold
ON_Brep / ON_SubD
TopoDS_Shape
```

Persist product semantics instead:

```text
BiomechDocument
 ├─ BaseCage
 │   ├─ stable vertex IDs
 │   ├─ faces / boundary / crease semantics
 │   └─ intrinsic anatomical coordinates
 ├─ ClinicalOperation[]
 ├─ ScanReference
 └─ ProductionSettings
```

Third-party objects are derived adapter/cache/runtime objects.

### 4.2 OpenSubdiv and Manifold are complementary rather than redundant

Conceptual split:

```text
OpenSubdiv
    -> clinical smooth limit surface

BiomechE-CAD domain algorithms
    -> thickness / lower rule / sidewall / closure

Manifold [only if qualified]
    -> robust solid-mesh operations / final production solid cases
```

This is a substantially cleaner overlap profile than pairing multiple NURBS/B-Rep kernels.

### 4.3 Adapter trigger rules

```text
Need .3dm / Rhino exact interchange?
    -> evaluate openNURBS / rhino3dm adapter

Need STEP / IGES / exact trimmed B-Rep / industrial CAD round-trip?
    -> evaluate OCCT adapter

Need robust arbitrary solid-mesh boolean or production fixture fails?
    -> evaluate Manifold

Need only lightweight P1 B-spline curves?
    -> evaluate TinySpline or a small in-house implementation
```

---

## 5. Recommendations that remain hypotheses, not frozen decisions

The following points are technically credible and worth spiking, but the research alone does not freeze them:

### 5.1 C++20 as the universal core implementation language

Strong candidate because it can compile native and through Emscripten, while both OpenSubdiv and Manifold are C++-native.

Still requires proof through the actual BiomechE build/toolchain and deployment targets.

### 5.2 Small C ABI as the authoritative host boundary

Architecturally sound because it hides C++ ABI and third-party types.

Still an API design decision that should be frozen only after the first headless core spike.

### 5.3 Same WebAssembly geometry artifact in browser, desktop WebView and mobile WebView

Technically plausible, but **not yet qualified** as a product deployment guarantee.

It needs explicit measurements for:

```text
iOS/WKWebView memory
startup/download size
single-thread CPU latency
SIMD availability
thread/SharedArrayBuffer policy
large scan memory behavior
background/foreground lifecycle
mobile thermal throttling
```

Native mobile bindings should not be built prematurely, but neither should they be ruled out before the WASM mobile spike passes.

### 5.4 Native server build from the same source rather than server-side WASM

This remains the preferred candidate because it preserves semantic/source identity while allowing native optimization. It should be verified through deterministic native-vs-WASM golden tests.

---

## 6. WebAssembly-specific validation rules accepted

Initial browser spike should be conservative:

```text
OpenSubdiv CPU path
no native graphics backend dependency
no TBB initially
Manifold parallel OFF if Manifold is present
run core in a Worker where practical
renderer remains separate
```

Do not require WebGPU compute or pthread/TBB WebAssembly for P0.

Measure the complete latency path, not only library evaluation time:

```text
T_total =
    event
  + JS/WASM boundary
  + clinical deformation
  + subdivision
  + normals
  + buffer handling
  + GPU upload
  + render
```

Important metrics:

```text
P50/P95/P99 update latency
peak WASM memory
WASM memory growth count
bytes copied per frame
JS/WASM calls per frame
startup/download size
large allocations during drag
main-thread stalls > 50 ms
native/WASM metric divergence
```

---

## 7. Recommended qualification stack

### Stage A — minimal core

```text
BiomechCore
+ OpenSubdiv 3.7.0
+ product-owned cage/operators/masks/query/DFM
```

### Stage B — production challenge

Run actual closure/thickness/watertight fixtures.

If proprietary production construction remains robust, Manifold stays out.

If it fails reproducibly or maintenance cost becomes excessive:

```text
BiomechCore
+ OpenSubdiv
+ Manifold
```

### Stage C — interoperability adapters

Only when product requirements appear:

```text
Rhino/.3dm -> rhino3dm/openNURBS
STEP/IGES/exact B-Rep -> OCCT
```

---

## 8. Spike/decision gates

### OpenSubdiv gate

Use the existing `ORTHO_CAGE_41x17_V0` and BT/A fixtures.

Required proof:

```text
stable topology
repeatable limit evaluation
heel extreme
arch extreme
2° / 4° / 6° wedge
metatarsal element
sculpt
scan conform
mirror
interactive latency
native/WASM metric equivalence
```

### Manifold entry gate

Add only when one or more production fixtures fail without it:

```text
production closure
thickness repair
arbitrary imported element
boolean add/subtract
thin/narrow heel
self-intersecting modifier
watertight final body
```

### OCCT entry gate

```text
STEP required?                 NO
IGES required?                 NO
exact trimmed B-Rep required?  NO
industrial CAD round-trip?     NO
```

If all remain `NO`, OCCT remains outside the default stack.

### openNURBS/rhino3dm entry gate

```text
Need exact .3dm / Rhino interoperability?
```

Only a `YES` promotes the adapter.

---

## 9. Final validated hierarchy

```text
                    BIOMECH CORE
                         │
              ┌──────────┴──────────┐
              │                     │
        REQUIRED / P0          OUR DOMAIN
              │                     │
       OpenSubdiv 3.7.0       Clinical ops
                              masks / fields
                              scan / query
                              production
                              DFM / history
              │
              ▼
        evaluated geometry
              │
      ┌───────┴───────────────┐
      │                       │
  IF FIXTURE FAILS        FEATURE ADAPTERS
      │                       │
 Manifold 3.5.2        ┌──────┴───────────┐
                       │                  │
                  .3dm / Rhino       STEP / B-Rep
                       │                  │
                rhino3dm/openNURBS      OCCT
```

This hierarchy is consistent with `CAD_ENGINE_CAPABILITY_SPEC.md` v2 and with the current EasyCAD2 parity work.

---

## 10. Archive conclusion

**Accepted:** yes.

The deeper research materially improves the implementation plan and does not contradict the current OpenSubdiv-first architecture.

The following are accepted as current research conclusions:

1. OpenSubdiv is the only external geometry dependency with a strong present P0 case.
2. Manifold is the strongest conditional second dependency, specifically for solid/manufacturing problems.
3. rhino3dm/openNURBS and OCCT solve interoperability categories that are not current P0 requirements.
4. A product-owned document model and domain API must remain independent of all third-party geometry types.
5. Native and WebAssembly builds should be produced from the same geometry-core source where feasible.
6. WebAssembly portability, especially mobile, must be measured before being frozen.
7. Additional dependencies remain gated by failing fixtures or explicit commercial interoperability requirements.

No change is required to the current decision that general NURBS/B-Rep is not P0.

---

## 11. Source list used for validation

### OpenSubdiv
- https://opensubdiv.org/docs/release_notes.html
- https://opensubdiv.org/
- https://opensubdiv.org/docs/osd_overview.html
- https://opensubdiv.org/docs/cmake_build.html
- https://github.com/PixarAnimationStudios/OpenSubdiv

### Manifold
- https://github.com/elalish/manifold
- https://github.com/elalish/manifold/releases

### rhino3dm / openNURBS
- https://github.com/mcneel/rhino3dm
- https://github.com/mcneel/rhino3dm/blob/8.x/CHANGELOG.md
- https://www.npmjs.com/package/rhino3dm
- https://www.nuget.org/packages/Rhino3dm
- https://github.com/mcneel/opennurbs

### OCCT
- https://dev.opencascade.org/doc/overview/html/index.html
- https://dev.opencascade.org/doc/overview/html/build_upgrade__building_occt.html
- https://dev.opencascade.org/about/data_exchange
- https://github.com/Open-Cascade-SAS/OCCT
- https://github.com/Open-Cascade-SAS/OCCT/discussions/1316

### FlatBuffers
- https://github.com/google/flatbuffers
- https://github.com/google/flatbuffers/releases
- https://flatbuffers.dev/support/

### geometry3Sharp
- https://github.com/gradientspace/geometry3Sharp
- https://www.nuget.org/packages/geometry3Sharp

### TinySpline
- https://github.com/msteinbeck/tinyspline
- https://www.nuget.org/packages/tinyspline

### Verb
- https://github.com/pboyer/verb

### WebView2 shared-buffer reference used only as optional desktop escape hatch
- https://learn.microsoft.com/en-us/microsoft-edge/webview2/reference/winrt/microsoft_web_webview2_core/corewebview2sharedbuffer
