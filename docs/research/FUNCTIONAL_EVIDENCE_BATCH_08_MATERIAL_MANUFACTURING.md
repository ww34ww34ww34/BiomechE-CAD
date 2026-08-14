# BiomechE-CAD — Functional Evidence Batch 08: Material Durability and Manufacturing

**Date:** 2026-08-14  
**Status:** ACTIVE research baseline — `MAT-001 / MAN-001`  
**Architecture:** intentionally out of scope / parked.  
**Bibliography:** `docs/BIBLIOGRAPHY.md` is authoritative for source metadata and locators.

---

## 0. Purpose

Define what BiomechE-CAD must preserve about **material, processing, manufactured state and service aging** before choosing geometry libraries or implementing material-aware production.

The central conclusion is:

> **A material name is not a mechanical property, and a supplier material is not the same thing as the manufactured orthosis.**

For an orthosis, actual behavior depends on a chain:

```text
BASE MATERIAL / FEEDSTOCK
        +
LAYER / REGION / STRUCTURE
        +
GEOMETRY / THICKNESS
        +
MANUFACTURING PROCESS
        +
POST-PROCESSING
        +
SERVICE / AGING STATE
        ↓
ACTUAL MANUFACTURED RESPONSE
```

This distinction is directly supported by orthotic-material studies showing differences due to density, thickness, stiffness, material combinations, thermal processing and cyclic loading [REF-CAD-094; REF-CAD-095; REF-CAD-096; REF-CAD-097; REF-CAD-099; REF-CAD-100]. Additive-manufacturing standards likewise distinguish feedstock, manufacturing process, part properties, geometry and acceptance [STD-ISOASTM-52901-2017; STD-ISOASTM-52903-1-2020; STD-ISOASTM-52924-2023].

---

# 1. Three property layers — do not collapse them

## 1.1 Nominal material / feedstock

Examples:

```text
EVA
Plastazote / polyethylene foam
PORON / polyurethane
TPU / EPU
PA11 / PA12
custom elastomer
```

A nominal material definition may include supplier/trade name, formulation, density, nominal hardness/modulus and datasheet source.

It does **not** prove that the final orthosis has those same properties.

## 1.2 Manufactured effective property

The actual device response additionally depends on:

```text
thickness
shape
material-stack order
interfaces / adhesive
heat / thermoforming
printing process
build orientation
infill / lattice
wall/shell parameters
post-processing
actual geometry
```

A foot-orthosis measurement study explicitly notes that stiffness, compression set and shape characterize the orthosis and are not defined by material alone [REF-CAD-102].

For lattice/metamaterial insoles, the effective compressive/shear response is deliberately controlled by structure even with the same base elastomer [REF-CAD-098].

## 1.3 Service-aged state

Foams and multilayer materials can change with cyclic or sustained loading. Studies have reported changing stress-strain response, compression set, elastic deformation and/or thickness across repeated loading [REF-CAD-095; REF-CAD-099; REF-CAD-100].

Therefore:

```text
MaterialDefinition
!=
ManufacturedPropertyState
!=
ServiceAgedPropertyState
```

---

# 2. Hardness is useful, but must be semantically strict

`50 Shore` is invalid data unless the scale/method are explicit.

At minimum:

```text
HardnessMeasurement
  value
  scale
  testStandardOrMethod
  instrument
  dwellTime
  specimenThickness
  temperature
  conditioning
  timestamp
```

ISO 868 defines Shore A and Shore D durometer measurement for plastics/ebonite and explicitly notes that the result is empirical, primarily useful for control, with **no simple relationship to a fundamental material property** [STD-ISO-868-2003].

Consequences:

```text
Shore A != Shore D
Shore C != Shore A
Shore hardness != Young modulus
```

BiomechE-CAD SHALL NOT perform an undocumented universal Shore-to-modulus conversion.

Literature can report other hardness scales/durometers; those are retained exactly with their original method. For example, arch-support studies already use Shore C conditions [REF-CAD-017].

---

# 3. Compression response matters more than a single nominal scalar for many cushioning materials

Flexible foams are nonlinear and time/load-history dependent. ISO 3386-1:2025 specifies compression stress-strain characterization for low-density flexible cellular materials [STD-ISO-3386-1-2025]. ISO 1856:2018 provides compression-set methods for flexible cellular materials [STD-ISO-1856-2018].

Orthotic research supports recording multiple mechanical descriptors. Paton et al. tested density, resilience, stiffness, friction, durability and compression set across commonly used diabetic-orthosis materials [REF-CAD-097].

Chatzistergos et al. showed that a cushioning stiffness optimum depended on loading/body mass in the tested setting and that tuning stiffness improved pressure reduction in that cohort [REF-CAD-099]. This supports preserving load-dependent effective stiffness; it does **not** establish a universal material-selection formula.

Recommended semantic layer:

```text
MechanicalPropertySet
  density
  hardness[]
  compressionCurveRef
  effectiveStiffness[]
  resilience / hysteresis
  compressionSet
  shearStiffness
  coefficientOfFriction
  thermal / moisture properties [where relevant]
  testCondition
  evidence/provenance
```

---

# 4. Thickness is a material-system variable, not merely geometry

Pressure attenuation and compression behavior depend on material thickness as well as foam structure/properties [REF-CAD-100]. Systematic review evidence also highlights density, hardness and thickness as relevant but inconsistently reported variables [REF-CAD-094].

Therefore the data model must distinguish:

```text
clinical geometric thickness prescription
material layer thickness
manufactured measured thickness
aged/service thickness
```

A single `thickness_mm` field is insufficient.

---

# 5. Multilayer stacks need order and interface provenance

Orthotic studies frequently test **combinations**, not isolated material names. Brodsky et al. compared multiple dual-density combinations over 100,000 cycles [REF-CAD-095]. Foto and Birke likewise found different degradation behavior among multidensity combinations, with much of the loss occurring early in their 100,000-cycle test [REF-CAD-101].

Store:

```text
MaterialStack
  layers[] ordered foot-side -> shoe-side
    materialDefinitionId
    nominalThickness
    localRegion?
    purpose: CUSHION | SUPPORT | COVER | SHEAR_LAYER | OTHER
  interfaces[]
    adhesive/process
    bondMethod
    postProcess
```

Layer order SHALL survive save/load/report/manufacturing export.

---

# 6. Heat molding / post-processing changes properties

Heating is not an innocuous metadata detail. Brodsky et al. measured commonly used insole materials before and after heating and found the tested heated combinations became stiffer and transmitted maximal load at lower strain [REF-CAD-096].

Consequently:

```text
MaterialDefinition: Plastazote X
```

and

```text
ManufacturedMaterialState:
  Plastazote X
  heatMolded = true
  process profile = ...
```

are distinct states.

Any process that can change mechanical response belongs to the manufacturing provenance:

```text
heating / thermoforming
annealing
curing
adhesive lamination
surface finishing
washing/chemical treatment where relevant
UV/thermal post-cure
```

---

# 7. Fatigue, compression set and service aging are first-class QC concepts

Orthoses experience cyclic loading, so initial mechanical properties alone are insufficient.

Evidence examples:

- dual-density combinations changed differently over 100,000 cycles [REF-CAD-095];
- multidensity materials lost performance during 100,000 cycles, much of it early in the test [REF-CAD-101];
- sustained/cyclic loading of polyethylene foam altered structural/compression behavior and could leave incomplete thickness recovery [REF-CAD-100];
- longitudinal insole studies found physical compression over months does not map trivially onto useful pressure performance, so visual wear alone is not a sufficient replacement criterion [REF-CAD-103].

Relevant current test frameworks include:

```text
ISO 3385:2014    constant-load pounding fatigue
ISO 24999:2008   constant-strain fatigue
ISO 1856:2018    compression set
```

[STD-ISO-3385-2014; STD-ISO-24999-2008; STD-ISO-1856-2018].

These standards are not automatically medical-device acceptance thresholds; they provide reusable test semantics. Product acceptance limits must be tied to a material/process/profile qualification.

---

# 8. Shear/friction and thermal comfort may matter independently of normal pressure

Material selection can influence shear/friction and thermal properties as well as normal-pressure response. Material-testing work in diabetic-foot contexts has explicitly investigated friction, shear, moisture and thermal-comfort behavior [REF-CAD-104]. A daily-use shear-reducing insole study measured pressure, shear and material stiffness prospectively as insoles aged [REF-CAD-105].

Therefore optional material properties should support:

```text
friction coefficient
shear stiffness / shear-force test
moisture absorption
thermal conductivity / thermal comfort test
```

when the use-case requires them.

Do not infer these quantities from Shore hardness or normal-pressure response.

---

# 9. Additive manufacturing: base polymer and printed structure are different layers

For polymer AM, BiomechE-CAD must preserve both feedstock and process/structure state.

ISO/ASTM 52903-1:2020 defines requirements for plastic feedstock used in material-extrusion AM [STD-ISOASTM-52903-1-2020]. ISO/ASTM 52924:2023 classifies polymer AM part quality using mechanical, physical and geometrical properties, reinforcing that **part properties** are the qualification object [STD-ISOASTM-52924-2023].

For regional lattice/metamaterial orthoses, studies show that geometry is deliberately used to generate local effective stiffness [REF-CAD-008; REF-CAD-098]. Therefore:

```text
base resin modulus
!=
effective lattice modulus
```

and:

```text
MaterialRegion
+ StructuralRegion / LatticeRegion
```

must remain separable.

Suggested AM provenance:

```text
AMProcessProfile
  technology
  machineId / model
  machineProfileVersion
  software/slicer/toolpath version

  feedstockMaterialId
  feedstockLot

  buildOrientation
  buildPosition
  coordinateConvention

  layerHeight
  wall/shell parameters
  infill/lattice family
  infill/lattice parameters
  local process parameters

  environmental conditions [when controlled]
  start/end timestamps
  operator

  postProcess[]
```

ISO 17295:2023 standardizes AM part positioning, coordinates and orientation terminology [STD-ISO-17295-2023].

---

# 10. AM quality is a process + part acceptance problem

ISO/ASTM 52901:2017 explicitly structures exchange/acceptance around part-definition data, feedstock, final part characteristics/properties, inspection and acceptance methods [STD-ISOASTM-52901-2017].

ISO/ASTM 52920:2023 addresses qualification of AM processes and production sites [STD-ISOASTM-52920-2023].

ISO/ASTM 52902:2023 provides AM test artefacts for quantitative geometric capability assessment/calibration [STD-ISOASTM-52902-2023].

BiomechE-CAD consequence:

```text
export succeeded
!=
part accepted
```

A produced orthosis can have states such as:

```text
GENERATED
MANUFACTURED
INSPECTED
ACCEPTED
REJECTED
CONDITIONALLY_ACCEPTED
```

and validation depends on the declared manufacturing profile.

---

# 11. CNC / subtractive manufacturing requires the same provenance principle

The evidence/standards above are richer for AM, but the product rule is technology-neutral.

For milling/CNC preserve at least:

```text
material blank definition + lot
blank dimensions / density / hardness where specified
machine / spindle / tooling profile
tool geometry + tool identifier
toolpath/CAM version
fixture/orientation
allowances / offsets
feeds/speeds when part of qualified process
post-processing / manual finishing
actual measured dimensions / QC
```

A CNC-milled EVA orthosis is not fully specified by its final STL or by `EVA` alone.

---

# 12. CAD geometry and manufactured geometry must both exist

Manufacturing introduces a measurable realization error.

The software should support:

```text
DesignGeometryRevision
ManufacturingGeometryTarget
ManufacturedGeometryMeasurement
DeviationMap / key dimensions
```

For AM, ISO/ASTM 52902:2023 is a relevant reference for system-level geometric capability testing [STD-ISOASTM-52902-2023]. Orthosis literature also reports measurable dimensional differences between digitally manufactured and traditional foot orthoses, reinforcing the need for actual-part measurement rather than assuming nominal CAD geometry [REF-CAD-106].

P0 does not need full metrology automation, but the schema needs a home for measured dimensional QC.

---

# 13. Proposed domain model

## 13.1 Material definition

```text
MaterialDefinition
  materialId
  supplier
  tradeName
  formulationCode
  materialFamily
  revision

  nominalDensity
  nominalProperties[]
  datasheetRef

  regulatory/biocompatibility refs [when applicable]
  evidenceRefs[]
```

## 13.2 Material lot / feedstock

```text
MaterialLot
  lotId
  materialId
  supplierLot
  manufactureDate?
  expiryDate?
  receivedDate?
  storageCondition?
  certificateRefs[]
  measuredIncomingProperties[]
```

## 13.3 Material region / stack

```text
MaterialRegion
  regionId
  anatomy/ROI reference
  materialId
  lotId?
  nominalThickness
  intendedRole
  targetPropertyProfile?

MaterialStack
  orderedLayers[]
  interfaces[]
```

## 13.4 Manufactured state

```text
ManufacturedPropertyState
  artifactId
  materialLotRefs[]
  processProfileId
  processRunId

  measuredGeometry
  measuredThicknesses[]
  measuredHardness[]
  measuredCompressionResponse[]
  measuredEffectiveStiffness[]
  measuredDensityMass?
  measuredShear/Friction?

  testEnvironment
  coupon/specimenRefs[]
  dataQuality
```

## 13.5 Service state

```text
ServiceState
  artifactId
  timestamp
  estimatedWearTime?
  estimatedWeightBearingExposure?
  cyclesEstimate?

  visibleWear?
  measuredThicknesses[]
  measuredMechanicalProperties[]
  pressureVerificationRef?
  userExperienceRef?

  disposition
    CONTINUE
    RECHECK
    REPLACE
    UNKNOWN
```

No automatic service-life prediction is P0.

---

# 14. DFM / qualification policy

Each `ManufacturingProfile` defines which checks are mandatory.

Potential classes:

```text
GEOMETRY
  dimensional tolerance
  minimum thickness
  surface / edge checks
  watertight/export integrity

MATERIAL
  identity / lot
  layer thickness
  hardness range
  compression response
  density/mass

PROCESS
  machine/profile
  orientation/tooling
  post-processing

DURABILITY
  cyclic qualification where required
  compression-set limit

FUNCTIONAL
  pressure verification for evidence-linked profiles when required
```

A profile-specific threshold must include:

```text
metric
method
specimen/part location
condition/environment
limit
source/qualification revision
```

---

# 15. Evidence boundaries

The current literature does **not** justify:

```text
one best material for all orthoses
one universal Shore hardness
one universal lifetime in months
one Shore -> modulus formula
one infill percentage -> stiffness formula
one global AM tolerance
one global CNC tolerance
```

The systematic review of orthotic materials found only limited heterogeneous pressure evidence [REF-CAD-094]. Manufacturing/process and durability evidence must therefore be used to make the software **measurable and reproducible**, not to invent unsupported automatic prescriptions.

---

# 16. P0 / P1 / P2 consequence

## P0

```text
material identity + supplier/formulation revision
material lot/feedstock provenance
hardness with scale + method
nominal density / thickness
ordered material stacks + interfaces
material regions distinct from geometry
manufacturing process/profile/version
AM orientation/infill/lattice/process parameters when applicable
CNC material/tooling/CAM provenance when applicable
post-processing provenance
manufactured artifact linked to exact design revision
QC state + declared tolerance/method
service-state data model
```

## P1

```text
coupon/specimen registry
compression stress-strain import
compression set test records
fatigue/cyclic durability qualification
shear/friction tests
actual geometry scan/deviation map
machine/process capability records
multi-material interface QC
wear/aging follow-up dashboard
```

## P2 / R&D

```text
predictive service-life model
automatic replacement recommendation
pressure -> material/stiffness optimization
automatic lattice/property synthesis
closed-loop material calibration from measured outcomes
process digital twin / advanced compensation
```

---

# 17. Acceptance semantics

## Material — `MAT-*`

```text
MAT-001  exact material identity and revision survive round-trip
MAT-002  material lot/feedstock provenance survives round-trip
MAT-003  hardness always stores scale + method; bare numeric hardness is invalid
MAT-004  no silent Shore-to-modulus conversion
MAT-005  density and layer thickness are independent explicit properties
MAT-006  ordered material stack and interface/bond method survive round-trip
MAT-007  base-material and effective structural/lattice properties remain separate
MAT-008  geometry dose and material/mechanical dose remain independently editable
MAT-009  heat/thermoform/post-process state is explicit
MAT-010  measured property includes test method/environment/specimen provenance
MAT-011  initial and service-aged property states remain separate
MAT-012  cyclic/fatigue test retains cycle/load/protocol metadata
MAT-013  compression-set data retains method and conditioning metadata
MAT-014  shear/friction properties are not inferred from normal-pressure/hardness data
MAT-015  material-region anatomy/ROI mapping survives mirror/save/load
MAT-016  material change never silently alters semantic clinical prescription
MAT-017  supplier nominal property is never presented as measured final-part property
MAT-018  evidence-linked material preset retains population/use-case/source context
```

## Manufacturing — `MAN-*`

```text
MAN-001  exact design revision -> manufacturing profile -> artifact lineage
MAN-002  process type/machine/profile/software versions are preserved
MAN-003  feedstock/blank lot is preserved when known/required
MAN-004  AM build orientation/position coordinate convention is explicit
MAN-005  AM infill/lattice/layer/shell parameters survive round-trip
MAN-006  CNC tooling/CAM/fixture provenance survives round-trip
MAN-007  all property-changing post-process steps are versioned
MAN-008  artifact export/hash is immutable and traceable
MAN-009  QC requirement includes metric + method + tolerance + profile revision
MAN-010  generated artifact cannot become ACCEPTED without required QC gates
MAN-011  failed mandatory QC prevents validated-production status
MAN-012  measured manufactured dimensions remain distinct from CAD nominal dimensions
MAN-013  coupon/specimen test data can link to build/run/part
MAN-014  measured final-part properties link to the exact process run
MAN-015  multi-material interfaces/adhesives are traceable
MAN-016  service-state inspection links to the exact physical artifact
MAN-017  replacement/lifetime guidance cannot be emitted without a qualified rule/source
MAN-018  AM/CNC process changes create a new manufacturing-profile revision
```

---

# 18. Conclusion

The material/manufacturing model should make the following chain auditable:

```text
PRESCRIPTION
    ↓
DESIGN GEOMETRY
    ↓
MATERIAL / STACK / REGION
    ↓
PROCESS PROFILE + LOT + POST-PROCESS
    ↓
PHYSICAL ARTIFACT
    ↓
QC / ACTUAL PROPERTIES
    ↓
SERVICE AGING
    ↓
PRESSURE + PROM + ADHERENCE OUTCOME
```

This is independent of OpenSubdiv, ON_SubD or any eventual geometry kernel.

The next project step after this batch is to promote mature evidence from Batches 03–08 into the consolidated functional specification, then derive `Project Schema v0` and a kernel-independent acceptance suite.

---

## Bibliography links

[REF-CAD-008]: ../BIBLIOGRAPHY.md#ref-cad-008
[REF-CAD-017]: ../BIBLIOGRAPHY.md#ref-cad-017
[REF-CAD-094]: ../BIBLIOGRAPHY.md#ref-cad-094
[REF-CAD-095]: ../BIBLIOGRAPHY.md#ref-cad-095
[REF-CAD-096]: ../BIBLIOGRAPHY.md#ref-cad-096
[REF-CAD-097]: ../BIBLIOGRAPHY.md#ref-cad-097
[REF-CAD-098]: ../BIBLIOGRAPHY.md#ref-cad-098
[REF-CAD-099]: ../BIBLIOGRAPHY.md#ref-cad-099
[REF-CAD-100]: ../BIBLIOGRAPHY.md#ref-cad-100
[REF-CAD-101]: ../BIBLIOGRAPHY.md#ref-cad-101
[REF-CAD-102]: ../BIBLIOGRAPHY.md#ref-cad-102
[REF-CAD-103]: ../BIBLIOGRAPHY.md#ref-cad-103
[REF-CAD-104]: ../BIBLIOGRAPHY.md#ref-cad-104
[REF-CAD-105]: ../BIBLIOGRAPHY.md#ref-cad-105
[REF-CAD-106]: ../BIBLIOGRAPHY.md#ref-cad-106
[STD-ISO-868-2003]: ../BIBLIOGRAPHY.md#std-iso-868-2003
[STD-ISO-1856-2018]: ../BIBLIOGRAPHY.md#std-iso-1856-2018
[STD-ISO-3385-2014]: ../BIBLIOGRAPHY.md#std-iso-3385-2014
[STD-ISO-24999-2008]: ../BIBLIOGRAPHY.md#std-iso-24999-2008
[STD-ISO-3386-1-2025]: ../BIBLIOGRAPHY.md#std-iso-3386-1-2025
[STD-ISOASTM-52901-2017]: ../BIBLIOGRAPHY.md#std-isoastm-52901-2017
[STD-ISOASTM-52902-2023]: ../BIBLIOGRAPHY.md#std-isoastm-52902-2023
[STD-ISOASTM-52903-1-2020]: ../BIBLIOGRAPHY.md#std-isoastm-52903-1-2020
[STD-ISOASTM-52920-2023]: ../BIBLIOGRAPHY.md#std-isoastm-52920-2023
[STD-ISOASTM-52924-2023]: ../BIBLIOGRAPHY.md#std-isoastm-52924-2023
[STD-ISO-17295-2023]: ../BIBLIOGRAPHY.md#std-iso-17295-2023
