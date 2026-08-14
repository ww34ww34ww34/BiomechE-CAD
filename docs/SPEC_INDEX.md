# BiomechE-CAD Specification Index

Markdown in this repository is the canonical specification source.

## Start / resume here

- [RESUME_HERE.md](RESUME_HERE.md) — current state, source hierarchy, DONE/TODO and exact restart point.
- [Canonical bibliography](BIBLIOGRAPHY.md) — **authoritative source IDs, full titles/citations, DOI/PMID/URLs and page/section locators used by all other documents.**
- [Architectural and product decisions](DECISIONS.md) — current decisions and open questions.
- [Research sources](research/SOURCES.md) — source intake, research queue and verification notes; bibliographic metadata must ultimately resolve to `BIBLIOGRAPHY.md`.
- [Functional + Scientific Evidence Matrix](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md) — **current active research baseline**: feature → EasyCAD2 evidence → literature → parameters → outcomes → priority.
- [Parameter / dose evidence batch](research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md) — forefoot wedge, metatarsal placement, arch geometry/hardness and heel containment/cushioning evidence.
- [Relief / offloading evidence batch](research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md) — relief/aperture semantics, target ROI + surrounding safety region, load redistribution and offloading acceptance rules.
- [Arch support deep dive](research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md) — **ARCH-001 complete**: arch geometry dose, hardness/stiffness, redistribution, population/task context, evidence gaps and `ARCH-001..014` acceptance semantics.
- [EasyCAD2 primary reference pack](references/easycad2/README.md) — manual, validation plan/report, versions, source links and page map.

## Current work priority

```text
FUNCTIONALITY
+ EASYCAD2 PARITY
+ SCIENTIFIC / BIOMECHANICAL EVIDENCE
+ MEASURABLE DOSE / PLACEMENT / OUTCOME
        ↓
PRODUCT REQUIREMENTS
        ↓
ARCHITECTURE LATER
```

The OpenSubdiv vs openNURBS/ON_SubD decision is intentionally parked.

---

## Current canonical product specifications

| File | Status | Purpose |
|---|---|---|
| [BIOMECHE_CAD_FUNCTIONAL_SPEC.md](spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md) | **Baseline / consolidated** | Unified EasyCAD2-inspired product/clinical functional specification |
| [CAD_ENGINE_CAPABILITY_SPEC.md](spec/CAD_ENGINE_CAPABILITY_SPEC.md) | **Capability baseline; architecture portion under addendum** | Geometry capability analysis developed during the previous architecture phase |
| [CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md](spec/CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md) | **CURRENT architecture-selection status** | Parks kernel selection and records future OpenSubdiv vs openNURBS/ON_SubD shoot-out |
| [03_geometry_operation_model.md](spec/03_geometry_operation_model.md) | **Hypothesis / not frozen** | Earlier control-cage/operation-stack model retained for later qualification |
| [04_base_template.md](spec/04_base_template.md) | **Fixture candidate / not frozen** | `ORTHO_CAGE_41x17_V0` candidate and BT qualification gates |
| [05_parametric_orthosis_geometry.md](spec/05_parametric_orthosis_geometry.md) | **Provisional math / not clinical evidence** | Reference formulas created for implementation experiments; not claimed EasyCAD2 or literature formulas |
| [06_corrective_elements.md](spec/06_corrective_elements.md) | **ACTIVE functional baseline v0** | Evidence-led corrective element taxonomy, anatomical placement, metatarsal pad/bar/dome/relief semantics and acceptance tests |
| [09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) | **ACTIVE functional baseline v0** | Peak pressure/PTI/contact-area/force/COP/shear policy, trial provenance, comparability, contextual thresholds, geometric QC and DFM |

---

## Active research specifications

| File | Status | Purpose |
|---|---|---|
| [FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md) | **ACTIVE / batch 1** | Main feature/evidence matrix; separates EC2 evidence, literature confidence, product requirement and P0/P1/P2 |
| [FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md](research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md) | **ACTIVE / batch 2 / bibliography-migrated** | Dose/placement detail for forefoot wedge, metatarsal pad, arch and heel features |
| [FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md](research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md) | **ACTIVE / batch 3 / bibliography-migrated** | Relief/aperture evidence, redistribution risks, target+safety-ring outcome model and OFF-001..009 acceptance semantics |
| [FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md](research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md) | **ACTIVE / batch 4 / ARCH-001 COMPLETE** | Height, longitudinal placement, shape, stiffness/hardness, redistribution, context profiles, structural outcomes, evidence gaps and ARCH-001..014 |
| [GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md](research/architecture/GEOMETRY_STACK_DEEP_RESEARCH_VALIDATED_2026-08-14.md) | **ARCHIVED / valid background** | Validated library/portability research; preserved but not current work priority |

---

## Validation specifications

| File | Status | Purpose |
|---|---|---|
| [easycad2_geometry_parity.md](validation/easycad2_geometry_parity.md) | **Behavioral architecture-coverage record** | Maps all 25 EasyCAD2 1.4 validation stories to the previous control-cage hypothesis; useful as feature inventory, not a frozen engine choice |
| `validation_strategy.md` | Planned | Overall validation hierarchy |
| `geometry_invariants.md` | Planned | Numerical invariants once product requirements are frozen |
| `golden_geometry.md` | Planned | Golden fixture format and regression policy |
| `manufacturing_validation.md` | Planned | Watertightness, thickness, orientation and production validation |

---

## Common specifications still to freeze

These should now be driven from the functional/evidence matrix rather than from a library API:

| File | Status | Purpose |
|---|---|---|
| `spec/01_coordinate_registration.md` | Planned | Coordinate spaces, units and acquisition registration |
| `spec/02_project_schema.md` | Planned | Versioned project schema, acquisitions, prescriptions, outcomes, revisions and hashes |
| [06_corrective_elements.md](spec/06_corrective_elements.md) | **v0 ACTIVE / bibliography-migrated** | Clinically named element library, anatomical placement, dimensions/dose, metatarsal family, neighboring-load analysis and acceptance metrics |
| `spec/07_sculpt_and_roi_deformation.md` | Planned | Local authoring semantics and ROI provenance |
| `spec/08_material_stiffness.md` | **Research-driven after heel/use-case pass** | Material/stiffness properties, regional maps and evidence boundaries |
| [09_analysis_qc_dfm.md](spec/09_analysis_qc_dfm.md) | **v0 ACTIVE / bibliography-migrated** | Pressure/outcome metrics, protocol provenance, compatibility, contextual thresholds, target/neighbor safety, geometry QC and DFM |
| `spec/10_manufacturing.md` | Planned | Manufacturing profiles and export semantics |
| `spec/11_biomeche_integration.md` | **Research-driven next phase** | Quantitative pressure bridge, ROI, pre/post outcome loop and provenance |
| `spec/12_reporting_traceability.md` | Planned | Prescription/design/manufacturing/outcome traceability and reports |

---

## Functional research rules

1. EasyCAD2 establishes a behavioral reference, not scientific truth.
2. Literature supports or limits the *purpose and measurable semantics* of a feature; it does not dictate the geometry kernel.
3. Population-specific evidence must remain population-specific.
4. A dose or placement shown to matter must be preserved as structured data with units/reference frame.
5. Pressure is quantitative data; target ROI and neighboring load-transfer effects should both be measurable.
6. Geometry and material/mechanical properties are separate prescription dimensions.
7. PROM/comfort/fit/adherence should link to the exact design/manufacturing revision.
8. No architecture library should be selected simply because it contains more features.
9. Offloading is treated as redistribution: local benefit must be checked against adjacent and remote loading.
10. Literature-derived placement values may become evidence-linked presets, never universal hidden defaults.
11. Pressure/outcome comparisons are protocol-bound; device/calibration/speed/steps/ROI-version provenance is part of the result.
12. Measured and predicted biomechanical outcomes must remain separate data classes.
13. Any concept derived from an external source should cite a stable ID from `BIBLIOGRAPHY.md`, with the most precise truthful locator available.
14. Exact page numbers are required for manual/PDF evidence when available; for web/abstract-only evidence cite the section (`Abstract—Results`, `Fig. 6`, etc.) rather than inventing a page.
15. Model-based evidence may justify keeping a design parameter explicit, but cannot silently become a clinical preset.
16. Arch geometry dose and arch mechanical dose remain independently inspectable/versioned.

---

## Research queue

### Functional/scientific

1. **heel cup/wrap/camber geometry vs cushioning/material — NEXT**;
2. use-case/population profiles: diabetic offloading, metatarsalgia, flatfoot, plantar heel pain, sport;
3. comfort/fit/adherence and PROM selection;
4. material durability/manufacturing evidence;
5. promote mature arch/offloading/corrective-element findings into the consolidated functional specification;
6. refine corrective-element presets only where evidence and population context justify them;
7. refine shear/COP policy as compatible acquisition hardware is defined;
8. continue migrating older research/spec documents to canonical bibliography IDs.

### Arch-specific open evidence gaps

- longitudinal arch-support extent dose;
- peak longitudinal location dose;
- curvature/roundness isolated effects;
- long-term tolerance thresholds for elevated medial-midfoot loading;
- interaction with footwear volume/fit and long-term material creep.

### Competitors

- ParoContour / DIERS;
- FitFoot360;
- Rodin4D / Neo;
- Vorum / Canfit;
- others discovered during research.

Competitors should be mapped against the **functional/scientific taxonomy**, not used as scientific evidence.

---

## Architecture queue — PARKED

When functional requirements are mature enough, resume:

```text
OpenSubdiv 3.7
    vs
openNURBS / ON_SubD 8.x
```

with one foundation selected for P0 if possible. See `CAD_ENGINE_ARCHITECTURE_STATUS_2026-08-14.md`.

---

## Documentation rules

1. `docs/BIBLIOGRAPHY.md` is the single authoritative bibliography.
2. Source evidence remains separate from engineering decisions.
3. New scientific/vendor sources are first recorded/verified, then assigned a stable bibliography ID before canonical specs rely on them.
4. `docs/research/SOURCES.md` is an intake/research queue, not a competing bibliography.
5. User-provided implementation facts are labeled separately when not independently documented.
6. Every P0 feature eventually needs acceptance criteria.
7. Preserve superseded architecture in Git history/research notes.
8. Update `RESUME_HERE.md` after substantial work.
9. Do not redistribute third-party EasyCAD2 PDFs/screenshots in the public repository without explicit rights clearance.
10. Never invent a page/section locator; use the most precise source location actually verified.
