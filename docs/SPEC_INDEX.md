# BiomechE-CAD Specification Index

Markdown in this repository is the canonical specification source.

## Start / resume here

- [RESUME_HERE.md](RESUME_HERE.md) — current state, source hierarchy, DONE/TODO and exact restart point.
- [Architectural and product decisions](DECISIONS.md) — current decisions and open questions.
- [Research sources](research/SOURCES.md) — primary EasyCAD2 documents and scientific source inventory.
- [Functional + Scientific Evidence Matrix](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md) — **current active research baseline**: feature → EasyCAD2 evidence → literature → parameters → outcomes → priority.
- [Parameter / dose evidence batch](research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md) — forefoot wedge, metatarsal placement, arch geometry/hardness and heel containment/cushioning evidence.
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

---

## Active research specifications

| File | Status | Purpose |
|---|---|---|
| [FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md](research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md) | **ACTIVE / batch 1** | Main feature/evidence matrix; separates EC2 evidence, literature confidence, product requirement and P0/P1/P2 |
| [FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md](research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md) | **ACTIVE / batch 2** | Dose/placement detail for forefoot wedge, metatarsal pad, arch and heel features |
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
| `spec/06_corrective_elements.md` | **Research-driven next** | Clinically named element library, anatomical placement, dimensions/dose and acceptance metrics |
| `spec/07_sculpt_and_roi_deformation.md` | Planned | Local authoring semantics and ROI provenance |
| `spec/08_material_stiffness.md` | **Research-driven next** | Material/stiffness properties, regional maps and evidence boundaries |
| `spec/09_analysis_qc_dfm.md` | **Research-driven next** | Sections, pressure/outcome metrics, angles, thickness, target/neighbor safety and manufacturing QC |
| `spec/10_manufacturing.md` | Planned | Manufacturing profiles and export semantics |
| `spec/11_biomeche_integration.md` | **Research-driven next** | Quantitative pressure bridge, ROI, pre/post outcome loop and provenance |
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

---

## Research queue

### Functional/scientific

1. forefoot posting/wedge — broaden dose/clinical evidence;
2. arch height/length/position dose;
3. heel cup/wrap/camber geometry vs cushioning;
4. metatarsal bar/dome height/shape/placement;
5. relief/aperture depth/transition + neighboring-pressure effect;
6. peak pressure vs PTI/FTI/contact area/COP/shear metric policy;
7. population-specific profiles: diabetic offloading, flatfoot, plantar heel pain, metatarsalgia, sport;
8. comfort/fit/adherence and PROM selection;
9. material durability/manufacturing evidence.

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

1. Source evidence remains separate from engineering decisions.
2. New scientific/vendor claims go to a source ledger or dated research document.
3. User-provided implementation facts are labeled separately when not independently documented.
4. Every P0 feature eventually needs acceptance criteria.
5. Preserve superseded architecture in Git history/research notes.
6. Update `RESUME_HERE.md` after substantial work.
7. Do not redistribute third-party EasyCAD2 PDFs/screenshots in the public repository without explicit rights clearance.
