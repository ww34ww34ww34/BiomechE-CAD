# BiomechE-CAD — RESUME HERE

**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Canonical branch:** `main`  
**Checkpoint:** 2026-08-14 — functional/scientific research is consolidated through Batch 08; Functional Spec v2, Project Schema v0 and the kernel-independent Functional Acceptance Suite v0 are now active. Architecture selection remains parked.

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

EasyCAD2 remains the behavioral benchmark, not scientific truth or the architectural ceiling.

---

## 2. Canonical documents

```text
docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md   -> product scope / P0-P1-P2
docs/spec/02_project_schema.md                 -> persisted semantic contract
docs/validation/functional_acceptance_suite.md -> kernel-independent acceptance contract
docs/BIBLIOGRAPHY.md                           -> single bibliographic authority
docs/DECISIONS.md                              -> cross-cutting decisions
```

Reference machine schema / current fixture:

```text
schemas/biomeche-cad-project-0.1.schema.json
fixtures/project/minimal-valid-project.json
```

---

## 3. Current work order

```text
EASYCAD2 + LITERATURE + BATCH 03–08
        ↓
FUNCTIONAL SPEC v2 — DONE
        ↓
PROJECT SCHEMA v0 — DONE BASELINE
        ↓
KERNEL-INDEPENDENT ACCEPTANCE SUITE — DONE BASELINE
        ↓
RICH FIXTURES + COORDINATE / REGISTRATION FREEZE — NEXT
        ↓
BIOMECHE INTEGRATION + REPORTING
        ↓
ARCHITECTURE SHOOT-OUT LATER
```

Do **not** resume OpenSubdiv vs ON_SubD yet.

---

## 4. Functional/scientific state

Completed families:

```text
OFF-001..009
CE-001..010
ARCH-001..014
HEEL-001..015
PROF-001..012
PROM-001..020
MAT-001..018
MAN-001..018
```

Key semantics:

- pressure stays quantitative; heatmaps are derived;
- offloading = target ROI + safety ring + remote load redistribution;
- arch/heel are multi-component geometry + mechanics prescriptions;
- dose/placement/reference/units are persistent semantics;
- measured and predicted outcomes are different classes;
- clinical targets are population/protocol/ROI/evidence specific;
- indication profiles are evidence-context layers, not diagnostic engines;
- PROM/pain/function/comfort/fit/satisfaction/adherence remain separate;
- material nominal/effective/manufactured/service-aged state remain separate;
- CAD export != manufactured part != accepted part.

---

## 5. Project Schema v0 state

Canonical:

`docs/spec/02_project_schema.md`

Machine reference:

`schemas/biomeche-cad-project-0.1.schema.json`

Schema rules:

```text
native semantic state = authoritative
committed DesignRevision = immutable
edit = successor revision
raw source evidence = immutable/hash-addressable
reusable definitions = exact version + content hash/snapshot
physical manufactured copy = own identity
nominal != measured != predicted != service-aged
storage/container/database/kernel = OPEN
```

P0 root collections explicitly include:

```text
PatientLink / Case / OrthosisProject
Definitions / Assets
FrameDefinitions / Acquisitions / Registrations / Landmarks / ROI
DesignRevisions
OutcomeTargets / Measurements / Comparisons
PROM / Comfort / Fit / Satisfaction / Adherence
MaterialLots / Regions / Stacks / StructuralRegions
MechanicalProperty / PostProcess / Durability
ManufacturingRun / Artifact / PhysicalOrthosis
QCRequirements / QCMeasurements / ServiceStates
ExportArtifacts / ReportArtifacts
Provenance / Audit / Migration
```

Reference conventions:

```text
UUIDv7 preferred for new internal IDs
RFC 3339 timestamps
SHA-256 baseline asset digest
JCS/RFC 8785 when canonical JSON hashing is required
JSON Schema Draft 2020-12 reference serialization
W3C-PROV-compatible Entity/Activity/Agent provenance model
optional FHIR R5 mappings only at interoperability boundary
```

Schema acceptance family:

```text
SCHEMA-001..SCHEMA-030
```

---

## 6. Functional Acceptance Suite v0 state

Canonical:

`docs/validation/functional_acceptance_suite.md`

The suite is deliberately kernel-independent.

It contains:

```text
L0 schema/integrity
L1 single-domain semantics
L2 cross-domain workflows
L3 geometry/numerical semantics
L4 manufacturing/physical-part semantics
L5 evidence/reporting/portability
```

It maps the 25 EasyCAD2 validation behavior groups to BiomechE-CAD acceptance paths and defines:

```text
XACC-001..XACC-050
```

Coverage includes:

- external patient identity;
- unit preservation;
- semantic bilateral mirror;
- template versioning;
- numeric pressure + registration/comparability;
- Scan3D raw evidence + landmark registration;
- Image2D calibration;
- thickness/heel/arch/wedge semantics;
- corrective elements and sculpt/scan conform;
- indication-profile confirmation/non-transfer;
- PROM/adherence historical meaning;
- offload safety-ring outcome;
- measured vs predicted outcome;
- design→manufacturing→physical part lineage;
- nominal vs measured material state;
- blocking QC;
- service history;
- deterministic revision replay;
- missing-definition/migration failure gates;
- manufacturing-minimum/privacy exports;
- report/evidence revision exactness;
- arbitrary section + fixed-height semantics (`XACC-046`);
- two-point ruler accuracy/view-independence (`XACC-047`);
- production closure + export lineage (`XACC-048`);
- report source exactness (`XACC-049`);
- profile-scoped minimum-thickness DFM detect/correction provenance (`XACC-050`).

The suite explicitly distinguishes:

```text
semantic exactness
numerical tolerance
bitwise/canonical determinism
visual equivalence
```

Exact geometry/registration tolerances are intentionally deferred to the coordinate/qualification specifications rather than guessed.

---

## 7. Architecture state — PARKED

Later comparison remains:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

The future engine must pass the already-defined functional/schema/acceptance contract. The contract is not rewritten around the winning library.

---

## 8. Exact restart point

### NEXT A — richer schema / acceptance fixtures

Create at least:

```text
fixtures/project/bilateral-project.json
fixtures/project/pressure-design-outcome-loop.json
fixtures/project/manufacturing-qc-lineage.json
fixtures/project/migration-v0.1.json

fixtures/acceptance/mirror-semantics.json
fixtures/acceptance/registration-known-transform.json
fixtures/acceptance/roi-version-comparison.json
fixtures/acceptance/profile-non-transfer.json
fixtures/acceptance/prom-versioning.json
fixtures/acceptance/offload-safety-ring.json
fixtures/acceptance/material-property-provenance.json
fixtures/acceptance/blocking-qc.json
fixtures/acceptance/section-height.json
fixtures/acceptance/ruler-known-distance.json
fixtures/acceptance/min-thickness-dfm.json
```

Start executable validation for `SCHEMA-*` / `XACC-*` in the implementation/CI environment.

### NEXT B — freeze `spec/01_coordinate_registration.md`

Must define before geometry implementation:

```text
canonical CAD/anatomical frames
handedness
axes + origin
LEFT/RIGHT semantic convention
s/q relation to global/anatomical frame
pressure matrix indexing vs physical axes
BiomechE pressure transforms
Scan3D heel/1st/5th landmark frame
Image2D calibration frame
matrix/vector convention
source→target transform direction
transform composition order
serialization
mirror semantics
units
numerical tolerances
round-trip invariants
no silent orientation inference
```

### THEN

```text
3. spec/11_biomeche_integration.md
4. spec/12_reporting_traceability.md
5. competitor functional-gap audit in parallel
6. product-specific PROM/material/process qualification
7. architecture shoot-out only after these freezes
```

---

## 9. DONE

- [x] EasyCAD2 25-story baseline.
- [x] Evidence-led functional research through Batch 08.
- [x] Canonical bibliography and stable evidence IDs.
- [x] Functional Specification v2 canonical.
- [x] Project Schema v0 semantic Markdown.
- [x] JSON Schema Draft 2020-12 reference manifest.
- [x] Minimal project fixture.
- [x] `SCHEMA-001..030` acceptance semantics.
- [x] Schema technical standards added to `BIBLIOGRAPHY.md`.
- [x] `D-CAD-022` project schema decision.
- [x] Kernel-independent Functional Acceptance Suite v0.
- [x] EasyCAD2 25 stories remapped into acceptance paths.
- [x] `XACC-001..050` cross-domain acceptance scenarios.
- [x] Dedicated EasyCAD completion cases for US19/20/21/23/24.
- [x] `SPEC_INDEX.md` updated through acceptance suite.

## 10. TODO

- [ ] Rich schema/acceptance fixtures — **NEXT A**.
- [ ] Executable schema/XACC validator tests.
- [ ] `spec/01_coordinate_registration.md` freeze — **NEXT B**.
- [ ] `spec/11_biomeche_integration.md`.
- [ ] `spec/12_reporting_traceability.md`.
- [ ] Expand shear/COP after target hardware is fixed.
- [ ] Competitor feature-gap audit in parallel.
- [ ] Built-in PROM selection after licensing/psychometric review.
- [ ] Product-specific material/process qualification/tolerances.
- [ ] Progressively migrate historical docs when edited.
- [ ] Later: OpenSubdiv vs openNURBS/ON_SubD shoot-out.
