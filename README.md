# Awesome Collaborative Perception [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of papers and resources on **Vehicular Collaborative Perception** from a Computer Vision perspective.

This repository accompanies our systematic literature review paper:

**"A Systematic Literature Review on Vehicular Collaborative Perception: A Computer Vision Perspective"**
*IEEE Transactions on Intelligent Transportation Systems (T-ITS), 2026*

📄 [Paper PDF](A_Systematic_Literature_Review_on_Vehicular_Collaborative_PerceptionA_Computer_Vision_Perspective.pdf) | 🔗 [BibTeX](collaborative-perception.bib)

## About Collaborative Perception

Collaborative perception (CP) enables multiple vehicles and infrastructure to share sensory information, creating a comprehensive understanding of the traffic environment. This approach overcomes the limitations of single-vehicle perception such as occlusions, limited sensing range, and sparse observations.

### Key Features
- 🚗 **V2V & V2I Communication**: Vehicle-to-Vehicle and Vehicle-to-Infrastructure
- 📊 **106 Papers**: Comprehensive collection from systematic literature review (2019-2024)
- 🏷️ **Organized Taxonomy**: By modality, collaboration type, and perception task
- 📈 **PRISMA 2020**: Follows systematic review guidelines

### Research Questions

This systematic literature review addresses five key research questions:

1. **RQ1: Taxonomy** - How can collaborative perception be classified within a structured taxonomy?
2. **RQ2: Methodological Approaches** - Which methodological approaches are being used for evaluating collaborative perception?
3. **RQ3: Evaluation Scenarios** - Which scenarios are covered by evaluation approaches for collaborative perception?
4. **RQ4: Evaluation Metrics** - Which metrics are used to measure the effectiveness of collaborative perception?
5. **RQ5: Challenges & Opportunities** - What are the challenges, opportunities, and risks of collaborative perception research?

### Related Surveys

While several surveys on collaborative perception exist, this systematic literature review distinguishes itself by:

- **Structured Methodology**: Following PRISMA 2020 guidelines for transparency and reproducibility
- **Comprehensive Taxonomy**: Multi-dimensional classification (modality × collaboration × task)
- **Computer Vision Focus**: In-depth analysis of perception algorithms and evaluation methods
- **Realistic Issues**: Systematic coverage of practical challenges (localization, latency, bandwidth, domain shift, etc.)
- **Comparative Analysis**: Understanding advantages/disadvantages of different approaches

**Prior Surveys**:
- Bai et al. (2024) - High-level overview of CP architecture and node structure
- Caillot et al. (2023) - Focus on localization, object detection, and tracking
- Hun et al. (2023) - CP methods for both ideal and adverse scenarios
- Liu et al. (2023) - Introduction to CP issues
- Huang et al. (2024) - Framework proposal for CP

Our survey provides a transparent, comprehensive, and structured analysis specifically from a computer vision perspective, addressing gaps in existing literature.

### How to Navigate This Repository

**Finding Papers by Your Interest:**

- 🔍 **Looking for specific sensor modality or task?** → Go to [Taxonomy](#taxonomy)
- 🔄 **Interested in detailed paper tables by task?** → See [Papers by Category](#papers-by-category)
- 🎯 **Working on a specific task?** → Check [Papers by Category](#papers-by-category)
- ⚡ **Solving practical challenges?** → Explore [Approaches to Realistic Issues](#approaches-to-realistic-issues)
- 📊 **Need datasets or metrics?** → Visit [Evaluation Methods](#evaluation-methods)
- 🚀 **Planning future research?** → Review [Challenges and Opportunities](#challenges-and-opportunities)

**Quick Access:**
- 📈 See [Statistics](#statistics) for an overview of the field
- 🗺️ Check [Survey Structure](#survey-structure) to understand the organization
- 📚 Browse [Research Questions](#research-questions) to understand what this survey addresses

---

## Table of Contents

- [Statistics](#statistics)
- [Survey Structure](#survey-structure)
- [Taxonomy](#taxonomy)
  - [Object Detection (OD)](#object-detection-od--78-papers)
  - [Semantic Segmentation (SS)](#semantic-segmentation-ss--7-papers)
  - [Object Tracking (OT)](#object-tracking-ot--5-papers)
  - [Motion Prediction (MP)](#motion-prediction-mp--5-papers)
  - [Lane Detection (LD)](#lane-detection-ld--3-papers)
  - [Multi-Task & Task-Agnostic](#multi-task--task-agnostic--10-papers)
- [Papers by Category](#papers-by-category)
  - [VI-A Object Detection (COD)](#vi-a-object-detection-cod)
  - [VI-B Semantic Segmentation (CSS)](#vi-b-semantic-segmentation-css)
  - [VI-C Object Tracking (COT)](#vi-c-object-tracking-cot)
  - [VI-D Motion Prediction (CMP)](#vi-d-motion-prediction-cmp)
  - [VI-E Lane Detection (CLD)](#vi-e-lane-detection-cld)
  - [VI-F Multi-Task & Task-Agnostic](#vi-f-multi-task--task-agnostic)
- [Approaches to Realistic Issues](#approaches-to-realistic-issues)
  - [VII-A Localization Errors](#vii-a-localization-errors)
  - [VII-B Time Latency](#vii-b-time-latency)
  - [VII-C Communication Bandwidth](#vii-c-communication-bandwidth-constraints)
  - [VII-D Communication Interruptions](#vii-d-communication-interruptions)
  - [VII-E Domain Shifts](#vii-e-domain-shifts)
  - [VII-F Heterogeneity](#vii-f-heterogeneity)
  - [VII-G Adversarial Attacks](#vii-g-adversarial-attacks)
- [Evaluation Methods](#evaluation-methods)
  - [Datasets](#datasets)
  - [Evaluation Scenarios](#evaluation-scenarios)
  - [Evaluation Metrics](#evaluation-metrics)
- [Challenges and Opportunities](#challenges-and-opportunities)
- [Tools](#tools)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

---

## Survey Structure

This repository follows the structure of our systematic literature review, which is organized according to the PRISMA 2020 guidelines:

```
├── Section II: Research Methodology
│   ├── PRISMA 2020 Application
│   └── Metadata Analysis
├── Section III: Overview and Taxonomy
│   ├── Modality Type (LiDAR, Camera, LiDAR-Camera)
│   ├── Collaboration Type (Early, Intermediate, Late, Hybrid)
│   └── Perception Tasks (Detection, Tracking, Segmentation, Prediction, Lane Detection, Multi-Task)
├── Section IV-V-VI: Detailed Taxonomy
│   ├── Modality-based Classification
│   ├── Collaboration-based Classification
│   └── Task-based Classification
├── Section VII: Approaches to Address Realistic Issues
│   ├── Localization Errors
│   ├── Time Latency
│   ├── Communication Bandwidth Constraints
│   ├── Communication Interruptions
│   ├── Domain Shifts
│   ├── Heterogeneity
│   └── Adversarial Attacks
├── Section VIII: Evaluation Methods
│   ├── Public Datasets
│   ├── Evaluation Scenarios
│   └── Evaluation Metrics
└── Section IX: Challenges, Opportunities, and Risks
```

See [Figure 2](A_Systematic_Literature_Review_on_Vehicular_Collaborative_PerceptionA_Computer_Vision_Perspective.pdf) in the paper for the complete structure diagram.

### Research Methodology

This systematic literature review follows the **PRISMA 2020 guidelines** for transparency and reproducibility:

**Search Strategy**:
- **Databases**: IEEE Xplore, ACM Library, ScienceDirect, MDPI, Scopus, Google Scholar
- **Search Terms**: `(collaborative OR collective OR cooperative OR multi-agent) AND perception AND (V2X OR V2V OR V2I)`
- **Initial Results**: 4,876 papers identified
- **After Screening**: 109 papers included (2019-2024, collection finalized March 2024)

**Selection Criteria**:
- ✅ Primary research studies with experimental or empirical character
- ✅ Published 2019-2024 in peer-reviewed venues
- ✅ Focus on multi-entity cooperative perception (V2V/V2I/V2X)
- ✅ Provide technical details about fusion algorithms and evaluation
- ❌ Excluded: Single-vehicle perception, roadside-only perception, non-English papers, preprints without peer review

**Quality Assurance**: Multi-round review process with cross-validation among authors to minimize bias

---

## Statistics

**Total Papers**: 106 (PRISMA 2020 selection, finalized March 2024)

> **TABLE VIII** — Summary of Surveyed Collaborative Perception Studies Across Multiple Dimensions

| Dimension | Categories (with counts) | Key observations |
|-----------|--------------------------|------------------|
| **Region** | Asia (54), North America (38), Europe (13), Africa (1) | Research predominantly conducted in Asia and North America |
| **Publication venue** (top 10) | ICRA (16), CVPR (8), IEEE T-IV (8), NeurIPS (8), ICCV (5), IEEE RA-L (5), IEEE ITSC (5), IEEE T-ITS (4), IEEE IoTJ (4) | Publications concentrated in leading robotics and vision venues |
| **Modality** | LiDAR (63), Camera (13), LiDAR-Camera (12) | LiDAR-based approaches remain predominant, reflecting their reliability for accurate 3D detection |
| **Collaboration** | Early (6), Intermediate (71), Late (15), Hybrid (6) | Intermediate fusion is the predominant strategy, balancing bandwidth efficiency with information richness |
| **Task** | Object detection (78), Semantic segmentation (6), Object tracking (5), Motion prediction (3), Lane detection (2), Multi-task (3), Task-agnostic (8) | Object detection dominates the field, while other tasks remain comparatively underexplored |

**Publication Timeline (2019-2024)**:
```
2019: ██ 2 papers
2020: ███████ 7 papers
2021: ██████ 6 papers
2022: ██████████████████ 18 papers
2023: ████████████████████████████████████████ 40 papers
2024: █████████████████████████████████ 33 papers
```

### Key Findings from Metadata Analysis

**Research Trends (2019-2024)**:
- 📈 Steady growth from 7 papers (2019) to 40 papers (2023), reflecting increasing research interest
- 🌏 **Regional Distribution**: Asia (54 papers) and North America (38 papers) lead the research landscape
- 📚 **Publication Venues**: Concentrated in leading robotics and vision conferences (ICRA, CVPR, IEEE T-IV, NeurIPS, ICCV) and journals

**Technical Characteristics**:
- 🔬 **LiDAR Dominance**: 76% of papers use LiDAR (83/109), reflecting its reliability for 3D perception
- 📸 **Camera Adoption**: Only 22% camera-only methods (24/109), with limited LiDAR-Camera fusion (11%)
- 🔄 **Intermediate Collaboration**: Most popular approach (71/109 papers, 65%), balancing bandwidth and accuracy
- 🎯 **Object Detection Focus**: 75% of papers (82/109) address object detection, with other tasks underexplored

**Research Gaps**:
- ⚠️ Semantic segmentation, lane detection, and motion prediction remain significantly underrepresented
- 🔀 LiDAR-Camera fusion and multi-modal approaches need more investigation
- 🌐 Real-world datasets integrating both V2V and V2I collaboration are lacking

---

## Taxonomy

Our systematic literature review categorizes collaborative perception methods along three dimensions:
**Modality** × **Collaboration Type** × **Perception Task**

> See **Table VIII** in the paper for summary statistics. Total: **106 papers** (2019–2024).

### By Perception Task

The tables below list all reviewed methods organized by target perception task. Method names link to the paper (DOI/arXiv); Code column links to the repository.

#### Object Detection (OD) — 78 papers

| Method | Venue | Year | Modality | Collaboration | Task | Code |
|--------|-------|------|----------|---------------|------|------|
| [JointPerception](https://arxiv.org/abs/2206.01001) | IEEE IV 2022 | 2022 | LiDAR | Early | OD | — |
| [RAO](https://doi.org/10.1109/IV55152.2023.10186584) | IEEE IV 2023 | 2023 | LiDAR | Early | OD | — |
| [EdgeCooper](https://arxiv.org/abs/2401.09128) | IEEE JSAC 2024 | 2024 | LiDAR | Early | OD | — |
| [FastClustering](https://arxiv.org/abs/2406.12256) | Cogn. Comput. 2024 | 2024 | LiDAR | Early | OD | — |
| [F-Cooper](https://arxiv.org/abs/1909.06459) | SEC 2019 | 2019 | LiDAR | Intermediate | OD | [Code](https://github.com/Aug583/F-COOPER) |
| [AFS-COD](https://doi.org/10.1109/CAVS51000.2020.9334618) | IEEE CAVS 2020 | 2020 | LiDAR | Intermediate | OD | — |
| [FS-COD](https://doi.org/10.1109/VTC2020-Fall49728.2020.9348723) | IEEE VTC 2020 | 2020 | LiDAR | Intermediate | OD | — |
| [CoFF](https://doi.org/10.1109/JIOT.2021.3053184) | IEEE IoT-J 2021 | 2021 | LiDAR | Intermediate | OD | — |
| [SyncNet](https://doi.org/10.1007/978-3-031-19824-3_19) | ECCV 2022 | 2022 | LiDAR | Intermediate | OD | [Code](https://github.com/MediaBrain-SJTU/SyncNet) |
| [PillarGrid](https://doi.org/10.1109/IV51971.2022.9827241) | IEEE IV 2022 | 2022 | LiDAR | Intermediate | OD | — |
| [Slim-FCP](https://doi.org/10.1007/978-3-031-20080-9_10) | ECCV 2022 | 2022 | LiDAR | Intermediate | OD | — |
| [AdaptiveFeature](https://doi.org/10.1109/WACV56688.2023.00124) | WACV 2023 | 2023 | LiDAR | Intermediate | OD | — |
| [CoBEVFlow](https://arxiv.org/abs/2308.01558) | NeurIPS 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/MediaBrain-SJTU/CoBEVFlow) |
| [DI-V2X](https://arxiv.org/abs/2306.09609) | AAAI 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/Serenos/DI-V2X) |
| [DFS](https://doi.org/10.1109/ITSC55140.2022.9921947) | IEEE ITSC 2023 | 2023 | LiDAR | Intermediate | OD | — |
| [FFNet](https://arxiv.org/abs/2305.14580) | NeurIPS 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/haibao-yu/FFNet-VIC3D) |
| [CoAlign](https://doi.org/10.1109/ICRA48891.2023.10161366) | ICRA 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/yifanlu0227/CoAlign) |
| [VINet](https://arxiv.org/abs/2306.04307) | arXiv 2023 | 2023 | LiDAR | Intermediate | OD | — |
| [FDA](https://arxiv.org/abs/2401.09427) | ICRA 2024 | 2024 | LiDAR | Intermediate | OD | — |
| [HP3D-V2V](https://arxiv.org/abs/2401.12636) | IEEE T-IV 2024 | 2024 | LiDAR | Intermediate | OD | — |
| [MACP](https://arxiv.org/abs/2401.05916) | ICRA 2024 | 2024 | LiDAR | Intermediate | OD | [Code](https://github.com/PurdueDigitalTwin/MACP) |
| [S2R-ViT](https://arxiv.org/abs/2403.09243) | ICRA 2024 | 2024 | LiDAR | Intermediate | OD | — |
| [Select2Col](https://arxiv.org/abs/2306.08534) | AAAI 2024 | 2024 | LiDAR | Intermediate | OD | [Code](https://github.com/huangqzj/Select2Col) |
| [PillarAttention](https://arxiv.org/abs/2310.03343) | IEEE IoT-J 2024 | 2024 | LiDAR | Intermediate | OD | — |
| [DUSA](https://arxiv.org/abs/2305.11548) | ACM MM 2023 | 2023 | LiDAR | Intermediate | OD | — |
| [UMC](https://arxiv.org/abs/2303.17015) | ICCV 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/ispc-lab/UMC) |
| [HPL-ViT](https://arxiv.org/abs/2312.08823) | ICRA 2024 | 2024 | LiDAR | Intermediate | OD | [Code](https://github.com/arnold-yyy/HPL-ViT) |
| [F-Transformer](https://doi.org/10.1007/978-3-031-15919-0_15) | ICANN 2022 | 2022 | LiDAR | Intermediate | OD | — |
| [CRCNet](https://doi.org/10.1109/TITS.2023.3272027) | IEEE T-ITS 2023 | 2022 | LiDAR | Intermediate | OD | — |
| [V2X-ViT](https://doi.org/10.1007/978-3-031-19842-7_7) | ECCV 2022 | 2022 | LiDAR | Intermediate | OD | [Code](https://github.com/DerrickXuNu/v2x-vit) |
| [MPDA](https://doi.org/10.1109/ICRA48891.2023.10160871) | ICRA 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/haibao-yu/FFNet-VIC3D) |
| [Co3D](https://arxiv.org/abs/2309.01963) | IEEE T-ITS 2023 | 2023 | LiDAR | Intermediate | OD | — |
| [FeaCo](https://arxiv.org/abs/2308.11648) | ACM MM 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/jmgu0212/FeaCo) |
| [How2comm](https://arxiv.org/abs/2305.01425) | NeurIPS 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/ydk122024/How2comm) |
| [LCRN](https://arxiv.org/abs/2310.02544) | NeurIPS 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/JesseWong333/metacoop) |
| [SCOPE](https://arxiv.org/abs/2307.08371) | ICCV 2023 | 2023 | LiDAR | Intermediate | OD | [Code](https://github.com/startracker0/SCOPE) |
| [What2comm](https://arxiv.org/abs/2307.12432) | ACM MM 2023 | 2023 | LiDAR | Intermediate | OD | — |
| [CenterCoop](https://doi.org/10.1109/LRA.2023.3339399) | IEEE RA-L 2024 | 2024 | LiDAR | Intermediate | OD | — |
| [V2X-INCOP](https://arxiv.org/abs/2309.09035) | IEEE T-IV 2024 | 2024 | LiDAR | Intermediate | OD | [Code](https://github.com/jinlong17/V2INCOP) |
| [MKD-Cooper](https://arxiv.org/abs/2404.06981) | arXiv 2024 | 2024 | LiDAR | Intermediate | OD | [Code](https://github.com/Bosszhe/MKD-Cooper) |
| [Self-Adaptive](https://arxiv.org/abs/2310.07954) | arXiv 2024 | 2024 | LiDAR | Intermediate | OD | — |
| [SemanticComm](https://arxiv.org/abs/2401.09279) | J. Franklin Inst. 2024 | 2024 | LiDAR | Intermediate | OD | — |
| [V2VFormer](https://arxiv.org/abs/2403.07647) | arXiv 2024 | 2024 | LiDAR | Intermediate | OD | [Code](https://github.com/PurdueDigitalTwin/V2VFormer) |
| [FL-Dynamic](https://doi.org/10.1109/LRA.2021.3134969) | IEEE RA-L 2021 | 2021 | LiDAR | Late | OD | [Code](https://github.com/yys123456/Federated-Learning-for-Cooperative-Perception) |
| [Env-T2TF](https://arxiv.org/abs/2209.01390) | arXiv 2022 | 2022 | LiDAR | Late | OD | — |
| [Co-perception](https://arxiv.org/abs/2307.01036) | IEEE IV 2023 | 2023 | LiDAR | Late | OD | — |
| [Among Us](https://arxiv.org/abs/2309.05061) | ICCV 2023 | 2023 | LiDAR | Late | OD | [Code](https://github.com/coperception/star) |
| [Collective PV-RCNN](https://doi.org/10.1109/ITSC57777.2023.10422079) | IEEE ITSC 2023 | 2023 | LiDAR | Late | OD | — |
| [Late-CNN](https://arxiv.org/abs/2204.00494) | arXiv 2022 | 2023 | LiDAR | Late | OD | [Code](https://github.com/coperception/coperception) |
| [Model-Agnostic](https://arxiv.org/abs/2401.11001) | arXiv 2023 | 2023 | LiDAR | Late | OD | [Code](https://github.com/tum-traffic-dataset/tumtraf-v2x) |
| [Double-M](https://arxiv.org/abs/2309.00668) | arXiv 2023 | 2023 | LiDAR | Late | OD | — |
| [Pillar-based CP](https://doi.org/10.1109/ITSC55140.2022.9921805) | IEEE ITSC 2022 | 2022 | LiDAR | Hybrid | OD | — |
| [ML-Cooper](https://arxiv.org/abs/2209.07756) | arXiv 2022 | 2022 | LiDAR | Hybrid | OD | — |
| [FPV-RCNN](https://arxiv.org/abs/2404.07717) | IEEE RA-L 2024 | 2024 | LiDAR | Hybrid | OD | [Code](https://github.com/YuanYunshuang/FPV_RCNN) |
| [FreeAlign](https://arxiv.org/abs/2405.05177) | ICRA 2024 | 2024 | LiDAR | Hybrid | OD | [Code](https://github.com/MediaBrain-SJTU/FreeAlign) |
| [ViT-FuseNet](https://arxiv.org/abs/2401.09025) | arXiv 2024 | 2024 | LiDAR, Camera | Early | OD | — |
| [Multi-vehicle fusion](https://arxiv.org/abs/2305.15747) | arXiv 2023 | 2023 | LiDAR, Camera | Intermediate | OD | — |
| [V2VFusion](https://arxiv.org/abs/2205.14979) | arXiv 2022 | 2023 | LiDAR, Camera | Intermediate | OD | — |
| [HEAL](https://arxiv.org/abs/2309.07882) | ICRA 2024 | 2024 | LiDAR, Camera | Intermediate | OD | [Code](https://github.com/yifanlu0227/HEAL) |
| [HGAN](https://doi.org/10.1145/3503161.3548197) | IEEE PAAP 2022 | 2022 | LiDAR, Camera | Intermediate | OD | — |
| [Distilled Co-Graph](https://arxiv.org/abs/2106.07060) | arXiv 2021 | 2021 | LiDAR, Camera | Intermediate | OD | [Code](https://github.com/ai4ce/DiscoNet) |
| [HM-ViT](https://arxiv.org/abs/2304.12516) | ICCV 2023 | 2023 | LiDAR, Camera | Intermediate | OD | [Code](https://github.com/XHwind/HM-ViT) |
| [Where2comm](https://arxiv.org/abs/2209.12836) | NeurIPS 2022 | 2022 | LiDAR, Camera | Intermediate | OD | [Code](https://github.com/MediaBrain-SJTU/where2comm) |
| [MCoT](https://arxiv.org/abs/2401.09476) | arXiv 2023 | 2023 | LiDAR, Camera | Intermediate | OD | — |
| [PAFNet](https://arxiv.org/abs/2402.01008) | arXiv 2024 | 2024 | LiDAR, Camera | Intermediate | OD | — |
| [V2VFormer++](https://arxiv.org/abs/2403.04563) | arXiv 2024 | 2024 | LiDAR, Camera | Intermediate | OD | — |
| [TCLF](https://doi.org/10.1109/CVPR52688.2022.02067) | CVPR 2022 | 2022 | LiDAR, Camera | Late | OD | — |
| [VICOD](https://arxiv.org/abs/2208.13026) | arXiv 2022 | 2022 | LiDAR, Camera | Late | OD | — |
| [CoCa3D](https://doi.org/10.1109/CVPR52729.2023.01318) | CVPR 2023 | 2023 | Camera | Intermediate | OD | [Code](https://github.com/MediaBrain-SJTU/CoCa3D) |
| [ActFormer](https://arxiv.org/abs/2403.09229) | ICRA 2024 | 2024 | Camera | Intermediate | OD | [Code](https://github.com/cwc1260/ActFormer) |
| [EMIFF](https://arxiv.org/abs/2309.00587) | ICRA 2024 | 2024 | Camera | Intermediate | OD | [Code](https://github.com/Bosszhe/EMIFF) |
| [QUEST](https://arxiv.org/abs/2308.04480) | arXiv 2024 | 2024 | Camera | Intermediate | OD | — |

#### Semantic Segmentation (SS) — 7 papers

| Method | Venue | Year | Modality | Collaboration | Task | Code |
|--------|-------|------|----------|---------------|------|------|
| [When2com](https://doi.org/10.1109/CVPR42600.2020.01499) | CVPR 2020 | 2020 | Camera | Intermediate | SS | [Code](https://github.com/GT-RIPL/MultiAgentPerception) |
| [Who2com](https://doi.org/10.1109/ICRA40945.2020.9197200) | ICRA 2020 | 2020 | Camera | Intermediate | SS | [Code](https://github.com/GT-RIPL/MultiAgentPerception) |
| [MASH](https://doi.org/10.1109/IROS45743.2020.9341059) | IROS 2021 | 2021 | Camera | Intermediate | SS | [Code](https://github.com/GT-RIPL/MultiAgentPerception) |
| [GenBEV](https://doi.org/10.5194/isprs-annals-X-1-W1-2023-303-2023) | ISPRS 2023 | 2023 | LiDAR | Early | SS | [Code](https://github.com/gaolong-data/GENBEV) |
| [CoBEVT](https://arxiv.org/abs/2207.02202) | CoRL 2023 | 2023 | Camera | Intermediate | SS | [Code](https://github.com/DerrickXuNu/CoBEVT) |
| [VICSS](https://doi.org/10.1109/VTC2023-Spring57618.2023.10201005) | IEEE VTC 2023 | 2023 | LiDAR | Intermediate | SS | — |
| [CoHFF](https://arxiv.org/abs/2404.04139) | CVPR 2024 | 2024 | Camera | Intermediate | SS | — |

#### Object Tracking (OT) — 5 papers

| Method | Venue | Year | Modality | Collaboration | Task | Code |
|--------|-------|------|----------|---------------|------|------|
| [Track-by-det](https://doi.org/10.1109/IV55152.2023.10186777) | IEEE IV 2023 | 2023 | Agnostic | N/A | OT | — |
| [HYDRO-3D](https://doi.org/10.1109/TIV.2022.3163231) | IEEE T-IV 2023 | 2023 | LiDAR | Intermediate | OT | — |
| [FFTrack](https://doi.org/10.1109/CVPR52729.2023.01318) | CVPR 2023 | 2023 | LiDAR | Intermediate | OT | — |
| [MOT-CUP](https://doi.org/10.1109/LRA.2024.3364450) | IEEE RA-L 2023 | 2023 | Agnostic | N/A | OT | — |
| [DMSTrack](https://doi.org/10.1109/ICRA57147.2024.10610148) | ICRA 2024 | 2024 | Agnostic | Late | OT | [Code](https://github.com/eddiesmo/DMSTrack) |

#### Motion Prediction (MP) — 5 papers

| Method | Venue | Year | Modality | Collaboration | Task | Code |
|--------|-------|------|----------|---------------|------|------|
| [V2VNet](https://doi.org/10.1007/978-3-030-58536-5_36) | ECCV 2020 | 2020 | LiDAR | Intermediate | MP | [Code](https://github.com/coperception/coperception) |
| [V2VNet-Robust](https://arxiv.org/abs/2111.00643) | CoRL 2021 | 2021 | LiDAR | Intermediate | MP | [Code](https://github.com/coperception/coperception) |
| [Late-early](https://doi.org/10.1109/TITS.2024.3353480) | IEEE T-ITS 2024 | 2024 | LiDAR | Hybrid | MP | [Code](https://github.com/SCP-CN-001/late_early) |
| [BEV-V2X](https://doi.org/10.1109/TIV.2023.3294681) | IEEE T-IV 2023 | 2023 | Camera | Intermediate | MP | — |
| [V2XFormer](https://doi.org/10.1609/aaai.v38i6.28370) | AAAI 2024 | 2024 | Camera | Intermediate | MP | [Code](https://github.com/winchell0203/V2XFormer) |

#### Lane Detection (LD) — 3 papers

| Method | Venue | Year | Modality | Collaboration | Task | Code |
|--------|-------|------|----------|---------------|------|------|
| [Co-mapping](https://doi.org/10.1109/CAVS51000.2020.9334564) | IEEE CAVS 2020 | 2020 | Camera | Late | LD | — |
| [CoLD Fusion](https://doi.org/10.1109/IV55152.2023.10186769) | IEEE IV 2023 | 2023 | Camera | Late | LD | — |
| [LaCPF](https://doi.org/10.1016/j.robot.2024.104705) | RAS 2024 | 2024 | Agnostic | Late | LD | — |

#### Multi-Task & Task-Agnostic — 10 papers

| Method | Venue | Year | Modality | Collaboration | Task | Code |
|--------|-------|------|----------|---------------|------|------|
| [V2VNet](https://doi.org/10.1007/978-3-030-58536-5_36) | ECCV 2020 | 2020 | LiDAR | Intermediate | OD, MP | [Code](https://github.com/coperception/coperception) |
| [Robust V2VNet](https://arxiv.org/abs/2111.00643) | CoRL 2021 | 2021 | LiDAR | Intermediate | OD, MP | [Code](https://github.com/coperception/coperception) |
| [BEV-V2X](https://doi.org/10.1109/TIV.2023.3294681) | IEEE T-IV 2023 | 2023 | Agnostic | Intermediate | SS, MP | — |
| [HYDRO-3D](https://doi.org/10.1109/TIV.2022.3163231) | IEEE T-IV 2023 | 2023 | LiDAR | Intermediate | OD, OT | — |
| [FF-Tracking](https://doi.org/10.1109/CVPR52729.2023.01318) | CVPR 2023 | 2023 | LiDAR, Camera | Intermediate | OD, OT | — |
| [CoBEVT](https://arxiv.org/abs/2207.02202) | CoRL 2023 | 2023 | Camera | Intermediate | OD, SS | [Code](https://github.com/DerrickXuNu/CoBEVT) |
| [V2XFormer](https://doi.org/10.1609/aaai.v38i6.28370) | AAAI 2024 | 2024 | LiDAR, Camera | Intermediate | OD, MP, AP | [Code](https://github.com/winchell0203/V2XFormer) |
| [Late-early](https://doi.org/10.1109/TITS.2024.3353480) | IEEE T-ITS 2024 | 2024 | Camera | Hybrid | OD, MP | [Code](https://github.com/SCP-CN-001/late_early) |
| [STAR](https://arxiv.org/abs/2207.05051) | CoRL 2022 | 2022 | LiDAR | Intermediate | Task-Agnostic | [Code](https://github.com/opensourcedot/starnet) |
| [Core](https://doi.org/10.1109/ICCV51070.2023.00800) | ICCV 2023 | 2023 | LiDAR | Intermediate | Task-Agnostic | [Code](https://github.com/MediaBrain-SJTU/CORE) |

---


## Papers by Category

This section organizes papers by **Perception Task** following **Section VI** of the survey, with detailed modality/fusion information matching the paper's tables.

### Perception Tasks

---

#### VI-A. Object Detection (COD)

> **TABLE XXIX** — Overview of the Methods for Collaborative Object Detection (COD) based on BEV and 3D Representations.
> **V**: Vehicle, **I**: Infrastructure, **Raw**: Raw Data Fusion, **Trad Feat**: Traditional Feature Fusion, **Atten Feat**: Attention Feature Fusion, **Obj**: Object-Level Fusion, **Graph**: Graph-Based Fusion

**78 papers** covering 3D bounding box detection organized by modality and collaboration scheme:

**LiDAR-based:**

| Method | Venue | Modality | Scheme | Year | Entity | Fusion | Code |
|--------|-------|----------|--------|------|--------|--------|:----:|
| [JointPerception](https://arxiv.org/abs/2206.01001) | IEEE IV 2022 | LiDAR | Early | 2022 | V | Raw | — |
| [RAO](https://doi.org/10.1109/IV55152.2023.10186584) | IEEE IV 2023 | LiDAR | Early | 2023 | V | Raw | — |
| [EdgeCooper](https://arxiv.org/abs/2401.09128) | IEEE JSAC 2024 | LiDAR | Early | 2024 | V,I | Trad Feat | — |
| [FastClustering](https://arxiv.org/abs/2406.12256) | Cogn. Comput. 2024 | LiDAR | Early | 2024 | V | Raw | — |
| [F-Cooper](https://arxiv.org/abs/1909.06459) | SEC 2019 | LiDAR | Intermediate | 2019 | V | Trad Feat | [Code](https://github.com/Aug583/F-COOPER) |
| [AFS-COD](https://doi.org/10.1109/CAVS51000.2020.9334618) | IEEE CAVS 2020 | LiDAR | Intermediate | 2020 | V | Trad Feat | — |
| [FS-COD](https://doi.org/10.1109/VTC2020-Fall49728.2020.9348723) | IEEE VTC 2020 | LiDAR | Intermediate | 2020 | V | Trad Feat | — |
| [CoFF](https://doi.org/10.1109/JIOT.2021.3053184) | IEEE IoT-J 2021 | LiDAR | Intermediate | 2021 | V | Trad Feat | — |
| [SyncNet](https://doi.org/10.1007/978-3-031-19824-3_19) | ECCV 2022 | LiDAR | Intermediate | 2022 | V | Trad Feat | [Code](https://github.com/MediaBrain-SJTU/SyncNet) |
| [PillarGrid](https://doi.org/10.1109/IV51971.2022.9827241) | IEEE IV 2022 | LiDAR | Intermediate | 2022 | V,I | Trad Feat | — |
| [Slim-FCP](https://doi.org/10.1007/978-3-031-20080-9_10) | ECCV 2022 | LiDAR | Intermediate | 2022 | V | Trad Feat | — |
| [AdaptiveFeature](https://doi.org/10.1109/WACV56688.2023.00124) | WACV 2023 | LiDAR | Intermediate | 2023 | V | Trad Feat | — |
| [CoBEVFlow](https://arxiv.org/abs/2308.01558) | NeurIPS 2023 | LiDAR | Intermediate | 2023 | V | Trad Feat | [Code](https://github.com/MediaBrain-SJTU/CoBEVFlow) |
| [DI-V2X](https://arxiv.org/abs/2306.09609) | AAAI 2023 | LiDAR | Intermediate | 2023 | V,I | Trad Feat | [Code](https://github.com/Serenos/DI-V2X) |
| [DFS](https://doi.org/10.1109/ITSC55140.2022.9921947) | IEEE ITSC 2023 | LiDAR | Intermediate | 2023 | V,I | Trad Feat | — |
| [FFNet](https://arxiv.org/abs/2305.14580) | NeurIPS 2023 | LiDAR | Intermediate | 2023 | V,I | Trad Feat | [Code](https://github.com/haibao-yu/FFNet-VIC3D) |
| [CoAlign](https://doi.org/10.1109/ICRA48891.2023.10161366) | ICRA 2023 | LiDAR | Intermediate | 2023 | V | Trad Feat | [Code](https://github.com/yifanlu0227/CoAlign) |
| [VINet](https://arxiv.org/abs/2306.04307) | arXiv 2023 | LiDAR | Intermediate | 2023 | V,I | Trad Feat | — |
| [FDA](https://arxiv.org/abs/2401.09427) | ICRA 2024 | LiDAR | Intermediate | 2024 | V,I | Trad Feat | — |
| [HP3D-V2V](https://arxiv.org/abs/2401.12636) | IEEE T-IV 2024 | LiDAR | Intermediate | 2024 | V | Trad Feat | — |
| [MACP](https://arxiv.org/abs/2401.05916) | ICRA 2024 | LiDAR | Intermediate | 2024 | V | Trad Feat | [Code](https://github.com/PurdueDigitalTwin/MACP) |
| [S2R-ViT](https://arxiv.org/abs/2403.09243) | ICRA 2024 | LiDAR | Intermediate | 2024 | V | Trad Feat | — |
| [Select2Col](https://arxiv.org/abs/2306.08534) | AAAI 2024 | LiDAR | Intermediate | 2024 | V | Trad Feat | [Code](https://github.com/huangqzj/Select2Col) |
| [PillarAttention](https://arxiv.org/abs/2310.03343) | IEEE IoT-J 2024 | LiDAR | Intermediate | 2024 | V,I | Trad Feat | — |
| [DUSA](https://arxiv.org/abs/2305.11548) | ACM MM 2023 | LiDAR | Intermediate | 2023 | V,I | — | — |
| [UMC](https://arxiv.org/abs/2303.17015) | ICCV 2023 | LiDAR | Intermediate | 2023 | V | Graph | [Code](https://github.com/ispc-lab/UMC) |
| [HPL-ViT](https://arxiv.org/abs/2312.08823) | ICRA 2024 | LiDAR | Intermediate | 2024 | V | Graph | [Code](https://github.com/arnold-yyy/HPL-ViT) |
| [F-Transformer](https://doi.org/10.1007/978-3-031-15919-0_15) | ICANN 2022 | LiDAR | Intermediate | 2022 | V | Atten Feat | — |
| [CRCNet](https://doi.org/10.1109/TITS.2023.3272027) | IEEE T-ITS 2023 | LiDAR | Intermediate | 2022 | V | Atten Feat | — |
| [V2X-ViT](https://doi.org/10.1007/978-3-031-19842-7_7) | ECCV 2022 | LiDAR | Intermediate | 2022 | V,I | Atten Feat | [Code](https://github.com/DerrickXuNu/v2x-vit) |
| [MPDA](https://doi.org/10.1109/ICRA48891.2023.10160871) | ICRA 2023 | LiDAR | Intermediate | 2023 | V,I | Atten Feat | [Code](https://github.com/haibao-yu/FFNet-VIC3D) |
| [Co3D](https://arxiv.org/abs/2309.01963) | IEEE T-ITS 2023 | LiDAR | Intermediate | 2023 | V,I | Atten Feat | — |
| [FeaCo](https://arxiv.org/abs/2308.11648) | ACM MM 2023 | LiDAR | Intermediate | 2023 | V | Atten Feat | [Code](https://github.com/jmgu0212/FeaCo) |
| [How2comm](https://arxiv.org/abs/2305.01425) | NeurIPS 2023 | LiDAR | Intermediate | 2023 | V | Atten Feat | [Code](https://github.com/ydk122024/How2comm) |
| [LCRN](https://arxiv.org/abs/2310.02544) | NeurIPS 2023 | LiDAR | Intermediate | 2023 | V | Atten Feat | [Code](https://github.com/JesseWong333/metacoop) |
| [SCOPE](https://arxiv.org/abs/2307.08371) | ICCV 2023 | LiDAR | Intermediate | 2023 | V | Atten Feat | [Code](https://github.com/startracker0/SCOPE) |
| [What2comm](https://arxiv.org/abs/2307.12432) | ACM MM 2023 | LiDAR | Intermediate | 2023 | V,I | Atten Feat | — |
| [CenterCoop](https://doi.org/10.1109/LRA.2023.3339399) | IEEE RA-L 2024 | LiDAR | Intermediate | 2024 | V,I | Atten Feat | — |
| [V2X-INCOP](https://arxiv.org/abs/2309.09035) | IEEE T-IV 2024 | LiDAR | Intermediate | 2024 | V,I | Atten Feat | [Code](https://github.com/jinlong17/V2INCOP) |
| [MKD-Cooper](https://arxiv.org/abs/2404.06981) | arXiv 2024 | LiDAR | Intermediate | 2024 | V | Atten Feat | [Code](https://github.com/Bosszhe/MKD-Cooper) |
| [Self-Adaptive](https://arxiv.org/abs/2310.07954) | arXiv 2024 | LiDAR | Intermediate | 2024 | V | Atten Feat | — |
| [SemanticComm](https://arxiv.org/abs/2401.09279) | J. Franklin Inst. 2024 | LiDAR | Intermediate | 2024 | V | Atten Feat | — |
| [V2VFormer](https://arxiv.org/abs/2403.07647) | arXiv 2024 | LiDAR | Intermediate | 2024 | V | Atten Feat | [Code](https://github.com/PurdueDigitalTwin/V2VFormer) |
| [FL-Dynamic](https://doi.org/10.1109/LRA.2021.3134969) | IEEE RA-L 2021 | LiDAR | Late | 2021 | V | Obj | [Code](https://github.com/yys123456/Federated-Learning-for-Cooperative-Perception) |
| [Env-T2TF](https://arxiv.org/abs/2209.01390) | arXiv 2022 | LiDAR | Late | 2022 | V | Obj | — |
| [Co-perception](https://arxiv.org/abs/2307.01036) | IEEE IV 2023 | LiDAR | Late | 2023 | V | Obj | — |
| [Among Us](https://arxiv.org/abs/2309.05061) | ICCV 2023 | LiDAR | Late | 2023 | V | Obj | [Code](https://github.com/coperception/star) |
| [Collective PV-RCNN](https://doi.org/10.1109/ITSC57777.2023.10422079) | IEEE ITSC 2023 | LiDAR | Late | 2023 | V | Trad Feat | — |
| [Late-CNN](https://arxiv.org/abs/2204.00494) | arXiv 2022 | LiDAR | Late | 2023 | V | Obj | [Code](https://github.com/coperception/coperception) |
| [Model-Agnostic](https://arxiv.org/abs/2401.11001) | arXiv 2023 | LiDAR | Late | 2023 | V | Obj | [Code](https://github.com/tum-traffic-dataset/tumtraf-v2x) |
| [Double-M](https://arxiv.org/abs/2309.00668) | arXiv 2023 | LiDAR | Late | 2023 | V,I | Obj | — |
| [Pillar-based CP](https://doi.org/10.1109/ITSC55140.2022.9921805) | IEEE ITSC 2022 | LiDAR | Hybrid | 2022 | V | Hybrid(Raw,Trad,Obj) | — |
| [ML-Cooper](https://arxiv.org/abs/2209.07756) | arXiv 2022 | LiDAR | Hybrid | 2022 | V | Hybrid(Raw,Trad,Obj) | — |
| [FPV-RCNN](https://arxiv.org/abs/2404.07717) | IEEE RA-L 2024 | LiDAR | Hybrid | 2024 | V | Trad Feat | [Code](https://github.com/YuanYunshuang/FPV_RCNN) |
| [FreeAlign](https://arxiv.org/abs/2405.05177) | ICRA 2024 | LiDAR | Hybrid | 2024 | V | Trad Feat | [Code](https://github.com/MediaBrain-SJTU/FreeAlign) |

**LiDAR-Camera fusion:**

| Method | Venue | Modality | Scheme | Year | Entity | Fusion | Code |
|--------|-------|----------|--------|------|--------|--------|:----:|
| [ViT-FuseNet](https://arxiv.org/abs/2401.09025) | arXiv 2024 | LiDAR, Camera | Early | 2024 | V,I | Atten Feat | — |
| [Multi-vehicle fusion](https://arxiv.org/abs/2305.15747) | arXiv 2023 | LiDAR, Camera | Intermediate | 2023 | V | Trad Feat | — |
| [V2VFusion](https://arxiv.org/abs/2205.14979) | arXiv 2022 | LiDAR, Camera | Intermediate | 2023 | V | Trad Feat | — |
| [HEAL](https://arxiv.org/abs/2309.07882) | ICRA 2024 | LiDAR, Camera | Intermediate | 2024 | V | Trad Feat | [Code](https://github.com/yifanlu0227/HEAL) |
| [HGAN](https://doi.org/10.1145/3503161.3548197) | IEEE PAAP 2022 | LiDAR, Camera | Intermediate | 2022 | V,I | Hybrid | — |
| [Distilled Co-Graph](https://arxiv.org/abs/2106.07060) | arXiv 2021 | LiDAR, Camera | Intermediate | 2021 | V | Graph | [Code](https://github.com/ai4ce/DiscoNet) |
| [HM-ViT](https://arxiv.org/abs/2304.12516) | ICCV 2023 | LiDAR, Camera | Intermediate | 2023 | V | Graph | [Code](https://github.com/XHwind/HM-ViT) |
| [Where2comm](https://arxiv.org/abs/2209.12836) | NeurIPS 2022 | LiDAR, Camera | Intermediate | 2022 | V | Atten Feat | [Code](https://github.com/MediaBrain-SJTU/where2comm) |
| [MCoT](https://arxiv.org/abs/2401.09476) | arXiv 2023 | LiDAR, Camera | Intermediate | 2023 | V | Atten Feat | — |
| [PAFNet](https://arxiv.org/abs/2402.01008) | arXiv 2024 | LiDAR, Camera | Intermediate | 2024 | V,I | Atten Feat | — |
| [V2VFormer++](https://arxiv.org/abs/2403.04563) | arXiv 2024 | LiDAR, Camera | Intermediate | 2024 | V | Atten Feat | — |
| [TCLF](https://doi.org/10.1109/CVPR52688.2022.02067) | CVPR 2022 | LiDAR, Camera | Late | 2022 | V,I | Obj | [Code](https://github.com/AIR-THU/DAIR-V2X) |
| [VICOD](https://arxiv.org/abs/2208.13026) | arXiv 2022 | LiDAR, Camera | Late | 2022 | V,I | Obj | — |

**Camera-based:**

| Method | Venue | Modality | Scheme | Year | Entity | Fusion | Code |
|--------|-------|----------|--------|------|--------|--------|:----:|
| [CoCa3D](https://doi.org/10.1109/CVPR52729.2023.01318) | CVPR 2023 | Camera | Intermediate | 2023 | V,I | Trad Feat | [Code](https://github.com/MediaBrain-SJTU/CoCa3D) |
| [ActFormer](https://arxiv.org/abs/2403.09229) | ICRA 2024 | Camera | Intermediate | 2024 | V | Atten Feat | [Code](https://github.com/cwc1260/ActFormer) |
| [EMIFF](https://arxiv.org/abs/2309.00587) | ICRA 2024 | Camera | Intermediate | 2024 | V,I | Trad Feat | [Code](https://github.com/Bosszhe/EMIFF) |
| [QUEST](https://arxiv.org/abs/2308.04480) | arXiv 2024 | Camera | Intermediate | 2024 | V,I | Trad Feat | — |

---

#### VI-B. Semantic Segmentation (CSS)

> **TABLE IX** — Overview of the Methods for Collaborative Semantic Segmentation (CSS).
> **V**: Vehicle, **I**: Infrastructure, **UAV**: Uncrewed Aerial Vehicle

**7 papers** providing pixel-wise / point-wise collaborative classification:

| Method | Venue | Year | Modality | Agents | Representation | Scheme | Fusion | Code |
|--------|-------|------|----------|--------|----------------|--------|--------|:----:|
| [When2com](https://doi.org/10.1109/CVPR42600.2020.01499) | CVPR 2020 | 2020 | Camera | UAV | **2D** | Intermediate | Trad Feat | [Code](https://github.com/GT-RIPL/MultiAgentPerception) |
| [Who2com](https://doi.org/10.1109/ICRA40945.2020.9197200) | ICRA 2020 | 2020 | Camera | UAV | **2D** | Intermediate | Trad Feat | [Code](https://github.com/GT-RIPL/MultiAgentPerception) |
| [MASH](https://doi.org/10.1109/IROS45743.2020.9341059) | IROS 2021 | 2021 | Camera | UAV | **2D** | Intermediate | Atten Feat | [Code](https://github.com/GT-RIPL/MultiAgentPerception) |
| [GenBEV](https://doi.org/10.5194/isprs-annals-X-1-W1-2023-303-2023) | ISPRS 2023 | 2023 | LiDAR | V | **BEV** | Early | Raw | [Code](https://github.com/gaolong-data/GENBEV) |
| [CoBEVT](https://arxiv.org/abs/2207.02202) | CoRL 2023 | 2023 | Camera | V | **BEV** | Intermediate | Trad Feat | [Code](https://github.com/DerrickXuNu/CoBEVT) |
| [VICSS](https://doi.org/10.1109/VTC2023-Spring57618.2023.10201005) | IEEE VTC 2023 | 2023 | LiDAR | V,I | **3D** | Intermediate | Atten Feat | — |
| [CoHFF](https://arxiv.org/abs/2404.04139) | CVPR 2024 | 2024 | Camera | V | **3D** | Intermediate | Atten Feat | — |

---

#### VI-C. Object Tracking (COT)

> **TABLE X** — Overview of the Methods for Collaborative Object Tracking (COT).
> **V**: Vehicle, **I**: Infrastructure

**5 papers** tracking dynamic objects across time:

| Method | Venue | Year | Modality | Entity | Scheme | Shared data | Tracker | Fusion | Code |
|--------|-------|------|----------|--------|--------|-------------|---------|--------|:----:|
| [Track-by-det](https://doi.org/10.1109/IV55152.2023.10186777) | IEEE IV 2023 | 2023 | Agnostic | V,I | NA | NA | **with COD** | NA | — |
| [HYDRO-3D](https://doi.org/10.1109/TIV.2022.3163231) | IEEE T-IV 2023 | 2023 | LiDAR | V,I | Intermediate | Feature | **with COD** | Atten Feat | — |
| [FFTrack](https://doi.org/10.1109/CVPR52729.2023.01318) | CVPR 2023 | 2023 | LiDAR | V,I | Intermediate | Feature | **with COD** | Atten Feat | — |
| [MOT-CUP](https://doi.org/10.1109/LRA.2024.3364450) | IEEE RA-L 2023 | 2023 | Agnostic | V | NA | Obj | **with COD** | NA | — |
| [DMSTrack](https://doi.org/10.1109/ICRA57147.2024.10610148) | ICRA 2024 | 2024 | Agnostic | V | Late | Obj | **without COD** | Obj Fusion | [Code](https://github.com/eddiesmo/DMSTrack) |

---

#### VI-D. Motion Prediction (CMP)

> **TABLE XI** — Overview of the Method for Collaborative Motion Prediction (CMP).

**5 papers** forecasting future trajectories or BEV map states:

| Method | Venue | Year | Modality | Entity | Scheme | Representation | Fusion | Code |
|--------|-------|------|----------|--------|--------|----------------|--------|:----:|
| [V2VNet](https://doi.org/10.1007/978-3-030-58536-5_36) | ECCV 2020 | 2020 | LiDAR | V | Intermediate | **Trajectory** | Graph | [Code](https://github.com/coperception/coperception) |
| [V2VNet-Robust](https://arxiv.org/abs/2111.00643) | CoRL 2021 | 2021 | LiDAR | V | Intermediate | **Trajectory** | Hybrid(Atten,Graph) | [Code](https://github.com/coperception/coperception) |
| [Late-early](https://doi.org/10.1109/TITS.2024.3353480) | IEEE T-ITS 2024 | 2024 | LiDAR | V,I | Hybrid | **Trajectory** | Hybrid(Raw,Obj) | [Code](https://github.com/SCP-CN-001/late_early) |
| [BEV-V2X](https://doi.org/10.1109/TIV.2023.3294681) | IEEE T-IV 2023 | 2023 | Camera | V,I | Intermediate | **BEV Map** | Atten Feat | — |
| [V2XFormer](https://doi.org/10.1609/aaai.v38i6.28370) | AAAI 2024 | 2024 | Camera | V,I | Intermediate | **BEV Map** | Trad Feat | [Code](https://github.com/winchell0203/V2XFormer) |

---

#### VI-E. Lane Detection (CLD)

> **TABLE XII** — Overview of the Methods for Collaborative Lane Detection (CLD).

**3 papers** determining road boundaries and lane markings collaboratively:

| Method | Venue | Year | Modality | Entity | Scheme | Representation | Fusion | Code |
|--------|-------|------|----------|--------|--------|----------------|--------|:----:|
| [Co-mapping](https://doi.org/10.1109/CAVS51000.2020.9334564) | IEEE CAVS 2020 | 2020 | Camera | V | Late | **Curve-model** | Kalman filter | — |
| [CoLD Fusion](https://doi.org/10.1109/IV55152.2023.10186769) | IEEE IV 2023 | 2023 | Agnostic | V | Late | **Curve-model** | Spline-based Fusion | — |
| [LaCPF](https://doi.org/10.1016/j.robot.2024.104705) | RAS 2024 | 2024 | Agnostic | V | Late | **BEV map** | Trad Feat | — |

---

#### VI-F. Multi-Task & Task-Agnostic

> **TABLE XIII** — Overview of methods for Multi-Task Pipeline and Task-Agnostic Pipeline.

**10 papers** (3 multi-task + 7 task-agnostic):

| Method | Venue | Year | Modality | Entity | Scheme | Fusion | Task | Code |
|--------|-------|------|----------|--------|--------|--------|------|:----:|
| [V2VNet](https://doi.org/10.1007/978-3-030-58536-5_36) | ECCV 2020 | 2020 | LiDAR | V | Intermediate | Graph | **OD, MP** | [Code](https://github.com/coperception/coperception) |
| [Robust V2VNet](https://arxiv.org/abs/2111.00643) | CoRL 2021 | 2021 | LiDAR | V | Intermediate | Atten Feat, Graph | **OD, MP** | [Code](https://github.com/coperception/coperception) |
| [BEV-V2X](https://doi.org/10.1109/TIV.2023.3294681) | IEEE T-IV 2023 | 2023 | Agnostic | V,I | Intermediate | Atten Feat | **SS, MP** | — |
| [HYDRO-3D](https://doi.org/10.1109/TIV.2022.3163231) | IEEE T-IV 2023 | 2023 | LiDAR | V | Intermediate | Atten Feat | **OD, OT** | — |
| [FF-Tracking](https://doi.org/10.1109/CVPR52729.2023.01318) | CVPR 2023 | 2023 | LiDAR, Camera | V,I | Intermediate | Trad Feat | **OD, OT** | — |
| [CoBEVT](https://arxiv.org/abs/2207.02202) | CoRL 2023 | 2023 | Camera | V | Intermediate | Trad Feat | **OD, SS** | [Code](https://github.com/DerrickXuNu/CoBEVT) |
| [V2XFormer](https://doi.org/10.1609/aaai.v38i6.28370) | AAAI 2024 | 2024 | LiDAR, Camera | V,I | Intermediate | Trad Feat | **OD, MP, AP** | [Code](https://github.com/winchell0203/V2XFormer) |
| [Late-early](https://doi.org/10.1109/TITS.2024.3353480) | IEEE T-ITS 2024 | 2024 | Camera | V,I | Hybrid | Hybrid(Raw,Obj) | **OD, MP** | [Code](https://github.com/SCP-CN-001/late_early) |
| [STAR](https://arxiv.org/abs/2207.05051) | CoRL 2022 | 2022 | LiDAR | V | Intermediate | Trad Feat | **Task-agnostic** | [Code](https://github.com/opensourcedot/starnet) |
| [Core](https://doi.org/10.1109/ICCV51070.2023.00800) | ICCV 2023 | 2023 | LiDAR | V | Intermediate | Trad Feat | **Task-agnostic** | [Code](https://github.com/MediaBrain-SJTU/CORE) |

---

## Approaches to Realistic Issues

This section follows **Section VII** of the survey. Each subsection addresses one category of practical challenges in deploying CP systems in real-world scenarios.

### VII-A. Localization Errors

> **TABLE XIV** — Overview of the Method for Addressing Pose Error.
> **V**: Vehicle, **I**: Infrastructure, **Raw**: Raw Sensor Data, **Feat**: Feature, **Obj**: Object-Level Data

Accurate spatial alignment is essential for effective data fusion. Approaches are categorized into three levels at which pose correction is applied:

| Method | Venue | Year | Modality | Entity | Data | Pose correction approach | Code |
|--------|-------|------|----------|--------|------|--------------------------|------|
| [JointPerception](https://arxiv.org/abs/2206.01001) | IEEE IV 2022 | 2022 | LiDAR | V | **Raw** | ICP Point cloud registration | — |
| [FastClustering](https://arxiv.org/abs/2406.12256) | Cogn. Comput. 2024 | 2024 | LiDAR | V | **Raw** | ICP Point cloud registration | — |
| [Robust V2VNet](https://arxiv.org/abs/2111.00643) | CoRL 2021 | 2021 | LiDAR | V | **Feat** | Markov random field | — |
| [BEV-V2X](https://doi.org/10.1109/TIV.2023.3294681) | IEEE T-IV 2023 | 2023 | Agnostic | V,I | **Feat** | Global spatial aware attention | — |
| [FeaCo](https://arxiv.org/abs/2308.11648) | ACM MM 2023 | 2023 | LiDAR | V | **Feat** | Proposal Centers Matching | [Code](https://github.com/jmgu0212/FeaCo) |
| [MoRFF](https://doi.org/10.1109/VTC2023-Spring57618.2023.10200856) | IEEE VTC 2023 | 2023 | Camera | V | **Feat** | Multi-view feature matching | — |
| [FPV-RCNN](https://arxiv.org/abs/2404.07717) | IEEE RA-L 2024 | 2024 | LiDAR | V | **Feat** | Semantic keypoint feature matching | [Code](https://github.com/YuanYunshuang/FPV_RCNN) |
| [Co-perception](https://arxiv.org/abs/2307.01036) | IEEE IV 2023 | 2023 | Agnostic | V | **Obj** | Optimal transport theory | — |
| [CoAlign](https://doi.org/10.1109/ICRA48891.2023.10161366) | ICRA 2023 | 2023 | LiDAR | V | **Obj** | Agent-Object Pose Graph Optimization | [Code](https://github.com/yifanlu0227/CoAlign) |
| [FreeAlign](https://arxiv.org/abs/2405.05177) | ICRA 2024 | 2024 | LiDAR | V | **Obj** | Graph matching | [Code](https://github.com/MediaBrain-SJTU/FreeAlign) |

### VII-B. Time Latency

> **TABLE XV** — Overview of Methods for Addressing Latency at the Feature Level.
> **V**: Vehicle, **I**: Infrastructure

Temporal misalignment due to communication delays reduces fusion accuracy. Three approaches are employed at different data levels:

| Method | Venue | Year | Modality | Entity | Latency approach | Code |
|--------|-------|------|----------|--------|------------------|------|
| [SyncNet](https://doi.org/10.1007/978-3-031-19824-3_19) | ECCV 2022 | 2022 | LiDAR | V | Time-series prediction | [Code](https://github.com/MediaBrain-SJTU/SyncNet) |
| [UMC](https://arxiv.org/abs/2303.17015) | ICCV 2023 | 2023 | LiDAR | V | Time-series prediction | [Code](https://github.com/ispc-lab/UMC) |
| [CoBEVFlow](https://arxiv.org/abs/2308.01558) | NeurIPS 2023 | 2023 | LiDAR | V | BEV/ROI flow prediction | [Code](https://github.com/MediaBrain-SJTU/CoBEVFlow) |
| [FFNet](https://arxiv.org/abs/2305.14580) | NeurIPS 2023 | 2023 | LiDAR | V,I | Feature flow prediction | [Code](https://github.com/haibao-yu/FFNet-VIC3D) |
| [How2comm](https://arxiv.org/abs/2305.01425) | NeurIPS 2023 | 2023 | LiDAR | V | Feature flow prediction | [Code](https://github.com/ydk122024/How2comm) |
| [FF-Tracking](https://doi.org/10.1109/CVPR52729.2023.01318) | CVPR 2023 | 2023 | LiDAR, Camera | V,I | Feature flow prediction | — |
| [V2X-INCOP](https://arxiv.org/abs/2309.09035) | IEEE T-IV 2024 | 2024 | LiDAR | V,I | Feature flow prediction | [Code](https://github.com/jinlong17/V2INCOP) |

### VII-C. Communication Bandwidth Constraints

> **TABLE XVI** — Overview of Methods for Addressing Communication Efficiency.
> **V**: Vehicle, **I**: Infrastructure

Bandwidth limits the volume of shared data in real V2X networks (<10 Mbps). Three strategies are employed:

| Method | Venue | Year | Modality | Entity | Comm. efficiency approach | Code |
|--------|-------|------|----------|--------|---------------------------|------|
| [F-Transformer](https://doi.org/10.1007/978-3-031-15919-0_15) | ICANN 2022 | 2022 | LiDAR | V | Data selection | — |
| [MASH](https://doi.org/10.1109/IROS45743.2020.9341059) | IROS 2021 | 2021 | Camera | UAV | Data selection | [Code](https://github.com/GT-RIPL/MultiAgentPerception) |
| [Where2comm](https://arxiv.org/abs/2209.12836) | NeurIPS 2022 | 2022 | LiDAR, Camera | V | Data selection, Cooperator selection | [Code](https://github.com/MediaBrain-SJTU/where2comm) |
| [CoCa3D](https://doi.org/10.1109/CVPR52729.2023.01318) | CVPR 2023 | 2023 | Camera | V,I | Data selection | [Code](https://github.com/MediaBrain-SJTU/CoCa3D) |
| [DFS](https://doi.org/10.1109/ITSC55140.2022.9921947) | IEEE ITSC 2023 | 2023 | LiDAR | V,I | Data selection | — |
| [What2comm](https://arxiv.org/abs/2307.12432) | ACM MM 2023 | 2023 | LiDAR | V,I | Data selection | — |
| [How2comm](https://arxiv.org/abs/2305.01425) | NeurIPS 2023 | 2023 | LiDAR | V | Data selection, Data compression | [Code](https://github.com/ydk122024/How2comm) |
| [FPV-RCNN](https://arxiv.org/abs/2404.07717) | IEEE RA-L 2024 | 2024 | LiDAR | V | Data selection | [Code](https://github.com/YuanYunshuang/FPV_RCNN) |
| [EdgeCooper](https://arxiv.org/abs/2401.09128) | IEEE JSAC 2024 | 2024 | LiDAR | V,I | Data selection | — |
| [SemanticComm](https://arxiv.org/abs/2401.09279) | J. Franklin Inst. 2024 | 2024 | LiDAR | V | Data selection | — |
| [PillarAttention](https://arxiv.org/abs/2310.03343) | IEEE IoT-J 2024 | 2024 | LiDAR | V,I | Data selection | — |
| [CenterCoop](https://doi.org/10.1109/LRA.2023.3339399) | IEEE RA-L 2024 | 2024 | LiDAR | V,I | Data selection | — |
| [AFS-COD](https://doi.org/10.1109/CAVS51000.2020.9334618) | IEEE CAVS 2020 | 2020 | LiDAR | V | Data compression | — |
| [Slim-FCP](https://doi.org/10.1007/978-3-031-20080-9_10) | ECCV 2022 | 2022 | LiDAR | V | Data compression | — |
| [When2com](https://doi.org/10.1109/CVPR42600.2020.01499) | CVPR 2020 | 2020 | Camera | UAV | Cooperator selection | — |
| [Who2com](https://doi.org/10.1109/ICRA40945.2020.9197200) | ICRA 2020 | 2020 | Camera | UAV | Cooperator selection | — |
| [Co3D](https://arxiv.org/abs/2309.01963) | IEEE T-ITS 2023 | 2023 | LiDAR | V,I | Cooperator selection | — |

### VII-D. Communication Interruptions

Ad-hoc vehicular networks are prone to packet loss and communication disruptions. Currently, **only one study** specifically addresses this challenge in CP:

- **[V2X-INCOP](https://arxiv.org/abs/2309.09035)** — Ren et al., *IEEE T-IV*, 2024 — [Code](https://github.com/jinlong17/V2INCOP)
  Estimates missing data through prediction using historical information from previous frames when packets fail to arrive due to collision (communication interruption).

### VII-E. Domain Shifts

> **TABLE XVII** — Overview of Methods for Addressing Domain Shift.
> **V**: Vehicle, **I**: Infrastructure

CP models often perform poorly across domains due to training data distribution gaps, sensor differences, or simulation-to-reality mismatches:

| Method | Venue | Year | Modality | Entity | Domain gap | Approach for bridging gap | Code |
|--------|-------|------|----------|--------|------------|---------------------------|------|
| [FDA](https://arxiv.org/abs/2401.09427) | ICRA 2024 | 2024 | LiDAR | V,I | Dataset domain | Learnable Feature Compensation | — |
| [DI-V2X](https://arxiv.org/abs/2306.09609) | AAAI 2023 | 2023 | LiDAR | V,I | LiDAR sensor domain | Domain invariant distillation | — |
| [HPL-ViT](https://arxiv.org/abs/2312.08823) | ICRA 2024 | 2024 | LiDAR | V | LiDAR sensor domain | Heterogeneous Graph-attention | — |
| [DUSA](https://arxiv.org/abs/2305.11548) | ACM MM 2023 | 2023 | LiDAR | V,I | Sim2Real domain | Sim/Real-invariant features | — |
| [S2R-ViT](https://arxiv.org/abs/2403.09243) | ICRA 2024 | 2024 | LiDAR | V | Sim2Real domain | Domain invariant feature learning | — |

### VII-F. Heterogeneity

> **TABLE XVIII** — Overview of Methods for Addressing the Problem of Heterogeneity.
> **V**: Vehicle, **I**: Infrastructure

Vehicles from different manufacturers have diverse sensors and perception models. Approaches address two types of heterogeneity:

| Method | Venue | Year | Modality | Entity | Heterogeneity | Approach | Code |
|--------|-------|------|----------|--------|---------------|----------|------|
| [MPDA](https://doi.org/10.1109/ICRA48891.2023.10160871) | ICRA 2023 | 2023 | LiDAR | V,I | **Model** | Cross-Domain Transformer | [Code](https://github.com/haibao-yu/FFNet-VIC3D) |
| [HGAN](https://doi.org/10.1145/3503161.3548197) | IEEE PAAP 2022 | 2022 | LiDAR, Camera | V,I | **Modality** | Data format alignment: virtual 3D points from RGB | — |
| [HM-ViT](https://arxiv.org/abs/2304.12516) | ICCV 2023 | 2023 | LiDAR, Camera | V | **Modality** | Feature interaction: 3D Graph Attention | [Code](https://github.com/XHwind/HM-ViT) |
| [HEAL](https://arxiv.org/abs/2309.07882) | ICRA 2024 | 2024 | Agnostic | V | **Modality** | Feature alignment: Backward alignment mechanism | [Code](https://github.com/yifanlu0227/HEAL) |

### VII-G. Adversarial Attacks

CP systems are vulnerable to adversarial attacks from malicious vehicles sharing falsified data. Currently, **only one study** specifically addresses this in CP:

- **[ROBOSAC (Among Us)](https://arxiv.org/abs/2309.05061)** — Hu et al., *ICCV 2023* — [Code](https://github.com/coperception/star)
  A general sampling-based framework for adversarially robust CP. Vehicles sample subsets of teammates, compare results with and without them, verify consensus to detect attackers, then output a collaborative result. Does not require prior knowledge of attack patterns.

---
## Evaluation Methods

### Datasets

> Based on **Table XIX–XXI** in the paper. Datasets used for evaluation, organized by real-world vs. synthetic.

**Real-World Datasets:**

| Dataset | Venue | Year | Collaboration | Modality | Task | Paper | Code |
|---------|-------|------|---------------|----------|------|-------|------|
| [T&J](https://arxiv.org/abs/1905.05618) | arXiv | 2019 | V2V | Camera | OD | [Paper](https://arxiv.org/abs/1905.05618) | — |
| [DAIR-V2X](https://doi.org/10.1109/CVPR52688.2022.02067) | CVPR 2022 | 2022 | V2V, V2I | LiDAR, Camera | OD | [Paper](https://doi.org/10.1109/CVPR52688.2022.02067) | [Code](https://github.com/AIR-THU/DAIR-V2X) |
| [V2V4Real](https://doi.org/10.1109/CVPR52729.2023.01318) | CVPR 2023 | 2023 | V2V | LiDAR | OD | [Paper](https://doi.org/10.1109/CVPR52729.2023.01318) | — |
| [TUMTraf-V2X](https://doi.org/10.1109/CVPR52733.2024.02139) | CVPR 2024 | 2024 | V2I | LiDAR, Camera | OD | [Paper](https://doi.org/10.1109/CVPR52733.2024.02139) | — |
| [V2XSet](https://arxiv.org/abs/2202.02951) | ECCV 2022 | 2022 | V2V, V2I | LiDAR | OD | [Paper](https://arxiv.org/abs/2202.02951) | [Code](https://github.com/DerrickXuNu/v2x-vit) |

**Synthetic Datasets (Simulation-Based):**

| Dataset | Venue | Year | Simulator | Collaboration | Modality | Task | Paper | Code |
|---------|-------|------|-----------|---------------|----------|------|-------|------|
| [OPV2V](https://doi.org/10.1109/ICRA46639.2022.9812038) | ICRA 2022 | 2022 | CARLA | V2V | LiDAR, Camera | OD | [Paper](https://doi.org/10.1109/ICRA46639.2022.9812038) | [Code](https://github.com/DerrickXuNu/OpenCOOD) |
| [V2X-Sim 1.0](https://proceedings.neurips.cc/paper/2022/hash/1f07204e5d8c0d2ec24b4be6f9a21dcf-Abstract-Conference.html) | NeurIPS 2022 | 2022 | CARLA+SUMO | V2V, V2I | LiDAR, Camera | OD, SS | [Paper](https://proceedings.neurips.cc/paper/2022/hash/1f07204e5d8c0d2ec24b4be6f9a21dcf-Abstract-Conference.html) | — |
| [V2X-Sim 2.0](https://arxiv.org/abs/2202.10049) | ICRA 2022 | 2022 | CARLA | V2V | LiDAR, Camera | OD | [Paper](https://arxiv.org/abs/2202.10049) | — |
| [IRV2V](https://arxiv.org/abs/2307.06108) | NeurIPS 2023 | 2023 | CARLA | V2V | LiDAR | OD | [Paper](https://arxiv.org/abs/2307.06108) | — |
| [OPV2V+](https://arxiv.org/abs/2401.17794) | arXiv 2024 | 2024 | CARLA | V2V | LiDAR | OD | [Paper](https://arxiv.org/abs/2401.17794) | — |
| [Semantic OPV2V](https://arxiv.org/abs/2207.02202) | CoRL 2023 | 2023 | CARLA | V2V | Camera | SS | [Paper](https://arxiv.org/abs/2207.02202) | — |
| [CODD](https://doi.org/10.1109/ITSC55140.2022.9921947) | IEEE ITSC 2022 | 2022 | SUMO | V2V | LiDAR | OD | [Paper](https://doi.org/10.1109/ITSC55140.2022.9921947) | — |
| [LUCOPP](https://doi.org/10.1109/IV55152.2023.10186693) | IEEE IV 2023 | 2023 | Other | V2V | LiDAR | OD | [Paper](https://doi.org/10.1109/IV55152.2023.10186693) | — |
| [HoloVIC](https://arxiv.org/abs/2403.02640) | arXiv 2024 | 2024 | CARLA | V2I | LiDAR, Camera | OD | [Paper](https://arxiv.org/abs/2403.02640) | — |
| [DeepAccident](https://doi.org/10.1609/aaai.v38i6.28370) | AAAI 2024 | 2024 | CARLA | V2V, V2I | LiDAR, Camera | OD, AP | [Paper](https://doi.org/10.1609/aaai.v38i6.28370) | — |
| [V2X-Seq](https://doi.org/10.1109/CVPR52729.2023.00797) | CVPR 2023 | 2023 | Real+CARLA | V2V, V2I | LiDAR, Camera | OD, MP | [Paper](https://doi.org/10.1109/CVPR52729.2023.00797) | [Code](https://github.com/AIR-THU/DAIR-V2X-Seq) |

### Evaluation Scenarios

**Environment Settings**:
- **Urban**: Most common setting with intersections and dense traffic
- **Rural**: Open roads with sparse traffic
- **Highway**: High-speed scenarios

**Road Configurations**: Roundabouts, straight roads with curves, cross intersections, T-junctions, parking lots

**Conditions**: Daytime, nighttime, various weather conditions (clear, cloudy, rainy, wet, foggy)

### Evaluation Metrics

**General Metrics** (adapted from single-vehicle perception):
- **Object Detection**: mAP (mean Average Precision), AP@IoU, Recall, Precision
- **Object Tracking**: AMOTA, AMOTP, MOTP, HOTA, IDF1, MT, ML, ID Switches
- **Semantic Segmentation**: mIoU (mean Intersection over Union)
- **Lane Detection**: Mean Squared Error, RMSE, MAE

**Custom CP Metrics**:
- **Communication Cost**: Average message size, bandwidth usage
- **Bandwidth-Perception Trade-off**: BIS (Bandwidth Improvement Score), AIB (Average Improvement to Bandwidth), RB Ratio
- **Perception Improvement**: Marginal Gain, ARSV, ARCV, ARCI, ARPC
- **Collaboration Benefit**: Performance gains from multi-agent vs. single-agent perception

---

## Challenges and Opportunities

### Challenges

**Hardware**:
- Multi-modal sensor calibration and synchronization
- Optimal sensor configuration for CP systems
- Hardware limitations and computational constraints

**Software**:
- **Communication**: Limited bandwidth, latency, interruptions, standardization of V2X protocols
- **Fusion Strategy**: Information loss, traditional fusion limitations, data alignment bottlenecks
- **Localization**: Achieving robustness under diverse scenarios, temporal alignment for asynchronous features
- **Uncertainty**: Black-box AI models, trust and reliability assessment
- **Efficiency**: Real-time processing demands vs. computational intensity
- **Domain Shift**: Sim2Real gap, heterogeneity in sensors and models
- **Compatibility**: Integration with existing single-vehicle perception pipelines

**Evaluation**:
- Lack of large-scale real-world datasets with diverse scenarios and modalities
- Need for heterogeneous evaluation considering model and modality differences
- Model training challenges and labeled data requirements
- Evaluation scenarios for safety-critical situations
- Development of CP-specific evaluation metrics

### Opportunities

**Hardware**:
- Optimal sensor configuration research
- Integration of new modalities (radar, thermal, event cameras)

**Software**:
- **Communication**: Data compression, efficient transmission protocols
- **Fusion Strategy**: Advanced hybrid fusion methods, GNN-based approaches
- **Robustness**: Hardware/software failure resilience, adversarial robustness
- **Efficiency**: Model optimization (V2X-ViT [[16]](https://doi.org/10.1007/978-3-031-19842-7_7))
- **Compatibility**: Plug-and-play CP modules for seamless integration

**Evaluation**:
- Large-scale diverse CP datasets with multi-modal sensors
- Open-source simulation frameworks for realistic V2X scenarios
- Comprehensive evaluation methods bridging research and deployment
- Standardized evaluation protocols

### Risks

- **Deployment Gap**: Complexity of real-world conditions vs. controlled experimental settings
- **Reproducibility**: Need for open-source code and standardized evaluation
- **Security**: Vulnerability to adversarial attacks and malicious agents

---

## Tools

This repository includes automated tools for systematic literature review:

### 📚 BibTeX Parser
Parse and categorize papers from BibTeX files based on keywords.

```bash
python tools/data_extraction/bib_parser.py
```

### 🔄 Forward Snowballing Tool
Automatically discover new papers that cite existing works.

```bash
python tools/snowballing/forward_snowballing.py
```

### 🤖 LLM-based Study Selection
Automated study selection using LLM to apply inclusion/exclusion criteria.

```bash
python tools/study_selection/llm_classifier.py
```

See [tools/README.md](tools/README.md) for detailed documentation.

---

## Contributing

We welcome contributions! If you know of papers that should be included, please:

1. Check if the paper meets our [inclusion criteria](docs/inclusion_criteria.md)
2. Add the BibTeX entry to `collaborative-perception.bib` with appropriate keywords
3. Run the parser: `python tools/data_extraction/bib_parser.py`
4. Generate updated README: `python tools/data_extraction/readme_generator.py`
5. Submit a pull request

### Keyword Convention

Use these keywords in BibTeX entries:

**Modality**: `CP-LiDAR`, `CP-Camera`, `CP-Fusion`
**Collaboration**: `CP-Early`, `CP-Intermediate`, `CP-Late`, `CP-Hybrid`
**Task**: `CP-Object Detection`, `CP-Object Tracking`, `CP-Semantic Segmentation`, `CP-Motion Prediction`, `CP-Lane Detection`, `CP-Multi-task`

---

## Citation

If you find this repository useful, please cite our survey paper:

```bibtex
@article{wan2026systematic,
  title={A Systematic Literature Review on Vehicular Collaborative Perception: A Computer Vision Perspective},
  author={Wan, Lei and others},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2026}
}
```

---

## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

---

**Maintained by**: Lei Wan ([lei.wan@partner.kit.edu](mailto:lei.wan@partner.kit.edu))
**Last Updated**: 2026-02
**Paper Version**: Published in IEEE T-ITS 2026
