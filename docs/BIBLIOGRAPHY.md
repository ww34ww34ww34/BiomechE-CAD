# BiomechE-CAD — Canonical Bibliography

**Status:** CANONICAL  
**Date initialized:** 2026-08-14  
**Purpose:** single authoritative bibliography for EasyCAD2 evidence, scientific literature, guidelines, vendor sources and architecture references used by BiomechE-CAD.

> Other project documents should cite the stable source IDs defined here instead of duplicating bibliographic metadata. `docs/research/SOURCES.md` is an intake/research ledger; this file is the canonical bibliographic authority.

---

## 0. Citation policy

### 0.1 Stable IDs

Use stable IDs in prose:

```text
[EC2-MANUAL-1.1, pp. 31–35]
[REF-CAD-013, pp. 84–88]
[REF-CAD-004, Abstract—Results]
[GUIDE-IWGDF-2023, Prevention recommendation/context]
```

Multiple references:

```text
[REF-CAD-004; REF-CAD-005; REF-CAD-007]
```

### 0.2 Locator hierarchy

Prefer the most precise locator available:

1. exact PDF/book/manual page(s);
2. article page(s), table, figure or numbered section;
3. HTML section heading;
4. PubMed/PMC abstract subsection (`Methods`, `Results`, `Conclusions`) when full-text pagination is not available;
5. whole-source citation only when no finer locator has yet been captured.

**Rule:** never invent an exact page number. If only an abstract or HTML section was inspected, record that fact explicitly.

### 0.3 Markdown linking convention

Documents under `docs/spec/`, `docs/research/`, or `docs/validation/` may use Markdown reference links:

```markdown
Pressure-informed design improved targeted offloading [REF-CAD-004].

[REF-CAD-004]: ../BIBLIOGRAPHY.md#ref-cad-004
```

A concept derived from a specific manual page should include the locator in prose:

```markdown
EasyCAD2 exposes element placement and custom editing [EC2-MANUAL-1.1, pp. 31–35].

[EC2-MANUAL-1.1]: ../BIBLIOGRAPHY.md#ec2-manual-11
```

### 0.4 Evidence integrity

A citation means only that the cited source supports the adjacent statement at the stated level of specificity. Population-specific, protocol-specific, model-based and vendor claims must remain labelled as such.

---

# A. Primary EasyCAD2 sources

<a id="ec2-manual-11"></a>
## EC2-MANUAL-1.1 — EasyCAD2 Manuale ITA 2.0

- **Title:** EasyCAD2 — Manuale d'uso / `Easycad2 Manuale ITA 2.0`
- **Source type:** primary product manual
- **Software version shown:** `1.1.x.x`
- **Document date:** 13/01/2024
- **Canonical URL:** https://drive.google.com/file/d/148X366g4e47cYOWtFWP-jeMqavSJqHTa/view
- **Locator map:**
  - pp. 7–12 — database/settings
  - p. 13 — navigation/multi-select
  - p. 14 — side/mirror
  - pp. 15–18 — DIMA/templates/dimensions
  - pp. 19–20 — plantar pressure import/registration
  - pp. 21–22 — Scan3D
  - p. 23 — Scan2D
  - pp. 24–30 — MODIFICA: thickness/flatten/heel/arch/wedge/smoothing
  - pp. 31–35 — ELEMENTI/custom element editing/integration
  - pp. 36–40 — POST PROCESSING/sculpt/global deformation/ROI
  - pp. 42–44 — CONTROLLO/sections/measurements
  - pp. 44–50 — PRODUCI/closure/STL/GCODE
  - pp. 50–52 — toolbar/history/measurement
  - pp. 52–53 — minimum-thickness warning/safe close
- **Project role:** behavioral baseline and exact UI/feature/page evidence.
- **Rights note:** do not redistribute PDF/screenshots in the public repository without explicit rights clearance.

<a id="ec2-val-plan-14"></a>
## EC2-VAL-PLAN-1.4 — EasyCAD2 software validation plan

- **Title:** PdV0001 — EasyCAD2 software validation plan / Piano di validazione software EasyCAD2
- **Source type:** primary validation plan
- **Target software:** EasyCAD2 `1.4.x.x`
- **Document version:** 1
- **Last update:** 15/01/2026
- **Canonical URL:** https://drive.google.com/file/d/19Pdjn76a6sAEcnUTut2qL0qzvfkniD4v/view
- **Locator:** user stories US1–US25; cite story number in addition to page when possible, e.g. `[EC2-VAL-PLAN-1.4, US13]`.
- **Project role:** authoritative validated-behavior inventory.

<a id="ec2-val-report-14"></a>
## EC2-VAL-REPORT-1.4 — EasyCAD2 validation report

- **Title:** RdT001 — Rapporto di Test di validazione software EasyCAD2 versione 1.4.x.x
- **Source type:** primary validation report
- **Compilation date:** 20/01/2026
- **Canonical URL:** https://drive.google.com/file/d/1kbDKQd6qskQH1MyZ5O3Y-WYt5p_7qRlJ/view
- **Locator:** report result table / test result section.
- **Recorded result:** 25 planned, 25 executed, 25 PASS, 0 FAIL, 0 BLOCKED.
- **Project role:** confirms successful execution of the 25-story validation baseline; does not reveal proprietary algorithms.

---

# B. Clinical guideline / consensus sources

<a id="guide-iwgdf-2023"></a>
## GUIDE-IWGDF-2023 — IWGDF Guidelines 2023

- **Title:** International Working Group on the Diabetic Foot (IWGDF) Guidelines 2023 — Prevention / Offloading guideline set
- **Source type:** international clinical guideline
- **Official landing page:** https://iwgdfguidelines.org/guidelines-2023/
- **Related publication:** Bus SA et al. *Guidelines on the prevention of foot ulcers in persons with diabetes (IWGDF 2023 update).* Diabetes Metab Res Rev. DOI `10.1002/dmrr.3651`.
- **Locator:** cite the named guideline, recommendation or section; do not cite generic project-wide thresholds without the population/protocol context.
- **Project role:** evidence that quantitative offloading targets may exist for specific diabetic-foot use cases; thresholds are not universal CAD defaults.

---

# C. Scientific literature

<a id="ref-cad-001"></a>
## REF-CAD-001 — Rearfoot posting dose response

- **Citation:** Telfer S, Abbott M, Steultjens MPM, Woodburn J. *Dose-response effects of customised foot orthoses on lower limb kinematics and kinetics in pronated foot type.* J Biomech. 2013;46(9):1489–1495.
- **PMID:** `23631857`
- **DOI:** `10.1016/j.jbiomech.2013.03.036`
- **Locator:** pp. 1489–1495; PubMed Abstract—Methods/Results records 2° rearfoot-post increments from 6° lateral to 10° medial and significant linear effects.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/23631857/
- **Project role:** wedge/posting must remain an explicit numerical prescription dose.

<a id="ref-cad-002"></a>
## REF-CAD-002 — 3D scanning methods

- **Citation:** Farhan M et al. *Comparison of 3D scanning versus traditional methods of capturing foot and ankle morphology for the fabrication of orthoses: a systematic review.* J Foot Ankle Res. 2021;14(1):2.
- **PMID:** `33413570`
- **DOI:** `10.1186/s13047-020-00442-8`
- **Locator:** full article / Abstract—Results and Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/33413570/
- **Project role:** scan provenance, acquisition protocol and QC.

<a id="ref-cad-003"></a>
## REF-CAD-003 — 3D foot-shape methodology/reporting

- **Citation:** Allan JJ et al. *Methodological and statistical approaches for the assessment of foot shape using three-dimensional foot scanning: a scoping review.* J Foot Ankle Res. 2023.
- **PMID:** `37106385`
- **DOI:** `10.1186/s13047-023-00617-z`
- **Locator:** full article; reporting-checklist / methodology sections.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/37106385/
- **Project role:** scanner, markers, weight-bearing and protocol metadata.

<a id="ref-cad-004"></a>
## REF-CAD-004 — Shape + pressure custom insole design

- **Citation:** Owings TM, Woerner JL, Frampton JD, Cavanagh PR, Botek G. *Custom therapeutic insoles based on both foot shape and plantar pressure measurement provide enhanced pressure relief.* Diabetes Care. 2008;31(5):839–844.
- **PMID:** `18252899`
- **DOI:** `10.2337/dc07-2288`
- **Locator:** pp. 839–844; PubMed Abstract—Results: 64/70 high-pressure regions better unloaded; peak pressure lower by 32% and 21% vs two shape-only conditions; FTI also reduced, with load transfer to midfoot.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/18252899/
- **Project role:** quantitative pressure-informed design, target ROI plus redistribution assessment.

<a id="ref-cad-005"></a>
## REF-CAD-005 — Pressure-guided iterative optimization

- **Citation:** Bus SA et al. *Evaluation and optimization of therapeutic footwear for neuropathic diabetic foot patients using in-shoe plantar pressure analysis.* Diabetes Care. 2011.
- **PMID:** `21610125`
- **DOI:** `10.2337/dc10-2206`
- **Locator:** PubMed Abstract—Results; full-text locator to be captured if needed.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/21610125/
- **Project role:** measure → modify → remeasure loop.

<a id="ref-cad-006"></a>
## REF-CAD-006 — IWGDF prevention publication

- **Citation:** Bus SA et al. *Guidelines on the prevention of foot ulcers in persons with diabetes (IWGDF 2023 update).* Diabetes Metab Res Rev. 2024.
- **DOI:** `10.1002/dmrr.3651`
- **Locator:** guideline recommendation/context; use `GUIDE-IWGDF-2023` for the guideline set.
- **Project role:** context-bound outcome targets.

<a id="ref-cad-007"></a>
## REF-CAD-007 — Offloading design features systematic review

- **Title:** *Footwear and insole design features for offloading the diabetic at risk foot — A systematic review and meta-analyses.*
- **PMID:** `33532602`
- **Locator:** PubMed Abstract/Results and full article where available.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/33532602/
- **Project role:** arch profiles, metatarsal additions/apertures, pressure-informed design and evidence heterogeneity.

<a id="ref-cad-008"></a>
## REF-CAD-008 — Pressure-based 3D printed accommodative insole

- **Citation:** Muir BC et al. *Evaluation of novel plantar pressure-based 3-dimensional printed accommodative insoles — A feasibility study.* Clin Biomech. 2022;98:105739.
- **PMID:** `35987171`
- **DOI:** `10.1016/j.clinbiomech.2022.105739`
- **Locator:** article 105739 / PubMed Abstract.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/35987171/
- **Project role:** pressure-derived offloading ROI and personalized mechanical-property direction.

<a id="ref-cad-009"></a>
## REF-CAD-009 — Orthosis stiffness in flexible flatfoot

- **Citation:** Cherni Y et al. *Effect of 3D printed foot orthoses stiffness on muscle activity and plantar pressures in individuals with flexible flatfeet.* Clin Biomech. 2022;92:105553.
- **PMID:** `34973589`
- **DOI:** `10.1016/j.clinbiomech.2021.105553`
- **Locator:** article 105553 / PubMed Abstract—Results.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/34973589/
- **Project role:** stiffness as an independent prescription/manufacturing variable.

<a id="ref-cad-010"></a>
## REF-CAD-010 — Stiffness/design/posting effects

- **Citation:** Desmyttere G et al. *Effect of 3D printed foot orthoses stiffness and design on foot kinematics and plantar pressures in healthy people.* Gait Posture. 2020.
- **PMID:** `32818861`
- **DOI:** `10.1016/j.gaitpost.2020.07.146`
- **Locator:** PubMed Abstract—Results.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/32818861/
- **Project role:** geometry and stiffness have region-specific biomechanical effects.

<a id="ref-cad-011"></a>
## REF-CAD-011 — Central metatarsal pressure meta-analysis

- **Citation:** Ruiz-Ramos M et al. *Effectiveness of bespoke or customised orthotic treatment in plantar pressure reduction of the central metatarsals: a systematic review and meta-analysis.* J Orthop. 2024;59:111–118.
- **PMID:** `39399760`
- **DOI:** `10.1016/j.jor.2023.12.006`
- **Locator:** pp. 111–118 / Results and Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/39399760/
- **Project role:** first-class metatarsal pressure-redistribution capability.

<a id="ref-cad-012"></a>
## REF-CAD-012 — Forefoot pressure systematic review 2026

- **Citation:** Thiaspras L et al. *Foot orthoses for forefoot pressure reduction and the hypothesized role in calf muscle stretching: A systematic review highlighting an evidence gap.* Foot. 2026;67:102251.
- **PMID:** `41931962`
- **DOI:** `10.1016/j.foot.2026.102251`
- **Locator:** article 102251; PubMed Abstract—Results/Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/41931962/
- **Project role:** forefoot loading, PTI and metatarsal/soft-contoured designs.

<a id="ref-cad-013"></a>
## REF-CAD-013 — Metatarsal pad placement in diabetic neuropathy

- **Citation:** Hastings MK, Mueller MJ, Pilgram TK, Lott DJ, Commean PK, Johnson JE. *Effect of metatarsal pad placement on plantar pressure in people with diabetes mellitus and peripheral neuropathy.* Foot Ankle Int. 2007;28(1):84–88.
- **PMID:** `17257544`
- **DOI:** `10.3113/FAI.2007.0015`
- **Locator:** pp. 84–88; PubMed Abstract—Results: placements 6.1–10.6 mm proximal to MTH line consistently reduced pressure in the studied population; too-distal placement could increase it.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/17257544/
- **Project role:** anatomical placement is a measurable dose/reference-frame variable, not a cosmetic transform.

<a id="ref-cad-014"></a>
## REF-CAD-014 — Hallux-valgus metatarsal pad placement

- **Citation:** Hakukawa S et al. *Optimal placement of metatarsal pads for patients with hallux valgus based on plantar pressure measurement.* Foot Ankle Surg. 2026;32(2):131–138.
- **PMID:** `40707294`
- **DOI:** `10.1016/j.fas.2025.07.005`
- **Locator:** pp. 131–138; PubMed Abstract—Results: 76% foot-length placement reduced central metatarsal pressure in the studied cohort.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/40707294/
- **Project role:** population-specific evidence that normalized placement matters.

<a id="ref-cad-015"></a>
## REF-CAD-015 — Forefoot wedge dose response

- **Title:** *Dose-response effects of forefoot and arch orthotic components on the center of pressure trajectory during running in pronated feet.*
- **PMID:** `34864487`
- **Locator:** PubMed Abstract—Methods/Results.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/34864487/
- **Project role:** preserve forefoot wedge angle/direction as an explicit dose.

<a id="ref-cad-016"></a>
## REF-CAD-016 — Insole configurations: pressure vs convenience

- **Citation:** Guldemond NA et al. *The effects of insole configurations on forefoot plantar pressure and walking convenience in diabetic patients with neuropathic feet.* Clin Biomech. 2007;22(1):81–87.
- **PMID:** `17046124`
- **DOI:** `10.1016/j.clinbiomech.2006.08.004`
- **Locator:** pp. 81–87; PubMed Abstract—Findings/Interpretation.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/17046124/
- **Project role:** combination effects and pressure-benefit vs comfort trade-off.

<a id="ref-cad-017"></a>
## REF-CAD-017 — Arch-support hardness

- **Title:** *Biomechanical effects of varying arch support hardness in foot orthosis for adults with flexible flatfoot: A comprehensive Bayesian statistical analysis.*
- **PMID:** `41455151`
- **DOI:** `10.1016/j.gaitpost.2025.110085`
- **Locator:** PubMed Abstract—Results/Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/41455151/
- **Project role:** hardness/stiffness is a dose separate from geometry; effects may plateau or shift loads.

<a id="ref-cad-018"></a>
## REF-CAD-018 — Heel plug custom foot orthosis

- **Citation:** Balsdon ME, Dombroski CE. *Custom-made foot orthoses with and without heel plugs and their effect on treatment outcomes and plantar pressures in patients with plantar fasciitis.*
- **PMID:** `40366378`
- **DOI:** `10.1097/PXR.0000000000000450`
- **Locator:** PubMed Abstract—Results.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/40366378/
- **Project role:** separate heel containment geometry from cushioning/material relief.

<a id="ref-cad-019"></a>
## REF-CAD-019 — Heel cup/arch pressure redistribution

- **Title:** *Effects of a range of 6 prefabricated orthotic insole designs on plantar pressure in a healthy population.*
- **PMID:** `39140763`
- **DOI:** `10.1097/PXR.0000000000000292`
- **Locator:** PubMed Abstract—Results.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/39140763/
- **Project role:** heel cup/arch design features and regional pressure/contact-area effects.

<a id="ref-cad-020"></a>
## REF-CAD-020 — Inter-individual offloading response

- **Title:** *Pressure relief and load redistribution by custom-made insoles in diabetic patients with neuropathy and foot deformity.*
- **PMID:** `15234488`
- **Locator:** PubMed Abstract—Results: 7/21 successful, 7/21 moderate, 7/21 inadequate first-MTH offloading; increased medial-midfoot load.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/15234488/
- **Project role:** patient-specific verification and target-plus-neighbour load-transfer analysis.

<a id="ref-cad-021"></a>
## REF-CAD-021 — Graded stiffness heel offloading

- **Title:** *Graded stiffness offloading insoles better redistribute heel plantar pressure to protect the diabetic neuropathic foot.*
- **PMID:** `36706604`
- **Locator:** PubMed Abstract / full text when needed.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/36706604/
- **Project role:** regional stiffness and perimeter-load management.

<a id="ref-cad-022"></a>
## REF-CAD-022 — Gradient lattice mapping 2026

- **Citation:** Wang Lihong et al. *Optimization of pressure relief in gradient lattice orthotic insoles based on plantar pressure-rod diameter mapping.* Med Eng Phys. 2026.
- **PMID:** `42049041`
- **DOI:** `10.1088/1873-4030/ae6593`
- **Locator:** PubMed Abstract / modeling-method section when full text is consulted.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/42049041/
- **Project role:** R&D evidence for pressure → regional modulus/lattice mapping; not a clinical rule.

<a id="ref-cad-023"></a>
## REF-CAD-023 — Partition TPMS lattice 2026

- **Title:** *Design of novel orthotic insoles based on partition infilling of TPMS structures.*
- **PMID:** `42147489`
- **Locator:** PubMed Abstract / full text when needed.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/42147489/
- **Project role:** R&D evidence for region-specific lattice structures.

<a id="ref-cad-024"></a>
## REF-CAD-024 — 3D printed orthoses clinical outcomes systematic review

- **Citation:** Atallah H et al. *The current state of 3D-printed orthoses clinical outcomes: a systematic review.* BMC Musculoskelet Disord. 2025.
- **PMID:** `40890671`
- **DOI:** `10.1186/s12891-025-09070-4`
- **Locator:** full article / Abstract—Results and Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/40890671/
- **Project role:** manufacturing/clinical feasibility, comfort/fit and evidence limitations.

<a id="ref-cad-025"></a>
## REF-CAD-025 — Assistive-device adherence

- **Title:** *Patient Compliance With Wearing Lower Limb Assistive Devices: A Scoping Review.*
- **PMID:** `35753880`
- **DOI:** `10.1016/j.jmpt.2022.04.003`
- **Locator:** PubMed Abstract / review results.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/35753880/
- **Project role:** fit/comfort/device properties and adherence.

<a id="ref-cad-026"></a>
## REF-CAD-026 — PROM landscape

- **Title:** *Patient reported outcome measures in the foot and ankle literature: A systematic review.*
- **PMID:** `41033023`
- **DOI:** `10.1016/j.foot.2025.102209`
- **Locator:** PubMed Abstract / full review when needed.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/41033023/
- **Project role:** avoid inventing one proprietary universal outcome score.

<a id="ref-cad-027"></a>
## REF-CAD-027 — Adult flatfoot evidence uncertainty

- **Title:** *Evidence for foot orthoses for adults with flatfoot: a systematic review.*
- **PMID:** `34844639`
- **Locator:** PubMed Abstract—Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/34844639/
- **Project role:** evidence heterogeneity; avoid universal arch/orthosis claims.

<a id="ref-cad-028"></a>
## REF-CAD-028 — Flexible flatfoot patient-reported outcomes

- **Title:** *Foot orthoses for flexible flatfeet in children and adults: a systematic review and meta-analysis of patient-reported outcomes.*
- **PMID:** `36611153`
- **DOI:** `10.1186/s12891-022-06044-8`
- **Locator:** full article / Abstract—Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/36611153/
- **Project role:** population-specific outcomes and uncertainty.

<a id="ref-cad-029"></a>
## REF-CAD-029 — Local offloading and neighbouring load transfer

- **Citation:** Shuang J et al. *The effect of calcaneus and metatarsal head offloading insoles on healthy subjects' gait kinematics, kinetics, asymmetry, and the implications for plantar pressure management: A pilot study.* PLoS One. 2024;19(5):e0303826.
- **PMID:** `38758937`
- **PMCID:** `PMC11101073`
- **DOI:** `10.1371/journal.pone.0303826`
- **Locator:** article e0303826; PubMed Abstract—Results/Conclusion; Fig. 1 for aperture configuration and Fig. 6 for ROI pressure/PTI.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/38758937/
- **Project role:** target ROI improvement may transfer load to surrounding regions; motivates safety-ring analysis.

<a id="ref-cad-030"></a>
## REF-CAD-030 — Reduction and redistribution using orthoses

- **Citation:** Kato H et al. *The reduction and redistribution of plantar pressures using foot orthoses in diabetic patients.* Diabetes Res Clin Pract. 1996;31(1–3):115–118.
- **PMID:** `8792110`
- **DOI:** `10.1016/0168-8227(96)01214-4`
- **Locator:** pp. 115–118; PubMed Abstract—Results: peak pressure reduction and increased contact area.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/8792110/
- **Project role:** total-contact redistribution and contact-area outcome.

<a id="ref-cad-031"></a>
## REF-CAD-031 — Rigid relief orthosis

- **Citation:** Novick A et al. *Reduction of plantar pressure with the rigid relief orthosis.* J Am Podiatr Med Assoc. 1993;83(3):115–122.
- **PMID:** `8468692`
- **DOI:** `10.7547/87507315-83-3-115`
- **Locator:** pp. 115–122; PubMed Abstract—Results notes first-MTH reduction plus changes at heel, midfoot and third MTH.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/8468692/
- **Project role:** local relief interacts with total-contact support and secondary regions.

<a id="ref-cad-032"></a>
## REF-CAD-032 — Pad shape can worsen peak pressure

- **Citation:** Nordsiden L et al. *The effect of 3 foot pads on plantar pressure of pes planus foot type.* J Sport Rehabil. 2010;19(1):71–85.
- **PMID:** `20231746`
- **DOI:** `10.1123/jsr.19.1.71`
- **Locator:** pp. 71–85; PubMed Abstract—Results: dome reduced MPP/PPP, U-pad reduced MPP, donut pad increased PPP in the tested cohort/activity.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/20231746/
- **Project role:** no relief primitive is intrinsically therapeutic or safe.

<a id="ref-cad-033"></a>
## REF-CAD-033 — Peak pressure vs pressure-time integral

- **Title:** *The value of reporting pressure-time integral data in addition to peak pressure data in studies on the diabetic foot: a systematic review.*
- **PMID:** `23273847`
- **DOI:** `10.1016/j.clinbiomech.2012.12.002`
- **Locator:** PubMed Abstract—Findings: clear differences between PTI and peak-pressure results in 15/35 eligible papers.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/23273847/
- **Project role:** retain PTI in addition to peak pressure.

<a id="ref-cad-034"></a>
## REF-CAD-034 — In-shoe plantar pressure measurement technology

- **Citation:** Castro-Martins P et al. *In-shoe plantar pressure measurement technologies for the diabetic foot: A systematic review.* Heliyon. 2024;10(9):e29672.
- **PMID:** `38699042`
- **PMCID:** `PMC11064085`
- **DOI:** `10.1016/j.heliyon.2024.e29672`
- **Locator:** article e29672; Abstract—Results/Conclusion; figures on sensor technologies/configurations.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/38699042/
- **Project role:** device/calibration/protocol provenance and device heterogeneity.

<a id="ref-cad-035"></a>
## REF-CAD-035 — In-shoe measurement reliability, steps and speed

- **Citation:** Kernozek TW, LaMott EE, Dancisak MJ. *Reliability of an in-shoe pressure measurement system during treadmill walking.* Foot Ankle Int. 1996;17(4):204–209.
- **PMID:** `8696496`
- **DOI:** `10.1177/107110079601700404`
- **Locator:** pp. 204–209; PubMed Abstract—Results: speed changes regional loading; up to eight steps were needed for >0.90 reliability across selected variables/regions in this protocol.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/8696496/
- **Project role:** trial provenance, gait speed and step-count awareness.

<a id="ref-cad-036"></a>
## REF-CAD-036 — Cross-system plantar-pressure comparability

- **Citation:** Chockalingam N, Giacomozzi C, Healy A, Sacco ICN. *Discrepancies between plantar pressure devices: Evaluating cross-system reliability for biomechanics, clinical use and predictive modelling.* Foot. 2025;64:102190.
- **PMID:** `40743570`
- **DOI:** `10.1016/j.foot.2025.102190`
- **Locator:** article 102190; PubMed Abstract—Results/Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/40743570/
- **Project role:** cross-device comparison warnings and calibration/protocol metadata.

<a id="ref-cad-037"></a>
## REF-CAD-037 — In-shoe pressure thresholds review

- **Citation:** Jones P et al. *In-shoe pressure thresholds for people with diabetes and neuropathy at risk of ulceration: A systematic review.* J Diabetes Complications. 2021;35(3):107815.
- **PMID:** `33280984`
- **DOI:** `10.1016/j.jdiacomp.2020.107815`
- **Locator:** article 107815; PubMed Abstract—Results/Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/33280984/
- **Project role:** thresholds are heterogeneous, limited-evidence and context-bound.

<a id="ref-cad-038"></a>
## REF-CAD-038 — Plantar pressure thresholds systematic review 2024

- **Citation:** Castro-Martins P et al. *Plantar pressure thresholds as a strategy to prevent diabetic foot ulcers: A systematic review.* Heliyon. 2024;10(4):e26161.
- **PMID:** `38390156`
- **PMCID:** `PMC10882031`
- **DOI:** `10.1016/j.heliyon.2024.e26161`
- **Locator:** article e26161; PubMed Abstract—Results/Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/38390156/
- **Project role:** threshold values vary with device, ROI and protocol; no universal project constant.

<a id="ref-cad-039"></a>
## REF-CAD-039 — Plantar shear measurement technologies

- **Citation:** Rajala S, Lekkala J. *Plantar shear stress measurements — A review.* Clin Biomech. 2014;29(5):475–483.
- **PMID:** `24820135`
- **DOI:** `10.1016/j.clinbiomech.2014.04.009`
- **Locator:** pp. 475–483; PubMed Abstract—Background/Findings.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/24820135/
- **Project role:** shear is distinct from normal pressure and has different measurement technology.

<a id="ref-cad-040"></a>
## REF-CAD-040 — Plantar shear in diabetic foot

- **Citation:** Jones AD et al. *Plantar shear stress in the diabetic foot: A systematic review and meta-analysis.* Diabet Med. 2022;39(1):e14661.
- **PMID:** `34324731`
- **DOI:** `10.1111/dme.14661`
- **Locator:** article e14661; PubMed Abstract—Aims/Methods/Results.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/34324731/
- **Project role:** support measured shear as a distinct outcome; never silently infer it from pressure-only data.

<a id="ref-cad-041"></a>
## REF-CAD-041 — Metatarsal domes in older people with forefoot pain

- **Citation:** Landorf KB et al. *Effects of metatarsal domes on plantar pressures in older people with a history of forefoot pain.* J Foot Ankle Res. 2020;13(1):18.
- **PMID:** `32375847`
- **PMCID:** `PMC7201604`
- **DOI:** `10.1186/s13047-020-00388-x`
- **Locator:** article 18; Abstract—Methods/Results/Conclusions: positions at 5 mm proximal, inline and 5 mm distal were tested; proximal placement gave the best balance in this cohort.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/32375847/
- **Project role:** placement and pad type/density matter; evidence-linked preset only.

<a id="ref-cad-042"></a>
## REF-CAD-042 — Metatarsal pad position in metatarsalgia

- **Citation:** Hsi WL, Kang JH, Lee XX. *Optimum position of metatarsal pad in metatarsalgia for pressure relief.* Am J Phys Med Rehabil. 2005;84(7):514–520.
- **PMID:** `15973088`
- **DOI:** `10.1097/01.phm.0000167680.70092.29`
- **Locator:** pp. 514–520; PubMed Abstract—Results/Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/15973088/
- **Project role:** relative position to MTH pressure peak is clinically meaningful.

<a id="ref-cad-043"></a>
## REF-CAD-043 — Forefoot pressure-relieving orthosis comparison

- **Title:** *Comparison of the Forefoot Pressure-Relieving Effects of Foot Orthoses.*
- **PMID:** `36031787`
- **Locator:** PubMed Abstract—Methods/Results; full-text page locator to capture if needed.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/36031787/
- **Project role:** pad concept/placement and cushioning should be compared by measured effect, not presence alone.

<a id="ref-cad-044"></a>
## REF-CAD-044 — Rheumatoid arthritis: metatarsal bar/dome pressure and pain

- **Citation:** Hodge MC, Bach TM, Carter GM. *Orthotic management of plantar pressure and pain in rheumatoid arthritis.* Clin Biomech. 1999;14(8):567–575.
- **PMID:** `10521640`
- **DOI:** `10.1016/S0268-0033(99)00034-0`
- **Locator:** pp. 567–575; PubMed Abstract—Results/Conclusions.
- **URL:** https://pubmed.ncbi.nlm.nih.gov/10521640/
- **Project role:** bar/dome designs affect pressure and pain; subjective outcome may differ from pressure alone.

---

# D. Vendor / market sources

<a id="vendor-sensormedica-easycad2"></a>
## VENDOR-SENSORMEDICA-EASYCAD2

- **Page title:** Sensor Medica — EasyCAD2
- **Source type:** vendor/product page
- **URL:** https://www.sensormedica.com/en/easycad-2/
- **Locator:** page section by feature heading; capture exact section when cited.
- **Use:** market/product description only; not scientific evidence.

<a id="vendor-sensormedica-insole"></a>
## VENDOR-SENSORMEDICA-INSOLE

- **Page title:** Sensor Medica — easyCAD Insole
- **URL:** https://www.sensormedica.com/en/easycad-insole/
- **Use:** vendor workflow/product claims only.

<a id="vendor-sensormedica-vulcan"></a>
## VENDOR-SENSORMEDICA-VULCAN

- **Page title:** Sensor Medica — Vulcan CNC
- **URL:** https://www.sensormedica.com/it/vulcan-cnc/
- **Use:** manufacturing/CNC market reference.

---

# E. Architecture references — currently parked

Architecture references are preserved because they may later be needed for the kernel shoot-out, but they must not be used as scientific justification for a clinical/product feature.

<a id="arch-opensubdiv"></a>
## ARCH-OPENSUBDIV

- **Title/page:** Pixar OpenSubdiv documentation
- **URLs:** https://opensubdiv.org/ ; https://opensubdiv.org/docs/intro.html ; https://opensubdiv.org/docs/subdivision_surfaces.html
- **Locator:** cite exact documentation page/section when architecture work resumes.
- **Use:** SubD implementation research only.

<a id="arch-opennurbs"></a>
## ARCH-OPENNURBS

- **Title/page:** McNeel openNURBS / `ON_SubD` source and public API
- **URL:** https://github.com/mcneel/opennurbs
- **Use:** geometry-foundation/interoperability research only.
- **Important locator:** `opennurbs_subd_data.h` explicitly marks unstable internal SubD core definitions as unsuitable for application code; cite exact source line/commit during shoot-out documentation.

<a id="arch-rhino3dm"></a>
## ARCH-RHINO3DM

- **Title/page:** McNeel rhino3dm
- **URL:** https://github.com/mcneel/rhino3dm
- **Use:** .NET/JS/WASM openNURBS interoperability research.

<a id="arch-manifold"></a>
## ARCH-MANIFOLD

- **Title/page:** Manifold geometry library
- **URL:** https://github.com/elalish/manifold
- **Use:** conditional solid-mesh/manufacturing research.

<a id="arch-occt"></a>
## ARCH-OCCT

- **Title/page:** Open CASCADE Technology documentation
- **URLs:** https://dev.opencascade.org/doc/overview/html/index.html ; https://github.com/Open-Cascade-SAS/OCCT
- **Use:** optional STEP/IGES/exact B-Rep/general-CAD adapter research.

---

# F. Bibliography maintenance rules

1. **Add the source here before relying on it in a canonical specification.**
2. Never reuse an ID for a different source.
3. Correct metadata here, not independently in every specification.
4. A source may have several concept locators; append them to the entry rather than creating duplicate IDs.
5. Exact page locators are mandatory for EasyCAD2/manual/PDF evidence whenever available.
6. For scientific web/abstract evidence, use a truthful section locator (`Abstract—Results`, `Fig. 6`, etc.) until exact full-text pages are captured.
7. When a full text is later acquired, enrich the existing entry with exact page/table/figure locators; do not change the source ID.
8. Vendor material is evidence of market functionality, **not** scientific efficacy.
9. Architecture documentation is evidence of technical capability, **not** clinical rationale.
10. `docs/research/SOURCES.md` tracks source intake, open verification tasks and research queue; it must point here for canonical metadata.
