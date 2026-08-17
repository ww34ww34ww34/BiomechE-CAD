# BiomechE-CAD — Mockups V2 / Surface-CAD Workstation

**Date:** 2026-08-17  
**Status:** ACTIVE DESIGN WORKSPACE  
**Owning visual direction:** `../../BIOMECHE_CAD_VISUAL_DIRECTION_V2_SURFACE_CAD_2026-08-17.md`

V2 is produced **one full-screen CAD workspace at a time**. Do not rebuild it as a five-screen collage.

## Screen register

| ID | Workspace | Status | Canonical asset / next action |
|---|---|---|---|
| `V2-S01` | Template / Modello | **APPROVED** | `approved/V2-S01-template-modello-approved.jpg` |
| `V2-S02` | Superficie / Edit Parametrico | **NEXT** | generate using S01 as visual-language authority |
| `V2-S03` | Elementi | NOT GENERATED | after S02 approval |
| `V2-S04` | Scultura / Post Processing | NOT GENERATED | after S03 approval |
| `V2-S05` | Analisi / Produzione | NOT GENERATED | after S04 approval |

## V2-S01 approval

Explicit user approval: **2026-08-17**.

Canonical visual asset:

`approved/V2-S01-template-modello-approved.jpg`

Repository asset is a high-quality review JPEG derived from the approved 1448×1086 generation. Visual content is authoritative for the V2-S01 appearance; frozen written product specifications remain semantic authority.

SHA-256 of the persisted JPEG materialization:

`2b26d9cd78083affbd8ec292e108d9aeb05181abd37c4a6ca4b5b499e38d032e`

### Visual traits frozen by S01 approval

- full-screen high-level industrial CAD workstation;
- dark graphite/navy neutral shell, not decorative sci-fi HUD;
- dominant 3D orthosis viewport;
- thin precise geometry lines, surface cage/curves/control points and dimensional annotations;
- main mode strip `MODELLO / SUPERFICIE / SCULTURA / ANALISI / PRODUZIONE`;
- compact contextual toolbars instead of dashboard cards;
- left input/reference context;
- right contextual parameters plus Scene/Layers;
- small orthographic reference views;
- restrained blue/cyan active-state accent;
- amber/orange reserved for selected geometry where useful;
- units/grid/snap/status visible but secondary;
- immediate, professional CAD readability.

## Approval workflow

```text
GENERATE -> REVIEW -> REVISE -> EXPLICIT USER APPROVAL -> PERSIST -> NEXT SCREEN
```

A generated image is never canonical merely because it exists.

## Exact next visual task

Generate **V2-S02 — Superficie / Edit Parametrico** as one normal-resolution full-screen application view. Use approved V2-S01 as the primary style reference. The new screen must feel like the same product and same CAD workstation, while the center viewport and contextual tools shift to semantic/parametric surface editing.