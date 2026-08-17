# BiomechE-CAD — Decision Register Addendum — Visual Direction V2

**Date:** 2026-08-17  
**Status:** CANONICAL ADDENDUM  
**Purpose:** record the current visual-design decisions without rewriting the historical P0/V1 baseline.

---

## D-CAD-037 — V1 remains functional visual evidence; V2 owns the active aesthetic direction

**Status:** ACTIVE DESIGN DECISION  
**Date:** 2026-08-17

The V1 visual package remains valid for functional/state/traceability coverage and must not be deleted.

However, the preferred implementation look-and-feel is now being redesigned as **Visual Direction V2 — Surface-CAD Workstation**.

Authority split:

```text
written frozen specs              semantic authority
V1 visual package                 functional/state/traceability visual evidence
V2 Surface-CAD direction          active aesthetic/workspace composition direction
```

V2 must never override written product semantics.

---

## D-CAD-038 — BiomechE-CAD should visually read as a high-level CAD workstation, not a medical dashboard

**Status:** ACTIVE DESIGN DECISION  
**Date:** 2026-08-17

The desired visual language is a professional industrial surface-modeling workstation adapted to orthotic CAD.

Required traits:

- dominant geometry viewport;
- dark graphite neutral application chrome;
- compact monochrome tools;
- contextual property panels;
- Scene/Layers hierarchy;
- direct surface/curve/control-point editing;
- metric annotations and orthographic/section views;
- restrained blue active accent;
- amber/orange selected geometry;
- rich geometry rendering with quiet UI.

Explicitly rejected as primary visual language:

- medical-dashboard/KPI-card composition;
- generic SaaS application layout;
- excessive neon/Jarvis HUD decoration;
- decorative circuit/grid borders;
- heatmap-dominated authoring;
- five-screen poster/collage as the screen-design artifact.

Futurism should come from precision, geometry quality and interaction sophistication, not ornamental sci-fi effects.

---

## D-CAD-039 — V2 is designed and approved one full-screen CAD workspace at a time

**Status:** ACTIVE DESIGN PROCESS RULE  
**Date:** 2026-08-17

Canonical V2 sequence:

```text
V2-S01 Template / Modello
V2-S02 Superficie / Edit Parametrico
V2-S03 Elementi
V2-S04 Scultura / Post Processing
V2-S05 Analisi / Produzione
```

Process:

```text
GENERATE -> REVIEW -> REVISE -> EXPLICIT APPROVAL -> PERSIST -> NEXT SCREEN
```

No generated screen is canonical before explicit approval.

Current state:

```text
V2-S01 REVIEW — latest candidate generated 2026-08-17, not yet approved
V2-S02..S05 NOT GENERATED
```

---

## D-CAD-040 — Orthotic context stays visible but subordinate to CAD authoring

**Status:** ACTIVE DESIGN DECISION  
**Date:** 2026-08-17

Pressure, Scan2D, Scan3D, landmarks and BiomechE results remain valuable contextual/reference data.

In V2 they should feed the CAD workspace rather than visually define it.

Examples:

- compact source thumbnails/visibility toggles;
- reference layers in Scene/Layers;
- overlays only when relevant;
- analysis data invoked contextually;
- corrective elements represented as semantic CAD objects.

The central visual identity remains the authored orthosis surface and its controllable geometry.

---

## D-CAD-041 — Q0 geometry qualification remains ready but is temporarily parked during V2 visual refinement

**Status:** ACTIVE EXECUTION ORDER  
**Date:** 2026-08-17

No architecture decision is reversed.

Q0 remains ready with the exact pinned OpenSubdiv/openNURBS candidates and the existing qualification harness. No engine winner exists.

The immediate conversation-level continuation point is currently **V2-S01 visual refinement**. Once the visual checkpoint is complete or the user explicitly returns to architecture work, continue Q0 without restarting generic engine research.
