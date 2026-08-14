# BiomechE-CAD — PROM, Comfort, Fit and Adherence Functional Specification

**Status:** ACTIVE functional baseline v0  
**Date:** 2026-08-14  
**Architecture:** implementation-neutral.  
**Evidence basis:** `docs/research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md` and `docs/BIBLIOGRAPHY.md`.

---

## 1. Scope

This specification defines how BiomechE-CAD records and interprets patient-reported and real-world use outcomes linked to an orthosis revision.

The system SHALL keep the following concepts separate:

```text
pain
function/activity
foot-specific health / quality of life
comfort
fit/usability
satisfaction/perceived benefit
adherence/wear exposure
```

There SHALL NOT be a hidden global composite `BiomechEScore` in P0/P1.

---

## 2. PROM instrument registry

```text
PROMInstrumentDefinition
  instrumentId: string
  canonicalName: string
  version: string
  language: string
  culturalAdaptationId?: string

  respondentType: enum
  validationContexts[]
  domains[]
  itemCount: int
  recallPeriod?: DurationOrText

  responseScale
  scoreRange
  scoreDirection
  scoringAlgorithmVersion

  interpretationRules[]
    type: MID | MCID | MDC | SEM | OTHER
    domain
    value/range
    populationContext
    estimationMethod?
    evidenceRef

  licensing
    status: UNKNOWN | REVIEWED | CLEARED | RESTRICTED
    owner?
    allowedUse?
    redistributionAllowed?
    commercialUseAllowed?
    reviewedAt?

  evidenceRefs[]
```

### Requirements

- Exact version and language SHALL be preserved.
- A translated/modified instrument SHALL be a distinct definition unless equivalence is explicitly established.
- Score direction SHALL be explicit (`higher=better`, `higher=worse`, or domain-specific).
- Interpretation values such as MID/MCID/MDC SHALL carry context and source; they SHALL NOT be global constants.
- Questionnaire item text SHALL NOT be bundled when redistribution rights are unknown or restricted.

---

## 3. PROM measurement

```text
PROMMeasurement
  measurementId
  patientId

  instrumentId
  instrumentVersion
  language
  scoringAlgorithmVersion

  timestamp
  recallWindow
  administrationMode
  administrator

  rawResponsesRef?
  domainScores[]
  totalScore?
  missingItemState
  scoringWarnings[]

  indicationProfileId?
  designRevisionId
  manufacturingRevisionId
  side

  footwearContext?
  activityContext?
  wearExposureContext?

  evidenceRefs[]
```

### Invariants

1. A saved measurement SHALL remain reproducible after future changes to the instrument/scoring registry.
2. Old measurements SHALL NOT be silently rescored with a newer algorithm.
3. Domain/subscale scores SHALL remain individually queryable.
4. A total score SHALL exist only if the selected instrument defines one.
5. Missing responses and any imputation/scoring warnings SHALL be preserved.

---

## 4. Candidate instrument policy

BiomechE-CAD does not select one universal PROM.

For Italian deployments, candidate validated families already identified include:

```text
17-IFFI
FAAM-I/ADL
EFAS Score
```

[REF-CAD-084; REF-CAD-085; REF-CAD-086]

Other candidates such as FFI, FHSQ and FAAM may be used where the exact language/version and population context are appropriate [REF-CAD-080; REF-CAD-081; REF-CAD-083].

Instrument selection SHOULD follow a fit-for-purpose process based on construct, measurement properties, interpretability and feasibility [GUIDE-COSMIN; GUIDE-FDA-PRO-DEVICE-2022].

---

## 5. Comfort assessment

Comfort SHALL be modelled independently from pain/function PROMs.

```text
ComfortAssessment
  assessmentId
  timestamp

  scaleType
  scaleMin
  scaleMax
  scoreDirection

  overallComfort?
  dimensions[]
    dimensionId
    value

  activity
  duration?
  surface?
  speedOrIntensity?
  footwearId/profile?
  fatigueState?

  designRevisionId
  manufacturingRevisionId
```

### Suggested configurable dimensions

These are product fields unless a validated named instrument is selected:

```text
overall comfort
heel cushioning
arch comfort/support
forefoot cushioning
stability
border/edge irritation
bulk / shoe-space perception
```

Validated task-specific instruments such as RUN-CAT MAY be registered as named instruments for their intended context; they SHALL NOT be relabelled as generic orthosis scores [REF-CAD-090].

Comfort thresholds from a specific study/protocol SHALL NOT become global defaults [REF-CAD-087; REF-CAD-088; REF-CAD-089].

---

## 6. Fit / usability assessment

```text
FitUsabilityAssessment
  timestamp

  footwearContext
  fitRating?
  slippageRating?
  edgeIrritationRating?
  stabilityRating?
  bulkRating?
  donningDoffingRating?
  compatibilityRating?
  perceivedBenefitRating?
  notes?

  designRevisionId
  manufacturingRevisionId
```

Fit/usability SHALL remain separate from comfort because a device may be comfortable during a short test but impractical in the prescribed footwear or daily setting.

---

## 7. Satisfaction / perceived benefit

```text
SatisfactionAssessment
  timestamp
  overallSatisfaction
  perceivedBenefit?
  willingnessToContinue?
  expectationMatch?
  notes?
  designRevisionId
  manufacturingRevisionId
```

Satisfaction SHALL NOT be substituted for pain/function outcomes or adherence.

---

## 8. Adherence / wear exposure

```text
AdherenceMeasurement
  measurementId
  method
    SELF_REPORT
    TEMPERATURE_SENSOR
    ACTIVITY_MONITOR
    COMBINED_OBJECTIVE
    OTHER

  observationStart
  observationEnd

  wearTimeMinutes?
  weightBearingTimeMinutes?
  stepsTotal?
  stepsWithDevice?

  adherenceRatio?
  denominator
    TIME_OUT_OF_BED
    WEIGHT_BEARING_TIME
    STEPS
    PRESCRIBED_SESSION
    OTHER

  indoorOutdoorContext?
  workSportHomeContext?

  sensorIds[]
  sourceFiles[]
  qualityFlags[]
  missingDataState

  designRevisionId
  manufacturingRevisionId
```

### Adherence rules

- Method and denominator SHALL always be explicit.
- `hours/day` SHALL NOT be treated as equivalent to `% weight-bearing time` or `% steps with device`.
- Objective and subjective adherence SHALL remain distinguishable.
- When both footwear temperature sensing and activity sensing are available, the system SHOULD support exposure-normalized adherence.
- Diabetic high-risk profiles SHOULD prefer objective adherence data when feasible because current evidence shows substantially better validity than subjective recall [REF-CAD-091; REF-CAD-092].

---

## 9. Patient experience bundle

```text
PatientExperienceBundle
  designRevisionId
  manufacturingRevisionId

  painMeasurements[]
  functionMeasurements[]
  footHealthMeasurements[]
  comfortAssessments[]
  fitUsabilityAssessments[]
  satisfactionAssessments[]
  adherenceMeasurements[]
```

The UI/report SHALL present dimensions in parallel rather than forcing an arithmetic average.

Example:

```text
Pressure target        improved
Pain                   improved
Function               unchanged
Comfort                good
Fit in work footwear   poor
Adherence              low
```

This is a valid multidimensional outcome and SHALL not be simplified to one green/red status without an explicit profile rule.

---

## 10. Longitudinal comparison

A comparison SHALL require:

```text
same or explicitly mapped instrument/version
compatible domain definition
known score direction
known timepoints
linked orthosis revisions
```

If instrument versions differ, the system SHALL mark the comparison as:

```text
DIRECTLY_COMPARABLE
MAPPED_WITH_VALIDATED_CROSSWALK
NOT_DIRECTLY_COMPARABLE
```

No crosswalk SHALL be generated ad hoc without validation evidence.

---

## 11. Interpretation rules

```text
InterpretationRule
  instrumentId
  instrumentVersion
  domain
  populationProfile
  ruleType
    MID
    MCID
    MDC
    SEM
    THRESHOLD
  value/range
  direction
  evidenceRef
  confidence
```

The application SHALL distinguish:

```text
statistical/measurement change
clinically important change
patient-perceived change
```

and SHALL not assume they are equivalent.

---

## 12. Licensing / localization

Before shipping a named instrument:

```text
licenseStatus == CLEARED
```

SHALL be required for any questionnaire text/scoring asset that requires redistribution permission.

The software SHOULD maintain:

```text
instrument owner
license/terms reference
allowed territories/languages
commercial-use status
translation provenance
last review date
```

A translated instrument SHALL retain the exact validated adaptation identity.

---

## 13. Priority

### P0

- instrument registry schema;
- version/language/scoring provenance;
- generic PROM measurement storage;
- domain scores;
- design/manufacturing linkage;
- comfort / fit / satisfaction / adherence separate objects;
- adherence denominator/method;
- interpretation-rule schema;
- licensing metadata;
- import/export/report serialization.

### P1

- selected built-in instruments after license review;
- profile-recommended instrument sets;
- longitudinal dashboard;
- remote questionnaires;
- objective adherence imports;
- MID/MCID/MDC interpretation warnings;
- wear-exposure dashboard.

### P2

- computer-adaptive PROM integrations;
- sensor-driven adherence coaching;
- validated crosswalks between instruments;
- research composite endpoints;
- prediction linking pressure/design/adherence/PROM.

---

## 14. Acceptance tests

```text
PROM-001  construct-before-instrument rule
PROM-002  version/language round-trip
PROM-003  domain-score persistence
PROM-004  score-direction persistence
PROM-005  scoring-version reproducibility
PROM-006  exact revision linkage
PROM-007  recall/admin context persistence
PROM-008  interpretation provenance
PROM-009  comfort != pain/function
PROM-010  comfort protocol persistence
PROM-011  fit != comfort
PROM-012  adherence method/denominator persistence
PROM-013  objective != subjective adherence
PROM-014  no hidden universal composite
PROM-015  licensing gate
PROM-016  validated localization identity
PROM-017  missing-item warnings persist
PROM-018  old score reproducibility
PROM-019  longitudinal comparison compatibility status
PROM-020  report shows multidimensional outcomes without silent averaging
```

---

## 15. Bibliography

[GUIDE-COSMIN]: ../BIBLIOGRAPHY.md#guide-cosmin
[GUIDE-FDA-PRO-DEVICE-2022]: ../BIBLIOGRAPHY.md#guide-fda-pro-device-2022
[REF-CAD-080]: ../BIBLIOGRAPHY.md#ref-cad-080
[REF-CAD-081]: ../BIBLIOGRAPHY.md#ref-cad-081
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
