# BiomechE-CAD — Canonical Bibliography

**Status:** CANONICAL  
**Date initialized:** 2026-08-14  
**Last normalized:** 2026-08-16  
**Purpose:** single authoritative bibliography for EasyCAD2 evidence, scientific literature, guidelines, standards, vendor sources and architecture references used by BiomechE-CAD.

> Other project documents cite the stable source IDs defined here instead of duplicating bibliographic metadata. `docs/research/SOURCES.md` is an intake/research ledger; this file is the canonical bibliographic authority.

---

## 0. Citation policy

Use stable IDs plus the most precise truthful locator available:

```text
[EC2-MANUAL-1.1, pp. 31–35]
[REF-CAD-013, pp. 84–88]
[REF-CAD-046, Table 2; Results; Discussion]
[GUIDE-IWGDF-2023, Prevention guideline]
[STD-ISO-868-2003, Abstract]
```

Locator priority:

1. exact PDF/manual/article page;
2. article table, figure or numbered section;
3. HTML section heading;
4. PubMed/PMC abstract subsection;
5. standards abstract/scope when the full standard has not been licensed/read;
6. whole source only when no finer locator has been captured.

**Never invent a page number.** Population-specific, protocol-specific, model-based, standards-derived and vendor claims remain labelled as such.

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
- **Title:** International Working Group on the Diabetic Foot Guidelines 2023.
- **Official page:** https://iwgdfguidelines.org/guidelines-2023/
- **Prevention publication:** Bus SA et al. *Guidelines on the prevention of foot ulcers in persons with diabetes (IWGDF 2023 update).* Diabetes Metab Res Rev. 2024;40(3):e3651. PMID `37302121`; DOI `10.1002/dmrr.3651`.
- **Offloading publication:** Bus SA et al. *Guidelines on offloading foot ulcers in persons with diabetes (IWGDF 2023 update).* Diabetes Metab Res Rev. 2024;40(3):e3647. PMID `37226568`; DOI `10.1002/dmrr.3647`.
- **Locators:** Prevention guideline recommendation on properly fitting accommodative therapeutic footwear and demonstrated plantar-pressure relief for recurrence prevention; Offloading guideline recommendation that a non-removable knee-high offloading device is first choice for healing a neuropathic plantar forefoot/midfoot ulcer.
- **Role:** diabetic-foot profile boundaries, context-specific pressure targets and active-ulcer pathway guard. Not a universal CAD default.

<a id="guide-heel-pain-2023"></a>
## GUIDE-HEEL-PAIN-2023 — Heel Pain / Plantar Fasciitis CPG 2023
- **Citation:** Koc TA Jr, Bise CG, Neville C, Carreira D, Martin RL, McDonough CM. *Heel Pain – Plantar Fasciitis: Revision 2023.* J Orthop Sports Phys Ther. 2023;53(12):CPG1–CPG39.
- **PMID:** `38037331`; **DOI:** `10.2519/jospt.2023.0303`.
- **Official page:** https://www.orthopt.org/content/s/heel-pain-plantar-fasciitis-revision-2023
- **Locator:** `FOOT ORTHOSES` recommendation/evidence synthesis.
- **Role:** plantar-heel-pain profile; orthoses are not an isolated short-term intervention and specific device superiority is limited.

<a id="guide-cosmin"></a>
## GUIDE-COSMIN — COSMIN outcome-measurement methodology
- **Title/page:** COnsensus-based Standards for the selection of health Measurement INstruments (COSMIN) — selection of the most suitable outcome measurement instrument.
- **Official pages:** https://www.cosmin.nl/ ; https://www.cosmin.nl/finding-right-tool/select-best-measurement-instrument/
- **Locator:** `I want to select the most suitable outcome measurement instrument` / recommendation categories A-B-C and feasibility considerations.
- **Role:** PROM selection should be based on construct, content validity, measurement properties, responsiveness/interpretability and feasibility; do not choose a questionnaire only because it is popular.

<a id="guide-fda-pro-device-2022"></a>
## GUIDE-FDA-PRO-DEVICE-2022 — FDA PRO instruments for medical-device evaluation
- **Title:** *Principles for Selecting, Developing, Modifying, and Adapting Patient-Reported Outcome Instruments for Use in Medical Device Evaluation.* FDA Guidance for Industry and FDA Staff. January 2022.
- **Official page:** https://www.fda.gov/regulatory-information/search-fda-guidance-documents/principles-selecting-developing-modifying-and-adapting-patient-reported-outcome-instruments-use
- **Locator:** guidance scope / fit-for-purpose principle.
- **Role:** selected PRO instruments and modifications/adaptations should be demonstrably fit for the intended device-evaluation context.

---

# C. Scientific literature

<a id="ref-cad-001"></a>
## REF-CAD-001 — Rearfoot posting dose response
Telfer S et al. *Dose-response effects of customised foot orthoses on lower limb kinematics and kinetics in pronated foot type.* J Biomech. 2013;46(9):1489–1495. PMID `23631857`; DOI `10.1016/j.jbiomech.2013.03.036`. Locator: pp.1489–1495; Abstract—Methods/Results. Role: posting angle as explicit dose.

<a id="ref-cad-002"></a>
## REF-CAD-002 — 3D scanning methods
Farhan M et al. *Comparison of 3D scanning versus traditional methods of capturing foot and ankle morphology for the fabrication of orthoses: a systematic review.* J Foot Ankle Res. 2021;14:2. PMID `33413570`; DOI `10.1186/s13047-020-00442-8`. Locator: full article / Abstract—Results/Conclusions. Role: scan provenance/protocol/QC.

<a id="ref-cad-003"></a>
## REF-CAD-003 — 3D foot-shape methodology/reporting
Allan JJ et al. *Methodological and statistical approaches for the assessment of foot shape using three-dimensional foot scanning: a scoping review.* J Foot Ankle Res. 2023. PMID `37106385`; DOI `10.1186/s13047-023-00617-z`. Locator: full article/reporting checklist. Role: scanner, markers, weight-bearing and protocol metadata.

<a id="ref-cad-004"></a>
## REF-CAD-004 — Shape + pressure custom insole design
Owings TM et al. *Custom therapeutic insoles based on both foot shape and plantar pressure measurement provide enhanced pressure relief.* Diabetes Care. 2008;31(5):839–844. PMID `18252899`; DOI `10.2337/dc07-2288`. Locator: pp.839–844; Abstract—Results. Role: pressure-informed design and redistribution.

<a id="ref-cad-005"></a>
## REF-CAD-005 — Pressure-guided iterative optimization
Bus SA, Haspels R, Busch-Westbroek TE. *Evaluation and optimization of therapeutic footwear for neuropathic diabetic foot patients using in-shoe plantar pressure analysis.* Diabetes Care. 2011;34(7):1595–1600. PMID `21610125`; PMCID `PMC3120171`; DOI `10.2337/dc10-2206`. Locator: pp.1595–1600; Abstract—Methods/Results/Conclusions. Role: explicit measure → modify → remeasure pressure-guided optimization workflow in neuropathic diabetic footwear; study thresholds remain context-specific.

<a id="ref-cad-006"></a>
## REF-CAD-006 — IWGDF prevention publication
Bus SA et al. *Guidelines on the prevention of foot ulcers in persons with diabetes (IWGDF 2023 update).* Diabetes Metab Res Rev. 2024. DOI `10.1002/dmrr.3651`. Use `GUIDE-IWGDF-2023` for guideline-level claims.

<a id="ref-cad-007"></a>
## REF-CAD-007 — Offloading design features systematic review
*Footwear and insole design features for offloading the diabetic at risk foot — A systematic review and meta-analyses.* PMID `33532602`. Locator: Abstract/Results and full article. Role: arch profiles, metatarsal additions/apertures, pressure-informed design and heterogeneity.

<a id="ref-cad-008"></a>
## REF-CAD-008 — Pressure-based 3D printed accommodative insole
Muir BC et al. *Evaluation of novel plantar pressure-based 3-dimensional printed accommodative insoles — A feasibility study.* Clin Biomech. 2022;98:105739. PMID `35987171`; DOI `10.1016/j.clinbiomech.2022.105739`. Role: pressure-derived offloading and personalized mechanics.

<a id="ref-cad-009"></a>
## REF-CAD-009 — Orthosis stiffness in flexible flatfoot
Cherni Y et al. *Effect of 3D printed foot orthoses stiffness on muscle activity and plantar pressures in individuals with flexible flatfeet: A statistical non-parametric mapping study.* Clin Biomech. 2022;92:105553. PMID `34973589`; DOI `10.1016/j.clinbiomech.2021.105553`. Locator: Abstract—Methods/Findings/Interpretation. Role: stiffness as independent dose.

<a id="ref-cad-010"></a>
## REF-CAD-010 — Stiffness/design/posting effects
Desmyttere G et al. *Effect of 3D printed foot orthoses stiffness and design on foot kinematics and plantar pressures in healthy people.* Gait Posture. 2020. PMID `32818861`; DOI `10.1016/j.gaitpost.2020.07.146`. Role: geometry/stiffness region-specific effects.

<a id="ref-cad-011"></a>
## REF-CAD-011 — Central metatarsal pressure meta-analysis
Ruiz-Ramos M et al. *Effectiveness of bespoke or customised orthotic treatment in plantar pressure reduction of the central metatarsals: a systematic review and meta-analysis.* J Orthop. 2024;59:111–118. PMID `39399760`; DOI `10.1016/j.jor.2023.12.006`. Locator: pp.111–118. Role: mechanical-metatarsalgia pressure reduction.

<a id="ref-cad-012"></a>
## REF-CAD-012 — Forefoot pressure systematic review 2026
Thiaspras L et al. *Foot orthoses for forefoot pressure reduction and the hypothesized role in calf muscle stretching: A systematic review highlighting an evidence gap.* Foot. 2026;67:102251. PMID `41931962`; DOI `10.1016/j.foot.2026.102251`. Role: forefoot loading and PTI.

<a id="ref-cad-013"></a>
## REF-CAD-013 — Metatarsal pad placement in diabetic neuropathy
Hastings MK et al. *Effect of metatarsal pad placement on plantar pressure in people with diabetes mellitus and peripheral neuropathy.* Foot Ankle Int. 2007;28(1):84–88. PMID `17257544`; DOI `10.3113/FAI.2007.0015`. Locator: pp.84–88; Abstract—Results. Role: anatomical placement as measurable dose.

<a id="ref-cad-014"></a>
## REF-CAD-014 — Hallux-valgus metatarsal pad placement
Hakukawa S et al. *Optimal placement of metatarsal pads for patients with hallux valgus based on plantar pressure measurement.* Foot Ankle Surg. 2026;32(2):131–138. PMID `40707294`; DOI `10.1016/j.fas.2025.07.005`. Role: normalized placement is population-specific.

<a id="ref-cad-015"></a>
## REF-CAD-015 — Forefoot wedge dose response
Zhang X, Lam WK, Vanwanseele B. *Dose-response effects of forefoot and arch orthotic components on the center of pressure trajectory during running in pronated feet.* Gait Posture. 2022;92:212–217. PMID `34864487`; DOI `10.1016/j.gaitpost.2021.11.033`. Role: forefoot wedge dose.

<a id="ref-cad-016"></a>
## REF-CAD-016 — Insole configurations: pressure vs convenience
Guldemond NA et al. *The effects of insole configurations on forefoot plantar pressure and walking convenience in diabetic patients with neuropathic feet.* Clin Biomech. 2007;22(1):81–87. PMID `17046124`; DOI `10.1016/j.clinbiomech.2006.08.004`. Role: pressure vs comfort trade-off.

<a id="ref-cad-017"></a>
## REF-CAD-017 — Arch-support hardness
Chen H et al. *Biomechanical effects of varying arch support hardness in foot orthosis for adults with flexible flatfoot: A comprehensive Bayesian statistical analysis.* Gait Posture. 2026;125:110085. PMID `41455151`; DOI `10.1016/j.gaitpost.2025.110085`. Locator: Shore C 30/50/70. Role: hardness separate from geometry.

<a id="ref-cad-018"></a>
## REF-CAD-018 — Heel plug custom foot orthosis
Balsdon ME, Dombroski CE. *Custom-made foot orthoses with and without heel plugs and their effect on treatment outcomes and plantar pressures in patients with plantar fasciitis: A crossover study.* Prosthet Orthot Int. 2026;50(2):198–204. PMID `40366378`; DOI `10.1097/PXR.0000000000000450`. Locator: pp.198–204. Role: containment vs cushioning/material.

<a id="ref-cad-019"></a>
## REF-CAD-019 — Heel cup/arch pressure redistribution
*Effects of a range of 6 prefabricated orthotic insole designs on plantar pressure in a healthy population.* PMID `39140763`; DOI `10.1097/PXR.0000000000000292`. Role: heel-cup/arch pressure and contact-area effects.

<a id="ref-cad-020"></a>
## REF-CAD-020 — Inter-individual offloading response
*Pressure relief and load redistribution by custom-made insoles in diabetic patients with neuropathy and foot deformity.* PMID `15234488`. Role: patient-specific verification and load transfer.

<a id="ref-cad-021"></a>
## REF-CAD-021 — Graded stiffness heel offloading
*Graded stiffness offloading insoles better redistribute heel plantar pressure to protect the diabetic neuropathic foot.* PMID `36706604`. Role: regional stiffness and perimeter loading.

<a id="ref-cad-022"></a>
## REF-CAD-022 — Gradient lattice mapping 2026
Wang Lihong et al. *Optimization of pressure relief in gradient lattice orthotic insoles based on plantar pressure-rod diameter mapping.* Med Eng Phys. 2026. PMID `42049041`; DOI `10.1088/1873-4030/ae6593`. Role: R&D pressure→regional modulus mapping.

<a id="ref-cad-023"></a>
## REF-CAD-023 — Partition TPMS lattice 2026
*Design of novel orthotic insoles based on partition infilling of TPMS structures.* PMID `42147489`. Role: R&D region-specific lattice.

<a id="ref-cad-024"></a>
## REF-CAD-024 — 3D printed orthoses clinical outcomes review
Atallah H et al. *The current state of 3D-printed orthoses clinical outcomes: a systematic review.* BMC Musculoskelet Disord. 2025. PMID `40890671`; DOI `10.1186/s12891-025-09070-4`. Role: feasibility, comfort/fit and material/durability limitations.

<a id="ref-cad-025"></a>
## REF-CAD-025 — Assistive-device adherence
*Patient Compliance With Wearing Lower Limb Assistive Devices: A Scoping Review.* PMID `35753880`; DOI `10.1016/j.jmpt.2022.04.003`. Role: comfort/fit/adherence.

<a id="ref-cad-026"></a>
## REF-CAD-026 — PROM landscape
*Patient reported outcome measures in the foot and ankle literature: A systematic review.* PMID `41033023`; DOI `10.1016/j.foot.2025.102209`. Role: avoid a universal proprietary outcome score.

<a id="ref-cad-027"></a>
## REF-CAD-027 — Adult flatfoot evidence uncertainty
Herchenröder M et al. *Evidence for foot orthoses for adults with flatfoot: a systematic review.* J Foot Ankle Res. 2021;14:57. PMID `34844639`; PMCID `PMC8628393`; DOI `10.1186/s13047-021-00499-z`. Role: adult flatfoot evidence heterogeneity.

<a id="ref-cad-028"></a>
## REF-CAD-028 — Flexible-flatfoot PROM review
*Foot orthoses for flexible flatfeet in children and adults: a systematic review and meta-analysis of patient-reported outcomes.* PMID `36611153`; DOI `10.1186/s12891-022-06044-8`. Role: population-specific outcomes.

<a id="ref-cad-029"></a>
## REF-CAD-029 — Local offloading and neighbouring load transfer
Shuang J et al. *The effect of calcaneus and metatarsal head offloading insoles ...* PLoS One. 2024;19(5):e0303826. PMID `38758937`; PMCID `PMC11101073`; DOI `10.1371/journal.pone.0303826`. Locator: Fig.1, Fig.6. Role: safety-ring load transfer.

<a id="ref-cad-030"></a>
## REF-CAD-030 — Reduction and redistribution using orthoses
Kato H et al. *The reduction and redistribution of plantar pressures using foot orthoses in diabetic patients.* Diabetes Res Clin Pract. 1996;31:115–118. PMID `8792110`; DOI `10.1016/0168-8227(96)01214-4`. Role: total-contact redistribution/contact area.

<a id="ref-cad-031"></a>
## REF-CAD-031 — Rigid relief orthosis
Novick A et al. *Reduction of plantar pressure with the rigid relief orthosis.* J Am Podiatr Med Assoc. 1993;83(3):115–122. PMID `8468692`; DOI `10.7547/87507315-83-3-115`. Role: local relief and secondary-region effects.

<a id="ref-cad-032"></a>
## REF-CAD-032 — Pad shape can worsen peak pressure
Nordsiden L et al. *The effect of 3 foot pads on plantar pressure of pes planus foot type.* J Sport Rehabil. 2010;19(1):71–85. PMID `20231746`; DOI `10.1123/jsr.19.1.71`. Role: no relief primitive is intrinsically beneficial.

<a id="ref-cad-033"></a>
## REF-CAD-033 — Peak pressure vs PTI
*The value of reporting pressure-time integral data in addition to peak pressure data in studies on the diabetic foot: a systematic review.* PMID `23273847`; DOI `10.1016/j.clinbiomech.2012.12.002`. Role: retain PTI with peak pressure.

<a id="ref-cad-034"></a>
## REF-CAD-034 — In-shoe plantar pressure technology
Castro-Martins P et al. *In-shoe plantar pressure measurement technologies for the diabetic foot: A systematic review.* Heliyon. 2024;10(9):e29672. PMID `38699042`; PMCID `PMC11064085`; DOI `10.1016/j.heliyon.2024.e29672`. Role: device/calibration/protocol provenance.

<a id="ref-cad-035"></a>
## REF-CAD-035 — In-shoe measurement reliability, steps and speed
Kernozek TW et al. *Reliability of an in-shoe pressure measurement system during treadmill walking.* Foot Ankle Int. 1996;17(4):204–209. PMID `8696496`; DOI `10.1177/107110079601700404`. Locator: pp.204–209; Abstract. Role: speed and step-count awareness.

<a id="ref-cad-036"></a>
## REF-CAD-036 — Cross-system pressure comparability
Chockalingam N, Giacomozzi C, Healy A, Sacco ICNS. *Discrepancies between plantar pressure devices: Evaluating cross-system reliability for biomechanics, clinical use and predictive modelling.* Foot (Edinb). 2025;64:102190. PMID `40743570`; DOI `10.1016/j.foot.2025.102190`. Locator: Abstract—Methods/Results/Conclusions. Role: cross-device warning; several pressure/force/time metrics are not automatically interchangeable between systems.

<a id="ref-cad-037"></a>
## REF-CAD-037 — In-shoe pressure thresholds review
Jones P et al. *In-shoe pressure thresholds for people with diabetes and neuropathy at risk of ulceration: A systematic review.* J Diabetes Complications. 2021;35(3):107815. PMID `33280984`; DOI `10.1016/j.jdiacomp.2020.107815`. Role: context-bound thresholds.

<a id="ref-cad-038"></a>
## REF-CAD-038 — Plantar pressure thresholds review 2024
Castro-Martins P et al. *Plantar pressure thresholds as a strategy to prevent diabetic foot ulcers: A systematic review.* Heliyon. 2024;10(4):e26161. PMID `38390156`; PMCID `PMC10882031`; DOI `10.1016/j.heliyon.2024.e26161`. Role: threshold heterogeneity.

<a id="ref-cad-039"></a>
## REF-CAD-039 — Plantar shear measurement technologies
Rajala S, Lekkala J. *Plantar shear stress measurements — A review.* Clin Biomech. 2014;29(5):475–483. PMID `24820135`; DOI `10.1016/j.clinbiomech.2014.04.009`. Role: shear distinct from normal pressure.

<a id="ref-cad-040"></a>
## REF-CAD-040 — Plantar shear in diabetic foot
Jones AD et al. *Plantar shear stress in the diabetic foot: A systematic review and meta-analysis.* Diabet Med. 2022;39(1):e14661. PMID `34324731`; DOI `10.1111/dme.14661`. Role: measured shear outcome.

<a id="ref-cad-041"></a>
## REF-CAD-041 — Metatarsal domes in older people
Landorf KB et al. *Effects of metatarsal domes on plantar pressures in older people with a history of forefoot pain.* J Foot Ankle Res. 2020;13:18. PMID `32375847`; PMCID `PMC7201604`; DOI `10.1186/s13047-020-00388-x`. Role: placement/type/density.

<a id="ref-cad-042"></a>
## REF-CAD-042 — Metatarsal pad position in metatarsalgia
Hsi WL et al. *Optimum position of metatarsal pad in metatarsalgia for pressure relief.* Am J Phys Med Rehabil. 2005;84(7):514–520. PMID `15973088`; DOI `10.1097/01.phm.0000167680.70092.29`. Role: position relative to pressure peak.

<a id="ref-cad-043"></a>
## REF-CAD-043 — Forefoot pressure-relieving orthosis comparison
*Comparison of the Forefoot Pressure-Relieving Effects of Foot Orthoses.* PMID `36031787`. Role: compare pad/cushion effects.

<a id="ref-cad-044"></a>
## REF-CAD-044 — RA metatarsal bar/dome pressure and pain
Hodge MC et al. *Orthotic management of plantar pressure and pain in rheumatoid arthritis.* Clin Biomech. 1999;14(8):567–575. PMID `10521640`; DOI `10.1016/S0268-0033(99)00034-0`. Role: pressure and pain may rank designs differently.

## Arch-support deep-dive additions

<a id="ref-cad-045"></a>
## REF-CAD-045 — Arch support height dose FE
Peng Y et al. *Influence of arch support heights on the internal foot mechanics of flatfoot during walking: A muscle-driven finite element analysis.* Comput Biol Med. 2021;132:104355. PMID `33812264`; DOI `10.1016/j.compbiomed.2021.104355`. Role: height dose; **model evidence**.

<a id="ref-cad-046"></a>
## REF-CAD-046 — Arch × posting × heel cup × material FE
Peng Y et al. *Different Design Feature Combinations of Flatfoot Orthosis ... Taguchi Method.* Front Bioeng Biotechnol. 2022;10:853085. PMID `35360398`; PMCID `PMC8960448`; DOI `10.3389/fbioe.2022.853085`. Locator: Table 2; Results/Table 4. Role: interacting design factors; **model evidence**.

<a id="ref-cad-047"></a>
## REF-CAD-047 — 3D-printed arch hardness and comfort
Channasanon S et al. *3D-printed medial arch supports of varying hardness versus a prefabricated arch support on plantar pressure...* Prosthet Orthot Int. 2023;47(2):210–217. PMID `36037286`; DOI `10.1097/PXR.0000000000000178`. Role: hardness/comfort.

<a id="ref-cad-048"></a>
## REF-CAD-048 — Flatfoot plantar-pressure review 2026
Mahmoudiyan V et al. *Effects of conservative interventions on plantar pressure in individuals with flat foot: a systematic review and meta-analysis.* Sci Rep. 2026;16:9867. PMID `41714420`; PMCID `PMC13018568`; DOI `10.1038/s41598-026-40771-5`. Role: redistribution; medial-midfoot increase with insoles in pooled data.

<a id="ref-cad-049"></a>
## REF-CAD-049 — Arch support in hallux valgus
Farzadi M et al. *Effect of medial arch support foot orthosis on plantar pressure distribution in females with mild-to-moderate hallux valgus...* Prosthet Orthot Int. 2015;39(2):134–139. PMID `24515981`; DOI `10.1177/0309364613518229`. Role: population-specific redistribution.

<a id="ref-cad-050"></a>
## REF-CAD-050 — Arch height during cutting
Toyooka S et al. *Association of medial arch support ... knee valgus ... cutting maneuvers in female athletes.* 2022. PMID `36536460`; PMCID `PMC9762016`; DOI `10.1186/s13102-022-00608-w`. Role: task-specific human height dose.

<a id="ref-cad-051"></a>
## REF-CAD-051 — Arch support and lateral-column load in sport
Yu B et al. *Effects of wearing foot orthosis with medial arch support on the fifth metatarsal loading and ankle inversion angle in selected basketball tasks.* PMID `17469671`; DOI `10.2519/jospt.2007.2327`. Role: remote load monitoring.

<a id="ref-cad-052"></a>
## REF-CAD-052 — Soft vs hard printed arch support RCT
Paecharoen S et al. *Effectiveness of a 3D-printed silicone medial arch support on foot pain in individuals with pes planus.* Ann Phys Rehabil Med. 2025;68(7):102007. PMID `40819420`; DOI `10.1016/j.rehab.2025.102007`. Role: pain/function vs pressure.

<a id="ref-cad-053"></a>
## REF-CAD-053 — Arch reinforcement/undercut
Cheng KW et al. *A Three-Dimensional Printed Foot Orthosis for Flexible Flatfoot: ... Reinforcement and Undercut.* Materials. 2021;14:5297. PMID `34576526`; PMCID `PMC8469370`; DOI `10.3390/ma14185297`. Role: geometry/stiffness separation.

<a id="ref-cad-054"></a>
## REF-CAD-054 — Arch support and plantar fasciitis 2026
Taseh A et al. *Arch-supports and plantar fasciitis...* J Exp Orthop. 2026;13:e70732. PMID `42130670`; DOI `10.1002/jeo2.70732`. Role: short-term clinical/structural evidence.

<a id="ref-cad-055"></a>
## REF-CAD-055 — Arch support pressure/contact area in flatfoot
Huang YP et al. *The arch support insoles show benefits to people with flatfoot...* PLoS One. 2020;15:e0237382. PMID `32817709`; PMCID `PMC7446821`; DOI `10.1371/journal.pone.0237382`. Role: pressure/contact-area redistribution.

<a id="ref-cad-056"></a>
## REF-CAD-056 — Arch correction under different loads
Lavoie-Turcotte T et al. *Flatfoot arch correction with generic 3D-printed orthoses at different body weight percentages.* Foot. 2024;59:102093. PMID `38520781`; DOI `10.1016/j.foot.2024.102093`. Role: structural outcome depends on loading condition.

<a id="ref-cad-057"></a>
## REF-CAD-057 — Structural medial arch support outcome
Escalona-Marfil C et al. *A radiographic and anthropometric study ... medial longitudinal arch.* J Foot Ankle Res. 2014;7:38. PMID `25317208`; PMCID `PMC4196133`; DOI `10.1186/s13047-014-0038-5`. Role: structural arch outcome.

## Heel / rearfoot deep-dive additions

<a id="ref-cad-058"></a>
## REF-CAD-058 — Individualized 3D-printed heel cup
Li L et al. *3D printing individualized heel cup for improving the self-reported pain of plantar fasciitis.* J Transl Med. 2018;16:167. DOI `10.1186/s12967-018-1547-y`. Locator: Methods—design/fabrication. Role: scan-derived heel-cup geometry; 5 mm was study-specific, not a default.

<a id="ref-cad-059"></a>
## REF-CAD-059 — Plastic heel cup confinement
Lin CY et al. *Biomechanical Effects of Plastic Heel Cup on Plantar Fasciitis Patients Evaluated by Ultrasound Shear Wave Elastography.* J Clin Med. 2022;11:2150. PMID `35456242`; PMCID `PMC9028113`; DOI `10.3390/jcm11082150`. Role: confinement mechanism.

<a id="ref-cad-060"></a>
## REF-CAD-060 — Heel cup in Sever's disease
Perhamre S et al. *A heel cup improves the function of the heel pad in Sever's injury...* Scand J Med Sci Sports. 2012;22(4):516–522. PMID `21410537`; DOI `10.1111/j.1600-0838.2010.01266.x`. **Pediatric evidence.**

<a id="ref-cad-061"></a>
## REF-CAD-061 — Heel cup versus wedge in Sever's disease
Perhamre S et al. *Sever's injury; treat it with a heel cup: a randomized, crossover study...* Scand J Med Sci Sports. 2011;21(6):e42–e47. PMID `20673253`; DOI `10.1111/j.1600-0838.2010.01140.x`. **Pediatric evidence.**

<a id="ref-cad-062"></a>
## REF-CAD-062 — Prefabricated vs custom in plantar fasciitis
Pfeffer G et al. *Comparison of custom and prefabricated orthoses in the initial treatment of proximal plantar fasciitis.* Foot Ankle Int. 1999;20(4):214–221. PMID `10229276`; DOI `10.1177/107110079902000402`. Role: custom is not automatically superior.

<a id="ref-cad-063"></a>
## REF-CAD-063 — Heel conformity/thickness/material FE
Goske S et al. *Reduction of plantar heel pressures: Insole design using finite element analysis.* J Biomech. 2006;39(13):2363–2370. PMID `16197952`; DOI `10.1016/j.jbiomech.2005.08.006`. Role: conformity, thickness, material; **model evidence**.

<a id="ref-cad-064"></a>
## REF-CAD-064 — Subject-specific cushioning model
Chatzistergos PE et al. *A method for subject-specific modelling and optimisation of the cushioning properties of insole materials used in diabetic footwear.* Med Eng Phys. 2015;37(6):531–538. PMID `25937545`; DOI `10.1016/j.medengphy.2015.03.009`. **Model/diabetic context.**

<a id="ref-cad-065"></a>
## REF-CAD-065 — Pressure-guided CAD/CAM orthosis in plantar fasciitis
Nakhaee M et al. *The effects of a custom foot orthosis on dynamic plantar pressure in patients with chronic plantar fasciitis: A randomized controlled trial.* Prosthet Orthot Int. 2023;47(3):241–252. PMID `36037272`; DOI `10.1097/PXR.0000000000000179`. Role: pressure + ultrasound + PROM outcomes.

<a id="ref-cad-066"></a>
## REF-CAD-066 — Plantar heel pain orthoses meta-analysis
Whittaker GA et al. *Foot orthoses for plantar heel pain: a systematic review and meta-analysis.* Br J Sports Med. 2018;52(5):322–328. PMID `28935689`; DOI `10.1136/bjsports-2016-097355`. Role: small medium-term pain benefit; no clear custom superiority.

<a id="ref-cad-067"></a>
## REF-CAD-067 — Heel cup in multimodal plantar-fasciopathy care
Riel H et al. *Does a corticosteroid injection plus exercise or exercise alone add to ... advice and a heel cup ...?* Br J Sports Med. 2023;57(18):1180–1186. PMID `37414460`; PMCID `PMC10579183`; DOI `10.1136/bjsports-2023-106948`. Role: multimodal context, not isolated cup-dose evidence.

## Use-case / population-profile additions

<a id="ref-cad-068"></a>
## REF-CAD-068 — Diabetic footwear offloading × adherence RCT
Bus SA et al. *Effect of custom-made footwear on foot ulcer recurrence in diabetes: a multicenter randomized controlled trial.* Diabetes Care. 2013;36(12):4109–4116. PMID `24130357`; PMCID `PMC3836114`; DOI `10.2337/dc13-0996`. Locator: pp.4109–4116; Abstract—Results/Conclusions. Role: adherence is outcome-critical.

<a id="ref-cad-069"></a>
## REF-CAD-069 — CareFUL pressure-based orthoses RCT
Ulbrecht JS et al. *Prevention of recurrent foot ulcers with plantar pressure-based in-shoe orthoses: the CareFUL prevention multicenter randomized controlled trial.* Diabetes Care. 2014;37(7):1982–1989. PMID `24760263`; PMCID `PMC4067390`; DOI `10.2337/dc13-2956`. Role: shape + pressure-based orthoses in high-risk population.

<a id="ref-cad-070"></a>
## REF-CAD-070 — Continuous pressure feedback and diabetic re-ulceration
Abbott CA et al. *Innovative intelligent insole system reduces diabetic foot ulcer recurrence at plantar sites: a prospective, randomised, proof-of-concept study.* Lancet Digit Health. 2019;1(6):e308–e318. PMID `33323253`; DOI `10.1016/S2589-7500(19)30128-1`. Role: P2 continuous pressure monitoring/feedback direction.

<a id="ref-cad-071"></a>
## REF-CAD-071 — DIASSIST adherence RCT 2026
Vossen LE et al. *An Integrated Personalized Multimodal Intervention Improves Adherence to Wearing Custom-Made Footwear in People With Diabetes at High Foot Ulcer Risk: A Multicenter Randomized Controlled Trial (DIASSIST).* Diabetes Care. 2026;49(8):1384–1394. PMID `42247281`; DOI `10.2337/dc25-3113`. Role: adherence intervention.

<a id="ref-cad-072"></a>
## REF-CAD-072 — Custom orthoses for forefoot pain review
Arias-Martín I et al. *Effectiveness of custom-made foot orthoses for treating forefoot pain: a systematic review.* Int Orthop. 2018;42(8):1865–1875. PMID `29423640`; DOI `10.1007/s00264-018-3817-y`. Role: heterogeneous forefoot conditions.

<a id="ref-cad-073"></a>
## REF-CAD-073 — Flatfoot network meta-analysis
Shim SR et al. *Optimizing Flatfoot Management With Foot Orthoses: A Systemic Review and Meta-analysis.* Am J Phys Med Rehabil. 2026;105(3):230–237. PMID `41065643`; DOI `10.1097/PHM.0000000000002833`. Role: RCT synthesis; age/population boundaries remain essential.

<a id="ref-cad-074"></a>
## REF-CAD-074 — Plantar fasciitis orthoses RCT meta-analysis 2026
Wang D et al. *Efficacy and safety of foot orthoses for improving pain and function in patients with plantar fasciitis: a systematic review and meta-analysis of randomized controlled trials.* Disabil Rehabil. 2026;48(5):1231–1245. PMID `40999841`; DOI `10.1080/09638288.2025.2563763`. Role: separate pain/function outcomes.

<a id="ref-cad-075"></a>
## REF-CAD-075 — Running biomechanics orthoses meta-analysis 2024
Jor A et al. *Effects of foot orthoses on running kinetics and kinematics: A systematic review and meta-analysis.* Gait Posture. 2024;109:240–258. PMID `38367456`; DOI `10.1016/j.gaitpost.2024.02.003`. Role: running pressure/comfort/kinematic/economy trade-offs.

<a id="ref-cad-076"></a>
## REF-CAD-076 — Orthoses and injury prevention meta-analysis
Bonanno DR et al. *Effectiveness of foot orthoses and shock-absorbing insoles for the prevention of injury: a systematic review and meta-analysis.* Br J Sports Med. 2017;51(2):86–96. PMID `27919918`; DOI `10.1136/bjsports-2016-096671`. Role: injury-prevention signal with heterogeneous trial quality.

<a id="ref-cad-077"></a>
## REF-CAD-077 — Footwear comfort and running economy
Van Alsenoy K et al. *Increased footwear comfort is associated with improved running economy - a systematic review and meta-analysis.* Eur J Sport Sci. 2023;23(1):121–133. PMID `34726119`; DOI `10.1080/17461391.2021.1998642`. Role: comfort is a meaningful sport outcome.

<a id="ref-cad-078"></a>
## REF-CAD-078 — Running with asymptomatic flatfoot meta-analysis
Jor A et al. *Effects of foot orthoses on lower extremity joint kinematics and kinetics in runners with asymptomatic flatfeet: A systematic review and meta-analysis.* Gait Posture. 2025;121:281–294. PMID `40516166`; DOI `10.1016/j.gaitpost.2025.06.003`. Role: running-flatfoot subtype and design interaction.

<a id="ref-cad-079"></a>
## REF-CAD-079 — Bone-stress injury prevention review
Lavigne A et al. *The Role of Footwear, Foot Orthosis, and Training-Related Strategies in the Prevention of Bone Stress Injuries: A Systematic Review and Meta-Analysis.* Int J Exerc Sci. 2023;16(3):721–743. PMID `37649463`; PMCID `PMC10464778`; DOI `10.70252/ZNRS2138`. Role: low-quality/military-heavy BSI evidence.

## PROM / comfort / fit / adherence additions

<a id="ref-cad-080"></a>
## REF-CAD-080 — Foot Health Status Questionnaire development
Bennett PJ et al. *Development and validation of a questionnaire designed to measure foot-health status.* J Am Podiatr Med Assoc. 1998;88(9):419–428. PMID `9770933`; DOI `10.7547/87507315-88-9-419`. Role: FHSQ foot-health PROM.

<a id="ref-cad-081"></a>
## REF-CAD-081 — Foot Function Index development
Budiman-Mak E et al. *The Foot Function Index: a measure of foot pain and disability.* J Clin Epidemiol. 1991;44(6):561–570. PMID `2037861`; DOI `10.1016/0895-4356(91)90220-4`. Role: pain/disability/activity-restriction PROM.

<a id="ref-cad-082"></a>
## REF-CAD-082 — FFI measurement-properties review
*Measurement properties of the Foot Function Index (FFI) questionnaire: A systematic review.* PMID `38856157`. Role: version/adaptation-specific measurement governance.

<a id="ref-cad-083"></a>
## REF-CAD-083 — FAAM development
Martin RL et al. *Evidence of validity for the Foot and Ankle Ability Measure (FAAM).* Foot Ankle Int. 2005;26(11):968–983. PMID `16309613`; DOI `10.1177/107110070502601113`. Role: ADL/Sport function domains.

<a id="ref-cad-084"></a>
## REF-CAD-084 — Italian 17-item FFI
Venditto T et al. *17-Italian Foot Function Index with numerical rating scale...* Foot. 2015;25(1):12–18. PMID `25641642`; DOI `10.1016/j.foot.2014.09.004`. Role: Italian validated FFI candidate.

<a id="ref-cad-085"></a>
## REF-CAD-085 — Italian FAAM ADL validation
*Foot and ankle ability measure: cross-cultural translation and validation of the Italian version of the ADL module (FAAM-I/ADL).* PMID `25134631`. Role: Italian FAAM ADL candidate.

<a id="ref-cad-086"></a>
## REF-CAD-086 — EFAS Score multilingual PROM
Richter M et al. *EFAS Score - Multilingual development and validation of a patient-reported outcome measure (PROM)...* Foot Ankle Surg. 2018. PMID `29933960`; DOI `10.1016/j.fas.2018.05.004`. Role: short multilingual candidate incl. Italian; current redistribution terms still require review.

<a id="ref-cad-087"></a>
## REF-CAD-087 — Reliable footwear comfort during running
Mündermann A et al. *Development of a reliable method to assess footwear comfort during running.* Gait Posture. 2002;16(1):38–45. PMID `12127185`; DOI `10.1016/S0966-6362(01)00197-7`. Role: protocol-dependent comfort measurement.

<a id="ref-cad-088"></a>
## REF-CAD-088 — Meaningful footwear comfort scales
Mills K et al. *Identifying clinically meaningful tools for measuring comfort perception of footwear.* PMID `20216463`. Role: scale reliability and context-specific change interpretation.

<a id="ref-cad-089"></a>
## REF-CAD-089 — Footwear comfort synthesis
*Footwear comfort: a systematic search and narrative synthesis of the literature.* PMID `34876192`. Role: multifactorial task/population-dependent comfort.

<a id="ref-cad-090"></a>
## REF-CAD-090 — RUN-CAT comfort instrument
*The running shoe comfort assessment tool (RUN-CAT)...* PMID `32508250`; DOI `10.1080/02640414.2020.1773613`. Role: task-specific multidimensional running-footwear comfort instrument.

<a id="ref-cad-091"></a>
## REF-CAD-091 — Therapeutic-footwear adherence measurement review
*Usability of Different Methods to Assess and Improve Adherence to Therapeutic Footwear in Persons with the Diabetic Foot in Remission. A Systematic Review.* PMID `37545201`. Role: objective vs subjective adherence.

<a id="ref-cad-092"></a>
## REF-CAD-092 — Footwear adherence metric validation
*Adherence and Wearing Time of Prescribed Footwear among People at Risk of Diabetes-Related Foot Ulcers: Which Measure to Use?* Sensors. 2023. PMID `36772691`; PMCID `PMC9919850`; DOI `10.3390/s23031648`. Role: weight-bearing/step denominator validity.

<a id="ref-cad-093"></a>
## REF-CAD-093 — Plantar-heel-pain MID for VAS/FHSQ
*Revised minimal important difference values for the visual analogue scale and Foot Health Status Questionnaire when used for plantar heel pain.* PMID `39682003`; PMCID `PMC11649508`; DOI `10.1002/jfa2.70021`. Role: MID is instrument/domain/population/context-specific.

## Material durability / manufacturing additions

<a id="ref-cad-094"></a>
## REF-CAD-094 — Orthotic materials and plantar pressure systematic review
Gerrard JM, Bonanno DR, Whittaker GA, Landorf KB. *Effect of different orthotic materials on plantar pressures: a systematic review.* J Foot Ankle Res. 2020;13(1):35. PMID `32527296`; PMCID `PMC7291735`; DOI `10.1186/s13047-020-00401-3`. Locator: Abstract—Methods/Results/Conclusion; full article. Role: limited heterogeneous evidence for PU/PORON, PE/Plastazote and EVA pressure effects; motivates explicit material density/hardness/thickness provenance rather than a universal material ranking.

<a id="ref-cad-095"></a>
## REF-CAD-095 — Dual-density orthotic material cyclic durability
Brodsky JW, Pollo FE, Cheleuitte D, Baum BS. *Physical properties, durability, and energy-dissipation function of dual-density orthotic materials used in insoles for diabetic patients.* Foot Ankle Int. 2007;28(8):880–889. PMID `17697652`; DOI `10.3113/FAI.2007.0880`. Locator: pp.880–889; Abstract—Methods/Results. Role: five multilayer combinations tested over 100,000 cycles; pressure/elastic-deformation response changed differently by combination.

<a id="ref-cad-096"></a>
## REF-CAD-096 — Heating changes insole material mechanical properties
Brodsky JW, Brajtbord J, Coleman SC, Raut S, Polo FE. *Effect of heating on the mechanical properties of insole materials.* Foot Ankle Int. 2012;33(9):772–778. PMID `22995267`; DOI `10.3113/FAI.2012.0772`. Locator: pp.772–778; Abstract—Methods/Results/Conclusion. Role: tested heated combinations became stiffer and changed stress-strain/force-transmission behavior; post-processing must be traceable.

<a id="ref-cad-097"></a>
## REF-CAD-097 — Physical properties of diabetic orthotic materials
Paton J, Jones RB, Stenhouse E, Bruce G. *The physical characteristics of materials used in the manufacture of orthoses for patients with diabetes.* Foot Ankle Int. 2007;28(10):1057–1063. PMID `17923055`; DOI `10.3113/FAI.2007.1057`. Locator: pp.1057–1063; Abstract—Methods/Results. Role: density, resilience, stiffness, friction, durability and compression-set testing across common materials; no single property is sufficient for suitability.

<a id="ref-cad-098"></a>
## REF-CAD-098 — Personalized lattice orthosis workflow and material testing
Hudak G et al. *A novel workflow to fabricate a patient-specific 3D printed accommodative foot orthosis with personalized latticed metamaterial.* Med Eng Phys. 2022. PMID `35641072`; DOI `10.1016/j.medengphy.2022.103802`. Locator: Abstract; full-text material/durability methods when consulted. Role: regionally varied lattice stiffness plus durability, shear-stiffness and compressive-stiffness testing; base resin and effective structure must be distinct.

<a id="ref-cad-099"></a>
## REF-CAD-099 — Subject-specific cushioning stiffness optimization
Chatzistergos PE, Naemi R, Healy A, Gerth P, Chockalingam N. *Subject Specific Optimisation of the Stiffness of Footwear Material for Maximum Plantar Pressure Reduction.* Ann Biomed Eng. 2017;45(8):1929–1940. PMID `28484892`; PMCID `PMC5527058`; DOI `10.1007/s10439-017-1826-4`. Locator: pp.1929–1940; Abstract—Results. Role: optimal tested cushioning stiffness depended on compressive load/body mass in the studied setting; supports load-dependent stiffness metadata, not a universal rule.

<a id="ref-cad-100"></a>
## REF-CAD-100 — Polyethylene foam load-bearing and incomplete recovery
Kuncir EJ, Wirta RW, Golbranson FL. *Load-bearing characteristics of polyethylene foam: an examination of structural and compression properties.* J Rehabil Res Dev. 1990;27(3):229–238. PMID `2401954`; DOI `10.1682/jrrd.1990.07.0229`. Locator: pp.229–238; Abstract. Role: time/cyclic behavior, thickness and foam structure affect pressure response; sustained loading can damage cellular integrity and prevent full thickness recovery.

<a id="ref-cad-101"></a>
## REF-CAD-101 — Multidensity orthotic materials over 100,000 cycles
Foto JG, Birke JA. *Evaluation of multidensity orthotic materials used in footwear for patients with diabetes.* Foot Ankle Int. 1998;19(12):836–841. PMID `9872471`; DOI `10.1177/107110079801901208`. Locator: pp.836–841; Abstract. Role: all tested multidensity combinations lost performance over 100,000 cycles, with greatest losses during the first 10,000 cycles in this test.

<a id="ref-cad-102"></a>
## REF-CAD-102 — Objective foot-orthosis stiffness/compression-set/shape measurement
Cuppens K et al. *Using a texture analyser to objectively quantify foot orthoses.* Annu Int Conf IEEE Eng Med Biol Soc. 2019:5348–5351. PMID `31947064`; DOI `10.1109/EMBC.2019.8857318`. Locator: pp.5348–5351; Abstract—Technique/Discussion. Role: stiffness, compression set and shape can be measured at anatomical landmark locations; orthosis behavior is not determined by material alone.

<a id="ref-cad-103"></a>
## REF-CAD-103 — 12-month functional/physical insole durability
Paton JS, Stenhouse E, Bruce G, Jones R. *A longitudinal investigation into the functional and physical durability of insoles used for the preventive management of neuropathic diabetic feet.* J Am Podiatr Med Assoc. 2014;104(1):50–57. PMID `24504577`; DOI `10.7547/0003-0538-104.1.50`. Locator: pp.50–57; Abstract—Results/Conclusions. Role: material depth changed over time while functional pressure reduction did not map trivially to visual compression; replacement should not rely on appearance alone.

<a id="ref-cad-104"></a>
## REF-CAD-104 — Physical, shear/friction and thermal comfort material testing
Lo WT, Yick KL, Ng SP, Yip J. *New methods for evaluating physical and thermal comfort properties of orthotic materials used in insoles for patients with diabetes.* J Rehabil Res Dev. 2014;51(2):311–324. PMID `24933729`; DOI `10.1682/JRRD.2013.01.0012`. Locator: pp.311–324; Abstract. Role: force/compression, friction, shear and thermal/moisture properties are distinct material-performance dimensions.

<a id="ref-cad-105"></a>
## REF-CAD-105 — Daily-use aging, pressure, shear and material stiffness
Lavery LA et al. *Wear and biomechanical characteristics of a novel shear-reducing insole with implications for high-risk persons with diabetes.* Diabetes Technol Ther. 2005;7(4):638–646. PMID `16120040`; DOI `10.1089/dia.2005.7.638`. Locator: pp.638–646; Abstract—Methods/Results. Role: pressure, shear and material stiffness were measured prospectively during use; multilayer interface design can change shear independently of peak pressure.

<a id="ref-cad-106"></a>
## REF-CAD-106 — 3D-printed vs traditional FO dimensional realization
Ho M et al. *Immediate comfort perception of 3D-printed foot orthoses in individuals with unilateral heel pain.* Prosthet Orthot Int. 2022;46(1):31–36. PMID `35179521`; PMCID `PMC8865620`; DOI `10.1097/PXR.0000000000000068`. Locator: pp.31–36; Table 1 / Figs.1–2. Role: 3D-printed and traditionally fabricated orthoses from the studied workflow differed in width, arch dimensions and heel-cup height; actual manufactured geometry should be measured rather than assumed identical to design intent.

<a id="ref-cad-107"></a>
## REF-CAD-107 — H/M1/M5 anatomical registration for COP
Wevers OT, Hearn TC, Hunter GA, Ala-Korpi T. *Method for relating the centre of pressure locus during dynamic stance to the anatomical structure of the foot.* Clin Biomech (Bristol). 1989;4(2):111–114. PMID `23916003`; DOI `10.1016/0268-0033(89)90048-X`. Locator: pp.111–114; Abstract. Role: historical method relating COP to anatomical references using the posterior calcaneus and first/fifth metatarsal heads; supports landmark semantics, not a universal modern registration tolerance.

## Integration / measurement provenance additions

<a id="ref-cad-108"></a>
## REF-CAD-108 — Step count and protocol validity for in-shoe pressure
Arts MLJ, Bus SA. *Twelve steps per foot are recommended for valid and reliable in-shoe plantar pressure data in neuropathic diabetic patients wearing custom made footwear.* Clin Biomech (Bristol, Avon). 2011;26(8):880–884. PMID `21641098`; DOI `10.1016/j.clinbiomech.2011.05.001`. Locator: pp.880–884; Abstract—Background/Methods/Findings/Interpretation. Role: demonstrates that included step count affects validity/reliability for regional pressure metrics in this specific neuropathic-diabetic/custom-footwear protocol. The 12-step result is **not** a universal BiomechE-CAD constant.

<a id="ref-cad-109"></a>
## REF-CAD-109 — Comparative technical assessment of plantar-pressure devices
Giacomozzi C. *Appropriateness of plantar pressure measurement devices: a comparative technical assessment.* Gait Posture. 2010;32(1):141–144. PMID `20399101`; DOI `10.1016/j.gaitpost.2010.03.014`. Locator: pp.141–144; Abstract. Role: device technology, calibration, accuracy, hysteresis, creep and COP performance affect measurement qualification; supports explicit device/calibration provenance rather than assumed equivalence.

<a id="ref-cad-110"></a>
## REF-CAD-110 — Hardware qualification of baropodometric sensor systems
Giacomozzi C. *Hardware performance assessment recommendations and tools for baropodometric sensor systems.* Ann Ist Super Sanita. 2010;46(2):158–167. PMID `20567067`; DOI `10.4415/ANN_10_02_09`. Locator: pp.158–167; Abstract. Role: methods/recommendations for technical performance assessment of plantar-pressure hardware; supports product/device qualification but does not provide a universal orthosis acceptance tolerance.

<a id="ref-cad-111"></a>
## REF-CAD-111 — Biomedical/translational provenance framework
Sahoo SS, Nguyen V, Bodenreider O, Parikh P, Minning T, Sheth AP. *A unified framework for managing provenance information in translational research.* BMC Bioinformatics. 2011;12:461. PMID `22126369`; PMCID `PMC3298549`; DOI `10.1186/1471-2105-12-461`. Locator: Abstract—Background/Results/Conclusions; full article. Role: provenance records origin/history and processing so researchers can verify data quality, reproduce results and validate scientific processes; supports structured domain-aware provenance.

<a id="ref-cad-112"></a>
## REF-CAD-112 — Biomedical data-provenance scoping review
Johns M, Meurers T, Wirth FN, Haber AC, Müller A, Halilovic M, Balzer F, Prasser F. *Data Provenance in Biomedical Research: Scoping Review.* J Med Internet Res. 2023;25:e42289. PMID `36972116`; PMCID `PMC10132013`; DOI `10.2196/42289`. Locator: Abstract—Results/Conclusions. Role: documents heterogeneous provenance approaches and limited uptake of established standards such as PROV; supports a consistent internal provenance contract and benchmarking/validation.

<a id="ref-cad-113"></a>
## REF-CAD-113 — FAIR data principles and detailed provenance
Wilkinson MD et al. *The FAIR Guiding Principles for scientific data management and stewardship.* Sci Data. 2016;3:160018. DOI `10.1038/sdata.2016.18`. Locator: Box 2, especially `I3` qualified references and `R1.2` detailed provenance; `The Principles precede implementation`. Role: supports qualified links between data/metadata and detailed provenance while remaining implementation-neutral; FAIR is guidance, not a specific storage technology.

---

# D. Standards / test-method / interoperability / regulatory / human-factors references

**Scope note:** a standards or guidance entry documents terminology, test, interoperability, qualification, regulatory or human-factors semantics available from the official source. It does **not** mean BiomechE-CAD automatically claims conformance, certification, legal classification or a universal acceptance threshold. Full conformance/applicability decisions require their own controlled assessment and, for paid standards, controlled access to the licensed text.

<a id="std-iso-868-2003"></a>
## STD-ISO-868-2003 — Shore durometer hardness
- **Standard:** ISO 868:2003, *Plastics and ebonite — Determination of indentation hardness by means of a durometer (Shore hardness).* Edition 3.
- **Official URL:** https://www.iso.org/standard/34804.html
- **Locator:** official Abstract/Scope.
- **Recorded scope point:** type A for softer and type D for harder materials; empirical control method; no simple relationship to a fundamental property.
- **Role:** hardness values require scale/method and must not be silently converted to modulus.

<a id="std-iso-1856-2018"></a>
## STD-ISO-1856-2018 — Flexible cellular material compression set
- **Standard:** ISO 1856:2018, *Flexible cellular polymeric materials — Determination of compression set.* Edition 4; confirmed current in 2024.
- **Official URL:** https://www.iso.org/standard/70213.html
- **Locator:** official Abstract/Scope.
- **Role:** compression-set test semantics for flexible cellular materials; not an automatic medical acceptance threshold.

<a id="std-iso-3385-2014"></a>
## STD-ISO-3385-2014 — Constant-load fatigue of flexible cellular materials
- **Standard:** ISO 3385:2014, *Flexible cellular polymeric materials — Determination of fatigue by constant-load pounding.* Edition 4; confirmed current in 2025.
- **Official URL:** https://www.iso.org/standard/55743.html
- **Locator:** official Abstract/Scope.
- **Role:** loss-in-thickness/hardness fatigue semantics under constant-load pounding; test results are related to but not necessarily identical to field-service loss.

<a id="std-iso-24999-2008"></a>
## STD-ISO-24999-2008 — Constant-strain fatigue of flexible cellular materials
- **Standard:** ISO 24999:2008, *Flexible cellular polymeric materials — Determination of fatigue by a constant-strain procedure.* Edition 1; reviewed/confirmed 2026.
- **Official URL:** https://www.iso.org/standard/42737.html
- **Locator:** official Abstract/Scope.
- **Role:** complementary constant-strain fatigue semantics and manufacturing QC.

<a id="std-iso-3386-1-2025"></a>
## STD-ISO-3386-1-2025 — Flexible cellular compression stress-strain
- **Standard:** ISO 3386-1:2025, *Polymeric materials, cellular flexible — Determination of stress-strain characteristics in compression — Part 1: Low-density materials.* Edition 3.
- **Official URL:** https://www.iso.org/standard/89164.html
- **Locator:** official Abstract/Scope.
- **Role:** compression stress-strain and compression-stress-value measurement for low-density flexible cellular materials.

<a id="std-isoastm-52901-2017"></a>
## STD-ISOASTM-52901-2017 — Purchased AM part requirements
- **Standard:** ISO/ASTM 52901:2017, *Additive manufacturing — General principles — Requirements for purchased AM parts.* Edition 1; confirmed current in 2023.
- **Official URL:** https://www.iso.org/standard/67288.html
- **Locator:** official Abstract/Scope.
- **Role:** traceable exchange of part definition, feedstock, final characteristics/properties, inspection and acceptance methods.

<a id="std-isoastm-52902-2023"></a>
## STD-ISOASTM-52902-2023 — AM geometric capability test artefacts
- **Standard:** ISO/ASTM 52902:2023, *Additive manufacturing — Test artefacts — Geometric capability assessment of additive manufacturing systems.* Edition 2; supersedes withdrawn 2019 edition.
- **Official URL:** https://www.iso.org/standard/79683.html
- **Locator:** official Abstract/Scope.
- **Role:** system geometric capability/calibration test-artifact semantics; does not define a universal orthosis tolerance.

<a id="std-isoastm-52903-1-2020"></a>
## STD-ISOASTM-52903-1-2020 — Polymer MEX feedstock requirements
- **Standard:** ISO/ASTM 52903-1:2020, *Additive manufacturing — Material extrusion-based additive manufacturing of plastic materials — Part 1: Feedstock materials.* Edition 1.
- **Official URL:** https://www.iso.org/standard/67290.html
- **Locator:** official Abstract/Scope.
- **Role:** feedstock/material requirement semantics for plastic material-extrusion AM.

<a id="std-isoastm-52920-2023"></a>
## STD-ISOASTM-52920-2023 — AM process/production-site qualification
- **Standard:** ISO/ASTM 52920:2023, *Additive manufacturing — Qualification principles — Requirements for industrial additive manufacturing processes and production sites.* Edition 1.
- **Official URL:** https://www.iso.org/standard/76911.html
- **Locator:** official Abstract/Scope.
- **Role:** quality-relevant process/site qualification principles independent of AM material/method.

<a id="std-isoastm-52924-2023"></a>
## STD-ISOASTM-52924-2023 — Polymer AM part-property classification
- **Standard:** ISO/ASTM 52924:2023, *Additive manufacturing of polymers — Qualification principles — Classification of part properties.* Edition 1.
- **Official URL:** https://www.iso.org/standard/76909.html
- **Locator:** official Abstract/Scope.
- **Role:** mechanical, physical and geometrical part-property classification for thermoplastic polymer PBF/MEX processes.

<a id="std-iso-17295-2023"></a>
## STD-ISO-17295-2023 — AM positioning, coordinates and orientation
- **Standard:** ISO 17295:2023, *Additive manufacturing — General principles — Part positioning, coordinates and orientation.* Edition 1; supersedes withdrawn ISO/ASTM 52921:2013.
- **Official URL:** https://www.iso.org/standard/76471.html
- **Locator:** official Abstract/Scope.
- **Role:** explicit build positioning/orientation/coordinate vocabulary for manufacturing provenance.

<a id="std-isoiec-25422-2025"></a>
## STD-ISOIEC-25422-2025 — 3D Manufacturing Format (3MF) specification suite
- **Standard:** ISO/IEC 25422:2025, *Information technology — 3D Manufacturing Format (3MF) specification suite.* Edition 1; published 2025-06.
- **Official URL:** https://www.iso.org/standard/90283.html
- **Locator:** official Abstract/Scope.
- **Role:** current standardized 3MF carrier-suite context. It supports format-capability reasoning, but does not make 3MF the BiomechE-CAD semantic authority or prove that every project semantic is preserved by a given exporter/importer.

<a id="std-isoastm-52915-2020"></a>
## STD-ISOASTM-52915-2020 — Additive Manufacturing File Format (AMF) v1.2
- **Standard:** ISO/ASTM 52915:2020, *Specification for additive manufacturing file format (AMF) Version 1.2.* Edition 3; published 2020-03; confirmed current in 2026.
- **Official URL:** https://www.iso.org/standard/74640.html
- **Locator:** official Abstract/Scope.
- **Role:** AM interchange-carrier semantics. Carrier support does not replace a project/manufacturing manifest, provenance, integrity policy or explicit information-loss declaration.

<a id="std-isoastm-52951-2026"></a>
## STD-ISOASTM-52951-2026 — Data packages for AM parts
- **Standard:** ISO/ASTM 52951:2026, *Additive manufacturing — Data — Data packages for AM parts.* Edition 1; published 2026-06.
- **Official URL:** https://www.iso.org/standard/76828.html
- **Locator:** official Abstract/Scope.
- **Recorded scope point:** establishes methods/parameter sets/models for a part data package across the AM workflow from design to acceptance and a referenceable digital thread; the detailed requirements are based on PBF-LB/M, while generalized workflow concepts may apply more broadly.
- **Role:** supports traceable design→manufacture→acceptance package semantics. It does not by itself qualify a BiomechE-CAD polymer-AM or CNC process.

<a id="std-iso-14971-2019"></a>
## STD-ISO-14971-2019 — Medical-device risk management
- **Standard:** ISO 14971:2019, *Medical devices — Application of risk management to medical devices.* Edition 3; confirmed current in 2025.
- **Official URL:** https://www.iso.org/standard/72704.html
- **Locator:** official Abstract/Scope.
- **Role:** lifecycle risk-management framework. It does not prescribe one universal acceptable-risk level and is not a substitute for a product-specific risk-management file.

<a id="std-iso-13485-2016"></a>
## STD-ISO-13485-2016 — Medical-device quality-management systems
- **Standard:** ISO 13485:2016, *Medical devices — Quality management systems — Requirements for regulatory purposes.* Edition 3; reviewed/confirmed current in 2025.
- **Official URL:** https://www.iso.org/standard/59752.html
- **Locator:** official Abstract/Scope.
- **Role:** QMS/regulatory-quality context. Referencing it in BiomechE-CAD documentation is not a claim that the project or organization is certified to ISO 13485.

<a id="std-iso-9241-210-2019"></a>
## STD-ISO-9241-210-2019 — Human-centred design for interactive systems
- **Standard:** ISO 9241-210:2019, *Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems.* Edition 2; confirmed current in 2025.
- **Official URL:** https://www.iso.org/standard/77520.html
- **Locator:** official Abstract/Scope.
- **Role:** human-centred design lifecycle/process context for workflow and visual-reference validation; does not define BiomechE-CAD clinical semantics.

<a id="std-iec-62366-1-2015-a1-2020"></a>
## STD-IEC-62366-1-2015-A1-2020 — Medical-device usability engineering
- **Standard:** IEC 62366-1:2015+A1:2020 consolidated version, *Medical devices — Part 1: Application of usability engineering to medical devices.* Edition 1.1.
- **Official URL:** https://webstore.iec.ch/en/publication/63181
- **Locator:** official Abstract/Scope.
- **Role:** usability engineering related to safety/use error. Applicability and formal conformance remain part of the future regulatory/QMS assessment.

<a id="std-isb-global-cs-1995"></a>
## STD-ISB-GLOBAL-CS-1995 — ISB global coordinate-system reporting proposal
- **Citation:** Wu G, Cavanagh PR. *ISB recommendations for standardization in the reporting of kinematic data.* J Biomech. 1995;28(10):1257–1261. PMID `8550644`; DOI `10.1016/0021-9290(95)00017-C`.
- **Official context:** International Society of Biomechanics, `Standards` → `Global coordinate systems`.
- **Locator:** pp.1257–1261; ISB Standards—Global coordinate systems. PubMed records no abstract.
- **Role:** coordinate-system/reporting standardization context. BiomechE-CAD's exact axis convention remains a documented product convention rather than an assertion that ISB prescribes these exact CAD axes.

<a id="std-isb-foot-kinematics-2021"></a>
## STD-ISB-FOOT-KINEMATICS-2021 — ISB multi-segment foot kinematics recommendations
- **Citation:** Leardini A, Stebbins J, Hillstrom H, Caravaggi P, Deschamps K, Arndt A. *ISB recommendations for skin-marker-based multi-segment foot kinematics.* J Biomech. 2021;125:110581. PMID `34217032`; DOI `10.1016/j.jbiomech.2021.110581`.
- **Official context:** International Society of Biomechanics, `Standards` → `Foot kinematics`.
- **Locator:** PubMed Abstract; ISB Standards—Foot kinematics.
- **Role:** anatomy/model/landmark/reporting standardization context; recommendations standardize collection/calculation/reporting but do not mandate one model for every application.

<a id="std-json-schema-2020-12"></a>
## STD-JSON-SCHEMA-2020-12 — JSON Schema Draft 2020-12
- **Specification:** JSON Schema Draft 2020-12, Core and Validation vocabularies.
- **Official URL:** https://json-schema.org/draft/2020-12
- **Locator:** official specification details; Core/Validation documents.
- **Role:** machine-readable reference validation for the portable BiomechE-CAD project manifest; does not select a database/storage engine.

<a id="std-w3c-prov-o-2013"></a>
## STD-W3C-PROV-O-2013 — W3C PROV-O
- **Specification:** *PROV-O: The PROV Ontology.* W3C Recommendation, 30 April 2013.
- **Official URL:** https://www.w3.org/TR/prov-o/
- **Locator:** §2 `PROV-O at a glance`; §3.1 `Starting Point Terms` (`Entity`, `Activity`, `Agent`).
- **Role:** conceptual/interoperability provenance model for input/output entities, generating activities and responsible agents; RDF storage is not required internally.

<a id="std-w3c-wcag-22"></a>
## STD-W3C-WCAG-2.2 — Web Content Accessibility Guidelines 2.2
- **Specification:** W3C Recommendation, *Web Content Accessibility Guidelines (WCAG) 2.2*, republished with errata 12 December 2024.
- **Official URL:** https://www.w3.org/TR/WCAG22/
- **Locator:** normative Success Criteria; especially non-text content, use of color, focus, keyboard, dragging movements, target size, labels/name/role/value as applicable.
- **Role:** testable accessibility reference for web-rendered visual prototypes and a source of accessibility principles. It is not by itself a complete native-desktop conformance claim.

<a id="guide-w3c-wcag2ict-22"></a>
## GUIDE-W3C-WCAG2ICT-2.2 — Applying WCAG 2.2 to non-web software/documents
- **Guidance:** W3C Group Note, *Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT)*, 11 December 2025.
- **Official URL:** https://www.w3.org/TR/wcag2ict-22/
- **Locator:** Abstract / guidance for non-web documents and software.
- **Role:** informative, non-normative bridge for applying WCAG concepts to desktop/non-web software. It explicitly does not set requirements on its own.

<a id="std-rfc-9562"></a>
## STD-RFC-9562 — UUIDs
- **Specification:** RFC 9562, *Universally Unique IDentifiers (UUIDs).* RFC Editor, 2024.
- **Official URL:** https://www.rfc-editor.org/info/rfc9562/
- **Locator:** §5.7 UUID Version 7; §6 generation/best-practice considerations.
- **Role:** persistent internal identifier semantics; UUIDv7 is the preferred new-ID form in Project Schema v0, while IDs remain opaque to business logic.

<a id="std-rfc-3339"></a>
## STD-RFC-3339 — Internet timestamps
- **Specification:** RFC 3339, *Date and Time on the Internet: Timestamps.* Proposed Standard, July 2002; updated by RFC 9557.
- **Official URL:** https://www.rfc-editor.org/info/rfc3339/
- **Locator:** §5.6 Internet Date/Time Format and local-offset semantics.
- **Role:** offset-aware serialized timestamp format for project/revision/provenance events.

<a id="std-rfc-8785"></a>
## STD-RFC-8785 — JSON Canonicalization Scheme (JCS)
- **Specification:** RFC 8785, *JSON Canonicalization Scheme (JCS).* Informational, June 2020.
- **Official URL:** https://www.rfc-editor.org/rfc/rfc8785.html
- **Locator:** §3 Detailed Operation, especially deterministic primitive serialization/property sorting; verified errata apply.
- **Role:** recommended canonical representation when hashing/signing selected JSON metadata; raw binary assets are hashed as raw bytes.

<a id="std-nist-fips-180-4"></a>
## STD-NIST-FIPS-180-4 — Secure Hash Standard
- **Standard:** NIST FIPS 180-4, *Secure Hash Standard (SHS).* Final update August 2015; NIST has announced a future revision.
- **Official URL:** https://csrc.nist.gov/pubs/fips/180-4/upd1/final
- **Locator:** official Abstract/standard; SHA family definitions.
- **Role:** SHA-256 baseline digest for Project Schema asset/content integrity. The algorithm name is persisted to permit future evolution.

<a id="std-hl7-fhir-r5-provenance"></a>
## STD-HL7-FHIR-R5-PROVENANCE — FHIR R5 Provenance
- **Specification:** HL7 FHIR R5 `Provenance` resource.
- **Official URL:** https://hl7.org/fhir/R5/provenance.html
- **Locator:** resource scope/boundaries and target/agent/entity provenance semantics.
- **Role:** optional healthcare-interoperability mapping target for version-specific provenance; not the internal CAD authoring schema.

<a id="std-hl7-fhir-r5-observation"></a>
## STD-HL7-FHIR-R5-OBSERVATION — FHIR R5 Observation
- **Specification:** HL7 FHIR R5 `Observation` resource.
- **Official URL:** https://hl7.org/fhir/R5/observation.html
- **Locator:** scope/boundaries for measurements and simple assertions.
- **Role:** optional mapping target for quantitative BiomechE-CAD outcomes; does not replace trial/ROI/revision semantics internally.

<a id="std-hl7-fhir-r5-questionnaire"></a>
## STD-HL7-FHIR-R5-QUESTIONNAIRE — FHIR R5 Questionnaire / QuestionnaireResponse
- **Specification:** HL7 FHIR R5 `QuestionnaireResponse` resource and linked `Questionnaire` definition.
- **Official URL:** https://hl7.org/fhir/R5/questionnaireresponse.html
- **Locator:** §2.6 resource scope and §2.6.2 boundaries/relationships; `QuestionnaireResponse.questionnaire` linkage.
- **Role:** optional mapping path for PROM/questionnaire responses while preserving exact instrument/version/licensing semantics in the BiomechE-CAD model.

<a id="reg-eu-mdr-2017-745"></a>
## REG-EU-MDR-2017-745 — Regulation (EU) 2017/745 (MDR)
- **Regulation:** Regulation (EU) 2017/745 on medical devices; current consolidated text consulted 2026-08-16.
- **Official URL:** https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02017R0745-20260101
- **Locator:** definitions, intended purpose, software/custom-made-device provisions and applicable annexes/rules as used by a future formal assessment.
- **Role:** regulatory boundary authority. The project does not infer a final BiomechE-CAD classification solely from this bibliography entry.

<a id="guide-mdcg-2019-11-rev1-2025"></a>
## GUIDE-MDCG-2019-11-REV1-2025 — Qualification/classification of software under MDR/IVDR
- **Guidance:** MDCG 2019-11 rev.1, *Guidance on Qualification and Classification of Software in Regulation (EU) 2017/745 – MDR and Regulation (EU) 2017/746 – IVDR*, June 2025.
- **Official registry:** European Commission MDCG endorsed guidance page.
- **Locator:** software qualification/classification decision logic and intended-purpose context.
- **Role:** future formal software-regulatory assessment. It does not pre-classify BiomechE-CAD while intended purpose/deployment claims remain under controlled definition.

<a id="guide-mdcg-2021-24-rev1-2026"></a>
## GUIDE-MDCG-2021-24-REV1-2026 — Classification of medical devices
- **Guidance:** MDCG 2021-24 rev.1, *Guidance on classification of medical devices*, April 2026; Commission update dated 20 April 2026.
- **Official registry:** European Commission MDCG guidance/current update pages.
- **Locator:** classification-rule interpretation.
- **Role:** classification context for a future formal MDR assessment; not an automatic classification of the CAD software or manufactured orthosis.

<a id="guide-mdcg-2019-16-rev1"></a>
## GUIDE-MDCG-2019-16-REV1 — Cybersecurity for medical devices
- **Guidance:** MDCG 2019-16 rev.1, *Guidance on Cybersecurity for medical devices*, publication listed by the European Commission as July 2020.
- **Official registry:** European Commission MDCG endorsed guidance page.
- **Role:** medical-device cybersecurity lifecycle context when/if applicable. Concrete security architecture and regulatory applicability remain separately assessed.

<a id="guide-mdcg-2021-3"></a>
## GUIDE-MDCG-2021-3 — Questions and Answers on Custom-Made Devices
- **Guidance:** MDCG 2021-3, *Questions and Answers on Custom-Made Devices*, March 2021.
- **Official URL:** European Commission custom-made-device guidance/current topic pages.
- **Role:** custom-made/adaptable/patient-matched regulatory terminology and boundary context. Product architecture must not equate “patient-specific” with one legal category without formal assessment.

<a id="reg-eu-gdpr-2016-679"></a>
## REG-EU-GDPR-2016-679 — General Data Protection Regulation
- **Regulation:** Regulation (EU) 2016/679 (GDPR).
- **Official URL:** https://eur-lex.europa.eu/eli/reg/2016/679/oj
- **Locators:** Article 25 `Data protection by design and by default`; Article 32 `Security of processing`; other provisions require applicability-specific assessment.
- **Role:** privacy/security boundary for personal and health-related data. This bibliography entry is not legal advice and does not replace a deployment-specific DPIA/controller-processor assessment where required.

<a id="guide-fda-hfe-2026"></a>
## GUIDE-FDA-HFE-2026 — Applying Human Factors and Usability Engineering to Medical Devices
- **Guidance:** U.S. FDA, *Applying Human Factors and Usability Engineering to Medical Devices — Guidance for Industry and Food and Drug Administration Staff*, Final, August 2026; docket FDA-2011-D-0469.
- **Official URL:** https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-factors-and-usability-engineering-medical-devices
- **Locator:** guidance purpose/scope and human-factors/usability-engineering process recommendations.
- **Role:** current human-factors safety evidence for minimizing use error and designing for intended users/use environments. It is guidance, not a claim of FDA applicability or clearance for BiomechE-CAD.

---

# E. Vendor / market sources

<a id="vendor-sensormedica-easycad2"></a>
## VENDOR-SENSORMEDICA-EASYCAD2
Sensor Medica — EasyCAD2. https://www.sensormedica.com/en/easycad-2/ . Use: market/product functionality only, not clinical efficacy.

<a id="vendor-sensormedica-insole"></a>
## VENDOR-SENSORMEDICA-INSOLE
Sensor Medica — easyCAD Insole. https://www.sensormedica.com/en/easycad-insole/ . Use: vendor workflow/product claims only.

<a id="vendor-sensormedica-vulcan"></a>
## VENDOR-SENSORMEDICA-VULCAN
Sensor Medica — Vulcan CNC. https://www.sensormedica.com/it/vulcan-cnc/ . Use: manufacturing/CNC market reference.

<a id="vendor-vertex-orthocad"></a>
## VENDOR-VERTEX-ORTHOCAD — Vertex Orthopedic OrthoCAD
- **Vendor page:** https://vertexorthopedic.com/solutions/software ; additional current product page: https://vertexorthopedic.com/solutions/orthocad .
- **Locator:** `OrthoCAD: Advanced Orthopedic Design Software`; `Key Features`; `How OrthoCAD Works`; on the dedicated page, `Key capabilities`, `Deterministic macro engine`, `Parametric dependency recalculation`.
- **Recorded market capabilities:** 2D/3D scan workflow; prescription/template-based orthotic CAD; medial/lateral posting and arch adjustments; patient/design history; CNC/3D-print export; current dedicated page also documents reusable custom macros and dependency recalculation.
- **Role:** competitor/market functionality only. Vendor performance, clinical-validation, speed and comparative-superiority claims are not treated as independent scientific evidence.

<a id="vendor-insolution-software"></a>
## VENDOR-INSOLUTION-SOFTWARE — Insolution Manager / CAD
- **Vendor page:** https://www.insolution.nl/en/our-total-solution/software/
- **Locator:** `Insolution Manager`; `Insolution CAD`; `Clear 3D view`.
- **Recorded market capabilities:** controls 2D/3D scanners and pressure plate; patient record/history/gait-video/findings/follow-up/report/treatment plan; insole plan including material, thickness and Shore value; CAD from 2D, 3D or pressure-measurement input and reusable libraries.
- **Role:** competitor/market functionality only, not clinical-efficacy evidence.

<a id="vendor-insolution-pressure"></a>
## VENDOR-INSOLUTION-PRESSURE — Insolution pressure plate
- **Vendor page:** https://www.insolution.nl/en/our-total-solution/hardware/pressure-measuring-plate/
- **Locator:** `Pressure plate`.
- **Recorded market capabilities:** static/dynamic pressure profiles; pressure, contact time and impulse; pressure measurements stored in patient archive; pressure images transferable to orthotic CAD as background with 2D/3D scan.
- **Role:** competitor/market functionality only. Vendor sensor counts/performance statements are not scientific qualification of BiomechE-CAD hardware.

<a id="vendor-voxelcare"></a>
## VENDOR-VOXELCARE — Voxelcare ecosystem
- **Vendor page:** https://www.voxelcare.com/
- **Locator:** `Produce`; `Online Platform`; `Cloud Voxelcare CAD`; `Adapted to every business size`.
- **Recorded market capabilities:** cloud-based custom-foot-orthotic design/production ecosystem; CNC milling and 3D printing; scanner/design/production workflow. Other reviewed Voxelcare public pages describe 2D/3D/plantar-pressure acquisition as supported inputs.
- **Role:** competitor/market functionality only, not clinical-efficacy evidence.

<a id="vendor-sharpshape-aoms"></a>
## VENDOR-SHARPSHAPE-AOMS — Sharp Shape AOMS
- **Vendor pages:** https://www.sharpshape.com/products.html ; https://sharpshape.com/ .
- **Locator:** `CAD (Computer Aided Design) Program in AOMS`; `CAM (Computer Aided Manufacturing) Program in AOMS`; `AOMS 3DPRN app (New 2024)`; `AOMS TOT CNC (New 2025)`.
- **Recorded market capabilities:** integrated 3D scanners + orthotic CAD/CAM; prescription-driven biomechanical cast corrections; positive-mold/orthotic-shell/footbed workflows; CNC toolpath integration; current mobile/3D-print workflows.
- **Role:** competitor/market functionality only. Market-share, popularity and superiority claims are not used as scientific evidence.

---

# F. Architecture / integration references — architecture selection still parked

<a id="arch-biomeche-coord-2026-08-14"></a>
## ARCH-BIOMECHE-COORD-2026-08-14 — BiomechE coordinate/acquisition contract snapshot
- **Repository/revision:** `ww34ww34ww34/BiomechE`, commit `b38ee9e6b10bf4abe8073f4608edcf867eb2e328`, consulted 2026-08-14.
- **Locators:** `docs/spec/01_coordinate_systems.md`; `docs/spec/02_input_data_model.md`; `docs/spec/algorithms/foot_axis.md`; `src/core/posturography/sensor_geometry.hpp`.
- **Role:** historical integration-side snapshot for matrix topology vs physical sensor geometry, `ExamFrame2D`, side-aware foot-axis semantics and sensor-centre/represented-area data. Not clinical efficacy evidence.

<a id="arch-biomeche-integration-2026-08-15"></a>
## ARCH-BIOMECHE-INTEGRATION-2026-08-15 — Current BiomechE quantitative integration snapshot
- **Repository/revision:** `ww34ww34ww34/BiomechE`, commit `d5e467a1a5551f4280cfef5b483da1999f1566e0`, consulted 2026-08-15.
- **Locators:** `docs/spec/01_coordinate_systems.md`; `docs/spec/02_input_data_model.md`; `docs/spec/04_pressure_physics.md`; `docs/spec/06_kpi_catalog.md`; `docs/spec/algorithms/foot_axis.md`; `docs/RESUME_HERE_DYNAMIC_GAIT_2026-08-15_DYN005.md`.
- **Recorded contract points:** matrix topology is distinct from physical `SensorGeometry`; pressure/force/COP use explicit metric geometry/units; KPI registry includes identifier, formula/definition, inputs, units, frame, analysis domain, quality and algorithm/profile provenance; result availability distinguishes `VALID/DEGRADED/UNAVAILABLE`; dynamic gait is frozen through `DYN-005` at this snapshot and `DYN-006` pressure/force/integral/region work remains upstream NEXT.
- **Role:** pinned implementation/specification reference for BiomechE↔BiomechE-CAD integration. Not clinical efficacy evidence and not a geometry-kernel selection.

<a id="arch-opensubdiv"></a>
## ARCH-OPENSUBDIV
Pixar OpenSubdiv documentation. https://opensubdiv.org/ . Use: SubD implementation research only.

<a id="arch-opennurbs"></a>
## ARCH-OPENNURBS
McNeel openNURBS / `ON_SubD`. https://github.com/mcneel/opennurbs . Use: geometry foundation/interoperability research only. Internal `opennurbs_subd_data.h` is not an application contract.

<a id="arch-rhino3dm"></a>
## ARCH-RHINO3DM
McNeel rhino3dm. https://github.com/mcneel/rhino3dm . Use: .NET/JS/WASM interoperability research.

<a id="arch-manifold"></a>
## ARCH-MANIFOLD
Manifold. https://github.com/elalish/manifold . Use: conditional solid-mesh/manufacturing research.

<a id="arch-occt"></a>
## ARCH-OCCT
Open CASCADE Technology. https://dev.opencascade.org/ ; https://github.com/Open-Cascade-SAS/OCCT . Use: optional exact-CAD/interoperability research.

---

# G. Bibliography maintenance rules

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
11. Population/indication profiles must state non-transfer rules when evidence/guidelines define different pathways.
12. PROM/instrument metadata must include the exact version/language and must not assume translations or modified forms have identical measurement properties.
13. Before bundling questionnaire item text or scoring code, verify current copyright/licensing/redistribution terms for that exact instrument/version.
14. A standards abstract/scope supports terminology and high-level test/qualification/interoperability semantics only; claiming full standard conformance requires an applicability assessment and, where applicable, a controlled copy.
15. Test standards never automatically define a universal clinical/material acceptance threshold; limits belong to a qualified product/manufacturing profile.
16. Superseded/withdrawn standard editions should not be used when a current replacement is known unless historical traceability specifically requires them.
17. Schema/interoperability standards can constrain representation/provenance without redefining clinical requirements.
18. `docs/research/SOURCES.md` tracks source intake/open verification; this file owns canonical metadata.
19. Competitor/vendor pages may support a statement that a feature is publicly advertised/documented; they do not prove clinical efficacy, internal implementation semantics or absence of unmentioned capabilities.
20. A pinned BiomechE repository snapshot may define integration semantics for that revision; later upstream changes require a new/updated integration pin rather than silently reinterpreting historical results.
21. Regulatory/guidance sources constrain applicability assessments but must not be converted into a product classification without the controlled intended-purpose and deployment context.
22. Human-factors/accessibility guidance may constrain interaction design and verification but cannot redefine clinical/domain semantics.
