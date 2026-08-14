# BiomechE-CAD — Research Source Inventory

This inventory preserves research provenance separately from evolving engineering specifications.

## A. Primary EasyCAD2 documents supplied by the user

### EC2-MANUAL-1.1

**EasyCAD2 — Manuale d'uso / Easycad2 Manuale ITA 2.0**  
Internal software version shown by the manual: `1.1.x.x`  
Manual date shown internally: `13/01/2024`  
Drive source:  
https://drive.google.com/file/d/148X366g4e47cYOWtFWP-jeMqavSJqHTa/view

Use for detailed workflow, UI controls, parameter names and screen/page evidence.

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

**Copyright handling:** do not redistribute manual screenshots/PDFs in this public repository without rights clearance. Preserve page locators and factual descriptions instead.

### EC2-VAL-PLAN-1.4

**PdV0001 — Piano di validazione software EasyCAD2**  
Version 1; last update 15/01/2026; validation target EasyCAD2 1.4.x.x.  
Drive source:  
https://drive.google.com/file/d/19Pdjn76a6sAEcnUTut2qL0qzvfkniD4v/view

Defines 25 validation user stories covering license, patient DB, settings, mirror, DIMA, acquisitions, editing, elements, custom elements, stiffness modifiers, post-processing, QC, production, reporting, minimum-thickness handling and safe-close behavior.

### EC2-VAL-REPORT-1.4

**RdT001 — Rapporto di Test di validazione software EasyCAD2 versione 1.4.x.x**  
Compilation date 20/01/2026.  
Drive source:  
https://drive.google.com/file/d/1kbDKQd6qskQH1MyZ5O3Y-WYt5p_7qRlJ/view

Reported result:

```text
planned = 25
executed = 25
PASS = 25
FAIL = 0
BLOCKED = 0
```

Use this as evidence that the user-story capabilities were validated for the 1.4 line; it does not reveal proprietary mathematical algorithms.

---

## B. Vendor / market sources from the initial EasyCAD research

- Sensor Medica — EasyCAD2  
  https://www.sensormedica.com/en/easycad-2/
- Sensor Medica — easyCAD Insole  
  https://www.sensormedica.com/en/easycad-insole/
- Sensor Medica — Vulcan CNC  
  https://www.sensormedica.com/it/vulcan-cnc/
- Sensor Medica — EasyCAD2 workflow/course material  
  https://www.sensormedica.com/it/elementor-13305/
- Chitti4Feet — EasyCAD2 overview, secondary source  
  https://www.chitti4feet.com/easycad2-per-la-creazione-di-ortesi-plantari/

Secondary/vendor claims should remain distinguishable from manual/validation evidence.

---

## C. Scientific baseline linked to CAD functionality

### REF-CAD-001 — Posting / wedge dose-response

Telfer S, Abbott M, Steultjens MPM, Woodburn J.  
**Dose-response effects of customised foot orthoses on lower limb kinematics and kinetics in pronated foot type.**  
J Biomech. 2013;46(9):1489-1495.  
PMID: 23631857  
DOI: 10.1016/j.jbiomech.2013.03.036

Used to justify preserving wedge/posting as a numerical prescription variable in degrees rather than only as baked geometry.

### REF-CAD-002 — 3D scanning methods

Farhan M, Wang JZ, Bray P, Burns J, Cheng TL.  
**Comparison of 3D scanning versus traditional methods of capturing foot and ankle morphology for the fabrication of orthoses: a systematic review.**  
J Foot Ankle Res. 2021;14(1):2.  
PMID: 33413570  
DOI: 10.1186/s13047-020-00442-8

Used to justify scan provenance, acquisition-condition metadata and QC.

### REF-CAD-003 — Pressure-based accommodative insole

Muir BC et al.  
**Evaluation of novel plantar pressure-based 3-dimensional printed accommodative insoles — A feasibility study.**  
Clin Biomech. 2022;98:105739.  
PMID: 35987171  
DOI: 10.1016/j.clinbiomech.2022.105739

Used to support quantitative target-ROI pressure/offloading workflows.

### REF-CAD-004 — Orthosis stiffness

Cherni Y et al.  
**Effect of 3D printed foot orthoses stiffness on muscle activity and plantar pressures in individuals with flexible flatfeet.**  
Clin Biomech. 2022;92:105553.  
PMID: 34973589  
DOI: 10.1016/j.clinbiomech.2021.105553

Used to justify stiffness/material properties as prescription/manufacturing variables.

### REF-CAD-005 — Customized 3D-printed insole

Xu R et al.  
**Comparative Study of the Effects of Customized 3D Printed Insole and Prefabricated Insole on Plantar Pressure and Comfort in Patients with Symptomatic Flatfoot.**  
Med Sci Monit. 2019;25:3510-3519.  
PMID: 31079137  
DOI: 10.12659/MSM.916975

### REF-CAD-006 — Metatarsal pressure reduction

Ruiz-Ramos M et al.  
**Effectiveness of bespoke or customised orthotic treatment in plantar pressure reduction of the central metatarsals: a systematic review and meta-analysis.**  
J Orthop. 2024;59:111-118.  
PMID: 39399760  
DOI: 10.1016/j.jor.2023.12.006

Used to preserve metatarsal pad/bar and forefoot offloading capabilities in the product baseline.

### REF-CAD-007 — 3D foot-shape methodology

Allan JJ et al.  
**Methodological and statistical approaches for the assessment of foot shape using three-dimensional foot scanning: a scoping review.**  
J Foot Ankle Res. 2023.  
PMID: 37106385  
DOI: 10.1186/s13047-023-00617-z

Used to support explicit acquisition/shape-method provenance.

---

## D. Related architecture source

The documentation method and integration constraints are intentionally aligned with:

- `ww34ww34ww34/BiomechE`

Relevant BiomechE principles reused here include:

- Markdown as canonical specification;
- source evidence separated from engineering decisions;
- dynamic `RESUME_HERE` handover;
- explicit canonical physical units;
- coordinate-system semantics independent of matrix memory layout;
- hardware/device adapters separated from core semantics;
- patient record management outside the numerical core;
- versionable interfaces/contracts;
- research evidence preserved even when a later decision supersedes an older proposal.

---

## E. Research audit queue

### Competitors to audit against the unified feature matrix

- ParoContour / DIERS / Formetric-related orthosis workflow
- FitFoot360
- Rodin4D / Neo
- Vorum / Canfit
- additional international CAD/CAM orthotics products discovered during market research

### EasyCAD2 unanswered questions

- exact arch equations;
- heel/camber equations;
- wedge construction/reference axes;
- pressure `GENERATE` algorithm;
- Global Deformation algorithm;
- full element-library inventory/versioning;
- physical properties behind five hardness classes;
- project `.raw` and ZIP formats;
- printer/CNC protocol details;
- GCODE post-processor behavior;
- API/SDK/plugin availability;
- 3MF/multi-material support;
- OBJ/STEP support;
- mesh repair/manifold validation;
- exact report fields;
- regulatory traceability;
- manufacturing tolerances.

Useful findings must be added here or to a dedicated dated competitor/scientific research note even when they do not immediately become requirements.
