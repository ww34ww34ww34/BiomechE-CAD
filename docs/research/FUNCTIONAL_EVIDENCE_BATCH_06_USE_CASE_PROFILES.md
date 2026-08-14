# BiomechE-CAD — Functional Evidence Batch 06: Use-case / Population Profiles

**Date:** 2026-08-14  
**Status:** ACTIVE research baseline — `PROFILE-001`  
**Architecture:** intentionally out of scope / parked.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is the authoritative source ledger.

---

## 0. Purpose

BiomechE-CAD must not encode one universal orthotic doctrine. The same geometric or mechanical intervention can have different goals, outcome metrics, evidence strength and safety implications in different populations.

This batch defines a **context layer** above the shared CAD features:

```text
COMMON CAD CAPABILITIES
        +
USE-CASE / POPULATION PROFILE
        ↓
relevant features
relevant outcomes
allowed evidence-linked targets
required acquisition protocol
warnings / non-transfer rules
```

A profile does **not** automatically prescribe an orthosis. It constrains interpretation and reporting.

---

# 1. Canonical profile contract

```text
IndicationProfile
  id
  version
  displayName

  populationBoundary
  indicationBoundary
  excludedOrSeparateContexts[]

  relevantFeatures[]
  recommendedMeasurements[]
  optionalMeasurements[]

  outcomeTargets[]
    metric
    ROI
    direction / threshold
    protocol
    evidenceRef
    confidence

  safetyRegions[]
  requiredAcquisitionMetadata[]
  warnings[]
  nonTransferRules[]

  evidenceRefs[]
  evidenceConfidence
```

The profile is a **versioned evidence context**, not a hardcoded collection of geometry values.

---

# 2. PROFILE-DIABETIC-OFFLOAD

## 2.1 Scope

Primary intended context:

```text
adult with diabetes
+ peripheral neuropathy / loss of protective sensation or elevated ulcer risk
+ prevention of plantar ulcer/re-ulceration
+ therapeutic footwear / custom insole workflow
```

The IWGDF prevention guideline recommends properly fitting accommodative therapeutic footwear for moderate-to-high risk people and, for preventing recurrence of a plantar ulcer, footwear with a **demonstrated plantar-pressure relieving effect during walking** [GUIDE-IWGDF-2023, Prevention guideline].

Pressure-informed orthosis design has direct trial evidence in people with diabetes, neuropathy and prior plantar ulceration [REF-CAD-004; REF-CAD-005; REF-CAD-069].

## 2.2 Hard non-transfer rule: active ulcer treatment is a separate pathway

Do **not** let a `DIABETIC_OFFLOAD_PREVENTION` profile imply that an insole CAD workflow is the first-line treatment for an active neuropathic plantar forefoot/midfoot ulcer.

IWGDF 2023 recommends a **non-removable knee-high offloading device** as first-choice treatment for healing that active-ulcer context; removable devices are subsequent choices depending on contraindication/tolerance [GUIDE-IWGDF-2023, Offloading guideline].

Therefore the software should distinguish at least:

```text
DIABETIC_PREVENTION / RE-ULCERATION
ACTIVE_DIABETIC_ULCER — CLINICAL OFFLOADING PATHWAY
```

If an active ulcer is recorded, the CAD may still support downstream footwear/orthosis design, but must show an explicit clinical-pathway warning and must not label an insole alone as guideline-equivalent first-line offloading.

## 2.3 Relevant CAD features

```text
pressure-guided ROI targeting
local relief / aperture
metatarsal pad/bar/dome
arch / total-contact contour
heel relief / containment when relevant
regional material / cushioning / stiffness
minimum thickness / DFM
footwear fit envelope
revision / manufacturing traceability
```

## 2.4 Primary outcome metrics

P0/P1 priorities:

```text
PeakPressure
PTI
ContactArea
regional load distribution
target ROI + safety ring
adherence / wear exposure
ulcer / lesion outcome [clinical follow-up]
```

Pressure remains protocol-bound and numerical [REF-CAD-033; REF-CAD-034; REF-CAD-035; REF-CAD-036].

## 2.5 Pressure targets

Where a guideline/profile defines a pressure-relief criterion, store it as a context object rather than a universal constant [GUIDE-IWGDF-2023; REF-CAD-037; REF-CAD-038].

Example structure:

```text
OutcomeTarget
  profile = DIABETIC_REULCERATION_PREVENTION
  metric = PeakPressure
  ROI = prior/high-risk plantar site
  criterion = evidence-linked
  acquisition = validated/calibrated in-shoe pressure
```

No threshold is globally inherited by metatarsalgia, flatfoot, heel pain or sport.

## 2.6 Adherence is a first-class outcome

Improved pressure offloading only reduced ulcer recurrence in the high-adherence subgroup of a multicenter RCT [REF-CAD-068, Abstract—Results/Conclusions]. A 2026 multicenter trial also demonstrated that personalized multimodal support can improve custom-footwear adherence [REF-CAD-071, Abstract—Results].

Therefore:

```text
orthosis efficacy
!=
CAD pressure effect alone
```

The profile should support:

```text
wearTime
percentageStepsWorn
indoor/outdoor footwear context
adherence quality flags
```

## 2.7 Daily-life pressure monitoring — optional P2 direction

Continuous pressure monitoring with personalized feedback has proof-of-concept RCT evidence for reducing ulcer-site recurrence [REF-CAD-070, pp. e308–e318]. This justifies a future integration hook, not a P0 CAD requirement.

## 2.8 Confidence

```text
HIGH for the need to demonstrate plantar-pressure relief in defined high-risk diabetic prevention contexts
MODERATE-HIGH for pressure-informed/custom optimization
HIGH that adherence materially modifies real-world effectiveness
```

---

# 3. PROFILE-MECHANICAL-METATARSALGIA

## 3.1 Scope

```text
adult mechanical/central metatarsalgia
forefoot pain / elevated central MTH loading
no automatic assumption of diabetic neuropathy
```

A meta-analysis of 5 studies/158 participants supports bespoke/custom orthotic treatment for reducing plantar pressure under the central 2nd–4th metatarsal heads [REF-CAD-011, pp. 111–118]. A broader systematic review of custom orthoses for forefoot pain included rheumatoid arthritis, hallux valgus and isolated/secondary metatarsalgia and generally found pain improvement, but heterogeneity means those conditions should not be silently merged into one diagnosis [REF-CAD-072, pp. 1865–1875].

## 3.2 Relevant features

```text
MetatarsalDome
MetatarsalPad
MetatarsalBar
MetatarsalHeadRelief
ForefootCushioning
ForefootPost / wedge when clinically intended
custom ROI relief
```

Placement is a dose. Evidence shows response varies with location relative to metatarsal heads/pressure peaks [REF-CAD-013; REF-CAD-041; REF-CAD-042].

## 3.3 Primary outcomes

```text
pain / walking pain
PeakPressure at symptomatic MTH ROI
PTI
forefoot contact area
adjacent / transfer load
comfort / shoe fit
function PROM when selected
```

The 2026 forefoot review supports retaining both peak pressure and PTI and highlights heterogeneity across pathologies and designs [REF-CAD-012].

## 3.4 Non-transfer rules

- Do not apply diabetic ulcer pressure thresholds automatically.
- Do not label one proximal-pad distance as universally optimal; evidence-linked values are population/design specific.
- Do not merge rheumatoid arthritis, hallux valgus, Morton-type symptoms, hallux rigidus or neuropathic ulcer prevention into one `METATARSALGIA` evidence profile without a subcontext.

## 3.5 Confidence

```text
MODERATE-HIGH for central MTH pressure reduction
MODERATE for pain benefit across heterogeneous forefoot conditions
MODERATE for placement sensitivity
```

---

# 4. PROFILE-FLEXIBLE-FLATFOOT

## 4.1 Scope must distinguish symptomatic status, age and task

At minimum distinguish:

```text
ADULT_SYMPTOMATIC_FLEXIBLE_FLATFOOT
ADULT_ASYMPTOMATIC_FLEXIBLE_FLATFOOT
PEDIATRIC_FLEXIBLE_FLATFOOT
RUNNING_WITH_ASYMPTOMATIC_FLATFOOT
```

These are not interchangeable populations.

An adult systematic review concluded that evidence for routine orthosis provision was weak/inconsistent [REF-CAD-027]. A newer network meta-analysis of RCTs reports improvements in pain and several biomechanical/radiographic outcomes, but its included ages span children/young adults and therefore does not erase the population-boundary problem [REF-CAD-073, Abstract—Methods/Results].

## 4.2 Relevant features

```text
MedialArchSupport
LateralArchSupport where indicated
RearfootPost
ForefootPost
HeelCup / containment
arch material/hardness
arch reinforcement / undercut
```

`ARCH-001` already established that arch geometry and mechanical dose must be separate.

## 4.3 Primary outcomes

Possible metrics depend on profile subtype:

```text
pain
function / PROM
PeakPressure + PTI by region
midfoot contact area
navicular drop / structural arch measure
calcaneal pitch / radiographic metric [import]
COP
rearfoot eversion / ankle moments [research]
comfort
```

A 2026 plantar-pressure review found that insoles can increase medial-midfoot pressure substantially while effects elsewhere differ, reinforcing redistribution rather than a global “pressure reduction” objective [REF-CAD-048].

## 4.4 Safety / interpretation rule

The medial midfoot is often a **target/support region**, not automatically an adverse ROI. A pressure increase there can reflect increased contact/support. Therefore the software should report:

```text
medial-midfoot pressure
contact area
symptoms / tolerance
forefoot + heel redistribution
```

rather than simply flagging any midfoot increase as failure.

## 4.5 Sport subtype

In runners with asymptomatic flatfoot, a 2025 meta-analysis found little significant change with arch-support-only orthoses, while arch support combined with medial rearfoot/forefoot posting altered several ankle/Achilles loading variables [REF-CAD-078]. Therefore the sport subtype must not inherit sedentary/walking flatfoot conclusions unmodified.

## 4.6 Confidence

```text
MIXED / MODERATE overall
MODERATE for measurable redistribution and some biomechanical effects
LOW-MODERATE for universal long-term clinical prescription rules
```

---

# 5. PROFILE-PLANTAR-HEEL-PAIN

## 5.1 Scope

```text
adult plantar heel pain / plantar fasciitis-type presentation
```

The 2023 clinical practice guideline treats foot orthoses as an adjunct/multimodal intervention rather than an isolated short-term treatment [GUIDE-HEEL-PAIN-2023].

A 2018 systematic review found a small medium-term pain benefit versus sham with uncertain clinical importance and no clear custom-over-prefabricated superiority [REF-CAD-066]. A newer meta-analysis of 8 RCTs reports significant pain relief but no significant function/walking-ability advantage, reinforcing outcome separation rather than a single “success” label [REF-CAD-074, Abstract—Results/Conclusion].

## 5.2 Relevant features

```text
HeelCup / containment
HeelMechanicalRegion / cushioning
HeelRelief / local target
ArchSupport
whole-foot contour / conformity
```

`HEEL-001` separates containment, relief, camber and mechanical regions.

## 5.3 Outcomes

```text
pain
Foot Function Index or selected PROM
comfort
fit
PeakPressure / MeanPressure / PTI at heel
ContactArea
plantar fascia thickness [optional clinical/research import]
heel-pad metrics [research]
```

Pressure and PROM outcomes remain separate [REF-CAD-018; REF-CAD-065].

## 5.4 Non-transfer rules

- Do not apply pediatric Sever's heel-cup results to adults without an explicit context change.
- Do not call custom devices intrinsically superior to prefabricated alternatives.
- Do not use a diabetic offloading pressure threshold as a heel-pain treatment target.
- Do not infer pain benefit from heel-pressure reduction alone.

## 5.5 Confidence

```text
MODERATE for pain benefit as part of conservative management
LOW-MODERATE for specific geometry/material superiority
MIXED for functional superiority
```

---

# 6. PROFILE-SPORT-PERFORMANCE

## 6.1 Scope

This profile covers healthy or athletic users where the primary objective may be:

```text
comfort
load redistribution
biomechanical modification
running economy / performance
injury-risk mitigation
sport-specific fit
```

It must not be treated as a therapeutic pathology profile.

## 6.2 Evidence is task-dependent

A 2024 systematic review/meta-analysis of 35 running studies found orthoses altered several pressure/kinematic variables, increased midfoot pressure, and improved perceived comfort with custom devices; however custom orthoses also showed an unfavorable pooled effect on running economy and perceived exertion in the included evidence [REF-CAD-075, pp. 240–258; Abstract—Results].

A systematic review/meta-analysis on injury prevention found reduced overall injury/stress-fracture risk with foot orthoses, but study quality varied and effects did not extend to all injury categories [REF-CAD-076, pp. 86–96]. A later bone-stress-injury review also characterized orthosis evidence as low quality and largely military-context dependent [REF-CAD-078A].

Comfort has its own performance relationship: a meta-analysis of recreational running footwear conditions found an association between greater comfort and improved running economy [REF-CAD-077, pp. 121–133]. This does not mean every custom orthosis improves economy.

## 6.3 Relevant features

```text
arch support
rearfoot / forefoot posting
heel cup
cushioning / material
mass / thickness / footwear envelope
metatarsal elements when specifically indicated
```

## 6.4 Required context metadata

```text
sport
surface
speed / pace
shoe model
shoe size / fit
training vs competition
session duration
body mass / load carried when relevant
foot strike / task where measured
```

## 6.5 Outcomes

```text
comfort
RPE
running economy / oxygen cost [research]
pace / time
regional pressure / PTI
COP
kinematics / kinetics [research]
injury exposure / incidence [longitudinal]
```

## 6.6 Non-transfer rules

- Healthy-runner biomechanical effects do not establish treatment effects in symptomatic patients.
- A pressure redistribution is not automatically an injury-prevention effect.
- An injury-prevention signal is not automatically a performance improvement.
- Comfort, economy and biomechanics may rank designs differently.

## 6.7 Confidence

```text
MODERATE for task-specific biomechanical/pressure effects
MODERATE for comfort effects
LOW-MODERATE for generalized injury prevention
MIXED for running-economy/performance benefit
```

---

# 7. PROFILE-GENERIC-CUSTOM-ORTHOSIS

## 7.1 Why it exists

A generic profile is needed when the clinician wants a custom orthosis without selecting a validated indication profile, or when the indication is outside the evidence packs currently encoded.

It is intentionally conservative.

## 7.2 Behavior

The generic profile enables all validated CAD authoring capabilities but applies **no disease-specific thresholds, recommendations or “optimal” presets**.

```text
allowed:
  DIMA / morphology
  scan / pressure registration
  heel / arch / wedge
  corrective elements
  relief
  material regions
  sculpt / local edit
  geometric QC / DFM

not automatically applied:
  diabetic pressure targets
  metatarsalgia pad-placement preset
  flatfoot arch-dose claim
  plantar-heel-pain treatment claim
  sport performance claim
```

## 7.3 Required intent field

Every generic prescription should record:

```text
clinical/design intent
free-text rationale
selected target ROI/metric if any
clinician/user author
```

This preserves traceability without pretending that an evidence profile exists.

## 7.4 Confidence

`DOMAIN-ONLY`: it is a safe software fallback, not a clinical evidence category.

---

# 8. Shared profile rules

## PROFILE-RULE-001 — one design may have multiple contexts, but one context is active for interpretation

A patient may have diabetes, metatarsalgia and heel pain simultaneously. The system may attach several relevant profiles, but threshold interpretation must identify which profile supplied each target/warning.

## PROFILE-RULE-002 — no silent threshold inheritance

A numerical threshold has:

```text
profileId
population
metric
ROI
protocol
evidenceRef
```

## PROFILE-RULE-003 — evidence-linked presets are optional and inspectable

A preset must show source, population and known/unknown design parameters.

## PROFILE-RULE-004 — measurements are not diagnoses

Pressure peaks, flatfoot morphology or pain maps do not automatically establish a diagnosis.

## PROFILE-RULE-005 — active pathology can change the treatment pathway

If the recorded context falls outside a CAD-insole pathway (e.g. an active diabetic plantar ulcer where guideline first-line offloading is a non-removable knee-high device), surface a clinical-pathway warning rather than silently applying a prevention profile.

## PROFILE-RULE-006 — human/model evidence separation

Model-derived design sensitivity can justify preserving a parameter, but cannot become a clinical target without appropriate evidence.

---

# 9. Profile compatibility matrix

| Capability / outcome | Diabetes offload | Mechanical metatarsalgia | Flexible flatfoot | Plantar heel pain | Sport/performance | Generic |
|---|---:|---:|---:|---:|---:|---:|
| Quantitative pressure | **Core** | **Core** | useful | useful | useful | optional |
| PTI | **Core** | **Core** | useful | useful | useful | optional |
| Target + safety ring | **Core** | **Core** | useful | useful | useful | optional |
| Metatarsal elements | frequent | **Core** | optional | optional | optional | available |
| Arch prescription | frequent | optional | **Core** | frequent | frequent | available |
| Heel containment | as indicated | optional | frequent | **Core** | frequent | available |
| Local cushioning/material | **Core** | frequent | optional | **Core** | frequent | available |
| PROM/pain | clinical follow-up | **Core** | **Core if symptomatic** | **Core** | secondary | optional |
| Adherence | **Core** | useful | useful | useful | useful | optional |
| Performance/economy | no | no | sport subtype | no | **Core/research** | no |
| Disease-specific threshold | context-bound | no universal | no universal | no universal | no universal | none |

---

# 10. Acceptance semantics

## PROFILE-001 — stable profile identity

Profile ID/version survives project save/load/history and is included in reports.

## PROFILE-002 — source provenance

Each profile target/warning can resolve to a canonical bibliography source ID.

## PROFILE-003 — no cross-profile threshold leakage

A diabetic pressure threshold is not applied after switching to mechanical-metatarsalgia or generic context unless explicitly reselected.

## PROFILE-004 — active-ulcer pathway guard

Recording an active diabetic plantar forefoot/midfoot ulcer prevents the prevention profile from being presented as sufficient first-line offloading guidance and surfaces the IWGDF pathway context.

## PROFILE-005 — multi-profile provenance

When multiple profiles are attached, every target/warning identifies its source profile.

## PROFILE-006 — population boundary

Pediatric evidence does not automatically populate an adult profile and vice versa.

## PROFILE-007 — activity boundary

Running/sport evidence is not silently transferred to walking/clinical outcome interpretation.

## PROFILE-008 — metric bundle

Profile-specific default dashboards expose the appropriate metric bundle without deleting raw numeric data.

## PROFILE-009 — generic profile neutrality

`GENERIC_CUSTOM_ORTHOSIS` applies no hidden disease-specific threshold or therapeutic claim.

## PROFILE-010 — clinical outcome separation

Pressure, PROM, adherence and event outcomes remain distinct observations tied to the same design/manufacturing revision.

## PROFILE-011 — evidence-confidence visibility

The UI/report can show whether a recommendation/target is `HIGH`, `MODERATE`, `EMERGING/MIXED`, or `DOMAIN-ONLY`.

## PROFILE-012 — protocol compatibility

Profile-specific comparisons reuse the acquisition comparability states defined in `spec/09_analysis_qc_dfm.md`.

---

# 11. P0 / P1 / P2

## P0

```text
IndicationProfile schema
GENERIC profile
diabetic prevention/re-ulceration profile boundary
mechanical metatarsalgia profile
flexible flatfoot profile
plantar heel pain profile
sport/performance profile
profile version + evidence refs
non-transfer rules
context-bound target model
multi-profile provenance
```

## P1

```text
guided profile selection
profile-specific dashboards
clinical-pathway warnings
evidence-linked presets
PROM/adherence integration
report generation by profile
```

## P2 / R&D

```text
automatic candidate profile suggestions
adaptive targets from longitudinal outcomes
predictive response models
cross-profile multi-objective optimization
continuous pressure/wearable integration
```

Automatic profile suggestion must never be serialized as a clinician-confirmed diagnosis without explicit confirmation.

---

# 12. Product conclusion

BiomechE-CAD should answer not only:

```text
What shape did we build?
```

but:

```text
For which population / indication?
What was the intended outcome?
Which features and metrics are relevant here?
Which numerical targets are actually valid in this context?
What must NOT be transferred from another population?
What evidence supports the interpretation?
```

That context layer is required before freezing a project schema or geometry architecture.

---

# 13. Bibliography links

[GUIDE-IWGDF-2023]: ../BIBLIOGRAPHY.md#guide-iwgdf-2023
[GUIDE-HEEL-PAIN-2023]: ../BIBLIOGRAPHY.md#guide-heel-pain-2023
[REF-CAD-004]: ../BIBLIOGRAPHY.md#ref-cad-004
[REF-CAD-005]: ../BIBLIOGRAPHY.md#ref-cad-005
[REF-CAD-011]: ../BIBLIOGRAPHY.md#ref-cad-011
[REF-CAD-012]: ../BIBLIOGRAPHY.md#ref-cad-012
[REF-CAD-013]: ../BIBLIOGRAPHY.md#ref-cad-013
[REF-CAD-018]: ../BIBLIOGRAPHY.md#ref-cad-018
[REF-CAD-027]: ../BIBLIOGRAPHY.md#ref-cad-027
[REF-CAD-033]: ../BIBLIOGRAPHY.md#ref-cad-033
[REF-CAD-034]: ../BIBLIOGRAPHY.md#ref-cad-034
[REF-CAD-035]: ../BIBLIOGRAPHY.md#ref-cad-035
[REF-CAD-036]: ../BIBLIOGRAPHY.md#ref-cad-036
[REF-CAD-037]: ../BIBLIOGRAPHY.md#ref-cad-037
[REF-CAD-038]: ../BIBLIOGRAPHY.md#ref-cad-038
[REF-CAD-041]: ../BIBLIOGRAPHY.md#ref-cad-041
[REF-CAD-042]: ../BIBLIOGRAPHY.md#ref-cad-042
[REF-CAD-048]: ../BIBLIOGRAPHY.md#ref-cad-048
[REF-CAD-065]: ../BIBLIOGRAPHY.md#ref-cad-065
[REF-CAD-066]: ../BIBLIOGRAPHY.md#ref-cad-066
[REF-CAD-068]: ../BIBLIOGRAPHY.md#ref-cad-068
[REF-CAD-069]: ../BIBLIOGRAPHY.md#ref-cad-069
[REF-CAD-070]: ../BIBLIOGRAPHY.md#ref-cad-070
[REF-CAD-071]: ../BIBLIOGRAPHY.md#ref-cad-071
[REF-CAD-072]: ../BIBLIOGRAPHY.md#ref-cad-072
[REF-CAD-073]: ../BIBLIOGRAPHY.md#ref-cad-073
[REF-CAD-074]: ../BIBLIOGRAPHY.md#ref-cad-074
[REF-CAD-075]: ../BIBLIOGRAPHY.md#ref-cad-075
[REF-CAD-076]: ../BIBLIOGRAPHY.md#ref-cad-076
[REF-CAD-077]: ../BIBLIOGRAPHY.md#ref-cad-077
[REF-CAD-078]: ../BIBLIOGRAPHY.md#ref-cad-078
[REF-CAD-078A]: ../BIBLIOGRAPHY.md#ref-cad-078a
