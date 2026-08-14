# BiomechE-CAD — Kernel-Independent Functional Acceptance Suite

**Status:** ACTIVE acceptance baseline v0  
**Date:** 2026-08-14  
**Architecture:** deliberately out of scope  
**Functional authority:** `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md`  
**Project schema:** `docs/spec/02_project_schema.md`  
**Bibliography:** `docs/BIBLIOGRAPHY.md`

---

## 0. Purpose

This document defines the acceptance contract that BiomechE-CAD must satisfy **before and independently from selecting a geometry foundation**.

The rule is:

```text
PRODUCT REQUIREMENT
        ↓
SEMANTIC / NUMERICAL ACCEPTANCE
        ↓
FIXTURE
        ↓
IMPLEMENTATION
```

not:

```text
LIBRARY CAPABILITY
        ↓
PRODUCT REQUIREMENT
```

OpenSubdiv, ON_SubD or any future engine is therefore judged against this suite; the suite is not rewritten to suit the engine.

---

# 1. Acceptance layers

## L0 — Document/schema integrity

Verifies persistence, identity, units, versions, references, migration and provenance without requiring geometry evaluation.

## L1 — Single-domain functional semantics

Verifies individual capabilities already specified by:

```text
OFF-*
CE-*
ARCH-*
HEEL-*
PROF-*
PROM-*
MAT-*
MAN-*
```

## L2 — Cross-domain workflow semantics

Verifies that acquisition, prescription, design revision, outcome, material, production and longitudinal state remain linked correctly.

## L3 — Geometry/numerical semantics

Verifies output geometry/measurements needed by the product but does not prescribe which geometry library produces them.

## L4 — Manufacturing / physical-part semantics

Verifies design→run→artifact→physical part→QC→service lineage.

## L5 — Evidence / reporting / portability

Verifies provenance, profile boundaries, privacy-minimum handoff, report reproducibility and package migration.

---

# 2. Mandatory acceptance-family coverage

A release candidate cannot call a P0 family implemented unless all P0 tests in that family are mapped to executable tests or an explicitly approved manual/HIL protocol.

| Family | Current IDs | Primary authority | Gate status |
|---|---|---|---|
| Project schema | `SCHEMA-001..030` | `spec/02_project_schema.md` | REQUIRED P0 |
| Offloading | `OFF-001..009` | Batch 03 / analysis spec | REQUIRED P0 |
| Corrective elements | `CE-001..010` | `spec/06_corrective_elements.md` | REQUIRED P0 |
| Arch | `ARCH-001..014` | Batch 04 | REQUIRED P0 |
| Heel | `HEEL-001..015` | Batch 05 | REQUIRED P0 |
| Indication profiles | `PROF-001..012` | `spec/13_use_case_profiles.md` | REQUIRED P0 |
| PROM / adherence | `PROM-001..020` | `spec/14_prom_comfort_adherence.md` | REQUIRED P0 where feature enabled |
| Material | `MAT-001..018` | `spec/08_material_stiffness.md` | REQUIRED P0 for material-aware workflow |
| Manufacturing | `MAN-001..018` | `spec/10_manufacturing.md` | REQUIRED P0 for production workflow |

No family may be replaced by one superficial “happy path” test.

---

# 3. EasyCAD2 behavioral parity gate

EasyCAD2 remains the initial behavioral benchmark, not the architecture definition.

The following 25 validated behavior groups must have an explicit BiomechE-CAD acceptance path [EC2-VAL-PLAN-1.4, US1–US25; EC2-VAL-REPORT-1.4, test result table]:

| US | Behavioral capability | Acceptance path |
|---|---|---|
| US1 | license/product activation where applicable | product-level gate / not geometry |
| US2 | create patient | `XACC-001` + app acceptance |
| US3 | search/edit/delete patient | app/data acceptance |
| US4 | language + units | `XACC-002` |
| US5 | 3D printer + CNC settings | `MAN-*` + manufacturing-profile versioning |
| US6 | DX→SX mirror | `XACC-003..005` |
| US7 | DIMA/template + L/W | `XACC-006` |
| US8 | pressure import/transform | `XACC-007..010` |
| US9 | Scan3D landmarks/alignment + Image2D | `XACC-011..013` |
| US10 | thickness + flatten | `XACC-014` |
| US11 | heel/wrap/camber | `HEEL-*`, `XACC-015` |
| US12 | medial/lateral arch | `ARCH-*`, `XACC-016` |
| US13 | rear/forefoot wedges | `XACC-017` |
| US14 | element insert/position/scale/rotate | `CE-*`, `XACC-018` |
| US15 | element vertex edit/custom preset | `CE-*`, `XACC-019` |
| US16 | stiffness/material modifier region | `MAT-*`, `XACC-020` |
| US17 | sculpt radius/strength | `XACC-021` |
| US18 | scan-driven conform | `XACC-022` |
| US19 | section + height constraints | `XACC-046` |
| US20 | two-point ruler | `XACC-047` |
| US21 | production closure + STL/GCODE | `MAN-*`, `XACC-048` |
| US22 | global/per-element hardness/density | `MAT-*`, `XACC-020` |
| US23 | report | `XACC-049` |
| US24 | min-thickness detect/fix | `XACC-050` |
| US25 | save + accidental-close protection | `SCHEMA-*`, `XACC-037..039` + app close-protection gate |

The old `easycad2_geometry_parity.md` remains useful history, but this suite supersedes any implication that parity itself selects OpenSubdiv or another engine.

---

# 4. Cross-domain acceptance scenarios

## `XACC-001` — external patient identity without duplicate authority

**Given** a project linked to an external BiomechE patient ID.  
**When** the project is exported/imported.  
**Then** the internal project patient ID and external identifier remain distinct and stable.  
**Must cover:** `SCHEMA-025`.

## `XACC-002` — unit display changes do not change prescription semantics

Store an operation in canonical units; render in an alternate display unit; save/reload; return to canonical display.

**Pass:** canonical quantity round-trips within declared numerical tolerance and operation meaning is unchanged.

## `XACC-003` — semantic bilateral mirror

Mirror a RIGHT design into LEFT.

**Pass:** medial remains medial anatomically, lateral remains lateral, wedge direction/reference and semantic ROI labels transform correctly; source design remains unchanged.

## `XACC-004` — mirrored revisions diverge independently

After mirror, modify only LEFT arch height.

**Pass:** RIGHT revision hash/content does not change; LEFT receives a successor revision.

## `XACC-005` — mirror round trip

RIGHT → LEFT mirror and semantic LEFT → RIGHT mirror under the same mirror algorithm version.

**Pass:** canonical semantic parameters return to original values within defined geometrical tolerance; IDs may differ but semantics do not drift.

---

# 5. Acquisition / registration scenarios

## `XACC-006` — template morph provenance

Change template length/width/size and commit.

**Pass:** exact template version, morph parameters, units and algorithm version survive reload; source template definition resolves exactly.

## `XACC-007` — pressure remains numeric

Import a pressure dataset and render a heatmap.

**Pass:** deleting/rebuilding the heatmap does not alter numeric source values; ROI metrics reproduce from the numeric dataset.

## `XACC-008` — pressure transform direction

Apply known translation/rotation/scale registration.

**Pass:** source→target frame is explicit; inverse is not silently substituted; known landmarks/points map within tolerance.

## `XACC-009` — pressure protocol mismatch warning

Compare baseline/outcome with a controlled difference such as device, calibration, gait speed or footwear.

**Pass:** comparison state follows configured policy (`VALID_WITH_WARNINGS` or `NOT_COMPARABLE`) rather than silently producing an unqualified delta.

## `XACC-010` — ROI-version sensitivity

Compute the same metric with ROI v1 and ROI v2.

**Pass:** both results retain their ROI versions and are not silently treated as identical measurements.

## `XACC-011` — Scan3D raw evidence preservation

Import a scan, crop/clean/derive an aligned representation.

**Pass:** original asset bytes/hash remain accessible; derived scan has separate asset/provenance identity.

## `XACC-012` — landmark registration

Use heel + first/fifth metatarsal landmarks on a known fixture.

**Pass:** registration records landmark set version, source/target frames, method and error metric; replay produces equivalent transform.

## `XACC-013` — Image2D calibration

Calibrate a fixture of known length.

**Pass:** computed physical distance meets tolerance and calibration metadata survives round-trip.

---

# 6. Prescription / geometry semantics

## `XACC-014` — thickness is explicit manufacturing/design semantics

Change global thickness without changing unrelated arch/wedge prescription.

**Pass:** thickness change is independently represented and does not silently bake unrelated geometry changes into other operation parameters.

## `XACC-015` — heel components stay independent

Create a heel cup, heel relief, heel camber and soft mechanical region.

Toggle each independently.

**Pass:** each component can be enabled/disabled/revised without mutating the other three prescriptions; see `HEEL-*`.

## `XACC-016` — arch geometry vs mechanics

Create an arch with geometry dose and mechanical profile.

Change hardness/stiffness only.

**Pass:** arch geometric parameters remain semantically unchanged; outcome/mechanical state references the changed material profile separately; see `ARCH-*`, `MAT-*`.

## `XACC-017` — wedge angle/reference semantics

Apply known 2°, 4°, 6° wedge fixtures with explicit pivot/reference and full/partial extent.

**Pass:** reported resulting angle agrees within geometric tolerance and pivot/reference semantics persist through save/replay.

## `XACC-018` — anatomical corrective-element placement

Place a metatarsal element relative to a landmark line and store mm + normalized coordinate.

**Pass:** reloading/resizing according to the defined policy preserves the chosen semantic/reference representation; no conversion to anonymous XYZ-only placement.

## `XACC-019` — custom element provenance

Edit a corrective element and save a custom preset.

**Pass:** preset receives version/content hash; later preset edits do not mutate historical design revisions that used the earlier preset.

## `XACC-020` — material region not geometry alias

Assign different stiffness/hardness to a semantic ROI without changing external geometry.

**Pass:** material state changes while design geometry semantics remain unchanged except where the production realization intentionally depends on material structure.

## `XACC-021` — sculpt is replayable

Apply a known brush center/radius/strength fixture.

**Pass:** operation parameters and algorithm version replay deterministically within geometry tolerance; source acquisition/ROI references remain unchanged.

## `XACC-022` — scan conform has bounded, traceable effect

Conform only a defined ROI to a scan with strength/max-displacement constraints.

**Pass:** outside-mask geometry remains within no-change tolerance; inside mask obeys displacement bound; scan and registration versions are recorded.

---

# 7. Context / evidence / patient-experience scenarios

## `XACC-023` — context profile cannot diagnose silently

Attach an indication profile as `SUGGESTED_NOT_CONFIRMED`.

**Pass:** it does not become `USER_CONFIRMED`, does not assert diagnosis and cannot silently activate a clinical threshold requiring confirmation; covers `PROF-*`, `SCHEMA-029`.

## `XACC-024` — profile non-transfer guard

Load a threshold/preset from one population/context and attempt to apply it to an incompatible profile.

**Pass:** system blocks or explicitly warns according to profile rules; evidence source remains visible.

## `XACC-025` — PROM historical reproducibility

Save a PROM measurement, then install a newer scoring algorithm/instrument definition.

**Pass:** old score remains linked to original version/language/scoring version and is not silently recalculated; covers `PROM-*`, `SCHEMA-016`.

## `XACC-026` — adherence denominator separation

Store equal numerical percentages with denominators `STEPS` and `WEIGHT_BEARING_TIME`.

**Pass:** records are not treated as equivalent measurements solely because numeric values match.

---

# 8. Offloading / outcome scenarios

## `XACC-027` — offloading evaluates target + safety ring

Apply an offloading feature to a pressure fixture.

**Pass:** target ROI result is reported together with configured adjacent/safety-ring and remote-region metrics; improvement in target alone cannot suppress detected overload elsewhere; covers `OFF-*`.

## `XACC-028` — measured vs predicted cannot collapse

Store one measured and one model-predicted pressure outcome with equal value.

**Pass:** they remain different measurement kinds; predicted record carries model/algorithm provenance.

## `XACC-029` — before/after traceability

Baseline measurement uses revision A; outcome uses physical orthosis generated from revision B.

**Pass:** comparison report resolves both exact revisions, physical part, acquisition protocols, ROI versions and comparability state.

---

# 9. Manufacturing / QC / physical-copy scenarios

## `XACC-030` — two physical copies from one design

Manufacture two parts from the same DesignRevision in separate runs/lots.

**Pass:** two distinct `PhysicalOrthosis` IDs exist; both resolve the same design but different run/lot lineage.

## `XACC-031` — nominal vs measured material property

Supplier datasheet says one property; coupon/final-part test measures another.

**Pass:** both are stored with different `sourceType`; no overwrite or implicit averaging; covers `MAT-*`.

## `XACC-032` — Shore method guard

Attempt to store hardness `50 Shore` without scale/method where the material spec requires it.

**Pass:** validation fails or marks record incomplete; no automatic modulus conversion.

## `XACC-033` — post-processing material state

Record heat/thermoforming/curing/lamination step that can alter properties.

**Pass:** new post-process state references prior material/part state and resulting measurements; pre-process values remain accessible.

## `XACC-034` — export success is not part acceptance

Generate an STL/GCODE successfully while one blocking QC requirement is failed.

**Pass:** export artifact may be valid, but `PhysicalOrthosis` cannot reach validated `ACCEPTED` state; covers `MAN-*`, `SCHEMA-020`.

## `XACC-035` — CAD geometry vs measured manufactured geometry

Compare nominal reference geometry with a deliberately perturbed manufactured scan.

**Pass:** deviation map/metrics are separate measured QC data; the original DesignRevision is not mutated to match the manufactured defect.

## `XACC-036` — service state append-only

Record service check at T1 and T2.

**Pass:** T1 remains queryable; T2 is appended and can refer to wear/thickness/mechanical/pressure/PROM data; covers `SCHEMA-021`.

---

# 10. Revision / replay / migration scenarios

## `XACC-037` — deterministic revision replay

Rebuild a committed semantic design from:

```text
exact template snapshot
operation stack
algorithm versions
material prescription
registered source inputs
```

**Pass:** normalized semantic hash matches; derived geometry meets configured numerical tolerance/hash policy.

## `XACC-038` — historical definition immutability

Change the global template/profile/material/preset registry after a project is committed.

**Pass:** old revision continues resolving historical version/snapshot/hash and produces unchanged interpretation.

## `XACC-039` — missing exact definition fails visibly

Remove access to a required immutable definition snapshot/external version.

**Pass:** package becomes warning/error state; implementation must not silently substitute `latest`.

## `XACC-040` — migration information-loss gate

Migrate a fixture containing a field unsupported by the target schema.

**Pass:** migration records `KNOWN_NONCRITICAL`, `REQUIRES_REVIEW` or `BLOCKING` as appropriate; clinically/manufacturing significant data are not silently discarded.

## `XACC-041` — migration source preservation

Import/migrate a legacy project.

**Pass:** original source asset/hash and known source version remain preserved even when semantic reconstruction is partial.

---

# 11. Privacy / handoff / reporting scenarios

## `XACC-042` — manufacturing-minimum handoff

Export a manufacturing package under `MANUFACTURING_MINIMUM` privacy policy.

**Pass:** unnecessary direct demographics are absent while design revision, side, manufacturing profile, material requirements, artifact hashes and traceability remain sufficient.

## `XACC-043` — pseudonymized clinical package

Create a pseudonymized package and later reconnect through an authorized external patient identifier mapping.

**Pass:** internal project lineage survives pseudonymization; no accidental direct-demographic leakage in the exported manifest/assets selected by policy.

## `XACC-044` — report revision exactness

Generate report from revision N, then edit project to N+1.

**Pass:** historical report still identifies revision N and its source measurements/artifacts/hashes; it does not silently present current N+1 data.

## `XACC-045` — evidence-linked target survives bibliography/profile evolution

Update a global indication profile/evidence interpretation after a project target was accepted.

**Pass:** historical target retains profile version, copied criterion/hash and bibliography evidence reference/locator used at the time.

---

# 12. EasyCAD geometry/query/production completion cases

These cases close EasyCAD2 parity items that are not naturally represented by the cross-domain scenarios above.

## `XACC-046` — arbitrary section + height constraint

Create a known geometry fixture, define a section by two points/plane, and apply a fixed-height constraint to a controlled region.

**Pass:** section intersects the expected reference geometry within tolerance; constrained heights satisfy the specified target/tolerance; operation is replayable and source geometry/revision remains traceable.

## `XACC-047` — two-point ruler

Measure two known 3D points and two known projected/2D points.

**Pass:** returned physical distance agrees with fixture truth within coordinate-system tolerance; camera/view changes do not alter physical measurement.

## `XACC-048` — production closure + export lineage

Generate a production body using a named closure rule and export STL and, when the profile enables it, CNC/GCODE artifact.

**Pass:** output identifies DesignRevision + ManufacturingProfile + generator version + hash; required body-validity/DFM gates pass; changing the export/profile does not mutate the clinical design revision.

## `XACC-049` — report source exactness

Generate the product report from a controlled revision containing acquisition, design, material/manufacturing and outcome data.

**Pass:** report references exact source revision/artifacts/profile versions and can be regenerated semantically from the same inputs; a later project revision does not alter the historical report record.

## `XACC-050` — minimum-thickness DFM detect + correction provenance

Use a fixture containing a deliberate below-profile-minimum region.

**Pass:** QC identifies the correct region/value; correction creates an explicit DFM/manufacturing operation or successor realization; the configured minimum is profile/material/process scoped rather than a universal hard-coded 0.8 mm; original clinical prescription remains traceable.

---

# 13. Geometry-independent numerical policy

The suite distinguishes:

```text
SEMANTIC EXACTNESS
NUMERICAL TOLERANCE
BITWISE DETERMINISM
VISUAL EQUIVALENCE
```

They are not interchangeable.

Examples:

- operation type, units, side, evidence refs: **semantic exactness**;
- angle/length/registration: **numerical tolerance**;
- canonical JSON/hash fixtures: **bitwise/canonical determinism** where specified;
- screenshots: never the sole evidence for a clinical/geometric P0 requirement.

Exact tolerances remain to be frozen in coordinate/geometry/manufacturing qualification documents rather than guessed here.

---

# 14. Fixture catalog

## Existing

```text
schemas/biomeche-cad-project-0.1.schema.json
fixtures/project/minimal-valid-project.json
```

## Required next fixtures

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

Geometry fixtures may additionally include OBJ/STL/mesh/reference numeric data, but their semantics must be described independently of a chosen kernel.

---

# 15. Test implementation rules

1. Every automated test uses a stable test ID.
2. Every fixture states schema/version and expected result.
3. Negative tests are mandatory for safety/provenance guards.
4. A PASS must be machine-decidable where practical.
5. HIL/manual gates are allowed only where physical device/process evidence is genuinely required.
6. UI screenshots can supplement but cannot replace semantic/numerical assertions.
7. Failure diagnostics must identify the violated requirement/field/metric, not merely `invalid project`.
8. Acceptance data must never rely on mutable external `latest` definitions.
9. Any change to an acceptance rule that alters product meaning requires explicit spec/decision review.
10. Architecture-specific benchmarks may be added later but cannot weaken these functional gates.

---

# 16. Release gate categories

Each P0 requirement receives one of:

```text
PASS
FAIL
BLOCKED
NOT_APPLICABLE_BY_PROFILE
```

`NOT_TESTED` is not a release-pass state.

A product configuration may legitimately mark some modules not applicable, e.g. CNC on a print-only deployment, but this must be profile/configuration based and explicit.

---

# 17. Next work

Immediate implementation/specification sequence:

```text
1. create richer Project Schema fixtures
2. implement schema validator tests for SCHEMA-001..030
3. map XACC-001..050 to executable test cases
4. freeze spec/01_coordinate_registration.md
5. add numerical tolerance registry once coordinate contract is frozen
6. define BiomechE integration/report traceability
7. only then resume geometry-foundation shoot-out
```

The architecture shoot-out will therefore receive a pre-existing, kernel-independent functional/numerical contract rather than defining its own success criteria.
