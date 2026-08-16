# BiomechE-CAD — Q0 Harness Validation

**Date:** 2026-08-16  
**Status:** **PASS FOR HARNESS / CANDIDATE BUILDS STILL NOT EXECUTED**  
**Purpose:** validate the BiomechE-owned Q0 qualification infrastructure independently from third-party candidate compilation.

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

The runtime does not contain the pinned OpenSubdiv/openNURBS source trees and direct `git clone` cannot resolve GitHub from the execution container. Actual candidate build PASS is therefore not claimed.

---

## 2. Runner syntax

Current strengthened `run_q0.py` passed Python bytecode compilation:

```text
python3 -m py_compile run_q0.py
PASS
```

---

## 3. Source-pin falsification tests

The runner now requires the exact commit from `candidate-lock.json`.

### Unverifiable source archive

Input: source directory with no Git metadata and no `--source-commit`.

Observed:

```text
exit   4
status NOT_EXECUTED
reason source_commit_unverified
```

**PASS:** unverified source is not compiled/qualified silently.

### Wrong declared commit

Input: source directory with a commit value different from the OpenSubdiv lock.

Observed:

```text
exit   5
status SOURCE_PIN_MISMATCH
```

**PASS:** a wrong upstream revision cannot masquerade as qualification evidence.

### Correct pin but missing Emscripten

Input: exact declared OpenSubdiv commit + license file, `--mode wasm`, no `emcmake` installed.

Observed:

```text
exit   7
status NOT_EXECUTED
reason emcmake_not_found
licenseSha256 recorded = true
```

**PASS:** missing WASM toolchain is neither candidate PASS nor candidate FAIL.

---

## 4. Evidence fields added to runner

For an executed build the runner records:

```text
expected upstream/ref/commit
actual or declared source commit
source-pin match
license SHA-256
host platform/system/architecture
Python/CMake/C++/Emscripten/Node versions
configure command/result/duration/stdout/stderr
build command/result/duration/stdout/stderr
CMakeCache SHA-256 + selected compiler/flags/generator entries
artifact paths/sizes/SHA-256
runtime result
native dependency probe via dumpbin / otool / ldd where available
```

This closes the main Q0 reproducibility-manifest gap for build smoke evidence.

---

## 5. Common adapter/executable C++20 smoke

The product-owned `adapter.hpp` + `main.cpp` contract was compiled with a local stub adapter under:

```text
-std=c++20 -Wall -Wextra -Wpedantic
```

Observed output:

```json
{"candidateId":"stub","candidateVersion":"0","capabilityMask":5,"ok":true}
```

Result: **PASS** for the candidate-neutral C++ harness structure.

---

## 6. Candidate adapter source-shape smoke

Temporary minimal headers reproducing only the exact pinned upstream API signatures used by the Q0 adapters were compiled through the common harness.

Observed:

```text
opensubdiv 1
opennurbs 1
```

This validates the BiomechE adapter source shape and factory/link organization. It does **not** validate the actual upstream build, transitive dependencies, ABI/numerical behavior or WASM portability.

Pinned upstream primary source separately confirms the OpenSubdiv factory/options/GetLevel API used by the adapter and the openNURBS public version/include/SubD path.

---

## 7. Harness verdict

```text
Python runner syntax                         PASS
source commit required/verified              PASS
wrong commit rejection                       PASS
missing-Emscripten truthfulness              PASS
license hash evidence path                   PASS
common C++20 adapter contract                PASS
candidate source-shape compile smoke         PASS
candidate-native OpenSubdiv build            NOT EXECUTED
candidate-native openNURBS build             NOT EXECUTED
direct Emscripten OpenSubdiv build           NOT EXECUTED
direct Emscripten openNURBS build            NOT EXECUTED
```

**Q0 HARNESS = READY FOR REAL EXECUTION.**

No hard gate requiring actual candidate compilation is promoted to PASS by these harness-only tests.
