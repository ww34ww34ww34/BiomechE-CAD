# BiomechE-CAD — Visual / Human-Factors Evidence Baseline

**Status:** EVIDENCE BASELINE v1  
**Date:** 2026-08-16  
**Purpose:** constrain VIS-01..VIS-04 with current human-centred design, medical-device usability and accessibility evidence without claiming regulatory conformance.

---

## 1. Evidence hierarchy for the visual phase

```text
FROZEN BIOMECHE-CAD SEMANTICS
        ↓
HUMAN-FACTORS / ACCESSIBILITY EVIDENCE
        ↓
VISUAL REFERENCE / MOCKUPS
        ↓
IMPLEMENTATION + USABILITY VALIDATION
```

A visual preference cannot override domain semantics, and a mockup cannot by itself demonstrate usability/safety.

---

## 2. ISO 9241-210:2019 — human-centred design

**Current status verified:** ISO 9241-210:2019, Edition 2, remains published/current and was confirmed in 2025.

**Relevant role:** provides requirements/recommendations for human-centred design activities across the lifecycle of interactive systems.

**BiomechE-CAD implication:**

- design around intended users, tasks and contexts rather than library/widget convenience;
- treat mockups as hypotheses to evaluate;
- refine with user/task feedback;
- preserve traceability from user/task needs to interface decisions.

**Not a claim:** VIS v1 is not a claim of ISO 9241-210 conformance.

---

## 3. IEC 62366-1:2015 + A1:2020 — usability engineering for medical devices

**Current status verified:** IEC 62366-1:2015 with Amendment 1:2020 consolidated version is current; IEC lists stability to 2028.

**Relevant role:** defines a usability-engineering process related to safety and use error for medical devices.

**BiomechE-CAD implication:** even though final regulatory qualification remains OPEN, the interface should already avoid preventable use-error patterns around high-impact states such as:

```text
wrong patient/case
wrong side
wrong units
unconfirmed landmark/profile
preview mistaken for committed revision
stale result mistaken for current
warning mistaken for pass
manufacturing artifact mistaken for accepted physical part
```

**Not a claim:** applying these principles does not classify BiomechE-CAD as a medical device and does not prove IEC 62366-1 compliance.

---

## 4. FDA Human Factors / Usability Engineering — current 2026 guidance

**Current status verified:** FDA's *Applying Human Factors and Usability Engineering to Medical Devices* final guidance was updated/issued in August 2026. FDA's current Human Factors pages emphasize the user-interface loop in which users perceive information, interpret it, decide and manipulate controls, while the system responds and provides feedback.

**BiomechE-CAD implications:**

1. critical state must be perceivable;
2. labels/units/context must support correct interpretation;
3. primary actions must make their consequence understandable;
4. the system must provide clear feedback after an action;
5. irreversible/high-risk transitions require stronger confirmation than routine reversible editing;
6. visual hierarchy should reflect task/risk importance, not merely aesthetic emphasis.

FDA also issued 2026 final guidance on human-factors information in device marketing submissions, reinforcing the importance of risk-based UI evidence where applicable.

**Not a claim:** these sources guide visual/human-factors quality; US regulatory applicability is outside current product classification.

---

## 5. WCAG 2.2 — accessibility baseline

**Current status verified:** WCAG 2.2 is a W3C Recommendation and W3C recommends adopting it as the current accessibility target for web content.

Relevant requirements/principles for BiomechE-CAD visual references include:

```text
1.4.1  color is not the only means of conveying information
2.4.11 focus must not be obscured (AA)
2.5.7  dragging functionality has a non-drag alternative where drag is not essential (AA)
2.5.8  minimum pointer target sizing/spacing (AA)
4.1.3  status messages programmatically determinable in web implementations (AA)
```

**BiomechE-CAD implications:**

- PASS/WARNING/BLOCKING/UNRESOLVED use icon/text/shape as well as color;
- selected/focused state must remain visually clear;
- drag handles also expose numeric or alternate pointer controls;
- dense CAD controls must not become unusably small;
- important async/status updates should have implementation hooks for assistive technology.

**Scope note:** desktop-native accessibility APIs differ from web, but the underlying interaction principles remain useful. Exact WCAG conformance target is an implementation/release decision.

---

## 6. Visual evidence-derived rules

### HF-VIS-001 — Context before command

Before a clinically/manufacturing-significant action, the user should be able to perceive the active case, side and relevant revision/profile context.

### HF-VIS-002 — State is redundant, not color-only

For:

```text
VALID
WARNING
BLOCKING
UNRESOLVED
SUGGESTED
CONFIRMED
PREVIEW
COMMITTED
RELEASED
```

use at least two of text, iconography, shape/border/pattern and color.

### HF-VIS-003 — Direct manipulation has numeric/semantic counterpart

Drag is not the only path for dose/placement edits where a numeric/semantic control is meaningful.

### HF-VIS-004 — Action consequence is legible

`Preview`, `Apply`, `Commit revision`, `Generate artifact`, `Release manufacturing`, `Accept physical part` must not have interchangeable visual weight/wording.

### HF-VIS-005 — Feedback follows action

After state-changing actions, the UI displays the resulting state/revision/warning without requiring the user to infer success from geometry alone.

### HF-VIS-006 — Risk salience follows consequence

Destructive/release/acceptance actions receive stronger visual confirmation and contextual summary than routine reversible edits.

### HF-VIS-007 — Dense workstation, not tiny controls

The UI may be information-dense but critical pointer targets and legibility must remain usable; density is achieved by hierarchy/grouping, not by shrinking every control.

### HF-VIS-008 — Focus/selection is never ambiguous

Keyboard focus, active tool, selected semantic object and active side are different states and need distinct visual treatment.

### HF-VIS-009 — Quantitative values stay readable

Clinical/engineering numbers use aligned digits, explicit units and consistent decimal/presentation policy; heatmaps never hide numeric access.

### HF-VIS-010 — Provenance available on demand, critical provenance visible inline

Do not flood the main viewport with every hash/version, but surface critical side/source/revision/quality context and provide immediate drill-down to complete provenance.

---

## 7. Sources to normalize into canonical bibliography later

Proposed future IDs:

```text
STD-ISO-9241-210-2019
STD-IEC-62366-1-2015-A1-2020
GUIDE-FDA-HFE-2026
STD-WCAG-2.2
```

Do not treat the proposed identifiers as canonical until added to `docs/BIBLIOGRAPHY.md`.

---

## 8. VIS phase consequence

VIS-01 and mockups M01..M14 must explicitly map `HF-VIS-*` rules alongside `UX-*` and the owning product-domain acceptance IDs.

The visual package remains a reference baseline pending implementation/user validation; it does not become evidence of safe/effective use by appearance alone.
