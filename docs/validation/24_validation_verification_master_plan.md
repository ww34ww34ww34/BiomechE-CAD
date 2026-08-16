# BiomechE-CAD — Validation & Verification Master Plan

**Version:** v1  
**Status:** **CANONICAL V&V MASTER PLAN v1**  
**Date:** 2026-08-16  
**Product authority:** `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` + frozen domain contracts.  
**Numerical authority:** `docs/spec/18_numerical_qualification_registry.md`.  
**CI status:** GitHub CI debt `TD-CI-001` remains deliberately deferred and is **not** a substitute for this plan.

---

## 0. Purpose

Define one validation/verification framework for BiomechE-CAD that connects:

```text
REQUIREMENT
  ↓
SEMANTIC ACCEPTANCE
  ↓
TEST / PROTOCOL
  ↓
FIXTURE / PHYSICAL EVIDENCE
  ↓
RESULT
  ↓
QUALIFICATION / RELEASE EVIDENCE
```

A green build, successful file export, attractive screenshot or single numerical benchmark cannot substitute for the required evidence layer.

---

# 1. Verification vs validation vocabulary

For this project:

### Verification

Evidence that an implemented artifact/function satisfies its specified product/engineering requirement.

Examples:

```text
serialization round-trip
semantic mirror correctness
measurement formula implementation
geometry replay equivalence
format/unit transform correctness
blocking-QC state machine
```

### Validation

Evidence that the selected specification/implemented behavior is appropriate for its declared intended context/use, including as applicable scientific evidence, usability/human review, device qualification, manufacturing qualification and measured outcome evidence.

This project uses `validation` in some historical file names for software acceptance. The master plan preserves those names but requires the evidence type to be explicit.

---

# 2. Evidence layers

Canonical V&V layers:

```text
V0  DOCUMENT / TRACEABILITY REVIEW
V1  DATA MODEL / SERIALIZATION
V2  PURE SEMANTIC / UNIT VERIFICATION
V3  GEOMETRY / NUMERICAL VERIFICATION
V4  CROSS-DOMAIN INTEGRATION
V5  INTERACTION / WORKFLOW / VISUAL ACCEPTANCE
V6  PERFORMANCE / RESOURCE QUALIFICATION
V7  DEVICE / ACQUISITION QUALIFICATION
V8  MANUFACTURING / PHYSICAL-PART QUALIFICATION
V9  SCIENTIFIC / OUTCOME / INTENDED-USE VALIDATION
```

Not every requirement needs every layer.

---

# 3. Requirement-to-evidence matrix fields

Each P0 requirement family should map at least:

```text
requirementId
requirementAuthority
priority / release scope
risk/criticality class when available
acceptanceId(s)
evidenceLayer(s)
testType
fixture/protocolId
expected result / oracle
tolerance/threshold authority ref
execution environment
result artifact
qualification status
known limitations/open items
```

`TRACEABILITY_MATRIX.md` remains the canonical high-level map; this plan defines the test/evidence semantics behind it.

---

# 4. Acceptance namespace registry

Current namespaces include or now require integration of:

```text
SCHEMA-001..030       project schema
OFF-001..009          offloading
CE-001..010           corrective elements
ARCH-001..014         arch
HEEL-001..015         heel
PROF-001..014         indication/use-case profiles
PROM-001..020         PROM/comfort/adherence
MAT-001..018          material/mechanical semantics
AQ-001..010           analysis/QC/DFM
MAN-001..018          manufacturing
BINT-001..018         BiomechE integration
RPT-001..018          reporting/traceability
PAQ-001..020          pressure acquisition qualification
GAUTH-001..040        frozen geometry authoring
WFLOW-001..030        frozen workflow/preset/macro
NREG-001..030         frozen numerical governance
AUTH-C01..C22         frozen representative authoring scenarios
INPUT-001..020        input/scan/reference data
UX-001..022           product workflow/interaction
XCHG-001..018         interchange/handoff
PERF-001..016         performance doctrine/qualification
XACC-*                 cross-domain functional scenarios
HG-01..HG-15          geometry-engine architecture hard gates
```

Exact ranges are updated when new requirements are formally added; gaps or superseded IDs are never silently reused with a different meaning.

---

# 5. Test-type taxonomy

```text
DOC_REVIEW
STATIC_SCHEMA
UNIT
PROPERTY_BASED
SERIALIZATION_ROUNDTRIP
GOLDEN_FIXTURE
NUMERICAL_REFERENCE
GEOMETRY_EQUIVALENCE
INTEGRATION
STATE_MACHINE
UI_INTERACTION
VISUAL_REFERENCE
PERFORMANCE_BENCHMARK
HARDWARE_BENCH
MANUFACTURING_COUPON
PHYSICAL_PART_INSPECTION
HUMAN_REVIEW
CLINICAL_OR_OUTCOME_STUDY
MANUAL_PROTOCOL
```

A requirement can use multiple test types.

---

# 6. Result state vocabulary

Canonical result states:

```text
NOT_RUN
PASS
FAIL
INDETERMINATE
BLOCKED_BY_MISSING_EVIDENCE
NOT_APPLICABLE
NOT_COMPARABLE
MEASURED_NOT_QUALIFIED
```

Rules:

```text
missing evidence != PASS
not comparable != zero difference
measured != qualified
not applicable requires rationale
```

---

# 7. Qualification lifecycle

Where a test result feeds a qualification profile, use the lifecycle in NREG or the domain-specific qualified state:

```text
OPEN
PROVISIONAL
QUALIFIED
FROZEN_CONVENTION
DEPRECATED
```

A test may PASS its implementation oracle while the broader profile remains PROVISIONAL because external/device/physical evidence is missing.

---

# 8. Test oracle hierarchy

Preferred oracle source order:

1. frozen product semantic requirement;
2. mathematically defined expected result;
3. independently computed reference implementation/dataset;
4. measured physical reference with uncertainty;
5. approved golden artifact/reference image;
6. expert/manual protocol where automation is not yet justified.

Competitor output is behavioral evidence but not scientific or numerical truth unless independently qualified.

---

# 9. Numerical tolerance policy

Every numerical comparison declares:

```text
toleranceId
authorityClass
value/units or method
scope
algorithm/version
qualification state
```

Never borrow:

```text
manufacturing tolerance
for algorithm equivalence
```

or:

```text
clinical threshold
for device/geometry numerical acceptance
```

If no justified tolerance exists, result remains `MEASURED_NOT_QUALIFIED` or the tolerance is explicitly provisional.

---

# 10. Semantic serialization verification

Required for persistent domain state:

```text
create
serialize
reload
resolve exact referenced definitions
compare normalized semantic state
replay where applicable
```

Must cover version/hash/snapshot identity and distinguish source evidence from derived caches.

Byte-identical JSON is not required unless byte identity is the declared oracle.

---

# 11. Golden geometry / authoring fixtures

Geometry fixtures should store:

```text
fixtureId/version
semantic source state
source hashes
operation sequence
algorithm versions
expected inspectable metrics
numerical tolerance refs
golden visualization where useful
manufacturing geometry summary where relevant
```

Golden geometry must be regenerated only through an explicit approval/change process; silently updating expected geometry to match a regression invalidates the test.

---

# 12. Mirror verification

Mirror tests require both:

```text
geometric equivalence
semantic/anatomical equivalence
```

A reflected mesh alone is insufficient.

Verify:

```text
side
medial/lateral semantics
posting direction/reference
landmark/ROI mapping
corrective element targets
material region mapping
workflow/preset mirror policy
```

---

# 13. Requested vs realized verification

For dose-bearing geometry operations:

```text
requested semantic dose
  ↓ engine realization
measured realized CAD dose
```

Both must remain accessible. Tests must not overwrite requested parameters with measured realization.

Where constraints change the result, constraint source and realized delta are part of the evidence.

---

# 14. Acquisition / scan verification

`INPUT-*` and `PAQ-*` tests cover different things:

```text
INPUT-*   source identity / processing / frame / landmark / registration provenance
PAQ-*     pressure-device/protocol technical qualification
```

For 3D scan inputs, test original-vs-derived preservation, units/side/frame resolution, processing provenance, landmark review and registration reproducibility.

A mesh-quality pass is not a scanner metrology qualification.

---

# 15. BiomechE integration verification

`BINT-*` verifies exact quantitative-result semantics, including:

```text
result ID/version
source dataset/protocol
metric definition
ROI/version
quality/provenance
comparison compatibility
reanalysis append-only behavior
```

CAD never recomputes a different hidden definition under the same BiomechE metric identifier.

---

# 16. Interaction / workflow verification

`UX-*` tests combine state-machine and visual interaction evidence.

Required representative flows:

```text
import unresolved source
registration + landmark confirmation
base/template application
parametric edit preview/apply/cancel
corrective-element drag + numeric coherence
sculpt replay
material assignment
inspection definition/result
BiomechE comparison
commit DesignRevision
manufacturing release
physical-part QC/follow-up
```

Visual-reference conformity is necessary for layout/state communication but does not replace state/semantic assertions.

---

# 17. Visual regression / mockup acceptance

The canonical visual-reference package is versioned.

Visual tests may assert:

```text
required controls/state visible
side/profile/warning context visible
layout hierarchy
empty/error/warning states
responsive/compact behavior
major component placement
```

Pixel-perfect tolerance, if used, is an engineering visual-regression parameter and should allow explicitly approved rendering/platform variance.

Visual acceptance never creates clinical defaults.

---

# 18. Performance qualification

`PERF-*` follows `23_realtime_performance_contract.md`.

Performance qualification requires:

```text
correctness PASS first
representative fixture
exact environment/build
min/p50/p95/p99/max/mean
memory/resource evidence
approved EngineeringPerformanceProfile budget for PASS/FAIL
```

Until a budget exists:

```text
MEASURED_NOT_QUALIFIED
```

---

# 19. Geometry-engine qualification

The engine shoot-out remains governed by:

```text
GEOMETRY_ENGINE_EVALUATION_SCORECARD_2026-08-15.md
GEOMETRY_ENGINE_POC_QUALIFICATION_PLAN_2026-08-15.md
```

Sequence:

```text
HG hard gates
  ↓
Q0..Q7 PoCs/benchmarks
  ↓
evidence grades
  ↓
weighted score
  ↓
architecture decision
```

No winner may be selected while selection-critical UNKNOWN hard gates remain.

---

# 20. Manufacturing qualification

`MAN-*` verification covers lifecycle/state/provenance. Physical manufacturing qualification additionally may require:

```text
process profile qualification
material/lot evidence
reference coupons/test artifacts
part dimensional inspection
property measurement
post-process verification
blocking QC execution
measurement uncertainty
```

A file export or watertight mesh does not qualify a physical orthosis.

---

# 21. Physical-part inspection

For physical verification preserve:

```text
physicalPartId
source design/manufacturing artifact/run
measurement method
instrument/calibration
alignment method/version for 3D comparisons
measured value/deviation map
uncertainty where available
acceptance requirement/ref
operator/timestamp
```

Measured manufactured geometry never mutates CAD nominal geometry.

---

# 22. Device / pressure bench qualification

`15_pressure_acquisition_qualification.md` and the FM12050/PFM2120 bench protocol govern pressure-hardware evidence.

Nominal vendor specifications are intake evidence, not qualification PASS.

Physical-unit qualification is independent of documentation freeze and geometry-engine architecture selection.

---

# 23. Scientific evidence validation

Clinical/product interpretation claims must map to canonical bibliography sources with:

```text
population
intervention/context
outcome
protocol
source locator
transfer limits
```

A statistically significant published result does not automatically become a global product threshold/preset.

Evidence updates may justify a new version of a profile/rule without rewriting historical projects.

---

# 24. Usability / human validation

For high-impact workflows, future validation should include representative users/tasks and record:

```text
user role/experience
scenario/task
critical information required
errors/near misses
warnings understood
time/effort where relevant
workarounds
subjective feedback
observed confusion
```

Human validation findings may change interaction design while preserving frozen clinical/domain semantics unless a formal product decision updates them.

---

# 25. Release evidence bundle

A future release candidate should be able to produce an evidence manifest containing:

```text
release commit/build
requirements baseline versions
executed test/protocol IDs
result artifacts/hashes
open/deferred tests
known limitations
qualified profiles
performance profile results
hardware/manufacturing qualification refs where in scope
visual baseline version
risk/approval refs when available
```

A release evidence bundle is version-specific and cannot be inherited automatically by a materially changed build.

---

# 26. Change impact / requalification

Every substantive change should classify impact on:

```text
semantic contract
serialization/schema
algorithm/numerics
visual/interaction
performance
input/import/export
manufacturing
physical qualification
scientific/profile interpretation
```

Then select the minimal complete affected test set.

Examples:

- UI spacing-only change → visual/accessibility subset;
- algorithm change → geometry/numerical + performance + affected integration;
- material qualification rule change → MAT/MAN + affected reports/profile;
- geometry engine update → relevant HG/Q phases + geometry/performance/interchange regression.

---

# 27. Defect severity and evidence handling

Suggested defect evidence classes:

```text
BLOCKING_SEMANTIC
BLOCKING_DATA_INTEGRITY
BLOCKING_MANUFACTURING
MAJOR_FUNCTIONAL
NUMERICAL_REGRESSION
PERFORMANCE_REGRESSION
VISUAL_INTERACTION
DOCUMENTATION_TRACEABILITY
```

Exact release-severity policy belongs to future release governance, but semantic/data-integrity/manufacturing blockers cannot be hidden by aggregate test counts.

---

# 28. Manual vs automated evidence

Automation is preferred for deterministic repeatable checks, but a manual/HIL/physical protocol is acceptable where it is the correct evidence source.

Manual evidence must still be reproducible:

```text
protocol version
operator
fixture/device/part ID
environment
steps
expected result
actual result
attachments/data
reviewer
```

No manual PASS without a controlled protocol.

---

# 29. CI independence

CI is an execution convenience, not requirement authority.

`TD-CI-001` means current GitHub Actions reliability is deferred. Therefore:

```text
missing green CI != permission to weaken requirement
current green CI != full qualification proof
local/manual controlled execution may provide valid evidence
```

When CI debt is repaired, pipelines should execute this V&V plan rather than define it.

---

# 30. V&V acceptance tests

```text
VV-001 every P0 requirement maps to acceptance/evidence or explicit deferral
VV-002 every numerical oracle resolves a correct authority/tolerance class
VV-003 missing evidence cannot become PASS
VV-004 golden reference update requires explicit review/version change
VV-005 semantic serialization verifies exact historical definition resolution
VV-006 geometry tests retain requested and realized values separately
VV-007 mirror tests include semantic side mapping, not geometry only
VV-008 scan input quality test is not mislabelled device metrology qualification
VV-009 UI visual PASS cannot replace state/semantic assertions
VV-010 performance PASS requires approved performance profile budget
VV-011 format conformance cannot replace manufacturing acceptance
VV-012 physical-part QC links exact physical/run/artifact/design identities
VV-013 scientific evidence claim records population/context/transfer limits
VV-014 manual/HIL PASS references controlled protocol/version/evidence
VV-015 release evidence bundle lists open/deferred/not-run gates
VV-016 change-impact analysis selects affected requalification families
VV-017 CI state does not change semantic requirement authority
VV-018 historical evidence remains linked to exact software/spec/profile versions
```

---

# 31. Current execution status

At documentation closure time:

```text
semantic authoring acceptance specification     FROZEN
multiple schema/acceptance fixtures              EXISTING
geometry-engine PoC plan                         DEFINED / EXECUTION DEFERRED
pressure physical bench qualification            PENDING PHYSICAL EVIDENCE
manufacturing physical qualification             PENDING PROCESS/PART EVIDENCE
performance numeric budgets                      OPEN
visual reference package                         PENDING VIS PHASE
CI repair                                         DEFERRED TD-CI-001
```

This is expected and does not block completion of the written product specification package.

---

# 32. Product conclusion

BiomechE-CAD may call a capability **verified/qualified** only when it can answer:

```text
Which requirement?
Which exact version?
Which acceptance test/protocol?
Which fixture/device/physical part?
Which oracle and tolerance authority?
What result artifact/hash?
On which build/environment?
What remains open or non-comparable?
```

This master plan is the bridge from documentation to executable evidence without allowing tooling/CI/library choices to redefine product truth.
