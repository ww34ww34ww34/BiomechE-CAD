# BiomechE-CAD — Specifica funzionale consolidata v2

**Stato:** CANONICAL FUNCTIONAL BASELINE v2  
**Data:** 2026-08-14  
**Architettura:** intenzionalmente non selezionata / parked  
**Bibliografia canonica:** `docs/BIBLIOGRAPHY.md`  
**Baseline storica preservata:** `docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC.md`

---

## 0. Scopo

Questo documento è la specifica funzionale consolidata di BiomechE-CAD dopo l'audit EasyCAD2 e i research batch evidence-led 03–08.

La regola di progetto è:

```text
FUNZIONALITÀ
+ EASYCAD2 PARITY
+ LETTERATURA SCIENTIFICA / BIOMECCANICA
+ DOSE / POSIZIONAMENTO / CONTESTO
+ OUTCOME MISURABILI
+ MATERIALE / PROCESSO / STATO DEL PEZZO
        ↓
REQUISITI DI PRODOTTO
        ↓
PROJECT SCHEMA + ACCEPTANCE SUITE
        ↓
ARCHITETTURA / KERNEL DOPO
```

La specifica definisce **che cosa** il prodotto deve rappresentare, misurare, versionare e validare. Non impone OpenSubdiv, openNURBS, B-Rep o un'altra tecnologia geometrica.

---

# 1. Governance delle fonti

## 1.1 Autorità bibliografica

`docs/BIBLIOGRAPHY.md` è l'unica bibliografia autorevole.

Namespace correnti:

```text
EC2-*      EasyCAD2 primary evidence
GUIDE-*    guideline / consensus
REF-CAD-*  letteratura scientifica
STD-*      standard tecnici / test / manufacturing
VENDOR-*   evidenza di mercato
ARCH-*     ricerca tecnica di architettura
```

I documenti funzionali citano ID stabili e locator verificati, per esempio:

```text
[EC2-MANUAL-1.1, pp. 31–35]
[REF-CAD-013, pp. 84–88]
[GUIDE-IWGDF-2023, Prevention guideline]
```

Non inventare pagine o precisione non verificata.

## 1.2 Ruolo delle evidenze

- EasyCAD2 è **baseline comportamentale**, non verità scientifica.
- La letteratura supporta o limita l'interpretazione di dose, placement, outcome e profili.
- Gli standard definiscono scope/test/qualification semantics; non implicano automaticamente conformità del prodotto.
- Le decisioni di prodotto sono registrate in `docs/DECISIONS.md`.
- Le formule geometriche sperimentali restano separate dall'evidenza clinica.

## 1.3 Baseline EasyCAD2

Fonti primarie:

- `EC2-MANUAL-1.1`;
- `EC2-VAL-PLAN-1.4`;
- `EC2-VAL-REPORT-1.4`.

Il validation report registra 25 test pianificati, 25 eseguiti e 25 PASS. La copertura funzionale è conservata in `docs/validation/easycad2_geometry_parity.md`.

---

# 2. Principi funzionali non negoziabili

## CAD-PRINC-001 — CAD verticale, non modellatore generico

BiomechE-CAD è specializzato nel workflow di plantari/ortesi plantari personalizzate. Un kernel CAD general-purpose non è un requisito di prodotto P0.

## CAD-PRINC-002 — Prescrizione semantica, non sola geometria finale

Ogni feature clinicamente significativa deve sopravvivere come oggetto/versione con:

```text
tipo
lato
regione anatomica
dose
unità
reference frame / landmark
estensione / placement
material/mechanical properties
intent
source/evidence
algorithm version
```

## CAD-PRINC-003 — Non distruttività e riproducibilità

Le operazioni devono essere versionate e ricostruibili ove tecnicamente ragionevole. Undo/redo non deve essere l'unica forma di provenance.

## CAD-PRINC-004 — Quantità fisiche esplicite

Unità canoniche coerenti con BiomechE:

```text
mm
s
N
kPa
deg
mm²
```

Conversioni e unità alternative devono essere esplicite e reversibili.

## CAD-PRINC-005 — Misurato ≠ predetto

`MeasuredOutcome`, `PredictedOutcome`, geometria nominale CAD e geometria misurata del pezzo fisico sono classi distinte.

## CAD-PRINC-006 — Nessun optimum universale nascosto

Threshold, preset e target evidence-based sono sempre legati a:

```text
population / indication
metric
ROI
protocol
evidence source
confidence
```

## CAD-PRINC-007 — Offloading = redistribuzione

Un miglioramento nella ROI target non è sufficiente senza controllare regioni circostanti e/o remote quando clinicamente rilevante.

## CAD-PRINC-008 — Geometry dose ≠ mechanical dose

Forma, spessore, materiale, durezza, stiffness, densità e struttura interna non devono essere compressi in un singolo slider ambiguo.

## CAD-PRINC-009 — Artifact chain completa

```text
Case
→ Acquisition
→ Prescription
→ DesignRevision
→ ManufacturingProfile
→ ManufacturingRun
→ PhysicalOrthosis
→ QC
→ WearExposure / ServiceState
→ Outcome
```

Ogni passaggio mantiene provenance.

---

# 3. Priorità

## P0 — core product

Necessario per un MVP professionalmente utilizzabile e coerente con la baseline EasyCAD2 + requisiti evidence-led maturi.

## P1 — advanced / next release

Valore elevato ma non necessario per il primo freeze funzionale.

## P2 — future / integration / R&D

Capacità future, specialistiche o dipendenti da hardware/evidenza ulteriore.

---

# 4. Modello funzionale di dominio

Il futuro `spec/02_project_schema.md` deve poter rappresentare almeno le seguenti entità.

```text
Patient
Case
OrthosisProject
DesignRevision

IndicationProfile[]
activeInterpretationProfile

Acquisition
ScanAcquisition
PressureAcquisition
Image2DAcquisition
Registration

Prescription
ArchSupportPrescription
HeelPrescription
RearfootWedgePrescription
ForefootWedgePrescription
CorrectiveElement
OffloadFeature
SculptOperation
ScanConformOperation

MaterialDefinition
MaterialLot
MaterialRegion
MaterialStack
StructuralMaterialRegion
MechanicalPropertyMeasurement
DurabilityTest
ServiceState

OutcomeTarget
OutcomeMeasurement
OffloadAssessment
MetricThreshold

PROMInstrumentDefinition
PROMMeasurement
ComfortAssessment
FitUsabilityAssessment
SatisfactionAssessment
AdherenceMeasurement
PatientExperienceBundle
InterpretationRule

ManufacturingProfile
ManufacturingRun
ManufacturingArtifact
PhysicalOrthosis
PostProcessStep
QCRequirement
QCMeasurement
ManufacturedGeometryMeasurement

ExportArtifact
ReportArtifact
AuditEvent
```

---

# 5. Progetto, paziente, casi e revisioni

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-PROJ-001 | Creare, modificare, ricercare e riaprire pazienti/casi | P0 |
| CAD-PROJ-002 | Collegare un caso a un ID paziente esterno/BiomechE | P0 |
| CAD-PROJ-003 | Gestire più casi e più revisioni nel tempo | P0 |
| CAD-PROJ-004 | Supportare DX/SX nello stesso case con identità separate | P0 |
| CAD-PROJ-005 | Conservare autore, timestamp, note e rationale per revisione | P0 |
| CAD-PROJ-006 | Rendere una revisione referenziabile in modo immutabile da export/outcome/QC | P0 |
| CAD-PROJ-007 | Import/export case package con manifest e hash | P1 |
| CAD-PROJ-008 | Offline-first per il normale authoring | P0 |

Baseline EasyCAD2: `[EC2-MANUAL-1.1, pp. 7–12]`, validation US1–US5.

---

# 6. Viewport, navigazione e laterality

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-VIEW-001 | Orbit, pan e zoom fluidi | P0 |
| CAD-VIEW-002 | Viste ortogonali e isometrica/default | P0 |
| CAD-VIEW-003 | Griglia metrica e assi/coordinate quando richiesti | P0 |
| CAD-VIEW-004 | Trasparenza e toggle layer | P0 |
| CAD-VIEW-005 | Height-map / quota sotto cursore | P0 |
| CAD-VIEW-006 | Righello 2D/3D | P0 |
| CAD-VIEW-007 | Picking/multi-select deterministico | P0 |
| CAD-LR-001 | Switch DX/SX esplicito | P0 |
| CAD-LR-002 | Mirror completo del progetto | P0 |
| CAD-LR-003 | Mirror semanticamente corretto medial↔lateral | P0 |
| CAD-LR-004 | Modifica indipendente dopo mirror | P0 |
| CAD-LR-005 | Mirror selettivo di feature/prescrizioni | P1 |

Baseline EasyCAD2: `[EC2-MANUAL-1.1, p. 13–14]`, US6.

---

# 7. DIMA / Base Template

## 7.1 Capacità P0

- template di base corrispondenti almeno alle famiglie funzionali EasyCAD2 SPORT/SANDALO/CLASSIC/COMFORT/DONNA;
- side-aware;
- lunghezza e larghezza in mm;
- shoe-size come metadato/mapping, non sostituto della geometria fisica;
- editing outline;
- salvataggio/caricamento template custom;
- morph non distruttivo;
- possibilità di registrare quale template/versione ha generato il design.

Baseline: `[EC2-MANUAL-1.1, pp. 15–18]`, US7.

## 7.2 Requisiti

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-TPL-001 | Selezione template/famiglia | P0 |
| CAD-TPL-002 | Lunghezza e larghezza fisiche esplicite | P0 |
| CAD-TPL-003 | Editing outline | P0 |
| CAD-TPL-004 | Template custom versionato | P0 |
| CAD-TPL-005 | Advanced template authoring | P1 |
| CAD-TPL-006 | Provenance del template | P0 |

---

# 8. Acquisizioni e registrazione

## 8.1 Pressione plantare

La pressure-map è una vista di dati numerici; RGB non è la fonte autorevole.

P0:

```text
source/device/model
calibration
sample rate quando disponibile
side
units
activity / gait protocol
speed protocol
footwear
orthosis revision
steps / trials
ROI mask version
coordinate system
registration
quality flags
```

Il design pressure-informed ha evidenza diretta in specifiche popolazioni [REF-CAD-004; REF-CAD-005; REF-CAD-069], senza diventare una regola universale.

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-PRESS-001 | Import pressione quantitativa | P0 |
| CAD-PRESS-002 | Traslazione/rotazione/scala/registrazione esplicita | P0 |
| CAD-PRESS-003 | Overlay heatmap derivato | P0 |
| CAD-PRESS-004 | ROI statistiche quantitative | P0 |
| CAD-PRESS-005 | Comparazione pre/post protocol-aware | P0 |
| CAD-PRESS-006 | Pressure-guided target authoring | P1 |
| CAD-PRESS-007 | Continuous/wearable pressure integration | P2 |

Baseline EasyCAD2: `[EC2-MANUAL-1.1, pp. 19–20]`, US8.

## 8.2 Scan3D

P0:

```text
original asset + hash
scanner/device
resolution/declared accuracy quando disponibile
weight-bearing condition
heel / 1st / 5th landmarks
side
coordinate system
registration transform
quality flags
```

La letteratura mostra eterogeneità di scanner e protocolli [REF-CAD-002; REF-CAD-003], quindi il contesto di acquisizione è parte dei dati.

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-SCAN-001 | Import STL/mesh 3D | P0 |
| CAD-SCAN-002 | Landmark heel/1st/5th | P0 |
| CAD-SCAN-003 | Align/registration | P0 |
| CAD-SCAN-004 | Crop/clean reference scan | P0 |
| CAD-SCAN-005 | Provenance di acquisizione | P0 |
| CAD-SCAN-006 | ICP/advanced registration | P1 |

Baseline EasyCAD2: `[EC2-MANUAL-1.1, pp. 21–22]`, US9.

## 8.3 Scan2D / Image2D

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-IMG-001 | Import immagine/scan 2D | P0 |
| CAD-IMG-002 | Calibrazione metrica esplicita | P0 |
| CAD-IMG-003 | Align/rotation/translation | P0 |
| CAD-IMG-004 | Provenance e scala salvate | P0 |

Baseline: `[EC2-MANUAL-1.1, p. 23]`.

---

# 9. Spessore, flatten e morph globale

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-BASE-001 | Spessore globale esplicito | P0 |
| CAD-BASE-002 | Flatten controllato | P0 |
| CAD-BASE-003 | 3/4 / length-type semantics quando richieste | P0 |
| CAD-BASE-004 | Editing avanzato XYZ disponibile come authoring esperto | P1 |
| CAD-BASE-005 | Spessore clinico/nominale separato dalla sua realizzazione produttiva | P0 |

Baseline: `[EC2-MANUAL-1.1, pp. 24–30]`, US10.

---

# 10. Heel authoring

Normativa dettagliata: `research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md` e acceptance `HEEL-001..HEEL-015`.

Il tallone non è una singola feature:

```text
HeelCup / containment
HeelRelief
HeelMechanicalRegion
HeelCamber
```

P0 deve preservare separatamente geometria e meccanica.

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-HEEL-001 | Heel cup / containment parametrico | P0 |
| CAD-HEEL-002 | Posterior/medial/lateral wall semantics | P0 |
| CAD-HEEL-003 | Wrap/camber separati | P0 |
| CAD-HEEL-004 | Heel-spur/local relief come feature nominata | P0 |
| CAD-HEEL-005 | Cushion/plug/material region indipendente | P0 |
| CAD-HEEL-006 | Outcome pressione/PTI/contact area separati da pain/PROM | P0 |
| CAD-HEEL-007 | Nessun optimum universale di cup-height hardcoded | P0 |

Evidenza: [REF-CAD-018; REF-CAD-058..067]. Baseline EasyCAD2: pp. 24–30; US11.

---

# 11. Arch support

Normativa dettagliata: `research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md`, acceptance `ARCH-001..ARCH-014`.

Un arch support è:

```text
GEOMETRY DOSE
+ MECHANICAL DOSE
+ CONTEXT
+ OUTCOME
```

## P0 geometry dose

```text
archType
side
start
peak/center
end
peakHeight_mm
width/depth
curvature
roundness
transitions
reference frame / landmarks
```

## P0 mechanical dose

```text
material region
hardness value + scale quando noto
stiffness/effective modulus quando misurato/qualificato
reinforcement / structural region
```

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-ARCH-001 | Medial arch parametric authoring | P0 |
| CAD-ARCH-002 | Lateral arch parametric authoring | P0 |
| CAD-ARCH-003 | start/peak/end persistenti | P0 |
| CAD-ARCH-004 | Height in mm come dose esplicita | P0 |
| CAD-ARCH-005 | Geometry e hardness/stiffness indipendenti | P0 |
| CAD-ARCH-006 | Outcome target + midfoot/remote redistribution | P0 |
| CAD-ARCH-007 | Nessun “optimal arch” universale | P0 |
| CAD-ARCH-008 | Evidence-linked preset con population/context provenance | P1 |

Height e stiffness hanno evidenza di dose in contesti specifici; start/peak/end/curvature/roundness restano P0 authoring parameters senza calibrazione universale [REF-CAD-017; REF-CAD-045..057].

Baseline EasyCAD2: US12.

---

# 12. Rearfoot e forefoot wedges

I wedges sono prescrizioni angolari, non deformazioni anonime.

```text
angle_deg
direction
side
pivot/reference
extent
full/partial
application length
```

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-WEDGE-001 | Rearfoot posting/wedge in gradi | P0 |
| CAD-WEDGE-002 | Forefoot wedge in gradi | P0 |
| CAD-WEDGE-003 | Full/partial extent | P0 |
| CAD-WEDGE-004 | Pivot/reference e side semantics espliciti | P0 |
| CAD-WEDGE-005 | Dose salvata indipendentemente dalla mesh finale | P0 |

Dose-response support: [REF-CAD-001; REF-CAD-015]. Baseline EasyCAD2: US13.

---

# 13. Corrective elements e offloading

Normativa dettagliata: `spec/06_corrective_elements.md`; evidence Batch 03; acceptance `CE-001..CE-010` e `OFF-001..OFF-009`.

## 13.1 Elementi P0

Almeno:

```text
heel cup / spur relief
medial/lateral arch variants
metatarsal dome
metatarsal pad
metatarsal bar
metatarsal-head relief/aperture
forefoot wedge
5th-met support
proprioceptive / custom named element
```

Gli elementi devono restare semanticamente nominati.

## 13.2 Placement metatarsale

```text
targetMetatarsals
referenceLandmarks
longitudinalPosition_mm
normalizedFootPosition
transversePosition_mm / normalized
width_mm
length_mm
height_mm
rotation_deg
```

La letteratura dimostra sensibilità al placement ma non autorizza un unico default universale [REF-CAD-013; REF-CAD-041; REF-CAD-042].

## 13.3 Offloading assessment

```text
TARGET ROI
+ SAFETY RING
+ REMOTE COMPARISON REGIONS
```

Metriche almeno:

```text
PeakPressure
PTI
ContactArea
```

L'offloading può trasferire carico [REF-CAD-020; REF-CAD-029; REF-CAD-030].

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-ELEM-001 | Inserimento/posizionamento elemento | P0 |
| CAD-ELEM-002 | Scala XYZ e rotazione | P0 |
| CAD-ELEM-003 | Elementi custom salvabili/versionabili | P0 |
| CAD-ELEM-004 | Advanced vertex/edit control per custom element | P1 |
| CAD-OFF-001 | Relief/aperture nominata | P0 |
| CAD-OFF-002 | Target ROI + safety ring | P0 |
| CAD-OFF-003 | Geometry e material dose indipendenti | P0 |
| CAD-OFF-004 | Outcome comparativo pre/post | P0 |

Baseline EasyCAD2: `[EC2-MANUAL-1.1, pp. 31–35]`, US14–US15.

---

# 14. Materiale, stiffness e regioni meccaniche

Normativa: `spec/08_material_stiffness.md`; acceptance `MAT-001..MAT-018`.

Regola centrale:

```text
NOMINAL MATERIAL
!=
MANUFACTURED EFFECTIVE PROPERTY
!=
SERVICE-AGED PROPERTY
```

## 14.1 MaterialDefinition P0

```text
materialId
supplier
commercialName
formulation / grade
lot/feedstock when known
nominalDensity
hardnessValue + hardnessScale + testMethod
propertyEvidence[]
```

Un dato `50 Shore` senza scala/metodo è invalido. Hardness non viene convertita silenziosamente in Young/effective modulus.

## 14.2 Regional mechanics P0

```text
MaterialRegion
StiffnessRegion
MaterialStack
StructuralMaterialRegion
transition rule
```

Base material e effective stiffness di lattice/infill/structure sono entità diverse.

## 14.3 Durability P1/P2

Supportare provenance per:

```text
hysteresis / damping quando misurato
compression set
creep
fatigue/cyclic test
aging
service state
```

Non hardcodare una durata universale del plantare.

Evidenza: [REF-CAD-009; REF-CAD-010; REF-CAD-017; REF-CAD-021..024; REF-CAD-094..106]. Test semantics: `STD-*` in bibliografia.

Baseline EasyCAD2: US16 e US22.

---

# 15. Sculpt, smooth e scan conform

## 15.1 Sculpt / local deformation

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-SCULPT-001 | Brush con radius | P0 |
| CAD-SCULPT-002 | Strength/delta controllato | P0 |
| CAD-SCULPT-003 | Freehand/circle/ROI selection | P0 |
| CAD-SCULPT-004 | Operazione versionata, non solo bake irreversibile | P0 |
| CAD-SCULPT-005 | Smooth locale | P0 |
| CAD-SCULPT-006 | Global smooth | P0 |

Baseline EasyCAD2: `[EC2-MANUAL-1.1, pp. 36–40]`, US17.

## 15.2 Scan conform

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-CONFORM-001 | Selezione ROI per conformazione allo scan | P0 |
| CAD-CONFORM-002 | Strength/max displacement controllabili | P0 |
| CAD-CONFORM-003 | Scan source e transform registrati | P0 |
| CAD-CONFORM-004 | Before/after metrics e operation version | P0 |
| CAD-CONFORM-005 | Advanced correspondence/ICP-assisted conform | P1 |

Baseline: US18.

---

# 16. Analisi quantitativa, QC e DFM

Normativa: `spec/09_analysis_qc_dfm.md`.

## 16.1 Metriche pressure P0

Quando disponibili dal sistema sorgente:

```text
PeakPressure
PressureTimeIntegral
ContactArea
ContactTime
MeanPressure con definizione esplicita
PeakForce / FTI quando validamente misurati
```

COP è P1; shear P1/P2 e solo se realmente misurato o chiaramente modellato come `PredictedOutcome` [REF-CAD-033..040].

## 16.2 Comparability state

Ogni confronto quantitativo deve poter risultare:

```text
VALID
VALID_WITH_WARNINGS
NOT_COMPARABLE
INSUFFICIENT_DATA
```

Motivi possibili: device, calibration, speed/task, footwear, step-count/protocol, ROI definition.

## 16.3 Geometric QC P0

```text
arbitrary section
height probe
ruler/distance
angle when applicable
thickness query
max/min height
minimum-thickness check
watertight/manufacturability state quando applicabile
```

Il limite EasyCAD ~0.8 mm resta evidenza di profilo EasyCAD, non costante universale. Il limite effettivo appartiene al manufacturing/material profile.

Baseline: US19, US20, US24; `[EC2-MANUAL-1.1, pp. 42–44, 52–53]`.

---

# 17. Indication / use-case profiles

Normativa: `spec/13_use_case_profiles.md`; acceptance `PROF-001..PROF-012`.

Initial P0 profiles:

```text
DIABETIC_REULCERATION_PREVENTION
MECHANICAL_METATARSALGIA
FLEXIBLE_FLATFOOT
PLANTAR_HEEL_PAIN
SPORT_PERFORMANCE
GENERIC_CUSTOM_ORTHOSIS
```

`IndicationProfile` è un **evidence-context layer versionato**.

Non è:

```text
diagnostic engine
automatic geometry generator
hidden rule mixer
```

Ogni target mantiene `profileId + evidenceRef + protocol`.

## 17.1 Non-transfer guards P0

- threshold diabetici non migrano automaticamente in metatarsalgia/flatfoot/heel pain/sport;
- pediatrico ≠ adulto;
- walking ≠ running;
- healthy runner effect ≠ trattamento clinico;
- pressure improvement ≠ pain/function improvement;
- injury prevention signal ≠ performance benefit.

## 17.2 Active diabetic ulcer guard

Il profilo di prevenzione/recidiva non deve essere presentato come pathway equivalente al trattamento di un'ulcera neuropatica plantare attiva. Applicare warning/pathway separato coerente con `GUIDE-IWGDF-2023`.

---

# 18. PROM, comfort, fit, satisfaction e adherence

Normativa: `spec/14_prom_comfort_adherence.md`; acceptance `PROM-001..PROM-020`.

Questi costrutti restano separati:

```text
PAIN
FUNCTION / ACTIVITY
FOOT-SPECIFIC HEALTH / QoL
COMFORT
FIT / USABILITY
SATISFACTION
ADHERENCE / WEAR EXPOSURE
```

Nessun `BiomechE Score` universale nascosto è ammesso in P0/P1.

## 18.1 PROMInstrumentDefinition P0

```text
instrumentId
canonicalName
version
language
culturalAdaptation
respondentType
validationContexts
domains
itemCount
recallPeriod
responseScale
scoreDirection
scoringAlgorithmVersion
MID/MCID/MDC/SEM rules
licensing/redistribution status
evidenceRefs
```

La scelta strumento segue construct + measurement properties + feasibility/fit-for-purpose [GUIDE-COSMIN; GUIDE-FDA-PRO-DEVICE-2022].

Candidate italiane già identificate, non selezionate globalmente:

```text
17-IFFI
FAAM-I/ADL
EFAS Score
```

[REF-CAD-084..086].

## 18.2 Adherence P0

Metodo e denominatore obbligatori:

```text
SELF_REPORT
TEMPERATURE_SENSOR
ACTIVITY_MONITOR
COMBINED_OBJECTIVE

TIME_OUT_OF_BED
WEIGHT_BEARING_TIME
STEPS
PRESCRIBED_SESSION
```

`hours/day`, `% weight-bearing time` e `% steps with device` non sono sinonimi [REF-CAD-068; REF-CAD-071; REF-CAD-091; REF-CAD-092].

Questionnaire text/scoring assets possono essere distribuiti solo dopo licensing review.

---

# 19. Manufacturing e physical artifact

Normativa: `spec/10_manufacturing.md`; acceptance `MAN-001..MAN-018`.

## 19.1 ManufacturingProfile P0

Deve essere versionato e specificare, quando applicabile:

```text
processType
machine/profile
material/feedstock/blank
build/stock orientation
layer/infill/lattice/process parameters
CAM/postprocessor/tooling
fixture
post-processing
nominal tolerances
minimum thickness rules
blocking QC requirements
```

## 19.2 ManufacturingRun / PhysicalOrthosis P0

```text
runId
sourceDesignRevision
manufacturingProfileVersion
materialLot/feedstock
machine identity
operator
timestamps
process deviations
postProcess history
artifact/part identity
QC state
```

## 19.3 AM

Quando usato, separare part definition, feedstock, final-part properties, inspection e acceptance. Questa impostazione è coerente con la struttura di ISO/ASTM 52901; non equivale a una dichiarazione automatica di conformità allo standard.

## 19.4 CNC

Versionare almeno:

```text
blank/material lot
machine profile
CAM version
postprocessor
tool/tooling
fixture/origin strategy
finishing
```

## 19.5 Export

P0:

```text
STL
project/package format
```

P1/P2 secondo manufacturing target:

```text
3MF
GCODE
CNC toolpath/package
other interoperable formats
```

Baseline EasyCAD2: `[EC2-MANUAL-1.1, pp. 44–50]`, US21.

`Export generated` non equivale a `PhysicalOrthosis accepted`.

---

# 20. Reporting e traceability

P0 report deve poter collegare:

```text
patient/case identifier
side
indication profile(s)
source acquisitions
registration/version
prescription features + dose
material regions/stack
DesignRevision
ManufacturingProfile/Run
QC status
ExportArtifact hash
PROM/outcomes quando presenti
wear/adherence context
bibliographic/evidence-linked presets quando usati
```

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-REP-001 | Report prescrittivo/design | P0 |
| CAD-REP-002 | Report manufacturing/QC | P0 |
| CAD-REP-003 | Report outcome pre/post | P1 |
| CAD-REP-004 | PDF/export umano leggibile | P0 |
| CAD-REP-005 | Machine-readable provenance package | P1 |

Baseline EasyCAD2: US23.

---

# 21. History, determinismo e audit

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-HIST-001 | Undo/redo | P0 |
| CAD-HIST-002 | Operation history persistente | P0 |
| CAD-HIST-003 | Algorithm version per operazione | P0 |
| CAD-HIST-004 | Stable IDs per oggetti semantici | P0 |
| CAD-HIST-005 | Hash asset/export dove pratico | P0 |
| CAD-HIST-006 | Replay/rebuild deterministico della revisione | P0 |
| CAD-HIST-007 | Diff semantico tra revisioni | P1 |
| CAD-HIST-008 | Audit log autore/timestamp/rationale | P0 |

Save/close non deve perdere modifiche confermate. Baseline EasyCAD2: toolbar/history e validation story finale.

---

# 22. BiomechE integration

P0 contract:

```text
external patient/case ID
quantitative pressure dataset
side
units
acquisition provenance
coordinate/registration metadata
ROI definitions/version
analysis/outcome metrics
```

P1:

```text
round-trip case links
pressure-guided targets
post-production outcome import
comparison dashboard
```

P2:

```text
continuous wearable pressure/adherence
advanced predicted outcomes
AI-assisted suggestion with explicit rationale/evidence
```

La specifica dettagliata sarà `spec/11_biomeche_integration.md`.

---

# 23. Functional P0 freeze matrix

P0 deve includere almeno:

| Area | P0 |
|---|---|
| Patient/case/revisions | sì |
| DX/SX + semantic mirror | sì |
| DIMA/template custom | sì |
| Pressure numeric import/registration/ROI | sì |
| Scan3D + landmarks/registration/provenance | sì |
| Scan2D/Image2D calibration | sì |
| Thickness/flatten | sì |
| Heel containment/relief/camber/mechanics | sì |
| Medial/lateral arch | sì |
| Rearfoot/forefoot wedges | sì |
| Corrective elements + metatarsal placement | sì |
| Relief/aperture + safety-ring outcome | sì |
| Material/stiffness regions | sì |
| Sculpt/smooth | sì |
| Scan conform | sì |
| Sections/ruler/height/thickness | sì |
| PeakPressure/PTI/ContactArea | sì, se disponibili dalla sorgente |
| Context-bound target/threshold model | sì |
| IndicationProfile | sì |
| PROM registry + measurement provenance | sì |
| Comfort/fit/satisfaction separate | sì |
| Adherence/wear exposure | sì |
| ManufacturingProfile/Run/PhysicalOrthosis | sì |
| DFM/min-thickness profile | sì |
| QC state distinct from export success | sì |
| STL/project package | sì |
| Report + revision/hash traceability | sì |
| Undo/history/replay | sì |
| Offline authoring | sì |

---

# 24. P1

- advanced template authoring;
- ICP and advanced registration;
- advanced custom-element control topology;
- evidence-linked clinical presets with inspectable provenance;
- adaptive/local geometry refinement if qualification requires it;
- curvature/geodesic utilities;
- COP analysis;
- 3MF/material-aware export;
- outcome comparison dashboard;
- machine-readable traceability package;
- advanced manufacturing/property QC;
- diff semantico delle revisioni;
- advanced regional/mechanical design.

---

# 25. P2 / R&D

- STEP/IGES/.3dm exact interoperability if later required;
- general B-Rep/NURBS authoring;
- generic CAD booleans/fillets/shells;
- multi-material/lattice optimization automatico;
- FEM/FEA;
- shear integration on qualified hardware;
- continuous wearable pressure/adherence;
- AI prescription/design suggestions;
- AI outcome prediction;
- automated pressure→material/lattice mapping;
- cloud collaboration.

Nessuna di queste capacità deve ridefinire retroattivamente il P0.

---

# 26. Acceptance hierarchy

La validazione futura deve essere kernel-independent e riutilizzare gli acceptance semantics già definiti:

```text
OFF-001..OFF-009
CE-001..CE-010
ARCH-001..ARCH-014
HEEL-001..HEEL-015
PROF-001..PROF-012
PROM-001..PROM-020
MAT-001..MAT-018
MAN-001..MAN-018
```

A questi si aggiungeranno test per:

```text
project/revision integrity
registration round-trip
laterality/mirror semantics
pressure comparability
history/replay
manufacturing traceability
report provenance
```

Ogni P0 deve avere almeno uno dei seguenti:

```text
deterministic invariant
numeric tolerance
schema invariant
round-trip test
workflow acceptance test
explicit safety guard
```

---

# 27. EasyCAD2 parity gate

Il nuovo prodotto non deve perdere intenzionalmente le capacità validate EasyCAD2 senza una decisione esplicita.

La parity record canonica resta:

`docs/validation/easycad2_geometry_parity.md`

Le 25 validation story EasyCAD2 devono continuare ad avere un implementation path nella specifica BiomechE-CAD.

Miglioramenti BiomechE-CAD rispetto alla baseline:

```text
semantic prescriptions
versioned operations
quantitative evidence chain
context-specific thresholds
outcome loop
PROM/adherence
material/process provenance
physical-part QC
scientific bibliography
reproducible audit trail
```

---

# 28. Architettura — PARKED

Questa specifica non seleziona il foundation engine.

Candidati futuri già individuati:

```text
A) product-owned clinical layer + OpenSubdiv
B) product-owned clinical layer + openNURBS / ON_SubD
```

Il confronto avverrà **dopo** Project Schema e acceptance suite.

Non introdurre un secondo kernel per “completezza teorica”; una dipendenza deve risolvere un requisito nominato o un fixture fallito.

---

# 29. Documenti subordinati canonici

```text
docs/BIBLIOGRAPHY.md

docs/research/FUNCTIONAL_SCIENTIFIC_EVIDENCE_MATRIX.md
docs/research/FUNCTIONAL_EVIDENCE_BATCH_03_RELIEF_OFFLOADING.md
docs/research/FUNCTIONAL_EVIDENCE_BATCH_04_ARCH.md
docs/research/FUNCTIONAL_EVIDENCE_BATCH_05_HEEL.md
docs/research/FUNCTIONAL_EVIDENCE_BATCH_06_USE_CASE_PROFILES.md
docs/research/FUNCTIONAL_EVIDENCE_BATCH_07_PROM_COMFORT_ADHERENCE.md
docs/research/FUNCTIONAL_EVIDENCE_BATCH_08_MATERIAL_MANUFACTURING.md

docs/spec/06_corrective_elements.md
docs/spec/08_material_stiffness.md
docs/spec/09_analysis_qc_dfm.md
docs/spec/10_manufacturing.md
docs/spec/13_use_case_profiles.md
docs/spec/14_prom_comfort_adherence.md
```

Quando una sub-spec contiene maggiore dettaglio, la sub-spec governa la semantica del proprio dominio; questa v2 governa scope, priorità e integrazione globale.

---

# 30. Next freeze sequence

```text
DONE: FUNCTIONAL SPEC v2 consolidation
        ↓
NEXT: spec/02_project_schema.md v0
        ↓
NEXT: kernel-independent functional acceptance suite
        ↓
FREEZE: spec/01_coordinate_registration.md
        ↓
spec/11_biomeche_integration.md
spec/12_reporting_traceability.md
        ↓
competitor gap audit / production-profile qualification
        ↓
architecture shoot-out
```

Non riprendere la selezione OpenSubdiv vs ON_SubD prima di schema + acceptance suite + coordinate contract.
