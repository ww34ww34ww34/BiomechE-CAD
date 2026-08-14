# BiomechE-CAD — EasyCAD2 1.4 Geometry/Architecture Parity Matrix

**Status:** architecture coverage gate  
**Date:** 2026-08-14  
**Primary source:** EasyCAD2 Validation Plan 1.4.x.x (15/01/2026) + Validation Report (20/01/2026).

Purpose: verify that the proposed **canonical control cage + OpenSubdiv + field/operator engine + scan/query + production layer** can cover the validated EasyCAD2 workflow without requiring a general-purpose NURBS/B-Rep CAD kernel.

Legend:

- `CORE` = geometry/control-cage/OpenSubdiv core;
- `DATA` = project/database/settings;
- `ACQ` = acquisition/registration;
- `PROD` = production/manufacturing;
- `REPORT` = reporting;
- `PASS-ARCH` = architecture has a defined implementation path;
- `OPEN-ALG` = exact algorithm/fixture still to freeze, but no new geometry paradigm is required.

| US | EasyCAD2 validated behavior | BiomechE-CAD module | Coverage | Need B-Rep/NURBS? |
|---|---|---|---|---|
| US1 | License activation | DATA | PASS-ARCH | No |
| US2 | Add patient | DATA | PASS-ARCH | No |
| US3 | Search/edit/delete patient | DATA | PASS-ARCH | No |
| US4 | Language + metric/imperial | DATA | PASS-ARCH | No |
| US5 | 3D printer + CNC settings | PROD/DATA | PASS-ARCH | No |
| US6 | Mirror current orthosis DX→SX | CORE | PASS-ARCH via compatible cage topology + semantic mirror | No |
| US7 | DIMA template + shoe size + L/W | CORE | PASS-ARCH via template/cage morph + outline constraints | No |
| US8 | Pressure .bpe/.csv + X/Y/rotation/scale | ACQ | PASS-ARCH via registered quantitative pressure layer | No |
| US9 | STL scan + heel/1st/5th + Align; Image2D L/W | ACQ | PASS-ARCH via scan mesh + landmarks + transform | No |
| US10 | Global thickness + flatten | CORE/PROD | OPEN-ALG: semantic thickness field + explicit flatten op | No |
| US11 | Heel/wrap/camber without mesh distortion | CORE | OPEN-ALG: heel field on stable cage + limit surface | No |
| US12 | Medial/lateral arch start/center/end etc. | CORE | OPEN-ALG: intrinsic `(s,q)` arch field | No |
| US13 | Rear/forefoot wedges in degrees, full/partial | CORE | PASS-ARCH: angular plane/field operator | No |
| US14 | Insert/position/scale/rotate elements on mesh | CORE | PASS-ARCH: corrective element field/cage transform | No |
| US15 | Modify element vertices + save CUSTOM | CORE/DATA | PASS-ARCH: element cage + versioned preset | No |
| US16 | Closed modifier region for 3D-print rigidity | CORE/PROD | PASS-ARCH: ROI + MaterialModifier, no shape topology change | No |
| US17 | Sculpt radius/strength locally deforms mesh | CORE | PASS-ARCH: brush displacement layer | No |
| US18 | Global deformation conforms mesh to scan | CORE/ACQ | PASS-ARCH: ScanConformOperation + nearest/project query | No |
| US19 | Diagonal cross-section + fix heights | CORE | PASS-ARCH: limit/tessellated-surface section + constraint ops | No |
| US20 | Two-point ruler | CORE | PASS-ARCH: geometric query | No |
| US21 | Closure + STL/GCODE | PROD | OPEN-ALG: orthosis-specific production-body builder | No general B-Rep required |
| US22 | Overall/per-element hardness/density | PROD/DATA | PASS-ARCH: material/stiffness regions | No |
| US23 | PDF report | REPORT | PASS-ARCH | No |
| US24 | Detect <0.8 mm and auto-fix | PROD/CORE | OPEN-ALG: thickness query + DFMFixOperation | No |
| US25 | Save + accidental close protection | DATA | PASS-ARCH | No |

---

## Result

**25/25 EasyCAD2 validation stories have an implementation path in the proposed architecture.**

Geometry-heavy stories US6–US22/US24 do not, based on their documented behavior, force any of the following into P0:

```text
NURBS surface authoring
trimmed B-Rep
STEP/IGES
loft/sweep/revolve feature tree
surface sewing
arbitrary shell/offset
fillet/chamfer kernel
general solid boolean kernel
```

This does **not** prove EasyCAD2 lacks such internal code. It proves only that the validated product behavior does not require us to make those capabilities architectural prerequisites.

---

## Why OpenSubdiv materially changes the inference

Official OpenSubdiv documentation states that it is optimized for interactive evaluation of deforming subdivision surfaces with static topology, using polygonal control cages and a smooth limit surface.

Combined with EasyCAD2 evidence of:

- direct vertex editing;
- smooth heel/arch/wedge deformation;
- element placement on the mesh;
- local sculpt;
- scan-driven deformation;

it is reasonable to use a **stable or mostly stable control cage** as the leading BiomechE-CAD architecture hypothesis.

The exact EasyCAD2 internal topology and formulas remain unknown.

---

## Architecture gates still open

The parity matrix is a functional coverage result, not an implementation proof. Before freezing the stack, BiomechE-CAD still needs to pass:

1. canonical cage topology qualification;
2. extreme heel/arch/wedge deformation without foldover;
3. element blending quality;
4. scan conform stability;
5. production closure/watertight generation;
6. min-thickness auto-fix;
7. deterministic tessellation and STL export;
8. performance on desktop and target WASM/server scenarios if required.

Only failures in these concrete gates should trigger evaluation of additional geometry libraries.
