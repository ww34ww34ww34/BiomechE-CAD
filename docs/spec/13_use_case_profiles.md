# BiomechE-CAD — Indication / Use-case Profile Functional Specification

**Version:** v0 — evidence-led  
**Date:** 2026-08-14  
**Status:** ACTIVE functional baseline  
**Architecture:** deliberately unspecified.  
**Evidence basis:** `docs/research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md` and `docs/BIBLIOGRAPHY.md`.

---

## 0. Purpose

Define a versioned context layer that determines **how CAD features and outcomes are interpreted**, without turning BiomechE-CAD into a diagnostic engine or hardcoding one orthotic doctrine.

```text
PATIENT / CLINICAL CONTEXT
          ↓
INDICATION PROFILE
          ↓
relevant features
relevant metrics
valid targets
warnings / non-transfer rules
          ↓
PRESCRIPTION / DESIGN / OUTCOME
```

A profile does not prescribe geometry automatically.

---

# 1. Core contract

```text
IndicationProfile
  profileId
  profileVersion
  displayName

  populationBoundary
  indicationBoundary
  excludedOrSeparateContexts[]

  relevantFeatureTypes[]
  metricBundle[]
  safetyRegionRules[]

  targetRules[]
    metric
    ROI
    criterion
    units
    protocolRef
    evidenceRef
    confidence

  requiredAcquisitionMetadata[]
  warnings[]
  nonTransferRules[]

  evidenceRefs[]
  evidenceConfidence
```

Every project stores the exact profile version used.

---

# 2. Initial P0 profile set

## 2.1 `DIABETIC_REULCERATION_PREVENTION`

Boundary:

```text
adult diabetes
+ neuropathy / loss of protective sensation or high ulcer risk
+ prevention / recurrence-prevention workflow
```

Key semantics:

- quantitative in-shoe pressure is a core outcome;
- pressure-relief targets are evidence/profile-bound;
- target ROI + adjacent/remote load transfer are reported;
- adherence/wear exposure is first-class;
- pressure-guided design/iteration is supported [GUIDE-IWGDF-2023; REF-CAD-004; REF-CAD-005; REF-CAD-068; REF-CAD-069].

### Active-ulcer guard

`ACTIVE_DIABETIC_PLANTAR_ULCER` is **not** silently treated as this prevention profile. For a neuropathic plantar forefoot/midfoot ulcer, IWGDF 2023 recommends a non-removable knee-high offloading device as first-choice healing intervention [GUIDE-IWGDF-2023, Offloading guideline].

The CAD may participate in later/downstream footwear design, but the profile UI/report must not present an insole alone as guideline-equivalent first-line treatment.

---

## 2.2 `MECHANICAL_METATARSALGIA`

Boundary:

```text
adult mechanical/central metatarsalgia
symptomatic forefoot / central MTH loading
```

Core features:

```text
MetatarsalPad
MetatarsalDome
MetatarsalBar
MetatarsalHeadRelief
ForefootCushioning
```

Core metrics:

```text
walking pain / PROM
PeakPressure
PTI
contact area
neighbor/transfer load
comfort / shoe fit
```

Placement remains landmark-relative and evidence-linked, never a universal hidden default [REF-CAD-011; REF-CAD-013; REF-CAD-041; REF-CAD-042; REF-CAD-072].

---

## 2.3 `FLEXIBLE_FLATFOOT`

Required subtype dimensions:

```text
adult vs pediatric
symptomatic vs asymptomatic
walking/general vs running/sport
```

Do not collapse these contexts.

Core features:

```text
Medial/LateralArchSupport
RearfootPost
ForefootPost
HeelCup
ArchMechanicalProfile
```

Core/optional outcomes:

```text
pain/function
regional pressure + PTI
midfoot contact area
structural arch measures
COP
rearfoot/ankle biomechanics [research]
comfort
```

A medial-midfoot pressure increase is not automatically failure; it may accompany increased support/contact and must be interpreted with contact area, symptoms and remote redistribution [REF-CAD-048]. Evidence remains heterogeneous and subtype-dependent [REF-CAD-027; REF-CAD-073; REF-CAD-078].

---

## 2.4 `PLANTAR_HEEL_PAIN`

Boundary:

```text
adult plantar heel pain / plantar-fasciitis-type context
```

Core features:

```text
HeelCup
HeelMechanicalRegion
HeelRelief
ArchSupport
rearfoot/whole-foot conformity
```

Core outcomes:

```text
pain
selected PROM/function
comfort / fit
heel PeakPressure / PTI / MeanPressure
ContactArea
```

Orthoses are interpreted as part of conservative/multimodal care, not as an isolated guaranteed treatment; pressure and pain/function outcomes remain separate [GUIDE-HEEL-PAIN-2023; REF-CAD-066; REF-CAD-074].

---

## 2.5 `SPORT_PERFORMANCE`

Boundary:

```text
healthy / athletic use
sport or running task
performance / comfort / load / injury-risk intent
```

Required activity metadata:

```text
sport
surface
speed / pace
shoe model / fit
training vs competition
session duration
external load when relevant
```

Possible outcomes:

```text
comfort
RPE
running economy / oxygen cost [research]
pace / time
pressure / PTI
COP
kinematics / kinetics [research]
injury incidence/exposure [longitudinal]
```

Do not equate biomechanical change, injury prevention and performance improvement. Running evidence is task-dependent and can include opposing effects across comfort, midfoot pressure and economy [REF-CAD-075; REF-CAD-076; REF-CAD-077; REF-CAD-079].

---

## 2.6 `GENERIC_CUSTOM_ORTHOSIS`

Safe fallback when no evidence profile is selected or available.

Enables validated CAD authoring features, but applies:

```text
NO disease-specific thresholds
NO automatic optimal presets
NO therapeutic-efficacy claim
```

Required:

```text
free-text design/clinical intent
author
selected ROI/metric if used
```

Evidence confidence: `DOMAIN-ONLY`.

---

# 3. Multi-profile projects

A person may have more than one clinically relevant context.

Store:

```text
attachedProfiles[]
activeInterpretationProfile
```

Every target/warning/preset records the profile that supplied it.

The system must never combine two thresholds into an anonymous global rule.

---

# 4. Target provenance

```text
ProfileTarget
  profileId
  profileVersion
  targetId

  population
  metric
  ROI
  criterion
  units

  acquisitionProtocol
  evidenceRef
  evidenceLocator
  confidence
```

A target copied into a project remains traceable even if the canonical profile is later updated.

---

# 5. Evidence-confidence vocabulary

```text
HIGH_NARROW_CONTEXT
MODERATE
EMERGING
MIXED
DOMAIN_ONLY
```

The confidence applies to the specific claim/target, not to the entire orthosis category.

---

# 6. Non-transfer policy

The first profile library must enforce at least:

```text
Diabetic re-ulceration target
  != mechanical-metatarsalgia target

Pediatric Sever heel evidence
  != adult plantar heel pain

Adult flatfoot walking evidence
  != asymptomatic flatfoot running evidence

Healthy runner biomechanical effect
  != treatment effect in symptomatic patient

Pressure reduction
  != pain/function improvement

Injury prevention signal
  != performance improvement
```

---

# 7. Profile selection must not diagnose

BiomechE-CAD may support:

```text
manual profile selection
candidate-profile suggestion [future]
```

but must not serialize an automatically suggested profile as a confirmed diagnosis without explicit clinician/user confirmation.

Pressure, scan morphology and symptom maps are input evidence, not diagnoses by themselves.

---

# 8. P0 UI semantics

Minimum UI behavior:

1. current profile(s) visibly displayed;
2. active interpretation profile identifiable;
3. source/evidence button for profile-specific targets;
4. warnings when profile boundary is violated;
5. no hidden automatic threshold transfer;
6. metric dashboard can be profile-oriented without deleting raw metrics;
7. switching profile shows which targets/presets become inactive.

---

# 9. Acceptance tests

## PROF-001 — version persistence
Profile ID/version round-trips through save/load/history.

## PROF-002 — evidence provenance
Every profile-derived target resolves to a canonical bibliography source.

## PROF-003 — threshold isolation
Switching from diabetic prevention to metatarsalgia/generic does not retain a diabetic threshold as active.

## PROF-004 — active-ulcer guard
An active neuropathic plantar forefoot/midfoot diabetic ulcer produces an explicit separate-pathway warning and does not present insole CAD as IWGDF first-line offloading.

## PROF-005 — multi-profile traceability
Every target/warning shows its originating profile.

## PROF-006 — age/population boundary
Pediatric evidence is not silently activated in adult profiles.

## PROF-007 — task boundary
Running evidence is not silently used to interpret walking outcomes.

## PROF-008 — generic neutrality
Generic profile contains no hidden disease-specific thresholds/presets.

## PROF-009 — measured outcome separation
Pressure, pain/PROM, adherence and clinical event outcomes remain separate measurements.

## PROF-010 — confidence visibility
Profile-derived recommendation/target can expose evidence confidence.

## PROF-011 — profile change audit
Changing the active profile is a versioned/auditable project event.

## PROF-012 — profile target snapshot
A target already applied to a design retains its source/profile version after a future library update.

---

# 10. Priority

## P0

- profile schema/versioning;
- six initial profiles;
- profile-bound targets/warnings;
- non-transfer guards;
- multi-profile provenance;
- generic neutral fallback;
- evidence refs and confidence.

## P1

- guided selection;
- profile dashboards;
- evidence-linked presets;
- PROM/adherence workflows;
- richer clinical-pathway warnings.

## P2

- candidate profile suggestions;
- adaptive longitudinal targets;
- continuous pressure/wearable integrations;
- predictive multi-objective support.

---

# 11. Product conclusion

The profile system is a **semantic safety and provenance layer**:

```text
same CAD feature
+ different population/context
= different interpretation
```

This layer is independent of OpenSubdiv/openNURBS or any future geometry kernel and should therefore be part of the product specification before architecture freeze.

---

## Bibliography links

[GUIDE-IWGDF-2023]: ../BIBLIOGRAPHY.md#guide-iwgdf-2023
[GUIDE-HEEL-PAIN-2023]: ../BIBLIOGRAPHY.md#guide-heel-pain-2023
[REF-CAD-004]: ../BIBLIOGRAPHY.md#ref-cad-004
[REF-CAD-005]: ../BIBLIOGRAPHY.md#ref-cad-005
[REF-CAD-011]: ../BIBLIOGRAPHY.md#ref-cad-011
[REF-CAD-013]: ../BIBLIOGRAPHY.md#ref-cad-013
[REF-CAD-027]: ../BIBLIOGRAPHY.md#ref-cad-027
[REF-CAD-041]: ../BIBLIOGRAPHY.md#ref-cad-041
[REF-CAD-042]: ../BIBLIOGRAPHY.md#ref-cad-042
[REF-CAD-048]: ../BIBLIOGRAPHY.md#ref-cad-048
[REF-CAD-066]: ../BIBLIOGRAPHY.md#ref-cad-066
[REF-CAD-068]: ../BIBLIOGRAPHY.md#ref-cad-068
[REF-CAD-069]: ../BIBLIOGRAPHY.md#ref-cad-069
[REF-CAD-073]: ../BIBLIOGRAPHY.md#ref-cad-073
[REF-CAD-074]: ../BIBLIOGRAPHY.md#ref-cad-074
[REF-CAD-075]: ../BIBLIOGRAPHY.md#ref-cad-075
[REF-CAD-076]: ../BIBLIOGRAPHY.md#ref-cad-076
[REF-CAD-077]: ../BIBLIOGRAPHY.md#ref-cad-077
[REF-CAD-078]: ../BIBLIOGRAPHY.md#ref-cad-078
[REF-CAD-079]: ../BIBLIOGRAPHY.md#ref-cad-079
