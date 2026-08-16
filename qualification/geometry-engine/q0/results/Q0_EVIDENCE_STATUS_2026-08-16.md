# BiomechE-CAD — Q0 Geometry Engine Evidence Status

**Date:** 2026-08-16  
**Status:** HARNESS READY / CANDIDATE BUILDS NOT YET EXECUTED  
**Selection:** **NO WINNER**

---

## 1. Candidate pins

### OpenSubdiv

```text
upstream       PixarAnimationStudios/OpenSubdiv
tag            v3_7_0
tag object     4951f30c00f395aa831a9fc42577cc28ce46fa81
commit         9dab8a47bfbb1388ec8388fe61f5f916e6123f38
license blob   aa357669b831a0bc7ebb827181b060782b580f24
```

Upstream primary documentation states that the core libraries are C++ with no dependencies beyond the C++ standard library, while Osd GPU/display paths and examples have optional dependencies. The pinned CMake tree creates `osd_static_cpu`, which is the Q0 target used by the headless adapter.

### openNURBS / ON_SubD

```text
upstream       mcneel/opennurbs
ref            8.x snapshot
commit         00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
license blob   101db5f8f5b99e27d7142bc1074c8159924e68de
cmake blob     5a1044c6934c0d01b1c88353ec948c8c6a7f982d
```

The pinned upstream CMake declares C++17 internally and creates `opennurbsStatic` / `OpenNURBS`; platform-specific dependencies are linked by the upstream target. On Linux the public static target links zlib, freetype and the uuid helper; Windows links Shlwapi/Usp10/zlib in the upstream CMake path. The public MSVC convenience header also documents static-link dependencies including zlib/freetype and Windows libraries.

These facts are dependency evidence, not performance or suitability scores.

---

## 2. Adapter containment

Implemented:

```text
include/biomeche_q0/adapter.hpp
src/main.cpp
src/candidate_opensubdiv.cpp
src/candidate_opennurbs.cpp
```

The product-owned header contains no `OpenSubdiv::*` or `ON_*` type.

Candidate native types are confined to implementation units:

```text
OpenSubdiv adapter -> Far::TopologyDescriptor / TopologyRefiner
openNURBS adapter  -> ON_SubD / ON::Version()
```

This is the intended evidence shape for `HG-01`/`HG-14`; final gate PASS still requires actual build/link execution on the target toolchains.

---

## 3. Build containment

Implemented:

```text
CMakeLists.txt
cmake/CandidateOpenSubdiv.cmake
cmake/CandidateOpenNurbs.cmake
run_q0.py
```

OpenSubdiv Q0 explicitly disables optional examples, tutorials, regression, Ptex, docs, OpenMP, TBB, CUDA, OpenCL, OpenGL and Metal and links only `osd_static_cpu`.

openNURBS Q0 uses the upstream `opennurbsStatic` target rather than copying a subset of source files. This keeps dependency evidence honest and lets upstream define the source compilation set.

---

## 4. WASM evidence policy

Emscripten documentation confirms the expected cross-compilation model: existing CMake/make-based C/C++ projects can be configured through the Emscripten wrappers/toolchain and linked to JS+WebAssembly output. This establishes the **test method**, not candidate support.

Therefore neither candidate receives a WASM PASS until the exact Q0 harness actually configures/builds/runs through Emscripten.

For openNURBS, rhino3dm's WebAssembly precedent remains supporting ecosystem evidence only; the Q0 test deliberately targets the same product-owned native adapter and direct openNURBS source snapshot.

---

## 5. Execution matrix

| Cell | Current status | Evidence needed for PASS |
|---|---|---|
| OpenSubdiv native Release | **NOT EXECUTED** | configure + build + smoke exit 0 + dependencies/sizes |
| OpenSubdiv headless/server | **NOT EXECUTED** | same native headless executable on target/server toolchain |
| OpenSubdiv Emscripten/WASM | **NOT EXECUTED** | configure + build + node/browser smoke + sizes/toolchain |
| openNURBS native Release | **NOT EXECUTED** | configure + build + smoke exit 0 + dependencies/sizes |
| openNURBS headless/server | **NOT EXECUTED** | same native headless executable on target/server toolchain |
| openNURBS Emscripten/WASM | **NOT EXECUTED** | configure + build + node/browser smoke + sizes/toolchain |

`NOT EXECUTED` is not FAIL and is not PASS.

---

## 6. Q0 gate status

```text
HG-01 semantic isolation       EVIDENCE POSITIVE / BUILD CONFIRMATION PENDING
HG-10 one core native+WASM     UNKNOWN / EXECUTION REQUIRED
HG-13 license/distribution     REVIEW REQUIRED; upstream terms captured
HG-14 dependency containment   PARTIAL EVIDENCE / BUILD CONFIRMATION PENDING
```

No weighted score should be finalized from this Q0 preparation alone.

---

## 7. Exact next execution

On a machine with the pinned source trees:

```bash
python qualification/geometry-engine/q0/run_q0.py \
  --candidate opensubdiv \
  --source-root <OpenSubdiv-v3_7_0> \
  --mode native --clean

python qualification/geometry-engine/q0/run_q0.py \
  --candidate opensubdiv \
  --source-root <OpenSubdiv-v3_7_0> \
  --mode wasm --clean

python qualification/geometry-engine/q0/run_q0.py \
  --candidate opennurbs \
  --source-root <opennurbs-00bdd2ce> \
  --mode native --clean

python qualification/geometry-engine/q0/run_q0.py \
  --candidate opennurbs \
  --source-root <opennurbs-00bdd2ce> \
  --mode wasm --clean
```

The generated JSON evidence must be committed before changing Q0 gates to PASS.
