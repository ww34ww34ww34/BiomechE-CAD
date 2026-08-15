# BiomechE-CAD — Numerical / Tolerance / Qualification Registry

**Status:** CANONICAL DRAFT FOR FREEZE v0.1  
**Date:** 2026-08-15  
**Scope:** governance of numerical defaults, limits, tolerances, acceptance thresholds and measurement uncertainty across CAD, biomechanics, devices and manufacturing.  
**Architecture:** implementation independent.

---

## 0. Purpose

BiomechE-CAD contains many numbers that look superficially similar but have fundamentally different authority.

Examples:

```text
UI slider default
clinical study dose
algorithm parameter
registration residual threshold
minimum thickness
printer dimensional tolerance
pressure-device linearity limit
report display precision
```

This document prevents those values from becoming anonymous constants scattered through UI/code/specs.

The rule is simple:

> **Every product-significant number has an owner, scope, unit, authority class and lifecycle.**

---

# 1. Registry concept

## NREG-001 — First-class numerical rule

A governed numerical value/range SHALL be representable as:

```text
NumericalRule
  ruleId
  version
  status
  authorityClass

  displayName
  quantityType
  value / range / functionRef
  unit

  scope
  applicability
  ownerSpec

  evidenceRefs[]?
  qualificationMethodRef?
  sourceProfileRef?
  algorithmRef?

  uncertaintyPolicy?
  rationale
  supersedes?
  effectiveFrom?
```

## NREG-002 — Required status

Every rule has one of:

```text
OPEN
PROVISIONAL
QUALIFIED
FROZEN_CONVENTION
DEPRECATED
```

`OPEN` is a valid explicit state and SHALL NOT be silently replaced by a convenient implementation value.

---

# 2. Authority classes

## NREG-003 — Mathematical/convention constant

```text
CONVENTION
```

Examples:

```text
coordinate sign convention
unit conversion definition
normalized coordinate domain
```

These may be frozen globally when definition-based rather than empirically qualified.

## NREG-004 — UI convenience default

```text
UI_CONVENIENCE_DEFAULT
```

Examples:

```text
initial brush radius
initial zoom
panel slider position
```

These affect usability but SHALL NOT be presented as clinical/manufacturing recommendations.

## NREG-005 — Product authoring default

```text
PRODUCT_DEFAULT
```

A product default may initialize an authoring field only if:

- its scope is explicit;
- it is safe as a starting value;
- it is not labelled as optimal unless evidence/profile qualification supports that claim;
- operator override is possible where clinically appropriate.

## NREG-006 — Evidence-profile rule

```text
EVIDENCE_PROFILE_RULE
```

A value/range derived from literature or guidelines SHALL retain:

```text
population
indication/context
intervention/design definition
anatomical reference
protocol
outcome
source/evidence confidence
```

It must not leak into unrelated profiles.

## NREG-007 — Algorithm parameter / numerical tolerance

```text
ALGORITHM_PARAMETER
ALGORITHM_NUMERICAL_TOLERANCE
```

Examples:

```text
iteration limit
convergence threshold
surface-equivalence epsilon
sampling tolerance
```

These belong to an exact algorithm/version and are not clinical thresholds.

## NREG-008 — Device qualification acceptance rule

```text
DEVICE_QUALIFICATION_LIMIT
```

Owned by a named `PressureAcquisitionQualificationProfile` / intended use.

Examples:

```text
zero drift
linearity error
repeatability
hysteresis
COP error
timing/frame loss
```

No universal PMD threshold is defined here; the qualification methodology in `15_pressure_acquisition_qualification.md` owns how evidence is produced.

## NREG-009 — Manufacturing/process acceptance rule

```text
MANUFACTURING_ACCEPTANCE_LIMIT
```

Owned by a named manufacturing profile and, where relevant:

```text
machine/process
material/feedstock
orientation/build strategy
feature class/region
inspection method
measurement uncertainty
```

ISO/ASTM 52901 supports explicit part-definition/inspection/acceptance requirements and ISO/ASTM 52902 supports geometric capability assessment, but neither creates one universal orthosis tolerance.

## NREG-010 — Clinical/outcome interpretation threshold

```text
OUTCOME_INTERPRETATION_RULE
```

Owned by a named population/protocol/ROI/metric/evidence profile.

A threshold from diabetic-foot offloading cannot silently become a generic threshold for sport, plantar heel pain, flatfoot or metatarsalgia.

---

# 3. Scope hierarchy

## NREG-011 — Most-specific applicable rule wins only by explicit resolution

Possible scope levels include:

```text
GLOBAL_CONVENTION
PRODUCT
OPERATION_TYPE
TEMPLATE_FAMILY
INDICATION_PROFILE
ACQUISITION_PROTOCOL
DEVICE_MODEL
DEVICE_UNIT
MATERIAL_DEFINITION
MANUFACTURING_PROFILE
MACHINE
FEATURE_CLASS
PROJECT
DESIGN_REVISION
```

The runtime must resolve a rule by a deterministic named policy, not by accidental configuration load order.

## NREG-012 — No silent fallback across authority classes

Example:

```text
missing MANUFACTURING_ACCEPTANCE_LIMIT
```

must not fall back to:

```text
UI_CONVENIENCE_DEFAULT
```

simply because both values are expressed in millimetres.

---

# 4. Evidence examples — what they mean and what they do not mean

## NREG-013 — Metatarsal-pad placement evidence

`REF-CAD-013` reports consistent peak-pressure reduction in its studied diabetic-neuropathy population when the pad was approximately 6.1–10.6 mm proximal to the metatarsal-head line, with pressure potentially increasing when positioned too distally.

Registry interpretation:

```text
authorityClass = EVIDENCE_PROFILE_RULE
population/context = exact study population
reference = metatarsal-head line
dose dimension = signed placement distance mm
status = evidence available, NOT universal product default
```

`REF-CAD-014` uses a different population/reference formulation, reinforcing that placement semantics and normalization definition must be preserved.

## NREG-014 — Heel/skive dose evidence

Heel/skive studies may support profile-specific dose-response knowledge, but a studied 2/4/6 mm modification sequence does not establish a universal `HEEL_SKIVE_DEFAULT_MM`.

Geometry Authoring stores the dose; this registry stores any approved default/range and its scope.

## NREG-015 — Arch support/stiffness evidence

Arch height/shape and mechanical stiffness/hardness are independent numerical dimensions. Literature showing effects for tested levels supports explicit dose metadata but not one cross-population optimum.

## NREG-016 — Pressure protocol counts

A study-specific result such as a recommended number of steps for a particular in-shoe diabetic-foot protocol (`REF-CAD-108`) may become an `EVIDENCE_PROFILE_RULE` for that compatible protocol; it must not become a universal hidden step-count constant.

---

# 5. Geometry numerical governance

## NREG-017 — Requested vs realized geometry

Where safety/DFM constraints alter requested geometry, record both:

```text
requested value
evaluated/realized value
constraint/rule responsible
```

## NREG-018 — Geometry equivalence tolerance

Deterministic replay may require an algorithm/profile-owned numerical equivalence tolerance.

This tolerance SHALL identify:

```text
representation
metric
unit
sampling method if any
algorithm/runtime scope
```

It is not automatically the manufacturing dimensional tolerance.

## NREG-019 — Registration acceptance

Registration residual thresholds SHALL be owned by an acquisition/registration profile with method and intended use.

Landmark uncertainty and scanner uncertainty may inform that profile but remain separate quantities.

## NREG-020 — Inspection precision vs acceptance tolerance

Display precision, computational precision and acceptance tolerance are separate.

Example:

```text
a thickness may display as 3.2 mm
while calculation uses full precision
and ManufacturingProfile acceptance uses an independent limit/rule
```

---

# 6. Manufacturing tolerance doctrine

## NREG-021 — No universal `CAD_TOLERANCE`

BiomechE-CAD SHALL NOT define one global dimensional tolerance for all manufactured orthoses.

A manufacturing tolerance must resolve at least:

```text
ManufacturingProfile
process/machine
material/feedstock
feature class or measurement location
nominal dimension/geometry definition
inspection method
acceptance rule
uncertainty policy where relevant
```

## NREG-022 — CAD nominal != achieved part

Persist separately:

```text
CAD nominal geometry
manufacturing artifact
measured physical-part geometry
geometric deviation result
accept/reject decision
```

`REF-CAD-106` supports the principle that realized orthosis geometry should not be assumed identical to design intent.

## NREG-023 — AM system capability evidence is contextual

ISO/ASTM 52902 test artefacts can characterize/calibrate AM system geometric performance, but application-specific grades/requirements remain profile-owned.

ISO 17295 coordinate/orientation semantics should be retained as manufacturing provenance where applicable.

---

# 7. Measurement uncertainty and guard bands

## NREG-024 — Measurement result and limit are distinct

Where a decision is sensitive to measurement uncertainty, the rule SHALL be able to preserve:

```text
measured value
uncertainty or method-quality metadata
acceptance limit
decision rule / guard-band policy
```

The project does not invent a universal guard-band policy here.

## NREG-025 — Unknown uncertainty is explicit

If uncertainty is required by a qualified profile but unavailable, the state is not silently treated as zero uncertainty.

Possible result:

```text
VALID_WITH_WARNINGS
UNAVAILABLE
NOT_QUALIFIED
```

according to the owning profile.

---

# 8. Registry resolution in presets/macros

## NREG-026 — Macro defaults resolve to registry IDs

A workflow/preset should reference a `ruleId + version` when a parameter default is governed.

This allows historical answers to questions such as:

```text
why was this default 4 mm?
was it a UI convenience, clinic profile or evidence rule?
which version was used?
```

## NREG-027 — Operator override remains project data

Overriding a registry-provided default does not mutate the registry. The project stores the overridden final value and provenance.

---

# 9. Initial registry backlog

The following classes exist conceptually but require actual values/qualification later:

| Rule area | Current state | Owner |
|---|---|---|
| scanner/registration acceptance residuals | OPEN | acquisition/registration profile |
| landmark-review confidence thresholds | OPEN | authoring/acquisition profile |
| geometry replay equivalence epsilon | OPEN | future geometry evaluator profile |
| sculpt radius/strength UI defaults | OPEN / usability-owned | product UX |
| template sizing defaults | profile/template-owned | template definitions |
| arch dose defaults | profile/context-owned | indication/workflow profiles |
| heel/skive/relief defaults | profile/context-owned | indication/workflow profiles |
| met-pad placement defaults | profile/reference-owned | indication/workflow profiles |
| minimum thickness | OPEN until process profile | ManufacturingProfile |
| dimensional part tolerance | OPEN until process qualification | ManufacturingProfile |
| pressure-device bench limits | OPEN per intended use | PressureAcquisitionQualificationProfile |
| static-load protocol limits | OPEN pending first qualification | acquisition profile |
| report display decimal policy | OPEN / presentation-owned | reporting profile |

`OPEN` here is deliberate product truth, not missing documentation to be filled with guesses.

---

# 10. Acceptance namespace

New acceptance family:

```text
NREG-001..030
```

Suggested allocation:

```text
NREG-001 every governed number has authority class
NREG-002 OPEN survives serialization/resolution
NREG-003 UI default cannot satisfy clinical/process limit
NREG-004 evidence rule retains population/context/reference
NREG-005 algorithm tolerance bound to algorithm version
NREG-006 device limit bound to qualification profile
NREG-007 manufacturing limit bound to manufacturing profile
NREG-008 outcome threshold bound to protocol/ROI/profile
NREG-009 rule resolution deterministic
NREG-010 cross-class silent fallback prohibited
NREG-011 met-pad evidence not universal default
NREG-012 requested vs realized geometry preserved
NREG-013 replay epsilon != manufacturing tolerance
NREG-014 registration limit method/profile explicit
NREG-015 display precision != acceptance tolerance
NREG-016 no global CAD manufacturing tolerance
NREG-017 measured geometry distinct from nominal geometry
NREG-018 AM capability evidence does not auto-create part acceptance
NREG-019 uncertainty not silently zero
NREG-020 macro default resolves exact registry rule/version
NREG-021 operator override leaves registry immutable
NREG-022..030 reserved
```

---

# 11. Freeze criteria

Move to `FROZEN v1` when:

1. all numerical authority classes are accepted;
2. the `OPEN` rule is explicitly preserved across specs;
3. geometry, device, manufacturing and clinical tolerances remain distinct;
4. workflow/preset defaults can reference exact registry rules;
5. representative P0 numbers can be catalogued without inventing universal thresholds;
6. the registry model is sufficient to drive later machine-readable implementation.
