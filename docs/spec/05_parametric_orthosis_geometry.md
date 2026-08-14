# BiomechE-CAD — Parametric Orthosis Geometry Operators

**Status:** mathematical reference model v0 / intentionally provisional  
**Date:** 2026-08-14  
**Dependency:** `03_geometry_operation_model.md`; final global coordinate semantics depend on `01_coordinate_registration.md`.

> The formulas below are **BiomechE-CAD engineering proposals**. EasyCAD2 documents parameter names and observable behavior, but does not disclose its internal formulas. The purpose is to create deterministic, testable operators with equivalent clinical semantics, not to claim algorithmic identity.

---

## 1. Intrinsic domain

For every canonical-cage vertex `v`:

```text
s(v) ∈ [0,1]    heel -> distal/toe
q(v) ∈ [-1,1]  lateral -> medial
```

Local position is `P(v)` and a chosen displacement direction is `d(v)`.

`d(v)` is operation-specific:

- `GLOBAL_Z`;
- `LIMIT_NORMAL`;
- `CAGE_NORMAL`;
- `ANATOMICAL_VERTICAL`;
- explicit local frame axis.

Never hide direction choice inside an implementation.

---

## 2. Common smooth functions

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

Properties:

- zero outside `[a,b]`;
- equals 1 at `c`;
- C1 smooth at endpoints for baseline smoothstep;
- deterministic and easy to test.

### 2.4 Shape exponent

```text
B_p = B^p, p > 0
```

`p` changes concentration/curvature without moving start/center/end.

### 2.5 Compact transverse profile

For normalized lateral distance `x`:

```text
Phi(x,p) = (1 - x²)^p     if |x| < 1
           0              otherwise
```

This gives finite support and smooth local blending for `p >= 2`.

---

# 3. Medial arch operator

EasyCAD2 exposes, according to the manual/validation baseline:

```text
height [mm]
roundness
depth [%]
curvature
start [%]
center [%]
end [%]
```

## 3.1 Proposed parameter mapping

```text
H          = arch height [mm]
a,c,b      = start/center/end mapped to s ∈ [0,1]
q_center   = medial transverse centerline
sigma      = transverse width/depth control
p_long     = longitudinal curvature exponent
p_trans    = transverse curvature exponent
roundness  = peak-softening/blend parameter
```

## 3.2 Baseline displacement

```text
wL(v) = B(s(v); a,c,b)^p_long
x(v)  = (q(v) - q_center(s(v))) / sigma
wT(v) = Phi(x(v), p_trans)
w(v)  = wL(v) * wT(v) * MedialMask(v)
ΔP(v) = d(v) * H * w(v)
```

`q_center(s)` may be a low-order curve following the medial arch centerline.

## 3.3 Roundness

Roundness should not be implemented as an undocumented magic constant. Candidate semantics:

```text
w_round = lerp(w, smooth_local_average(w), r)
```

or an equivalent peak-shape interpolation.

The chosen formula must be frozen as `MedialArch/v1` only after visual + geometric fixtures.

## 3.4 Acceptance criteria

- height at designated center reaches target within tolerance;
- displacement is zero outside support ROI;
- start/center/end semantics remain monotonic;
- no inverted cage faces in supported range;
- limit surface has no visible ripple at transition;
- serialization round-trip reproduces geometry.

---

# 4. Lateral arch operator

Same mathematical family as medial arch but with lateral semantic mask and centerline.

```text
w(v) = B(s;a,c,b)^p_long
     * Phi((q-q_lateral_center(s))/sigma, p_trans)
     * LateralMask(v)

ΔP(v) = d(v) * H * w(v)
```

Medial/lateral are separate operator types so parameter defaults, limits and clinical semantics can differ even if they share implementation primitives.

---

# 5. Rearfoot / forefoot wedge

EasyCAD2 validation confirms wedge inclination specified/applied in degrees and full/partial application.

The core contract should therefore be angular, not an arbitrary Z displacement.

## 5.1 Reference geometry

Let:

```text
θ = target wedge angle [deg]
A = selected anatomical pivot axis/line
d⊥(v) = signed transverse distance of vertex from A
```

Baseline height contribution:

```text
h(v) = tan(θ) * d⊥(v)
```

Apply a longitudinal region mask:

```text
Rearfoot: Wr(s)
Forefoot: Wf(s)
```

and optional medial/lateral/full-partial application mask `Wp(v)`:

```text
ΔP(v) = z_dir * h(v) * Wr/f(s) * Wp(v)
```

## 5.2 Pivot preservation

The pivot axis must have zero displacement by construction.

This prevents wedge application from silently translating the whole orthosis.

## 5.3 Measurement-based validation

Test 2°, 4°, 6° fixtures:

```text
abs(measured_angle - θ) <= ANGLE_TOL
```

Measurement should use the same documented reference region, not arbitrary global mesh points.

---

# 6. Heel wrap / rearfoot operator

EasyCAD2 exposes heel/wrap height, wrap curvature and camber-related controls.

The internal EasyCAD formula is unknown.

BiomechE-CAD v0 should use a semantic heel coordinate centered at `Hc` in intrinsic space.

## 6.1 Heel elliptical radius

```text
r(v) = sqrt(((s-sh)/as)^2 + ((q-qh)/aq)^2)
```

Define heel support falloff:

```text
Wh(v) = Phi(r(v), p_heel)
```

## 6.2 Boundary emphasis for cup/wrap

A heel cup rises more near the heel perimeter than at the central plantar contact.

Use a boundary-distance semantic field `b(v) ∈ [0,1]`, where 1 approaches selected heel boundary:

```text
Wwrap(v) = Wh(v) * b(v)^p_boundary
ΔPwrap(v) = d_wrap(v) * Hwrap * Wwrap(v)
```

`d_wrap` may include vertical + inward normal components depending on the chosen clinical model.

## 6.3 Camber longitudinal component

Represent camber with start/end/height as an independent smooth longitudinal field:

```text
Wcamber(v) = B(s; a_cam, c_cam, b_cam)^p_cam * RearfootMask(v)
ΔPcamber(v) = d_cam(v) * Hcam * Wcamber(v)
```

Keeping wrap and camber as separate subfields allows independent testing and later calibration.

---

# 7. Global thickness and flatten

Thickness is a manufacturing/solid-generation semantic field:

```text
t(v) = t_global + Σ localThicknessModifiers(v)
```

## 7.1 Global thickness

Set `t_global` in mm; do not bake it into the clinical upper cage.

## 7.2 Flatten

`FlattenOperation` is a high-level operation with an explicit target plane/frame.

Possible v0 behavior:

- preserve template outline;
- replace clinical upper height with a constant or controlled planar target as defined by the product UX;
- generate lower production surface consistent with target thickness.

Because EasyCAD2’s exact internal flatten construction is undocumented, the exact BiomechE-CAD behavior must be specified via golden fixtures and UI acceptance criteria.

---

# 8. Corrective element field

A P0 corrective element should be representable as:

```text
E(s,q; params) -> signed height/support contribution
```

with transform parameters:

```text
center_s
center_q
rotation
scale_s
scale_q
scale_z
```

Transform intrinsic coordinates into element-local coordinates `(u,v)` and evaluate:

```text
h = scale_z * E(u,v)
```

## 8.1 ADD_FROM_TOP

```text
z_target = z_current + h
```

or normal-direction equivalent.

## 8.2 PLACE_FROM_BASE

Element target is referenced to production base/lower surface:

```text
z_target = max(z_current, z_base + h)
```

This is a **BiomechE-CAD candidate semantic interpretation** of EasyCAD2’s documented upper/lower-surface integration behavior, not a claim of identical implementation.

## 8.3 Example metatarsal dome/bar basis

A compact ellipsoidal basis:

```text
rho² = (u/a)^2 + (v/b)^2
E = H * (1-rho²)^p   if rho < 1
    0                 otherwise
```

A bar can use an elongated `a/b` ratio or a spline centerline.

---

# 9. Sculpt brush

For brush center projected to intrinsic/surface location `C`, radius `R`, signed strength `A`:

```text
x = distance_surface_or_local(P(v), C) / R
w = Phi(x, p)
ΔP(v) = d(v) * A * w
```

P0 implementation may use local Euclidean distance on sufficiently regular cage neighborhoods; P1 can use geodesic/surface distance if fixtures prove value.

Brush strokes should consolidate into sparse displacement layers keyed by persistent vertex ID.

---

# 10. Smooth

Smoothing is not allowed to silently destroy prescribed heights or protected boundaries.

Baseline cage-space smoothing:

```text
P'_i = P_i + λ * mask_i * (weightedNeighborAverage(P_i) - P_i)
```

Constraints:

- preserve protected boundary when requested;
- preserve fixed/locked vertices;
- avoid net shrinkage where possible (Taubin-like two-step or constrained smoothing can be evaluated);
- save algorithm/version/iterations/strength.

OpenSubdiv smoothing does not replace this operation: subdivision evaluates a limit surface; it does not semantically perform the user's EasyCAD2-style `Smooth` edit.

---

# 11. Global scan conform

Given registered scan target `T` and ROI mask `m(v)`:

1. query target point `Q(v)` by selected projection method;
2. compute delta `δ(v) = Q(v) - P(v)`;
3. clamp magnitude to `max_displacement`;
4. apply strength and falloff.

```text
ΔP(v) = m(v) * strength * clampVector(δ(v), maxDisp)
```

Projection method is serialized:

```text
CLOSEST_POINT
ANATOMICAL_VERTICAL
SURFACE_NORMAL_RAY
```

The validation fixture must report pre/post residual distance and protected-region displacement.

---

# 12. Height constraints / CONTROLLO fixes

EasyCAD2 exposes operations such as fixing medial/lateral arch height, heel/forefoot minimum height and maximum project height.

Model these as explicit constraint operations rather than hidden post-processing.

Example target-height operation:

```text
ConstraintRegion
TargetMetric
TargetValue [mm]
AdjustmentPolicy
Tolerance
```

Possible policies:

```text
SHIFT_REGION
SCALE_FIELD
CLAMP_MAX
CLAMP_MIN
BLEND_TO_TARGET
```

Each must be deterministic and previewable.

---

# 13. Minimum thickness auto-fix

For production thickness field `t(v)` and rule `t_min(v)`:

```text
violation(v) = max(0, t_min(v) - t(v))
```

Generate a smoothed correction field while respecting protected clinical upper surface where possible.

Preferred P0 policy:

- modify lower/production geometry first;
- alter clinical upper surface only if manufacturing profile explicitly allows it;
- record max correction and affected area;
- show preview before commit.

EasyCAD2’s 0.8 mm warning is a compatibility reference, not a universal BiomechE-CAD constant.

---

# 14. Operator invariants

All P0 operators must satisfy:

```text
finite coordinates
no NaN/Inf
stable vertex IDs
topology unchanged unless operation explicitly says otherwise
no inverted control faces in supported parameter envelope
bounded displacement
replay determinism
unit-explicit parameters
mirror semantics defined
```

For a frozen algorithm version:

```text
serialize -> load -> replay -> compare
```

must stay inside declared geometric tolerance.

---

# 15. Parameter-limit policy

Do not guess clinically safe min/max from implementation convenience.

Each operator has three envelopes:

```text
HARD_NUMERIC_LIMITS
PRODUCT_UI_LIMITS
VALIDATED_CLINICAL/MANUFACTURING_LIMITS
```

Only the latter two may be exposed as product constraints after validation.

---

# 16. Golden fixtures to create first

1. Neutral template cage.
2. Medial arch low/medium/high.
3. Lateral arch low/medium/high.
4. Rearfoot wedge 2/4/6°.
5. Forefoot wedge 2/4/6°.
6. Heel wrap low/high.
7. Camber low/high.
8. Metatarsal dome/bar placement + scaling.
9. Sculpt raise/lower.
10. Scan conform rectangle ROI.
11. Minimum thickness violation + fix.
12. Mirror right->left for every above fixture.

Each fixture stores:

```text
input cage hash
operation JSON
expected metrics
expected output cage hash/tolerance signature
reference screenshots
manufacturing mesh validation report
```

---

# 17. Open questions

- exact mapping of EasyCAD2 `roundness`, `depth`, `curvature` to our medial arch formula;
- exact heel wrap/camber interpretation;
- whether displacement should default to anatomical vertical or limit-surface normal per operator;
- exact semantics of `PLACE_FROM_BASE` for elements;
- whether current-cage normals or baseline normals produce more stable clinical behavior;
- whether scan conform should preserve local tangential position;
- whether production closure should use direct triangulated construction or an auxiliary robust-solid library.

These are test/calibration questions, not reasons to adopt a full B-Rep kernel prematurely.
