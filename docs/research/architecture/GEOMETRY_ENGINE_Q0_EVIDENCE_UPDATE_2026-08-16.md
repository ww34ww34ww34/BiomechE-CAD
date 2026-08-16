# BiomechE-CAD — Geometry Engine Q0 Evidence Update

**Date:** 2026-08-16  
**Status:** Q0 HARNESS READY / REAL CANDIDATE BUILDS PENDING  
**Selection status:** **NO WINNER**

---

## 1. Purpose

Record the transition from architecture planning to executable Q0 qualification without prematurely scoring unexecuted candidate builds.

Canonical harness:

`qualification/geometry-engine/q0/`

---

## 2. Pinned candidates

### A — Pixar OpenSubdiv

```text
tag       v3_7_0
commit    9dab8a47bfbb1388ec8388fe61f5f916e6123f38
```

Primary-source evidence supports:

- high-performance subdivision evaluation on CPU/GPU;
- core C++ libraries without dependencies beyond the C++ standard library;
- optional Osd/render/example dependencies separable by build configuration;
- a dedicated static CPU target `osd_static_cpu` in the pinned source;
- candidate-neutral construction from `Far::TopologyDescriptor` / `TopologyRefinerFactory`.

Q0 harness uses only the headless CPU/core target.

### B — McNeel openNURBS / ON_SubD

```text
ref       8.x snapshot
commit    00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
```

Primary-source evidence supports:

- standalone C++ toolkit without requiring Rhino process/runtime for normal openNURBS application use;
- public `ON_SubD` type plus broad NURBS/geometry/3dm toolkit;
- upstream static target `opennurbsStatic`;
- broader platform dependency footprint than the minimal OpenSubdiv core path, including zlib and platform-specific dependencies; the pinned CMake also includes freetype/uuid on Linux.

This broader footprint is a Q0 dependency fact, not a negative final score by itself.

---

## 3. Product-owned containment evidence

The Q0 product header contains no candidate-native type:

`qualification/geometry-engine/q0/include/biomeche_q0/adapter.hpp`

Candidate-specific types are isolated to:

```text
src/candidate_opensubdiv.cpp
src/candidate_opennurbs.cpp
```

Common executable:

`src/main.cpp`

Common C++ standard:

```text
C++20
```

This is positive evidence for the feasibility of `HG-01` semantic isolation and `HG-14` dependency containment, but actual target-toolchain builds remain required before marking those gates PASS.

---

## 4. Harness validation already executed

`qualification/geometry-engine/q0/results/Q0_HARNESS_VALIDATION_2026-08-16.md`

Observed:

```text
Python runner syntax                         PASS
missing-Emscripten truthfulness              PASS
common C++20 adapter contract                PASS
candidate source-shape compile smoke         PASS
```

These tests validate BiomechE-owned qualification infrastructure only.

---

## 5. Actual Q0 execution status

```text
OpenSubdiv native Release       NOT EXECUTED
OpenSubdiv headless/server      NOT EXECUTED
OpenSubdiv direct WASM          NOT EXECUTED
openNURBS native Release        NOT EXECUTED
openNURBS headless/server       NOT EXECUTED
openNURBS direct WASM           NOT EXECUTED
```

Current chat runtime has native C++/CMake/Node, but no Emscripten and no direct clone/DNS path for pulling the pinned third-party trees into the local execution container. Therefore no candidate compilation is claimed.

---

## 6. Gate interpretation

```text
HG-01 semantic isolation       POSITIVE STRUCTURAL EVIDENCE / BUILD CONFIRMATION PENDING
HG-10 native+server+WASM       UNKNOWN / EXECUTION REQUIRED
HG-13 license/distribution     UPSTREAM TERMS CAPTURED / FORMAL REVIEW REQUIRED
HG-14 dependency containment   PARTIAL POSITIVE EVIDENCE / BUILD CONFIRMATION PENDING
```

No weighted final score and no winner should be declared from this evidence update.

---

## 7. Exact next work

Run `qualification/geometry-engine/q0/run_q0.py` against the exact pinned source trees on the local/toolchain machine and commit the generated JSON evidence.

Only after those builds should Q0 gates be promoted to PASS/FAIL and Q1 begin.
