# BiomechE-CAD — P0 Authoring Acceptance Integration Addendum

**Status:** CANONICAL ADDENDUM v1  
**Date:** 2026-08-15  
**Parent document:** `functional_acceptance_suite.md`  
**Execution note:** executable GitHub CI is deferred under `TD-CI-001`; this addendum governs semantic acceptance independently of that debt.

---

## 0. Purpose

`functional_acceptance_suite.md` predates the P0 authoring formalization completed on 2026-08-15.

This addendum integrates the new architecture-independent acceptance families without destructively rewriting the older acceptance baseline and without duplicating the detailed requirements already owned by the new specifications.

Where the older suite's status/`NEXT` wording conflicts with this addendum, `SPEC_INDEX.md`, `TRACEABILITY_MATRIX.md` or `RESUME_HERE.md`, the newer canonical documents describe the current work state. Existing acceptance definitions remain valid unless explicitly superseded.

---

# 1. New acceptance families

The functional acceptance baseline is extended with:

```text
GAUTH-001..040
  owner: docs/spec/16_geometry_authoring_contract.md
  scope: geometry-authoring semantics, acquisition/landmark provenance,
         placement/dose, mirror, inspection, deterministic replay,
         clinical-vs-production geometry boundary

WFLOW-001..030
  owner: docs/spec/17_workflow_preset_macro.md
  scope: exact workflow/preset versioning, typed inputs, overrides,
         dependencies, review/confirmation, compatibility, bilateral/mirror,
         deterministic semantic expansion

NREG-001..030
  owner: docs/spec/18_numerical_qualification_registry.md
  scope: numerical authority classes, OPEN values, rule resolution,
         clinical/device/manufacturing/algorithm tolerance separation,
         uncertainty and default governance
```

The owning specs contain the normative semantic definition of each family. This addendum does not duplicate the full ID catalog.

---

# 2. Representative semantic scenarios

Canonical scenario catalog:

`docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md`

It currently defines 22 representative architecture-independent cases:

```text
AUTH-C01  arch dose + placement survives commit
AUTH-C02  heel concepts remain semantically distinct
AUTH-C03  rearfoot wedge mirror preserves anatomical direction
AUTH-C04  metatarsal placement reference modes remain non-equivalent
AUTH-C05  pressure-target offload retains quantitative source semantics
AUTH-C06  sculpt remains replayable rather than anonymous baked geometry
AUTH-C07  scan conform retains acquisition + registration provenance
AUTH-C08  requested dose vs constrained realized dose
AUTH-C09  unknown weight-bearing remains UNKNOWN
AUTH-C10  landmark source provenance survives review
AUTH-C11  section definition is reproducible
AUTH-C12  distance definition is explicit
AUTH-C13  thickness method is explicit
AUTH-C14  CAD vs measured-part deviation retains method/registration
AUTH-C15  workflow expansion freezes exact definition version/hash
AUTH-C16  workflow override retains original + final value provenance
AUTH-C17  suggestion is not user confirmation
AUTH-C18  unsafe child step blocks automatic macro mirror
AUTH-C19  missing manufacturing tolerance remains OPEN/not qualified
AUTH-C20  UI convenience default cannot satisfy qualification limit
AUTH-C21  evidence rule remains profile/context scoped
AUTH-C22  geometry replay epsilon remains distinct from part tolerance
```

Synthetic values inside these scenarios are test values only and SHALL NOT be interpreted as clinical/product defaults.

---

# 3. Acceptance layering

The existing acceptance-layer doctrine is extended as follows:

```text
L0  serialization/schema validity
L1  semantic identity/provenance invariants
L2  operation/workflow/numerical-rule invariants
L3  geometry/query behavior once an evaluator exists
L4  device/process/manufacturing qualification evidence
L5  clinical/outcome validation where applicable
```

`GAUTH`, `WFLOW` and `NREG` primarily occupy L1–L3.

A semantic requirement may therefore be frozen before a particular geometry engine exists. The later engine must satisfy it rather than redefine it.

---

# 4. Cross-family ownership

When more than one family applies, ownership remains split by domain rather than duplicated.

Examples:

```text
metatarsal pad
  CE-*      element clinical taxonomy / intended effect
  GAUTH-*   placement/dose/replay representation
  NREG-*    any governed default/range/threshold authority

pressure-guided offload
  OFF-*     redistribution semantics
  BINT-*    imported quantitative BiomechE result semantics
  PAQ-*     pressure device/protocol qualification
  GAUTH-*   design placement/operation provenance
  NREG-*    governed thresholds/defaults

manufactured thickness
  GAUTH-*   authoring/inspection definition
  MAN-*     manufacturing lifecycle/QC
  NREG-*    qualified acceptance limit ownership
```

No family should duplicate another family's formula or source of truth merely to make an acceptance case self-contained.

---

# 5. Architecture independence

The new acceptance families deliberately do not require:

```text
OpenSubdiv
openNURBS / ON_SubD
OCCT
Manifold
BRep/NURBS
specific mesh topology
specific language/runtime
specific renderer
```

A future architecture scorecard must derive from these semantic requirements and representative scenarios.

---

# 6. CI / executable-validation debt

`TD-CI-001` remains open and explicitly deferred by the project owner.

Therefore:

```text
semantic acceptance definition     ACTIVE / can be frozen
fixture/test specification         ACTIVE / can advance
GitHub executable result           NOT CURRENT QUALIFICATION AUTHORITY
architecture-independent docs      NOT BLOCKED
```

The historical validation report remains evidence only for its exact historical commit.

Do not:

- remove semantic tests because the current harness does not execute them;
- claim `main` is fully qualified from a green workflow badge;
- delay authoring-contract freeze solely because CI is currently unreliable.

When `TD-CI-001` is reopened, implementation should map the then-current semantic catalog into reliable executable tests.

---

# 7. Current acceptance-document precedence

For current authoring work use:

```text
1. docs/spec/16_geometry_authoring_contract.md
2. docs/spec/17_workflow_preset_macro.md
3. docs/spec/18_numerical_qualification_registry.md
4. docs/validation/P0_AUTHORING_ACCEPTANCE_CATALOG.md
5. this addendum
6. docs/validation/functional_acceptance_suite.md for pre-existing families
```

Coordinate, BiomechE, reporting, pressure qualification, corrective-element, material and manufacturing domain owners keep their existing authority.

---

# 8. Integration status

```text
new family allocation             DONE
representative P0 scenarios       DONE — 22
cross-document semantic audit     DONE — 0 blocking contradictions
CI execution dependency           explicitly deferred
functional acceptance integration DONE through this addendum
```

Remaining work is no longer feature discovery. It is document freeze/normalization and then architecture evaluation against the frozen contract.
