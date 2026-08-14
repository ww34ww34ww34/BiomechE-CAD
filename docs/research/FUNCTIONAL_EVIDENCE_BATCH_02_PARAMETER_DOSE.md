# BiomechE-CAD — Functional Evidence Batch 02: Parameter Dose and Placement

**Date:** 2026-08-14  
**Status:** research input to `FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md`  
**Architecture:** out of scope / parked.

This batch deepens four areas where the product should preserve not only the feature name but also a measurable **dose / placement / material parameter**.

---

## 1. Forefoot wedge — preserve angle and direction

### Source

**Dose-response effects of forefoot and arch orthotic components on the center of pressure trajectory during running in pronated feet.**  
PMID `34864487`.

### What the study supports

- 15 recreational runners with symptomatic pronated feet.
- Ten orthosis conditions varied forefoot wedge across five levels and arch support across two levels.
- Forefoot wedge conditions changed mediolateral center-of-pressure trajectory during portions of stance.
- A linear effect of forefoot-wedge dose on mediolateral COP displacement was reported during propulsion.
- Almost all orthoses reduced force-time integral under the 2nd metatarsal and medial heel; medial forefoot wedges also reduced hallux FTI.

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

This was a small study in recreational runners with pronated feet. It supports dose sensitivity of the feature; it does **not** define a universal optimal angle.

---

## 2. Metatarsal pad — placement is clinically meaningful

### Source A

**Effect of metatarsal pad placement on plantar pressure in people with diabetes mellitus and peripheral neuropathy.**  
PMID `17257544`; DOI `10.3113/FAI.2007.0015`.

### Findings relevant to CAD

In the tested population, metatarsal pad location relative to the metatarsal-head line materially changed peak plantar pressure. Placement approximately **6.1–10.6 mm proximal** to the metatarsal-head line consistently reduced pressure, while placement too distal could increase pressure.

This number is **not a universal CAD default**. It is evidence that placement relative to anatomical landmarks must be explicit and measurable.

### Source B

**Optimal placement of metatarsal pads for patients with hallux valgus based on plantar pressure measurement.**  
PMID `40707294`.

The crossover study found the tested pad placement at 76% of foot length reduced central metatarsal pressure in the studied hallux-valgus cohort.

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

BiomechE-CAD should be able to report placement both in absolute millimetres and in normalized anatomical coordinates.

---

## 3. Arch support — geometry and hardness are different doses

### Source A

**The effects of insole configurations on forefoot plantar pressure and walking convenience in diabetic patients with neuropathic feet.**  
PMID `17046124`; DOI `10.1016/j.clinbiomech.2006.08.004`.

Twelve configurations combined metatarsal dome, varus/valgus wedges and arch supports of different heights. Pressure reductions differed by region and configuration, while walking-convenience scores generally worsened as additional/extra support elements were added.

### Source B

**Biomechanical effects of varying arch support hardness in foot orthosis for adults with flexible flatfoot: A comprehensive Bayesian statistical analysis.**  
PMID `41455151`; DOI `10.1016/j.gaitpost.2025.110085`.

In 20 women with asymptomatic flexible flatfoot, higher arch-support hardness altered rearfoot mechanics but benefits plateaued while harder conditions increased some knee/forefoot loading measures.

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

The 2026 hardness study is small and population-specific. It supports the importance of retaining hardness as a dose, not an automatic therapeutic rule.

---

## 4. Heel cup / heel relief — separate containment from cushioning

### Sources

- **Effects of a range of 6 prefabricated orthotic insole designs on plantar pressure in a healthy population** — PMID `39140763`; DOI `10.1097/PXR.0000000000000292`.
- **Custom-made foot orthoses with and without heel plugs... plantar fasciitis** — PMID `40366378`; DOI `10.1097/PXR.0000000000000450`.
- **The Soft Prefabricated Orthopedic Insole Decreases Plantar Pressure during Uphill Walking with Heavy Load Carriage** — PMID `36978744`; DOI `10.3390/bioengineering10030353`.

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

This separation is useful because heel geometry and local material compliance can affect pressure through different mechanisms.

---

# 5. Cross-cutting rule — every tunable feature needs a reference frame

The literature repeatedly describes design effects relative to anatomical or pressure landmarks. Therefore every P0 feature that can be moved or dosed should explicitly identify its reference:

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

The next useful parameter-evidence batch should cover:

1. relief/aperture size/depth and transition;
2. metatarsal bar/dome geometry beyond placement;
3. arch-support height/length dose in clinical populations;
4. heel-cup height/shape dose;
5. pressure metrics and neighboring-region safety criteria.
