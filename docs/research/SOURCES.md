# BiomechE-CAD — Research Source Inventory

This inventory preserves research provenance separately from evolving engineering specifications.

## A. Primary EasyCAD2 documents supplied by the user

### EC2-MANUAL-1.1

**EasyCAD2 — Manuale d'uso / Easycad2 Manuale ITA 2.0**  
Internal software version shown by the manual: `1.1.x.x`  
Manual date: `13/01/2024`  
Drive source:  
https://drive.google.com/file/d/148X366g4e47cYOWtFWP-jeMqavSJqHTa/view

Key page map:

```text
7-12   database/settings
13     navigation/multi-select
14     side/mirror
15-18  DIMA/templates/dimensions
19-20  pressure
21-22  Scan3D
23     Scan2D
24-30  MODIFICA
31-35  ELEMENTI/custom
36-40  POST PROCESSING
42-44  CONTROLLO
44-50  PRODUCI
50-52  TOOLBAR/history/measurement
52-53  thickness warning/safe close
```

**Copyright handling:** do not redistribute manual screenshots/PDFs in this public repository without rights clearance.

### EC2-VAL-PLAN-1.4

**PdV0001 — Piano di validazione software EasyCAD2**  
Version 1; updated `15/01/2026`; target EasyCAD2 `1.4.x.x`.  
Drive: https://drive.google.com/file/d/19Pdjn76a6sAEcnUTut2qL0qzvfkniD4v/view

Defines 25 user stories covering database/settings, mirror, DIMA, acquisitions, modification, elements, material/rigidity, post-processing, QC, production, report, thickness handling and save/close behavior.

### EC2-VAL-REPORT-1.4

**RdT001 — Rapporto di Test di validazione software EasyCAD2 versione 1.4.x.x**  
Compilation date `20/01/2026`.  
Drive: https://drive.google.com/file/d/1kbDKQd6qskQH1MyZ5O3Y-WYt5p_7qRlJ/view

```text
planned = 25
executed = 25
PASS = 25
FAIL = 0
BLOCKED = 0
```

---

## B. Vendor / market sources

- Sensor Medica — EasyCAD2: https://www.sensormedica.com/en/easycad-2/
- Sensor Medica — easyCAD Insole: https://www.sensormedica.com/en/easycad-insole/
- Sensor Medica — Vulcan CNC: https://www.sensormedica.com/it/vulcan-cnc/
- Sensor Medica — EasyCAD2 workflow/course material: https://www.sensormedica.com/it/elementor-13305/
- Chitti4Feet — EasyCAD2 overview, secondary source: https://www.chitti4feet.com/easycad2-per-la-creazione-di-ortesi-plantari/

Vendor/secondary claims remain separate from manual/validation evidence.

---

## C. Scientific baseline linked to CAD functionality

The detailed feature mapping is maintained in:

- `docs/research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md`
- `docs/research/FUNCTIONAL_EVIDENCE_BATCH_02_PARAMETER_DOSE.md`

### REF-CAD-001 — Rearfoot posting dose response

Telfer S, Abbott M, Steultjens MPM, Woodburn J.  
**Dose-response effects of customised foot orthoses on lower limb kinematics and kinetics in pronated foot type.**  
J Biomech. 2013.  
PMID `23631857`  
DOI `10.1016/j.jbiomech.2013.03.036`

Role: preserve posting/wedge as a numerical prescription dose.

### REF-CAD-002 — 3D scanning methods

Farhan M et al.  
**Comparison of 3D scanning versus traditional methods of capturing foot and ankle morphology for the fabrication of orthoses: a systematic review.**  
J Foot Ankle Res. 2021.  
PMID `33413570`  
DOI `10.1186/s13047-020-00442-8`

Role: scan provenance, protocol and QC.

### REF-CAD-003 — 3D scan reporting / methodology

Allan JJ et al.  
**Methodological and statistical approaches for the assessment of foot shape using three-dimensional foot scanning: a scoping review.**  
J Foot Ankle Res. 2023.  
PMID `37106385`  
DOI `10.1186/s13047-023-00617-z`

Role: scanner/weight-bearing/markers/protocol metadata.

### REF-CAD-004 — Shape + pressure custom insole design

Owings TM et al.  
**Custom therapeutic insoles based on both foot shape and plantar pressure measurement provide enhanced pressure relief.**  
Diabetes Care. 2008.  
PMID `18252899`  
DOI `10.2337/dc07-2288`

Role: quantitative pressure-informed design and targeted ROI offloading.

### REF-CAD-005 — Pressure-guided iterative optimization

Bus SA et al.  
**Evaluation and optimization of therapeutic footwear for neuropathic diabetic foot patients using in-shoe plantar pressure analysis.**  
Diabetes Care. 2011.  
PMID `21610125`  
DOI `10.2337/dc10-2206`

Role: closed-loop measure → modify → remeasure workflow.

### REF-CAD-006 — IWGDF offloading criterion context

Bus SA et al.  
**Guidelines on the prevention of foot ulcers in persons with diabetes (IWGDF 2023 update).**  
Diabetes Metab Res Rev. 2024.  
DOI `10.1002/dmrr.3651`

Role: demonstrates that outcome targets may be quantitative and protocol/population specific. Do not promote diabetic-foot thresholds to universal CAD defaults.

### REF-CAD-007 — Offloading design features systematic review

**Footwear and insole design features for offloading the diabetic at risk foot — A systematic review and meta-analyses.**  
PMID `33532602`.

Role: evidence for arch profiles, metatarsal additions/apertures and pressure-informed design; also highlights heterogeneity.

### REF-CAD-008 — Pressure-based 3D printed accommodative insole

Muir BC et al.  
**Evaluation of novel plantar pressure-based 3-dimensional printed accommodative insoles — A feasibility study.**  
Clin Biomech. 2022.  
PMID `35987171`  
DOI `10.1016/j.clinbiomech.2022.105739`

Role: pressure-derived offloading ROI and personalized metamaterial direction.

### REF-CAD-009 — Orthosis stiffness in flexible flatfoot

Cherni Y et al.  
**Effect of 3D printed foot orthoses stiffness on muscle activity and plantar pressures in individuals with flexible flatfeet.**  
Clin Biomech. 2022.  
PMID `34973589`  
DOI `10.1016/j.clinbiomech.2021.105553`

Role: stiffness is an independent prescription/manufacturing variable.

### REF-CAD-010 — Stiffness/design/posting in healthy cohort

Desmyttere G et al.  
**Effect of 3D printed foot orthoses stiffness and design on foot kinematics and plantar pressures in healthy people.**  
Gait Posture. 2020.  
PMID `32818861`  
DOI `10.1016/j.gaitpost.2020.07.146`

Role: geometry and stiffness have region-specific biomechanical effects.

### REF-CAD-011 — Central metatarsal pressure reduction

Ruiz-Ramos M et al.  
**Effectiveness of bespoke or customised orthotic treatment in plantar pressure reduction of the central metatarsals: a systematic review and meta-analysis.**  
PMID `39399760`  
DOI `10.1016/j.jor.2023.12.006`

Role: preserve metatarsal pad/bar/offloading functions.

### REF-CAD-012 — Forefoot pressure systematic review 2026

Thiaspras L et al.  
**Foot orthoses for forefoot pressure reduction and the hypothesized role in calf muscle stretching: A systematic review highlighting an evidence gap.**  
Foot. 2026.  
PMID `41931962`  
DOI `10.1016/j.foot.2026.102251`

Role: forefoot-load reduction, PTI and metatarsal/contoured designs.

### REF-CAD-013 — Metatarsal pad placement

**Effect of metatarsal pad placement on plantar pressure in people with diabetes mellitus and peripheral neuropathy.**  
PMID `17257544`  
DOI `10.3113/FAI.2007.0015`

Role: demonstrates that anatomical placement is a dose/reference-frame variable, not a cosmetic transform.

### REF-CAD-014 — Hallux-valgus metatarsal pad placement

**Optimal placement of metatarsal pads for patients with hallux valgus based on plantar pressure measurement.**  
PMID `40707294`.

Role: additional population-specific evidence that normalized placement matters.

### REF-CAD-015 — Forefoot wedge dose response

**Dose-response effects of forefoot and arch orthotic components on the center of pressure trajectory during running in pronated feet.**  
PMID `34864487`.

Role: preserve forefoot wedge angle/direction as an explicit numerical prescription.

### REF-CAD-016 — Insole configurations, arch support and walking convenience

**The effects of insole configurations on forefoot plantar pressure and walking convenience in diabetic patients with neuropathic feet.**  
PMID `17046124`  
DOI `10.1016/j.clinbiomech.2006.08.004`

Role: combination effects; pressure benefit vs comfort tradeoff.

### REF-CAD-017 — Arch-support hardness 2026

**Biomechanical effects of varying arch support hardness in foot orthosis for adults with flexible flatfoot: A comprehensive Bayesian statistical analysis.**  
PMID `41455151`  
DOI `10.1016/j.gaitpost.2025.110085`

Role: hardness/stiffness is a dose separate from geometry; effects can plateau and shift loads.

### REF-CAD-018 — Heel plug custom FO

Balsdon ME, Dombroski CE.  
**Custom-made foot orthoses with and without heel plugs and their effect on treatment outcomes and plantar pressures in patients with plantar fasciitis.**  
PMID `40366378`  
DOI `10.1097/PXR.0000000000000450`

Role: separate heel containment geometry from cushioning/material relief.

### REF-CAD-019 — Heel cup/arch design pressure redistribution

**Effects of a range of 6 prefabricated orthotic insole designs on plantar pressure in a healthy population.**  
PMID `39140763`  
DOI `10.1097/PXR.0000000000000292`

Role: heel cup/arch design features and regional pressure/contact-area effects.

### REF-CAD-020 — Inter-individual offloading response

**Pressure relief and load redistribution by custom-made insoles in diabetic patients with neuropathy and foot deformity.**  
PMID `15234488`.

Role: supports patient-specific outcome verification and shows local pressure relief can redistribute load elsewhere.

### REF-CAD-021 — Graded stiffness heel offloading

**Graded stiffness offloading insoles better redistribute heel plantar pressure to protect the diabetic neuropathic foot.**  
PMID `36706604`.

Role: regional stiffness / perimeter-load management.

### REF-CAD-022 — Gradient lattice mapping 2026

Wang Lihong et al.  
**Optimization of pressure relief in gradient lattice orthotic insoles based on plantar pressure-rod diameter mapping.**  
Med Eng Phys. 2026.  
PMID `42049041`  
DOI `10.1088/1873-4030/ae6593`

Role: R&D evidence for pressure→regional modulus/lattice mapping; not yet a clinical rule.

### REF-CAD-023 — Partition TPMS lattice 2026

**Design of novel orthotic insoles based on partition infilling of TPMS structures.**  
PMID `42147489`.

Role: R&D evidence for region-specific lattice structures/material realization.

### REF-CAD-024 — 3D printed orthoses outcomes systematic review

Atallah H et al.  
**The current state of 3D-printed orthoses clinical outcomes: a systematic review.**  
BMC Musculoskelet Disord. 2025.  
PMID `40890671`  
DOI `10.1186/s12891-025-09070-4`

Role: manufacturing/clinical feasibility, comfort/fit and evidence limitations.

### REF-CAD-025 — Lower-limb assistive-device adherence

**Patient Compliance With Wearing Lower Limb Assistive Devices: A Scoping Review.**  
PMID `35753880`  
DOI `10.1016/j.jmpt.2022.04.003`

Role: fit/comfort/device properties and adherence.

### REF-CAD-026 — PROM landscape

**Patient reported outcome measures in the foot and ankle literature: A systematic review.**  
PMID `41033023`  
DOI `10.1016/j.foot.2025.102209`

Role: avoid inventing a single proprietary universal clinical outcome score.

### REF-CAD-027 — Adult flatfoot uncertainty

**Evidence for foot orthoses for adults with flatfoot: a systematic review.**  
PMID `34844639`.

Role: evidence heterogeneity; avoid universal arch/orthosis claims.

### REF-CAD-028 — Flexible flatfoot patient-reported outcomes

**Foot orthoses for flexible flatfeet in children and adults: a systematic review and meta-analysis of patient-reported outcomes.**  
PMID `36611153`  
DOI `10.1186/s12891-022-06044-8`

Role: population-specific outcomes and uncertainty.

---

## D. Architecture research sources — preserved but currently parked

Architecture research remains preserved under `docs/research/architecture/` and the architecture status addendum.

Important upstream projects previously verified include:

- Pixar OpenSubdiv
- McNeel openNURBS / rhino3dm
- Manifold
- Open CASCADE Technology
- FlatBuffers

These sources are **not** used to decide functional requirements during the current research phase.

---

## E. Related BiomechE architecture/documentation source

The documentation method is aligned with `ww34ww34ww34/BiomechE`:

- Markdown canonical specs;
- evidence separated from decisions;
- dynamic `RESUME_HERE`;
- canonical units;
- coordinate semantics independent of memory layout;
- versionable adapters/contracts;
- preserved historical evidence.

---

## F. Research audit queue

### Functional/scientific next

- forefoot posting beyond the current dose-response study;
- arch height/length/position-specific dose;
- heel cup/wrap/camber geometry separated from cushioning;
- metatarsal bar/dome height/shape/placement;
- local relief/aperture depth/transition and neighboring load transfer;
- pressure metric policy: peak, mean, PTI/FTI, contact area, COP, shear when available;
- population-specific evidence profiles;
- comfort/fit/adherence and PROM selection;
- manufacturing tolerance, fatigue and durability evidence.

### Competitors

- ParoContour / DIERS
- FitFoot360
- Rodin4D / Neo
- Vorum / Canfit
- additional international orthotic CAD/CAM products

Competitor features should be mapped to the functional evidence matrix, but competitor behavior is not scientific evidence.
