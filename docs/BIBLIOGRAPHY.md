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
[GUIDE-IWGDF-2023, Prevention guideline]
```

Locator priority:
1. exact PDF/manual/article page;
2. article table, figure or numbered section;
3. HTML section heading;
4. PubMed/PMC abstract subsection;
5. whole source only when no finer locator has been captured.

**Never invent a page number.** Population-specific, protocol-specific, model-based and vendor claims remain labelled as such.

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
Bus SA et al. *Evaluation and optimization of therapeutic footwear for neuropathic diabetic foot patients using in-shoe plantar pressure analysis.* Diabetes Care. 2011. PMID `21610125`; DOI `10.2337/dc10-2206`. Locator: Abstract—Results. Role: measure → modify → remeasure.

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
Cherni Y et al. *Effect of 3D printed foot orthoses stiffness on muscle activity and plantar pressures in individuals with flexible flatfeet.* Clin Biomech. 2022;92:105553. PMID `34973589`; DOI `10.1016/j.clinbiomech.2021.105553`. Role: stiffness as independent dose.

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
Kernozek TW et al. *Reliability of an in-shoe pressure measurement system during treadmill walking.* Foot Ankle Int. 1996;17(4):204–209. PMID `8696496`; DOI `10.1177/107110079601700404`. Role: speed and step-count awareness.

<a id="ref-cad-036"></a>
## REF-CAD-036 — Cross-system pressure comparability
Chockalingam N et al. *Discrepancies between plantar pressure devices...* Foot. 2025;64:102190. PMID `40743570`; DOI `10.1016/j.foot.2025.102190`. Role: cross-device warnings.

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
Bus SA et al. *Effect of custom-made footwear on foot ulcer recurrence in diabetes: a multicenter randomized controlled trial.* Diabetes Care. 2013;36(12):4109–4116. PMID `24130357`; PMCID `PMC3836114`; DOI `10.2337/dc13-0996`. Locator: pp.4109–4116; Abstract—Results/Conclusions. Role: improved offloading did not significantly reduce recurrence in intention-to-treat, but did in the objectively high-adherence subgroup; adherence is outcome-critical.

<a id="ref-cad-069"></a>
## REF-CAD-069 — CareFUL pressure-based orthoses RCT
Ulbrecht JS, Hurley T, Mauger DT, Cavanagh PR. *Prevention of recurrent foot ulcers with plantar pressure-based in-shoe orthoses: the CareFUL prevention multicenter randomized controlled trial.* Diabetes Care. 2014;37(7):1982–1989. PMID `24760263`; PMCID `PMC4067390`; DOI `10.2337/dc13-2956`. Locator: pp.1982–1989; Abstract/Results. Role: shape + barefoot-pressure-based orthoses reduced submetatarsal ulcer recurrence versus standard-of-care orthoses in the studied high-risk population.

<a id="ref-cad-070"></a>
## REF-CAD-070 — Continuous pressure feedback and diabetic re-ulceration
Abbott CA et al. *Innovative intelligent insole system reduces diabetic foot ulcer recurrence at plantar sites: a prospective, randomised, proof-of-concept study.* Lancet Digit Health. 2019;1(6):e308–e318. PMID `33323253`; DOI `10.1016/S2589-7500(19)30128-1`. Locator: pp.e308–e318; Abstract—Findings. Role: continuous pressure monitoring + feedback/offloading guidance; future P2 integration direction.

<a id="ref-cad-071"></a>
## REF-CAD-071 — DIASSIST adherence RCT 2026
Vossen LE et al. *An Integrated Personalized Multimodal Intervention Improves Adherence to Wearing Custom-Made Footwear in People With Diabetes at High Foot Ulcer Risk: A Multicenter Randomized Controlled Trial (DIASSIST).* Diabetes Care. 2026;49(8):1384–1394. PMID `42247281`; DOI `10.2337/dc25-3113`. Locator: pp.1384–1394; Abstract—Results. Role: adherence can be materially improved with personalized multimodal support.

<a id="ref-cad-072"></a>
## REF-CAD-072 — Custom orthoses for forefoot pain review
Arias-Martín I, Reina-Bueno M, Munuera-Martínez PV. *Effectiveness of custom-made foot orthoses for treating forefoot pain: a systematic review.* Int Orthop. 2018;42(8):1865–1875. PMID `29423640`; DOI `10.1007/s00264-018-3817-y`. Locator: pp.1865–1875; Abstract—Results/Conclusions. Role: pain outcomes across heterogeneous forefoot conditions; do not merge diagnoses silently.

<a id="ref-cad-073"></a>
## REF-CAD-073 — Flatfoot network meta-analysis
Shim SR et al. *Optimizing Flatfoot Management With Foot Orthoses: A Systemic Review and Meta-analysis.* Am J Phys Med Rehabil. 2026;105(3):230–237. PMID `41065643`; DOI `10.1097/PHM.0000000000002833`. Locator: pp.230–237; Abstract—Results. Role: RCT synthesis for pain, navicular drop, calcaneal pitch and COP; included ages span children/young adults, so population boundaries remain essential.

<a id="ref-cad-074"></a>
## REF-CAD-074 — Plantar fasciitis orthoses RCT meta-analysis 2026
Wang D, Lin Z, Tan G, Han X, Huang Y. *Efficacy and safety of foot orthoses for improving pain and function in patients with plantar fasciitis: a systematic review and meta-analysis of randomized controlled trials.* Disabil Rehabil. 2026;48(5):1231–1245. PMID `40999841`; DOI `10.1080/09638288.2025.2563763`. Locator: pp.1231–1245; Abstract—Results/Conclusion. Role: pain benefit without clear function/walking-ability superiority; supports separate outcome classes.

<a id="ref-cad-075"></a>
## REF-CAD-075 — Running biomechanics orthoses meta-analysis 2024
Jor A et al. *Effects of foot orthoses on running kinetics and kinematics: A systematic review and meta-analysis.* Gait Posture. 2024;109:240–258. PMID `38367456`; DOI `10.1016/j.gaitpost.2024.02.003`. Locator: pp.240–258; Abstract—Results. Role: healthy-runner task-specific pressure, comfort, kinematic and running-economy trade-offs.

<a id="ref-cad-076"></a>
## REF-CAD-076 — Orthoses and injury prevention meta-analysis
Bonanno DR, Landorf KB, Munteanu SE, Murley GS, Menz HB. *Effectiveness of foot orthoses and shock-absorbing insoles for the prevention of injury: a systematic review and meta-analysis.* Br J Sports Med. 2017;51(2):86–96. PMID `27919918`; DOI `10.1136/bjsports-2016-096671`. Locator: pp.86–96; Abstract—Results. Role: overall/stress-fracture prevention signal with heterogeneous trial quality; not a universal injury-prevention claim.

<a id="ref-cad-077"></a>
## REF-CAD-077 — Footwear comfort and running economy
Van Alsenoy K, van der Linden ML, Girard O, Santos D. *Increased footwear comfort is associated with improved running economy - a systematic review and meta-analysis.* Eur J Sport Sci. 2023;23(1):121–133. PMID `34726119`; DOI `10.1080/17461391.2021.1998642`. Locator: pp.121–133; Abstract. Role: comfort is a meaningful sport outcome and may relate to economy, but does not prove custom-orthosis performance superiority.

<a id="ref-cad-078"></a>
## REF-CAD-078 — Running with asymptomatic flatfoot meta-analysis
Jor A et al. *Effects of foot orthoses on lower extremity joint kinematics and kinetics in runners with asymptomatic flatfeet: A systematic review and meta-analysis.* Gait Posture. 2025;121:281–294. PMID `40516166`; DOI `10.1016/j.gaitpost.2025.06.003`. Locator: pp.281–294; Abstract—Results. Role: arch-support-only and arch+medial-post configurations behave differently in a running flatfoot subtype.

<a id="ref-cad-079"></a>
## REF-CAD-079 — Bone-stress injury prevention review
Lavigne A et al. *The Role of Footwear, Foot Orthosis, and Training-Related Strategies in the Prevention of Bone Stress Injuries: A Systematic Review and Meta-Analysis.* Int J Exerc Sci. 2023;16(3):721–743. PMID `37649463`; PMCID `PMC10464778`; DOI `10.70252/ZNRS2138`. Locator: pp.721–743; Abstract—Results/Conclusion. Role: possible BSI prevention effect with low-quality/military-heavy evidence; do not generalize to athletes universally.

## PROM / comfort / fit / adherence additions

<a id="ref-cad-080"></a>
## REF-CAD-080 — Foot Health Status Questionnaire development
Bennett PJ, Patterson C, Wearing S, Baglioni T. *Development and validation of a questionnaire designed to measure foot-health status.* J Am Podiatr Med Assoc. 1998;88(9):419–428. PMID `9770933`; DOI `10.7547/87507315-88-9-419`. Locator: pp.419–428; Abstract. Role: 13-item foot-health PROM covering pain, function, footwear and general foot health.

<a id="ref-cad-081"></a>
## REF-CAD-081 — Foot Function Index development
Budiman-Mak E, Conrad KJ, Roach KE. *The Foot Function Index: a measure of foot pain and disability.* J Clin Epidemiol. 1991;44(6):561–570. PMID `2037861`; DOI `10.1016/0895-4356(91)90220-4`. Locator: pp.561–570; Abstract. Role: foot pain/disability/activity-restriction PROM baseline.

<a id="ref-cad-082"></a>
## REF-CAD-082 — FFI measurement-properties systematic review
*Measurement properties of the Foot Function Index (FFI) questionnaire: A systematic review.* PMID `38856157`. Locator: Abstract—Results/Conclusion. Role: recent COSMIN-oriented review; supports version/language-specific instrument governance rather than assuming all adaptations are equivalent.

<a id="ref-cad-083"></a>
## REF-CAD-083 — Foot and Ankle Ability Measure development
Martin RL, Irrgang JJ, Burdett RG, Conti SF, Van Swearingen JM. *Evidence of validity for the Foot and Ankle Ability Measure (FAAM).* Foot Ankle Int. 2005;26(11):968–983. PMID `16309613`; DOI `10.1177/107110070502601113`. Locator: pp.968–983; Abstract—Methods/Results. Role: ADL and Sport function domains, responsiveness and context-specific MDC/MCID evidence.

<a id="ref-cad-084"></a>
## REF-CAD-084 — Italian 17-item Foot Function Index
Venditto T et al. *17-Italian Foot Function Index with numerical rating scale: development, reliability, and validity of a modified version of the original Foot Function Index.* Foot. 2015;25(1):12–18. PMID `25641642`; DOI `10.1016/j.foot.2014.09.004`. Locator: Abstract—Methods/Results/Conclusions. Role: validated Italian-language candidate for musculoskeletal foot/ankle outcome tracking.

<a id="ref-cad-085"></a>
## REF-CAD-085 — Italian FAAM ADL validation
*Foot and ankle ability measure: cross-cultural translation and validation of the Italian version of the ADL module (FAAM-I/ADL).* PMID `25134631`. Locator: Abstract—Methods/Results/Conclusions. Role: Italian-language FAAM ADL candidate; scoring/translation version must be explicit.

<a id="ref-cad-086"></a>
## REF-CAD-086 — EFAS Score multilingual PROM
Richter M et al. *EFAS Score - Multilingual development and validation of a patient-reported outcome measure (PROM) by the score committee of the European Foot and Ankle Society (EFAS).* Foot Ankle Surg. 2018. PMID `29933960`; DOI `10.1016/j.fas.2018.05.004`. Locator: Abstract—Methods/Results/Conclusions. Role: short multilingual foot/ankle PROM validated including Italian; article reports score versions freely available via EFAS, but current redistribution terms must still be checked before bundling item text.

<a id="ref-cad-087"></a>
## REF-CAD-087 — Reliable footwear comfort assessment during running
Mündermann A, Nigg BM, Stefanyshyn DJ, Humble RN. *Development of a reliable method to assess footwear comfort during running.* Gait Posture. 2002;16(1):38–45. PMID `12127185`; DOI `10.1016/S0966-6362(01)00197-7`. Locator: pp.38–45; Abstract. Role: comfort is task/protocol dependent; VAS can be reliable under a controlled repeated-measure protocol.

<a id="ref-cad-088"></a>
## REF-CAD-088 — Clinically meaningful footwear comfort scales
Mills K et al. *Identifying clinically meaningful tools for measuring comfort perception of footwear.* PMID `20216463`. Locator: Abstract—Methods/Results. Role: VAS, Likert and ranking scales differ in reliability; approximately 10 mm change on a 100-mm VAS was meaningful in this specific study/protocol, not a universal project threshold.

<a id="ref-cad-089"></a>
## REF-CAD-089 — Footwear comfort narrative synthesis
*Footwear comfort: a systematic search and narrative synthesis of the literature.* PMID `34876192`. Locator: Abstract—Results/Conclusion. Role: comfort is multifactorial and population/task dependent; simple VAS can capture overall comfort but design-factor evidence is fragmented.

<a id="ref-cad-090"></a>
## REF-CAD-090 — RUN-CAT comfort instrument
*The running shoe comfort assessment tool (RUN-CAT): Development and evaluation of a new multi-item assessment tool for evaluating the comfort of running footwear.* PMID `32508250`; DOI `10.1080/02640414.2020.1773613`. Locator: Abstract—Methods/Results. Role: example of a validated task-specific multidimensional comfort instrument (heel cushioning, stability, forefoot cushioning, forefoot flexibility); not a generic orthosis PROM.

<a id="ref-cad-091"></a>
## REF-CAD-091 — Therapeutic-footwear adherence measurement systematic review
*Usability of Different Methods to Assess and Improve Adherence to Therapeutic Footwear in Persons with the Diabetic Foot in Remission. A Systematic Review.* PMID `37545201`. Locator: Abstract—Results/Conclusion. Role: objective adherence methods (temperature sensor/activity monitor) reduce limitations of subjective self-report.

<a id="ref-cad-092"></a>
## REF-CAD-092 — Footwear adherence metric validation
*Adherence and Wearing Time of Prescribed Footwear among People at Risk of Diabetes-Related Foot Ulcers: Which Measure to Use?* Sensors. 2023. PMID `36772691`; PMCID `PMC9919850`; DOI `10.3390/s23031648`. Locator: Abstract—Methods/Results/Conclusions. Role: proportion of weight-bearing time/steps with prescribed footwear is more valid than subjective wearing-time recall; adherence denominator matters.

<a id="ref-cad-093"></a>
## REF-CAD-093 — Plantar-heel-pain MID for VAS/FHSQ
*Revised minimal important difference values for the visual analogue scale and Foot Health Status Questionnaire when used for plantar heel pain.* PMID `39682003`; PMCID `PMC11649508`; DOI `10.1002/jfa2.70021`. Locator: Abstract—Methods/Results. Role: MID is instrument-, construct- and population/context-specific and should be stored with evidence provenance.

---

# D. Vendor / market sources

<a id="vendor-sensormedica-easycad2"></a>
## VENDOR-SENSORMEDICA-EASYCAD2
Sensor Medica — EasyCAD2. https://www.sensormedica.com/en/easycad-2/ . Use: market/product functionality only, not clinical efficacy.

<a id="vendor-sensormedica-insole"></a>
## VENDOR-SENSORMEDICA-INSOLE
Sensor Medica — easyCAD Insole. https://www.sensormedica.com/en/easycad-insole/ . Use: vendor workflow/product claims only.

<a id="vendor-sensormedica-vulcan"></a>
## VENDOR-SENSORMEDICA-VULCAN
Sensor Medica — Vulcan CNC. https://www.sensormedica.com/it/vulcan-cnc/ . Use: manufacturing/CNC market reference.

---

# E. Architecture references — currently parked

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
11. Population/indication profiles must state non-transfer rules when evidence/guidelines define different pathways.
12. PROM/instrument metadata must include the exact version/language and must not assume that translations or modified forms have identical measurement properties.
13. Before bundling questionnaire item text or scoring code, verify current copyright/licensing/redistribution terms for that exact instrument/version.
14. `docs/research/SOURCES.md` tracks source intake/open verification; this file owns canonical metadata.
