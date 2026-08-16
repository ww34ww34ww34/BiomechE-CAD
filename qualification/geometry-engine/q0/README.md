# BiomechE-CAD — Geometry Engine Qualification Q0

**Status:** EXECUTION HARNESS v0.1  
**Scope:** Q0 only — native/headless/WASM build and dependency containment  
**Selection status:** **NO WINNER**

This directory implements the first executable layer of `docs/validation/GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md`.

It deliberately tests only whether the same small **product-owned C++20 adapter boundary** can contain each candidate. It does not select a geometry engine and does not encode clinical/product semantics in candidate-native objects.

## Candidate locks

See `candidate-lock.json`.

Current frozen-for-Q0 pins:

```text
OpenSubdiv
  tag       v3_7_0
  commit    9dab8a47bfbb1388ec8388fe61f5f916e6123f38

openNURBS
  ref       8.x snapshot
  commit    00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
```

These pins are qualification inputs, not a decision that they remain the permanent production versions.

## Harness contract

The harness exposes one candidate-neutral factory:

```cpp
std::unique_ptr<biomeche::q0::Adapter> make_adapter();
```

and a common result shape:

```text
candidate id
candidate version/pin
smoke success
capability flags
```

Candidate-specific types are confined to candidate source files and must not cross `include/biomeche_q0/adapter.hpp`.

## Native/headless build

OpenSubdiv:

```bash
cmake -S . -B build-osd \
  -DCMAKE_BUILD_TYPE=Release \
  -DBIOMECHE_Q0_CANDIDATE=opensubdiv \
  -DBIOMECHE_OPENSUBDIV_ROOT=/path/to/OpenSubdiv
cmake --build build-osd --config Release
./build-osd/biomeche_geometry_q0_smoke
```

openNURBS:

```bash
cmake -S . -B build-on \
  -DCMAKE_BUILD_TYPE=Release \
  -DBIOMECHE_Q0_CANDIDATE=opennurbs \
  -DBIOMECHE_OPENNURBS_ROOT=/path/to/opennurbs
cmake --build build-on --config Release
./build-on/biomeche_geometry_q0_smoke
```

The executable is headless and has no rendering/UI dependency.

## WASM build

Use the same source tree and adapter through the Emscripten toolchain:

```bash
emcmake cmake -S . -B build-osd-wasm \
  -DCMAKE_BUILD_TYPE=Release \
  -DBIOMECHE_Q0_CANDIDATE=opensubdiv \
  -DBIOMECHE_OPENSUBDIV_ROOT=/path/to/OpenSubdiv
cmake --build build-osd-wasm --config Release
```

and equivalently for openNURBS.

For Q0 the web target is a compile/link/runtime smoke only. Browser filesystem, rendering and persistent storage are not product decisions here.

## Required evidence per executed configuration

Record at minimum:

```text
candidate pin
source/license hash
host OS/arch
compiler + version
CMake version
C++ standard
build type/flags
static/dynamic dependency list
binary or wasm size
build duration
runtime exit/status
WASM toolchain/version/flags where applicable
```

Use `results/Q0_EVIDENCE_STATUS_2026-08-16.md` as the current ledger and create machine-readable result artifacts when execution starts.

## Current status

The repository-side harness and upstream evidence/pins are prepared. Actual candidate compilation has **not** been claimed from this chat environment because the pinned third-party source trees/toolchains are not present locally and CI repair/use is deliberately outside this phase.

Therefore current build cells remain:

```text
OpenSubdiv native      NOT EXECUTED
OpenSubdiv WASM        NOT EXECUTED
openNURBS native       NOT EXECUTED
openNURBS WASM         NOT EXECUTED
```

This is correct `OPEN/NOT EXECUTED` evidence, not a failure and not a PASS.
