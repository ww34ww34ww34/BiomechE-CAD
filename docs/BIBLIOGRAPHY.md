# BiomechE-CAD — Canonical Bibliography

**Status:** CANONICAL  
**Date initialized:** 2026-08-14  
**Last normalized:** 2026-08-14  
**Purpose:** single authoritative bibliography for EasyCAD2 evidence, scientific literature, guidelines, vendor sources and architecture references used by BiomechE-CAD.

> Other project documents cite the stable source IDs defined here instead of duplicating bibliographic metadata. `docs/research/SOURCES.md` is an intake/research ledger; this file is the canonical bibliographic authority.

---

## 0. Citation policy

Use stable IDs plus the most precise truthful locator available:

```text
[EC2-MANUAL-1.1, pp. 31–35]
[REF-CAD-013, pp. 84–88]
[REF-CAD-046, Table 2; Results; Discussion]
[GUIDE-IWGDF-2023, Prevention recommendation/context]
```

Locator priority:

1. exact PDF/manual/article page;
2. article table, figure or numbered section;
3. HTML section heading;
4. PubMed/PMC abstract subsection;
5. whole source only when no finer locator has been captured.

**Never invent a page number.** Population-specific, protocol-specific, model-based and vendor claims remain labelled as such.

Documents may link source IDs to this file:

```markdown
[REF-CAD-004]: ../BIBLIOGRAPHY.md#ref-cad-004
```

---

# A. Primary EasyCAD2 sources

<a id="ec2-manual-11"></a>
## EC2-MANUAL-1.1 — EasyCAD2 Manuale ITA 2.0
- **Title:** EasyCAD2 — Manuale d'uso / `Easycad2 Manuale ITA 2.0`
- **Type/version/date:** primary product manual; software `1.1.x.x`; 13/01/2024.
- **URL:** https://drive.google.com/file/d/148X366g4e47cYOWtFWP-jeMqavSJqHTa/view
- **Locator map:** pp. 7–12 database/settings; p.13 navigation; p.14 side/mirror; pp.15–18 DIMA; pp.19–20 pressure; pp.21–22 Scan3D; p.23 Scan2D; pp.24–30 MODIFICA/heel/arch/wedge; pp.31–35 ELEMENTI/custom; pp.36–40 POST PROCESSING; pp.42–44 CONTROLLO; pp.44–50 PRODUCI; pp.50–52 toolbar/history; pp.52–53 thickness warning/safe close.
- **Role:** behavioral baseline and exact feature/page evidence. Do not redistribute PDF/screenshots publicly without rights clearance.

<a id="ec2-val-plan-14"></a>
## EC2-VAL-PLAN-1.4 — EasyCAD2 software validation plan
- **Title:** PdV0001 — Piano di validazione software EasyCAD2.
- **Type/version/date:** primary validation plan; target `1.4.x.x`; version 1; 15/01/2026.
- **URL:** https://drive.google.com/file/d/19Pdjn76a6sAEcnUTut2qL0qzvfkniD4v/view
- **Locator:** US1–US25; cite story number, e.g. `[EC2-VAL-PLAN-1.4, US12]`.
- **Role:** authoritative validated-behavior inventory.

<a id="ec2-val-report-14"></a>
## EC2-VAL-REPORT-1.4 — EasyCAD2 validation report
- **Title:** RdT001 — Rapporto di Test di validazione software EasyCAD2 versione 1.4.x.x.
- **Date:** 20/01/2026.
- **URL:** https://drive.google.com/file/d/1kbDKQd6qskQH1MyZ5O3Y-WYt5p_7qRlJ/view
- **Locator/result:** result table/test-result section; 25 planned, 25 executed, 25 PASS, 0 FAIL, 0 BLOCKED.
- **Role:** confirms validation outcome, not proprietary algorithms.

---

# B. Clinical guideline / consensus sources

<a id="guide-iwgdf-2023"></a>
## GUIDE-IWGDF-2023 — IWGDF Guidelines 2023
- **Title:** International Working Group on the Diabetic Foot Guidelines 2023 — Prevention / Offloading guideline set.
- **Official page:** https://iwgdfguidelines.org/guidelines-2023/
- **Related publication:** Bus SA et al. *Guidelines on the prevention of foot ulcers in persons with diabetes (IWGDF 2023 update).* DOI `10.1002/dmrr.3651`.
- **Locator:** named guideline/recommendation/section.
- **Role:** quantitative targets may exist for specific diabetic-foot contexts; not universal CAD defaults.

<a id="guide-heel-pain-2023"></a>
## GUIDE-HEEL-PAIN-2023 — Heel Pain / Plantar Fasciitis Clinical Practice Guideline 2023
- **Citation:** Koc TA Jr, Bise CG, Neville C, Carreira D, Martin RL, McDonough CM. *Heel Pain – Plantar Fasciitis: Revision 2023.* J Orthop Sports Phys Ther. 2023;53(12):CPG1–CPG39.
- **PMID:** `38037331`
- **DOI:** `10.2519/jospt.2023.0303`
- **Official page:** https://www.orthopt.org/content/s/heel-pain-plantar-fasciitis-revision-2023
- **Locator:** `FOOT ORTHOSES` recommendation/evidence synthesis; pp. CPG1–CPG39.
- **Role:** plantar-heel-pain context; orthoses should not be treated as an isolated short-term intervention, and evidence for specific orthosis types/materials/designs remains limited.

---

# C. Scientific literature

<a id="ref-cad-001"></a>
## REF-CAD-001 — Rearfoot posting dose response
Telfer S, Abbott M, Steultjens MPM, Woodburn J. *Dose-response effects of customised foot orthoses on lower limb kinematics and kinetics in pronated foot type.* J Biomech. 2013;46(9):1489–1495. PMID `23631857`; DOI `10.1016/j.jbiomech.2013.03.036`. Locator: pp.1489–1495; Abstract—Methods/Results. URL: https://pubmed.ncbi.nlm.nih.gov/23631857/ . Role: posting angle as explicit numerical dose.

<a id="ref-cad-002"></a>
## REF-CAD-002 — 3D scanning methods
Farhan M et al. *Comparison of 3D scanning versus traditional methods of capturing foot and ankle morphology for the fabrication of orthoses: a systematic review.* J Foot Ankle Res. 2021;14:2. PMID `33413570`; DOI `10.1186/s13047-020-00442-8`. Locator: full article / Abstract—Results/Conclusions. URL: https://pubmed.ncbi.nlm.nih.gov/33413570/ . Role: scan provenance/protocol/QC.

<a id="ref-cad-003"></a>
## REF-CAD-003 — 3D foot-shape methodology/reporting
Allan JJ et al. *Methodological and statistical approaches for the assessment of foot shape using three-dimensional foot scanning: a scoping review.* J Foot Ankle Res. 2023. PMID `37106385`; DOI `10.1186/s13047-023-00617-z`. Locator: full article/reporting checklist. URL: https://pubmed.ncbi.nlm.nih.gov/37106385/ . Role: scanner, markers, weight-bearing and protocol metadata.

<a id="ref-cad-004"></a>
## REF-CAD-004 — Shape + pressure custom insole design
Owings TM et al. *Custom therapeutic insoles based on both foot shape and plantar pressure measurement provide enhanced pressure relief.* Diabetes Care. 2008;31(5):839–844. PMID `18252899`; DOI `10.2337/dc07-2288`. Locator: pp.839–844; Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/18252899/ . Role: quantitative pressure-informed design and redistribution.

<a id="ref-cad-005"></a>
## REF-CAD-005 — Pressure-guided iterative optimization
Bus SA et al. *Evaluation and optimization of therapeutic footwear for neuropathic diabetic foot patients using in-shoe plantar pressure analysis.* Diabetes Care. 2011. PMID `21610125`; DOI `10.2337/dc10-2206`. Locator: Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/21610125/ . Role: measure → modify → remeasure.

<a id="ref-cad-006"></a>
## REF-CAD-006 — IWGDF prevention publication
Bus SA et al. *Guidelines on the prevention of foot ulcers in persons with diabetes (IWGDF 2023 update).* Diabetes Metab Res Rev. 2024. DOI `10.1002/dmrr.3651`. Locator: guideline recommendation/context. Role: context-bound outcome targets.

<a id="ref-cad-007"></a>
## REF-CAD-007 — Offloading design features systematic review
*Footwear and insole design features for offloading the diabetic at risk foot — A systematic review and meta-analyses.* PMID `33532602`. Locator: Abstract/Results and full article where available. URL: https://pubmed.ncbi.nlm.nih.gov/33532602/ . Role: arch profiles, metatarsal additions/apertures, pressure-informed design, heterogeneity.

<a id="ref-cad-008"></a>
## REF-CAD-008 — Pressure-based 3D printed accommodative insole
Muir BC et al. *Evaluation of novel plantar pressure-based 3-dimensional printed accommodative insoles — A feasibility study.* Clin Biomech. 2022;98:105739. PMID `35987171`; DOI `10.1016/j.clinbiomech.2022.105739`. Locator: article 105739 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/35987171/ . Role: pressure-derived offloading and personalized mechanics.

<a id="ref-cad-009"></a>
## REF-CAD-009 — Orthosis stiffness in flexible flatfoot
Cherni Y et al. *Effect of 3D printed foot orthoses stiffness on muscle activity and plantar pressures in individuals with flexible flatfeet.* Clin Biomech. 2022;92:105553. PMID `34973589`; DOI `10.1016/j.clinbiomech.2021.105553`. Locator: Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/34973589/ . Role: stiffness as independent dose.

<a id="ref-cad-010"></a>
## REF-CAD-010 — Stiffness/design/posting effects
Desmyttere G et al. *Effect of 3D printed foot orthoses stiffness and design on foot kinematics and plantar pressures in healthy people.* Gait Posture. 2020. PMID `32818861`; DOI `10.1016/j.gaitpost.2020.07.146`. Locator: Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/32818861/ . Role: geometry/stiffness region-specific effects.

<a id="ref-cad-011"></a>
## REF-CAD-011 — Central metatarsal pressure meta-analysis
Ruiz-Ramos M et al. *Effectiveness of bespoke or customised orthotic treatment in plantar pressure reduction of the central metatarsals: a systematic review and meta-analysis.* J Orthop. 2024;59:111–118. PMID `39399760`; DOI `10.1016/j.jor.2023.12.006`. Locator: pp.111–118. URL: https://pubmed.ncbi.nlm.nih.gov/39399760/ . Role: metatarsal pressure redistribution.

<a id="ref-cad-012"></a>
## REF-CAD-012 — Forefoot pressure systematic review 2026
Thiaspras L et al. *Foot orthoses for forefoot pressure reduction and the hypothesized role in calf muscle stretching: A systematic review highlighting an evidence gap.* Foot. 2026;67:102251. PMID `41931962`; DOI `10.1016/j.foot.2026.102251`. Locator: article 102251 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/41931962/ . Role: forefoot load reduction/PTI.

<a id="ref-cad-013"></a>
## REF-CAD-013 — Metatarsal pad placement in diabetic neuropathy
Hastings MK et al. *Effect of metatarsal pad placement on plantar pressure in people with diabetes mellitus and peripheral neuropathy.* Foot Ankle Int. 2007;28(1):84–88. PMID `17257544`; DOI `10.3113/FAI.2007.0015`. Locator: pp.84–88; Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/17257544/ . Role: anatomical placement as measurable dose.

<a id="ref-cad-014"></a>
## REF-CAD-014 — Hallux-valgus metatarsal pad placement
Hakukawa S et al. *Optimal placement of metatarsal pads for patients with hallux valgus based on plantar pressure measurement.* Foot Ankle Surg. 2026;32(2):131–138. PMID `40707294`; DOI `10.1016/j.fas.2025.07.005`. Locator: pp.131–138 / Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/40707294/ . Role: normalized placement is population-specific.

<a id="ref-cad-015"></a>
## REF-CAD-015 — Forefoot wedge dose response
Zhang X, Lam WK, Vanwanseele B. *Dose-response effects of forefoot and arch orthotic components on the center of pressure trajectory during running in pronated feet.* Gait Posture. 2022;92:212–217. PMID `34864487`; DOI `10.1016/j.gaitpost.2021.11.033`. Locator: pp.212–217 / Abstract—Methods/Results. URL: https://pubmed.ncbi.nlm.nih.gov/34864487/ . Role: forefoot wedge dose; arch support effect in this specific running protocol was minimal.

<a id="ref-cad-016"></a>
## REF-CAD-016 — Insole configurations: pressure vs convenience
Guldemond NA et al. *The effects of insole configurations on forefoot plantar pressure and walking convenience in diabetic patients with neuropathic feet.* Clin Biomech. 2007;22(1):81–87. PMID `17046124`; DOI `10.1016/j.clinbiomech.2006.08.004`. Locator: pp.81–87 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/17046124/ . Role: combination effects; pressure vs comfort trade-off.

<a id="ref-cad-017"></a>
## REF-CAD-017 — Arch-support hardness
Chen H et al. *Biomechanical effects of varying arch support hardness in foot orthosis for adults with flexible flatfoot: A comprehensive Bayesian statistical analysis.* Gait Posture. 2026;125:110085. PMID `41455151`; DOI `10.1016/j.gaitpost.2025.110085`. Locator: Abstract—Methods/Results/Conclusions; hardness conditions Shore C 30/50/70. URL: https://pubmed.ncbi.nlm.nih.gov/41455151/ . Role: hardness is separate from geometry; effects can plateau and transfer load.

<a id="ref-cad-018"></a>
## REF-CAD-018 — Heel plug custom foot orthosis
Balsdon ME, Dombroski CE. *Custom-made foot orthoses with and without heel plugs and their effect on treatment outcomes and plantar pressures in patients with plantar fasciitis: A crossover study.* Prosthet Orthot Int. 2026;50(2):198–204. PMID `40366378`; DOI `10.1097/PXR.0000000000000450`. Locator: pp.198–204; Abstract—Methods/Results: matched custom orthoses, one with a softer PORON heel plug; hindfoot average/peak pressure and pressure contact area were lower with the plug; FFI/comfort did not differ between orthosis conditions. URL: https://pubmed.ncbi.nlm.nih.gov/40366378/ . Role: containment geometry vs cushioning/material relief.

<a id="ref-cad-019"></a>
## REF-CAD-019 — Heel cup/arch pressure redistribution
*Effects of a range of 6 prefabricated orthotic insole designs on plantar pressure in a healthy population.* PMID `39140763`; DOI `10.1097/PXR.0000000000000292`. Locator: Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/39140763/ . Role: heel-cup/arch regional pressure and contact-area effects.

<a id="ref-cad-020"></a>
## REF-CAD-020 — Inter-individual offloading response
*Pressure relief and load redistribution by custom-made insoles in diabetic patients with neuropathy and foot deformity.* PMID `15234488`. Locator: Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/15234488/ . Role: patient-specific verification and load transfer.

<a id="ref-cad-021"></a>
## REF-CAD-021 — Graded stiffness heel offloading
*Graded stiffness offloading insoles better redistribute heel plantar pressure to protect the diabetic neuropathic foot.* PMID `36706604`. Locator: Abstract / full text as needed. URL: https://pubmed.ncbi.nlm.nih.gov/36706604/ . Role: regional stiffness and perimeter loading.

<a id="ref-cad-022"></a>
## REF-CAD-022 — Gradient lattice mapping 2026
Wang Lihong et al. *Optimization of pressure relief in gradient lattice orthotic insoles based on plantar pressure-rod diameter mapping.* Med Eng Phys. 2026. PMID `42049041`; DOI `10.1088/1873-4030/ae6593`. Locator: Abstract/modeling methods. URL: https://pubmed.ncbi.nlm.nih.gov/42049041/ . Role: R&D pressure→regional modulus mapping.

<a id="ref-cad-023"></a>
## REF-CAD-023 — Partition TPMS lattice 2026
*Design of novel orthotic insoles based on partition infilling of TPMS structures.* PMID `42147489`. Locator: Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/42147489/ . Role: R&D region-specific lattice.

<a id="ref-cad-024"></a>
## REF-CAD-024 — 3D printed orthoses clinical outcomes systematic review
Atallah H et al. *The current state of 3D-printed orthoses clinical outcomes: a systematic review.* BMC Musculoskelet Disord. 2025. PMID `40890671`; DOI `10.1186/s12891-025-09070-4`. Locator: full article / Abstract—Results/Conclusions. URL: https://pubmed.ncbi.nlm.nih.gov/40890671/ . Role: feasibility, comfort/fit, material/durability limitations.

<a id="ref-cad-025"></a>
## REF-CAD-025 — Assistive-device adherence
*Patient Compliance With Wearing Lower Limb Assistive Devices: A Scoping Review.* PMID `35753880`; DOI `10.1016/j.jmpt.2022.04.003`. Locator: Abstract/review results. URL: https://pubmed.ncbi.nlm.nih.gov/35753880/ . Role: comfort/fit/adherence.

<a id="ref-cad-026"></a>
## REF-CAD-026 — PROM landscape
*Patient reported outcome measures in the foot and ankle literature: A systematic review.* PMID `41033023`; DOI `10.1016/j.foot.2025.102209`. Locator: Abstract/full review. URL: https://pubmed.ncbi.nlm.nih.gov/41033023/ . Role: avoid a proprietary universal outcome score.

<a id="ref-cad-027"></a>
## REF-CAD-027 — Adult flatfoot evidence uncertainty
*Evidence for foot orthoses for adults with flatfoot: a systematic review.* PMID `34844639`. Locator: Abstract—Conclusions. URL: https://pubmed.ncbi.nlm.nih.gov/34844639/ . Role: heterogeneity/uncertainty.

<a id="ref-cad-028"></a>
## REF-CAD-028 — Flexible flatfoot patient-reported outcomes
*Foot orthoses for flexible flatfeet in children and adults: a systematic review and meta-analysis of patient-reported outcomes.* PMID `36611153`; DOI `10.1186/s12891-022-06044-8`. Locator: full article / Abstract—Conclusions. URL: https://pubmed.ncbi.nlm.nih.gov/36611153/ . Role: population-specific outcomes.

<a id="ref-cad-029"></a>
## REF-CAD-029 — Local offloading and neighbouring load transfer
Shuang J et al. *The effect of calcaneus and metatarsal head offloading insoles on healthy subjects' gait kinematics, kinetics, asymmetry, and the implications for plantar pressure management: A pilot study.* PLoS One. 2024;19(5):e0303826. PMID `38758937`; PMCID `PMC11101073`; DOI `10.1371/journal.pone.0303826`. Locator: Fig.1 and Fig.6; Abstract—Results/Conclusion. URL: https://pubmed.ncbi.nlm.nih.gov/38758937/ . Role: safety-ring load-transfer analysis.

<a id="ref-cad-030"></a>
## REF-CAD-030 — Reduction and redistribution using orthoses
Kato H et al. *The reduction and redistribution of plantar pressures using foot orthoses in diabetic patients.* Diabetes Res Clin Pract. 1996;31:115–118. PMID `8792110`; DOI `10.1016/0168-8227(96)01214-4`. Locator: pp.115–118 / Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/8792110/ . Role: total-contact redistribution/contact area.

<a id="ref-cad-031"></a>
## REF-CAD-031 — Rigid relief orthosis
Novick A et al. *Reduction of plantar pressure with the rigid relief orthosis.* J Am Podiatr Med Assoc. 1993;83(3):115–122. PMID `8468692`; DOI `10.7547/87507315-83-3-115`. Locator: pp.115–122 / Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/8468692/ . Role: local relief interacts with total contact and secondary regions.

<a id="ref-cad-032"></a>
## REF-CAD-032 — Pad shape can worsen peak pressure
Nordsiden L et al. *The effect of 3 foot pads on plantar pressure of pes planus foot type.* J Sport Rehabil. 2010;19(1):71–85. PMID `20231746`; DOI `10.1123/jsr.19.1.71`. Locator: pp.71–85 / Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/20231746/ . Role: no relief primitive is intrinsically beneficial.

<a id="ref-cad-033"></a>
## REF-CAD-033 — Peak pressure vs pressure-time integral
*The value of reporting pressure-time integral data in addition to peak pressure data in studies on the diabetic foot: a systematic review.* PMID `23273847`; DOI `10.1016/j.clinbiomech.2012.12.002`. Locator: Abstract—Findings. URL: https://pubmed.ncbi.nlm.nih.gov/23273847/ . Role: retain PTI with peak pressure.

<a id="ref-cad-034"></a>
## REF-CAD-034 — In-shoe plantar pressure measurement technology
Castro-Martins P et al. *In-shoe plantar pressure measurement technologies for the diabetic foot: A systematic review.* Heliyon. 2024;10(9):e29672. PMID `38699042`; PMCID `PMC11064085`; DOI `10.1016/j.heliyon.2024.e29672`. Locator: article/figures/Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/38699042/ . Role: device/calibration/protocol provenance.

<a id="ref-cad-035"></a>
## REF-CAD-035 — In-shoe measurement reliability, steps and speed
Kernozek TW, LaMott EE, Dancisak MJ. *Reliability of an in-shoe pressure measurement system during treadmill walking.* Foot Ankle Int. 1996;17(4):204–209. PMID `8696496`; DOI `10.1177/107110079601700404`. Locator: pp.204–209 / Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/8696496/ . Role: speed and step-count awareness.

<a id="ref-cad-036"></a>
## REF-CAD-036 — Cross-system plantar-pressure comparability
Chockalingam N et al. *Discrepancies between plantar pressure devices: Evaluating cross-system reliability for biomechanics, clinical use and predictive modelling.* Foot. 2025;64:102190. PMID `40743570`; DOI `10.1016/j.foot.2025.102190`. Locator: article 102190 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/40743570/ . Role: cross-device warnings.

<a id="ref-cad-037"></a>
## REF-CAD-037 — In-shoe pressure thresholds review
Jones P et al. *In-shoe pressure thresholds for people with diabetes and neuropathy at risk of ulceration: A systematic review.* J Diabetes Complications. 2021;35(3):107815. PMID `33280984`; DOI `10.1016/j.jdiacomp.2020.107815`. Locator: Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/33280984/ . Role: thresholds are context-bound.

<a id="ref-cad-038"></a>
## REF-CAD-038 — Plantar pressure thresholds systematic review 2024
Castro-Martins P et al. *Plantar pressure thresholds as a strategy to prevent diabetic foot ulcers: A systematic review.* Heliyon. 2024;10(4):e26161. PMID `38390156`; PMCID `PMC10882031`; DOI `10.1016/j.heliyon.2024.e26161`. Locator: article/Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/38390156/ . Role: threshold heterogeneity.

<a id="ref-cad-039"></a>
## REF-CAD-039 — Plantar shear measurement technologies
Rajala S, Lekkala J. *Plantar shear stress measurements — A review.* Clin Biomech. 2014;29(5):475–483. PMID `24820135`; DOI `10.1016/j.clinbiomech.2014.04.009`. Locator: pp.475–483. URL: https://pubmed.ncbi.nlm.nih.gov/24820135/ . Role: shear distinct from normal pressure.

<a id="ref-cad-040"></a>
## REF-CAD-040 — Plantar shear in diabetic foot
Jones AD et al. *Plantar shear stress in the diabetic foot: A systematic review and meta-analysis.* Diabet Med. 2022;39(1):e14661. PMID `34324731`; DOI `10.1111/dme.14661`. Locator: Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/34324731/ . Role: measured shear outcome.

<a id="ref-cad-041"></a>
## REF-CAD-041 — Metatarsal domes in older people with forefoot pain
Landorf KB et al. *Effects of metatarsal domes on plantar pressures in older people with a history of forefoot pain.* J Foot Ankle Res. 2020;13:18. PMID `32375847`; PMCID `PMC7201604`; DOI `10.1186/s13047-020-00388-x`. Locator: article 18 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/32375847/ . Role: pad placement/type/density.

<a id="ref-cad-042"></a>
## REF-CAD-042 — Metatarsal pad position in metatarsalgia
Hsi WL, Kang JH, Lee XX. *Optimum position of metatarsal pad in metatarsalgia for pressure relief.* Am J Phys Med Rehabil. 2005;84(7):514–520. PMID `15973088`; DOI `10.1097/01.phm.0000167680.70092.29`. Locator: pp.514–520 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/15973088/ . Role: position relative to MTH pressure peak.

<a id="ref-cad-043"></a>
## REF-CAD-043 — Forefoot pressure-relieving orthosis comparison
*Comparison of the Forefoot Pressure-Relieving Effects of Foot Orthoses.* PMID `36031787`. Locator: Abstract—Methods/Results. URL: https://pubmed.ncbi.nlm.nih.gov/36031787/ . Role: compare measured effects of pad/cushion concepts.

<a id="ref-cad-044"></a>
## REF-CAD-044 — Rheumatoid arthritis: metatarsal bar/dome pressure and pain
Hodge MC, Bach TM, Carter GM. *Orthotic management of plantar pressure and pain in rheumatoid arthritis.* Clin Biomech. 1999;14(8):567–575. PMID `10521640`; DOI `10.1016/S0268-0033(99)00034-0`. Locator: pp.567–575 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/10521640/ . Role: pressure and subjective pain need not rank designs identically.

## Arch-support deep-dive additions

<a id="ref-cad-045"></a>
## REF-CAD-045 — Arch support height dose: finite-element analysis
Peng Y et al. *Influence of arch support heights on the internal foot mechanics of flatfoot during walking: A muscle-driven finite element analysis.* Comput Biol Med. 2021;132:104355. PMID `33812264`; DOI `10.1016/j.compbiomed.2021.104355`. Locator: Abstract—Methods/Results/Conclusion. URL: https://pubmed.ncbi.nlm.nih.gov/33812264/ . Role: height is a biomechanical dose; higher support can reduce some pressures/plantar-fascia strains while increasing midfoot pressure and central fascia loading. **Model-based evidence.**

<a id="ref-cad-046"></a>
## REF-CAD-046 — Arch height × posting × heel cup × material interaction
Peng Y et al. *Different Design Feature Combinations of Flatfoot Orthosis on Plantar Fascia Strain and Plantar Pressure: A Muscle-Driven Finite Element Analysis With Taguchi Method.* Front Bioeng Biotechnol. 2022;10:853085. PMID `35360398`; PMCID `PMC8960448`; DOI `10.3389/fbioe.2022.853085`. Locator: Table 2 (arch 42/45/48 mm; posting 0/2/4°; heel cup 14/16/18 mm; material 3/5/7 MPa), Results/Table 4, Discussion. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8960448/ . Role: arch geometry cannot be interpreted independently from posting, heel cup and stiffness; heel-cup height is also an explicit modeled design factor. **Model-based evidence.**

<a id="ref-cad-047"></a>
## REF-CAD-047 — 3D-printed arch-support hardness and comfort
Channasanon S et al. *3D-printed medial arch supports of varying hardness versus a prefabricated arch support on plantar pressure: A 1-month randomized crossover study in healthy volunteers.* Prosthet Orthot Int. 2023;47(2):210–217. PMID `36037286`; DOI `10.1097/PXR.0000000000000178`. Locator: pp.210–217 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/36037286/ . Role: hardness/comfort relationship.

<a id="ref-cad-048"></a>
## REF-CAD-048 — Flatfoot plantar-pressure interventions systematic review 2026
Mahmoudiyan V et al. *Effects of conservative interventions on plantar pressure in individuals with flat foot: a systematic review and meta-analysis.* Sci Rep. 2026;16:9867. PMID `41714420`; PMCID `PMC13018568`; DOI `10.1038/s41598-026-40771-5`. Locator: Abstract/full meta-analysis. URL: https://www.nature.com/articles/s41598-026-40771-5 . Role: redistribution and medial-midfoot load.

<a id="ref-cad-049"></a>
## REF-CAD-049 — Medial arch support in hallux valgus
Farzadi M et al. *Effect of medial arch support foot orthosis on plantar pressure distribution in females with mild-to-moderate hallux valgus after one month of follow-up.* Prosthet Orthot Int. 2015;39(2):134–139. PMID `24515981`; DOI `10.1177/0309364613518229`. Locator: pp.134–139 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/24515981/ . Role: population-specific redistribution.

<a id="ref-cad-050"></a>
## REF-CAD-050 — Arch-support height dose during cutting
Toyooka S et al. *Association of medial arch support of foot orthoses with knee valgus angle at initial contact during cutting maneuvers in female athletes: a controlled laboratory study.* BMC Sports Sci Med Rehabil. 2022. PMID `36536460`; PMCID `PMC9762016`; DOI `10.1186/s13102-022-00608-w`. Locator: Abstract—Methods/Results. URL: https://pubmed.ncbi.nlm.nih.gov/36536460/ . Role: human height-dose evidence for a specific sport task.

<a id="ref-cad-051"></a>
## REF-CAD-051 — Arch support and lateral-column load in sport
Yu B et al. *Effects of wearing foot orthosis with medial arch support on the fifth metatarsal loading and ankle inversion angle in selected basketball tasks.* J Orthop Sports Phys Ther. 2007. PMID `17469671`; DOI `10.2519/jospt.2007.2327`. Locator: Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/17469671/ . Role: remote/safety-region monitoring.

<a id="ref-cad-052"></a>
## REF-CAD-052 — Soft vs hard 3D-printed medial arch support RCT
Paecharoen S et al. *Effectiveness of a 3D-printed silicone medial arch support on foot pain in individuals with pes planus: A randomized controlled trial.* Ann Phys Rehabil Med. 2025;68(7):102007. PMID `40819420`; DOI `10.1016/j.rehab.2025.102007`. Locator: Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/40819420/ . Role: pain/function vs pressure effects in pes planus.

<a id="ref-cad-053"></a>
## REF-CAD-053 — Arch reinforcement and undercut
Cheng KW et al. *A Three-Dimensional Printed Foot Orthosis for Flexible Flatfoot: An Exploratory Biomechanical Study on Arch Support Reinforcement and Undercut.* Materials. 2021;14(18):5297. PMID `34576526`; PMCID `PMC8469370`; DOI `10.3390/ma14185297`. Locator: Abstract/full article design-method/results. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8469370/ . Role: geometry and stiffness reinforcement are separable.

<a id="ref-cad-054"></a>
## REF-CAD-054 — Arch support and plantar fasciitis 2026
Taseh A et al. *Arch-supports and plantar fasciitis: A prospective study incorporating patient-reported outcomes and finite element analysis.* J Exp Orthop. 2026;13:e70732. PMID `42130670`; DOI `10.1002/jeo2.70732`. Locator: Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/42130670/ . Role: short-term clinical/structural/pressure evidence; uncontrolled prospective design.

<a id="ref-cad-055"></a>
## REF-CAD-055 — Arch-support insole plantar pressure/contact area in flatfoot
Huang YP et al. *The arch support insoles show benefits to people with flatfoot on stance time, cadence, plantar pressure and contact area.* PLoS One. 2020;15(8):e0237382. PMID `32817709`; PMCID `PMC7446821`; DOI `10.1371/journal.pone.0237382`. Locator: Abstract/full article tables. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7446821/ . Role: regional pressure/contact-area changes.

<a id="ref-cad-056"></a>
## REF-CAD-056 — Arch correction under different body-weight loads
Lavoie-Turcotte T et al. *Flatfoot arch correction with generic 3D-printed orthoses at different body weight percentages.* Foot (Edinb). 2024;59:102093. PMID `38520781`; DOI `10.1016/j.foot.2024.102093`. Locator: article 102093 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/38520781/ . Role: structural outcome depends on loading condition.

<a id="ref-cad-057"></a>
## REF-CAD-057 — Radiographic/anthropometric medial arch support
Escalona-Marfil C et al. *A radiographic and anthropometric study of the effect of a contoured sandal and foot orthosis on supporting the medial longitudinal arch.* J Foot Ankle Res. 2014;7:38. PMID `25317208`; PMCID `PMC4196133`; DOI `10.1186/s13047-014-0038-5`. Locator: article 38 / Abstract. URL: https://pubmed.ncbi.nlm.nih.gov/25317208/ . Role: structural arch-height outcome.

## Heel / rearfoot deep-dive additions

<a id="ref-cad-058"></a>
## REF-CAD-058 — Individualized 3D-printed heel cup
Li L et al. *3D printing individualized heel cup for improving the self-reported pain of plantar fasciitis.* J Transl Med. 2018;16:167. DOI `10.1186/s12967-018-1547-y`. Locator: Methods—Heel cup design and fabrication; Abstract—Results/Conclusion. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6007068/ . Role: scan-derived patient-specific heel-cup geometry; study device was 5 mm thick and wrapped the plantar heel from the upper calcaneal margin toward the arch. **Do not generalize 5 mm as an optimum.**

<a id="ref-cad-059"></a>
## REF-CAD-059 — Plastic heel cup confinement mechanism
Lin CY et al. *Biomechanical Effects of Plastic Heel Cup on Plantar Fasciitis Patients Evaluated by Ultrasound Shear Wave Elastography.* J Clin Med. 2022;11(8):2150. PMID `35456242`; PMCID `PMC9028113`; DOI `10.3390/jcm11082150`. Locator: Abstract—Methods/Results/Conclusion; full article figures on heel-pad confinement. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9028113/ . Role: heel cup can alter heel-pad thickness and measured stiffness through confinement; geometry is mechanistically distinct from soft cushioning.

<a id="ref-cad-060"></a>
## REF-CAD-060 — Heel cup, heel-pad thickness, pressure and pain in Sever's disease
Perhamre S, Lundin F, Klässbo M, Norlin R. *A heel cup improves the function of the heel pad in Sever's injury: effects on heel pad thickness, peak pressure and pain.* Scand J Med Sci Sports. 2012;22(4):516–522. PMID `21410537`; DOI `10.1111/j.1600-0838.2010.01266.x`. Locator: pp.516–522; Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/21410537/ . Role: pediatric evidence that heel containment can increase heel-pad thickness and reduce peak pressure/pain. **Population-specific; not an adult default.**

<a id="ref-cad-061"></a>
## REF-CAD-061 — Heel cup versus heel wedge in Sever's disease
Perhamre S, Lundin F, Norlin R, Klässbo M. *Sever's injury; treat it with a heel cup: a randomized, crossover study with two insole alternatives.* Scand J Med Sci Sports. 2011;21(6):e42–e47. PMID `20673253`; DOI `10.1111/j.1600-0838.2010.01140.x`. Locator: pp.e42–e47; Abstract—Results. URL: https://pubmed.ncbi.nlm.nih.gov/20673253/ . Role: cup and wedge are not interchangeable intervention classes; pediatric diagnosis-specific evidence.

<a id="ref-cad-062"></a>
## REF-CAD-062 — Prefabricated inserts versus custom orthosis in plantar fasciitis
Pfeffer G et al. *Comparison of custom and prefabricated orthoses in the initial treatment of proximal plantar fasciitis.* Foot Ankle Int. 1999;20(4):214–221. PMID `10229276`; DOI `10.1177/107110079902000402`. Locator: pp.214–221; Abstract—Methods/Results. URL: https://pubmed.ncbi.nlm.nih.gov/10229276/ . Role: custom geometry is not automatically superior to simpler heel/insole devices in a specific short-term multimodal treatment context.

<a id="ref-cad-063"></a>
## REF-CAD-063 — Heel insole conformity, thickness and material FE study
Goske S, Erdemir A, Petre M, Budhabhatti S, Cavanagh PR. *Reduction of plantar heel pressures: Insole design using finite element analysis.* J Biomech. 2006;39(13):2363–2370. PMID `16197952`; DOI `10.1016/j.jbiomech.2005.08.006`. Locator: pp.2363–2370; Abstract—Methods/Results/Discussion. URL: https://pubmed.ncbi.nlm.nih.gov/16197952/ . Role: in the modeled design space, conformity was more influential than material choice for peak heel pressure; supports independent conformity, thickness and material parameters. **Model-based evidence.**

<a id="ref-cad-064"></a>
## REF-CAD-064 — Subject-specific heel cushioning material modeling
Chatzistergos PE, Naemi R, Chockalingam N. *A method for subject-specific modelling and optimisation of the cushioning properties of insole materials used in diabetic footwear.* Med Eng Phys. 2015;37(6):531–538. PMID `25937545`; DOI `10.1016/j.medengphy.2015.03.009`. Locator: pp.531–538; Abstract—Methods/Results/Conclusion. URL: https://pubmed.ncbi.nlm.nih.gov/25937545/ . Role: cushioning response depends on subject/loading context; material name alone is insufficient. **Model-based / diabetic-foot context.**

<a id="ref-cad-065"></a>
## REF-CAD-065 — Pressure-guided CAD/CAM orthosis in chronic plantar fasciitis
Nakhaee M et al. *The effects of a custom foot orthosis on dynamic plantar pressure in patients with chronic plantar fasciitis: A randomized controlled trial.* Prosthet Orthot Int. 2023;47(3):241–252. PMID `36037272`; DOI `10.1097/PXR.0000000000000179`. Locator: pp.241–252; Abstract—Methods/Results/Conclusions. URL: https://pubmed.ncbi.nlm.nih.gov/36037272/ . Role: links pressure-guided CAD/CAM orthoses with pressure/force, ultrasound and PROM outcomes; shows clinical outcome is not reducible to a single peak-pressure direction.

<a id="ref-cad-066"></a>
## REF-CAD-066 — Plantar heel pain orthoses systematic review/meta-analysis
Whittaker GA et al. *Foot orthoses for plantar heel pain: a systematic review and meta-analysis.* Br J Sports Med. 2018;52(5):322–328. PMID `28935689`; DOI `10.1136/bjsports-2016-097355`. Locator: pp.322–328; Abstract—Results/Conclusion. URL: https://pubmed.ncbi.nlm.nih.gov/28935689/ . Role: moderate evidence for a small medium-term pain effect, uncertainty about clinical importance, and no clear custom-versus-prefabricated superiority.

<a id="ref-cad-067"></a>
## REF-CAD-067 — Heel cup + advice context in plantar fasciopathy RCT
Riel H et al. *Does a corticosteroid injection plus exercise or exercise alone add to the effect of patient advice and a heel cup for patients with plantar fasciopathy? A randomised clinical trial.* Br J Sports Med. 2023;57(18):1180–1186. PMID `37414460`; PMCID `PMC10579183`; DOI `10.1136/bjsports-2023-106948`. Locator: pp.1180–1186; Abstract—Methods/Results/Conclusion. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10579183/ . Role: heel cup appears within a multimodal treatment context; the study does not isolate heel-cup geometry dose.

---

# D. Vendor / market sources

<a id="vendor-sensormedica-easycad2"></a>
## VENDOR-SENSORMEDICA-EASYCAD2
- **Page:** Sensor Medica — EasyCAD2. URL: https://www.sensormedica.com/en/easycad-2/
- **Use:** market/product functionality only, not clinical efficacy.

<a id="vendor-sensormedica-insole"></a>
## VENDOR-SENSORMEDICA-INSOLE
- **Page:** Sensor Medica — easyCAD Insole. URL: https://www.sensormedica.com/en/easycad-insole/
- **Use:** vendor workflow/product claims only.

<a id="vendor-sensormedica-vulcan"></a>
## VENDOR-SENSORMEDICA-VULCAN
- **Page:** Sensor Medica — Vulcan CNC. URL: https://www.sensormedica.com/it/vulcan-cnc/
- **Use:** manufacturing/CNC market reference.

---

# E. Architecture references — currently parked

<a id="arch-opensubdiv"></a>
## ARCH-OPENSUBDIV
Pixar OpenSubdiv documentation. URLs: https://opensubdiv.org/ ; https://opensubdiv.org/docs/intro.html ; https://opensubdiv.org/docs/subdivision_surfaces.html . Use: SubD implementation research only.

<a id="arch-opennurbs"></a>
## ARCH-OPENNURBS
McNeel openNURBS / `ON_SubD`. URL: https://github.com/mcneel/opennurbs . Use: geometry foundation/interoperability research only. `opennurbs_subd_data.h` is an unstable internal API and must not be used as application contract.

<a id="arch-rhino3dm"></a>
## ARCH-RHINO3DM
McNeel rhino3dm. URL: https://github.com/mcneel/rhino3dm . Use: .NET/JS/WASM openNURBS interoperability research.

<a id="arch-manifold"></a>
## ARCH-MANIFOLD
Manifold geometry library. URL: https://github.com/elalish/manifold . Use: conditional solid-mesh/manufacturing research.

<a id="arch-occt"></a>
## ARCH-OCCT
Open CASCADE Technology. URLs: https://dev.opencascade.org/doc/overview/html/index.html ; https://github.com/Open-Cascade-SAS/OCCT . Use: optional exact-CAD/interoperability research.

---

# F. Bibliography maintenance rules

1. Add a source here before relying on it in a canonical specification.
2. Never reuse an ID for a different source.
3. Correct metadata here rather than independently in each specification.
4. Append new locators to an existing entry rather than duplicating the source.
5. Exact page locators are mandatory for EasyCAD2/manual/PDF evidence whenever available.
6. For scientific web/abstract evidence, use a truthful locator (`Abstract—Results`, table, figure, HTML section) until exact full-text pages are captured.
7. When full text is later acquired, enrich the existing entry without changing the source ID.
8. Vendor material is evidence of market functionality, not scientific efficacy.
9. Architecture documentation is evidence of technical capability, not clinical rationale.
10. Model-based evidence must remain explicitly labelled and cannot silently become a clinical rule.
11. `docs/research/SOURCES.md` tracks source intake/open verification; this file owns canonical metadata.
