# BiomechE-CAD Specification Index

Markdown under `docs/` is the canonical specification source.

## Start / resume here

1. [RESUME_HERE.md](RESUME_HERE.md) — current checkpoint, DONE/TODO and exact restart point.
2. [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) — **canonical product scope**.
3. [spec/02_project_schema.md](spec/02_project_schema.md) — persisted semantic contract.
4. [validation/functional_acceptance_suite.md](validation/functional_acceptance_suite.md) — kernel-independent cross-domain acceptance baseline.
5. [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) — frozen coordinate/registration semantics.
6. [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) — frozen BiomechE↔CAD quantitative integration semantics.
7. [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) — frozen reporting/traceability semantics.
8. [DECISIONS.md](DECISIONS.md) — cross-cutting decisions.
9. [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) — **single authoritative bibliography**.

`docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` remains a historical/audit baseline and must not be destructively rewritten to look current.

---

## Current work order

```text
FUNCTIONALITY + EASYCAD2 + SCIENTIFIC EVIDENCE     DONE baseline
        ↓
FUNCTIONAL SPEC v2                                 DONE / CANONICAL
        ↓
PROJECT SCHEMA v0                                  DONE baseline
        ↓
KERNEL-INDEPENDENT ACCEPTANCE SUITE                DONE baseline
        ↓
RICH PROJECT / ACCEPTANCE FIXTURES                 DONE current batch
        ↓
COORDINATE / REGISTRATION SEMANTICS                FROZEN v1
        ↓
BIOMECHE INTEGRATION                               FROZEN v1
        ↓
REPORTING / TRACEABILITY                           FROZEN v1
        ↓
EXECUTABLE BINT/RPT + REAL-WORLD QUALIFICATION     NEXT
        ↓
COMPETITOR DEEP AUDIT / WORKFLOW AUTOMATION        PARALLEL
        ↓
ARCHITECTURE SHOOT-OUT                             LATER
```

OpenSubdiv vs openNURBS/ON_SubD remains intentionally parked. No OCCT/Manifold/other geometry kernel has been added.

---

# Canonical product specifications

| File | Status | Purpose |
|---|---|---|
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md) | **CANONICAL v2** | Consolidated evidence-led P0/P1/P2 product scope |
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | Historical baseline preserved | Original detailed EasyCAD2-inspired baseline retained for audit/history |
| [spec/01_coordinate_registration.md](spec/01_coordinate_registration.md) | **FROZEN semantic baseline v1** | CAD/anatomical frames, side, intrinsic `s/q`, pressure/index mapping, registration algebra, mirror, tolerances classes |
| [spec/02_project_schema.md](spec/02_project_schema.md) | **ACTIVE SCHEMA BASELINE v0** | Immutable revisions, exact definitions, acquisitions, outcomes, materials, manufacturing, physical part, provenance and migration |
| [spec/06_corrective_elements.md](spec/06_corrective_elements.md) | ACTIVE v0 | Corrective-element/offload taxonomy and semantics |
| [spec/08_material_stiffness.md](spec/08_material_stiffness.md) | ACTIVE v0 | Material identity/lot/stacks/regions/effective properties/post-process/service state |
| [spec/09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) | ACTIVE v0 | Quantitative pressure/PTI/contact/force/COP/shear direction, protocol provenance and QC/DFM |
| [spec/10_manufacturing.md](spec/10_manufacturing.md) | ACTIVE v0 | Manufacturing profile/run/artifact, physical part, QC and acceptance |
| [spec/11_biomeche_integration.md](spec/11_biomeche_integration.md) | **FROZEN semantic baseline v1** | BiomechE result envelope, KPI/quality/protocol provenance, comparison, reanalysis and dynamic capability gating |
| [spec/12_reporting_traceability.md](spec/12_reporting_traceability.md) | **FROZEN semantic baseline v1** | Immutable report artifacts, exact source manifests, provenance, privacy and semantic reproducibility |
| [spec/13_use_case_profiles.md](spec/13_use_case_profiles.md) | ACTIVE v0 | Evidence-context profiles and non-transfer guards |
| [spec/14_prom_comfort_adherence.md](spec/14_prom_comfort_adherence.md) | ACTIVE v0 | PROM/function/pain/comfort/fit/satisfaction/adherence separation |

## Architecture-hypothesis files — preserved, not current selection work

| File | Status |
|---|---|
| [spec/CAD_ENGINE_CAPABILITY_SPEC.md](spec/CAD_ENGINE_CAPABILITY_SPEC.md) | capability baseline; architecture parked |
| [spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md](spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md) | parked architecture-selection status |
| [spec/03_geometry_operation_model.md](spec/03_geometry_operation_model.md) | historical hypothesis / not frozen; coordinate conflicts defer to `01_coordinate_registration.md` |
| [spec/04_base_template.md](spec/04_base_template.md) | candidate / not frozen |
| [spec/05_parametric_orthosis_geometry.md](spec/05_parametric_orthosis_geometry.md) | provisional math / not clinical evidence |

---

# Project Schema / executable fixtures

| File | Status | Purpose |
|---|---|---|
| [`schemas/biomeche-cad-project-0.1.schema.json`](../schemas/biomeche-cad-project-0.1.schema.json) | ACTIVE reference schema | JSON Schema Draft 2020-12 serialization |
| [`fixtures/project/minimal-valid-project.json`](../fixtures/project/minimal-valid-project.json) | baseline | minimal valid envelope |
| [`fixtures/project/bilateral-project.json`](../fixtures/project/bilateral-project.json) | rich fixture | bilateral ownership/mirror lineage |
| [`fixtures/project/pressure-design-outcome-loop.json`](../fixtures/project/pressure-design-outcome-loop.json) | rich fixture | pressure→design→measured-outcome loop |
| [`fixtures/project/manufacturing-qc-lineage.json`](../fixtures/project/manufacturing-qc-lineage.json) | rich fixture | design→run→artifact→part→QC lineage |
| [`fixtures/project/migration-v0.1.json`](../fixtures/project/migration-v0.1.json) | rich fixture | legacy migration provenance |
| [`tools/validate_fixtures.py`](../tools/validate_fixtures.py) | ACTIVE harness | JSON Schema + current kernel-independent semantic checks |
| [`requirements-dev.txt`](../requirements-dev.txt) | ACTIVE | validator development dependency |

## Acceptance fixtures

Existing rich batch:

```text
mirror-semantics.json
registration-known-transform.json
roi-version-comparison.json
profile-non-transfer.json
prom-versioning.json
offload-safety-ring.json
material-property-provenance.json
blocking-qc.json
```

New integration/reporting fixtures:

```text
fixtures/acceptance/biomeche-result-import.json
fixtures/acceptance/report-source-exactness.json
```

The new fixtures exercise actual Project Schema v0 entities rather than detached expectation JSON.

---

# Acceptance namespaces

Canonical cross-domain suite:

```text
SCHEMA-001..030
OFF-001..009
CE-001..010
ARCH-001..014
HEEL-001..015
PROF-001..012
PROM-001..020
MAT-001..018
MAN-001..018
XACC-001..050
```

New domain-contract families defined in their frozen specs:

```text
BINT-001..018  -> spec/11_biomeche_integration.md
RPT-001..018   -> spec/12_reporting_traceability.md
```

The next validation-maintenance pass should merge the `BINT/RPT` summaries into `functional_acceptance_suite.md` without changing their frozen semantics.

---

# Current BiomechE integration pin

Integration work currently references:

```text
ww34ww34ww34/BiomechE
d5e467a1a5551f4280cfef5b483da1999f1566e0
```

The upstream state is frozen through dynamic-gait `DYN-005`; `DYN-006` dynamic pressure/force/integral/region semantics are still upstream NEXT. CAD therefore pins the supported capability/version and does not invent replacement formulas.

Canonical source ID: `ARCH-BIOMECHE-INTEGRATION-2026-08-15`.

---

# Functional/scientific research

| File | Status | Purpose |
|---|---|---|
| [research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md) | ACTIVE master matrix | feature → evidence → requirement mapping |
| [research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md](research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md) | complete | wedge/metatarsal/arch/heel dose |
| [research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md](research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md) | complete | relief/offloading redistribution |
| [research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md](research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md) | complete | arch geometry/mechanics/context/outcome |
| [research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md](research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md) | complete | heel containment/relief/camber/material |
| [research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md](research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md) | complete | indication/profile boundaries |
| [research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md](research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md) | complete | outcome-instrument and adherence governance |
| [research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md](research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md) | complete | material/process/QC/service provenance |
| [research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md](research/COMPETITOR_FUNCTIONAL_GAP_AUDIT_2026-08-15.md) | **first public-source baseline** | current orthotic CAD/CAM functional-gap audit |
| [research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md](research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md) | archived background | library/portability research; not current priority |

---

# Current adopted conclusions

1. EasyCAD2 is behavioral evidence, not scientific truth.
2. Pressure remains numeric quantitative data; heatmaps are derived views.
3. Dose/placement/reference/units survive as structured prescription semantics.
4. Offloading is evaluated as redistribution: target + safety-ring + remote regions.
5. Geometry and material/mechanical dose are separate.
6. Thresholds are population/context/protocol/ROI specific.
7. Profile attachment is versioned evidence context, not diagnosis or auto-prescription.
8. PROM/pain/function/comfort/fit/satisfaction/adherence remain distinct.
9. Material nominal/manufactured/effective/service-aged states remain distinct.
10. `CAD export != ManufacturingArtifact != PhysicalOrthosis != accepted part`.
11. Committed `DesignRevision` and issued reports are immutable historical entities.
12. Raw acquisitions/assets and BiomechE result bundles are hash-addressed provenance anchors.
13. BiomechE is quantitative KPI authority; CAD owns prescription/design/lifecycle semantics.
14. `UNAVAILABLE` measurement is not zero; quality state survives integration.
15. Cross-device/protocol pressure comparison is explicitly gated.
16. Reanalysis creates new result/measurement identities rather than rewriting history.
17. Reports retain exact source refs/manifests; PDF/HTML/charts are presentation artifacts.
18. Semantic report reproducibility is distinguished from byte-identical rendering.
19. No hidden universal `BiomechE Score`.
20. Architecture selection remains downstream of these contracts.

---

# Work queue — NEXT

1. Run/CI-qualify the expanded fixture validator and retain a machine-readable validation result.
2. Merge `BINT-*` and `RPT-*` catalog summaries into `functional_acceptance_suite.md` and expand executable coverage.
3. Define/qualify real pressure acquisition profiles: device/calibration/protocol/step/window and cross-device policy.
4. Follow upstream BiomechE `DYN-006+` and bind dynamic pressure/force/region semantics only after they freeze.
5. Deepen competitor audit from manuals/trials; address `GAP-COMP-001` workflow macros first.
6. Qualify actual material/manufacturing profiles and tolerances.
7. Select built-in PROM instruments only after population/psychometric/licensing review.
8. Only after these: resume OpenSubdiv vs openNURBS/ON_SubD shoot-out.

---

# Documentation rules

1. `docs/BIBLIOGRAPHY.md` is the single authoritative bibliography.
2. Add a source ID before a canonical claim relies on it; never invent page numbers.
3. Vendor pages establish market capabilities only, not efficacy.
4. Scientific thresholds remain population/protocol/ROI specific.
5. Standards are used only to the scope actually reviewed.
6. Preserve superseded historical/architecture material in Git.
7. Update `RESUME_HERE.md` and this index after substantial work.
8. Architecture dependencies must still earn entry through a named requirement/failing fixture.
