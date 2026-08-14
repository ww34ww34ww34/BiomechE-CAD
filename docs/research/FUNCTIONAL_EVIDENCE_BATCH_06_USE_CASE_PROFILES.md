# BiomechE-CAD — Functional Evidence Batch 06: Use-case / Population Profiles

**Date:** 2026-08-14  
**Status:** ACTIVE research baseline — `PROFILE-001`  
**Architecture:** intentionally out of scope / parked.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is authoritative.  
**Promoted specification:** `docs/spec/13_use_case_profiles.md`.

---

## 0. Research question

Can BiomechE-CAD use one universal interpretation layer for every custom foot orthosis?

**Conclusion: no.** The same CAD feature can have different intended effects, relevant outcomes, evidence strength and safety implications depending on population, diagnosis/status and activity.

The evidence therefore supports a versioned context layer:

```text
COMMON CAD CAPABILITIES
        +
INDICATION / USE-CASE PROFILE
        ↓
relevant features
relevant measurements
context-valid targets
warnings / non-transfer rules
```

A profile constrains interpretation; it does not automatically prescribe geometry and does not establish a diagnosis.

---

# 1. Profile schema derived from the evidence

```text
IndicationProfile
  id / version
  populationBoundary
  indicationBoundary
  excludedOrSeparateContexts[]

  relevantFeatures[]
  recommendedMeasurements[]
  optionalMeasurements[]

  outcomeTargets[]
    metric / ROI
    criterion / units
    protocol
    evidenceRef
    confidence

  safetyRegions[]
  requiredAcquisitionMetadata[]
  warnings[]
  nonTransferRules[]
  evidenceRefs[]
```

This model is promoted formally in `docs/spec/13_use_case_profiles.md`.

---

# 2. Diabetic offloading / re-ulceration prevention

## Boundary

```text
adult diabetes
+ peripheral neuropathy / loss of protective sensation or high ulcer risk
+ prevention / recurrence-prevention
+ therapeutic footwear / custom insole context
```

The IWGDF prevention guideline recommends properly fitting accommodative therapeutic footwear for moderate/high-risk people and therapeutic footwear with **demonstrated plantar-pressure relief during walking** to help prevent recurrent plantar ulceration [GUIDE-IWGDF-2023, Prevention guideline].

Pressure-informed design/optimization is supported by human studies and RCT evidence [REF-CAD-004; REF-CAD-005; REF-CAD-069].

## Critical non-transfer boundary: active ulcer

An active neuropathic plantar forefoot/midfoot diabetic ulcer is a different pathway. IWGDF 2023 recommends a **non-removable knee-high offloading device** as first-choice healing intervention; removable devices follow depending on contraindications/tolerance [GUIDE-IWGDF-2023, Offloading guideline].

Therefore:

```text
DIABETIC_REULCERATION_PREVENTION
!=
ACTIVE_DIABETIC_PLANTAR_ULCER
```

The CAD can participate in later therapeutic-footwear design, but must not present an insole as guideline-equivalent first-line treatment for that active-ulcer scenario.

## Metrics / data

Core:

```text
PeakPressure
PTI
ContactArea
target ROI + safety ring
regional redistribution
adherence / wear exposure
ulcer/lesion follow-up
```

Acquisition remains device/calibration/protocol-bound [REF-CAD-033; REF-CAD-034; REF-CAD-035; REF-CAD-036].

## Adherence

A multicenter RCT found that improved offloading did not significantly change recurrence in intention-to-treat, but did reduce recurrence in the high-adherence subgroup [REF-CAD-068, Abstract—Results/Conclusions]. A 2026 multicenter RCT showed improved adherence with personalized multimodal support [REF-CAD-071].

Continuous daily-life pressure feedback also has proof-of-concept randomized evidence [REF-CAD-070, pp. e308–e318], but belongs to future integration rather than core CAD P0.

**Confidence:** high for pressure-verification importance in defined high-risk prevention contexts; moderate-high for pressure-informed optimization; high that adherence modifies real-world effectiveness.

---

# 3. Mechanical metatarsalgia

## Boundary

```text
adult mechanical/central metatarsalgia
symptomatic forefoot / central metatarsal-head loading
```

A meta-analysis supports bespoke/custom orthoses for reducing pressure under central 2nd–4th metatarsal heads [REF-CAD-011, pp.111–118]. A broader review of forefoot pain reports pain improvement across several conditions but also shows why rheumatoid arthritis, hallux valgus and other forefoot disorders must not be silently merged into one homogeneous evidence group [REF-CAD-072, pp.1865–1875].

## Features

```text
MetatarsalPad / Dome / Bar
MetatarsalHeadRelief
ForefootCushioning
ForefootPost when intended
custom ROI offload
```

Placement is a measurable dose and is landmark/context dependent [REF-CAD-013; REF-CAD-041; REF-CAD-042].

## Outcomes

```text
walking pain / PROM
PeakPressure
PTI
contact area
adjacent load transfer
comfort / footwear fit
```

The 2026 forefoot review supports retaining peak pressure and PTI and emphasizes heterogeneity [REF-CAD-012].

**Non-transfer:** no diabetic ulcer thresholds; no universal “optimal” pad distance; other forefoot diagnoses require their own subcontext.

**Confidence:** moderate-high for central MTH pressure reduction; moderate for pain across heterogeneous conditions; moderate for placement sensitivity.

---

# 4. Flexible flatfoot

## Required subtype dimensions

```text
adult vs pediatric
symptomatic vs asymptomatic
walking/general vs running/sport
```

These populations are not interchangeable.

An adult review found weak/inconsistent evidence for routine provision [REF-CAD-027]. A newer network meta-analysis reports improvements in pain and selected structural/biomechanical outcomes, but included ages span children and young adults, so profile boundaries remain essential [REF-CAD-073].

## Features

```text
Medial/LateralArchSupport
RearfootPost
ForefootPost
HeelCup
ArchMechanicalProfile
```

## Outcomes

```text
pain / PROM
PeakPressure + PTI
midfoot contact area
navicular drop / structural arch measure
calcaneal pitch [import]
COP
rearfoot/ankle biomechanics [research]
comfort
```

A 2026 pressure meta-analysis found increased medial-midfoot pressure with insoles in pooled studies [REF-CAD-048]. This is not automatically a failure: midfoot can be the intended support/contact region. Interpret pressure with contact area, symptoms and remote redistribution.

In runners with asymptomatic flatfoot, arch-support-only and arch + medial-post configurations show different effects [REF-CAD-078]. Running findings therefore remain in a specific subtype.

**Confidence:** mixed/moderate overall; moderate for measurable redistribution; low-moderate for universal long-term prescription rules.

---

# 5. Adult plantar heel pain

The 2023 CPG places foot orthoses within conservative/multimodal management rather than as an isolated short-term intervention [GUIDE-HEEL-PAIN-2023].

A systematic review found a small medium-term pain effect and no clear custom-vs-prefabricated superiority [REF-CAD-066]. A newer RCT meta-analysis reports pain benefit but no significant advantage for function/walking ability, reinforcing separate outcome classes [REF-CAD-074].

## Features

```text
HeelCup / containment
HeelMechanicalRegion
HeelRelief
ArchSupport
whole-foot/rearfoot conformity
```

## Outcomes

```text
pain
selected PROM/function
comfort / fit
heel PeakPressure / MeanPressure / PTI
ContactArea
plantar-fascia/heel-pad measures [optional research/clinical import]
```

Pressure and PROM outcomes remain separate [REF-CAD-018; REF-CAD-065].

**Non-transfer:** pediatric Sever evidence is not an adult rule; custom is not intrinsically superior; diabetic pressure thresholds are not heel-pain targets; pressure reduction alone does not establish pain/function benefit.

**Confidence:** moderate for pain as part of conservative management; low-moderate for specific geometry/material superiority; mixed for function.

---

# 6. Sport / performance

## Boundary

```text
healthy / athletic user
sport-specific task
comfort / load / biomechanics / performance / injury-risk intent
```

This is not a disease-treatment profile.

A 2024 meta-analysis of running studies found task-specific pressure/kinematic changes and improved perceived comfort with custom orthoses, but also an unfavorable pooled running-economy/perceived-exertion effect for custom orthoses in the included evidence [REF-CAD-075, pp.240–258].

An injury-prevention meta-analysis found signals for reduced overall injury and stress-fracture risk but not all injury categories, with heterogeneous trial quality [REF-CAD-076]. A later bone-stress-injury review judged orthosis evidence low quality and heavily influenced by military populations [REF-CAD-079].

Footwear comfort has an association with running economy in a separate meta-analysis [REF-CAD-077], but this does not imply every custom orthosis improves performance.

## Required metadata

```text
sport
surface
speed / pace
shoe model / fit
training vs competition
session duration
external load when relevant
```

## Outcomes

```text
comfort
RPE
running economy / oxygen cost [research]
pace / time
pressure / PTI
COP
kinematics / kinetics [research]
injury exposure / incidence
```

**Non-transfer:** biomechanical change != injury prevention != performance improvement. Healthy-runner findings do not become treatment rules for symptomatic patients.

**Confidence:** moderate for task-specific biomechanical/pressure and comfort effects; low-moderate for generalized injury prevention; mixed for performance benefit.

---

# 7. Generic custom orthosis

`GENERIC_CUSTOM_ORTHOSIS` is the neutral fallback when no evidence profile is selected or the indication is outside current evidence packs.

It enables validated CAD features but applies:

```text
NO disease-specific thresholds
NO hidden evidence-derived optimum
NO therapeutic efficacy claim
```

Required provenance:

```text
clinical/design intent
free-text rationale
author
selected ROI/metric if any
```

**Confidence:** `DOMAIN-ONLY`.

---

# 8. Cross-profile rules derived from the research

1. Multiple profiles may be attached to one patient/project, but every target/warning records its originating profile.
2. Thresholds never inherit silently across profiles.
3. Evidence-linked presets expose population, protocol, source and unknown parameters.
4. Pressure/scan/symptom measurements do not themselves establish diagnoses.
5. Active pathology can redirect the clinical pathway and trigger a non-transfer guard.
6. Model evidence may justify keeping a design parameter explicit but cannot silently become a therapeutic target.
7. Pediatric, adult, walking, running, symptomatic and asymptomatic evidence remain separable.
8. Pressure, PROM, adherence and clinical-event outcomes remain distinct observations.

---

# 9. Initial profile compatibility matrix

| Capability/outcome | Diabetes prevention | Mechanical metatarsalgia | Flexible flatfoot | Heel pain | Sport | Generic |
|---|---:|---:|---:|---:|---:|---:|
| Quantitative pressure | **Core** | **Core** | useful | useful | useful | optional |
| PTI | **Core** | **Core** | useful | useful | useful | optional |
| Target + safety region | **Core** | **Core** | useful | useful | useful | optional |
| Metatarsal elements | frequent | **Core** | optional | optional | optional | available |
| Arch prescription | frequent | optional | **Core** | frequent | frequent | available |
| Heel containment | as indicated | optional | frequent | **Core** | frequent | available |
| Regional cushioning | **Core** | frequent | optional | **Core** | frequent | available |
| Pain/PROM | clinical follow-up | **Core** | core if symptomatic | **Core** | secondary | optional |
| Adherence | **Core** | useful | useful | useful | useful | optional |
| Performance/economy | no | no | sport subtype | no | **Core/research** | no |
| Disease-specific threshold | context-bound | none universal | none universal | none universal | none universal | none |

---

# 10. Acceptance implications

The evidence justifies the `PROF-001..PROF-012` acceptance semantics now formalized in `docs/spec/13_use_case_profiles.md`, including:

```text
profile/version persistence
evidence provenance
threshold isolation
active-diabetic-ulcer pathway guard
multi-profile traceability
population/age boundary
activity boundary
generic-profile neutrality
pressure/PROM/adherence separation
confidence visibility
profile-change audit
profile-target snapshot
```

---

# 11. Research conclusion

The scientifically safer abstraction is:

```text
CAD FEATURE
+ INDICATION PROFILE
+ MEASUREMENT PROTOCOL
+ EVIDENCE CONTEXT
= INTERPRETABLE PRESCRIPTION / OUTCOME
```

not:

```text
CAD FEATURE = same meaning for every patient
```

The next evidence block should therefore address **PROM / comfort / fit / adherence** as cross-profile outcome objects, followed by material durability/manufacturing evidence.

---

## Bibliography links

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
[REF-CAD-079]: ../BIBLIOGRAPHY.md#ref-cad-079
