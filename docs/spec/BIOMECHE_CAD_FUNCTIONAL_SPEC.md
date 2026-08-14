# BiomechE-CAD — Specifica funzionale unificata per CAD di plantari

**Stato:** baseline funzionale preliminare consolidata  
**Data:** 2026-08-14  
**Repository target:** `ww34ww34ww34/BiomechE-CAD`  
**Fonte d'ispirazione principale:** EasyCAD2 / Sensor Medica  
**Approccio documentale:** coerente con `ww34ww34ww34/BiomechE`: Markdown canonico, source provenance, requisiti testabili, handover dinamico, separazione tra evidenza, decisione ingegneristica e questioni aperte.

---

## 0. Scopo del documento

Questo documento definisce la prima **specifica funzionale unificata** di BiomechE-CAD, un CAD verticale per la progettazione di plantari/ortesi plantari personalizzate da integrare con l'ecosistema BiomechE.

La specifica prende **fortemente spunto da EasyCAD2**, utilizzando come fonti primarie:

- manuale EasyCAD2 1.1.x.x;
- piano di validazione EasyCAD2 1.4.x.x;
- rapporto finale di validazione EasyCAD2 1.4.x.x;
- documentazione pubblica EasyCAD2/easyCAD;
- la precedente ricerca feature-by-feature svolta per BiomechE-CAD;
- letteratura scientifica su foot orthoses, pressure offloading, 3D scanning, stiffness/posting e CAD/additive manufacturing.

L'obiettivo non è replicare l'implementazione interna di EasyCAD2, ma ricostruire e formalizzare un **set di capacità clinico-geometriche completo**, mantenendo i punti forti del workflow EasyCAD2 e migliorando:

1. riproducibilità;
2. versioning;
3. non-distruttività;
4. interoperabilità;
5. integrazione con BiomechE;
6. audit scientifico;
7. validabilità automatica;
8. apertura a stiffness/material maps, additive manufacturing e AI explainable.

---

# 1. Gerarchia delle fonti ed evidenza

## 1.1 Fonti primarie EasyCAD2

### EC2-MANUAL-1.1
**EasyCAD2 — Manuale d'uso, versione software 1.1.x.x, 13/01/2024.**  
Google Drive:  
https://drive.google.com/file/d/148X366g4e47cYOWtFWP-jeMqavSJqHTa/view

Il manuale descrive in dettaglio:

- database e impostazioni;
- navigazione;
- modalità destra/sinistra;
- DIMA;
- PRESSURE;
- SCAN3D;
- SCAN2D;
- MODIFICA;
- ELEMENTI;
- POST PROCESSING;
- CONTROLLO;
- PRODUCI;
- TOOLBAR;
- avvertimenti di spessore minimo;
- salvataggio e chiusura sicura.

### EC2-VAL-PLAN-1.4
**PdV0001 — Piano di validazione software EasyCAD2, versione 1, last update 15/01/2026.**  
Google Drive:  
https://drive.google.com/file/d/19Pdjn76a6sAEcnUTut2qL0qzvfkniD4v/view

Definisce 25 user story con passi e risultati attesi per EasyCAD2 1.4.x.x.

### EC2-VAL-REPORT-1.4
**RdT001 — Rapporto di Test di validazione software EasyCAD2 versione 1.4.x.x, 20/01/2026.**  
Google Drive:  
https://drive.google.com/file/d/1kbDKQd6qskQH1MyZ5O3Y-WYt5p_7qRlJ/view

Risultato dichiarato:

- 25 test pianificati;
- 25 eseguiti;
- 25 PASS;
- 0 FAIL;
- 0 BLOCKED.

## 1.2 Regola di precedenza

Il manuale 1.1.x.x è più dettagliato dal punto di vista UI/geometrico ma più vecchio.

Il piano/rapporto di validazione 1.4.x.x è più recente e viene usato per **promuovere a funzione confermata** capacità che nel precedente audit erano ancora considerate lineage o secondary.

Quando una funzione:

- è descritta nel manuale 1.1 → comportamento UI/geometrico confermato per 1.1;
- è testata nel piano/rapporto 1.4 → capacità funzionale confermata anche nella linea 1.4;
- è assente dal manuale ma presente nella validazione 1.4 → la capacità è considerata reale, ma i dettagli UI/algoritmici restano da verificare.

## 1.3 Provenance tag per BiomechE-CAD

Usare nei documenti futuri:

- `SOURCE / EASYCAD2-MANUAL`
- `SOURCE / EASYCAD2-VALIDATION`
- `SOURCE / EASYCAD-LEGACY`
- `SOURCE / LITERATURE`
- `SOURCE / MARKET`
- `ENGINEERING DECISION`
- `OPEN QUESTION`
- `R&D CANDIDATE`

Nessun comportamento osservato deve diventare automaticamente una regola di BiomechE-CAD senza una decisione esplicita.

---

# 2. Visione del prodotto

## 2.1 Il pattern EasyCAD2 da mantenere

EasyCAD2 è un **clinical CAD verticale**, non un modellatore 3D generico.

Il workflow principale è:

```text
Paziente / Progetto
    -> DIMA
    -> Caricamento esami
       -> Pressione
       -> Scan3D
       -> Scan2D
    -> MODIFICA
    -> ELEMENTI / MODIFICATORI
    -> POST PROCESSING
    -> CONTROLLO
    -> PRODUCI
    -> REPORT / EXPORT
```

Per BiomechE-CAD il workflow consigliato diventa:

```text
Patient / Case
    -> OrthosisProject [DX/SX]
    -> AcquisitionLayer[]
    -> Registration
    -> BaseTemplate
    -> ParametricOperation[]
    -> CorrectiveElement[]
    -> MaterialModifier[]
    -> SculptOperation[]
    -> Analysis + DFM/QC
    -> ManufacturingProfile
    -> ExportArtifact[]
    -> Clinical/Manufacturing Report
```

## 2.2 Principio architetturale principale

**ENGINEERING DECISION — proposta baseline**

Non utilizzare una catena di sole deformazioni distruttive della mesh.

Ogni intervento clinico/geometrico deve essere rappresentato, ove possibile, come operazione versionata:

```text
evidence / measurement
    -> prescription
    -> parametric geometry operation
    -> evaluated mesh
    -> manufacturing result
```

Una `ParametricOperation` dovrebbe poter registrare:

```text
operation_id
operation_type
side
anatomical_region
parameters + units
mask / ROI
source_dataset_id
clinical_rationale
author
timestamp
algorithm_version
before_metrics
after_metrics
enabled/disabled
```

Questo consente:

- undo/redo robusto;
- editing successivo;
- confronto fra versioni;
- regression test;
- audit;
- report prescrittivo;
- AI explainable;
- riproduzione deterministica.

---

# 3. Modello dati funzionale

## CAD-DATA-001 — Patient

Il CAD deve poter associare i progetti a un soggetto.

Campi minimi:

```text
patient_id
external_patient_id?
name?
surname?
sex?
birth_date?
anthropometrics?
notes?
```

**Nota architetturale:** come in BiomechE, il core numerico non deve diventare il patient repository. La gestione anagrafica appartiene all'applicazione CAD/integration layer.

## CAD-DATA-002 — Case / Prescription

Un paziente può avere più casi/prescrizioni nel tempo.

```text
case_id
patient_id
date
clinician/operator
indication?
shoe/use_case?
clinical_notes
source_exam_ids[]
```

## CAD-DATA-003 — OrthosisProject

```text
project_id
case_id
left_project?
right_project?
template_id
project_schema_version
created_at
updated_at
author
status
```

## CAD-DATA-004 — AcquisitionLayer

Tipi iniziali:

```text
PRESSURE
SCAN_3D
SCAN_2D
IMAGE_2D
REFERENCE_MESH
BIOMECHE_RESULT
```

Metadati obbligatori:

```text
source
device/model
timestamp
side
units
coordinate_system
registration_transform
original_file_hash
processing_history
quality
```

Per scansioni 3D aggiungere quando disponibili:

```text
declared_accuracy
resolution
weight_bearing_condition
landmarks
mesh_quality
```

## CAD-DATA-005 — MaterialRegion / MaterialModifier

Deve essere possibile rappresentare regioni di proprietà meccanica differenziata indipendentemente dalla geometria esterna.

```text
modifier_id
region
material_id?
stiffness_class?
density_class?
print_profile?
transition_rule?
```

## CAD-DATA-006 — ExportArtifact

Ogni export deve registrare:

```text
artifact_id
format
side
source_project_revision
generated_at
manufacturing_profile
validation_status
hash
```

---

# 4. Database, progetti e impostazioni

## Requisiti

| ID | Requisito BiomechE-CAD | Priorità | Evidenza EasyCAD2 | Acceptance criteria |
|---|---|---:|---|---|
| CAD-DB-001 | Creare un nuovo paziente | P0 | Manuale pp. 7-9; US2 | Il record persiste e può essere riaperto |
| CAD-DB-002 | Modificare paziente | P0 | Manuale; US3 | Le modifiche sono persistenti |
| CAD-DB-003 | Eliminare paziente con conferma | P0 | Manuale; US3 | Nessuna cancellazione involontaria |
| CAD-DB-004 | Ricerca paziente | P0 | Manuale p. 9; US3 | Ricerca reattiva su campi configurati |
| CAD-DB-005 | Ordinamento alfabetico/data | P1 | Manuale p. 9 | Ordinamento deterministico |
| CAD-DB-006 | Visualizzare storico progetti | P0 | Manuale p. 9 | Tutte le revisioni/casi recuperabili |
| CAD-DB-007 | Import/export scheda paziente | P1 | Manuale p. 8 | Round-trip documentato |
| CAD-DB-008 | Collegamento a ID paziente esterno | P0 | Derivato da integrazione BiomechE | Non duplicare anagrafiche se integrate |
| CAD-DB-009 | Dati antropometrici | P1 | Manuale p. 9 | Campi versionati e unit-aware |
| CAD-DB-010 | Note cliniche e prescrittive | P0 | Report US23 | Persistono per progetto/revisione |
| CAD-SET-001 | Gestione licenza | P2/prodotto | Manuale pp. 5,10; US1 | Stato licenza verificabile |
| CAD-SET-002 | Lingua UI | P1 | Manuale p. 10; US4 | Cambio lingua senza perdita dati |
| CAD-SET-003 | Unità metriche/imperiali | P0 | Manuale p. 12; US4 | Conversione esplicita e reversibile |
| CAD-SET-004 | Taglia EU/US | P1 | US4 | Mapping separato dalla lunghezza reale |
| CAD-SET-005 | Configurazione stampante 3D | P1 | Manuale p. 10; US5 | Profilo persistente |
| CAD-SET-006 | Configurazione CNC | P1 | Manuale p. 11; US5 | Profilo macchina persistente |
| CAD-SET-007 | Configurazione sorgenti/archivi esterni | P1 | Manuale FreeStep p. 11 | Mapping configurabile |
| CAD-SET-008 | Offline-first | P0 | Manuale: internet non necessario per uso normale | CAD utilizzabile senza cloud obbligatorio |

---

# 5. Navigazione, viewport e interazione

EasyCAD2 documenta:

- rotazione 3D con tasto destro;
- zoom con rotella;
- pan con tasto centrale;
- zoom/pan 2D;
- multi-selezione con SHIFT;
- viste top/bottom/left/right/front/back/default;
- trasparenza;
- grid;
- height-based visualization;
- show/hide pressure;
- show/hide Scan3D;
- show/hide Scan2D;
- misura altezza sotto mouse;
- righello due punti.

## Requisiti

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-VIEW-001 | Orbit 3D fluido | P0 |
| CAD-VIEW-002 | Pan 2D/3D | P0 |
| CAD-VIEW-003 | Zoom continuo | P0 |
| CAD-VIEW-004 | Viste ortogonali predefinite | P0 |
| CAD-VIEW-005 | Vista default/isometrica | P0 |
| CAD-VIEW-006 | Griglia metrica | P0 |
| CAD-VIEW-007 | Trasparenza per layer | P0 |
| CAD-VIEW-008 | Toggle Pressure/Scan3D/Scan2D | P0 |
| CAD-VIEW-009 | Height map / colore per quota | P0 |
| CAD-VIEW-010 | Quota Z sotto cursore | P0 |
| CAD-VIEW-011 | Righello 3D/2D fra due punti | P0 |
| CAD-VIEW-012 | Multi-select | P0 |
| CAD-VIEW-013 | Selezione visiva coerente di vertici/elementi/ROI | P0 |
| CAD-VIEW-014 | Frame rate interattivo su mesh operative | P0 |
| CAD-VIEW-015 | Overlay delle coordinate/assi quando utile | P1 |

**Acceptance baseline:** ogni operazione di camera non deve alterare la geometria; picking e misura devono restare stabili al variare della vista.

---

# 6. Laterality e workflow bilaterale

EasyCAD2 consente:

- passaggio DX/SX;
- creazione da zero del controlaterale;
- specchio del progetto esistente;
- gestione distinta del lato in varie modalità;
- validazione US6 conferma DX -> SX.

## Requisiti

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-LR-001 | Progetto esplicitamente Left/Right | P0 |
| CAD-LR-002 | Switch rapido DX/SX | P0 |
| CAD-LR-003 | Creazione controlaterale vuota | P0 |
| CAD-LR-004 | Mirror del plantare completo | P0 |
| CAD-LR-005 | Mirror selettivo di template/operazioni | P1 |
| CAD-LR-006 | Dopo il mirror, i due lati diventano editabili indipendentemente | P0 |
| CAD-LR-007 | Trasformazione anatomica corretta di medial/lateral e wedge semantics | P0 |

L'ultimo requisito è un miglioramento fondamentale: il mirror non deve limitarsi a `x -> -x`, ma deve mantenere correttamente la semantica anatomica.

---

# 7. DIMA / Base Template

EasyCAD2 parte sempre dalla DIMA.

## 7.1 Template confermati

Manuale 1.1 e US7 confermano:

- SPORT;
- SANDALO;
- CLASSIC;
- COMFORT;
- DONNA.

EasyCAD2 consente inoltre:

- salvataggio del template corrente;
- caricamento template personalizzato;
- DIMA AVANZATA;
- shoe size;
- lunghezza L in mm;
- larghezza W in mm;
- lock/unlock proporzioni;
- modifica di vertici del contorno;
- riferimenti a lunghezza totale, larghezza metatarsale e larghezza tallone.

## 7.2 DIMA AVANZATA

Il manuale descrive una combinazione pesata di caratteristiche:

```text
SPORT
SANDALO
CLASSIC
COMFORT
DONNA
```

tramite slider di intensità.

Per BiomechE-CAD questo comportamento può essere mantenuto come **template morphing**, ma la geometria deve essere descritta in modo deterministico e versionato.

## Requisiti

| ID | Requisito | Pri. | Acceptance |
|---|---|---:|---|
| CAD-DIMA-001 | Libreria di template | P0 | Template selezionabile e versionato |
| CAD-DIMA-002 | Template per uso/calzatura | P0 | Almeno profili equivalenti a Sport/Sandal/Classic/Comfort/Women |
| CAD-DIMA-003 | Salvataggio template custom | P1 | Preset riutilizzabile |
| CAD-DIMA-004 | Import template custom | P1 | Formato documentato |
| CAD-DIMA-005 | Edit boundary tramite control point | P0 | Outline continuo senza self-intersection |
| CAD-DIMA-006 | Lunghezza mm | P0 | Quota reale verificabile |
| CAD-DIMA-007 | Larghezza mm | P0 | Quota reale verificabile |
| CAD-DIMA-008 | Shoe size come controllo di convenienza | P1 | Non sostituisce le quote metriche |
| CAD-DIMA-009 | Lock aspect/proportion | P0 | L/W scalano coerentemente |
| CAD-DIMA-010 | Unlock L/W indipendenti | P0 | Modifica indipendente |
| CAD-DIMA-011 | Riferimento metatarsal width | P1 | Visibile/misurabile |
| CAD-DIMA-012 | Riferimento heel width | P1 | Visibile/misurabile |
| CAD-DIMA-013 | Template blend/morph | P1 | Risultato deterministico e salvabile |
| CAD-DIMA-014 | Validazione outline | P0 | Nessun bordo degenerato/self-crossing |
| CAD-DIMA-015 | Generazione template assistita da scan/foot outline | P1 | Sempre confermabile dall'operatore |

---

# 8. Acquisizioni cliniche e registrazione

## 8.1 Pressure

EasyCAD2 1.1:

- importa `.bpe`;
- importa `.csv`;
- X [mm];
- Y [mm];
- rotation [deg];
- scale;
- reset trasformazioni;
- show/hide;
- `GENERATE` crea un modello 3D usando la matrice delle pressioni.

US8 1.4 conferma caricamento `.csv/.bpe` e allineamento.

### Requisiti Pressure

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-ACQ-P-001 | Import pressure dataset nativo BiomechE | P0 |
| CAD-ACQ-P-002 | Import CSV | P0 |
| CAD-ACQ-P-003 | Adapter BPE se necessario per legacy | P1 |
| CAD-ACQ-P-004 | Translation X/Y in mm | P0 |
| CAD-ACQ-P-005 | Rotation in deg | P0 |
| CAD-ACQ-P-006 | Scale esplicita solo se necessaria | P0 |
| CAD-ACQ-P-007 | Reset registration | P0 |
| CAD-ACQ-P-008 | Show/hide + opacity | P0 |
| CAD-ACQ-P-009 | Pressure color map quantitativa | P0 |
| CAD-ACQ-P-010 | ROI pressure statistics | P0 |
| CAD-ACQ-P-011 | Pressure-to-shape suggestion/generation | P1 |
| CAD-ACQ-P-012 | Nessun algoritmo pressure-to-shape opaco | P0 architetturale |
| CAD-ACQ-P-013 | Provenance del pressure dataset | P0 |
| CAD-ACQ-P-014 | Preservare coordinate metriche BiomechE | P0 |

### Miglioramento rispetto al solo overlay

La pressure map deve restare **dato numerico metrico**, non diventare una texture raster non tracciabile.

Il CAD deve poter conoscere almeno:

```text
pressure[kPa]
position[mm]
foot side
ROI
source exam
aggregation method
quality/provenance
```

---

## 8.2 Scan3D

EasyCAD2 1.1:

- importa `.stl`;
- landmark heel;
- landmark first metatarsal;
- landmark fifth metatarsal;
- `Align`;
- dopo l'allineamento permette di tagliare/rimuovere la porzione superiore della scan.

US9 conferma l'allineamento spaziale.

### Requisiti Scan3D

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-ACQ-3D-001 | Import STL | P0 |
| CAD-ACQ-3D-002 | Import OBJ | P1 |
| CAD-ACQ-3D-003 | Landmark heel/1st/5th | P0 |
| CAD-ACQ-3D-004 | Auto-landmark assistito con conferma | P1 |
| CAD-ACQ-3D-005 | Rigid registration scan-template | P0 |
| CAD-ACQ-3D-006 | Manual fine registration | P0 |
| CAD-ACQ-3D-007 | Crop/trim scan | P0 |
| CAD-ACQ-3D-008 | Mesh quality checks | P0 |
| CAD-ACQ-3D-009 | Unit detection/confirmation | P0 |
| CAD-ACQ-3D-010 | Scan provenance | P0 |
| CAD-ACQ-3D-011 | Visual comparison scan/orthosis | P0 |
| CAD-ACQ-3D-012 | Deform orthosis toward scan in controlled ROI | P0/P1 |

---

## 8.3 Scan2D / Image2D

US9 1.4 chiarisce che l'immagine 2D viene calibrata inserendo L e W.

### Requisiti

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-ACQ-2D-001 | Import Scan2D/image | P0 |
| CAD-ACQ-2D-002 | Calibrazione metrica L/W | P0 |
| CAD-ACQ-2D-003 | Translation/rotation/scale | P0 |
| CAD-ACQ-2D-004 | Foot outline assistito | P1 |
| CAD-ACQ-2D-005 | Provenance immagine | P0 |

---

# 9. MODIFICA — geometria parametrica principale

Questa è una delle sezioni più importanti da prendere da EasyCAD2.

## 9.1 Spessore globale

EasyCAD2:

- selettore in mm;
- default documentato: 2 mm;
- `Appiattisci` porta la soletta a spessore costante;
- US10 conferma il comportamento.

### Requisiti

- `CAD-EDIT-001` — global thickness in mm — P0.
- `CAD-EDIT-002` — flatten a thickness target — P0.
- `CAD-EDIT-003` — thickness come parametro, non semplice risultato mesh — P0.
- `CAD-EDIT-004` — visual thickness map — P0.
- `CAD-EDIT-005` — min thickness evaluation — P0.

---

## 9.2 Editing vertici

EasyCAD2:

- mostra vertici selezionati sulla superficie superiore;
- spostamento X/Y/Z;
- modalità `Avanzato` rende modificabili tutti i vertici;
- `Reset`;
- `Tre quarti`;
- `Trasformazione avanzata` permette XYZ anche sui bordi.

### Requisiti

- `CAD-EDIT-010` — editing locale control points/mesh — P0.
- `CAD-EDIT-011` — vincoli per evitare mesh degenerata — P0.
- `CAD-EDIT-012` — advanced mode esplicita — P1.
- `CAD-EDIT-013` — reset scoped alla modalità/operazione — P0.
- `CAD-EDIT-014` — boundary XYZ editing — P1.
- `CAD-EDIT-015` — selezione multipla e trasformazioni coordinate — P0.

**Miglioramento:** preferire cage/control surface/parametric layer rispetto a modifiche dirette non tracciabili di milioni di triangoli.

---

## 9.3 Retropiede / heel

Il manuale EasyCAD2 descrive:

```text
Altezza avvolgenza
Curvatura avvolgenza
Lunghezza/Inizio cambratura [%]
Raccordo/Fine cambratura [%]
Altezza cambratura
```

US11 conferma generazione di altezza e cambratura senza distorsioni.

### Requisito parametrico

`CAD-EDIT-HEEL-001` — `HeelOperation`

Parametri minimi:

```text
wrap_height_mm
wrap_curvature
camber_start_pct
camber_end_or_blend_pct
camber_height_mm
transition_profile
```

Requisiti aggiuntivi:

- controllo simmetria/asimmetria;
- preview in sezione;
- no fold/self-intersection;
- misure numeriche riproducibili.

---

## 9.4 Arco mediale

Il manuale mostra per l'arco mediale:

```text
Altezza arco [mm]
Rotondità dell'arco
Profondità dell'arco [%]
Curvatura dell'arco
Inizio arco [%]
Centro dell'arco [%]
Fine arco [%]
```

US12 conferma parametri percentuali inizio/centro/fine.

### Requisito

`CAD-EDIT-ARCH-M-001` — `MedialArchOperation`

```text
height_mm
roundness
depth_pct
curvature
start_pct
center_pct
end_pct
blend/transition
```

### Vincoli

```text
0 <= start < center < end <= 100
height bounded by configured safety profile
continuous surface
no local negative thickness below manufacturing minimum
```

---

## 9.5 Arco laterale

Il manuale documenta:

```text
Altezza arco [mm]
Profondità [%]
Curvatura
Inizio [%]
Centro [%]
Fine [%]
```

### Requisito

`CAD-EDIT-ARCH-L-001` — `LateralArchOperation`

Stessa filosofia del medial arch, con parametri indipendenti.

---

# 10. Cunei / posting

EasyCAD2 1.1 e US13 1.4 confermano:

- applicazione `Completo` o `Parziale`;
- cuneo posteriore in gradi;
- cuneo avampiede in gradi;
- lunghezza di applicazione;
- validazione dell'inclinazione calcolata.

## Requisiti

### CAD-EDIT-WEDGE-001 — Rearfoot wedge
P0.

```text
angle_deg
application = FULL | PARTIAL
medial_lateral_semantics
length_pct_or_mm
transition_length
reference_axis
```

### CAD-EDIT-WEDGE-002 — Forefoot wedge
P0.

Stesso modello con regione anteriore.

### CAD-EDIT-WEDGE-003 — Unit-safe prescription
P0.

Il valore in gradi deve essere preservato anche dopo la generazione mesh.

### CAD-EDIT-WEDGE-004 — mm/deg helper
P1.

Consentire la conversione fra elevazione lineare e angolo soltanto quando è definita la distanza di riferimento.

### CAD-EDIT-WEDGE-005 — mirror semantic correctness
P0.

Medial/lateral devono trasformarsi correttamente fra DX/SX.

### CAD-EDIT-WEDGE-006 — misura angolo risultante
P0.

Lo strumento di controllo deve verificare la geometria prodotta.

---

# 11. Smooth nella fase MODIFICA

EasyCAD2 permette levigatura:

- bordo;
- superficie;
- entrambi.

## Requisiti

- `CAD-EDIT-SMOOTH-001` — smooth border — P0/P1.
- `CAD-EDIT-SMOOTH-002` — smooth surface — P0.
- `CAD-EDIT-SMOOTH-003` — preview + intensità — P0.
- `CAD-EDIT-SMOOTH-004` — preservare, quando richiesto, quote/feature protette — P1.

---

# 12. ELEMENTI — libreria correttori

La documentazione EasyCAD2 conferma una libreria organizzata per:

```text
RETROPIEDE
MESOPIEDE
AVAMPIEDE
PROPRIO
PERSONALIZZATO
```

Il manuale e gli screenshot mostrano, fra gli altri:

- conca tallone;
- conca tallone + supporto volta mediale;
- cunei posteriori;
- tallonetta per spina calcaneare;
- tallonetta tre quarti;
- volta laterale;
- diverse varianti di volta mediale;
- barre metatarsali multiple;
- cuneo avampiede;
- cuneo quinto metatarso;
- gocce;
- elementi propriocettivi/stimoli.

La schermata `PARAMETRI STAMPA` mostra esplicitamente un elemento `BARRA_METATARSALE1`, confermando che il concetto di barra metatarsale è presente nel workflow.

## 12.1 Gestione elemento

EasyCAD2 consente:

- add;
- delete;
- show/hide;
- integrazione nella mesh;
- modalità `SOMMA`;
- modalità `INTERSEZIONE`;
- X/Y position;
- X/Y scale;
- Z scale;
- rotation;
- lock proportions;
- rotazione interattiva Z;
- traslazione interattiva X/Y.

## Requisiti

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-ELEM-001 | Libreria elementi versionata | P0 |
| CAD-ELEM-002 | Categorie anatomiche | P0 |
| CAD-ELEM-003 | Search/filter | P1 |
| CAD-ELEM-004 | Add/remove/show/hide | P0 |
| CAD-ELEM-005 | Position X/Y in mm | P0 |
| CAD-ELEM-006 | Rotation deg | P0 |
| CAD-ELEM-007 | Scale X/Y/Z | P0 |
| CAD-ELEM-008 | Lock aspect ratio | P1 |
| CAD-ELEM-009 | Boolean/additive integration modes | P0 |
| CAD-ELEM-010 | Preview prima del bake/evaluation | P0 |
| CAD-ELEM-011 | Parametri persistenti | P0 |
| CAD-ELEM-012 | Element rationale/clinical tag | P1 |
| CAD-ELEM-013 | Element metrics (height, area, volume) | P1 |

## 12.2 Libreria minima raccomandata

P0/P1:

```text
heel cup / heel contour
heel relief / heel spur accommodation
medial arch support
lateral arch support
rearfoot wedge/post
forefoot wedge/post
metatarsal bar
metatarsal dome/pad
5th metatarsal support/offload
local drop/raise
local depression/offload
three-quarter heel/orthosis element
```

Specialistico/P2:

```text
proprioceptive elements
neuromuscular stimulation shapes
sport-specific elements
condition-specific protocols
```

---

# 13. Elemento Custom

US15 1.4 conferma:

- selezione elemento;
- `MODIFICA`;
- spostamento vertici X/Y/Z;
- salvataggio `ELEMENTO PRESET CUSTOM`;
- riuso futuro.

## Requisiti

- `CAD-ELEM-CUSTOM-001` — edit geometry of element — P1.
- `CAD-ELEM-CUSTOM-002` — save custom preset — P1.
- `CAD-ELEM-CUSTOM-003` — version custom preset — P1.
- `CAD-ELEM-CUSTOM-004` — metadata: name, author, date, category, indication — P1.
- `CAD-ELEM-CUSTOM-005` — avoid destructive overwrite of factory preset — P0.

---

# 14. Modificatori di rigidità / densità

Questa funzione era solo ipotizzata nel primo audit; il piano e rapporto di validazione 1.4 la confermano.

US16:

- crea area tramite Ctrl+Shift+click;
- chiude area;
- assegna nome;
- la regione può variare la rigidità in produzione.

US22:

- durezza complessiva plantare;
- durezza per ogni singolo elemento;
- 5 livelli da extra morbido a extra duro;
- stampa differenziata.

## Requisiti

### CAD-MAT-001 — MaterialModifier region
P0/P1.

Creare ROI chiusa sopra il plantare.

### CAD-MAT-002 — stiffness class
P1.

Almeno schema astratto:

```text
EXTRA_SOFT
SOFT
MEDIUM
HARD
EXTRA_HARD
```

### CAD-MAT-003 — separate geometry/material semantics
P0 architetturale.

La regione di materiale non deve richiedere una deformazione geometrica.

### CAD-MAT-004 — per-element material override
P1.

### CAD-MAT-005 — transition rule
P1/P2.

Gestire transizione fra proprietà meccaniche.

### CAD-MAT-006 — physical property profile
P2.

In futuro associare i livelli qualitativi a proprietà misurate:

```text
Shore hardness
effective modulus
density
infill/lattice parameters
material
```

### CAD-MAT-007 — 3MF/multi-material capable data model
P1.

Anche se l'export iniziale è STL, il modello interno non deve essere limitato a una sola superficie senza materiali.

---

# 15. POST PROCESSING

EasyCAD2 divide il post-processing in:

1. `DEFORMAZIONE GLOBALE`;
2. strumenti locali (`SCOLPIRE`, `Smooth`, `Global Smooth`, `Deforma`).

## 15.1 Deformazione globale

EasyCAD2:

- selezione con parallelepipedo/rettangolo;
- Position X/Y;
- Width [%];
- Length [%];
- intensità;
- target: PRESSURE, SCAN3D o SCAN2D.

US18 conferma la deformazione rispetto all'esame.

### Requisiti

- `CAD-POST-GLOBAL-001` — ROI rettangolare/cage — P0.
- `CAD-POST-GLOBAL-002` — position X/Y — P0.
- `CAD-POST-GLOBAL-003` — width/length — P0.
- `CAD-POST-GLOBAL-004` — intensity — P0.
- `CAD-POST-GLOBAL-005` — source acquisition explicitly selected — P0.
- `CAD-POST-GLOBAL-006` — preview before apply — P0.
- `CAD-POST-GLOBAL-007` — non-destructive operation record — P0.
- `CAD-POST-GLOBAL-008` — residual/deviation visualization from source scan — P1.

---

## 15.2 Sculpt

EasyCAD2:

```text
Raggio
Forza
incremento/decremento altezza
```

US17 conferma deformazione locale.

### Requisiti

- `CAD-SCULPT-001` — raise/lower brush — P0.
- `CAD-SCULPT-002` — radius — P0.
- `CAD-SCULPT-003` — strength — P0.
- `CAD-SCULPT-004` — falloff profile — P1.
- `CAD-SCULPT-005` — brush stroke history — P0.
- `CAD-SCULPT-006` — symmetry optional — P1.
- `CAD-SCULPT-007` — numerical delta visualization — P1.

---

## 15.3 Smooth / Global Smooth

EasyCAD2:

- local Smooth;
- radius;
- force;
- include borders;
- Global Smooth;
- global intensity;
- include borders.

### Requisiti

- `CAD-SCULPT-SMOOTH-001` — local smooth — P0.
- `CAD-SCULPT-SMOOTH-002` — radius/strength — P0.
- `CAD-SCULPT-SMOOTH-003` — include/exclude boundary — P0.
- `CAD-SCULPT-SMOOTH-004` — global smooth — P1.
- `CAD-SCULPT-SMOOTH-005` — preserve thickness constraints — P0.

---

## 15.4 Deforma area chiusa

EasyCAD2:

- selection `Mano Libera` o `Cerchio`;
- punti tramite Ctrl+Shift+click;
- area chiusa;
- `Cambia altezza`;
- `Smooth` per transizione più ripida o graduale.

### Requisiti

- `CAD-DEFORM-ROI-001` — freehand closed ROI — P0.
- `CAD-DEFORM-ROI-002` — circle/ellipse ROI — P0.
- `CAD-DEFORM-ROI-003` — numerical height delta — P0.
- `CAD-DEFORM-ROI-004` — transition width/smoothness — P0.
- `CAD-DEFORM-ROI-005` — subtractive depression/offload — P0.
- `CAD-DEFORM-ROI-006` — additive raise/support — P0.
- `CAD-DEFORM-ROI-007` — save ROI as reusable mask — P1.

Questa sezione copre il requisito precedente relativo a depressioni nelle aree di iperpressione.

---

# 16. CONTROLLO / ANALYSIS / QC

EasyCAD2 offre:

- sezione trasversale;
- piano di sezione inclinabile;
- contorno superiore/inferiore;
- misure in tempo reale;
- `SMOOTH BORDO TALLONE`;
- fissa altezza minima avampiede;
- fissa altezza minima tallone;
- fissa arco mediale;
- fissa arco laterale;
- fissa altezza massima progetto;
- height-based visualization;
- height under mouse;
- ruler;
- warning di spessore minimo.

## Requisiti

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-QC-001 | Cross-section arbitraria | P0 |
| CAD-QC-002 | Cross-section inclinabile/ruotabile | P0 |
| CAD-QC-003 | Upper/lower surface profile | P0 |
| CAD-QC-004 | Thickness lungo la sezione | P0 |
| CAD-QC-005 | Min thickness globale/localizzato | P0 |
| CAD-QC-006 | Height map | P0 |
| CAD-QC-007 | Local height probe | P0 |
| CAD-QC-008 | Distance ruler | P0 |
| CAD-QC-009 | Wedge angle measure | P0 |
| CAD-QC-010 | Arch height measure | P0 |
| CAD-QC-011 | Heel/forefoot min height controls | P1 |
| CAD-QC-012 | Max project height | P1 |
| CAD-QC-013 | Heel border smooth utility | P1 |
| CAD-QC-014 | Mesh manifold validation | P0 |
| CAD-QC-015 | Self-intersection detection | P0 |
| CAD-QC-016 | Non-manifold edge detection | P0 |
| CAD-QC-017 | Degenerate triangle check | P0 |
| CAD-QC-018 | Unit/orientation sanity check | P0 |

---

# 17. Avviso spessore minimo e DFM auto-fix

Manuale:

- se esistono zone < **0,8 mm** compare un alert;
- l'utente può premere `FISSA`;
- il software aumenta automaticamente lo spessore per rientrare nel limite.

US24 1.4 verifica alert a 0,7 mm e auto-fix.

## Requisiti BiomechE-CAD

### CAD-DFM-001 — Minimum thickness profile
P0.

**Non hardcodare universalmente 0,8 mm.**

Il valore deve dipendere da:

```text
manufacturing_process
material
printer/CNC profile
closure mode
quality profile
```

0,8 mm può essere un preset compatibile EasyCAD2, non una legge universale.

### CAD-DFM-002 — Live warning
P0.

### CAD-DFM-003 — Localize violations
P0.

Mostrare la mappa delle aree problematiche.

### CAD-DFM-004 — Auto-fix preview
P0.

Prima di alterare la geometria mostrare cosa cambierà.

### CAD-DFM-005 — Fix operation in history
P0.

### CAD-DFM-006 — DFM rule provenance
P1.

Registrare quale profilo/materiale ha imposto il limite.

---

# 18. PRODUCI / manufacturing

## 18.1 Formati

EasyCAD2:

- STL;
- GCODE;
- ZIP progetto per condivisione;
- invio diretto a stampante 3D.

## Requisiti

- `CAD-EXP-001` — STL — P0.
- `CAD-EXP-002` — project package ZIP — P0.
- `CAD-EXP-003` — GCODE backend/profile — P1.
- `CAD-EXP-004` — 3MF — P1.
- `CAD-EXP-005` — OBJ — P1.
- `CAD-EXP-006` — eventuale STEP/BREP se il kernel lo rende sensato — P2.
- `CAD-EXP-007` — export validation report — P0.
- `CAD-EXP-008` — hash + project revision provenance — P0.

---

## 18.2 Tipologia di chiusura

EasyCAD2 documenta tre modalità.

### Bridge

- superficie/spessore di supporto;
- bordi raccordati;
- smussatura.

### Dritto

- bottom surface piana;
- pareti laterali perpendicolari;
- spessore minimo;
- smussatura;
- compatibile anche con fresatura.

### Obliquo

- bottom surface piana;
- bordi inclinati;
- controllo dell'inclinazione;
- spessore.

### Chiusura avanzata

Ibrido Bridge/Obliquo con:

- inizio supporto;
- fine supporto;
- larghezza supporto.

## Requisiti

- `CAD-MFG-CLOSE-001` — Bridge — P0/P1.
- `CAD-MFG-CLOSE-002` — Straight — P0.
- `CAD-MFG-CLOSE-003` — Beveled/Oblique — P0/P1.
- `CAD-MFG-CLOSE-004` — hybrid support — P1.
- `CAD-MFG-CLOSE-005` — thickness parameter — P0.
- `CAD-MFG-CLOSE-006` — bevel/smoothing parameter — P1.
- `CAD-MFG-CLOSE-007` — DFM preview cross-section — P0.

---

## 18.3 Testo / engraving

EasyCAD2 permette testo in `Slice3D`.

### Requisiti

- `CAD-MFG-TEXT-001` — text engraving/emboss — P1.
- `CAD-MFG-TEXT-002` — patient/project identifiers as optional tokens — P1.
- `CAD-MFG-TEXT-003` — privacy-safe default — P0.
- `CAD-MFG-TEXT-004` — placement/size/depth validation — P1.

---

## 18.4 Materiale / Panetto

Il manuale consente di selezionare materiale personalizzato, con esempio `Cover`.

### Requisiti

- `CAD-MFG-MAT-001` — material library — P1.
- `CAD-MFG-MAT-002` — properties metadata — P1.
- `CAD-MFG-MAT-003` — CNC stock/block profile — P1.
- `CAD-MFG-MAT-004` — top-cover metadata separato dalla shell — P1.
- `CAD-MFG-MAT-005` — material compatibility rules — P1.

---

## 18.5 CNC

EasyCAD2:

- configurazione macchina;
- selezione macchina al momento della produzione;
- GCODE.

### Requisiti

- `CAD-CAM-001` — machine profile abstraction — P1.
- `CAD-CAM-002` — stock/material dimensions — P1.
- `CAD-CAM-003` — tool profile — P1.
- `CAD-CAM-004` — toolpath backend separato dal CAD core — P1.
- `CAD-CAM-005` — post-processor versioning — P1.
- `CAD-CAM-006` — collision/reachability checks quando disponibili — P2.
- `CAD-CAM-007` — CNC output validation — P1.

Architetturalmente il GCODE non deve contaminare il modello CAD: deve essere generato da un modulo CAM/post-processor.

---

## 18.6 Stampa 3D

EasyCAD2:

- selezione printer;
- hardness globale;
- hardness per elemento;
- 5 livelli;
- Export;
- Produci diretto.

### Requisiti

- `CAD-PRINT-001` — printer profile — P1.
- `CAD-PRINT-002` — overall material/stiffness profile — P1.
- `CAD-PRINT-003` — per-region/per-element profile — P1.
- `CAD-PRINT-004` — export package — P0/P1.
- `CAD-PRINT-005` — direct print adapter optional — P2.
- `CAD-PRINT-006` — slicer integration optional — P1/P2.
- `CAD-PRINT-007` — generated artifact provenance — P0.

---

# 19. REPORT

Il piano/rapporto 1.4 aggiunge una funzione non sufficientemente descritta nel manuale 1.1:

US23:

- sezione REPORT;
- campo NOTE;
- generazione PDF;
- informazioni paziente;
- passi del progetto;
- note.

## Requisiti

### CAD-REP-001 — Project report
P0/P1.

Contenuti minimi:

```text
patient/case identifier
side
date/operator
input acquisitions
template
parametric corrections
elements
material modifiers
key dimensions
DFM status
manufacturing profile
notes
export artifact references
```

### CAD-REP-002 — Clinical prescription summary
P1.

### CAD-REP-003 — Manufacturing report
P1.

### CAD-REP-004 — Machine-readable JSON report
P0.

PDF non deve essere l'unica forma di tracciabilità.

### CAD-REP-005 — scientific/provenance block
P1.

Indicare algorithm/version per operazioni automatiche o assistite.

---

# 20. Toolbar, save, history e sicurezza del lavoro

EasyCAD2 documenta:

- Salva;
- Salva con nome;
- Importa Plantare;
- Visualizzazione storia azioni;
- undo/redo;
- chiusura con progetto non salvato;
- Salva su DB;
- Salva esterno `.raw`.

US25 conferma il salvataggio alla chiusura.

## Requisiti

| ID | Requisito | Pri. |
|---|---|---:|
| CAD-HIST-001 | Undo | P0 |
| CAD-HIST-002 | Redo | P0 |
| CAD-HIST-003 | Action history visibile | P0 |
| CAD-HIST-004 | Enable/disable operation | P0 |
| CAD-HIST-005 | Save | P0 |
| CAD-HIST-006 | Save As / duplicate project | P0 |
| CAD-HIST-007 | Autosave | P0 |
| CAD-HIST-008 | Dirty-state tracking | P0 |
| CAD-HIST-009 | Safe-close prompt | P0 |
| CAD-HIST-010 | Crash recovery | P0 |
| CAD-HIST-011 | Project schema version | P0 |
| CAD-HIST-012 | Migration pipeline | P0 |
| CAD-HIST-013 | Revision comparison | P1 |
| CAD-HIST-014 | Immutable export revision | P0 |

**Miglioramento decisivo rispetto a un semplice `.raw`:** il progetto deve avere un formato documentato/versionabile e migrazioni automatiche.

---

# 21. Integrazione con BiomechE

BiomechE adotta:

- unità fisiche canoniche;
- distinzione sensor/platform/exam coordinate spaces;
- pressure in kPa;
- position in mm;
- angle in deg;
- provenance della risoluzione/resampling;
- hardware-specific behavior fuori dal core;
- patient record fuori dal core numerico.

BiomechE-CAD deve rispettare questi confini.

## Requisiti

### CAD-BIO-001 — canonical units
P0.

```text
distance: mm
angle: deg
pressure: kPa
force: N
area: mm2
```

### CAD-BIO-002 — coordinate-system contract
P0.

Non assumere che row/column della pressure matrix coincidano con X/Y anatomici.

### CAD-BIO-003 — BiomechE exam reference
P0.

Il progetto CAD deve poter referenziare un risultato/esame BiomechE.

### CAD-BIO-004 — immutable source data
P0.

Il CAD non altera i dati quantitativi originali BiomechE; crea layer/derived representations.

### CAD-BIO-005 — region semantics
P0/P1.

Le ROI del CAD devono poter essere associate alle regioni anatomiche BiomechE senza assumere che una particolare segmentazione commerciale sia universale.

### CAD-BIO-006 — pre/post comparison
P1.

Supportare confronto fra:

```text
source exam
prescription/design
follow-up exam
```

### CAD-BIO-007 — pressure-based design helper
P1.

Esempio:

```text
high-pressure ROI
 -> suggest local offload
 -> operator accepts/modifies
 -> CAD records rationale
```

### CAD-BIO-008 — no opaque clinical AI
P0 principle.

Ogni suggerimento automatico deve esporre dati di origine e parametri.

---

# 22. Requisiti scientifici derivati dalla ricerca precedente

## SCI-01 — Posting dose-response

Telfer et al. hanno studiato ortesi personalizzate variando il rearfoot post in incrementi di 2°, osservando una risposta biomeccanica dose-response.

**Conseguenza CAD:**

- wedge in gradi;
- regione esplicita;
- asse esplicito;
- valore prescrittivo preservato;
- confronto quantitativo tra design.

Reference:  
Telfer S, Abbott M, Steultjens MPM, Woodburn J.  
*Dose-response effects of customised foot orthoses on lower limb kinematics and kinetics in pronated foot type.*  
J Biomech. 2013;46(9):1489-1495.  
PMID 23631857. DOI 10.1016/j.jbiomech.2013.03.036.

---

## SCI-02 — 3D scanning provenance

La systematic review di Farhan et al. evidenzia eterogeneità di metodi, carico, scanner e accuratezza.

**Conseguenza CAD:**

lo scan deve conservare provenance e condition metadata.

Reference:  
Farhan M, Wang JZ, Bray P, Burns J, Cheng TL.  
*Comparison of 3D scanning versus traditional methods of capturing foot and ankle morphology for the fabrication of orthoses: a systematic review.*  
J Foot Ankle Res. 2021;14(1):2.  
PMID 33413570. DOI 10.1186/s13047-020-00442-8.

---

## SCI-03 — Pressure-driven offloading

La letteratura su customized accommodative insoles mostra che pressure-driven design può ridurre carichi in regioni target.

Reference:  
Muir BC et al.  
*Evaluation of novel plantar pressure-based 3-dimensional printed accommodative insoles — A feasibility study.*  
Clin Biomech. 2022;98:105739.  
PMID 35987171. DOI 10.1016/j.clinbiomech.2022.105739.

**Conseguenza CAD:** pressure ROI, offload target e outcome devono poter essere quantitativi.

---

## SCI-04 — Stiffness

Cherni et al. mostrano che la stiffness delle foot orthoses 3D printed è biomeccanicamente rilevante.

Reference:  
Cherni Y et al.  
*Effect of 3D printed foot orthoses stiffness on muscle activity and plantar pressures in individuals with flexible flatfeet.*  
Clin Biomech. 2022;92:105553.  
PMID 34973589. DOI 10.1016/j.clinbiomech.2021.105553.

**Conseguenza CAD:** `MaterialModifier`/stiffness map non è solo una funzione di manufacturing, ma una variabile prescrittiva.

---

## SCI-05 — Customized 3D printed insole outcome

Xu R et al.  
*Comparative Study of the Effects of Customized 3D Printed Insole and Prefabricated Insole on Plantar Pressure and Comfort in Patients with Symptomatic Flatfoot.*  
Med Sci Monit. 2019;25:3510-3519.  
PMID 31079137. DOI 10.12659/MSM.916975.

---

## SCI-06 — Metatarsal offloading

Ruiz-Ramos M et al.  
*Effectiveness of bespoke or customised orthotic treatment in plantar pressure reduction of the central metatarsals: a systematic review and meta-analysis.*  
J Orthop. 2024;59:111-118.  
PMID 39399760. DOI 10.1016/j.jor.2023.12.006.

**Conseguenza CAD:** metatarsal bar/pad/offloading deve rimanere nella libreria funzionale.

---

## SCI-07 — 3D foot shape methodology

Allan JJ et al.  
*Methodological and statistical approaches for the assessment of foot shape using three-dimensional foot scanning: a scoping review.*  
J Foot Ankle Res. 2023.  
PMID 37106385. DOI 10.1186/s13047-023-00617-z.

---

# 23. Funzioni strategiche da aggiungere oltre EasyCAD2

Queste non risultano confermate nella documentazione EasyCAD2 analizzata, ma sono raccomandate per BiomechE-CAD.

## P0 strategico

### CAD-OPEN-001 — Project schema documentato
JSON/structured manifest + binary geometry assets.

### CAD-OPEN-002 — deterministic rebuild
Dallo stesso project revision e dallo stesso engine version deve essere possibile rigenerare la stessa geometria entro tolleranza dichiarata.

### CAD-OPEN-003 — mesh validation
Manifold/self-intersection/degenerate/min thickness.

### CAD-OPEN-004 — provenance
Ogni import e auto-operation conserva fonte/versione.

### CAD-OPEN-005 — API boundary
Separare CAD engine da UI e manufacturing.

## P1

- 3MF;
- OBJ;
- plugin/import adapter;
- SDK/API;
- protocol library;
- reusable prescription presets;
- pre/post BiomechE outcome;
- version comparison;
- automatic anatomical landmark suggestion;
- DFM profile per materiale/macchina;
- report JSON + PDF;
- material maps;
- formula/parameter export.

## R&D

- variable density;
- variable stiffness;
- lattice/metamaterial;
- multi-material printing;
- FEM;
- pressure outcome prediction;
- automatic design optimization;
- AI assistant;
- learned shape suggestion.

Regola:

```text
AI suggests
operator approves
system records rationale + evidence + model/version
```

---

# 24. Non-functional requirements

## CAD-NFR-001 — Performance

Editing interattivo senza blocchi percepibili su workstation target.

Target iniziale da validare:

```text
camera/preview: >= 60 fps preferred
interactive editing: >= 30 fps acceptable
expensive final rebuild: async/cancellable
```

## CAD-NFR-002 — Numerical determinism

Operazioni geometriche critiche devono essere testabili con fixture deterministiche.

## CAD-NFR-003 — Unit safety

Nessun valore geometrico senza unità semantica.

## CAD-NFR-004 — Data integrity

Autosave, crash recovery, versioned project schema.

## CAD-NFR-005 — Privacy

Patient-identifiable data separabile/escludibile dagli artifact manufacturing.

## CAD-NFR-006 — Audit

Registrare:

```text
operator
time
operation
parameters
source
software version
```

## CAD-NFR-007 — Offline operability

La progettazione base non dipende da cloud/internet.

## CAD-NFR-008 — Hardware independence

Scanner, platform e printer integrations devono essere adapter/plugin, non logica hardcoded nel geometry core.

## CAD-NFR-009 — Testability

Ogni requisito P0 deve avere acceptance test o testable invariant.

## CAD-NFR-010 — Backward compatibility

Project migration obbligatoria tra schema versioni supportate.

---

# 25. Architettura software funzionale raccomandata

```text
BiomechE-CAD.App
    UI / workflow / patient/project management

BiomechE-CAD.Contracts
    public DTO/enums/units/project schema

BiomechE-CAD.Geometry
    template
    parametric surfaces
    operations
    elements
    mesh generation
    boolean/offset/smoothing

BiomechE-CAD.Acquisition
    pressure adapter
    Scan3D
    Scan2D
    registration
    BiomechE bridge

BiomechE-CAD.Analysis
    measurements
    sections
    thickness
    geometry QC
    DFM

BiomechE-CAD.Manufacturing
    closure profiles
    material maps
    STL/3MF
    manufacturing package

BiomechE-CAD.CAM
    optional CNC post-processors / GCODE

BiomechE-CAD.Reporting
    JSON
    PDF

BiomechE-CAD.Persistence
    project DB
    migrations
    audit/history
```

Third-party geometry/rendering libraries possono essere usate internamente ma non devono definire il formato progetto o i contratti pubblici.

---

# 26. MVP consigliato

## P0 — MVP clinico serio

### Workflow/dati
- patient/case/project;
- DX/SX;
- mirror;
- versioned project;
- autosave/history.

### Acquisition
- BiomechE pressure;
- CSV pressure;
- STL scan;
- 2D image;
- registration;
- heel/1st/5th landmarks.

### DIMA
- template;
- L/W;
- shoe size helper;
- editable outline;
- custom template.

### Parametric EDIT
- global thickness;
- flatten;
- heel/wrap;
- camber;
- medial arch;
- lateral arch;
- rearfoot wedge;
- forefoot wedge;
- smooth.

### Elements
- heel cup;
- metatarsal bar/pad;
- arch supports;
- heel relief;
- wedges;
- local raise/drop;
- custom transform.

### Sculpt
- raise/lower;
- smooth;
- freehand ROI;
- circle ROI;
- deformation to scan.

### QC
- section;
- ruler;
- height;
- angle;
- thickness map;
- min thickness;
- manifold validation.

### Production
- STL;
- project package;
- straight/bridge/bevel closure;
- DFM report.

---

# 27. P1

- full EasyCAD2-style element library;
- custom element editor;
- material modifier;
- five-level stiffness abstraction;
- 3MF;
- CNC/GCODE;
- printer profiles;
- custom material profiles;
- text engraving;
- PDF report;
- project comparison;
- template morphing;
- pressure-based suggestion;
- reusable clinical protocol presets.

---

# 28. P2 / R&D

- lattice;
- variable stiffness physical map;
- multi-material;
- automatic optimization;
- FEM;
- ML/AI;
- predicted pressure redistribution;
- cloud collaboration;
- centralized preset distribution.

---

# 29. Validation strategy

Il piano EasyCAD2 1.4 è un buon modello per il livello di user-story validation, ma BiomechE-CAD dovrebbe aggiungere anche test quantitativi geometrici.

## 29.1 Functional validation

Creare test `CAD-US-*` equivalenti almeno alle 25 user stories EasyCAD2:

1. project/database;
2. laterality/mirror;
3. dima;
4. pressure;
5. Scan3D/2D;
6. global thickness;
7. heel/camber;
8. arches;
9. wedges;
10. elements;
11. custom elements;
12. material modifiers;
13. sculpt;
14. global deformation;
15. section/QC;
16. ruler;
17. production;
18. material/stiffness;
19. report;
20. min-thickness warning;
21. safe close.

## 29.2 Geometry invariants

Aggiungere test automatici:

```text
no NaN/Inf
valid orientation
no unexpected self intersections
manifold when export requires it
minimum thickness >= profile limit
boundary closed
area/volume finite
mirror preserves anatomical semantics
unit conversion round-trip
registration transform invertible
```

## 29.3 Golden geometry tests

Per ogni operazione parametrica, fixture con:

```text
input template
parameters
expected key dimensions
expected section profiles
mesh fingerprint tolerant to allowed tessellation changes
```

## 29.4 Scientific validation

Distinguere sempre:

```text
geometry correctness
manufacturing correctness
biomechanical efficacy
clinical efficacy
```

Il fatto che un CAD generi correttamente un wedge di 4° non dimostra automaticamente che 4° sia la prescrizione clinica corretta per un paziente.

---

# 30. Screen/page evidence map — EasyCAD2 manual

Per evitare di copiare immagini protette nel repository, conservare riferimenti pagina/descrizione anziché redistribuire automaticamente gli screenshot.

| Manual PDF page | Evidenza |
|---:|---|
| 7-12 | database, patient, project history, settings, printers, CNC, units |
| 13 | camera/navigation/multiselect |
| 14 | DX/SX + mirror |
| 15-18 | DIMA, template, advanced template, dimensions |
| 19-20 | Pressure, registration X/Y/rotation/scale, Generate |
| 21-22 | Scan3D landmarks, Align, crop |
| 23 | Scan2D |
| 24-30 | EDIT: vertices, thickness, flatten, advanced, heel, arches, wedges, smooth |
| 31-35 | Elements library, categories, sum/intersection, transforms, custom element |
| 36-40 | Post Processing, global deformation, sculpt, smooth, freehand/circle deform |
| 42-44 | Control, cross-section, fixed heights |
| 44-50 | Produce, closures, text, materials, CNC, 3D print hardness |
| 50-52 | Toolbar, views, overlays, height, ruler, history |
| 52-53 | min thickness warning, auto-fix, safe close |

---

# 31. Audit di completezza rispetto alla ricerca EasyCAD2 precedente

Questo capitolo serve esplicitamente a verificare che il consolidamento non abbia perso informazioni.

## 31.1 Precedenti feature EC2-001 ... EC2-030

Tutte le 30 feature del primo audit sono state mantenute e, con il manuale, dettagliate.

Aggiornamenti più importanti:

| Finding precedente | Stato dopo manuale/validation | Destinazione |
|---|---|---|
| Patient/project DB | CONFERMATO + dettagli CRUD/history | §4 |
| Pressure input | CONFERMATO `.bpe/.csv`, X/Y/rot/scale/Generate | §8.1 |
| Scan3D | CONFERMATO `.stl`, heel/1st/5th, Align, crop | §8.2 |
| Scan2D | CONFERMATO + calibration L/W da validation | §8.3 |
| DIMA control points | CONFERMATO | §7 |
| Template pressure overlay | CONFERMATO | §8 |
| Heel | CONFERMATO con wrap/camber params | §9.3 |
| Medial arch | CONFERMATO con 7 parametri | §9.4 |
| Lateral arch | CONFERMATO con 6 parametri | §9.5 |
| Wedges | CONFERMATO in gradi | §10 |
| Elements | CONFERMATO e ampliato | §12 |
| 3D sculpt | CONFERMATO e dettagliato | §15 |
| Numeric control | CONFERMATO | §16 |
| Height visualization | CONFERMATO | §16 |
| STL | CONFERMATO | §18 |
| GCODE | CONFERMATO | §18 |
| CNC | CONFERMATO | §18.5 |
| 3D print | CONFERMATO | §18.6 |
| project compatibility/version concern | PRESERVATO come requisito schema/migration | §20 |

---

## 31.2 Precedenti feature LINEAGE-001 ... LINEAGE-035

### Ora promosse a confermate

- Template per calzatura/use case → SPORT/SANDALO/CLASSIC/COMFORT/DONNA.
- Import/riposizionamento scan/pressure.
- Shape adaptation toward scan/pressure → Global Deformation.
- Auto-modelling da pressure → `GENERATE`.
- Global thickness.
- Heel/arch parameters.
- Libreria forefoot/midfoot/rearfoot.
- Barre metatarsali.
- Cunei.
- Proprioceptive elements.
- Transform element.
- Position/scale/rotation.
- Local deformation/offload.
- Freehand area.
- edge/border smoothing.
- mirror controlaterale.
- smoothing.
- cross-section.
- wedge angle semantics.
- reusable template.
- reusable custom element.
- materials.
- CAM setup.
- sharing package ZIP.

### Confermate ma con semantica diversa/più precisa

- `Custom selections` → presenti come ROI freehand/circle e modifier regions; il salvataggio riusabile della ROI generica va ancora specificato.
- `Thickness/elevation element` → Z SCALE confermato; non necessariamente identico al vecchio parametro legacy.
- `Report PDF` → confermato in 1.4 validation.
- `Material/density` → confermato tramite hardness overall/per-element e modifier regions.

### Restano non confermate

- generazione positiva per termoformatura;
- scheda di conformità regolatoria dedicata;
- compatibilità ufficiale generale con scanner/pedane di terze parti;
- exact scaling range 18-55;
- trasferimento cloud fra centri come servizio;
- specifica completa dei rivestimenti multilayer.

Nessuna di queste voci è stata rimossa: rimane nel backlog/open questions.

---

## 31.3 Precedenti claim SECONDARY

| Claim precedente | Nuovo stato |
|---|---|
| Generazione automatica DIMA da Scan3D | NON CONFERMATA in questa forma; confermati Align + deformazione |
| Pulizia/allineamento 2D | PARZIALE: calibration/alignment confermati |
| Cloud template library | NON CONFERMATA |
| Arch start/end/curvature | CONFERMATA e ampliata |
| Wedge mm/deg | DEG CONFERMATO; mm non confermato come input wedge |
| Bridge | CONFERMATO |
| Thin insole workflow | PARZIALE: thickness + 0.8 mm warning confermati |
| Density regions | CONFERMATO in 1.4 |
| Patient-name engraving | testo 3D generico CONFERMATO; auto patient-name non confermato |
| Automatic toolpath | GCODE CONFERMATO; algoritmo toolpath non documentato |
| DFM thin warning | CONFERMATO |
| Improved smoothing/color scale | smoothing + height visualization CONFERMATI |

---

## 31.4 Requisiti scientifici precedenti

Tutti preservati:

- wedge/posting parametrico;
- pressure dataset quantitativo;
- scan provenance;
- variable stiffness/material map;
- scientific evidence ledger;
- explainable future AI.

---

## 31.5 P0/P1/P2 precedente

La precedente prioritizzazione è stata mantenuta e raffinata nei §§26-28.

Nessun requisito P0 precedente è stato eliminato.

---

## 31.6 Audit meccanico delle voci con corrispondenza lessicale debole

Un secondo controllo meccanico del documento precedente (`EC2-*` + `LIN-*`) ha evidenziato alcune voci che nella nuova specifica erano presenti semanticamente ma non sempre con la stessa terminologia. Per evitare perdite future vengono rese esplicite qui:

- **EC2-014 — winding/avvolgimento:** preservato come `heel/wrap` / `Altezza avvolgenza` / `Curvatura avvolgenza`; la semantica geometrica esatta resta da formalizzare.
- **EC2-015 — bowl/cup:** preservato come `heel cup / conca tallone` e nella libreria elementi.
- **EC2-022 — mappa 3D colorata delle altezze:** preservata come `Height map / colore per quota`.
- **EC2-029 — import legacy ADM:** non è requisito MVP, ma va mantenuto nel backlog di interoperabilità legacy come possibile adapter/migratore qualora BiomechE-CAD debba importare progetti EasyCAD storici.
- **LIN-014 — fillings/stability/heel adjustment:** il concetto generale è coperto dagli elementi, heel adjustment e deformazioni locali; eventuali specifici “fill/stability” del legacy EasyCAD devono essere verificati nella futura compatibility matrix e non sono considerati già equivalenti.
- **LIN-017 — selezioni anatomiche predefinite:** preservate come requisito P1 di `semantic/anatomical ROI masks`, da collegare ai modelli regionali BiomechE senza assumere una segmentazione commerciale universale.
- **LIN-018 — salvataggio selezioni custom:** il documento già prevede ROI freehand/circle e modifier regions; viene mantenuto esplicitamente il requisito P1 di salvare una ROI/mask custom come preset riusabile.
- **LIN-020 — edge height/shape:** preservato come requisito di boundary/sidewall editing e controllo bordo; dovrà essere formalizzato nella specifica geometrica.
- **LIN-029 — generatore di modelli/preset riutilizzabili:** preservato come `clinical protocol / prescription preset library`, separato dai soli template geometrici.
- **LIN-034 — trasmissione dati tra centri produttivi:** preservata come P2 `production handoff/collaboration package`; il package progetto deve poter essere trasferibile senza rendere obbligatorio un cloud proprietario.
- **LIN-035 — hardware di terze parti:** resta un obiettivo strategico tramite adapter/plugin; non è attribuito come capacità EasyCAD2 1.4 senza nuova evidenza primaria.

### Requisiti espliciti aggiunti dall'audit

- `CAD-ROI-001` — anatomical semantic masks / region presets — **P1**.
- `CAD-ROI-002` — save/load reusable custom ROI masks — **P1**.
- `CAD-PRESET-001` — reusable clinical/prescription protocol presets — **P1**.
- `CAD-COLLAB-001` — portable production-handoff package independent from mandatory cloud — **P2**.
- `CAD-LEGACY-001` — optional EasyCAD/ADM legacy import adapter if business requirements demand migration — **P2/compatibility**.
- `CAD-ADAPTER-001` — third-party acquisition/manufacturing integrations behind explicit adapters — **P0 architectural / implementation as needed**.

**Audit conclusion:** after this explicit preservation pass, no feature from the previous 65-row `EC2-*`/`LIN-*` inventory is intentionally dropped. Items not promoted to product requirements remain traceable as lineage, compatibility or open research rather than disappearing.

---

# 32. Gap attuali dopo il consolidamento

## EasyCAD2 — ancora da verificare

1. Formula matematica esatta di medial/lateral arch.
2. Formula di camber/heel wrap.
3. Formula wedge e asse geometrico interno.
4. Algoritmo `GENERATE` da pressure.
5. Algoritmo Global Deformation da pressure/scan.
6. Full element library con nomi/versioni.
7. Meaning esatto di tutti i proprioceptive elements.
8. Material property associata ai 5 livelli hardness.
9. Formato del package ZIP.
10. Formato `.raw`.
11. Formato interno DB/progetto.
12. Slicer/API protocol per `Produci`.
13. GCODE post-processor details.
14. Report PDF exact fields.
15. Eventuale SDK/API.
16. Eventuale plugin system.
17. Cloud/preset distribution.
18. 3MF/multi-material native support.
19. OBJ/STEP import/export.
20. mesh repair/manifold checker.
21. version diff.
22. formal project schema migration.
23. full regulatory traceability.
24. physical manufacturing tolerance definitions.
25. validation of clinical efficacy versus only software behavior.

---

# 33. Decisioni preliminari da congelare nel progetto

## D-CAD-001
Markdown sotto `docs/` è la source of truth della specifica.

## D-CAD-002
EasyCAD2 è il principale behavioral benchmark iniziale, non il limite architetturale del prodotto.

## D-CAD-003
Geometry operations sono non-distruttive/versionate quando tecnicamente ragionevole.

## D-CAD-004
Unità canoniche coerenti con BiomechE: mm, deg, kPa, N.

## D-CAD-005
Acquisition provenance e registration transform sono first-class data.

## D-CAD-006
Pressure non è una texture: rimane dataset quantitativo.

## D-CAD-007
Material/stiffness regions sono separate dalla pura geometria.

## D-CAD-008
CAM/GCODE è un modulo separato dal geometry core.

## D-CAD-009
Ogni export è legato a una project revision immutabile.

## D-CAD-010
Ogni feature P0 dovrà avere acceptance criteria e regression test.

---

# 34. Prossimo passo operativo

Prima dell'implementazione del kernel CAD:

1. congelare coordinate system e side semantics;
2. definire `Project Schema v0`;
3. definire `BaseTemplate`;
4. definire `Operation Stack`;
5. definire matematicamente:
   - heel;
   - medial arch;
   - lateral arch;
   - wedge;
   - local ROI deform;
6. scegliere kernel geometrico/mesh representation;
7. costruire synthetic geometry test suite;
8. implementare DIMA + section/thickness inspector;
9. poi acquisizioni e registration;
10. poi parametric EDIT;
11. poi Elements;
12. poi post-processing;
13. poi manufacturing.

---

# 35. TODO / DONE consolidato

## DONE

- [x] Manuale EasyCAD2 1.1.x.x acquisito e analizzato.
- [x] Piano validazione EasyCAD2 1.4.x.x acquisito.
- [x] Rapporto validazione EasyCAD2 1.4.x.x acquisito.
- [x] 25 user story di validazione integrate nella specifica.
- [x] Workflow EasyCAD2 ricostruito.
- [x] DIMA dettagliata.
- [x] Pressure import/registration dettagliati.
- [x] Scan3D landmark/alignment dettagliati.
- [x] Scan2D calibration identificata.
- [x] Parametri heel/camber dettagliati.
- [x] Parametri medial/lateral arch dettagliati.
- [x] Wedge DEG confermato.
- [x] Element library e categorie confermate.
- [x] Barra metatarsale confermata.
- [x] Custom elements confermati.
- [x] Material modifiers confermati.
- [x] Stiffness overall/per-element confermata.
- [x] Global deformation confermata.
- [x] Sculpt/smooth/deform ROI dettagliati.
- [x] Control/cross-section dettagliato.
- [x] Minimum thickness 0.8 mm warning + auto-fix confermato.
- [x] Bridge/Dritto/Obliquo dettagliati.
- [x] text/Slice3D confermato.
- [x] CNC/GCODE confermato.
- [x] STL confermato.
- [x] ZIP sharing package confermato.
- [x] PDF report confermato in 1.4.
- [x] Action history/undo/redo confermato.
- [x] Safe close confermato.
- [x] Ricerca scientifica precedente preservata.
- [x] Audit delle feature precedenti eseguito.
- [x] P0/P1/P2 aggiornati.

## TODO

- [ ] Audit competitor one-by-one contro questa specifica.
- [ ] ParoContour / DIERS deep feature audit.
- [ ] FitFoot360 audit.
- [ ] Rodin4D/Neo audit.
- [ ] Vorum/Canfit audit.
- [ ] Altri CAD/CAM ortesici internazionali.
- [ ] Mathematical geometry spec per arch/heel/wedge.
- [ ] Project schema v0.
- [ ] Coordinate/registering spec.
- [ ] Material/stiffness property model.
- [ ] Manufacturing/DFM profile spec.
- [ ] Kernel technology evaluation.
- [ ] Performance architecture.
- [ ] Validation strategy dettagliata con golden meshes.
- [ ] Regulatory/data privacy analysis.
- [ ] Source reference ledger completo.
- [ ] Eventuale audit diretto EasyCAD2 1.4 build/video.
- [ ] Verifica full element library EasyCAD2.
- [ ] Verifica `.raw` e ZIP schemas se disponibili.
- [ ] Verifica API/protocollo produzione.
- [ ] Aggiornare questo documento quando una fonte nuova modifica una conclusione.

---

# 36. Bibliografia e fonti web già individuate nella ricerca precedente

## Vendor

- Sensor Medica — EasyCAD2  
  https://www.sensormedica.com/en/easycad-2/
- Sensor Medica — easyCAD Insole  
  https://www.sensormedica.com/en/easycad-insole/
- Sensor Medica — Vulcan CNC  
  https://www.sensormedica.com/it/vulcan-cnc/
- Sensor Medica — workflow/corso EasyCAD2  
  https://www.sensormedica.com/it/elementor-13305/
- Chitti4Feet — EasyCAD2 overview, secondary source  
  https://www.chitti4feet.com/easycad2-per-la-creazione-di-ortesi-plantari/

## Primary documents supplied for this consolidation

- EasyCAD2 Manuale ITA 2.0 / software 1.1.x.x  
  https://drive.google.com/file/d/148X366g4e47cYOWtFWP-jeMqavSJqHTa/view
- Piano validazione EasyCAD2 1.4.x.x  
  https://drive.google.com/file/d/19Pdjn76a6sAEcnUTut2qL0qzvfkniD4v/view
- Rapporto test validazione EasyCAD2 1.4.x.x  
  https://drive.google.com/file/d/1kbDKQd6qskQH1MyZ5O3Y-WYt5p_7qRlJ/view

---

# 37. Nota finale di interpretazione

La documentazione EasyCAD2 dimostra che un CAD per plantari maturo non è soltanto:

```text
import STL -> sculpt -> export STL
```

ma una combinazione di:

```text
clinical data
+ template
+ anatomical/parametric edits
+ corrective feature library
+ freeform refinement
+ quantitative QC
+ manufacturing semantics
+ patient/project traceability
```

BiomechE-CAD dovrebbe mantenere questa completezza funzionale, ma rendere ogni passaggio più **esplicito, misurabile, versionato, interoperabile e scientificamente tracciabile**.
