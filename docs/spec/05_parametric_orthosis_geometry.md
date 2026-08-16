# BiomechE-CAD — Parametric Orthosis Geometry Operators

**Status:** **ENGINEERING MATHEMATICAL REFERENCE — INTENTIONALLY PROVISIONAL / NOT PRODUCT AUTHORITY**  
**Version:** v0 reference model  
**Date:** 2026-08-16 status clarification; original proposal 2026-08-14  
**Authority:** semantic operator behavior is governed by `16_geometry_authoring_contract.md`; reusable parameter/preset semantics by `17_workflow_preset_macro.md`; numerical/default/tolerance ownership by `18_numerical_qualification_registry.md`.

> **NON-AUTHORITATIVE ALGORITHM HYPOTHESES.** The formulas below are candidate deterministic implementations and qualification fixtures. They are not validated clinical laws, not proof of EasyCAD2 algorithmic identity, and do not select a geometry engine. Exact bump functions, displacement directions, smoothing/projection methods, supported envelopes and tolerances may change after PoC/qualification without reopening frozen product semantics.

> EasyCAD2 documents parameter names and observable behavior, but does not disclose its internal formulas. The purpose of this file is to preserve candidate implementations that can be tested against the frozen semantic contract.

---

## 1. Intrinsic domain — candidate representation

A future implementation may expose stable intrinsic/surface coordinates. The historical candidate used:

```text
s(v) ∈ [0,1]    heel -> distal/toe
q(v) ∈ [-1,1]  lateral -> medial
```

Local position is `P(v)` and a chosen displacement direction is `d(v)`.

Candidate direction classes:

```text
GLOBAL_Z
LIMIT_NORMAL
CAGE_NORMAL
ANATOMICAL_VERTICAL
explicit local frame axis
```

**Frozen requirement:** direction/reference choice must be explicit, versioned and replayable. No particular direction above is the product default until qualified.

---

## 2. Common smooth functions — candidate primitives

### 2.1 Clamp

```text
sat(x) = min(1, max(0, x))
```

### 2.2 Smoothstep

```text
S(x) = u²(3 - 2u),  u = sat(x)
```

### 2.3 Compact bump on interval `[a,b]` with center `c`

For `a < c < b`:

```text
L(s) = S((s-a)/(c-a))
R(s) = S((b-s)/(b-c))
B(s;a,c,b) = L(s) * R(s)
```

### 2.4 Shape exponent

```text
B_p = B^p, p > 0
```

### 2.5 Compact transverse profile

```text
Phi(x,p) = (1 - x²)^p     if |x| < 1
           0              otherwise
```

These functions are convenient deterministic PoC bases only. The product contract does not require these exact functions.

---

# 3. Medial arch operator — candidate realization

EasyCAD2 exposes controls such as height, roundness, depth, curvature and start/center/end percentages according to the manual/validation baseline. BiomechE-CAD's frozen semantics require explicit requested dose, typed placement/reference and inspectable realized dose.

Candidate mapping:

```text
H          = requested arch height [mm]
a,c,b      = start/center/end mapped to candidate intrinsic s
q_center   = medial transverse centerline
sigma      = transverse width/depth control
p_long     = longitudinal curvature exponent
p_trans    = transverse curvature exponent
roundness  = peak-shape/blend parameter
```

Candidate displacement:

```text
wL(v) = B(s(v); a,c,b)^p_long
x(v)  = (q(v) - q_center(s(v))) / sigma
wT(v) = Phi(x(v), p_trans)
w(v)  = wL(v) * wT(v) * MedialMask(v)
ΔP(v) = d(v) * H * w(v)
```

A candidate roundness realization may blend the field with a local smooth average. Exact mapping remains qualification-dependent.

Acceptance must be measurement-based and use the frozen requested-vs-realized semantics; algorithm epsilon is not a clinical/manufacturing tolerance.

---

# 4. Lateral arch operator

A lateral arch may share implementation primitives with medial arch while remaining a distinct semantic operator family. Candidate field:

```text
w(v) = B(s;a,c,b)^p_long
     * Phi((q-q_lateral_center(s))/sigma, p_trans)
     * LateralMask(v)

ΔP(v) = d(v) * H * w(v)
```

Shared math does not imply shared clinical defaults or supported envelopes.

---

# 5. Rearfoot / forefoot wedge

The frozen product contract treats wedge/posting dose as an explicit angular prescription where appropriate. A candidate geometric realization is:

```text
θ = requested wedge angle [deg]
A = typed anatomical/reference pivot axis/line
d⊥(v) = signed transverse distance from A
h(v) = tan(θ) * d⊥(v)
ΔP(v) = z_dir * h(v) * regionMask(v)
```

The pivot/reference must be serialized and inspectable. Example fixtures such as 2°/4°/6° remain **engineering test samples**, not clinical defaults or UI recommendations.

---

# 6. Heel wrap / rearfoot operator

Heel cup/wrap/camber is semantically first-class, but exact fields are not frozen. Historical candidate constructs include an elliptical heel support field, perimeter emphasis and independent camber field:

```text
r(v) = sqrt(((s-sh)/as)^2 + ((q-qh)/aq)^2)
Wh(v) = candidate compact falloff
Wwrap(v) = Wh(v) * boundaryWeight(v)^p
ΔPwrap(v) = d_wrap(v) * Hwrap * Wwrap(v)
```

and a separate longitudinal camber field. Keeping requested wrap/camber semantics separate is useful; exact equations/directions require qualification.

---

# 7. Global thickness and flatten

Thickness belongs to production/material realization rather than being silently baked into the clinical/contact surface.

Candidate field:

```text
t(v) = t_global + Σ localThicknessModifiers(v)
```

`FlattenOperation` remains a named semantic operation only when its target/reference and preservation policy are explicit. The exact construction must be qualified with visual/geometric fixtures and manufacturing constraints.

---

# 8. Corrective element field

A candidate corrective element may be evaluated as a signed local contribution in a stable local coordinate system:

```text
E(localCoordinates; params) -> signed height/support contribution
```

Candidate compact ellipsoidal basis:

```text
rho² = (u/a)^2 + (v/b)^2
E = H * (1-rho²)^p   if rho < 1
    0                 otherwise
```

This is only one possible implementation. `06_corrective_elements.md` owns clinical semantic identity, typed placement, requested/realized dose, intended effect and evidence context.

Historical notions such as `ADD_FROM_TOP` / `PLACE_FROM_BASE` are candidate realization policies and must be made explicit/versioned if used; they do not override `GAUTH` production-boundary semantics.

---

# 9. Sculpt brush

Candidate local field:

```text
x = distance(P(v), C) / R
w = Phi(x,p)
ΔP(v) = d(v) * A * w
```

The frozen requirement is that sculpt remains replayable with stable addressing/reference, explicit radius/strength/direction and versioned algorithm semantics. Euclidean vs geodesic distance is a qualification choice.

---

# 10. Smooth

Smoothing may never silently destroy prescribed geometry or protected boundaries.

Historical candidate cage-space form:

```text
P'_i = P_i + λ * mask_i * (weightedNeighborAverage(P_i) - P_i)
```

Possible Taubin-like/constrained alternatives remain implementation choices. A smoothing operation must preserve its method/version/iterations/strength and protected/fixed semantics; SubD evaluation itself is not equivalent to a user `Smooth` edit.

---

# 11. Global scan conform

Frozen semantics require exact source/registration/ROI/projection/residual/version provenance. A candidate realization is:

1. query target `Q(v)` by an explicit projection method;
2. compute delta `δ(v)`;
3. apply strength/falloff and any explicit bounded displacement policy;
4. report pre/post residual and protected-region movement.

Candidate projection classes:

```text
CLOSEST_POINT
ANATOMICAL_VERTICAL
SURFACE_NORMAL_RAY
```

No method is the product default until qualification. Any maximum displacement is an explicit qualified numerical parameter, not a hidden safety rule.

---

# 12. Height constraints / control fixes

Named constraints may represent target arch heights, heel/forefoot bounds or project-height controls, but each must preserve:

```text
ConstraintRegion
TargetMetric
TargetValue + units
AdjustmentPolicy
NumericalAuthorityRef
```

Candidate policies such as shift/scale/clamp/blend are implementation strategies. They require deterministic replay and requested-vs-realized inspection.

---

# 13. Minimum thickness auto-fix

Minimum thickness is a manufacturing-profile concern. A candidate correction algorithm may compute local violations and prefer modifying lower/production geometry while preserving the clinical/contact surface where possible.

Frozen rules:

```text
manufacturing minimum != global CAD constant
manufacturing tolerance != algorithm epsilon
correction must be previewable/auditable
requested clinical surface change must never be silent
```

EasyCAD2's historical warning value is compatibility evidence only, not a BiomechE-CAD universal rule.

---

# 14. Operator invariants inherited from frozen contracts

Any candidate implementation must satisfy at least:

```text
finite coordinates / explicit invalid state
stable product semantic IDs/references
deterministic version-bound replay
typed units
side-aware mirror semantics
requested vs realized distinction
bounded/qualified supported envelope
no silent topology/provenance loss
```

Representation-specific conditions such as control-face inversion are architecture qualification checks, not universal product concepts.

---

# 15. Parameter-limit policy

Three different concepts must remain separate:

```text
HARD_NUMERIC_LIMITS              implementation safety
PRODUCT_UI_LIMITS                product/UX profile
VALIDATED_CLINICAL_OR_MANUFACTURING_LIMITS
```

Every value requires an explicit NREG authority class/status. No limit is frozen merely because it appears in this engineering reference.

---

# 16. Candidate golden fixtures

Useful future qualification fixtures include:

```text
neutral template
medial/lateral arch variants
rear/forefoot wedge sample angles
heel wrap/camber variants
metatarsal dome/bar placement/scaling
sculpt raise/lower
scan conform ROI
minimum-thickness violation/correction
right↔left semantic mirror
```

Fixture parameter values are test samples unless separately qualified. Each fixture should retain input hash, semantic operation record, algorithm version, expected metrics/tolerance authority, reference images and production/inspection result where relevant.

---

# 17. Open engineering questions

Still intentionally open until architecture/algorithm qualification:

- mapping of vendor-like roundness/depth/curvature controls to internal operators;
- exact heel wrap/camber construction;
- displacement direction by operator;
- local-element realization relative to clinical vs production surfaces;
- baseline vs current normals/reference fields;
- scan-conform projection strategy and tangential preservation;
- smoothing family;
- production closure/body strategy;
- robust spatial-query implementation;
- candidate representation/topology.

These are not reasons to alter the frozen semantic authoring contract.

---

# 18. Final disposition

```text
named operator semantics           product authority: spec/16 + related frozen specs
exact formulas in this file        engineering hypotheses
specific smooth/bump basis         engineering hypotheses
projection/smoothing algorithms    engineering hypotheses
sample fixture values              qualification samples
algorithm tolerances               OPEN until NREG-qualified
clinical defaults/thresholds       NONE frozen here
manufacturing limits               NONE frozen here
geometry engine                    NOT selected by this file
```

This file remains useful for PoC continuity and deterministic algorithm experiments, but it cannot override or redefine the frozen product contract.
