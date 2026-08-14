# BiomechE-CAD — Functional Evidence Batch 02: Parameter Dose and Placement

**Date:** 2026-08-14  
**Status:** research input to `FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md`  
**Architecture:** out of scope / parked.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is authoritative for all source metadata and locators.

This batch deepens four areas where the product should preserve not only the feature name but also a measurable **dose / placement / material parameter**.

---

## 1. Forefoot wedge — preserve angle and direction

A dose-response running study varied forefoot wedge across five levels and arch support across two levels in 15 recreational runners with symptomatic pronated feet. Forefoot-wedge conditions changed mediolateral COP trajectory and a linear dose effect was reported during propulsion; regional force-time-integral changes were also observed [REF-CAD-015, Abstract—Methods/Results].

### Product consequence

Forefoot posting should remain a structured numerical prescription:

```text
ForefootWedge
  angle_deg
  medial_or_lateral
  pivot/reference
  longitudinal extent
  transverse extent
  transition
```

Do not save only the resulting mesh.

### Evidence caution

This was a small, population-specific study. It supports dose sensitivity of the feature; it does **not** define a universal optimal angle [REF-CAD-015].

---

## 2. Metatarsal pad — placement is clinically meaningful

In people with diabetes, peripheral neuropathy and prior forefoot ulceration, pad location relative to the metatarsal-head line materially changed peak plantar pressure; placement approximately 6.1–10.6 mm proximal consistently reduced pressure in that study, while placement too distal could increase it [REF-CAD-013, pp. 84–88].

A separate crossover study in hallux-valgus patients found that the tested pad placement at 76% of foot length reduced central metatarsal pressure in that cohort [REF-CAD-014, pp. 131–138].

These values are **not universal CAD defaults**. They demonstrate that placement relative to anatomical landmarks must be explicit, measurable and linked to population/protocol/source.

### Product consequence

The element model should include at least:

```text
MetatarsalElement
  target region / MTH group
  reference landmark system
  longitudinal position_mm
  normalized foot-length position
  width_mm
  length_mm
  height_mm
  rotation_deg
  shape/profile
```

BiomechE-CAD should report placement both in absolute millimetres and normalized anatomical coordinates.

---

## 3. Arch support — geometry and hardness are different doses

In diabetic neuropathy, twelve configurations combining metatarsal dome, varus/valgus wedges and arch supports of different heights produced region-dependent pressure changes while subjective walking convenience generally worsened as extra support elements were added [REF-CAD-016, pp. 81–87].

A later flexible-flatfoot study varying arch-support hardness found biomechanical differences and suggests that hardness can act as an independent dose rather than merely a manufacturing afterthought [REF-CAD-017, Abstract—Results/Conclusions].

### Product consequence

Do not represent “arch support” with a single scalar.

```text
ArchGeometry
  start
  center
  end
  height_mm
  width/depth
  curvature
  transition

ArchMechanicalProfile
  material
  hardness/stiffness
  regional transition
```

The software should allow geometry and mechanical-property changes to be varied and compared independently.

### Evidence caution

Hardness evidence remains population/protocol specific. It supports retaining hardness as a dose, not an automatic therapeutic rule [REF-CAD-017].

---

## 4. Heel cup / heel relief — separate containment from cushioning

Heel-cup/arch designs can change heel pressure and contact area [REF-CAD-019]. A custom-orthosis study with and without a softer heel plug supports treating local cushioning/material as a separate variable from the surrounding orthosis geometry [REF-CAD-018].

### Product consequence

The heel feature should not collapse together:

```text
HeelContainment
  cup_height
  cup_width
  medial/lateral wall profile
  transition/camber

HeelCushioningOrRelief
  ROI
  material/hardness
  thickness
  plug/relief depth
  transition
```

This separation is useful because heel geometry and local material compliance can affect pressure through different mechanisms [REF-CAD-018; REF-CAD-019].

---

# 5. Cross-cutting rule — every tunable feature needs a reference frame

The literature repeatedly describes design effects relative to anatomical or pressure landmarks [REF-CAD-001; REF-CAD-013; REF-CAD-014; REF-CAD-041; REF-CAD-042]. Therefore every P0 feature that can be moved or dosed should explicitly identify its reference:

```text
absolute project XYZ
anatomical normalized s/q
heel landmark
metatarsal-head line
foot length percentage
pressure ROI centroid
custom clinician landmark
```

A value such as:

```text
met_pad_y = 183.4
```

is insufficient without the coordinate/reference definition.

---

# 6. Acceptance-test implications

The functional evidence now justifies quantitative tests independent of geometry implementation:

```text
WEDGE-DOSE-001
requested angle is preserved and measurable

META-POS-001
metatarsal element position relative to chosen landmark is preserved after reload/mirror

ARCH-DOSE-001
geometry and stiffness are independently editable/versioned

HEEL-VAR-001
containment geometry can change without silently changing cushioning material, and vice versa
```

These tests remain valid regardless of the eventual CAD kernel.

---

# 7. Research conclusion

This batch strengthens a general product principle:

> A clinically meaningful CAD feature should be stored as a named prescription with **dose, anatomical placement, units and reference frame**, not merely as final geometry.

Relief/aperture and neighbouring-load criteria were continued in `FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md`; metatarsal element semantics were promoted into `docs/spec/06_corrective_elements.md`; pressure/outcome policy is now in `docs/spec/09_analysis_qc_dfm.md`.

---

## Bibliography links

[REF-CAD-001]: ../BIBLIOGRAPHY.md#ref-cad-001
[REF-CAD-013]: ../BIBLIOGRAPHY.md#ref-cad-013
[REF-CAD-014]: ../BIBLIOGRAPHY.md#ref-cad-014
[REF-CAD-015]: ../BIBLIOGRAPHY.md#ref-cad-015
[REF-CAD-016]: ../BIBLIOGRAPHY.md#ref-cad-016
[REF-CAD-017]: ../BIBLIOGRAPHY.md#ref-cad-017
[REF-CAD-018]: ../BIBLIOGRAPHY.md#ref-cad-018
[REF-CAD-019]: ../BIBLIOGRAPHY.md#ref-cad-019
[REF-CAD-041]: ../BIBLIOGRAPHY.md#ref-cad-041
[REF-CAD-042]: ../BIBLIOGRAPHY.md#ref-cad-042
