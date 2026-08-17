# BiomechE-CAD — Next Chat Prompt

**Updated:** 2026-08-17  
**Purpose:** copy/paste into a new ChatGPT conversation to continue from the current checkpoint.

---

Continua il progetto **BiomechE-CAD** dal checkpoint corrente.

Repository canonico: `ww34ww34ww34/BiomechE-CAD`, branch `main`.

## Leggi prima

```text
docs/RESUME_HERE.md
docs/ux/BIOMECHE_CAD_VISUAL_DIRECTION_V2_SURFACE_CAD_2026-08-17.md
docs/ux/mockups/v2/README.md
docs/DECISIONS_2026-08-17_VISUAL_V2_ADDENDUM.md
docs/SPEC_INDEX.md
docs/spec/BIOMECHE_CAD_FUNCTIONAL_SPEC_V2.md
docs/TRACEABILITY_MATRIX.md
```

La documentazione P0 è completa e il Q0 geometry-engine harness è già pronto, ma **in questo momento stiamo rifinendo la Visual Direction V2** prima di tornare ai test architetturali.

## DIREZIONE VISIVA DA ASSUMERE

Non usare il vecchio look da medical dashboard come riferimento estetico principale.

La nuova direzione è:

```text
HIGH-LEVEL INDUSTRIAL SURFACE CAD
premium desktop workstation
geometry-first
professional dark graphite UI
compact contextual controls
Scene/Layers + Properties
surface curves / control points / section views when useful
restrained blue active states
amber/orange selected geometry
rich neutral geometry rendering
minimal decorative glow
```

Il riferimento concettuale è la grammatica visiva dei CAD di surface modeling professionali: grande viewport, tool strip sottile, pannelli tecnici compatti, gerarchia Scene/Layers, proprietà contestuali, materiale clay/graphite, curve e punti di controllo visibili.

**Da evitare:**

```text
medical SaaS dashboard
KPI cards / score rings come identità principale
five-screen poster/collage
Jarvis neon HUD
circuiti/griglie decorative
cyan glow eccessivo
rainbow heatmap su ogni schermata
interfaccia consumer con geometria piccola
```

Futuristico sì, ma per precisione e qualità CAD, non per decorazione sci-fi.

## WORKFLOW V2

Disegnare e approvare **una schermata completa alla volta**:

```text
V2-S01 Template / Modello                 REVIEW
V2-S02 Superficie / Edit Parametrico      NOT GENERATED
V2-S03 Elementi                           NOT GENERATED
V2-S04 Scultura / Post Processing         NOT GENERATED
V2-S05 Analisi / Produzione               NOT GENERATED
```

Processo obbligatorio:

```text
GENERATE -> REVIEW -> REVISE -> EXPLICIT APPROVAL -> PERSIST -> NEXT SCREEN
```

Non assumere che un'immagine generata sia approvata.

## PROSSIMO TASK ESATTO

**Refina soltanto V2-S01 — Template / Modello.**

Genera una singola schermata CAD full-screen, non una tavola di presentazione e non un collage.

La schermata deve includere:

```text
TOP APP BAR
  BiomechE-CAD, progetto/case context, undo/redo/save/help/settings

PRIMARY MODE TABS
  MODELLO | SUPERFICIE | SCULTURA | ANALISI | PRODUZIONE
  MODELLO attivo

CONTEXT CAD TOOLBAR
  icone compatte e professionali

LEFT AREA
  source/reference data compatti: pressure / Scan2D / Scan3D
  + tool rail CAD

CENTRAL VIEWPORT
  deve dominare la schermata
  plantare/ortesi 3D high-quality clay/graphite
  curve di riferimento selezionate
  pochi control point chiari
  quote metriche mm
  illuminazione studio sobria

RIGHT AREA
  Scene / Layers
  parametri Template/Base contestuali
  eventuali proprietà della selezione

FLOATING MINI VIEWS
  top / side / rear quando utili

BOTTOM STATUS
  units mm / grid / snap / current mode / optional FPS/status
```

La geometria deve sembrare una vera superficie CAD di alto livello, non una mesh da demo. L'interfaccia deve poter essere immaginata come ambiente di lavoro quotidiano per un progettista di plantari.

Non passare a V2-S02 fino ad approvazione esplicita dell'utente.

## PRINCIPI DI PRODOTTO DA NON VIOLARE

```text
committed DesignRevision immutable
original source != processed/registered/derived
placement typed anatomical/reference, not raw XYZ authority
requested dose != realized CAD dose
geometry dose != mechanical/material dose
semantic prescription survives geometry
no hidden universal clinical default
OPEN means OPEN
BiomechE quantitative KPI authority
preview != commit != manufacturing release
geometry kernel satisfies frozen contract, never redefines it
```

Il V2 cambia estetica/workspace composition, non la semantica frozen.

## Q0 ARCHITECTURE — PARKED BUT READY

Quando il visual checkpoint sarà completato o l'utente chiederà di tornare all'architettura, riprendi Q0 senza rifare ricerca generica.

Candidate locks:

```text
OpenSubdiv v3_7_0
commit 9dab8a47bfbb1388ec8388fe61f5f916e6123f38

openNURBS 8.x snapshot
commit 00bdd2ce8f3e4cd3d4921343909bbe123b2e9d58
```

Harness:

`qualification/geometry-engine/q0/`

Actual candidate native/server/WASM builds = **NOT EXECUTED**. No engine winner selected.

Project Schema v0.2 = **APPROVED / NOT MATERIALIZED**.  
`TD-CI-001` = **DEFERRED / NON-BLOCKING**.

## At each phase transition

Update:

```text
docs/RESUME_HERE.md
docs/SPEC_INDEX.md
docs/NEXT_CHAT_PROMPT.md
docs/ux/mockups/v2/README.md
```

Keep DONE/TODO explicit and never claim approval or executed evidence that did not occur.
