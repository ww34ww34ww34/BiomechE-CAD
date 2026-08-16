# BiomechE-CAD — Decision Register Addendum — P0 Closure / Visual / Q0

**Date:** 2026-08-16  
**Status:** CANONICAL ADDENDUM to `docs/DECISIONS.md`  
**Purpose:** record decisions taken after `D-CAD-029` without rewriting historical decision text.

---

## D-CAD-030 — P0 written documentation is closed; engineering hypotheses remain subordinate

**Status:** FROZEN  
**Date:** 2026-08-16

The final P0 cross-document audit reports **0 blocking semantic contradictions**.

Rules:

1. `DOC-00..DOC-14` are complete for the P0 product-semantic baseline;
2. `04_base_template.md` is an engineering candidate/qualification fixture, not product authority;
3. `05_parametric_orthosis_geometry.md` is a provisional engineering mathematical reference, not product authority;
4. no `41×17`, Catmull-Clark/OpenSubdiv, bump/wedge/scan-conform formula or sample value becomes a product requirement merely because it appears in `04/05`;
5. Project Schema v0.2 remains approved/not materialized;
6. `TD-CI-001` remains deferred/non-blocking.

---

## D-CAD-031 — The visual reference is versioned product infrastructure, but written specifications remain semantic authority

**Status:** FROZEN  
**Date:** 2026-08-16

Canonical source:

`docs/ux/mockups/v1/biomeche-cad-mockups-v1.html`

Rules:

1. M01..M14 are the canonical P0 visual/interaction source baseline;
2. visual screens map to written requirements through `docs/ux/mockups/v1/manifest.md`;
3. the browser audit executed all 14 screens with zero runtime exceptions;
4. M01..M13 use 1440×960 and M14 uses 1024×768 as reference viewports;
5. M07/M10 are representative dark references;
6. a mockup cannot introduce a clinical threshold, diagnosis, geometry algorithm or manufacturing authority not present in written specs;
7. if a mockup conflicts with a frozen written contract, the mockup is corrected;
8. the repository PNG binary archive is a rendered-reference convenience, not semantic authority or an architecture-entry gate.

Canonical browser audit:

`docs/ux/VISUAL_RENDER_BROWSER_AUDIT_2026-08-16.md`.

---

## D-CAD-032 — Accessibility/human-factors corrections are implementation obligations, not clinical-model changes

**Status:** FROZEN DESIGN-GOVERNANCE RULE  
**Date:** 2026-08-16

The visual browser review records three explicit corrective items:

```text
VIS-A11Y-01 quantitative graphics need accessible naming/description or explicit decorative semantics with equivalent accessible numeric representation
VIS-A11Y-02 interactive viewport tools use semantic controls with keyboard/name/role/state
VIS-A11Y-03 explicit visible focus treatment is frozen/tested for light and dark modes
```

These rules are supported by the current human-centred/usability/accessibility source set but do not claim formal conformance to ISO/IEC/FDA/WCAG requirements until a deployment-specific applicability/conformance plan says so.

---

## D-CAD-033 — Canonical bibliography remains single-source authority and current regulatory/standards/HFE references are normalized

**Status:** FROZEN GOVERNANCE RULE  
**Date:** 2026-08-16

`docs/BIBLIOGRAPHY.md` is the single bibliographic authority.

The 2026-08-16 normalization added stable IDs for current 3MF/AMF/AM data-package, MDR/MDCG/GDPR, risk/QMS and human-factors/accessibility references.

Rules:

1. research supplements remain intake/audit ledgers, not parallel bibliography authorities;
2. a standards abstract/scope supports only truthful high-level semantics unless the controlled full text has been reviewed;
3. regulatory guidance does not automatically classify BiomechE-CAD;
4. standards/guidance references do not automatically create certification/conformance claims;
5. no standard/guidance entry becomes a universal clinical threshold.

---

## D-CAD-034 — Geometry-engine Q0 uses exact candidate pins and one product-owned C++20 adapter boundary

**Status:** ACTIVE QUALIFICATION DECISION  
**Date:** 2026-08-16

Q0 candidate locks:

```text
OpenSubdiv
  tag       v3_7_0
  commit    9dab8a47bfbb1388ec8388fe61f5f916e6123f38

openNURBS
  ref       8.x snapshot
  commit    00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
```

Rules:

1. these revisions are qualification pins, not a final engine/version selection;
2. both candidates must pass through the same product-owned `biomeche_q0::Adapter` boundary;
3. candidate-native types may exist only inside candidate implementation units during Q0;
4. the common smoke executable is headless C++20 and is reused for native/server/WASM qualification;
5. OpenSubdiv Q0 links the minimal upstream CPU/core target and disables unrelated optional rendering/example stacks;
6. openNURBS Q0 uses its upstream public static target rather than copying an arbitrary subset of source files;
7. actual native and WASM PASS requires real pinned-source/toolchain execution and committed result evidence;
8. missing source/toolchain is `NOT EXECUTED`, never PASS and never candidate FAIL;
9. no winner is selected from Q0 scaffold/API/dependency evidence alone.

Canonical harness:

`qualification/geometry-engine/q0/`.

---

## D-CAD-035 — Q0 harness validation is distinct from candidate qualification

**Status:** FROZEN EVIDENCE RULE  
**Date:** 2026-08-16

The BiomechE-owned harness has separately passed syntax/common-interface/source-shape validation.

This evidence can support confidence that the harness is ready, but it cannot promote candidate build gates that require the actual OpenSubdiv/openNURBS source trees and Emscripten/native target toolchains.

Therefore current truth remains:

```text
Q0 HARNESS                         READY
OpenSubdiv native                  NOT EXECUTED
OpenSubdiv direct WASM             NOT EXECUTED
openNURBS native                   NOT EXECUTED
openNURBS direct WASM              NOT EXECUTED
FINAL ENGINE SELECTION             OPEN / NO WINNER
```

---

## Open decisions after this addendum

Still intentionally open:

- final geometry engine selection;
- native/server/WASM candidate qualification results;
- Q1..Q7 geometry/query/DFM/performance evidence;
- exact topology/geometry algorithms;
- numerical performance budgets;
- Project Schema v0.2 materialization;
- physical pressure/material/manufacturing qualification;
- formal regulatory classification/QMS/privacy/security deployment decisions;
- exact built-in PROM licensing/selection;
- repository storage of the 14 rendered PNG reference binaries.
