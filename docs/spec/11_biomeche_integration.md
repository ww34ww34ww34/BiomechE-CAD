# 11 — BiomechE Integration Contract

**Status:** FROZEN semantic integration baseline v1  
**Date:** 2026-08-15  
**Scope:** kernel-independent contract between the BiomechE quantitative core and BiomechE-CAD project/design/outcome semantics.  
**Depends on:** Functional Specification v2, Project Schema v0, Coordinate/Registration v1, Analysis/QC v0, Functional Acceptance Suite v0.  
**Dynamic note:** BiomechE dynamic gait is frozen through `DYN-005`; exact dynamic pressure/force/integral/region bindings that depend on `DYN-006+` remain explicitly `OPEN/PENDING_BIOMECHE_FREEZE`.

> BiomechE-CAD consumes quantitative evidence from BiomechE. It does not silently fork or reimplement BiomechE KPI semantics merely to draw, report or compare them.

---

## 1. Purpose

The integration must preserve the complete chain:

```text
RAW ACQUISITION
  -> BiomechE quantitative analysis
  -> evidence/context interpretation
  -> semantic CAD prescription
  -> immutable DesignRevision
  -> ManufacturingArtifact
  -> PhysicalOrthosis + QC
  -> outcome acquisition
  -> BiomechE quantitative analysis
  -> compatible before/after comparison
  -> report / next revision
```

Pressure-guided footwear research directly supports an iterative `measure -> modify -> remeasure` workflow rather than treating a pressure image as a decorative input [REF-CAD-005, pp. 1595–1600; Abstract—Methods/Results/Conclusions]. Reliability work also shows that acquisition protocol and included step count can materially affect the validity/reliability of pressure results; the reported 12-step requirement is population/protocol-specific and is **not** a universal product constant [REF-CAD-108, pp. 880–884; Abstract—Methods/Findings/Interpretation].

The integration therefore transports **measurement semantics and provenance**, not only numbers or heatmaps.

---

## 2. Authority boundary

### 2.1 BiomechE owns quantitative biomechanical semantics

BiomechE is the authoritative producer for its named KPI/result semantics, including where applicable:

```text
pressure / force primitives
COP
static-load KPI
stabilometry KPI
dynamic contact/event/spatiotemporal KPI
region-model results
quality states / reason flags
algorithm/profile versions
analysis-domain semantics
```

A BiomechE KPI identifier represents a defined numerical/biomechanical semantic, not a localized UI label.

### 2.2 BiomechE-CAD owns design and lifecycle semantics

BiomechE-CAD is authoritative for:

```text
Case / OrthosisProject
IndicationProfile attachment
OutcomeTarget
ROI mapping into design anatomy
semantic prescription / DesignOperation
DesignRevision history
materials / manufacturing realization
ManufacturingArtifact
PhysicalOrthosis
QC / service state
OutcomeComparison
report / traceability artifact
```

### 2.3 No duplicate formula authority

If BiomechE exposes a canonical KPI semantic, BiomechE-CAD SHALL NOT create a second hidden formula under the same human-readable metric name.

Allowed patterns:

```text
A) consume BiomechE result directly;
B) reproduce it only through the same frozen algorithm/profile contract for deterministic validation;
C) define a CAD-specific derived metric under a distinct ID and explicit algorithm version.
```

A CAD-specific metric SHALL never masquerade as a BiomechE KPI.

---

## 3. Version pinning and capability negotiation

Every imported BiomechE result bundle SHALL preserve enough producer identity to reconstruct its historical meaning:

```text
product = BiomechE
software version
Git commit/build ID when available
result-contract/schema version
exam type
capability/profile IDs + versions
algorithm IDs + versions
region-model IDs + versions when used
coordinate-frame convention versions
```

Current integration reference snapshot:

```text
ww34ww34ww34/BiomechE
commit d5e467a1a5551f4280cfef5b483da1999f1566e0
```

[ARCH-BIOMECHE-INTEGRATION-2026-08-15]

The adapter SHALL negotiate supported semantics by explicit identifiers/versions, not by assuming that a newer BiomechE build has unchanged output meaning.

Unknown mandatory semantic versions cause `UNSUPPORTED_CONTRACT` or equivalent explicit failure. They are never interpreted as the nearest known version.

---

## 4. Two-layer import model

BiomechE-CAD imports BiomechE results at two complementary layers.

### 4.1 Layer A — immutable result bundle / evidence snapshot

The complete imported result/exam payload is preserved as an immutable asset and indexed by an acquisition:

```text
Acquisition
  acquisitionType = BIOMECHE_RESULT
  rawAssetRefs[] -> result bundle bytes
  sourceFrameRef
  units / protocol / qualityFlags
  provenanceRecordId
```

The result asset receives a SHA-256 digest and retains source acquisition/hash references where available.

This layer is the reproducibility/audit anchor.

### 4.2 Layer B — normalized outcome records

Named values needed by CAD logic are normalized into `OutcomeMeasurement` objects:

```text
OutcomeMeasurement
  measurementKind
  caseId / orthosisProjectId / side
  designRevisionId
  physicalOrthosisId?      # outcome with manufactured part
  acquisitionId           # BIOMECHE_RESULT and/or source quantitative acquisition linkage
  metric
  roiRef?
  value? / seriesRef?
  units
  computationDefinition
  timestamp
  protocolRef
  qualityState
  algorithmRef
  uncertainty?
  provenanceRecordId
```

The full bundle is not discarded after extracting scalars.

---

## 5. Canonical result-envelope semantics

A BiomechE adapter SHALL be able to reconstruct the conceptual envelope:

```text
BiomechEResultEnvelope
  producer
    product
    version
    commit/build

  resultContractVersion
  examType
  side / subject scope

  sourceAcquisitionRefs[]
  sourceAssetHashes[]

  examFrameRef
  sensorGeometryRef
  registrationRefs[]

  protocol
    activity
    acquisition mode
    device/calibration
    timing/sample metadata
    trial/pass/contact/step selection
    speed/footwear/surface where relevant
    analysis window

  capabilityProfileRefs[]
  algorithmRefs[]
  regionModelRefs[]

  KPIResult[]
  quality / reason flags
  derivedAssetRefs[]
```

The transport encoding may evolve; these semantics may not be silently lost.

---

## 6. KPI transfer contract

For each imported KPI/result, preserve at minimum:

```text
metric namespace
canonical metric/KPI ID
semantic/computation version
result shape: SCALAR / SERIES / MAP / EVENT_SET / OTHER
value or asset/series reference
units
side / subject scope
coordinate frame when spatial
analysis domain
ROI / region model identity and version
trial/window/contact/step provenance where applicable
algorithm/profile version
quality status
reason flags
uncertainty when available
source result/acquisition identity
```

### 6.1 Metric namespace

P0 recommended normalized identifier:

```text
BIOMECHE:<CANONICAL_KPI_ID>
```

or an equivalent structured namespace field in a later schema revision.

Localized display text never replaces the canonical identifier.

### 6.2 Units

BiomechE-CAD canonical physical units remain:

```text
mm, s, N, kPa, deg, mm²
```

A result may be imported in another explicitly declared unit only if conversion semantics are exact and traceable. A unit conversion changes representation, not metric identity.

---

## 7. Quality-state propagation

BiomechE currently distinguishes result availability/quality states such as:

```text
VALID
DEGRADED
UNAVAILABLE
```

[ARCH-BIOMECHE-INTEGRATION-2026-08-15, `docs/spec/06_kpi_catalog.md`]

BiomechE-CAD SHALL preserve this meaning.

Rules:

1. `UNAVAILABLE` SHALL NOT be imported as numeric zero.
2. `DEGRADED` MAY carry a numeric result but SHALL preserve all available reason flags.
3. CAD SHALL NOT silently upgrade a degraded result to valid.
4. A report SHALL expose material quality/comparability warnings relevant to interpretation.
5. A comparison policy may reject degraded inputs even when an individual measurement is numerically present.

The existing `OutcomeMeasurement.value` being optional permits a semantically unavailable result to exist without a fabricated scalar.

---

## 8. Raw numeric pressure remains authoritative

For pressure workflows:

```text
numeric pressure dataset
  + timestamps
  + physical SensorGeometry
  + device/calibration/protocol
  + coordinate frame
```

is authoritative.

A heatmap is a derived view.

BiomechE pressure physics explicitly reconstructs normal force from pressure and represented area and computes COP in declared metric sensor coordinates; raw row/column topology is not a physical coordinate system [ARCH-BIOMECHE-INTEGRATION-2026-08-15, `docs/spec/04_pressure_physics.md`].

If quantitative resampling is performed, the adapter SHOULD preserve the source representation and, where applicable, verify force conservation:

```text
sum(source pressure_i * area_i)
≈
sum(target pressure_j * area_j)
```

within a declared computational/qualification tolerance.

---

## 9. Device, calibration and protocol provenance

Plantar-pressure hardware differs in accuracy, hysteresis, creep and COP performance, and device-specific calibration can materially affect results [REF-CAD-109, pp. 141–144; Abstract]. Hardware characterization therefore belongs to qualification/provenance rather than an assumed universal accuracy [REF-CAD-110, pp. 158–167; Abstract]. More recent cross-system evidence likewise shows limited interchangeability across devices for several pressure/force/time metrics [REF-CAD-036, Abstract—Methods/Results/Conclusions].

Every pressure-derived result used for longitudinal comparison SHALL therefore retain, where available/required by profile:

```text
device identity/model/serial
sensor technology
calibration identity/date/version
sample semantics/units
sample rate/timestamps
measurement mode (platform/in-shoe/...)
activity
footwear context
walking surface
speed protocol
trial/step selection and exclusions
analysis window
operator / quality flags
```

A product profile decides which differences are blocking versus warning; no universal cross-device equivalence is assumed.

---

## 10. ROI and RegionModel mapping

BiomechE regions and BiomechE-CAD `ROIDefinition` objects are related by explicit mapping, never name matching alone.

A mapping preserves:

```text
BiomechE region_model_id/version
BiomechE region_id
CAD roiId/version
generation/application profile
frame/registration
boundary policy
coverage denominator when relevant
mapping algorithm/version
```

Two measurements using different region-model/ROI versions remain distinct even when they share a display label.

For offloading workflows the CAD comparison model preserves at least:

```text
target ROI
safety-ring / adjacent ROI
remote comparison regions
```

because local pressure reduction can transfer load to neighbouring or remote regions [REF-CAD-029, Fig.1; Fig.6].

---

## 11. Coordinate bridge

All spatial BiomechE data enter through the frozen coordinate contract:

```text
matrix topology
 -> physical SensorGeometry
 -> BiomechE ExamFrame2D / source metric frame
 -> explicit Registration
 -> CAD-ANAT-1
```

The adapter maps semantic meaning, not variable names.

BiomechE foot-local positive transverse semantics are lateral -> medial on both sides; this is compatible with CAD intrinsic `q`, while global Cartesian `Y` remains subject-left and therefore side-dependent for medial/lateral meaning.

No orientation, laterality or transform direction is inferred from display layout.

---

## 12. Baseline -> design -> physical part -> outcome loop

Canonical P0 loop:

```text
Baseline PressureAcquisition
    -> BiomechEResult baseline
    -> OutcomeMeasurement baseline
    -> OutcomeTarget / profile context
    -> DesignRevision N
    -> ManufacturingRun
    -> ManufacturingArtifact
    -> PhysicalOrthosis P
    -> QC gate
    -> Outcome PressureAcquisition wearing P
    -> BiomechEResult outcome
    -> OutcomeMeasurement outcome
    -> OutcomeComparison
    -> optional DesignRevision N+1
```

### 12.1 Baseline measurement

A baseline result may have no `physicalOrthosisId`. It still identifies the design/case context against which it is being used.

### 12.2 Outcome measurement

When a physical orthosis was worn/tested, `physicalOrthosisId` SHOULD be present and SHALL resolve through its manufacturing run/artifact to the exact `DesignRevision`.

### 12.3 No causal overclaim

A before/after improvement documents an observed compatible comparison. It does not by itself prove causal clinical efficacy outside the protocol/population studied.

---

## 13. Compatibility policy

`OutcomeComparison` is valid only after explicit compatibility evaluation.

At minimum evaluate:

```text
measurementKind
canonical metric semantic/version
units / conversion
side
exam type
analysis domain
ROI / RegionModel mapping
coordinate frame / registration
source device + calibration policy
activity
speed protocol
footwear / orthosis context
trial/step/window aggregation
quality state / reason flags
```

Possible states remain:

```text
VALID
VALID_WITH_WARNINGS
NOT_COMPARABLE
INSUFFICIENT_DATA
```

The comparison engine SHALL explain which fields caused degradation or rejection.

---

## 14. Measured vs predicted

BiomechE-CAD preserves:

```text
MEASURED != PREDICTED
```

A predicted pressure/COP/shear/other KPI SHALL retain model identity/version, applicability domain and uncertainty where available. It cannot become a measured result merely because its units and value match a measured record.

Predictions may inform design assistance but do not replace post-manufacture verification.

---

## 15. Reanalysis and software evolution

Historical measurements are append-only with respect to semantic meaning.

If a newer BiomechE build, algorithm or region model reprocesses an old acquisition:

```text
old BiomechEResult          preserved
old OutcomeMeasurement     preserved
new BiomechEResult          new identity/hash/provenance
new OutcomeMeasurement     new identity/version context
```

The system MAY compare analyses, but it SHALL NOT silently rewrite historical results in place.

This follows the broader provenance requirement that origin/history and processing steps remain available for quality verification and reproducibility [REF-CAD-111, Abstract—Background]. FAIR principles similarly call for detailed provenance and qualified references between related data/metadata [REF-CAD-113, Box 2, I3/R1.2].

---

## 16. Dynamic-gait staged integration

At the pinned BiomechE snapshot:

```text
DYN-001  GO
DYN-002  GO
DYN-003  GO structurally
DYN-004  GO structurally
DYN-005  GO
DYN-006  NEXT / not frozen
```

[ARCH-BIOMECHE-INTEGRATION-2026-08-15, `docs/RESUME_HERE_DYNAMIC_GAIT_2026-08-15_DYN005.md`]

Therefore:

### Allowed to bind now

```text
exam/trial/pass/contact identity
IC/FC and contact-sequence provenance
DYN-005 temporal/spatial KPI identifiers whose definitions are frozen
placement/progression/foot-axis provider IDs and versions
observability / quality state
```

### Explicitly pending

Exact dynamic bindings for:

```text
peak/mean pressure variants
PTI variants
force/integral regional dynamics
contact-time maps
stance-normalized curves
DYN-006 regional/curve aggregation
DYN-007+ COP/CPEI/rollover families
```

CAD SHALL not freeze substitute formulas while BiomechE is still defining them.

---

## 17. Failure semantics

The adapter SHALL fail visibly or degrade explicitly for at least:

```text
unsupported result-contract version
missing producer/build identity where required
missing source acquisition/hash
unknown canonical KPI semantic
unknown units
unresolved side/orientation/frame
missing region/ROI mapping
missing exact algorithm/profile definition
UNAVAILABLE KPI used as numeric input
cross-device/protocol mismatch forbidden by policy
broken physical-part lineage
invalid/dangling provenance reference
```

No failure path may fabricate a plausible zero, identity transform, `latest` profile or default side.

---

## 18. Privacy and data minimization

BiomechE result data may be clinically sensitive. Export policy remains driven by Project Schema privacy classes:

```text
FULL_CLINICAL
PSEUDONYMIZED
MANUFACTURING_MINIMUM
```

A manufacturing-minimum handoff SHALL not include raw pressure/PROM/demographics merely because those assets exist in the project. It includes only what the manufacturing process requires plus sufficient revision/material/profile traceability.

---

## 19. Interoperability boundary

FHIR is an optional adapter, not the internal CAD model.

Possible mappings:

```text
quantitative OutcomeMeasurement -> FHIR Observation
PROM responses -> QuestionnaireResponse
result/report derivation -> FHIR Provenance
```

The internal BiomechE/CAD identities, ROI versions, trial semantics and manufacturing lineage remain richer than a generic exchange mapping and must not be discarded to fit FHIR.

---

## 20. Acceptance family — `BINT-*`

### `BINT-001` — immutable result bundle
Imported BiomechE result bytes have asset identity + hash; later reanalysis does not replace them.

### `BINT-002` — producer/version pin
Imported result preserves BiomechE product/build/commit/contract/profile/algorithm identifiers required by its semantic version.

### `BINT-003` — numeric pressure authority
Deleting/rebuilding a heatmap cannot change quantitative pressure-derived results.

### `BINT-004` — explicit physical mapping
Matrix index topology cannot be consumed as physical coordinates without SensorGeometry/frame mapping.

### `BINT-005` — canonical KPI identity
Normalized measurement preserves the BiomechE KPI namespace/semantic version; UI labels cannot substitute for it.

### `BINT-006` — quality propagation
`VALID/DEGRADED/UNAVAILABLE` and reason flags round-trip without silent upgrade.

### `BINT-007` — unavailable is not zero
An unavailable KPI has no fabricated numeric zero and cannot enter a numeric comparison.

### `BINT-008` — protocol provenance
Device/calibration/activity/steps/window metadata required by the selected analysis profile survive import.

### `BINT-009` — region-version exactness
Result preserves RegionModel/region and CAD ROI mapping versions.

### `BINT-010` — side/frame exactness
Spatial results preserve side and coordinate-frame/registration identity.

### `BINT-011` — compatibility gate
Known protocol mismatch produces configured warning or `NOT_COMPARABLE`, never an unqualified delta.

### `BINT-012` — cross-device guard
Cross-device comparison requires explicit policy/harmonization provenance.

### `BINT-013` — measured/predicted separation
A predicted result cannot serialize as measured.

### `BINT-014` — physical-part lineage
Post-manufacture measurement resolves the tested `PhysicalOrthosis` and exact design/run/artifact chain.

### `BINT-015` — reanalysis append-only
Reprocessing the same raw acquisition under a new BiomechE algorithm/build creates new result/measurement identities.

### `BINT-016` — dynamic capability gate
A CAD build cannot claim support for a BiomechE dynamic semantic whose required DYN contract is not supported/frozen.

### `BINT-017` — quantitative resampling invariant
When configured, pressure resampling demonstrates force conservation within a declared computational tolerance; source data remain preserved.

### `BINT-018` — no formula fork
A CAD-derived quantity that differs from a BiomechE KPI receives a distinct metric/algorithm ID.

---

## 21. Mapping to existing cross-domain acceptance

```text
BINT-003/004      -> XACC-007/008
BINT-008/011/012  -> XACC-009
BINT-009           -> XACC-010
BINT-013           -> XACC-028
BINT-014           -> XACC-029/030
BINT-015           -> XACC-037/038
```

`BINT-*` adds integration-contract precision without weakening the existing XACC gates.

---

## 22. OPEN qualification items

These remain intentionally open until evidence/hardware or BiomechE upstream semantics justify a freeze:

```text
real platform/in-shoe accuracy tolerances
cross-device harmonization acceptance limits
scanner-to-pressure registration tolerances
minimum step/trial counts by each product protocol/profile
DYN-006+ dynamic pressure/force/integral exact bindings
DYN-007+ COP/CPEI dynamic bindings
measured plantar shear hardware profiles
prediction-model qualification thresholds
final wire/API transport encoding
```

No implementation may fill an `OPEN` item with an undocumented constant.

---

## 23. Evidence basis

- Iterative pressure-guided modification/verification: [REF-CAD-005, pp. 1595–1600; Abstract—Methods/Results/Conclusions].
- Protocol/step-count validity as population-specific: [REF-CAD-108, pp. 880–884; Abstract—Methods/Findings/Interpretation].
- PMD technical performance/calibration qualification: [REF-CAD-109, pp. 141–144; Abstract]; [REF-CAD-110, pp. 158–167; Abstract].
- Cross-device comparability guard: [REF-CAD-036, Abstract—Methods/Results/Conclusions].
- Provenance for quality/reproducibility: [REF-CAD-111, Abstract—Background].
- FAIR qualified references/detailed provenance: [REF-CAD-113, Box 2, I3/R1.2].
- Current upstream implementation/spec snapshot: [ARCH-BIOMECHE-INTEGRATION-2026-08-15].

---

## 24. Freeze conclusion

The P0 integration architecture is therefore:

```text
BiomechE = quantitative semantic authority
BiomechE-CAD = prescription/design/lifecycle authority

exchange = versioned + hashable + quality-bearing + protocol-bearing
historical results = append-only meaning
comparison = explicit compatibility gate
visualization = derived view
```

This contract is independent of the future CAD geometry foundation and does not reopen the architecture shoot-out.
