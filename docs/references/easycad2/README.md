# EasyCAD2 — Primary Reference Pack

This directory is the canonical pointer for the primary EasyCAD2 source documents used by BiomechE-CAD.

The actual source PDFs are maintained externally and are referenced here by stable source link, version, date and scope. Because the BiomechE-CAD repository is public, binary copies are not duplicated here by default; this avoids creating unnecessary redistributed copies while preserving exact traceability.

## REF-EC2-001 — EasyCAD2 Manual

**Document:** `Easycad2 Manuale ITA 2.0.pdf`  
**Software version stated in document:** `1.1.x.x`  
**Document date stated internally:** `13/01/2024`  
**Primary source:**  
https://drive.google.com/file/d/148X366g4e47cYOWtFWP-jeMqavSJqHTa/view

### Role in BiomechE-CAD

Primary source for detailed workflow, screen organization, parameter names and user interaction semantics.

### High-value page map

| PDF page | Main evidence |
|---:|---|
| 7-12 | Database, patient/project management, settings, printers, CNC, units |
| 13 | 2D/3D navigation and multi-selection |
| 14 | LEFT/RIGHT workflow and mirror |
| 15-18 | DIMA, templates, advanced DIMA, dimensions |
| 19-20 | PRESSURE import, X/Y/rotation/scale and Generate |
| 21-22 | Scan3D landmarks, Align and trim |
| 23 | Scan2D |
| 24-30 | MODIFICA: thickness, flatten, heel, arches, wedges, smooth |
| 31-35 | ELEMENTI: categories, transforms, custom element |
| 36-40 | POST PROCESSING: global deformation, sculpt, smooth, ROI deform |
| 42-44 | CONTROLLO / cross-section / fixed heights |
| 44-50 | PRODUCI: closure modes, text, materials, CNC, 3D print hardness |
| 50-52 | Toolbar, views, overlays, height probe, ruler, history |
| 52-53 | Minimum-thickness warning, auto-fix and safe close |

### Important usage rule

The manual documents product behavior and UI semantics. It does **not** disclose the proprietary mathematical implementation of arch, heel/camber, wedge, pressure-to-shape or scan-deformation algorithms. BiomechE-CAD specifications must not invent these internal formulas.

---

## REF-EC2-002 — EasyCAD2 Software Validation Plan

**Document:** `PdV0001_EasyCAD2 software validation plan.pdf`  
**Validation-plan version:** `1`  
**Last update:** `15/01/2026`  
**Target software line:** EasyCAD2 `1.4.x.x`  
**Primary source:**  
https://drive.google.com/file/d/19Pdjn76a6sAEcnUTut2qL0qzvfkniD4v/view

### Role in BiomechE-CAD

Primary source for expected behavior and acceptance-level validation of the later EasyCAD2 1.4 line.

The plan contains 25 user stories covering:

- first-run activation;
- patient database;
- patient search/edit/delete;
- language and units;
- 3D printer/CNC configuration;
- project mirror;
- DIMA selection and dimension editing;
- pressure `.csv/.bpe` import and registration;
- Scan3D/Image2D alignment;
- global thickness and flatten;
- heel/camber;
- medial/lateral arches;
- wedges;
- elements;
- custom elements;
- 3D-print rigidity modifiers;
- sculpt;
- global deformation from acquisition data;
- cross-section / fixed heights;
- ruler;
- STL/GCODE production;
- overall/per-element hardness;
- PDF report;
- minimum-thickness warning/auto-fix;
- safe save/close.

---

## REF-EC2-003 — EasyCAD2 Software Validation Report

**Document:** `RdT001_Rapporto di Test di validazione software EasyCAD2 versione 14xx.pdf`  
**Software version:** `1.4.x.x`  
**Compilation date:** `20/01/2026`  
**Document status:** Approved / Final  
**Primary source:**  
https://drive.google.com/file/d/1kbDKQd6qskQH1MyZ5O3Y-WYt5p_7qRlJ/view

### Reported validation result

```text
Total planned tests: 25
Executed:           25
PASS:               25
FAIL:                0
BLOCKED:             0
```

### Role in BiomechE-CAD

Used to promote capabilities from `probable/lineage/secondary` to **primary-confirmed EasyCAD2 1.4 capability** when the corresponding validation user story passed.

This report validates software behavior under the declared test plan; it does not by itself prove biomechanical or clinical efficacy of every prescription parameter.

---

# How these references are used

The evidence hierarchy is:

```text
EasyCAD2 Manual 1.1.x.x
    -> detailed UI / parameter behavior

EasyCAD2 Validation Plan 1.4.x.x
    -> expected behavior / user stories

EasyCAD2 Validation Report 1.4.x.x
    -> confirmation that those user stories passed on the validated 1.4 line
```

When sources conflict or differ by version:

1. preserve both facts;
2. prefer the newer validation documents for feature-existence claims;
3. use the manual for detailed parameter/UI semantics only where supported;
4. mark unresolved differences as version-specific or `OPEN QUESTION`;
5. never silently infer the internal algorithm.

---

# Related BiomechE-CAD documents

- `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md` — consolidated EasyCAD2-inspired functional baseline.
- `docs/research/SOURCES.md` — source inventory and scientific references.
- `docs/RESUME_HERE.md` — dynamic project handover.
- `docs/DECISIONS.md` — engineering decisions separated from evidence.

---

# Reference maintenance rule

When another useful primary document becomes available — for example a newer EasyCAD2 manual, release notes, technical validation report, file-format specification, manufacturing guide or official training material — add it to `docs/references/easycad2/` with:

```text
stable REF ID
document title
software/document version
date
source link
scope
page/section map
claims supported
known limitations
supersession/version notes
```

Do not remove an older source simply because a newer version appears; preserve version history so behavioral changes remain auditable.
