# BiomechE-CAD Specification Index

Markdown under `docs/` is the canonical specification source.

## Start / resume here

- [RESUME_HERE.md](RESUME_HERE.md) — current state, DONE/TODO and exact restart point.
- [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) — **single authoritative bibliography**: stable IDs, title/citation, DOI/PMID/URL, standards and page/section locators.
- [DECISIONS.md](DECISIONS.md) — cross-cutting product/architecture decisions.
- [research/SOURCES.md](research/SOURCES.md) — intake/research queue; not a competing bibliography.

## Current work order

```text
FUNCTIONALITY
+ EASYCAD2 PARITY
+ SCIENTIFIC / BIOMECHANICAL EVIDENCE
+ DOSE / PLACEMENT / OUTCOME / CONTEXT
+ MATERIAL / PROCESS / MANUFACTURED STATE
        ↓
CONSOLIDATED PRODUCT REQUIREMENTS
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
| [spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | Baseline / **next consolidation target** | Unified EasyCAD2-inspired functional baseline; needs promotion of mature Batch 03–08 results |
| [spec/CAD_ENGINE_CAPABILITY_SPEC.md](spec/CAD_ENGINE_CAPABILITY_SPEC.md) | Capability baseline; architecture parked | Geometry capabilities independent from current research priority |
| [spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md](spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md) | Current architecture-selection status | Records parked OpenSubdiv vs ON_SubD decision |
| [spec/03_geometry_operation_model.md](spec/03_geometry_operation_model.md) | Hypothesis / not frozen | Earlier control-cage/operation-stack hypothesis |
| [spec/04_base_template.md](spec/04_base_template.md) | Fixture candidate / not frozen | `ORTHO_CAGE_41x17_V0` candidate |
| [spec/05_parametric_orthosis_geometry.md](spec/05_parametric_orthosis_geometry.md) | Provisional math | Experimental operator formulas; not claimed as clinical evidence |
| [spec/06_corrective_elements.md](spec/06_corrective_elements.md) | **ACTIVE v0** | Corrective-element taxonomy, metatarsal/offload semantics and acceptance tests |
| [spec/08_material_stiffness.md](spec/08_material_stiffness.md) | **ACTIVE v0** | Material identity/lot, hardness-method semantics, stacks/regions, effective properties, post-process and service aging |
| [spec/09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) | **ACTIVE v0** | Pressure/PTI/contact area/force/COP/shear, protocol provenance, QC/DFM |
| [spec/10_manufacturing.md](spec/10_manufacturing.md) | **ACTIVE v0** | Manufacturing profiles/runs, AM/CNC provenance, immutable artifacts, QC/acceptance and physical-part identity |
| [spec/13_use_case_profiles.md](spec/13_use_case_profiles.md) | **ACTIVE v0** | Evidence-context profiles, target provenance and non-transfer guards |
| [spec/14_prom_comfort_adherence.md](spec/14_prom_comfort_adherence.md) | **ACTIVE v0** | PROM registry, pain/function/comfort/fit/satisfaction/adherence separation, wear exposure and licensing governance |

---

# Active functional/scientific research

| File | Status | Purpose |
|---|---|---|
| [research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md) | ACTIVE master matrix | `FSE-001..019` feature → evidence → requirement baseline |
| [research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md](research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md) | Batch 02 complete | Forefoot wedge, metatarsal placement, arch/heel dose |
| [research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md](research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md) | Batch 03 complete | Relief/aperture, redistribution, target+safety-ring semantics |
| [research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md](research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md) | Batch 04 complete | `ARCH-001`; geometry/mechanics/context/outcomes; `ARCH-001..014` |
| [research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md](research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md) | Batch 05 complete | `HEEL-001`; containment/relief/camber/material; `HEEL-001..015` |
| [research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md](research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md) | Batch 06 complete | Diabetes, metatarsalgia, flatfoot, heel pain, sport and neutral generic profiles |
| [research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md](research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md) | Batch 07 complete | `PROM-001`: instrument/version/language, multidimensional patient experience and objective/subjective adherence semantics |
| [research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md](research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md) | **Batch 08 complete** | `MAT-001 / MAN-001`: nominal material vs effective/manufactured/service state, cyclic durability, AM/CNC process provenance and acceptance semantics |
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
14. Pain, function, comfort, fit/usability, satisfaction and adherence are separate outcome constructs.
15. PROM identity includes exact instrument version, language/adaptation and scoring algorithm version.
16. MID/MCID/MDC/SEM values are instrument/domain/population/context specific rather than universal constants.
17. Adherence preserves method and denominator; hours worn, weight-bearing exposure and percentage of steps are not interchangeable.
18. No hidden universal `BiomechE Score` is allowed without an independently validated, transparent profile-specific definition.
19. Questionnaire text/translations/scoring assets require explicit licensing/redistribution review before bundling.
20. Material name / supplier datasheet property is not the same as manufactured final-part property.
21. Hardness requires scale + method; Shore hardness is not a silent proxy for Young/effective modulus.
22. Thickness, material-stack order, interfaces and property-changing post-processing are first-class material/manufacturing data.
23. Base polymer and effective lattice/infill stiffness are separate properties.
24. Initial and service-aged material states remain distinct; visual compression alone is not a universal replacement rule.
25. AM/CNC manufacturing is a versioned process; export success does not imply part acceptance.
26. CAD nominal geometry and manufactured measured geometry remain distinct.
27. Qualified profile-defined blocking QC failures prevent validated-production status.
28. Standards provide test/qualification semantics; they do not silently become universal clinical acceptance thresholds.

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
| `spec/02_project_schema.md` | Planned after evidence promotion | Versioned project schema including profiles, targets, PROM/adherence, materials, manufacturing, outcomes, physical artifacts, revisions and hashes |
| `spec/07_sculpt_and_roi_deformation.md` | Planned | Local authoring semantics and ROI provenance |
| `spec/11_biomeche_integration.md` | Planned | Quantitative pressure bridge and pre/post outcome loop |
| `spec/12_reporting_traceability.md` | Planned | Prescription/design/manufacturing/outcome reports |

---

# Research / specification queue — NEXT

1. **Promote mature Batch 03–08 findings into `BIOMECHE_CAD_FUNCTIONAL_SPEC.md`** and reconcile P0/P1/P2 priorities without losing provenance.
2. Derive `Project Schema v0` from the evidence-led domain model.
3. Derive a kernel-independent functional acceptance suite from `OFF / CE / ARCH / HEEL / PROF / PROM / MAT / MAN` semantics.
4. Refine shear/COP policy after target acquisition hardware is fixed.
5. Competitor functional gap audit can proceed in parallel.
6. Select actual built-in PROMs only after profile fit, psychometric and licensing review.
7. Qualify real product material/process profiles and acceptance limits separately from generic literature/test standards.
8. Only later resume OpenSubdiv vs openNURBS/ON_SubD.

---

# Validation specs / queue

| File | Status | Purpose |
|---|---|---|
| [validation/easycad2_geometry_parity.md](validation/easycad2_geometry_parity.md) | Existing behavioral coverage record | 25 EasyCAD user stories; not a frozen engine choice |
| `validation_strategy.md` | Planned | Validation hierarchy |
| `geometry_invariants.md` | Planned | Numerical invariants |
| `golden_geometry.md` | Planned | Golden fixtures / regression |
| `manufacturing_validation.md` | Planned; now driven by spec 08/10 | Thickness, geometry trueness, materials/process/QC and production validation |

---

# Documentation rules

1. `docs/BIBLIOGRAPHY.md` is the single authoritative bibliography.
2. Source evidence remains separate from product decisions.
3. New sources receive stable bibliography IDs before canonical specs rely on them.
4. Exact page/figure/section locators are used where actually verified; never invent pages.
5. Vendor material is market evidence, not clinical efficacy evidence.
6. Model/FE evidence remains explicitly model-based.
7. Every P0 feature/profile eventually needs an acceptance criterion.
8. PROM/instrument definitions preserve exact version/language and licensing status.
9. Standards abstracts/scopes support high-level test semantics; claiming full standard compliance requires controlled access and applicability review.
10. A test standard does not by itself define a universal product acceptance limit.
11. Update `RESUME_HERE.md` after substantial work.
12. Preserve superseded architecture/history in Git.
13. Do not redistribute third-party EasyCAD PDFs/screenshots or questionnaire content publicly without rights clearance.
