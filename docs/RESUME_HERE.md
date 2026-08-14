# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint:** 2026-08-14 — functional/scientific research is consolidated through Batch 08; `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md` is the canonical functional baseline; **Project Schema v0 is now active** with a Draft 2020-12 JSON reference schema and initial fixture. Architecture selection remains parked.

---

## 1. Product goal

Professional CAD for custom foot orthoses integrated with BiomechE:

```text
Acquisition
 -> quantitative evidence
 -> indication/context
 -> prescription
 -> immutable design revision
 -> material / manufacturing realization
 -> physical artifact + QC
 -> wear exposure / service state
 -> outcome measurement
 -> comparison / iteration
```

EasyCAD2 remains the detailed behavioral benchmark, not scientific truth or the architectural ceiling.

---

## 2. Evidence / standards governance

`docs/BIBLIOGRAPHY.md` is the single bibliographic authority.

Namespaces:

```text
EC2-*
GUIDE-*
REF-CAD-*
STD-*
VENDOR-*
ARCH-*
```

Cite exact truthful locators. Never invent pages.

The canonical bibliography now also records the technical references used by Project Schema v0:

```text
STD-JSON-SCHEMA-2020-12
STD-W3C-PROV-O-2013
STD-RFC-9562
STD-RFC-3339
STD-RFC-8785
STD-NIST-FIPS-180-4
STD-HL7-FHIR-R5-PROVENANCE
STD-HL7-FHIR-R5-OBSERVATION
STD-HL7-FHIR-R5-QUESTIONNAIRE
```

These constrain representation/interoperability/provenance, not clinical prescription semantics.

---

## 3. Current work order

```text
EASYCAD2 + LITERATURE + BATCH 03–08
        ↓
FUNCTIONAL SPEC v2 — DONE
        ↓
PROJECT SCHEMA v0 — DONE BASELINE
        ↓
KERNEL-INDEPENDENT ACCEPTANCE SUITE — NEXT
        ↓
COORDINATE / REGISTRATION FREEZE
        ↓
BIOMECHE INTEGRATION + REPORTING
        ↓
ARCHITECTURE SHOOT-OUT LATER
```

Do **not** resume OpenSubdiv vs ON_SubD yet.

---

## 4. Canonical functional specification

Current canonical:

`docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`

It consolidates normative requirements from Batches 03–08 and active subordinate specs:

```text
spec/06_corrective_elements.md
spec/08_material_stiffness.md
spec/09_analysis_qc_dfm.md
spec/10_manufacturing.md
spec/13_use_case_profiles.md
spec/14_prom_comfort_adherence.md
```

The previous `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` is preserved as historical detailed baseline.

---

## 5. Project Schema v0 — ACTIVE

Canonical semantic schema:

`docs/spec/02_project_schema.md`

Machine-readable reference:

`schemas/biomeche-cad-project-0.1.schema.json`

Initial fixture:

`fixtures/project/minimal-valid-project.json`

### Core schema rules

```text
native semantic prescription/operations = authoritative
committed DesignRevision = immutable
edit = successor revision
raw evidence/source asset = immutable
reusable definitions = exact version + hash/snapshot
physical manufactured copy = own identity
nominal != measured != predicted != service-aged
container/database/kernel = not selected by schema
```

`DesignRevision` preserves exact:

```text
parent revision(s)
side
base template version
source acquisitions
registrations
attached indication profiles
operation stack
material prescription
algorithm versions
derived-geometry references
validation summary
content hash
provenance
```

### Root P0 domain graph

```text
PatientLink / Case / OrthosisProject
Definitions
Assets
FrameDefinitions
Acquisitions / Registration / Landmarks / ROI
DesignRevisions
OutcomeTargets / Measurements / Comparisons
PROM / Comfort / Fit / Satisfaction / Adherence
MaterialLots / Regions / Stacks / StructuralRegions
MechanicalPropertyMeasurements / PostProcess states / Durability
ManufacturingRuns / Artifacts / PhysicalOrthoses
QCRequirements / QCMeasurements / ServiceStates
ExportArtifacts / ReportArtifacts
Provenance / Audit / Migration
```

### Version/integrity conventions

```text
internal new IDs: UUIDv7 preferred
external/business identifiers: separate
serialized event timestamps: RFC 3339
asset digest baseline: SHA-256
canonical JSON hash when needed: JCS / RFC 8785
reference serialization: UTF-8 JSON + JSON Schema Draft 2020-12
```

### Provenance/interoperability

The internal provenance contract is lightweight `Entity / Activity / Agent` compatible. W3C PROV is a conceptual/interoperability reference; RDF is not required.

FHIR R5 `Observation`, `QuestionnaireResponse` and `Provenance` are optional P1 exchange mappings. They do not become the internal CAD schema and cannot erase revision/ROI/material/manufacturing semantics.

### Schema acceptance family

Defined:

```text
SCHEMA-001..SCHEMA-030
```

Key coverage:

- semantic round-trip;
- unique IDs;
- no dangling mandatory refs;
- immutable revisions;
- revision DAG;
- exact-definition resolution;
- asset hash integrity;
- timestamp/unit preservation;
- side consistency;
- source→target registration direction;
- ROI version integrity;
- measured/predicted separation;
- outcome→revision/physical-part linkage;
- profile/evidence provenance;
- PROM reproducibility;
- material property source typing;
- manufacturing lineage;
- physical-copy uniqueness;
- blocking QC guard;
- append-only service history;
- migration trace;
- privacy-minimum export;
- profile confirmation state;
- explicit root-domain completeness.

### Packaging remains OPEN

Possible future physical realizations can include directory, ZIP-like project file, local DB export package, object store or server graph.

A future `.biomechecad` format is therefore a packaging decision, not a new domain model.

---

## 6. Key adopted functional semantics

- EasyCAD2 is behavioral evidence, not scientific truth.
- Dose, placement, units and anatomical reference survive as structured prescription data.
- Offloading is redistribution: target + safety ring + remote regions.
- Arch and heel are multi-component prescriptions, not single sliders.
- Geometry and mechanical/material dose remain independent.
- Pressure is quantitative; heatmaps are derived views.
- Measured and predicted outcomes remain distinct.
- Thresholds are population/protocol/ROI specific.
- `IndicationProfile` is an evidence-context layer, not a diagnosis engine.
- Active diabetic plantar ulcer uses a separate clinical pathway guard.
- Pain, function, comfort, fit, satisfaction and adherence are separate constructs.
- PROM version/language/scoring/licensing are first-class metadata.
- Material nominal property, manufactured effective property and service-aged property are distinct.
- Export success does not mean physical-part acceptance.
- CAD nominal geometry and manufactured measured geometry remain distinct.
- Definition/version meaning must survive future registry changes.

---

## 7. Acceptance semantics already available

```text
SCHEMA-001..SCHEMA-030
OFF-001..OFF-009
CE-001..CE-010
ARCH-001..ARCH-014
HEEL-001..HEEL-015
PROF-001..PROF-012
PROM-001..PROM-020
MAT-001..MAT-018
MAN-001..MAN-018
```

The next document must unify these into a kernel-independent end-to-end suite and add EasyCAD parity / mirror / registration / replay / reporting scenarios.

---

## 8. Architecture state — PARKED

Later comparison remains:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

Prefer one P0 SubD foundation. No major geometry dependency enters merely for theoretical capability coverage.

---

## 9. Exact restart point

### NEXT — `validation/functional_acceptance_suite.md`

Create a **kernel-independent functional acceptance suite**.

It must map requirements to deterministic/business-semantic fixtures before any geometry-engine choice.

Minimum blocks:

```text
1. SCHEMA-001..030
2. EasyCAD2 25-story behavioral parity map
3. OFF-* target/safety-ring semantics
4. CE-* anatomical element placement
5. ARCH-* geometry/mechanics/context/outcome
6. HEEL-* containment/relief/camber/mechanics
7. PROF-* context/non-transfer guards
8. PROM-* instrument/adherence/revision linkage
9. MAT-* property-source/durability semantics
10. MAN-* run/artifact/QC/physical-part lineage
11. bilateral mirror semantics
12. acquisition/registration directionality
13. pressure before/after comparability
14. deterministic revision replay
15. migration / missing-definition failure cases
16. privacy-minimum manufacturing handoff
```

Create/plan fixture set:

```text
fixtures/project/bilateral-project.json
fixtures/project/pressure-design-outcome-loop.json
fixtures/project/manufacturing-qc-lineage.json
fixtures/project/migration-v0.1.json
fixtures/acceptance/*
```

### THEN

```text
2. freeze `spec/01_coordinate_registration.md`
3. `spec/11_biomeche_integration.md`
4. `spec/12_reporting_traceability.md`
5. competitor functional-gap audit in parallel
6. product-specific PROM/material/process qualification
7. architecture shoot-out only after these freezes
```

---

## 10. DONE

- [x] EasyCAD2 primary behavior + 25-story baseline.
- [x] Functionality-first/science-first work mode.
- [x] Canonical bibliography/provenance governance.
- [x] Quantitative pressure/protocol policy.
- [x] Relief/offloading Batch 03 + `OFF-*`.
- [x] Corrective-elements spec + `CE-*`.
- [x] Arch Batch 04 + `ARCH-*`.
- [x] Heel Batch 05 + `HEEL-*`.
- [x] Use-case/population Batch 06 + `PROF-*`.
- [x] Diabetic active-ulcer pathway guard.
- [x] PROM/comfort/fit/adherence Batch 07 + `PROM-*`.
- [x] Material/manufacturing Batch 08 + `MAT-*` / `MAN-*`.
- [x] Functional specification v2 consolidated/canonical.
- [x] Historical functional spec preserved.
- [x] **`spec/02_project_schema.md` v0 created.**
- [x] **Machine JSON Schema Draft 2020-12 reference created.**
- [x] Initial `minimal-valid-project.json` fixture created.
- [x] Root machine schema normalized for frame, patient experience, material, QC, export/report collections.
- [x] Suggested-vs-confirmed profile state represented explicitly.
- [x] `SCHEMA-001..SCHEMA-030` defined.
- [x] Schema/provenance/interoperability standards added to canonical bibliography.
- [x] `D-CAD-022` project-schema decision recorded.
- [x] `SPEC_INDEX.md` updated through Project Schema v0.

## 11. TODO

- [ ] `validation/functional_acceptance_suite.md` — **NEXT**.
- [ ] Rich project fixtures: bilateral / pressure-loop / manufacturing-QC / migration.
- [ ] Execute automated JSON-Schema fixture validation in the implementation/CI environment.
- [ ] `spec/01_coordinate_registration.md` freeze before geometry implementation.
- [ ] `spec/11_biomeche_integration.md`.
- [ ] `spec/12_reporting_traceability.md`.
- [ ] Expand shear/COP when target hardware is fixed.
- [ ] Competitor feature-gap audit in parallel.
- [ ] Built-in PROM selection after licensing/psychometric review.
- [ ] Product-specific material/process qualification and tolerances.
- [ ] Progressively migrate historical docs when edited.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
