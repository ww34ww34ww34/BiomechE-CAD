# BiomechE-CAD — Q0 Harness Validation

**Date:** 2026-08-16  
**Status:** PASS FOR HARNESS / CANDIDATE BUILDS STILL NOT EXECUTED  
**Purpose:** validate the BiomechE-owned Q0 harness independently from third-party candidate compilation.

---

## 1. Local validation environment

```text
Python       3.13.5
CMake        3.31.6
C++ compiler Debian g++ 14.2.0
Node         v22.16.0
Emscripten   NOT INSTALLED (`emcmake`/`emcc` absent)
Git          2.47.3
```

This environment does not contain the pinned OpenSubdiv/openNURBS source trees and cannot resolve GitHub through direct `git clone`; candidate build PASS is therefore not claimed.

---

## 2. Runner syntax / NOT_EXECUTED semantics

`run_q0.py` was reconstructed from the committed source and passed Python bytecode compilation:

```text
python3 -m py_compile run_q0.py
PASS
```

The WASM path was exercised in an environment without Emscripten.

Observed result:

```json
{
  "schema": "BiomechE.CAD.GeometryEngineQ0Result/1",
  "candidateId": "opensubdiv",
  "mode": "wasm",
  "status": "NOT_EXECUTED",
  "reason": "emcmake_not_found"
}
```

Observed process exit:

```text
3
```

This confirms the runner does not silently turn a missing toolchain into PASS or candidate FAIL.

---

## 3. Common adapter/executable C++20 smoke

The product-owned `adapter.hpp` + `main.cpp` contract was compiled with a local stub adapter under:

```text
-std=c++20 -Wall -Wextra -Wpedantic
```

Observed output:

```json
{"candidateId":"stub","candidateVersion":"0","capabilityMask":5,"ok":true}
```

Result: **PASS** for the candidate-neutral ABI-free C++ harness structure.

---

## 4. Candidate adapter source-shape compile smoke

Because upstream source trees were unavailable locally, temporary minimal headers reproducing only the exact API signatures used by the Q0 adapters were created from the pinned upstream primary-source definitions.

Both adapter translation units compiled and ran through the same common harness:

```text
opensubdiv 1
opennurbs 1
```

This validates:

- namespace/include/factory usage in our adapter source shape;
- candidate type containment behind `biomeche_q0/adapter.hpp`;
- common factory/executable linkage pattern.

It **does not** validate upstream library compilation, transitive dependencies, ABI behavior, numerical behavior or WASM portability. Those remain actual Q0 candidate executions.

---

## 5. Upstream API cross-check

Pinned OpenSubdiv primary source confirms:

```text
TopologyRefinerFactory<MESH>::Options()
  defaults to Catmull-Clark
  exposes validateFullTopology
TopologyRefinerFactory<MESH>::Create(...)
TopologyRefiner::GetLevel(int)
TopologyLevel::GetNumVertices()/GetNumFaces()
```

Pinned openNURBS source documents `ON::Version()` as the supported application version query, and its public toolkit header exposes the normal standalone-application include path. `ON_SubD` is part of the public header set.

This provides primary-source API evidence for the Q0 smoke source, while actual compilation remains the final proof.

---

## 6. Harness verdict

```text
Python runner syntax                         PASS
Missing-Emscripten truthfulness              PASS
Common C++20 adapter contract                PASS
Candidate source-shape compile smoke         PASS
Candidate-native OpenSubdiv build            NOT EXECUTED
Candidate-native openNURBS build             NOT EXECUTED
Direct Emscripten OpenSubdiv build            NOT EXECUTED
Direct Emscripten openNURBS build             NOT EXECUTED
```

**Q0 HARNESS = READY FOR REAL EXECUTION.**

No architecture gate that requires actual candidate compilation is promoted to PASS by this harness validation.
