# 12 — Reporting and Traceability Contract

**Status:** FROZEN semantic reporting baseline v1  
**Date:** 2026-08-15  
**Scope:** kernel-independent report, evidence, provenance, privacy and historical reproducibility semantics for BiomechE-CAD.  
**Depends on:** Functional Specification v2, Project Schema v0, BiomechE Integration v1, Analysis/QC v0, Material/Manufacturing specs, PROM/Adherence spec.  

> A report is an immutable derived artifact over exact source entities. It is never the authoritative replacement for the project data that generated it.

---

## 1. Purpose

BiomechE-CAD must be able to answer, years after a design/report was generated:

```text
which patient/case context was represented?
which side?
which exact DesignRevision?
which source acquisitions and registrations?
which BiomechE KPI definitions/versions?
which ROI/profile/evidence versions?
which material/manufacturing run/artifact/physical part?
which QC state?
which measured/predicted outcomes?
which PROM/comfort/fit/adherence records?
which warnings and comparability state?
which software generated the report?
what changed after the report was generated?
```

Biomedical provenance literature emphasizes origin/history metadata as necessary for quality verification, process validation and reproducibility [REF-CAD-111, Abstract—Background]. FAIR likewise requires qualified references among data/metadata and detailed provenance [REF-CAD-113, Box 2, I3/R1.2].

The product therefore treats reporting as a reproducible provenance activity, not merely PDF layout.

---

## 2. Authority model

```text
Project entities / immutable assets     AUTHORITATIVE DATA
Report semantic source manifest         DERIVATION SNAPSHOT
Report PDF/HTML/charts                   PRESENTATION ARTIFACTS
```

Rules:

1. A chart never becomes the numeric source of truth.
2. A PDF number is not re-parsed later to reconstruct an outcome when the underlying measurement exists.
3. A report generated from revision N remains tied to N after N+1 is created.
4. Reissuing/regenerating creates a new report artifact; it does not mutate historical bytes under the old identity.

---

## 3. Report types

Project Schema v0 already defines:

```text
DESIGN
MANUFACTURING_QC
OUTCOME
TRACEABILITY
OTHER
```

Recommended P0 semantics:

### 3.1 DESIGN

Documents the exact prescription/design revision and its source evidence.

### 3.2 MANUFACTURING_QC

Documents design->profile->run->artifact->physical part, required QC and acceptance/disposition.

### 3.3 OUTCOME

Documents protocol-bound measured/predicted outcomes, comparisons and patient-experience results.

### 3.4 TRACEABILITY

Documents lineage across acquisition, design, manufacture, physical part, service and outcomes.

One report may include multiple sections, but its `reportType` identifies the principal purpose.

---

## 4. Three-part report object

A complete reporting implementation SHOULD distinguish:

```text
ReportDefinition
  what content/sections/layout policy should be produced

ReportGenerationActivity
  the actual generation event, inputs, software and warnings

ReportArtifact
  immutable output bytes + hash + exact source references
```

`ReportDefinition` may initially live as a versioned project/global definition or generator configuration until promoted into the core schema.

`ReportGenerationActivity` maps naturally to `ProvenanceRecord`.

`ReportArtifact` is already a Project Schema v0 entity.

---

## 5. Immutable ReportArtifact

P0 report identity SHALL include or resolve:

```text
reportArtifactId
reportType
assetRef
asset SHA-256
generatedAt
generator product/version/build/commit
sourceRefs[]
provenanceRecordId or equivalent derivation record
```

When `ReportArtifact` v0 lacks a first-class field, generator build/provenance information MAY be carried through the associated `ProvenanceRecord` / asset metadata / extension until promoted by schema evolution.

A historical report asset is immutable once issued/referenced as evidence.

---

## 6. Semantic source manifest

Each clinically/manufacturing significant report SHOULD have a machine-readable semantic companion manifest.

Conceptual contract:

```text
ReportSourceManifest
  reportArtifactId
  reportDefinitionId/version/hash
  generator build/commit

  patient/case reference under chosen privacy policy
  orthosisProjectId / side

  designRevisionRefs[] + content hashes
  sourceAcquisitionRefs[] + hashes
  registrationRefs[]
  ROI / RegionModel refs[]
  indication/profile refs[]
  evidence refs[]

  material refs / lots / property measurements
  manufacturing profile/run/artifact/physical part refs
  QC requirement/measurement refs

  outcome target/measurement/comparison refs
  PROM / comfort / fit / satisfaction / adherence refs
  service-state refs

  warning / quality / comparability snapshot
  rounding/display policy
```

When hashed, selected JSON metadata SHOULD use JCS/RFC 8785 according to Project Schema policy.

The semantic manifest exists so a PDF renderer, HTML renderer or future reporting service can be replaced without losing historical meaning.

---

## 7. Minimum content by domain

### 7.1 Identity/context

As permitted by privacy policy:

```text
project/case identifier
external clinical identifier when authorized
side
report identity/type/date
clinician/author when appropriate
clinical intent / attached indication profiles
```

### 7.2 Acquisition/protocol

For each quantitative outcome used:

```text
source acquisition ID
device/model/calibration where relevant
activity / footwear / surface / speed protocol
trial/step/window aggregation
units
coordinate/registration identity
quality status / reason flags
```

### 7.3 Design prescription

Report structured semantics, not only an image:

```text
DesignRevision ID/hash
base template exact version/hash
operation stack summary
feature type
side/anatomical region
dose + units
placement/reference frame
mechanical/material prescription
algorithm/profile versions
```

### 7.4 Material/manufacturing

Where applicable:

```text
material definition + lot
nominal vs measured property distinction
manufacturing profile version/hash
run ID / machine/process
artifact ID/hash
physical part ID/serial
post-process state
QC measurements + acceptance state
```

### 7.5 Outcomes

For each reported quantitative result:

```text
MEASURED or PREDICTED
canonical metric/KPI identity
value/series/map reference
units
ROI/region version
protocol
quality state
uncertainty when available
comparison compatibility state
absolute/relative deltas computed from full-precision source values
```

### 7.6 Patient experience

PROM, pain/function, comfort, fit/usability, satisfaction and adherence remain separate constructs. A report SHALL not collapse them into an undocumented universal score.

---

## 8. Evidence citations

Scientific/guideline claims in generated reports SHALL reference stable source IDs and truthful locators inherited from the project/profile/target definition, for example:

```text
REF-CAD-005 — pp.1595–1600
GUIDE-IWGDF-2023 — Prevention guideline recommendation
```

A bibliography update after report generation SHALL NOT retroactively change which source/version/locator the historical target or interpretation relied on.

The report MAY render formatted citations, but the source manifest retains stable IDs.

---

## 9. Historical exactness

Canonical scenario:

```text
DesignRevision N
  -> ReportArtifact R1
DesignRevision N+1 created later
```

`R1` SHALL still resolve N and the exact measurements/profiles/artifacts used at its generation time.

The application SHALL NOT make an old PDF card silently show current N+1 values while keeping the old report identity.

If the user asks for an updated report:

```text
R1 preserved
R2 generated from N+1 or selected current source set
R2 has new reportArtifactId + bytes/hash + generation provenance
```

---

## 10. Regeneration and reproducibility

Two reproducibility levels are distinguished.

### 10.1 Semantic reproducibility

Given the same source entity versions, report definition and generator semantic version, the generated **semantic source manifest** SHOULD be canonically equivalent.

This is the P0 reproducibility target.

### 10.2 Byte reproducibility

Byte-identical PDF/HTML output is optional unless a deterministic rendering profile explicitly claims it.

Fonts, PDF metadata timestamps, library versions and compression may change bytes without changing report meaning.

Therefore:

```text
semantic-equivalent report != necessarily byte-identical report
```

Every emitted file still receives its own byte hash.

---

## 11. Charts and visual overlays

Heatmaps, bar charts, pressure curves, COP plots and geometry snapshots are derived views.

For every clinically/manufacturing significant chart, the report source manifest SHALL retain the underlying data/source refs and plotting definition/version sufficient to explain the view.

Rules:

1. Color scale boundaries and units are explicit.
2. A heatmap does not replace numeric pressure data.
3. Visual normalization/stance interpolation is identified when used.
4. A camera/view change cannot alter a reported physical distance/angle.
5. An image annotation never overrides a structured measurement.

---

## 12. Rounding and display policy

Calculations use authoritative full-precision stored values.

Display rounding occurs only after calculations.

Example:

```text
baseline stored = full precision
outcome stored  = full precision
delta computed  = full precision difference
report display  = each field formatted by named rounding policy
```

A report SHALL NOT recompute relative deltas from already rounded display numbers when authoritative values exist.

The manifest SHOULD identify the rounding/display policy version.

---

## 13. Quality, warnings and uncertainty

A report must not make degraded evidence look fully valid through formatting.

Where material to interpretation, include:

```text
measurement quality state
reason flags
comparison compatibility state
protocol mismatch warnings
missing/unavailable result state
uncertainty / confidence interval when supplied
QC blocking/warning state
OPEN/unqualified product limits where relevant
```

`UNAVAILABLE` is rendered as unavailable/not computed with reason, never `0`.

---

## 14. Measured vs predicted presentation

Measured and predicted outcomes SHALL be visibly and semantically distinguishable.

At minimum preserve:

```text
measurementKind
model ID/version for predictions
uncertainty/applicability information when available
source acquisition for measurements
```

A report cannot remove the `PREDICTED` label merely to simplify presentation.

---

## 15. Privacy profiles

Reporting/export follows Project Schema privacy classes:

```text
FULL_CLINICAL
PSEUDONYMIZED
MANUFACTURING_MINIMUM
```

### FULL_CLINICAL
May include direct clinical identifiers where authorized by deployment policy.

### PSEUDONYMIZED
Uses project/case pseudonymous identity while preserving internal lineage.

### MANUFACTURING_MINIMUM
Contains only manufacturing-required identity/context plus revision/material/process traceability. Raw pressure, PROM responses, diagnosis text and unnecessary demographics are excluded by default.

Privacy filtering is performed from structured source data before rendering, not by post-hoc black rectangles over a full report.

---

## 16. Report vs export vs audit

Keep distinct:

```text
ReportArtifact
  human/machine-readable presentation of selected project state

ExportArtifact
  geometry/toolpath/package output used by another system/process

ProvenanceRecord
  how/why an entity/result/report was generated

AuditEvent
  significant user/application/security event
```

One event may create several linked entities, but their meanings do not collapse.

---

## 17. Manufacturing/QC report gate

A manufacturing report SHALL distinguish:

```text
export/generated successfully
manufactured
measured/QC checked
accepted
issued
```

A valid STL/GCODE export cannot be rendered as `ACCEPTED PART` if blocking QC failed or required QC is absent.

The report references the exact `PhysicalOrthosis`; two physical copies from the same design remain separate reportable entities.

---

## 18. Outcome report gate

Before reporting a before/after delta as a compatible outcome comparison, the report generator resolves `OutcomeComparison.compatibilityState`.

If:

```text
VALID
```

then normal comparative presentation is allowed.

If:

```text
VALID_WITH_WARNINGS
```

warnings are surfaced with the comparison.

If:

```text
NOT_COMPARABLE
INSUFFICIENT_DATA
```

the report SHALL NOT present the delta as an unqualified efficacy result.

Device/protocol differences are especially relevant because cross-system plantar-pressure measurements can differ materially [REF-CAD-036, Abstract—Methods/Results/Conclusions].

---

## 19. Report generation provenance

A report generation `ProvenanceRecord` SHOULD answer:

```text
activityType = REPORT_GENERATION
inputEntityRefs = exact source entities
outputEntityRefs = ReportArtifact + report asset/manifest
recordedAt
agentRefs
softwareBuildRefs
algorithmRefs / reportDefinition refs
profileRefs
evidenceRefs when the generator injects interpretation
warnings
```

The provenance graph allows the system to move from report -> source result -> source acquisition -> design/manufacturing state rather than relying on filenames.

---

## 20. External interoperability

A reporting package MAY expose standardized mappings such as:

```text
FHIR Observation
FHIR QuestionnaireResponse
FHIR Provenance
```

or a FAIR-style machine-readable companion manifest.

External mapping is additive. It does not replace the richer internal CAD lineage.

Electronic signatures, legal attestation, certified PDF profiles and jurisdiction-specific record-retention rules remain separate qualification decisions.

---

## 21. Acceptance family — `RPT-*`

### `RPT-001` — exact design revision
Report resolves the exact `DesignRevision` ID + content hash used at generation.

### `RPT-002` — immutable report bytes
Issued report asset has hash and is not overwritten in place.

### `RPT-003` — source manifest
Significant report has a machine-readable source manifest or equivalent exact source-ref set.

### `RPT-004` — generator provenance
Report retains generator product/version/build and generation activity provenance.

### `RPT-005` — acquisition protocol
Reported biomechanical outcomes retain device/protocol/quality references required by their analysis profile.

### `RPT-006` — ROI/metric exactness
Report preserves canonical metric ID and ROI/RegionModel version.

### `RPT-007` — evidence exactness
Evidence-linked target/report resolves the historical stable source ID + locator/profile version used at generation.

### `RPT-008` — material/manufacturing lineage
Manufacturing report resolves exact material lot/profile/run/artifact/physical part where applicable.

### `RPT-009` — blocking QC visibility
Blocking QC failure cannot be hidden behind a successful export state.

### `RPT-010` — measured/predicted distinction
Predicted outcomes remain explicitly predicted in semantic manifest and presentation.

### `RPT-011` — patient-experience separation
PROM, comfort, fit, satisfaction and adherence remain distinct constructs.

### `RPT-012` — privacy-profile filtering
Pseudonymized/manufacturing-minimum outputs exclude fields disallowed by selected policy while retaining required lineage.

### `RPT-013` — historical immutability
Creating revision N+1 does not change report generated from N.

### `RPT-014` — regeneration creates new artifact
Regeneration/reissue produces a new report identity/hash/provenance while preserving prior report.

### `RPT-015` — semantic reproducibility
Same source versions + same report definition/generator semantic version reproduce a canonically equivalent source manifest.

### `RPT-016` — chart is derived
Deleting/re-rendering chart assets does not change underlying quantitative results.

### `RPT-017` — full-precision computation
Delta/relative change uses authoritative values, not rounded display values.

### `RPT-018` — missing-source failure
A report cannot be regenerated as fully traceable if a required immutable source/definition is missing; failure/warning is explicit rather than substituting `latest`.

---

## 22. Existing XACC mapping

```text
RPT-001/013       -> XACC-044 / XACC-049
RPT-007           -> XACC-045
RPT-008/009       -> XACC-034 / XACC-048 / XACC-049
RPT-012           -> XACC-042 / XACC-043
RPT-018           -> XACC-039
```

The reporting family adds report-specific precision while keeping `XACC-*` as cross-domain gates.

---

## 23. OPEN qualification items

```text
final PDF/HTML/report-template technology
legal/electronic signature profile
qualified archival retention policy
regulated-record requirements by jurisdiction/deployment
PDF/A or other archival conformance profile
cryptographic attestation/signing keys
byte-deterministic rendering profile if ever required
final machine-readable external report interchange schema
```

These items are not geometry-kernel decisions.

---

## 24. Evidence basis

- Provenance supports data-quality verification and reproducibility: [REF-CAD-111, Abstract—Background].
- Biomedical provenance reviews support consistent structured provenance rather than ad-hoc metadata: [REF-CAD-112, Abstract—Results/Conclusions].
- FAIR requires qualified references and detailed provenance: [REF-CAD-113, Box 2, I3/R1.2].
- Pressure outcomes must remain protocol/device aware: [REF-CAD-036, Abstract—Methods/Results/Conclusions]; [REF-CAD-108, pp. 880–884; Abstract].
- Project provenance semantics remain aligned conceptually with W3C PROV: [STD-W3C-PROV-O-2013, §2; §3.1].

---

## 25. Freeze conclusion

P0 reporting is frozen semantically as:

```text
exact sources
  -> versioned report definition/generator
  -> provenance-bearing generation activity
  -> immutable report bytes + hash
  -> machine-readable semantic source manifest
```

Historical reports do not float with the current project, and presentation never becomes the authoritative source of quantitative/design/manufacturing meaning.
