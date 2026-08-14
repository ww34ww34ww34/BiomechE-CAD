# BiomechE-CAD Specification Index

Markdown under `docs/` is the canonical specification source.

## Start / resume here

- [RESUME_HERE.md](RESUME_HERE.md) — current state, DONE/TODO and exact restart point.
- [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) — **single authoritative bibliography**: stable IDs, title/citation, DOI/PMID/URL and page/section locators.
- [DECISIONS.md](DECISIONS.md) — cross-cutting product/architecture decisions.
- [research/SOURCES.md](research/SOURCES.md) — intake/research queue; not a competing bibliography.

## Current work order

```text
FUNCTIONALITY
+ EASYCAD2 PARITY
+ SCIENTIFIC / BIOMECHANICAL EVIDENCE
+ DOSE / PLACEMENT / OUTCOME / CONTEXT
        ↓
PRODUCT REQUIREMENTS
        ↓
PROJECT SCHEMA + ACCEPTANCE TESTS
        ↓
ARCHITECTURE LATER
```

OpenSubdiv vs openNURBS/ON_SubD remains intentionally parked.

---

# Canonical product specifications

| File | Status | Purpose |
|---|---|---|
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | Baseline / consolidation pending latest evidence promotion | Unified EasyCAD2-inspired functional baseline |
| [spec/CAD_ENGINE_CAPABILITY_SPEC.md](spec/CAD_ENGINE_CAPABILITY_SPEC.md) | Capability baseline; architecture parked | Geometry capabilities independent from current research priority |
| [spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md](spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md) | Current architecture-selection status | Records parked OpenSubdiv vs ON_SubD decision |
| [spec/03_geometry_operation_model.md](spec/03_geometry_operation_model.md) | Hypothesis / not frozen | Earlier control-cage/operation-stack hypothesis |
| [spec/04_base_template.md](spec/04_base_template.md) | Fixture candidate / not frozen | `ORTHO_CAGE_41x17_V0` candidate |
| [spec/05_parametric_orthosis_geometry.md](spec/05_parametric_orthosis_geometry.md) | Provisional math | Experimental operator formulas; not claimed as clinical evidence |
| [spec/06_corrective_elements.md](spec/06_corrective_elements.md) | **ACTIVE v0** | Corrective-element taxonomy, metatarsal/offload semantics and acceptance tests |
| [spec/09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) | **ACTIVE v0** | Pressure/PTI/contact area/force/COP/shear, protocol provenance, QC/DFM |
| [spec/13_use_case_profiles.md](spec/13_use_case_profiles.md) | **ACTIVE v0** | Evidence-context profiles, target provenance and non-transfer guards |

---

# Active functional/scientific research

| File | Status | Purpose |
|---|---|---|
| [research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md) | ACTIVE master matrix | `FSE-001..019` feature → evidence → requirement baseline |
| [research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md](research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md) | Batch 02 complete | Forefoot wedge, metatarsal placement, arch/heel dose |
| [research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md](research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md) | Batch 03 complete | Relief/aperture, redistribution, target+safety-ring semantics |
| [research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md](research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md) | Batch 04 complete | `ARCH-001`; geometry/mechanics/context/outcomes; `ARCH-001..014` |
| [research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md](research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md) | Batch 05 complete | `HEEL-001`; containment/relief/camber/material; `HEEL-001..015` |
| [research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md](research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md) | **Batch 06 complete** | Diabetes, metatarsalgia, flatfoot, heel pain, sport and neutral generic profiles |
| [research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md](research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md) | ARCHIVED / valid background | Library/portability research; not current work priority |

---

# Functional conclusions currently adopted

1. EasyCAD2 is behavioral evidence, not scientific truth.
2. External-source claims cite stable IDs from `BIBLIOGRAPHY.md` with truthful locators.
3. Pressure remains quantitative numeric data; rendered heatmaps are derived views.
4. Dose/placement/reference frame survive as structured prescription data.
5. Offloading = redistribution: target + adjacent/remote regions are evaluated.
6. Geometry and mechanical/material dose are independent.
7. Arch support is not one scalar.
8. Heel is not one scalar: containment, relief, camber and cushioning/material are separate.
9. Outcome comparisons are protocol-bound and measured/predicted values remain distinct.
10. Thresholds are population/context/protocol specific.
11. `IndicationProfile` is a versioned evidence-context layer, not a diagnostic engine.
12. Pediatric/adult, symptomatic/asymptomatic and walking/running evidence do not transfer silently.
13. An active diabetic plantar ulcer can trigger a different guideline pathway rather than merely another CAD preset.
14. Pressure, PROM, adherence and clinical-event outcomes remain separate observations.

---

# Initial P0 indication profiles

```text
DIABETIC_REULCERATION_PREVENTION
MECHANICAL_METATARSALGIA
FLEXIBLE_FLATFOOT
PLANTAR_HEEL_PAIN
SPORT_PERFORMANCE
GENERIC_CUSTOM_ORTHOSIS
```

See `spec/13_use_case_profiles.md` and research Batch 06.

---

# Specifications still to create/freeze

| File | Status | Purpose |
|---|---|---|
| `spec/01_coordinate_registration.md` | Planned | Coordinate spaces, units, acquisitions and registration |
| `spec/02_project_schema.md` | Planned after current evidence promotion | Versioned project schema including profiles, targets, outcomes, revisions and hashes |
| `spec/07_sculpt_and_roi_deformation.md` | Planned | Local authoring semantics and ROI provenance |
| `spec/08_material_stiffness.md` | **Research-driven next after PROM** | Material/stiffness properties, regional maps and evidence boundaries |
| `spec/10_manufacturing.md` | Planned | Manufacturing profiles / tolerances / export semantics |
| `spec/11_biomeche_integration.md` | Planned | Quantitative pressure bridge and pre/post outcome loop |
| `spec/12_reporting_traceability.md` | Planned | Prescription/design/manufacturing/outcome reports |

---

# Research queue — NEXT

1. **PROM / comfort / fit / adherence** — cross-profile outcome specification.
2. **Material durability / manufacturing evidence** — hardness/modulus/durability/process/tolerance.
3. Promote mature Batch 03–06 findings into the consolidated P0/P1 functional specification.
4. Derive Project Schema v0 from the evidence-led domain model.
5. Derive a kernel-independent acceptance suite.
6. Refine shear/COP policy after target acquisition hardware is fixed.
7. Competitor functional gap audit can proceed in parallel.
8. Only later resume OpenSubdiv vs openNURBS/ON_SubD.

---

# Validation specs / queue

| File | Status | Purpose |
|---|---|---|
| [validation/easycad2_geometry_parity.md](validation/easycad2_geometry_parity.md) | Existing behavioral coverage record | 25 EasyCAD user stories; not a frozen engine choice |
| `validation_strategy.md` | Planned | Validation hierarchy |
| `geometry_invariants.md` | Planned | Numerical invariants |
| `golden_geometry.md` | Planned | Golden fixtures / regression |
| `manufacturing_validation.md` | Planned | Thickness, watertightness, tolerances, production QC |

---

# Documentation rules

1. `docs/BIBLIOGRAPHY.md` is the single authoritative bibliography.
2. Source evidence remains separate from product decisions.
3. New sources receive stable bibliography IDs before canonical specs rely on them.
4. Exact page/figure/section locators are used where actually verified; never invent pages.
5. Vendor material is market evidence, not clinical efficacy evidence.
6. Model/FE evidence remains explicitly model-based.
7. Every P0 feature/profile eventually needs an acceptance criterion.
8. Update `RESUME_HERE.md` after substantial work.
9. Preserve superseded architecture/history in Git.
10. Do not redistribute third-party EasyCAD PDFs/screenshots publicly without rights clearance.
