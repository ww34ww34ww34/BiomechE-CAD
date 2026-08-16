# BiomechE-CAD — Intended Use, Risk, Privacy & Security Boundary

**Version:** v1  
**Status:** **CANONICAL BOUNDARY v1 — REGULATORY CLASSIFICATION NOT YET FROZEN**  
**Date:** 2026-08-16  
**Jurisdiction baseline:** European Union / Italy-oriented product planning.  
**Important:** this document is a product-engineering boundary and evidence map, **not legal advice and not a conformity/classification determination**. A formal regulatory assessment must use the final intended purpose, claims, deployment model, manufacturer role and current applicable law/guidance.

---

## 0. Purpose

Prevent product architecture, UI, automation and data handling from silently creating regulatory, safety or privacy claims before they are deliberately assessed.

Core rule:

```text
TECHNICAL CAPABILITY
!= INTENDED PURPOSE
!= REGULATORY QUALIFICATION
!= REGULATORY CLASSIFICATION
```

and:

```text
AI / ALGORITHM SUGGESTION
!= DIAGNOSIS
!= PRESCRIPTION AUTHORITY
!= HUMAN CONFIRMATION
```

---

# 1. Current regulatory non-decision

BiomechE-CAD is intended as a vertical CAD for patient-specific/custom foot orthosis design, integrating source morphology, quantitative biomechanics, semantic prescription, manufacturing preparation and outcome traceability.

**The project does not yet freeze whether the software itself is:**

```text
medical device software
accessory to a medical device
software used in manufacture/design of a medical device but not itself a device
a combination of separately qualified modules
another legally relevant category
```

The answer depends primarily on the **manufacturer's intended purpose and claims**, not simply on the presence of patient data, pressure maps, algorithms or CAD functions.

EU MDR explicitly distinguishes software specifically intended for medical purposes from general-purpose software used in healthcare. Current MDCG 2019-11 rev.1 (June 2025) is the current EU software qualification/classification guidance baseline and must be used in a formal assessment.

---

# 2. Orthosis / custom-made-device context

EU MDR Article 2 defines a custom-made device around patient-exclusive use, a written prescription by an authorised person under national law and specific design characteristics under that person's responsibility; mass-produced industrial products merely adapted to instructions are excluded from that definition.

BiomechE-CAD therefore SHALL NOT assume that every personalized orthosis produced through the software automatically qualifies as a `custom-made device` under MDR.

The project must preserve enough data to support the applicable manufacturer/regulatory pathway, including as relevant:

```text
patient/case linkage
prescriber/authorised-person role
prescription/design responsibility
specific design characteristics
exact committed DesignRevision
manufacturing lineage
physical-part identity
statement/report/package references
```

Which of these become legally mandatory fields is deferred to formal regulatory analysis.

---

# 3. Intended-purpose template

Before market/release classification, create a controlled intended-purpose statement containing at least:

```text
product/module name + version
intended medical/non-medical purpose
intended user(s)
intended patient/population
intended use environment
input data
principal outputs
clinical/manufacturing decisions supported
what the software explicitly does NOT decide
required professional oversight
supported hardware/integration context
contraindicated/excluded contexts if any
```

Marketing, UI labels, manuals and automated recommendations must remain consistent with the approved intended-purpose statement.

---

# 4. Candidate intended-user roles

Product roles may include:

```text
orthotic / podiatry professional
authorised prescriber according to local law
CAD technician
manufacturing technician
clinical reviewer
quality reviewer
administrator
research user
read-only/report recipient
```

Role labels do not themselves determine professional legal authorization. Deployments map users to actual national/organizational permissions.

---

# 5. Human authority boundary

P0 frozen rule:

```text
algorithm may calculate
algorithm may suggest
workflow may prefill
preset may expand
BUT clinically/materially significant prescription confirmation remains explicit human action unless a separately validated/regulatorily assessed automation is approved
```

At minimum, the product distinguishes:

```text
SYSTEM_SUGGESTED
USER_EDITED
USER_CONFIRMED
SYSTEM_DERIVED_MEASUREMENT
SYSTEM_BLOCKED_BY_RULE
```

No machine-generated `suggested` state becomes a confirmed diagnosis/prescription by persistence alone.

---

# 6. Diagnostic / therapeutic decision boundary

MDR Rule 11 specifically addresses software intended to provide information used to make diagnostic or therapeutic decisions, with class depending on potential impact of those decisions.

BiomechE-CAD therefore treats the following as **regulatory-significant claim boundaries** requiring formal assessment before product claims are made:

```text
automatic diagnosis
automatic treatment selection
patient-specific therapeutic recommendation
automatic clinical risk stratification
automatic statement that one orthosis design is clinically optimal
algorithmic threshold interpreted as diagnosis/treatment decision
```

Current P0 semantics deliberately avoid these claims by keeping profiles contextual, suggestions unconfirmed, and outcomes/thresholds evidence-bound.

---

# 7. Risk-management boundary

If/where BiomechE-CAD is within medical-device scope, risk management should be integrated across lifecycle using the applicable regulatory/QMS process. ISO 14971:2019 remains current after 2025 confirmation and provides the medical-device risk-management process framework.

This product document defines **hazard themes**, not final risk acceptability criteria.

Candidate hazard families:

```text
wrong patient/case
wrong side/laterality
wrong units/scale
wrong source registration
incorrect/unreviewed landmarks
stale or incompatible source data
semantic mirror error
incorrect dose realization
material identity/property confusion
clinical threshold used outside profile
measured vs predicted confusion
manufacturing artifact/revision mismatch
blocking QC bypass
physical-part identity mix-up
loss/corruption of provenance
unauthorized data access/change
software update changing historical interpretation
algorithm performance/latency causing stale state presentation
```

Risk acceptability limits are not defined here.

---

# 8. Safety-related product controls already frozen

Existing BiomechE-CAD contracts already provide candidate controls for multiple hazard themes:

```text
immutable DesignRevision
source/hash provenance
typed side/anatomical placement
requested vs realized dose
profile non-transfer rules
OPEN numerical states
measured != predicted
workflow/preset exact version/hash
warning vs blocking states
ManufacturingArtifact != PhysicalOrthosis
blocking QC state
report source manifests
```

Future risk management should map hazards→controls→verification IDs rather than duplicate semantic logic.

---

# 9. Software lifecycle / security significance

MDR Annex I software requirements include development/manufacture according to state of the art taking account of software lifecycle, risk management including information security, verification and validation; they also address requirements for hardware/network characteristics and cybersecurity protection needed for intended operation.

If BiomechE-CAD falls within that scope, the existing V&V/performance/provenance plans provide partial engineering inputs but do not alone establish conformity.

Current EU guidance registry still lists MDCG 2019-16 rev.1 as cybersecurity guidance for medical devices.

---

# 10. Privacy data classification

BiomechE-CAD may process data that constitute personal data and, depending on content/context, health data under GDPR.

Potential data categories:

```text
direct identifiers
pseudonymous patient/case ID
contact/demographic data
clinical indication/context
foot morphology/scan data
pressure/biomechanics data
prescription/design history
PROM/pain/function data
adherence/service data
manufacturing/physical-part linkage
operator/professional identity
audit/security logs
```

Whether a specific datum is personal/health data depends on identifiability and context; a UUID alone does not automatically anonymize linked clinical data.

---

# 11. Privacy by design / minimization

GDPR Article 25 requires appropriate technical/organizational measures implementing data-protection principles such as minimization and protection by default.

Product doctrine:

```text
collect only data needed for declared purposes
separate clinical identity from manufacturing-minimum handoff
prefer pseudonymous IDs across manufacturing/external packages
avoid copying demographics into geometry files
make retention/export purpose explicit
preserve provenance without duplicating unnecessary identity data
```

Pseudonymization is a safeguard; it is not equivalent to irreversible anonymization.

---

# 12. Privacy contexts / package policies

Define package policy classes such as:

```text
FULL_CLINICAL_PROJECT
CLINICAL_REPORT
BIOMECHE_INTEGRATION_MINIMUM
MANUFACTURING_MINIMUM
EXTERNAL_INSPECTION_MINIMUM
RESEARCH_PSEUDONYMOUS
SUPPORT_DIAGNOSTIC_PACKAGE [explicit consent/policy]
```

Each policy defines which fields/assets are permitted, required, redacted or pseudonymized.

Manufacturing packages SHOULD default to the minimum identity needed for traceable production under organizational policy.

---

# 13. Security requirements baseline

GDPR Article 32 requires security appropriate to risk, including as appropriate pseudonymization/encryption, confidentiality/integrity/availability/resilience, restoration capability and regular evaluation of controls.

Product/security architecture SHALL therefore plan for:

```text
identity/authentication where multi-user/networked
role/authorization boundaries
transport protection
storage protection appropriate to deployment
integrity hashes for immutable artifacts
secure secrets/key handling
backup/restore and disaster recovery
security/audit logging
session/access control
update provenance
vulnerability/dependency management
incident response hooks
periodic security verification
```

Exact cryptographic algorithms/key policies belong to a dedicated security architecture/threat model and current organizational security standards, not this semantic document.

---

# 14. Authentication / authorization doctrine

When deployed with user accounts:

```text
identity != authorization
clinical role != system administrator
read != modify != commit != release manufacturing != accept QC
```

Suggested permission boundaries include:

```text
VIEW_CASE
IMPORT_SOURCE
EDIT_WORKING_DESIGN
CONFIRM_PROFILE_OR_LANDMARK
COMMIT_DESIGN
GENERATE_MANUFACTURING_ARTIFACT
RELEASE_MANUFACTURING_PACKAGE
ENTER_QC
ACCEPT_PHYSICAL_PART
VIEW_IDENTIFIERS
EXPORT_CLINICAL_DATA
ADMINISTER_USERS
```

Exact role mapping is deployment/configuration policy.

---

# 15. Audit trail

Security/clinical/manufacturing-significant actions SHOULD generate append-only/auditable events with:

```text
who / agent
what action
object/revision affected
before/after semantic reference where appropriate
timestamp
reason/override note where required
software version
result
```

High-value actions include:

```text
side/units override
landmark/profile confirmation
DesignRevision commit
manufacturing release
blocking warning override/deviation
QC acceptance
external export
data deletion/retention action
permission/security changes
```

Audit trail must avoid unnecessarily duplicating protected content.

---

# 16. Data retention / deletion boundary

No universal retention period is frozen here because legal/clinical/QMS requirements depend on role, jurisdiction and device status.

The system should support policy-driven:

```text
retention class
legal/QMS hold
de-identification/pseudonymization
export before deletion
soft/queued deletion where policy requires
cryptographic/object-store lifecycle where applicable
audit of retention action
```

Deletion policy must account for immutable regulatory/manufacturing records and data-subject rights; this requires deployment-specific legal/QMS review.

---

# 17. Backup / restore / integrity

Backup and restore must preserve:

```text
project semantic consistency
asset hashes/links
revision immutability
manufacturing/physical-part lineage
audit identity
schema/version metadata
```

Restore is a controlled recovery operation, not creation of silent duplicate authoritative histories.

---

# 18. Cloud / processor boundary

If patient/health data are processed in cloud/external services, the deployment must identify:

```text
controller / processor roles
purpose and processing scope
data location/transfer context
subprocessors
security responsibilities
backup/retention responsibilities
support access policy
incident/breach process
```

The codebase SHALL NOT assume that selecting a cloud provider automatically resolves GDPR/QMS obligations.

---

# 19. Research / analytics / AI boundary

Secondary research/analytics and model training require an explicit lawful/governance basis and dataset policy separate from routine patient-care/manufacturing use.

Product rule:

```text
operational patient project data
!= automatically approved model-training corpus
```

Future ML/AI functionality must preserve:

```text
model ID/version
training/validation provenance where applicable
intended use/applicability domain
uncertainty/quality state
suggestion vs confirmation
measured vs predicted output
```

Current EU guidance includes a 2025 FAQ on MDR/IVDR interaction with the AI Act; applicability must be reassessed when AI functionality becomes a release feature.

---

# 20. Regulatory change surveillance

Regulatory/guidance baselines change. Maintain a periodic review of at least:

```text
EU MDR consolidated text
MDCG software qualification/classification guidance
MDCG cybersecurity guidance
custom-made-device guidance
MDR/AI Act guidance when AI is in scope
GDPR / national privacy guidance
harmonised standards/common specifications relevant to final intended purpose
```

A new guidance version triggers impact review, not automatic product-semantic mutation.

---

# 21. Formal regulatory decision gate

Before first regulated-market release, a controlled assessment must decide and document:

```text
manufacturer/legal entity
final intended purpose/claims
software qualification under MDR or exclusion rationale
accessory/module boundaries
classification rule(s) if applicable
custom-made/patient-matched/device-production pathway implications
QMS scope
risk-management process
clinical evaluation/performance evidence scope
software lifecycle/usability/cybersecurity standards applicability
post-market/vigilance obligations
labeling/UDI/EUDAMED implications where applicable
```

This is a project gate outside geometry-engine selection.

---

# 22. Acceptance tests / governance checks

```text
REG-001 final intended-purpose statement exists before regulatory classification claim
REG-002 UI/marketing/manual claims do not exceed approved intended purpose
REG-003 suggestion cannot persist as confirmed diagnosis/prescription without explicit authority
REG-004 profile evidence rule does not become universal clinical threshold
REG-005 regulatory classification status is explicit, never inferred from code architecture
REG-006 custom-made-device status is not inferred solely from patient-specific geometry
REG-007 risk register can trace hazard -> control -> verification evidence
REG-008 health/personal data export follows explicit package/privacy policy
REG-009 manufacturing-minimum package excludes unnecessary direct demographics by default policy
REG-010 pseudonymous ID is not labelled anonymous without anonymization assessment
REG-011 permission model separates view/edit/commit/release/QC/admin actions
REG-012 significant override/release/QC/security actions are auditable
REG-013 backup/restore preserves immutable lineage and integrity identities
REG-014 operational project data is not automatically used for model training
REG-015 regulatory/guidance baseline has version/date and periodic review
REG-016 formal market-release gate records current MDR/MDCG/GDPR applicability assessment
```

---

# 23. Current open decisions

The following remain intentionally **OPEN**:

```text
final software MDR qualification
software MDR class, if applicable
accessory vs standalone/module boundaries
exact custom-made/patient-matched pathway for final orthosis business model
QMS certification scope
final data-controller/processor model per deployment
retention periods
DPIA requirement per deployment/processing scale
cybersecurity architecture/control baseline
AI Act applicability for future AI features
```

`OPEN` is safer and more correct than an unsupported early classification.

---

# 24. Current official-source baseline

The 2026 documentation pass verified against official sources:

```text
Regulation (EU) 2017/745 — current consolidated MDR baseline
MDCG 2019-11 rev.1 — software qualification/classification, June 2025
MDCG 2021-24 rev.1 — medical-device classification guidance, April 2026
MDCG 2019-16 rev.1 — cybersecurity guidance (current MDCG registry listing)
MDCG 2021-3 — custom-made-device Q&A
Regulation (EU) 2016/679 — GDPR
ISO 14971:2019 — confirmed current 2025
ISO 13485:2016 — confirmed current 2025
```

These sources guide assessment; their presence here is not a claim of conformity/certification.

---

# 25. Frozen boundary invariants

```text
capability != intended purpose
patient-specific != automatically custom-made regulatory status
suggestion != diagnosis
suggestion != confirmed prescription
pseudonymized != anonymous
health-data provenance != permission to reuse for AI training
security hash != access control
software verification != regulatory conformity
regulatory guidance != product classification until formal assessment
```

---

# 26. Product conclusion

BiomechE-CAD documentation must preserve enough separation that a future regulatory/QMS team can answer:

```text
What exactly is the software intended to do?
Who is responsible for the prescription/design decision?
Which outputs influence diagnosis/treatment/manufacturing?
Which data are health/personal data and why are they processed?
Which safeguards/roles/audit records exist?
Which hazards map to which verified controls?
What is software scope vs physical-orthosis/manufacturing scope?
Which regulatory classification decisions are actually approved, and which remain OPEN?
```

This boundary is canonical while the final legal/regulatory classification remains deliberately unresolved.

---

## Current official-source supplements pending canonical bibliography normalization

- Regulation (EU) 2017/745 (MDR), current consolidated official EUR-Lex text.
- MDCG 2019-11 rev.1, *Qualification and classification of software — Regulation (EU) 2017/745 and Regulation (EU) 2017/746*, June 2025.
- MDCG 2021-24 rev.1, *Guidance on classification of medical devices*, April 2026.
- MDCG 2019-16 rev.1, *Guidance on cybersecurity for medical devices*, current MDCG registry.
- MDCG 2021-3, *Questions and Answers on Custom-Made Devices*.
- Regulation (EU) 2016/679 (GDPR), especially Articles 9, 25, 32 and risk-based DPIA provisions.
- ISO 14971:2019, *Medical devices — Application of risk management to medical devices*, confirmed current in 2025.
- ISO 13485:2016, *Medical devices — Quality management systems — Requirements for regulatory purposes*, confirmed current in 2025.
