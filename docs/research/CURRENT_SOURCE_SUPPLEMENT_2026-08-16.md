# BiomechE-CAD — Current Source Verification Supplement

**Status:** EVIDENCE SUPPLEMENT — pending normalization into `docs/BIBLIOGRAPHY.md` where new stable IDs are required  
**Date:** 2026-08-16  
**Purpose:** preserve the current-source verification performed during `P0-DOC-CLOSURE` without redefining the canonical bibliography governance.

---

## 1. Rule

`docs/BIBLIOGRAPHY.md` remains the authoritative stable-ID bibliography.

This supplement records:

1. current primary-source verification of existing bibliography concepts;
2. new 2025/2026 official sources used by the closure documents;
3. exact role/limits of each source;
4. items requiring later stable-ID normalization.

No source below creates a universal clinical default.

---

## 2. Scientific papers already represented in canonical bibliography

### `REF-CAD-002` — 3D scanning vs traditional morphology capture

**Role:** supports explicit capture method/protocol and caution about treating one scanning modality as universally accurate/reliable.

**Used by:** `20_input_scan_reference_data.md`.

### `REF-CAD-003` — 3D foot scanning methodology scoping review

**Role:** supports retaining scanner specifications, weight-bearing condition, markers, capture count and measurement/reporting methodology.

**Used by:** `20_input_scan_reference_data.md`.

### `REF-CAD-011` — customized orthotic treatment / central metatarsal pressure meta-analysis (2024)

**Role:** supports customized forefoot pressure reduction while not justifying one universal geometry/placement recipe.

**Used by:** `06_corrective_elements.md`, `13_use_case_profiles.md`.

### `REF-CAD-012` — forefoot plantar-load systematic review (2026)

**Role:** supports measurable forefoot PPP/PTI response and preserves mechanistic uncertainty.

**Used by:** `06_corrective_elements.md`, `13_use_case_profiles.md`.

### `REF-CAD-094` — orthotic material plantar-pressure systematic review

**Role:** supports material relevance while showing limited/heterogeneous evidence rather than a global material ranking.

**Used by:** `08_material_stiffness.md`.

### `REF-CAD-099` — subject-specific cushioning stiffness optimization

**Role:** supports load/context dependence of effective cushioning choice.

**Used by:** `08_material_stiffness.md`.

### `REF-CAD-091/092` — objective footwear adherence evidence

**Role:** supports explicit method/denominator and separation of objective vs subjective adherence.

**Used by:** `14_prom_comfort_adherence.md`.

---

## 3. Current guideline/methodology verification

### `GUIDE-IWGDF-2023`

Current official IWGDF guidance was rechecked during closure.

**Role:** contextual diabetic prevention/offloading evidence; prevention/recurrence pathway must not be silently conflated with active-ulcer treatment.

### `GUIDE-HEEL-PAIN-2023`

Current JOSPT/APTA heel-pain CPG baseline rechecked.

**Role:** supports multimodal interpretation and prevents a universal claim that orthoses are an isolated short-term treatment for plantar heel pain.

### `GUIDE-COSMIN`

Current COSMIN methodology pages rechecked.

**Role:** construct-first and fit-for-purpose/evidence-based selection of outcome measurement instruments.

### `GUIDE-FDA-PRO-DEVICE-2022`

Official FDA guidance rechecked.

**Role:** fit-for-purpose PRO instrument use in medical-device evaluation context.

---

## 4. New manufacturing/interchange official sources requiring stable-ID normalization

### ISO/IEC 25422:2025

**Title:** *Information technology — 3D Manufacturing Format (3MF) specification suite*.  
**Edition:** 1, 2025-06.  
**Status observed:** Published International Standard.

**Role in BiomechE-CAD:** evidence that 3MF is a standardized specification suite and may serve as a richer manufacturing carrier; does **not** make 3MF the product semantic model.

**Used by:** `22_interchange_manufacturing_handoff.md`.

### ISO/ASTM 52915:2020

**Title:** *Specification for additive manufacturing file format (AMF) Version 1.2*.  
**Edition:** 3, 2020-03.  
**Status observed:** confirmed current in 2026.

**Role:** AMF interchange-format evidence; the standard itself recognizes additional final-part information outside the current format.

**Used by:** `22_interchange_manufacturing_handoff.md`.

### ISO/ASTM 52951:2026

**Title:** *Additive manufacturing — Data — Data packages for AM parts*.  
**Edition:** 1, 2026-06.  
**Status observed:** Published.

**Role:** supports structured, application/organization-specific part data packages and design→acceptance information flow; directly supports the BiomechE-CAD manufacturing-package concept.

**Used by:** `10_manufacturing.md`, `22_interchange_manufacturing_handoff.md`, DOC-00/DOC-14 audits.

---

## 5. Current medical-device/regulatory official sources requiring stable-ID normalization

### Regulation (EU) 2017/745 — MDR

Current consolidated official EUR-Lex baseline was checked.

**Roles used:**

- medical-device/software qualification depends on intended purpose;
- Rule 11 is relevant when software is intended to provide information used for diagnostic/therapeutic decisions;
- software lifecycle/risk/information-security/verification-validation requirements exist where software is within device scope;
- custom-made-device definition is prescription/patient/design-responsibility specific.

**Used by:** `25_intended_use_risk_privacy_security_boundary.md`.

### MDCG 2019-11 rev.1 — June 2025

**Title:** *Qualification and classification of software — Regulation (EU) 2017/745 and Regulation (EU) 2017/746*.

**Role:** current EU guidance baseline for formal medical-device-software qualification/classification analysis.

**Used by:** `25_intended_use_risk_privacy_security_boundary.md`.

### MDCG 2021-24 rev.1 — April 2026

**Title:** *Guidance on classification of medical devices*.

**Role:** current classification guidance baseline to consult in formal market-release assessment.

### MDCG 2019-16 rev.1

**Title:** *Guidance on cybersecurity for medical devices*.

**Status observed:** still listed in the current European Commission MDCG guidance registry.

**Role:** cybersecurity regulatory guidance baseline if medical-device scope applies.

### MDCG 2021-3

**Title:** *Questions and Answers on Custom-Made Devices*.

**Role:** supports the need to assess rather than assume custom-made-device status for personalized orthoses.

---

## 6. Privacy/security official sources requiring stable-ID normalization

### Regulation (EU) 2016/679 — GDPR

Official EUR-Lex text checked, including:

```text
Article 9   special categories / health data
Article 25  data protection by design and by default
Article 32  security of processing
Article 35  DPIA risk-based requirements
```

**Role:** supports minimization/pseudonymization/security/DPIA decision boundaries; does not set one deployment-independent retention or DPIA outcome.

### ISO 14971:2019

**Title:** *Medical devices — Application of risk management to medical devices*.  
**Status observed:** confirmed current in 2025.

**Role:** medical-device risk-management process framework if/where applicable; it does not specify universal risk-acceptability levels.

### ISO 13485:2016

**Title:** *Medical devices — Quality management systems — Requirements for regulatory purposes*.  
**Status observed:** confirmed current in 2025.

**Role:** QMS framework if/where applicable; presence in documentation is not a claim of certification.

---

## 7. Source-role cautions

```text
paper result != global clinical default
guideline recommendation != cross-population transfer
standard capability != product implementation support
format standard != product semantic model
vendor nominal value != internal qualification
MDR/MDCG citation != final product classification
ISO 14971/13485 citation != conformity/certification
GDPR citation != one universal deployment policy
```

---

## 8. Normalization TODO

Add stable bibliography IDs for at least:

```text
STD-ISOIEC-25422-2025
STD-ISOASTM-52915-2020
STD-ISOASTM-52951-2026
REG-EU-MDR-2017-745
GUIDE-MDCG-2019-11-REV1-2025
GUIDE-MDCG-2021-24-REV1-2026
GUIDE-MDCG-2019-16-REV1
GUIDE-MDCG-2021-3
REG-EU-GDPR-2016-679
STD-ISO-14971-2019
STD-ISO-13485-2016
```

Exact naming should follow the existing `BIBLIOGRAPHY.md` taxonomy during the dedicated normalization pass.
