# BiomechE-CAD — Functional Evidence Batch 04: Arch Support

**Date:** 2026-08-14  
**Status:** ACTIVE research baseline — `ARCH-001` deep dive  
**Architecture:** intentionally out of scope / parked.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is authoritative for source metadata and locators.

---

## 0. Purpose

Define what an `ArchSupport` must mean functionally before any geometry-kernel or operator implementation is frozen.

The central conclusion of this batch is:

> **Arch support is not one scalar and there is no evidence-supported universal “optimal arch”.**

A clinically meaningful arch prescription needs at least four distinct dimensions:

```text
GEOMETRY DOSE
+ MECHANICAL DOSE
+ CLINICAL / ACTIVITY CONTEXT
+ MEASURED OUTCOME
```

EasyCAD2 already exposes multiple geometry controls for medial/lateral arch editing [EC2-MANUAL-1.1, pp. 24–30; EC2-VAL-PLAN-1.4, US12]. The literature supports keeping height and mechanical properties explicit, but also shows load redistribution and context-dependent trade-offs rather than a monotonic “more support = better” rule [REF-CAD-017; REF-CAD-045; REF-CAD-046; REF-CAD-048].

---

# 1. EasyCAD2 behavioral baseline

EasyCAD2 validates separate medial and lateral arch modification with parameters including start/center/end and shape-related controls [EC2-VAL-PLAN-1.4, US12]. The manual exposes height plus longitudinal and shape controls for the arch-edit workflow [EC2-MANUAL-1.1, pp. 24–30].

For BiomechE-CAD these parameters remain useful **authoring capabilities**, but their presence in EasyCAD2 is behavioral evidence, not proof that each parameter has a known clinical dose-response curve.

Therefore preserve the distinction:

```text
EASYCAD PARITY PARAMETER
!=
SCIENTIFICALLY CALIBRATED DOSE
```

---

# 2. Evidence hierarchy used in this batch

Arch evidence is heterogeneous, so claims are classified as:

```text
HUMAN CLINICAL / RCT
HUMAN BIOMECHANICAL / CROSSOVER
SYSTEMATIC REVIEW / META-ANALYSIS
MODEL / FINITE ELEMENT
DOMAIN / CAD REQUIREMENT
```

Model-based findings are useful for deciding **which parameters must remain explicit**, but they cannot silently become therapeutic presets.

---

# 3. Arch height is a real design dose — but not a universal optimum

## 3.1 Height-specific finite-element evidence

A muscle-driven finite-element study explicitly compared low, neutral and high custom arch-support conditions in a flexible-flatfoot model. Increasing arch support height reduced some peak pressures and proximal plantar-fascia loading, while increasing midfoot pressure and loading in other plantar-fascia regions [REF-CAD-045, Abstract—Methods/Results/Conclusion].

This supports two product requirements:

```text
arch height must be explicit and measurable
```

and

```text
higher arch support must not automatically be labelled better
```

because benefit in one region may coexist with increased loading elsewhere.

## 3.2 Multi-factor finite-element evidence

Peng et al. varied four factors:

```text
arch support height:       42 / 45 / 48 mm
medial posting inclination: 0 / 2 / 4 deg
heel cup height:            14 / 16 / 18 mm
material stiffness:          3 / 5 / 7 MPa
```

[REF-CAD-046, Table 2].

In that model, arch-support height was a major contributor to predicted forefoot, midfoot and hindfoot pressure response and proximal plantar-fascia strain. However, higher support increased medial-midfoot pressure, and the authors explicitly cautioned against excessive arch support [REF-CAD-046, Results/Table 4; Discussion].

**Functional consequence:** `ArchHeight` must be independent from posting, heel-cup and material properties. The software must preserve combinations rather than flatten them into an opaque “support strength”.

---

# 4. Human height-dose evidence exists, but is task-specific

In female collegiate athletes performing a cutting maneuver, three medial arch heights were compared: flat/no arch, a commercial-height arch and an intentionally high/double-height arch. Higher arch support was associated with a lower knee valgus angle at initial contact, while other measured variables did not differ significantly [REF-CAD-050, Abstract—Methods/Results].

This is useful evidence that **height is a biomechanical dose**, but it is not a universal prescription rule because:

- the cohort was female athletes;
- the task was a cutting maneuver;
- the outcome was knee valgus at initial contact;
- the “high” condition was deliberately an overcorrection experiment.

Therefore BiomechE-CAD may support evidence-linked height presets only when they preserve population, activity and outcome context.

---

# 5. Arch support redistributes load; midfoot load is a first-class safety outcome

This is one of the strongest recurring patterns.

A 2026 systematic review/meta-analysis of conservative interventions in flexible flatfoot found that insole interventions increased medial-midfoot pressure in the pooled analyses while effects in other regions varied [REF-CAD-048, Abstract—Results]. Long-term efficacy remained uncertain [REF-CAD-048, Abstract—Conclusion].

A one-month study in women with mild-to-moderate hallux valgus found reduced pressure/force at hallux and several metatarsal regions but increased medial-midfoot peak pressure, force and contact area with medial arch support [REF-CAD-049, pp. 134–139; Abstract—Results].

A flatfoot walking study likewise showed increased midfoot contact area and regional pressure changes rather than a simple global reduction [REF-CAD-055, Abstract—Results/Conclusions].

Therefore arch verification must include at minimum:

```text
TARGET / INTENDED REGION
MEDIAL MIDFOOT
LATERAL MIDFOOT
FOREFOOT
HEEL
REMOTE / SAFETY REGIONS
```

and pressure outcomes should include Peak Pressure, PTI when available, and Contact Area under a compatible measurement protocol.

---

# 6. Remote load transfer can matter outside the arch itself

In basketball landing/shuttle tasks, a medial arch-support orthosis increased inversion angle and fifth-metatarsal loading in the tested male cohort [REF-CAD-051, Abstract—Results/Conclusion].

This does **not** establish that arch support is unsafe in sport generally. It establishes a more useful software rule:

> A local medial intervention can alter remote/lateral-column loading, so a CAD/outcome system should not monitor only the medial arch ROI.

For sport profiles, candidate safety regions should include at least lateral forefoot/fifth-metatarsal areas when supported by the measurement setup.

---

# 7. Mechanical dose is distinct from geometric dose

## 7.1 Hardness/stiffness can alter response

In adults with flexible flatfoot, varying arch-support hardness across Shore C 30, 50 and 70 changed biomechanical/musculoskeletal outcomes; harder conditions showed diminishing/plateauing benefits with increases in some knee/forefoot loading measures [REF-CAD-017, Abstract—Methods/Results/Conclusions].

In another randomized crossover study of healthy volunteers, two 3D-printed silicone arch supports of differing hardness and one prefabricated support redistributed pressure similarly after one month, while the printed supports were rated more comfortable [REF-CAD-047, pp. 210–217; Abstract—Results].

A 78-participant randomized trial in pes planus comparing soft 3D-printed silicone, hard 3D-printed silicone and total-contact insoles found improvement in pain/function across groups without clear superiority in plantar-pressure redistribution between orthosis types [REF-CAD-052, Abstract—Methods/Results/Conclusion].

These studies reinforce the requirement to store:

```text
material identity
hardness scale + value
stiffness / modulus when known
thickness / regional construction
```

separately from arch height/shape.

## 7.2 Reinforcement and geometric undercut are separable

An exploratory 3D-printed flatfoot study varied arch reinforcement and arch-height undercut/elevation as separate design features. Stronger combined support did not automatically produce more favorable outcomes [REF-CAD-053, Abstract/full article].

**Product consequence:** an `ArchSupport` cannot be represented by a single UI slider named `strength` if that slider simultaneously changes geometry and material mechanics.

---

# 8. Structural arch correction is measurable, but protocol-bound

A 2024 study of generic 3D-printed orthoses measured medial arch correction at 0%, 50% and 125% body-weight loading. Orthoses increased arch height across the tested loading conditions [REF-CAD-056, Abstract—Methods/Results].

A radiographic/anthropometric study also demonstrated measurable elevation of the medial longitudinal arch with a contoured support/orthosis [REF-CAD-057, Abstract—Results/Conclusions].

Therefore arch geometry/QC should distinguish:

```text
DESIGN ARCH HEIGHT
vs
FOOT / OUTCOME ARCH HEIGHT
```

and any patient structural measurement must preserve the loading condition:

```text
non-weight-bearing
partial weight-bearing
full weight-bearing
single-leg / augmented load
walking / running dynamic
```

A CAD height in millimetres is not equivalent to a measured navicular/arch-height change in vivo.

---

# 9. Arch support may be useful in multiple populations, but the evidence must remain separated

## 9.1 Flexible flatfoot / pes planus

Systematic reviews previously incorporated into the project show heterogeneous evidence for adult/flexible flatfoot and do not justify one universal orthotic doctrine [REF-CAD-027; REF-CAD-028]. The newer pressure-focused systematic review confirms that plantar-pressure redistribution occurs, but longer-term effects remain uncertain [REF-CAD-048].

A 2025 RCT in pes planus supports pain/function improvement across multiple support types without demonstrating a universally superior hardness/material condition [REF-CAD-052].

## 9.2 Diabetic/offloading context

Arch profiles are among the design features associated with offloading effects in diabetic-foot literature, but targets and verification protocols remain use-case specific [REF-CAD-007; GUIDE-IWGDF-2023].

## 9.3 Hallux valgus

Medial arch support can redistribute load away from parts of the forefoot toward the midfoot in the studied cohort [REF-CAD-049].

## 9.4 Plantar heel pain / plantar fasciitis

A 2026 prospective study reported short-term symptom improvement, increased arch measures and lower modeled heel stress with arch-support insoles, but it was not a controlled trial and explicitly calls for longer controlled studies [REF-CAD-054, Abstract—Methods/Results/Conclusion].

## 9.5 Running / sport

In symptomatic pronated runners, adding the tested arch-support component had relatively small COP effects compared with forefoot wedge dose [REF-CAD-015, pp. 212–217; Abstract—Results]. Other sport tasks show possible remote lateral-column load effects [REF-CAD-051].

**Rule:** do not transfer a finding from one use case into another profile without explicit evidence.

---

# 10. Evidence gap: longitudinal extent, peak location, curvature and “roundness”

The targeted literature search found substantially more evidence isolating:

```text
arch height
material hardness/stiffness
posting
heel cup interaction
pressure redistribution
```

than evidence that independently calibrates:

```text
longitudinal start
peak/center location
longitudinal end
arch width/depth
curvature
roundness
proximal/distal transition length
```

for a specific clinical outcome.

EasyCAD2 exposes several of these shape parameters [EC2-MANUAL-1.1, pp. 24–30], so they remain legitimate P0 CAD controls. But at this checkpoint they should be classified as:

```text
AUTHORING / PRESCRIPTION PARAMETERS
NOT SCIENTIFICALLY CALIBRATED UNIVERSAL DOSES
```

This is a research gap, not a reason to remove the controls.

---

# 11. Proposed canonical functional model

```text
ArchSupportPrescription
  id
  side
  archType
    MEDIAL
    LATERAL

  intendedEffect
    SUPPORT
    REDISTRIBUTE
    CONTAIN
    ALIGN
    OFFLOAD_SECONDARY_REGION

  contextProfileRef
  evidenceRefs[]

  anatomy
    targetArch
    targetROI
    referenceLandmarks[]

  geometry
    start_s
    peak_s
    end_s
    transverseCenter_q

    peakHeight_mm
    width_or_depth_mm
    curvature
    roundness

    proximalTransition_mm
    distalTransition_mm
    medialTransition_mm
    lateralTransition_mm

  geometryReference
    template/base surface
    scan-derived foot surface
    foot-length normalized frame
    clinician landmark set

  mechanical
    materialProfileRef
    hardnessScale
    hardnessValue
    effectiveModulus_MPa [when known]
    regionalThickness_mm [when relevant]
    reinforcementProfileRef [optional]

  outcomeIntent
    targetMetrics[]
    safetyRegions[]

  author
  timestamp
  algorithmVersion
```

The exact implementation may later change, but these semantics should survive independently of the geometry kernel.

---

# 12. Measurement model

## 12.1 Design-side geometric measurements

P0 should report:

```text
requested peak arch height
actual design peak arch height
peak longitudinal position
start/end longitudinal extent
arch width/depth
local section profiles
transition lengths
```

with units/reference frame.

## 12.2 Patient/outcome measurements

Where acquisition supports them:

```text
navicular height
arch height index / chosen structural index
medial longitudinal arch angle
midfoot contact area
regional peak pressure
PTI
COP / kinematics [profile dependent]
comfort / pain / function
```

Patient/outcome metrics must preserve loading/activity protocol.

---

# 13. Arch target + safety-region concept

Arch support should adopt the same redistribution philosophy already established for local offloading:

```text
ARCH TARGET REGION
+
ADJACENT MIDFOOT REGION
+
FOREFOOT / HEEL
+
REMOTE PROFILE-SPECIFIC SAFETY REGIONS
```

For example, a result may legitimately be:

```text
Forefoot peak pressure: improved
Medial midfoot pressure: increased
Contact area: increased
Comfort: acceptable
```

rather than being collapsed into a single green/red state.

---

# 14. Preset policy

Allowed:

```text
Evidence-linked preset
  source
  population
  task
  geometry/material dose
  outcome studied
  evidence strength
```

Not allowed:

```text
Optimal Arch = 45 mm
Hardness = Shore C 50
```

as global hidden defaults.

Even the explicit 42/45/48 mm values in the Taguchi finite-element study belong to that model/subject/design setup [REF-CAD-046, Table 2] and must not be promoted to universal clinical values.

---

# 15. P0 / P1 / P2

## P0

- medial and lateral arch as named prescription objects;
- explicit start/peak/end and height;
- shape controls including width/depth, curvature/roundness and transitions;
- absolute + normalized anatomical reporting;
- geometry/mechanical-property separation;
- material/hardness/stiffness metadata when known;
- target + safety-region analysis hooks;
- design geometric QC;
- evidence/provenance links;
- save/load/history/versioning.

## P1

- evidence-linked context presets;
- scan/pressure-guided arch adjustment assistant;
- before/after regional dashboards;
- structural arch-height/navicular integration;
- comfort/PROM workflow;
- population/activity profiles;
- regional mechanical-property realization.

## P2 / R&D

- predictive pressure/kinematic response to arch geometry;
- automatic multi-objective arch optimization;
- patient-specific FE/surrogate optimization;
- learned geometry + stiffness recommendation with uncertainty/applicability domain.

---

# 16. Functional acceptance tests

## ARCH-001 — semantic identity
A medial/lateral arch remains a named prescription through save/load/history and is not reduced to anonymous geometry.

## ARCH-002 — explicit height dose
Requested `peakHeight_mm` is stored, reportable and measurable on the resulting design in the declared reference convention.

## ARCH-003 — longitudinal placement
`start_s`, `peak_s` and `end_s` survive save/load and template-supported morphing without changing semantic order.

## ARCH-004 — shape parameters remain explicit
Width/depth, curvature/roundness and transition parameters can be inspected/versioned even though current evidence does not define universal therapeutic values for them.

## ARCH-005 — geometry/mechanics independence
Changing material/hardness does not silently change arch geometry; changing geometry does not silently overwrite material properties.

## ARCH-006 — physical hardness provenance
A hardness value cannot be serialized as an unlabeled number; scale/type (e.g. Shore family) and source/profile are required.

## ARCH-007 — loading context
Patient structural arch measurements identify loading/activity condition; static CAD height is never mislabeled as in-vivo arch correction.

## ARCH-008 — target + redistribution outcome
Pressure comparison can report arch/midfoot plus forefoot/heel changes rather than only the target region.

## ARCH-009 — remote safety region
A use-case profile can add remote safety ROIs such as fifth-metatarsal/lateral column for dynamic sport tasks.

## ARCH-010 — no universal optimum
No global preset is labelled clinically optimal solely from a single study/model.

## ARCH-011 — evidence-linked preset context
A literature-derived preset preserves source ID, population, task/activity, tested dose and outcome.

## ARCH-012 — combined-feature provenance
Arch height, posting, heel cup and material parameters remain separately identifiable when used together.

## ARCH-013 — outcome traceability
Pressure, structural and PROM outcomes identify the exact design + manufacturing revision tested.

## ARCH-014 — mirror/side semantics
Left/right mirroring preserves medial/lateral anatomical meaning rather than merely reflecting arbitrary XYZ coordinates.

---

# 17. Product decisions supported by this batch

### ARCH-RULE-001
`ArchSupport` is a structured prescription, not a generic bulge or one-dimensional strength slider.

### ARCH-RULE-002
Arch geometry and arch mechanics are independent prescription dimensions.

### ARCH-RULE-003
Higher arch support is not globally better; redistribution and comfort/safety outcomes must remain visible.

### ARCH-RULE-004
Longitudinal start/center/end, curvature and roundness remain editable P0 parameters, but they are not currently assigned universal evidence-derived dose defaults.

### ARCH-RULE-005
Any evidence-derived arch preset is population/task/outcome specific.

### ARCH-RULE-006
Design height and patient structural arch height are distinct quantities with different reference/loading conditions.

---

# 18. Research gaps remaining after ARCH-001

1. Direct human dose-response evidence isolating **arch longitudinal extent**.
2. Direct human evidence isolating **peak longitudinal location**.
3. Direct evidence isolating **arch curvature/roundness** while holding height/material constant.
4. Better clinical thresholds for excessive midfoot load/comfort intolerance.
5. Interaction of arch geometry with shoe volume/fit and long-term adherence.
6. Long-term material creep/fatigue changing the effective arch mechanical dose.
7. Better population-specific evidence separating symptomatic vs asymptomatic flexible flatfoot.
8. Prospective pressure-guided arch optimization studies using repeatable CAD parameter reporting.

These are legitimate future research questions and should not be hidden by implementation assumptions.

---

# 19. Conclusion

The P0 abstraction should be:

```text
ARCH SUPPORT
   │
   ├── anatomical placement
   ├── geometry dose
   │     height
   │     start / peak / end
   │     width/depth
   │     curvature/roundness
   │     transitions
   │
   ├── mechanical dose
   │     material
   │     hardness/stiffness
   │     reinforcement
   │
   ├── clinical/activity context
   │
   └── measured outcome
         target region
         midfoot redistribution
         forefoot / heel
         remote safety regions
         structural arch metrics
         comfort / PROM
```

not:

```text
arch_strength = 0..100
```

This functional contract is independent of the future geometry engine and is mature enough to feed the consolidated functional specification and eventual acceptance suite.

---

## Bibliography links

[EC2-MANUAL-1.1]: ../BIBLIOGRAPHY.md#ec2-manual-11
[EC2-VAL-PLAN-1.4]: ../BIBLIOGRAPHY.md#ec2-val-plan-14
[GUIDE-IWGDF-2023]: ../BIBLIOGRAPHY.md#guide-iwgdf-2023
[REF-CAD-007]: ../BIBLIOGRAPHY.md#ref-cad-007
[REF-CAD-009]: ../BIBLIOGRAPHY.md#ref-cad-009
[REF-CAD-015]: ../BIBLIOGRAPHY.md#ref-cad-015
[REF-CAD-016]: ../BIBLIOGRAPHY.md#ref-cad-016
[REF-CAD-017]: ../BIBLIOGRAPHY.md#ref-cad-017
[REF-CAD-027]: ../BIBLIOGRAPHY.md#ref-cad-027
[REF-CAD-028]: ../BIBLIOGRAPHY.md#ref-cad-028
[REF-CAD-045]: ../BIBLIOGRAPHY.md#ref-cad-045
[REF-CAD-046]: ../BIBLIOGRAPHY.md#ref-cad-046
[REF-CAD-047]: ../BIBLIOGRAPHY.md#ref-cad-047
[REF-CAD-048]: ../BIBLIOGRAPHY.md#ref-cad-048
[REF-CAD-049]: ../BIBLIOGRAPHY.md#ref-cad-049
[REF-CAD-050]: ../BIBLIOGRAPHY.md#ref-cad-050
[REF-CAD-051]: ../BIBLIOGRAPHY.md#ref-cad-051
[REF-CAD-052]: ../BIBLIOGRAPHY.md#ref-cad-052
[REF-CAD-053]: ../BIBLIOGRAPHY.md#ref-cad-053
[REF-CAD-054]: ../BIBLIOGRAPHY.md#ref-cad-054
[REF-CAD-055]: ../BIBLIOGRAPHY.md#ref-cad-055
[REF-CAD-056]: ../BIBLIOGRAPHY.md#ref-cad-056
[REF-CAD-057]: ../BIBLIOGRAPHY.md#ref-cad-057
