# BiomechE-CAD Specification Index

Markdown under `docs/` is the canonical specification source.

## Start / resume here

- [RESUME_HERE.md](RESUME_HERE.md) — current state, DONE/TODO and exact restart point.
- [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) — **single authoritative bibliography**: stable IDs, title/citation, DOI/PMID/URL, standards and truthful page/section locators.
- [DECISIONS.md](DECISIONS.md) — cross-cutting product/architecture decisions.
- [research/SOURCES.md](research/SOURCES.md) — intake/research queue; not a competing bibliography.

## Current work order

```text
FUNCTIONALITY + EASYCAD2 PARITY + EVIDENCE
        ↓
FUNCTIONAL SPEC v2                         DONE / CANONICAL
        ↓
PROJECT SCHEMA v0                         DONE baseline
        ↓
KERNEL-INDEPENDENT ACCEPTANCE SUITE       DONE baseline
        ↓
RICH FIXTURES + EXECUTABLE VALIDATION     DONE current batch
        ↓
COORDINATE / REGISTRATION SEMANTICS       FROZEN baseline
        ↓
BIOMECHE INTEGRATION                      NEXT
        ↓
REPORTING / TRACEABILITY                  NEXT
        ↓
COMPETITOR + REAL-WORLD QUALIFICATION     PARALLEL
        ↓
ARCHITECTURE SHOOT-OUT                    LATER
```

OpenSubdiv vs openNURBS/ON_SubD remains intentionally parked. No OCCT/Manifold/other geometry kernel has been added.

---

# Canonical product specifications

| File | Status | Purpose |
|---|---|---|
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) | **CANONICAL v2** | Consolidated evidence-led product scope, P0/P1/P2 priorities and cross-domain requirements |
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | Historical baseline preserved | Original detailed baseline retained for audit/history |
| [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) | **FROZEN semantic baseline v1** | Canonical CAD/anatomical frames, side, medial/lateral, intrinsic `s/q`, pressure/index mapping, Scan3D/Image2D registration, transform algebra, mirror and tolerance classes |
| [spec/02_project_schema.md](spec/02_project_schema.md) | **ACTIVE SCHEMA BASELINE v0** | Logical persisted contract: immutable revisions, exact definition snapshots, acquisitions, outcomes, materials, manufacturing, physical parts, provenance and migration |
| [spec/06_corrective_elements.md](spec/06_corrective_elements.md) | **ACTIVE v0** | Corrective-element taxonomy, metatarsal/offload semantics and acceptance tests |
| [spec/08_material_stiffness.md](spec/08_material_stiffness.md) | **ACTIVE v0** | Material identity/lot, stacks/regions, effective properties, post-process and service aging |
| [spec/09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) | **ACTIVE v0** | Pressure/PTI/contact area/force/COP/shear, protocol provenance, QC/DFM |
| [spec/10_manufacturing.md](spec/10_manufacturing.md) | **ACTIVE v0** | Manufacturing profiles/runs, artifacts, QC/acceptance and physical-part identity |
| [spec/13_use_case_profiles.md](spec/13_use_case_profiles.md) | **ACTIVE v0** | Evidence-context profiles, target provenance and non-transfer guards |
| [spec/14_prom_comfort_adherence.md](spec/14_prom_comfort_adherence.md) | **ACTIVE v0** | PROM registry and pain/function/comfort/fit/satisfaction/adherence separation |
| [spec/CAD_ENGINE_CAPABILITY_SPEC.md](spec/CAD_ENGINE_CAPABILITY_SPEC.md) | Capability baseline; architecture parked | Geometry capabilities independent from current research priority |
| [spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md](spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md) | Architecture status | Records parked OpenSubdiv vs ON_SubD decision |
| [spec/03_geometry_operation_model.md](spec/03_geometry_operation_model.md) | Historical hypothesis / not frozen | Earlier control-cage/operation-stack hypothesis; coordinate semantics are superseded by `01_coordinate_registration.md` where conflicting |
| [spec/04_base_template.md](spec/04_base_template.md) | Fixture candidate / not frozen | `ORTHO_CAGE_41x17_V0` candidate |
| [spec/05_parametric_orthosis_geometry.md](spec/05_parametric_orthosis_geometry.md) | Provisional math | Experimental operator formulas; not clinical evidence |

## Project Schema / fixtures / executable checks

Reference serialization:

- [`schemas/biomeche-cad-project-0.1.schema.json`](../schemas/biomeche-cad-project-0.1.schema.json) — JSON Schema Draft 2020-12 reference schema.
- [`fixtures/project/minimal-valid-project.json`](../fixtures/project/minimal-valid-project.json) — minimal bootstrap fixture.

Rich project fixtures:

- `fixtures/project/bilateral-project.json`
- `fixtures/project/pressure-design-outcome-loop.json`
- `fixtures/project/manufacturing-qc-lineage.json`
- `fixtures/project/migration-v0.1.json`

Kernel-independent acceptance fixtures:

- `fixtures/acceptance/mirror-semantics.json`
- `fixtures/acceptance/registration-known-transform.json`
- `fixtures/acceptance/roi-version-comparison.json`
- `fixtures/acceptance/profile-non-transfer.json`
- `fixtures/acceptance/prom-versioning.json`
- `fixtures/acceptance/offload-safety-ring.json`
- `fixtures/acceptance/material-property-provenance.json`
- `fixtures/acceptance/blocking-qc.json`

Executable harness:

```text
python -m pip install -r requirements-dev.txt
python tools/validate_fixtures.py
```

The harness runs the canonical JSON Schema first and then current kernel-independent semantic checks. It intentionally does **not** claim coverage of geometry-dependent acceptance tests or every `SCHEMA-*`/`XACC-*` ID.

---

# Validation specifications

| File | Status | Purpose |
|---|---|---|
| [validation/functional_acceptance_suite.md](validation/functional_acceptance_suite.md) | **ACTIVE v0** | Kernel-independent release contract joining `SCHEMA/OFF/CE/ARCH/HEEL/PROF/PROM/MAT/MAN` and `XACC-001..050` |
| [validation/easycad2_geometry_parity.md](validation/easycad2_geometry_parity.md) | Historical architecture-coverage record | 25 EasyCAD user stories; behavioral inventory, not engine-selection baseline |
| `validation_strategy.md` | Planned | Validation hierarchy |
| `geometry_invariants.md` | Planned | Numerical invariants after actual geometry operators exist |
| `golden_geometry.md` | Planned | Golden geometry/regression fixtures |
| `manufacturing_validation.md` | Planned | Physical/material/process validation |

The current rich fixture batch exercises both expected-valid state and expected blocking/non-comparable state; visual screenshots remain supplementary rather than P0 substitutes for semantic/numerical checks.

---

# Active functional/scientific research

| File | Status | Purpose |
|---|---|---|
| [research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md) | ACTIVE master matrix | `FSE-001..019` feature → evidence → requirement baseline |
| [research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md](research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md) | Complete | Forefoot wedge, metatarsal placement, arch/heel dose |
| [research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md](research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md) | Complete | Relief/aperture, redistribution, target+safety-ring semantics |
| [research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md](research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md) | Complete | Arch geometry/mechanics/context/outcomes |
| [research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md](research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md) | Complete | Heel containment/relief/camber/material |
| [research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md](research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md) | Complete | Diabetes, metatarsalgia, flatfoot, heel pain, sport, generic |
| [research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md](research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md) | Complete | PROM, comfort/fit and adherence semantics |
| [research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md](research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md) | Complete | Material/manufacturing provenance and QC |
| [research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md](research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md) | ARCHIVED valid background | Library/portability research; not current priority |

New coordinate/registration evidence is centralized in `BIBLIOGRAPHY.md` as `REF-CAD-107`, `STD-ISB-GLOBAL-CS-1995`, `STD-ISB-FOOT-KINEMATICS-2021` plus the pinned internal integration snapshot `ARCH-BIOMECHE-COORD-2026-08-14`.

---

# Core conclusions currently adopted

1. EasyCAD2 is behavioral evidence, not scientific truth.
2. External-source claims cite stable bibliography IDs with truthful locators.
3. Pressure remains quantitative numeric data; heatmaps are derived views.
4. Dose/placement/reference frame survive as structured prescription data.
5. Offloading = redistribution: target + safety ring + remote regions.
6. Geometry dose and mechanical/material dose are independent.
7. Arch and heel are multi-parameter prescriptions.
8. Outcome comparisons are protocol/ROI/version bound; measured and predicted values remain distinct.
9. Thresholds are population/context/protocol specific.
10. Patient experience constructs remain separate; no hidden universal score.
11. Material nominal, effective/manufactured and service-aged states are distinct.
12. CAD export, manufacturing artifact, physical part and accepted part are distinct identities/states.
13. Committed `DesignRevision` is immutable; edits create successor revisions.
14. Definitions resolve exact `id + version + hash/snapshot`, never implicit `latest`.
15. Raw acquisitions/assets are immutable and hash-addressable.
16. Project schema is storage/container independent.
17. Coordinate semantics are now frozen independently of the future geometry kernel.
18. `CAD-ANAT-1`: right-handed; `+X` heel→distal, `+Y` subject-right→subject-left, `+Z` plantar→dorsal.
19. Matrix memory orientation never implies physical/anatomical orientation.
20. Intrinsic `s/q` is side-normalized; semantic mirror preserves `s/q` meaning while reflecting canonical `Y`.
21. Persisted registrations are explicit source→target transforms with column-vector algebra.
22. Real acquisition/registration tolerances remain qualification-specific `OPEN` values rather than invented constants.
23. Acceptance criteria precede architecture selection.

---

# Specifications still to create/freeze

| File | Status | Purpose |
|---|---|---|
| `spec/11_biomeche_integration.md` | **NEXT** | Exact BiomechE acquisition/pressure adapter, pinned source contract, pre/post outcome compatibility |
| `spec/12_reporting_traceability.md` | **NEXT** | Prescription/design/manufacturing/outcome reports and traceability views |
| `spec/07_sculpt_and_roi_deformation.md` | Planned | Local authoring semantics and ROI provenance |

---

# Work queue — NEXT

1. **Create/freeze `spec/11_biomeche_integration.md`** against the pinned BiomechE coordinate/acquisition contracts.
2. **Create/freeze `spec/12_reporting_traceability.md`**.
3. Expand executable acceptance coverage for additional kernel-independent `SCHEMA-* / XACC-*` cases; then add geometry fixtures only when operators exist.
4. Qualify real pressure/scan/Image2D systems so `OPEN` acquisition/registration tolerances can become system-specific acceptance criteria.
5. Competitor functional-gap audit can proceed in parallel.
6. Select/qualify built-in PROMs and real material/process profiles separately.
7. Only later resume OpenSubdiv vs openNURBS/ON_SubD.

---

# Documentation rules

1. `docs/BIBLIOGRAPHY.md` is the single authoritative bibliography.
2. Source evidence remains separate from product decisions.
3. New sources receive stable bibliography IDs before canonical specs rely on them.
4. Never invent pages or tolerance values.
5. Vendor material is market evidence, not clinical efficacy evidence.
6. Model/FE evidence remains explicitly model-based.
7. Every P0 feature/profile needs acceptance coverage.
8. Standards constrain only the semantics within their reviewed scope.
9. Update `RESUME_HERE.md` and this index after substantial work.
10. Preserve superseded architecture/history in Git.
11. Do not redistribute third-party EasyCAD PDFs/screenshots or questionnaire content publicly without rights clearance.
