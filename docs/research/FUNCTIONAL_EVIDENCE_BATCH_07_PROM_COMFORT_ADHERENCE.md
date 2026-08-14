# BiomechE-CAD — Functional Evidence Batch 07: PROM / Comfort / Fit / Adherence

**Date:** 2026-08-14  
**Status:** ACTIVE research baseline — `PROM-001`  
**Architecture:** intentionally out of scope / parked.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is authoritative for source metadata and locators.

---

## 0. Purpose

BiomechE-CAD needs to connect a design revision not only to pressure/geometric outcomes but also to the patient's experienced outcome.

The key conclusion of this batch is:

> **Pain, function, comfort, fit/usability, satisfaction and adherence are distinct constructs. They must not be collapsed into one proprietary “BiomechE score”.**

The foot/ankle literature uses many PROMs inconsistently: a 2025 systematic review found 125 different PROMs across 1,553 articles and explicitly called for greater consistency in the use of validated instruments [REF-CAD-026, Abstract—Results/Conclusion].

COSMIN recommends selecting an instrument by the construct to be measured, evidence for measurement properties and feasibility rather than by popularity alone [GUIDE-COSMIN, `select best measurement instrument`]. FDA device guidance similarly emphasizes that a PRO instrument should be fit for purpose in its intended evaluation context [GUIDE-FDA-PRO-DEVICE-2022].

Therefore BiomechE-CAD needs an **instrument registry + measurement model**, not one built-in universal questionnaire.

---

# 1. First choose the construct, then the instrument

The product must separate at least:

```text
PAIN
FUNCTION / ACTIVITY
FOOT-SPECIFIC HEALTH / QUALITY OF LIFE
COMFORT
FIT / USABILITY
SATISFACTION / PERCEIVED BENEFIT
ADHERENCE / WEAR EXPOSURE
```

A reduction in plantar pressure does not prove pain relief; pain relief does not prove improved function; a comfortable orthosis is not necessarily worn for the required exposure; wearing time does not prove that it was worn during the relevant weight-bearing activity.

This separation is consistent with the existing evidence-led profiles and with literature in which pressure and patient-reported outcomes can rank interventions differently [REF-CAD-016; REF-CAD-018; REF-CAD-044; REF-CAD-074; REF-CAD-075].

---

# 2. PROM instrument registry — required P0 infrastructure

A canonical definition should be versioned:

```text
PROMInstrumentDefinition
  instrumentId
  canonicalName
  version
  language
  culturalAdaptation
  respondentType
  targetPopulation / validationContexts[]

  domains[]
  itemCount
  recallPeriod
  responseScale
  scoreDirection
  scoringAlgorithmVersion

  measurementPropertyEvidence[]
  MID_MCIDs[]
  MDC_SEM[]

  licenseStatus
  redistributionStatus
  sourceRefs[]
```

## 2.1 Why version and language are first-class

The original FFI is a 23-item self-administered measure of foot pain, disability and activity restriction [REF-CAD-081, Abstract]. A recent systematic review found many cross-cultural adaptations and specifically emphasized that measurement quality varies by version/adaptation [REF-CAD-082, Abstract—Results/Conclusion].

For Italy there are already useful candidates rather than a need to invent a score:

- `17-IFFI` — validated Italian modified Foot Function Index [REF-CAD-084];
- `FAAM-I/ADL` — validated Italian ADL module [REF-CAD-085];
- `EFAS Score` — a short multilingual PROM whose development included Italian validation [REF-CAD-086].

The existence of these tools **does not select one globally**. Their constructs, populations, burden and measurement properties differ.

---

# 3. Candidate PROM families relevant to BiomechE-CAD

## 3.1 Foot Function Index

The FFI was designed for pain, disability and activity restriction [REF-CAD-081]. It is useful when those constructs match the selected profile and language/version is supported.

Product consequence:

```text
instrument = FFI-family
version = exact adaptation
language = exact language
subscale scores retained separately
```

Do not create a generic `FFI score` without version metadata.

## 3.2 Foot Health Status Questionnaire

The original FHSQ has 13 foot-specific items covering pain, function, footwear and general foot health [REF-CAD-080]. This multidomain structure is attractive for orthosis follow-up because it explicitly contains a footwear-related domain, but the suitability of any translation/version must be checked for the actual population.

A plantar-heel-pain study has revised minimal-important-difference estimates for VAS and FHSQ in that specific condition [REF-CAD-093]. This illustrates a product rule:

```text
MID / MCID
!= instrument-wide universal constant
```

It belongs to:

```text
instrument version
+ domain
+ population
+ baseline/context
+ estimation method
+ source
```

## 3.3 Foot and Ankle Ability Measure

FAAM contains separate ADL and Sport subscales and was developed as a responsive functional measure for lower-leg/foot/ankle musculoskeletal disorders [REF-CAD-083]. The original study reported different MDC/MCID values for ADL and Sport, again demonstrating that interpretation belongs to an instrument/subscale/context rather than to the application globally.

For Italy, `FAAM-I/ADL` has published validation data [REF-CAD-085].

## 3.4 EFAS Score

The EFAS Score is a short 6-item multilingual PROM validated across several European languages including Italian [REF-CAD-086]. It is a potentially useful low-burden candidate for a general foot/ankle follow-up profile.

The article states that versions are freely available through EFAS, but BiomechE-CAD must still verify the **current** redistribution/license terms before bundling item text or scoring assets in the product.

---

# 4. PROM measurement object

A completed measurement should preserve:

```text
PROMMeasurement
  measurementId
  patientId
  instrumentId
  instrumentVersion
  language

  timestamp
  recallWindow
  administrationMode
  administrator [self / clinician-assisted / remote]

  rawResponsesRef [when legally/operationally retained]
  domainScores[]
  totalScore [only if instrument defines one]
  scoreDirection

  missingItemState
  scoringWarnings[]

  indicationProfileId
  designRevisionId
  manufacturingRevisionId
  orthosisSide
  footwearContext
  wearExposureContext

  interpretationRef
  evidenceRefs[]
```

### Rule

Never recompute old scores with a silently changed scoring algorithm. A scoring algorithm is versioned just like geometry/manufacturing logic.

---

# 5. Comfort is a separate outcome class

Comfort literature is heterogeneous and task-dependent [REF-CAD-089, Abstract—Results/Conclusion]. Simple VAS can be reliable, but the result depends on protocol and repeated/control conditions [REF-CAD-087]. Another study comparing VAS, Likert and ranking scales found different reliability characteristics and an approximately 10 mm meaningful change on a 100-mm VAS in that specific experimental context [REF-CAD-088].

Therefore:

```text
10 mm comfort VAS
!= universal BiomechE threshold
```

## 5.1 ComfortAssessment

```text
ComfortAssessment
  timestamp
  scaleType
  scaleMin / scaleMax
  scoreDirection

  overallComfort
  dimensions[]

  activity
  duration
  footwear
  surface
  speed / intensity [when relevant]
  fresh / fatigued [when relevant]

  designRevisionId
  manufacturingRevisionId
```

## 5.2 Multidimensional comfort

Running-footwear research provides an example of a validated task-specific multidimensional instrument. RUN-CAT uses dimensions including heel cushioning, stability, forefoot cushioning and forefoot flexibility [REF-CAD-090, Abstract—Methods/Results].

This supports a general product capability for multidimensional comfort, but **RUN-CAT must not be relabelled as a generic orthosis comfort instrument**.

BiomechE-CAD may expose orthosis-specific comfort dimensions such as:

```text
heel cushioning
arch support/cushioning
forefoot cushioning
stability
edge/border irritation
bulk / shoe-space perception
thermal perception [future]
```

as configurable research/clinical fields unless a validated named instrument is explicitly selected.

---

# 6. Fit and usability are distinct from comfort

`FIT` means physical accommodation and practical usability, not merely subjective pleasantness.

Suggested orthosis/footwear usability dimensions:

```text
shoe fit / available volume
slippage
edge pressure / irritation
stability
weight/bulk perception
donning / doffing
compatibility with intended footwear
perceived benefit
```

These should be recorded separately from pain/function PROM scores.

A product can therefore report:

```text
Pain improved
Function stable
Comfort high
Fit poor in work shoe
Adherence low
```

without forcing those observations into one contradictory total score.

---

# 7. Adherence is not simply “hours worn”

This is especially important for high-risk diabetic profiles.

A systematic review found objective methods such as temperature sensors and activity monitors more usable/accurate for therapeutic-footwear adherence than subjective methods, which are vulnerable to response bias and missing data [REF-CAD-091, Abstract—Results/Conclusion].

A validation study found that **proportion of weight-bearing time / daily steps in prescribed footwear** correlated strongly with a reference adherence measure, while subjective wearing-time recall was substantially weaker [REF-CAD-092, Abstract—Results/Conclusions].

This reinforces evidence already captured in the diabetic profile that adherence can materially modify real-world clinical effectiveness [REF-CAD-068; REF-CAD-071].

## 7.1 AdherenceMeasurement

```text
AdherenceMeasurement
  method
    SELF_REPORT
    TEMPERATURE_SENSOR
    ACTIVITY_MONITOR
    COMBINED_OBJECTIVE

  observationStart
  observationEnd

  wearTime_minutes
  weightBearingTime_minutes [if available]
  stepsTotal [if available]
  stepsWithDevice [if available]

  adherenceRatio
  adherenceDenominator
    TIME_OUT_OF_BED
    WEIGHT_BEARING_TIME
    STEPS
    PRESCRIBED_SESSION

  indoorOutdoorContext [if known]
  workSportHomeContext [if known]

  sensorIds[]
  dataQuality
  missingData

  designRevisionId
  manufacturingRevisionId
```

### Critical rule

```text
4 h/day worn
```

cannot be compared directly with:

```text
80% of weight-bearing steps worn
```

without retaining the adherence definition/denominator.

---

# 8. PatientExperienceBundle

For a design revision, the software should be able to display parallel outcomes:

```text
PatientExperienceBundle
  pain
  function
  footHealth / qualityOfLife
  comfort
  fitUsability
  satisfaction
  adherence
```

Example:

```text
Revision 14

PeakPressure MTH2-4       -24%
PTI                       -19%
FFI pain                  improved
FAAM ADL                  unchanged
Overall comfort           82/100
Arch comfort              61/100
Fit in work shoe          poor
Adherence                 46% of weight-bearing steps
```

The point is not to calculate an average of those numbers. The point is to preserve the multidimensional result.

---

# 9. No universal BiomechE outcome score

The current evidence argues against creating:

```text
BiomechE Score = 87 / 100
```

from arbitrary weighted combinations of pressure, PROM, comfort and adherence.

The 2025 foot/ankle PROM review already demonstrates substantial instrument heterogeneity [REF-CAD-026]. COSMIN explicitly recommends selection according to construct, measurement properties and feasibility [GUIDE-COSMIN].

Therefore any future composite score must be:

```text
named
versioned
validated
profile-specific
transparent in weighting
supported by measurement-property evidence
```

and remains **P2 research** until validated.

---

# 10. Licensing / questionnaire-content rule

BiomechE-CAD may store instrument definitions and measurements only with explicit provenance.

Before embedding question text, translations or proprietary scoring assets:

```text
verify copyright owner
verify permitted use
verify redistribution rights
verify commercial-software rights
verify translation rights
record license version/date
```

A bibliographic publication validating an instrument does **not automatically grant permission to redistribute its questionnaire text**.

This is a product/legal governance rule, not a clinical claim.

---

# 11. P0 / P1 / P2 consequence

## P0

```text
PROM instrument registry schema
version + language + scoring-version provenance
PROMMeasurement with domain scores
pain/function/comfort/fit/adherence as distinct classes
design/manufacturing revision linkage
manual/self-report adherence recording with explicit denominator
instrument license-status metadata
context-specific MID/MCID/MDC data model
```

## P1

```text
built-in validated instruments after licensing review
profile-recommended instrument sets
longitudinal PROM dashboard
comfort multidimensional workflow
objective sensor import for adherence
wear-exposure visualization
MID/MCID interpretation with warnings
remote follow-up questionnaires
```

## P2 / R&D

```text
PROMIS/CAT integrations
adaptive questionnaires
sensor-driven adherence coaching
joint pressure + PROM + adherence prediction
validated profile-specific composite endpoints
```

---

# 12. Acceptance semantics

```text
PROM-001  construct is declared before instrument selection
PROM-002  instrument version/language survives save/load/export
PROM-003  subscale/domain scores are not silently collapsed
PROM-004  score direction and units/range are explicit
PROM-005  scoring algorithm is versioned
PROM-006  PROM measurement links to exact design/manufacturing revision
PROM-007  recall period and administration mode are preserved
PROM-008  MID/MCID/MDC carries instrument/domain/population/source context
PROM-009  comfort remains separate from pain and function
PROM-010  comfort assessment preserves activity/protocol context
PROM-011  fit/usability remains separate from comfort
PROM-012  adherence method and denominator are explicit
PROM-013  subjective and objective adherence are not treated as equivalent
PROM-014  no universal hidden BiomechE composite score
PROM-015  questionnaire text/scoring assets cannot ship without license-status review
PROM-016  Italian/localized instrument is identified by exact validated adaptation
PROM-017  missing responses/scoring warnings survive provenance
PROM-018  old measurements remain reproducible after instrument/scoring updates
```

---

# 13. Evidence gaps / caution

- No single PROM is established as universally best for all BiomechE-CAD profiles.
- The most commonly used instrument is not necessarily the best validated instrument [REF-CAD-026; GUIDE-COSMIN].
- Comfort measurement is highly protocol/task dependent [REF-CAD-087; REF-CAD-089].
- Published MID/MCID values are not portable by default across populations, languages or instrument versions [REF-CAD-083; REF-CAD-093].
- Objective adherence evidence is strongest in therapeutic-footwear/diabetic contexts; its exact implementation in generic orthosis populations needs separate validation [REF-CAD-091; REF-CAD-092].
- Licensing/redistribution must be checked independently of psychometric validity.

---

# 14. Current conclusion

BiomechE-CAD should treat patient experience with the same traceability discipline already applied to geometry and pressure:

```text
DESIGN REVISION
      ↓
MANUFACTURED DEVICE
      ↓
WEAR EXPOSURE
      ↓
PAIN / FUNCTION / COMFORT / FIT
      ↓
ADHERENCE
      ↓
FOLLOW-UP / REVISION
```

The next evidence batch should address **material durability + manufacturing**, because clinical experience and adherence can only be interpreted correctly when the actual produced device and its aging/material state are traceable.

---

## Bibliography links

[GUIDE-COSMIN]: ../BIBLIOGRAPHY.md#guide-cosmin
[GUIDE-FDA-PRO-DEVICE-2022]: ../BIBLIOGRAPHY.md#guide-fda-pro-device-2022
[REF-CAD-016]: ../BIBLIOGRAPHY.md#ref-cad-016
[REF-CAD-018]: ../BIBLIOGRAPHY.md#ref-cad-018
[REF-CAD-026]: ../BIBLIOGRAPHY.md#ref-cad-026
[REF-CAD-044]: ../BIBLIOGRAPHY.md#ref-cad-044
[REF-CAD-068]: ../BIBLIOGRAPHY.md#ref-cad-068
[REF-CAD-071]: ../BIBLIOGRAPHY.md#ref-cad-071
[REF-CAD-074]: ../BIBLIOGRAPHY.md#ref-cad-074
[REF-CAD-075]: ../BIBLIOGRAPHY.md#ref-cad-075
[REF-CAD-080]: ../BIBLIOGRAPHY.md#ref-cad-080
[REF-CAD-081]: ../BIBLIOGRAPHY.md#ref-cad-081
[REF-CAD-082]: ../BIBLIOGRAPHY.md#ref-cad-082
[REF-CAD-083]: ../BIBLIOGRAPHY.md#ref-cad-083
[REF-CAD-084]: ../BIBLIOGRAPHY.md#ref-cad-084
[REF-CAD-085]: ../BIBLIOGRAPHY.md#ref-cad-085
[REF-CAD-086]: ../BIBLIOGRAPHY.md#ref-cad-086
[REF-CAD-087]: ../BIBLIOGRAPHY.md#ref-cad-087
[REF-CAD-088]: ../BIBLIOGRAPHY.md#ref-cad-088
[REF-CAD-089]: ../BIBLIOGRAPHY.md#ref-cad-089
[REF-CAD-090]: ../BIBLIOGRAPHY.md#ref-cad-090
[REF-CAD-091]: ../BIBLIOGRAPHY.md#ref-cad-091
[REF-CAD-092]: ../BIBLIOGRAPHY.md#ref-cad-092
[REF-CAD-093]: ../BIBLIOGRAPHY.md#ref-cad-093
