# BiomechE-CAD — Competitor Functional Gap Audit

**Date:** 2026-08-15  
**Status:** FIRST PUBLIC-SOURCE BASELINE / market-function audit  
**Scope:** publicly documented functional capabilities relevant to custom foot-orthosis CAD/CAM.  
**Architecture:** out of scope; this audit does not select a geometry kernel.  
**Scientific authority:** competitor/vendor claims are never treated as clinical-efficacy evidence.

---

## 1. Purpose and evidence rule

This audit asks:

```text
what workflow capabilities are publicly evidenced in current competing systems?
which of those are already baseline requirements for BiomechE-CAD?
where is BiomechE-CAD intentionally stronger in semantics/traceability?
where do competitor public materials reveal a real functional gap to investigate?
```

Public vendor pages support only **market/product capability** claims.

Language rule:

```text
EVIDENCED
  capability explicitly stated/shown on reviewed public source

PARTIALLY EVIDENCED
  adjacent capability is documented but exact semantic depth is unclear

NOT EVIDENCED ON REVIEWED PUBLIC SOURCE
  do NOT interpret as proof that the product lacks the capability
```

No clinical superiority is inferred from vendor marketing.

---

## 2. Reviewed systems

### Sensor Medica EasyCAD2

Role: behavioral baseline already audited in depth from the primary manual + validation plan/report [EC2-MANUAL-1.1; EC2-VAL-PLAN-1.4; EC2-VAL-REPORT-1.4].

### Vertex Orthopedic — OrthoCAD

Publicly documents 2D/3D scan workflow, prescription/template-driven design, medial/lateral posting, arch adjustment, CNC/3D-print export and patient/design history [VENDOR-VERTEX-ORTHOCAD].

### Insolution — Manager / OrthoPodoCad ecosystem

Publicly documents control of 2D/3D scanners and pressure plate, patient/history/gait-video/report/treatment-plan workflow, material/thickness/Shore prescription, and pressure imagery usable during orthotic modelling [VENDOR-INSOLUTION-SOFTWARE; VENDOR-INSOLUTION-PRESSURE].

### Voxelcare

Publicly documents 2D, 3D and plantar-pressure acquisition, cloud CAD, custom orthotic design, and integrated CNC/3D-print production [VENDOR-VOXELCARE].

### Sharp Shape — AOMS

Publicly documents 3D scanners, prescription-driven biomechanical cast corrections, orthotic-shell/footbed workflows, CNC toolpath integration and newer 3D-print workflows [VENDOR-SHARPSHAPE-AOMS].

---

## 3. Functional comparison matrix

Legend:

```text
YES      explicitly evidenced
PARTIAL  related capability evidenced; exact semantics not established
N/E      not evidenced on reviewed public source
```

| Capability | EasyCAD2 | OrthoCAD | Insolution | Voxelcare | Sharp Shape AOMS | BiomechE-CAD target |
|---|---:|---:|---:|---:|---:|---|
| patient/case workflow | YES | YES | YES | PARTIAL | PARTIAL | P0 + external patient-link boundary |
| 2D scan/image input | YES | YES | YES | YES | PARTIAL | P0 explicit calibration/frame |
| 3D scan input | YES | YES | YES | YES | YES | P0 raw immutable + landmark registration |
| plantar-pressure input | YES | YES/PARTIAL | YES | YES | N/E reviewed | P0 quantitative numeric authority |
| pressure as design background | YES | YES | YES | YES/PARTIAL | N/E reviewed | P0 plus metric ROI/outcome semantics |
| template/prescription workflow | YES | YES | YES | YES | YES | P0 exact version/hash |
| arch/posting/corrections | YES | YES | PARTIAL | YES/PARTIAL | YES | P0 structured dose + anatomical reference |
| local relief/accommodation | YES | YES | PARTIAL | YES/PARTIAL | YES | P0 corrective/offload semantics |
| material/thickness parameters | YES | YES | YES | PARTIAL | PARTIAL | P0 geometry vs mechanical dose separation |
| multi-density/variable mechanics | YES/PARTIAL | YES | PARTIAL | PARTIAL | N/E reviewed | P0/P1 explicit material regions/provenance |
| sculpt/manual correction | YES | YES | PARTIAL | YES/PARTIAL | YES | P0 replayable/versioned operation |
| CNC output | YES | YES | PARTIAL | YES | YES | P0 profile/run/artifact lineage |
| 3D-print output | YES | YES | PARTIAL | YES | YES | P0 profile/run/artifact lineage |
| design history/reorder | YES | YES | PARTIAL | PARTIAL | N/E reviewed | P0 immutable DesignRevision graph |
| report generation | YES | YES/PARTIAL | YES | N/E reviewed | N/E reviewed | P0 exact-source report artifact |
| quantitative before/after outcome | PARTIAL | vendor page claims before/after pressure | PARTIAL | N/E reviewed | N/E reviewed | P0 protocol/ROI/quality-gated comparison |
| explicit raw numeric pressure provenance | PARTIAL | N/E reviewed | N/E reviewed | N/E reviewed | N/E reviewed | P0 |
| exact ROI/region versioning | N/E | N/E | N/E | N/E | N/E | P0 |
| measured vs predicted distinction | N/E | N/E | N/E | N/E | N/E | P0 |
| indication/evidence profile versioning | N/E | N/E | N/E | N/E | N/E | P0 |
| PROM/comfort/fit/adherence separation | N/E | N/E | PARTIAL clinical record | N/E | N/E | P0/P1 depending module |
| material nominal vs manufactured vs aged | N/E | N/E | N/E | N/E | N/E | P0 provenance model |
| CAD revision vs manufactured physical copy | N/E | N/E | N/E | N/E | N/E | P0 distinct identities |
| blocking QC prevents accepted-part state | PARTIAL | vendor claims built-in manufacturing checks | N/E | N/E | N/E | P0 explicit gate |
| append-only service/longitudinal state | N/E | N/E | follow-up record PARTIAL | N/E | N/E | P0 schema |
| machine-readable provenance graph | N/E | N/E | N/E | N/E | N/E | P0 |
| reproducible report source manifest | N/E | N/E | N/E | N/E | N/E | P0 target |

`N/E` means only that the reviewed public material did not establish the capability.

---

## 4. Market baseline that BiomechE-CAD must meet

The reviewed market material makes the following capabilities table stakes rather than differentiators:

```text
2D/3D scan ingestion
orthosis-specific CAD rather than generic freeform CAD
prescription/template libraries
arch/posting/accommodation adjustments
pressure visualization/integration in at least some systems
patient/case storage
CNC and/or 3D-print manufacturing output
repeatable/customizable workflows
```

Therefore BiomechE-CAD cannot claim product leadership merely because it supports scan->CAD->STL/CNC.

---

## 5. Differentiation target 1 — semantic prescription survives geometry

BiomechE-CAD freezes a stronger contract:

```text
feature type
side/anatomical target
dose + units
placement/reference frame
ROI/landmark references
material/mechanical dose
intent
evidence refs
algorithm/profile version
```

The final surface/mesh does not erase this semantic state.

Public competitor materials often demonstrate strong orthosis-specific tooling, but the reviewed pages do not establish an equivalent immutable semantic/audit contract. This remains a **traceability differentiation hypothesis**, not a claim that competitors lack internal metadata.

---

## 6. Differentiation target 2 — quantitative outcome loop, not pressure wallpaper

BiomechE-CAD requires:

```text
raw numeric pressure
+ device/calibration/protocol
+ RegionModel/ROI version
+ quality status
+ exact KPI algorithm/profile
+ target/safety-ring/remote regions
+ measured physical orthosis identity
+ compatibility-gated before/after comparison
```

This goes beyond simply displaying a colored pressure map behind the CAD.

The design is supported by pressure-guided optimization research [REF-CAD-005, pp. 1595–1600] and by evidence that protocol/step count and device characteristics affect pressure-result validity/comparability [REF-CAD-108; REF-CAD-109; REF-CAD-036].

---

## 7. Differentiation target 3 — design != manufacturing artifact != physical part

BiomechE-CAD explicitly models:

```text
DesignRevision
   !=
ManufacturingArtifact
   !=
PhysicalOrthosis
```

and keeps:

```text
manufacturing profile/run
machine/process
material lot
QC measurement
acceptance state
service-aged state
```

This permits two physical copies produced from one CAD revision to have different lot/run/QC/service histories.

The reviewed competitor pages strongly evidence manufacturing connectivity, but not this exact public traceability model.

---

## 8. Differentiation target 4 — evidence/profile governance

BiomechE-CAD does not treat a diagnosis label or vendor template as a universal rule.

It preserves:

```text
IndicationProfile exact version/hash
population/context boundary
OutcomeTarget evidence refs
protocol/ROI-specific threshold
USER_CONFIRMED vs SUGGESTED_NOT_CONFIRMED
```

This is particularly important because orthosis/offloading evidence is population- and protocol-dependent; it should not leak silently from diabetic-foot evidence into metatarsalgia, flatfoot, heel-pain or sport workflows.

No reviewed competitor page was sufficient to establish comparable evidence-governance semantics; that is a documentation gap, not proof of absence.

---

## 9. Differentiation target 5 — reporting as provenance

BiomechE-CAD reports are immutable derived artifacts over exact source references.

Required lineage includes:

```text
source DesignRevision/hash
acquisition/protocol
BiomechE KPI/version/quality
ROI/profile/evidence version
material/manufacturing/physical part
QC
measured/predicted outcome
PROM/adherence constructs
report generator/version
report bytes/hash
```

This follows biomedical provenance/reproducibility principles [REF-CAD-111; REF-CAD-113].

A report PDF is therefore a view over a machine-readable traceability graph, not the only historical record.

---

## 10. Competitor signals worth adopting/validating

### 10.1 OrthoCAD — reusable macro/workflow automation

Current public OrthoCAD material emphasizes reusable automation/macros and parametric recalculation [VENDOR-VERTEX-ORTHOCAD].

BiomechE-CAD already has immutable operation stacks/presets, but should explicitly ensure that future UI/workflow layers support:

```text
named multi-operation macro/preset
ordered operations
parameter dependencies
preview before commit
exact macro/preset version + hash
```

This is a **real functional follow-up**, independent of the geometry engine.

### 10.2 Insolution — integrated clinical record / gait video / follow-up

Insolution publicly combines scanner/pressure control with history, gait video, findings, report, treatment plan and follow-up [VENDOR-INSOLUTION-SOFTWARE].

BiomechE-CAD should remain CAD-focused rather than duplicate a full EMR, but the competitor signal supports clear adapter hooks for:

```text
external clinical record
video/media evidence refs
follow-up/service assessment
report handoff
```

### 10.3 Voxelcare — cloud end-to-end workflow

Voxelcare publicly presents scan->cloud CAD->production as one connected ecosystem [VENDOR-VOXELCARE].

BiomechE-CAD schema is already storage/runtime independent; later implementation should preserve this portability instead of assuming desktop-local storage.

### 10.4 Sharp Shape — configurable correction workflows + long manufacturing integration

Sharp Shape publicly documents prescription-driven corrections and configurable CNC integration [VENDOR-SHARPSHAPE-AOMS].

BiomechE-CAD should retain equivalent ability to adapt manufacturing profiles without changing clinical prescription semantics.

---

## 11. Gaps to add to product backlog

### GAP-COMP-001 — workflow macro/preset orchestration

**Priority:** P1 product UX / semantic layer.  
Define a versioned multi-operation workflow preset/macro contract instead of only single-element presets.

Acceptance direction:

```text
macro version/hash frozen in committed revision
ordered operation expansion visible
parameter overrides explicit
replay deterministic at semantic level
later macro edits do not mutate historical revisions
```

### GAP-COMP-002 — external clinical-media adapter

**Priority:** P1 integration.  
Allow video/photo/clinical-document evidence links without turning BiomechE-CAD into the authoritative EMR.

### GAP-COMP-003 — cloud/offline synchronization contract

**Priority:** P1/P2 implementation architecture, not yet runtime selection.  
Project IDs, immutable revisions/assets/hashes already support this direction; conflict/sync semantics need a future dedicated spec.

### GAP-COMP-004 — manufacturing-profile UX breadth

**Priority:** P1 after actual process qualification.  
Competitors expose broad CNC/3D-print workflows. BiomechE-CAD must make qualified profile/machine/material selection practical while retaining traceability.

---

## 12. Things **not** justified by this audit

The public-source audit does not justify:

```text
adding a geometry kernel
copying a competitor internal representation
assuming vendor clinical-efficacy claims are proven
claiming a competitor lacks a feature not mentioned publicly
hard-coding competitor material/pressure thresholds
reopening OpenSubdiv vs ON_SubD
```

---

## 13. Next competitor-research phase

A deeper audit should acquire, where lawfully/contractually available:

```text
current manuals / release notes
trial/demo workflows
report examples
project/export file semantics
pressure comparison behavior
revision/history behavior
material/manufacturing profile semantics
QC/physical-part tracking
cloud/offline behavior
API/interoperability surfaces
```

Priority comparison systems:

```text
EasyCAD2
OrthoCAD
Insolution / OrthoPodoCad
Voxelcare
Sharp Shape AOMS
additional modern 3D-print-first systems after source qualification
```

This deeper phase remains parallel to product-specific acquisition/material/process qualification.

---

## 14. First-pass conclusion

The market baseline is already strong at:

```text
scan
orthosis-specific CAD
corrections/templates
manufacturing output
```

BiomechE-CAD should therefore optimize for a more defensible differentiator:

```text
EVIDENCE
  + QUANTITATIVE BIOMECHANICS
  + SEMANTIC PRESCRIPTION
  + IMMUTABLE REVISION
  + MANUFACTURING / PHYSICAL-PART LINEAGE
  + OUTCOME LOOP
  + REPRODUCIBLE REPORTING
```

while still matching the usability/automation breadth of established orthotic CAD/CAM systems.
