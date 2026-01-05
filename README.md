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
- 📊 **109 Papers**: Comprehensive collection from systematic literature review (2019-2024)
- 🏷️ **Organized Taxonomy**: By modality, collaboration type, and perception task
- 📈 **PRISMA 2020**: Follows systematic review guidelines

---

## Table of Contents

- [Statistics](#statistics)
- [Taxonomy](#taxonomy)
  - [By Modality](#by-modality)
  - [By Collaboration Type](#by-collaboration-type)
  - [By Perception Task](#by-perception-task)
- [Papers](#papers)
  - [LiDAR-based Methods](#lidar-based-methods)
  - [Camera-based Methods](#camera-based-methods)
  - [Early Collaboration](#early-collaboration)
  - [Intermediate Collaboration](#intermediate-collaboration)
  - [Late Collaboration](#late-collaboration)
  - [Hybrid Collaboration](#hybrid-collaboration)
  - [Object Detection](#object-detection)
  - [Object Tracking](#object-tracking)
  - [Semantic Segmentation](#semantic-segmentation)
  - [Motion Prediction & Lane Detection](#motion-prediction--lane-detection)
- [Tools](#tools)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

---

## Statistics

**Total Papers**: 109

| Category | Count |
|----------|-------|
| **Modality** | |
| └─ LiDAR | 83 |
| └─ Camera | 24 |
| **Collaboration Type** | |
| └─ Late | 12 |
| └─ Intermediate | 71 |
| └─ Hybrid | 3 |
| └─ Early | 7 |
| **Perception Task** | |
| └─ Object Tracking | 3 |
| └─ Object Detection | 82 |
| └─ Semantic Segmentation | 5 |
| └─ Lane Detection | 3 |

---

## Taxonomy

Our systematic literature review categorizes collaborative perception methods along three dimensions:

### By Modality

- **LiDAR-based**: Methods using 3D point cloud data from LiDAR sensors
- **Camera-based**: Methods using 2D RGB images from cameras
- **LiDAR-Camera Fusion**: Methods combining both modalities

### By Collaboration Type

- **Early Collaboration**: Sharing raw sensor data (point clouds, images)
- **Intermediate Collaboration**: Sharing intermediate feature representations
- **Late Collaboration**: Sharing detection/prediction results
- **Hybrid Collaboration**: Combining multiple collaboration strategies

### By Perception Task

- **Object Detection**: 3D bounding box detection
- **Object Tracking**: Multi-object tracking across time
- **Semantic Segmentation**: Point-wise or pixel-wise classification
- **Motion Prediction**: Future trajectory forecasting
- **Lane Detection**: Road structure understanding
- **Multi-task**: Multiple perception tasks simultaneously

---

## Papers

### LiDAR-based Methods

**83 papers**

- **3D Multi-Object Tracking**  
  Su, Hao, Arakawa, Shin'Ichi, Murata, Masayuki  
  *2023 IEEE Intelligent Vehicles Symposium*, 2023  
  [[DOI](https://doi.org/10.1109/IV55152.2023.10186777)]
- **Adaptive Feature Fusion**  
  Qiao, Donghao, Zulkernine, Farhana  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/WACV56688.2023.00124)]
- **Asynchrony-Robust Collaborative Perception**  
  Wei, Sizhe et al.  
  *N/A*, N/A
- **Bandwidth-Adaptive Feature Sharing**  
  Marvasti, Ehsan Emad et al.  
  *2020 IEEE*, 2020  
  [[DOI](https://doi.org/10.1109/CAVS51000.2020.9334618)]
- **Breaking Data Silos**  
  Li, Jinlong et al.  
  *N/A*, 2024
- **Bridging the Domain Gap**  
  Xu, Runsheng et al.  
  *2023 IEEE International Conference*, 2023  
  [[DOI](https://doi.org/10.1109/ICRA48891.2023.10160871)]
- **CenterCoop**  
  Zhou, Linyi, Gan, Zhongxue, Fan, Jiayuan  
  *IEEE Robotics and Automation Letters*, 2024  
  [[DOI](https://doi.org/10.1109/LRA.2023.3339399)]
- **CoFF**  
  Guo, Jingda et al.  
  *IEEE Internet of Things Journal*, 2021  
  [[DOI](https://doi.org/10.1109/JIOT.2021.3053184)]
- **Collaborative 3D Object Detection**  
  Wang, J., Zeng, Y., Gong, Y.  
  *IEEE Transactions on Intelligent Transportation Systems*, 2023  
  [[DOI](https://doi.org/10.1109/TITS.2023.3272027)]
- **Collaborative Multi-Object Tracking With Conformal Uncertainty Propagation**  
  Su, Sanbao et al.  
  *IEEE Robotics and Automation Letters*, 2024  
  [[DOI](https://doi.org/10.1109/LRA.2024.3364450)]
- **Collective PV-RCNN**  
  Teufel, Sven, Gamerdinger, J{\"o  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ITSC57777.2023.10422079)]
- **Complementarity-Enhanced**  
  Luo, Guiyang et al.  
  *Proceedings of the 30th ACM International Conference*, 2022  
  [[DOI](https://doi.org/10.1145/3503161.3548197)]
- **Cooperative LIDAR Object Detection**  
  Marvasti, Ehsan Emad et al.  
  *2020 IEEE*, 2020  
  [[DOI](https://doi.org/10.1109/VTC2020-Fall49728.2020.9348723)]
- **Cooperative Perception With Learning-Based V2V Communications**  
  Liu, Chenguang et al.  
  *IEEE Wireless Communications Letters*, 2023  
  [[DOI](https://doi.org/10.1109/LWC.2023.3295612)]
- **A Cooperative Perception System Robust**  
  Song, Zhiying et al.  
  *2023 IEEE Intelligent Vehicles Symposium*, 2023  
  [[DOI](https://doi.org/10.1109/IV55152.2023.10186727)]
- **Core: Cooperative Reconstruction**  
  Wang, Binglu et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00800)]
- **DAIR-V2X**  
  Yu, Haibao et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/CVPR52688.2022.02067)]
- **Latency-Aware Collaborative Perception**  
  Lei, Zixing et al.  
  *Computer Vision - ECCV*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-19824-3\\\\_19)]
- **DI-V2X**  
  Xiang, Li et al.  
  *N/A*, 2023
- **DOLPHINS**  
  Mao, Ruiqing et al.  
  *Computer Vision*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-26348-4\_29)]
- **DUSA**  
  Kong, Xianghao et al.  
  *Proceedings of the 31st ACM International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3581783.3611948)]
- **DeepAccident**  
  Wang, Tianqi et al.  
  *Proceedings of the AAAI Conference on Artificial Intelligence*, 2024  
  [[DOI](https://doi.org/10.1609/aaai.v38i6.28370)]
- **Distributed Dynamic Map Fusion**  
  Zhang, Zijian et al.  
  *2021 IEEE International Conference*, 2021  
  [[DOI](https://doi.org/10.1109/ICRA48506.2021.9561612)]
- **Dynamic Feature Sharing**  
  Bai, Zhengwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ITSC57777.2023.10422242)]
- **EdgeCooper**  
  Luo, Guiyang et al.  
  *IEEE Journal on Selected Areas in Communications*, 2024  
  [[DOI](https://doi.org/10.1109/JSAC.2023.3322764)]
- **F-Transformer**  
  Wang, Jie et al.  
  *Artificial Neural Networks*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-15919-0\_15)]
- **Fast Clustering**  
  Kuang, Xinkai et al.  
  *Cognitive Computation*, 2024  
  [[DOI](https://doi.org/10.1007/s12559-023-10211-x)]
- **F-Cooper: Feature Based Cooperative Perception for Autonomous Vehicle Edge Computing System Using 3D**  
  Chen, Qi et al.  
  *Proceedings of the 4th ACM*, 2019  
  [[DOI](https://doi.org/10.1145/3318216.3363300)]
- **FeaCo**  
  Gu, Jiaming et al.  
  *Proceedings of the 31st ACM International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3581783.3611880)]
- **Flow-Based Feature Fusion**  
  Yu, Haibao et al.  
  *N/A*, 2023
- **Generating Evidential BEV Maps**  
  Yuan, Yunshuang et al.  
  *ISPRS Journal of Photogrammetry and Remote Sensing*, 2023  
  [[DOI](https://doi.org/10.1016/j.isprsjprs.2023.08.013)]
- **HP3D-V2V**  
  Chen, Hongmei et al.  
  *Sensors*, 2024  
  [[DOI](https://doi.org/10.3390/s24072170)]
- **HPL-ViT**  
  Liu, Yuhang et al.  
  *N/A*, 2023
- **HYDRO-3D**  
  Meng, Zonglin et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2023  
  [[DOI](https://doi.org/10.1109/TIV.2023.3282567)]
- **How2comm: Communication-Efficient**  
  Yang, Dingkang et al.  
  *N/A*, N/A
- **Interruption-Aware Cooperative Perception**  
  Ren, Shunli et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2024.3371974)]
- **A Joint Perception Scheme For Connected Vehicles**  
  Ahmed, Ahmed N. et al.  
  *2022 IEEE Sensors*, 2022  
  [[DOI](https://doi.org/10.1109/SENSORS52175.2022.9967271)]
- **Keypoints-Based Deep Feature Fusion**  
  Yuan, Yunshuang, Cheng, Hao, Sester, Monika  
  *IEEE Robotics and Automation Letters*, 2022  
  [[DOI](https://doi.org/10.1109/LRA.2022.3143299)]
- **Learning to Communicate**  
  Vadivelu, Nicholas et al.  
  *Proceedings of the 2020 Conference*, 2021
- **Learning Distilled Collaboration Graph**  
  Li, Yiming et al.  
  *Advances in Neural Information Processing Systems*, 2021
- **Learning for Vehicle-to-Vehicle Cooperative Perception Under Lossy Communication**  
  Li, Jinlong et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2023  
  [[DOI](https://doi.org/10.1109/TIV.2023.3260040)]
- **A LiDAR Semantic Segmentation Framework**  
  Liu, Hongwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/VTC2023-Fall60731.2023.10333790)]
- **MACP**  
  Ma, Yunsheng et al.  
  *2024 IEEE*, 2024  
  [[DOI](https://doi.org/10.1109/WACV57701.2024.00334)]
- **MCoT**  
  Shi, Shanwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICPADS60453.2023.00226)]
- **MKD-Cooper**  
  Li, Zhiyuan et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2023.3310580)]
- **Model-Agnostic Multi-Agent Perception Framework**  
  Xu, Runsheng et al.  
  *2023 IEEE International Conference*, 2023  
  [[DOI](https://doi.org/10.1109/ICRA48891.2023.10161460)]
- **Multi-Modal Virtual-Real Fusion**  
  Zhang, Hui et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/PAAP56126.2022.10010640)]
- **Multi-Robot Scene Completion**  
  Li, Yiming et al.  
  *N/A*, N/A
- **Multimodal Cooperative 3D Object Detection Over Connected Vehicles**  
  Chi, Fangyuan et al.  
  *IEEE Network*, 2023  
  [[DOI](https://doi.org/10.1109/MNET.010.2300029)]
- **Multistage Fusion Approach**  
  Yu, Hang et al.  
  *2022 5th World Conference*, 2022  
  [[DOI](https://doi.org/10.1109/WCMEIM56910.2022.10021459)]
- **OPV2V**  
  Xu, Runsheng et al.  
  *2022 International Conference*, 2022  
  [[DOI](https://doi.org/10.1109/ICRA46639.2022.9812038)]
- **PAFNet**  
  Wang, Luyang, Lan, Jinhui, Li, Min  
  *Symmetry*, 2024  
  [[DOI](https://doi.org/10.3390/sym16040401)]
- **Pillar Attention Encoder**  
  Bai, Zhengwei et al.  
  *IEEE Internet of Things Journal*, 2024  
  [[DOI](https://doi.org/10.1109/JIOT.2024.3390552)]
- **Pillar-Based Cooperative Perception**  
  Wang, Jian et al.  
  *Wireless Communications and Mobile Computing*, 2022  
  [[DOI](https://doi.org/10.1155/2022/3646272)]
- **PillarGrid**  
  Bai, Zhengwei et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/ITSC55140.2022.9921947)]
- **Practical Collaborative Perception**  
  Dao, Minh-Quan, Berrio, Julie Stephany, Fr{\'e  
  *IEEE Transactions on Intelligent Transportation Systems*, 2024  
  [[DOI](https://doi.org/10.1109/TITS.2024.3371177)]
- **Region-Based Hybrid Collaborative Perception**  
  Liu, Pengfei et al.  
  *IEEE Transactions on Vehicular Technology*, 2024  
  [[DOI](https://doi.org/10.1109/TVT.2023.3324439)]
- **Robust Collaborative 3D Object Detection**  
  Lu, Yifan et al.  
  *2023 IEEE International Conference*, 2023  
  [[DOI](https://doi.org/10.1109/ICRA48891.2023.10160546)]
- **Robust Collaborative Perception**  
  Ren, Shunli et al.  
  *N/A*, N/A
- **Robust Collaborative Perception**  
  Lei, Zixing et al.  
  *N/A*, 2024 [[arXiv](https://arxiv.org/abs/2405.02965)]
- **Robust Real-time Multi-vehicle Collaboration**  
  Zhang, Qingzhao et al.  
  *Proceedings of the 29th Annual International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3570361.3613271)]
- **S2R-ViT**  
  Li, Jinlong et al.  
  *N/A*, 2024
- **Select2Col**  
  Liu, Yuntao et al.  
  *N/A*, 2024
- **Self-Supervised Adaptive Weighting**  
  Liu, Chenguang et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2023.3345035)]
- **Semantic Communication for Cooperative Perception Based on Importance Map**  
  Sheng, Yucheng et al.  
  *Journal of the Franklin Institute*, 2024  
  [[DOI](https://doi.org/10.1016/j.jfranklin.2024.106739)]
- **Slim-FCP**  
  Guo, Jingda et al.  
  *IEEE Internet of Things Journal*, 2022  
  [[DOI](https://doi.org/10.1109/JIOT.2022.3153260)]
- **Soft Actor**  
  Xie, Qi et al.  
  *IEEE Internet of Things Journal*, 2022  
  [[DOI](https://doi.org/10.1109/JIOT.2022.3179739)]
- **Spatio-Temporal Domain Awareness**  
  Yang, Kun et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.02137)]
- **TUMTraf V2X Cooperative Perception Dataset**  
  Zimmer, Walter et al.  
  *N/A*, 2024
- **UMC**  
  Wang, Tianhang et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00752)]
- **Uncertainty Quantification**  
  Su, Sanbao et al.  
  *N/A*, 2023 [[arXiv](https://arxiv.org/abs/2209.08162)]
- **Among Us**  
  Li, Yiming et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00024)]
- **V2VFormer**  
  Yin, Hongbo et al.  
  *IEEE Transactions on Intelligent Transportation Systems*, 2024  
  [[DOI](https://doi.org/10.1109/TITS.2023.3314919)]
- **V2VFormer**  
  Lin, Chunmian et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2024.3353254)]
- **V2VFusion**  
  Zhang, Lei et al.  
  *2023 China Automation Congress*, 2023  
  [[DOI](https://doi.org/10.1109/CAC59555.2023.10450676)]
- **V2VNet**  
  Wang, Tsun-Hsuan et al.  
  *Computer Vision*, 2020  
  [[DOI](https://doi.org/10.1007/978-3-030-58536-5\_36)]
- **V2X-Seq**  
  Yu, Haibao et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/CVPR52729.2023.00531)]
- **V2X-ViT**  
  Xu, Runsheng et al.  
  *Computer Vision*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-19842-7\_7)]
- **VINet**  
  Bai, Zhengwei et al.  
  *Mechanical Systems and Signal Processing*, 2023  
  [[DOI](https://doi.org/10.1016/j.ymssp.2023.110723)]
- **Vehicle-Infrastructure Cooperative 3D Object Detection**  
  Yu, Haibao et al.  
  *N/A*, 2023
- **ViT-FuseNet**  
  Zhou, Yang et al.  
  *IEEE access : practical innovations, open solutions*, 2024  
  [[DOI](https://doi.org/10.1109/ACCESS.2024.3368404)]
- **What2comm: Towards Communication-efficient Collaborative Perception**  
  Yang, Kun et al.  
  *Proceedings of the 31st ACM International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3581783.3611699)]
- **Where2comm: Communication-Efficient Collaborative Perception**  
  Hu, Yue et al.  
  *N/A*, 2022

### Camera-based Methods

**24 papers**

- **ActFormer**  
  Huang, Suozhi et al.  
  *N/A*, 2024
- **Bandwidth Constrained Cooperative Object Detection in Images**  
  Marez, Diego, Nans, Lena, Borden, Samuel T.  
  *Artificial Intelligence*, 2022  
  [[DOI](https://doi.org/10.1117/12.2636279)]
- **CoBEVT**  
  Xu, Runsheng et al.  
  *Proceedings of The*, 2023
- **CoLD Fusion**  
  Gamerdinger, J{\"o  
  *2023 IEEE Intelligent Vehicles Symposium*, 2023  
  [[DOI](https://doi.org/10.1109/IV55152.2023.10186632)]
- **Collaboration Helps Camera Overtake LiDAR**  
  Hu, Yue et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/CVPR52729.2023.00892)]
- **Collaborative Semantic Occupancy Prediction**  
  Song, Rui et al.  
  *N/A*, 2024
- **DAIR-V2X**  
  Yu, Haibao et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/CVPR52688.2022.02067)]
- **DOLPHINS**  
  Mao, Ruiqing et al.  
  *Computer Vision*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-26348-4\_29)]
- **DeepAccident**  
  Wang, Tianqi et al.  
  *Proceedings of the AAAI Conference on Artificial Intelligence*, 2024  
  [[DOI](https://doi.org/10.1609/aaai.v38i6.28370)]
- **EMIFF**  
  Wang, Zhe et al.  
  *N/A*, 2024
- **Enhancing Lane Detection with a Lightweight Collaborative Late Fusion Model**  
  Jahn, Lennart Lorenz Freimuth et al.  
  *Robotics and Autonomous Systems*, 2024  
  [[DOI](https://doi.org/10.1016/j.robot.2024.104680)]
- **MCoT**  
  Shi, Shanwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICPADS60453.2023.00226)]
- **MoRFF**  
  Mao, Ruiqing et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/VTC2023-Fall60731.2023.10333428)]
- **Multimodal Cooperative 3D Object Detection Over Connected Vehicles**  
  Chi, Fangyuan et al.  
  *IEEE Network*, 2023  
  [[DOI](https://doi.org/10.1109/MNET.010.2300029)]
- **Multistage Fusion Approach**  
  Yu, Hang et al.  
  *2022 5th World Conference*, 2022  
  [[DOI](https://doi.org/10.1109/WCMEIM56910.2022.10021459)]
- **OPV2V**  
  Xu, Runsheng et al.  
  *2022 International Conference*, 2022  
  [[DOI](https://doi.org/10.1109/ICRA46639.2022.9812038)]
- **Overcoming Obstructions**  
  Glaser, Nathaniel et al.  
  *2021 IEEE*, 2021  
  [[DOI](https://doi.org/10.1109/IROS51168.2021.9636761)]
- **QUEST**  
  Fan, Siqi et al.  
  *N/A*, 2023
- **TUMTraf V2X Cooperative Perception Dataset**  
  Zimmer, Walter et al.  
  *N/A*, 2024
- **V2VFormer**  
  Yin, Hongbo et al.  
  *IEEE Transactions on Intelligent Transportation Systems*, 2024  
  [[DOI](https://doi.org/10.1109/TITS.2023.3314919)]
- **V2VFusion**  
  Zhang, Lei et al.  
  *2023 China Automation Congress*, 2023  
  [[DOI](https://doi.org/10.1109/CAC59555.2023.10450676)]
- **V2X-Seq**  
  Yu, Haibao et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/CVPR52729.2023.00531)]
- **ViT-FuseNet**  
  Zhou, Yang et al.  
  *IEEE access : practical innovations, open solutions*, 2024  
  [[DOI](https://doi.org/10.1109/ACCESS.2024.3368404)]
- **Where2comm: Communication-Efficient Collaborative Perception**  
  Hu, Yue et al.  
  *N/A*, 2022

### Early Collaboration

**7 papers**

- **EdgeCooper**  
  Luo, Guiyang et al.  
  *IEEE Journal on Selected Areas in Communications*, 2024  
  [[DOI](https://doi.org/10.1109/JSAC.2023.3322764)]
- **Fast Clustering**  
  Kuang, Xinkai et al.  
  *Cognitive Computation*, 2024  
  [[DOI](https://doi.org/10.1007/s12559-023-10211-x)]
- **Generating Evidential BEV Maps**  
  Yuan, Yunshuang et al.  
  *ISPRS Journal of Photogrammetry and Remote Sensing*, 2023  
  [[DOI](https://doi.org/10.1016/j.isprsjprs.2023.08.013)]
- **A Joint Perception Scheme For Connected Vehicles**  
  Ahmed, Ahmed N. et al.  
  *2022 IEEE Sensors*, 2022  
  [[DOI](https://doi.org/10.1109/SENSORS52175.2022.9967271)]
- **Multi-Robot Scene Completion**  
  Li, Yiming et al.  
  *N/A*, N/A
- **Pillar-Based Cooperative Perception**  
  Wang, Jian et al.  
  *Wireless Communications and Mobile Computing*, 2022  
  [[DOI](https://doi.org/10.1155/2022/3646272)]
- **Robust Real-time Multi-vehicle Collaboration**  
  Zhang, Qingzhao et al.  
  *Proceedings of the 29th Annual International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3570361.3613271)]

### Intermediate Collaboration

**71 papers**

- **ActFormer**  
  Huang, Suozhi et al.  
  *N/A*, 2024
- **Adaptive Feature Fusion**  
  Qiao, Donghao, Zulkernine, Farhana  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/WACV56688.2023.00124)]
- **Asynchrony-Robust Collaborative Perception**  
  Wei, Sizhe et al.  
  *N/A*, N/A
- **BEV-V2X**  
  Chang, Cheng et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2023  
  [[DOI](https://doi.org/10.1109/TIV.2023.3293954)]
- **Bandwidth-Adaptive Feature Sharing**  
  Marvasti, Ehsan Emad et al.  
  *2020 IEEE*, 2020  
  [[DOI](https://doi.org/10.1109/CAVS51000.2020.9334618)]
- **Bandwidth Constrained Cooperative Object Detection in Images**  
  Marez, Diego, Nans, Lena, Borden, Samuel T.  
  *Artificial Intelligence*, 2022  
  [[DOI](https://doi.org/10.1117/12.2636279)]
- **Breaking Data Silos**  
  Li, Jinlong et al.  
  *N/A*, 2024
- **Bridging the Domain Gap**  
  Xu, Runsheng et al.  
  *2023 IEEE International Conference*, 2023  
  [[DOI](https://doi.org/10.1109/ICRA48891.2023.10160871)]
- **CenterCoop**  
  Zhou, Linyi, Gan, Zhongxue, Fan, Jiayuan  
  *IEEE Robotics and Automation Letters*, 2024  
  [[DOI](https://doi.org/10.1109/LRA.2023.3339399)]
- **CoBEVT**  
  Xu, Runsheng et al.  
  *Proceedings of The*, 2023
- **CoFF**  
  Guo, Jingda et al.  
  *IEEE Internet of Things Journal*, 2021  
  [[DOI](https://doi.org/10.1109/JIOT.2021.3053184)]
- **Collaboration Helps Camera Overtake LiDAR**  
  Hu, Yue et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/CVPR52729.2023.00892)]
- **Collaborative 3D Object Detection**  
  Wang, J., Zeng, Y., Gong, Y.  
  *IEEE Transactions on Intelligent Transportation Systems*, 2023  
  [[DOI](https://doi.org/10.1109/TITS.2023.3272027)]
- **Collaborative Semantic Occupancy Prediction**  
  Song, Rui et al.  
  *N/A*, 2024
- **Complementarity-Enhanced**  
  Luo, Guiyang et al.  
  *Proceedings of the 30th ACM International Conference*, 2022  
  [[DOI](https://doi.org/10.1145/3503161.3548197)]
- **Cooperative LIDAR Object Detection**  
  Marvasti, Ehsan Emad et al.  
  *2020 IEEE*, 2020  
  [[DOI](https://doi.org/10.1109/VTC2020-Fall49728.2020.9348723)]
- **Core: Cooperative Reconstruction**  
  Wang, Binglu et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00800)]
- **Latency-Aware Collaborative Perception**  
  Lei, Zixing et al.  
  *Computer Vision - ECCV*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-19824-3\\\\_19)]
- **DI-V2X**  
  Xiang, Li et al.  
  *N/A*, 2023
- **DUSA**  
  Kong, Xianghao et al.  
  *Proceedings of the 31st ACM International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3581783.3611948)]
- **Dynamic Feature Sharing**  
  Bai, Zhengwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ITSC57777.2023.10422242)]
- **EMIFF**  
  Wang, Zhe et al.  
  *N/A*, 2024
- **An Extensible Framework**  
  Lu, Yifan et al.  
  *N/A*, 2024
- **F-Transformer**  
  Wang, Jie et al.  
  *Artificial Neural Networks*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-15919-0\_15)]
- **F-Cooper: Feature Based Cooperative Perception for Autonomous Vehicle Edge Computing System Using 3D**  
  Chen, Qi et al.  
  *Proceedings of the 4th ACM*, 2019  
  [[DOI](https://doi.org/10.1145/3318216.3363300)]
- **FeaCo**  
  Gu, Jiaming et al.  
  *Proceedings of the 31st ACM International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3581783.3611880)]
- **Flow-Based Feature Fusion**  
  Yu, Haibao et al.  
  *N/A*, 2023
- **HM-ViT**  
  Xiang, Hao, Xu, Runsheng, Ma, Jiaqi  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00033)]
- **HP3D-V2V**  
  Chen, Hongmei et al.  
  *Sensors*, 2024  
  [[DOI](https://doi.org/10.3390/s24072170)]
- **HPL-ViT**  
  Liu, Yuhang et al.  
  *N/A*, 2023
- **HYDRO-3D**  
  Meng, Zonglin et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2023  
  [[DOI](https://doi.org/10.1109/TIV.2023.3282567)]
- **How2comm: Communication-Efficient**  
  Yang, Dingkang et al.  
  *N/A*, N/A
- **Interruption-Aware Cooperative Perception**  
  Ren, Shunli et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2024.3371974)]
- **Keypoints-Based Deep Feature Fusion**  
  Yuan, Yunshuang, Cheng, Hao, Sester, Monika  
  *IEEE Robotics and Automation Letters*, 2022  
  [[DOI](https://doi.org/10.1109/LRA.2022.3143299)]
- **Learning to Communicate**  
  Vadivelu, Nicholas et al.  
  *Proceedings of the 2020 Conference*, 2021
- **Learning Distilled Collaboration Graph**  
  Li, Yiming et al.  
  *Advances in Neural Information Processing Systems*, 2021
- **Learning for Vehicle-to-Vehicle Cooperative Perception Under Lossy Communication**  
  Li, Jinlong et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2023  
  [[DOI](https://doi.org/10.1109/TIV.2023.3260040)]
- **A LiDAR Semantic Segmentation Framework**  
  Liu, Hongwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/VTC2023-Fall60731.2023.10333790)]
- **MACP**  
  Ma, Yunsheng et al.  
  *2024 IEEE*, 2024  
  [[DOI](https://doi.org/10.1109/WACV57701.2024.00334)]
- **MCoT**  
  Shi, Shanwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICPADS60453.2023.00226)]
- **MKD-Cooper**  
  Li, Zhiyuan et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2023.3310580)]
- **MoRFF**  
  Mao, Ruiqing et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/VTC2023-Fall60731.2023.10333428)]
- **Multi-Modal Virtual-Real Fusion**  
  Zhang, Hui et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/PAAP56126.2022.10010640)]
- **Multimodal Cooperative 3D Object Detection Over Connected Vehicles**  
  Chi, Fangyuan et al.  
  *IEEE Network*, 2023  
  [[DOI](https://doi.org/10.1109/MNET.010.2300029)]
- **Multistage Fusion Approach**  
  Yu, Hang et al.  
  *2022 5th World Conference*, 2022  
  [[DOI](https://doi.org/10.1109/WCMEIM56910.2022.10021459)]
- **Overcoming Obstructions**  
  Glaser, Nathaniel et al.  
  *2021 IEEE*, 2021  
  [[DOI](https://doi.org/10.1109/IROS51168.2021.9636761)]
- **PAFNet**  
  Wang, Luyang, Lan, Jinhui, Li, Min  
  *Symmetry*, 2024  
  [[DOI](https://doi.org/10.3390/sym16040401)]
- **Pillar Attention Encoder**  
  Bai, Zhengwei et al.  
  *IEEE Internet of Things Journal*, 2024  
  [[DOI](https://doi.org/10.1109/JIOT.2024.3390552)]
- **PillarGrid**  
  Bai, Zhengwei et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/ITSC55140.2022.9921947)]
- **QUEST**  
  Fan, Siqi et al.  
  *N/A*, 2023
- **Robust Collaborative 3D Object Detection**  
  Lu, Yifan et al.  
  *2023 IEEE International Conference*, 2023  
  [[DOI](https://doi.org/10.1109/ICRA48891.2023.10160546)]
- **Robust Collaborative Perception**  
  Ren, Shunli et al.  
  *N/A*, N/A
- **Robust Collaborative Perception**  
  Lei, Zixing et al.  
  *N/A*, 2024 [[arXiv](https://arxiv.org/abs/2405.02965)]
- **S2R-ViT**  
  Li, Jinlong et al.  
  *N/A*, 2024
- **Select2Col**  
  Liu, Yuntao et al.  
  *N/A*, 2024
- **Self-Supervised Adaptive Weighting**  
  Liu, Chenguang et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2023.3345035)]
- **Semantic Communication for Cooperative Perception Based on Importance Map**  
  Sheng, Yucheng et al.  
  *Journal of the Franklin Institute*, 2024  
  [[DOI](https://doi.org/10.1016/j.jfranklin.2024.106739)]
- **Slim-FCP**  
  Guo, Jingda et al.  
  *IEEE Internet of Things Journal*, 2022  
  [[DOI](https://doi.org/10.1109/JIOT.2022.3153260)]
- **Spatio-Temporal Domain Awareness**  
  Yang, Kun et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.02137)]
- **UMC**  
  Wang, Tianhang et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00752)]
- **Uncertainty Quantification**  
  Su, Sanbao et al.  
  *N/A*, 2023 [[arXiv](https://arxiv.org/abs/2209.08162)]
- **V2VFormer**  
  Yin, Hongbo et al.  
  *IEEE Transactions on Intelligent Transportation Systems*, 2024  
  [[DOI](https://doi.org/10.1109/TITS.2023.3314919)]
- **V2VFormer**  
  Lin, Chunmian et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2024.3353254)]
- **V2VFusion**  
  Zhang, Lei et al.  
  *2023 China Automation Congress*, 2023  
  [[DOI](https://doi.org/10.1109/CAC59555.2023.10450676)]
- **V2VNet**  
  Wang, Tsun-Hsuan et al.  
  *Computer Vision*, 2020  
  [[DOI](https://doi.org/10.1007/978-3-030-58536-5\_36)]
- **V2X-ViT**  
  Xu, Runsheng et al.  
  *Computer Vision*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-19842-7\_7)]
- **VINet**  
  Bai, Zhengwei et al.  
  *Mechanical Systems and Signal Processing*, 2023  
  [[DOI](https://doi.org/10.1016/j.ymssp.2023.110723)]
- **Vehicle-Infrastructure Cooperative 3D Object Detection**  
  Yu, Haibao et al.  
  *N/A*, 2023
- **ViT-FuseNet**  
  Zhou, Yang et al.  
  *IEEE access : practical innovations, open solutions*, 2024  
  [[DOI](https://doi.org/10.1109/ACCESS.2024.3368404)]
- **What2comm: Towards Communication-efficient Collaborative Perception**  
  Yang, Kun et al.  
  *Proceedings of the 31st ACM International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3581783.3611699)]
- **Where2comm: Communication-Efficient Collaborative Perception**  
  Hu, Yue et al.  
  *N/A*, 2022

### Late Collaboration

**12 papers**

- **3D Multi-Object Tracking**  
  Su, Hao, Arakawa, Shin'Ichi, Murata, Masayuki  
  *2023 IEEE Intelligent Vehicles Symposium*, 2023  
  [[DOI](https://doi.org/10.1109/IV55152.2023.10186777)]
- **CoLD Fusion**  
  Gamerdinger, J{\"o  
  *2023 IEEE Intelligent Vehicles Symposium*, 2023  
  [[DOI](https://doi.org/10.1109/IV55152.2023.10186632)]
- **Collaborative Multi-Object Tracking With Conformal Uncertainty Propagation**  
  Su, Sanbao et al.  
  *IEEE Robotics and Automation Letters*, 2024  
  [[DOI](https://doi.org/10.1109/LRA.2024.3364450)]
- **Collective PV-RCNN**  
  Teufel, Sven, Gamerdinger, J{\"o  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ITSC57777.2023.10422079)]
- **A Cooperative Perception System Robust**  
  Song, Zhiying et al.  
  *2023 IEEE Intelligent Vehicles Symposium*, 2023  
  [[DOI](https://doi.org/10.1109/IV55152.2023.10186727)]
- **Cooperative Road Geometry Estimation**  
  Sakr, Ahmed Hamdi  
  *2020 IEEE*, 2020  
  [[DOI](https://doi.org/10.1109/CAVS51000.2020.9334579)]
- **Distributed Dynamic Map Fusion**  
  Zhang, Zijian et al.  
  *2021 IEEE International Conference*, 2021  
  [[DOI](https://doi.org/10.1109/ICRA48506.2021.9561612)]
- **Enhancing Lane Detection with a Lightweight Collaborative Late Fusion Model**  
  Jahn, Lennart Lorenz Freimuth et al.  
  *Robotics and Autonomous Systems*, 2024  
  [[DOI](https://doi.org/10.1016/j.robot.2024.104680)]
- **Environment-Aware Optimization**  
  Volk, Georg et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/ITSC55140.2022.9922388)]
- **Model-Agnostic Multi-Agent Perception Framework**  
  Xu, Runsheng et al.  
  *2023 IEEE International Conference*, 2023  
  [[DOI](https://doi.org/10.1109/ICRA48891.2023.10161460)]
- **Practical Collaborative Perception**  
  Dao, Minh-Quan, Berrio, Julie Stephany, Fr{\'e  
  *IEEE Transactions on Intelligent Transportation Systems*, 2024  
  [[DOI](https://doi.org/10.1109/TITS.2024.3371177)]
- **Probabilistic 3D Multi-Object Cooperative Tracking**  
  Chiu, Hsu-kuang et al.  
  *N/A*, 2024

### Hybrid Collaboration

**3 papers**

- **Cooperative Perception With Learning-Based V2V Communications**  
  Liu, Chenguang et al.  
  *IEEE Wireless Communications Letters*, 2023  
  [[DOI](https://doi.org/10.1109/LWC.2023.3295612)]
- **Region-Based Hybrid Collaborative Perception**  
  Liu, Pengfei et al.  
  *IEEE Transactions on Vehicular Technology*, 2024  
  [[DOI](https://doi.org/10.1109/TVT.2023.3324439)]
- **Soft Actor**  
  Xie, Qi et al.  
  *IEEE Internet of Things Journal*, 2022  
  [[DOI](https://doi.org/10.1109/JIOT.2022.3179739)]

### Object Detection

**82 papers**

- **ActFormer**  
  Huang, Suozhi et al.  
  *N/A*, 2024
- **Adaptive Feature Fusion**  
  Qiao, Donghao, Zulkernine, Farhana  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/WACV56688.2023.00124)]
- **Asynchrony-Robust Collaborative Perception**  
  Wei, Sizhe et al.  
  *N/A*, N/A
- **Bandwidth-Adaptive Feature Sharing**  
  Marvasti, Ehsan Emad et al.  
  *2020 IEEE*, 2020  
  [[DOI](https://doi.org/10.1109/CAVS51000.2020.9334618)]
- **Bandwidth Constrained Cooperative Object Detection in Images**  
  Marez, Diego, Nans, Lena, Borden, Samuel T.  
  *Artificial Intelligence*, 2022  
  [[DOI](https://doi.org/10.1117/12.2636279)]
- **Breaking Data Silos**  
  Li, Jinlong et al.  
  *N/A*, 2024
- **Bridging the Domain Gap**  
  Xu, Runsheng et al.  
  *2023 IEEE International Conference*, 2023  
  [[DOI](https://doi.org/10.1109/ICRA48891.2023.10160871)]
- **CenterCoop**  
  Zhou, Linyi, Gan, Zhongxue, Fan, Jiayuan  
  *IEEE Robotics and Automation Letters*, 2024  
  [[DOI](https://doi.org/10.1109/LRA.2023.3339399)]
- **CoFF**  
  Guo, Jingda et al.  
  *IEEE Internet of Things Journal*, 2021  
  [[DOI](https://doi.org/10.1109/JIOT.2021.3053184)]
- **Collaboration Helps Camera Overtake LiDAR**  
  Hu, Yue et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/CVPR52729.2023.00892)]
- **Collaborative 3D Object Detection**  
  Wang, J., Zeng, Y., Gong, Y.  
  *IEEE Transactions on Intelligent Transportation Systems*, 2023  
  [[DOI](https://doi.org/10.1109/TITS.2023.3272027)]
- **Collective PV-RCNN**  
  Teufel, Sven, Gamerdinger, J{\"o  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ITSC57777.2023.10422079)]
- **Complementarity-Enhanced**  
  Luo, Guiyang et al.  
  *Proceedings of the 30th ACM International Conference*, 2022  
  [[DOI](https://doi.org/10.1145/3503161.3548197)]
- **Cooperative LIDAR Object Detection**  
  Marvasti, Ehsan Emad et al.  
  *2020 IEEE*, 2020  
  [[DOI](https://doi.org/10.1109/VTC2020-Fall49728.2020.9348723)]
- **Cooperative Perception With Learning-Based V2V Communications**  
  Liu, Chenguang et al.  
  *IEEE Wireless Communications Letters*, 2023  
  [[DOI](https://doi.org/10.1109/LWC.2023.3295612)]
- **A Cooperative Perception System Robust**  
  Song, Zhiying et al.  
  *2023 IEEE Intelligent Vehicles Symposium*, 2023  
  [[DOI](https://doi.org/10.1109/IV55152.2023.10186727)]
- **Core: Cooperative Reconstruction**  
  Wang, Binglu et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00800)]
- **Latency-Aware Collaborative Perception**  
  Lei, Zixing et al.  
  *Computer Vision - ECCV*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-19824-3\\\\_19)]
- **DI-V2X**  
  Xiang, Li et al.  
  *N/A*, 2023
- **DUSA**  
  Kong, Xianghao et al.  
  *Proceedings of the 31st ACM International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3581783.3611948)]
- **Distributed Dynamic Map Fusion**  
  Zhang, Zijian et al.  
  *2021 IEEE International Conference*, 2021  
  [[DOI](https://doi.org/10.1109/ICRA48506.2021.9561612)]
- **Dynamic Feature Sharing**  
  Bai, Zhengwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ITSC57777.2023.10422242)]
- **EMIFF**  
  Wang, Zhe et al.  
  *N/A*, 2024
- **EdgeCooper**  
  Luo, Guiyang et al.  
  *IEEE Journal on Selected Areas in Communications*, 2024  
  [[DOI](https://doi.org/10.1109/JSAC.2023.3322764)]
- **Environment-Aware Optimization**  
  Volk, Georg et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/ITSC55140.2022.9922388)]
- **An Extensible Framework**  
  Lu, Yifan et al.  
  *N/A*, 2024
- **F-Transformer**  
  Wang, Jie et al.  
  *Artificial Neural Networks*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-15919-0\_15)]
- **Fast Clustering**  
  Kuang, Xinkai et al.  
  *Cognitive Computation*, 2024  
  [[DOI](https://doi.org/10.1007/s12559-023-10211-x)]
- **F-Cooper: Feature Based Cooperative Perception for Autonomous Vehicle Edge Computing System Using 3D**  
  Chen, Qi et al.  
  *Proceedings of the 4th ACM*, 2019  
  [[DOI](https://doi.org/10.1145/3318216.3363300)]
- **FeaCo**  
  Gu, Jiaming et al.  
  *Proceedings of the 31st ACM International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3581783.3611880)]
- **Flow-Based Feature Fusion**  
  Yu, Haibao et al.  
  *N/A*, 2023
- **Generating Evidential BEV Maps**  
  Yuan, Yunshuang et al.  
  *ISPRS Journal of Photogrammetry and Remote Sensing*, 2023  
  [[DOI](https://doi.org/10.1016/j.isprsjprs.2023.08.013)]
- **HM-ViT**  
  Xiang, Hao, Xu, Runsheng, Ma, Jiaqi  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00033)]
- **HP3D-V2V**  
  Chen, Hongmei et al.  
  *Sensors*, 2024  
  [[DOI](https://doi.org/10.3390/s24072170)]
- **HPL-ViT**  
  Liu, Yuhang et al.  
  *N/A*, 2023
- **HYDRO-3D**  
  Meng, Zonglin et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2023  
  [[DOI](https://doi.org/10.1109/TIV.2023.3282567)]
- **How2comm: Communication-Efficient**  
  Yang, Dingkang et al.  
  *N/A*, N/A
- **Interruption-Aware Cooperative Perception**  
  Ren, Shunli et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2024.3371974)]
- **A Joint Perception Scheme For Connected Vehicles**  
  Ahmed, Ahmed N. et al.  
  *2022 IEEE Sensors*, 2022  
  [[DOI](https://doi.org/10.1109/SENSORS52175.2022.9967271)]
- **Keypoints-Based Deep Feature Fusion**  
  Yuan, Yunshuang, Cheng, Hao, Sester, Monika  
  *IEEE Robotics and Automation Letters*, 2022  
  [[DOI](https://doi.org/10.1109/LRA.2022.3143299)]
- **Learning to Communicate**  
  Vadivelu, Nicholas et al.  
  *Proceedings of the 2020 Conference*, 2021
- **Learning Distilled Collaboration Graph**  
  Li, Yiming et al.  
  *Advances in Neural Information Processing Systems*, 2021
- **Learning for Vehicle-to-Vehicle Cooperative Perception Under Lossy Communication**  
  Li, Jinlong et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2023  
  [[DOI](https://doi.org/10.1109/TIV.2023.3260040)]
- **MACP**  
  Ma, Yunsheng et al.  
  *2024 IEEE*, 2024  
  [[DOI](https://doi.org/10.1109/WACV57701.2024.00334)]
- **MCoT**  
  Shi, Shanwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICPADS60453.2023.00226)]
- **MKD-Cooper**  
  Li, Zhiyuan et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2023.3310580)]
- **MoRFF**  
  Mao, Ruiqing et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/VTC2023-Fall60731.2023.10333428)]
- **Model-Agnostic Multi-Agent Perception Framework**  
  Xu, Runsheng et al.  
  *2023 IEEE International Conference*, 2023  
  [[DOI](https://doi.org/10.1109/ICRA48891.2023.10161460)]
- **Multi-Modal Virtual-Real Fusion**  
  Zhang, Hui et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/PAAP56126.2022.10010640)]
- **Multi-Robot Scene Completion**  
  Li, Yiming et al.  
  *N/A*, N/A
- **Multimodal Cooperative 3D Object Detection Over Connected Vehicles**  
  Chi, Fangyuan et al.  
  *IEEE Network*, 2023  
  [[DOI](https://doi.org/10.1109/MNET.010.2300029)]
- **Multistage Fusion Approach**  
  Yu, Hang et al.  
  *2022 5th World Conference*, 2022  
  [[DOI](https://doi.org/10.1109/WCMEIM56910.2022.10021459)]
- **PAFNet**  
  Wang, Luyang, Lan, Jinhui, Li, Min  
  *Symmetry*, 2024  
  [[DOI](https://doi.org/10.3390/sym16040401)]
- **Pillar Attention Encoder**  
  Bai, Zhengwei et al.  
  *IEEE Internet of Things Journal*, 2024  
  [[DOI](https://doi.org/10.1109/JIOT.2024.3390552)]
- **Pillar-Based Cooperative Perception**  
  Wang, Jian et al.  
  *Wireless Communications and Mobile Computing*, 2022  
  [[DOI](https://doi.org/10.1155/2022/3646272)]
- **PillarGrid**  
  Bai, Zhengwei et al.  
  *2022 IEEE*, 2022  
  [[DOI](https://doi.org/10.1109/ITSC55140.2022.9921947)]
- **Practical Collaborative Perception**  
  Dao, Minh-Quan, Berrio, Julie Stephany, Fr{\'e  
  *IEEE Transactions on Intelligent Transportation Systems*, 2024  
  [[DOI](https://doi.org/10.1109/TITS.2024.3371177)]
- **QUEST**  
  Fan, Siqi et al.  
  *N/A*, 2023
- **Region-Based Hybrid Collaborative Perception**  
  Liu, Pengfei et al.  
  *IEEE Transactions on Vehicular Technology*, 2024  
  [[DOI](https://doi.org/10.1109/TVT.2023.3324439)]
- **Robust Collaborative 3D Object Detection**  
  Lu, Yifan et al.  
  *2023 IEEE International Conference*, 2023  
  [[DOI](https://doi.org/10.1109/ICRA48891.2023.10160546)]
- **Robust Collaborative Perception**  
  Ren, Shunli et al.  
  *N/A*, N/A
- **Robust Collaborative Perception**  
  Lei, Zixing et al.  
  *N/A*, 2024 [[arXiv](https://arxiv.org/abs/2405.02965)]
- **Robust Real-time Multi-vehicle Collaboration**  
  Zhang, Qingzhao et al.  
  *Proceedings of the 29th Annual International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3570361.3613271)]
- **S2R-ViT**  
  Li, Jinlong et al.  
  *N/A*, 2024
- **Select2Col**  
  Liu, Yuntao et al.  
  *N/A*, 2024
- **Self-Supervised Adaptive Weighting**  
  Liu, Chenguang et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2023.3345035)]
- **Semantic Communication for Cooperative Perception Based on Importance Map**  
  Sheng, Yucheng et al.  
  *Journal of the Franklin Institute*, 2024  
  [[DOI](https://doi.org/10.1016/j.jfranklin.2024.106739)]
- **Slim-FCP**  
  Guo, Jingda et al.  
  *IEEE Internet of Things Journal*, 2022  
  [[DOI](https://doi.org/10.1109/JIOT.2022.3153260)]
- **Soft Actor**  
  Xie, Qi et al.  
  *IEEE Internet of Things Journal*, 2022  
  [[DOI](https://doi.org/10.1109/JIOT.2022.3179739)]
- **Spatio-Temporal Domain Awareness**  
  Yang, Kun et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.02137)]
- **UMC**  
  Wang, Tianhang et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00752)]
- **Among Us**  
  Li, Yiming et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/ICCV51070.2023.00024)]
- **V2VFormer**  
  Yin, Hongbo et al.  
  *IEEE Transactions on Intelligent Transportation Systems*, 2024  
  [[DOI](https://doi.org/10.1109/TITS.2023.3314919)]
- **V2VFormer**  
  Lin, Chunmian et al.  
  *IEEE Transactions on Intelligent Vehicles*, 2024  
  [[DOI](https://doi.org/10.1109/TIV.2024.3353254)]
- **V2VFusion**  
  Zhang, Lei et al.  
  *2023 China Automation Congress*, 2023  
  [[DOI](https://doi.org/10.1109/CAC59555.2023.10450676)]
- **V2VNet**  
  Wang, Tsun-Hsuan et al.  
  *Computer Vision*, 2020  
  [[DOI](https://doi.org/10.1007/978-3-030-58536-5\_36)]
- **V2X-ViT**  
  Xu, Runsheng et al.  
  *Computer Vision*, 2022  
  [[DOI](https://doi.org/10.1007/978-3-031-19842-7\_7)]
- **VINet**  
  Bai, Zhengwei et al.  
  *Mechanical Systems and Signal Processing*, 2023  
  [[DOI](https://doi.org/10.1016/j.ymssp.2023.110723)]
- **Vehicle-Infrastructure Cooperative 3D Object Detection**  
  Yu, Haibao et al.  
  *N/A*, 2023
- **ViT-FuseNet**  
  Zhou, Yang et al.  
  *IEEE access : practical innovations, open solutions*, 2024  
  [[DOI](https://doi.org/10.1109/ACCESS.2024.3368404)]
- **What2comm: Towards Communication-efficient Collaborative Perception**  
  Yang, Kun et al.  
  *Proceedings of the 31st ACM International Conference*, 2023  
  [[DOI](https://doi.org/10.1145/3581783.3611699)]
- **Where2comm: Communication-Efficient Collaborative Perception**  
  Hu, Yue et al.  
  *N/A*, 2022

### Object Tracking

**3 papers**

- **3D Multi-Object Tracking**  
  Su, Hao, Arakawa, Shin'Ichi, Murata, Masayuki  
  *2023 IEEE Intelligent Vehicles Symposium*, 2023  
  [[DOI](https://doi.org/10.1109/IV55152.2023.10186777)]
- **Collaborative Multi-Object Tracking With Conformal Uncertainty Propagation**  
  Su, Sanbao et al.  
  *IEEE Robotics and Automation Letters*, 2024  
  [[DOI](https://doi.org/10.1109/LRA.2024.3364450)]
- **Probabilistic 3D Multi-Object Cooperative Tracking**  
  Chiu, Hsu-kuang et al.  
  *N/A*, 2024

### Semantic Segmentation

**5 papers**

- **CoBEVT**  
  Xu, Runsheng et al.  
  *Proceedings of The*, 2023
- **Collaborative Semantic Occupancy Prediction**  
  Song, Rui et al.  
  *N/A*, 2024
- **A LiDAR Semantic Segmentation Framework**  
  Liu, Hongwei et al.  
  *2023 IEEE*, 2023  
  [[DOI](https://doi.org/10.1109/VTC2023-Fall60731.2023.10333790)]
- **Multi-Robot Scene Completion**  
  Li, Yiming et al.  
  *N/A*, N/A
- **Overcoming Obstructions**  
  Glaser, Nathaniel et al.  
  *2021 IEEE*, 2021  
  [[DOI](https://doi.org/10.1109/IROS51168.2021.9636761)]

### Motion Prediction & Lane Detection

**3 papers**

- **CoLD Fusion**  
  Gamerdinger, J{\"o  
  *2023 IEEE Intelligent Vehicles Symposium*, 2023  
  [[DOI](https://doi.org/10.1109/IV55152.2023.10186632)]
- **Cooperative Road Geometry Estimation**  
  Sakr, Ahmed Hamdi  
  *2020 IEEE*, 2020  
  [[DOI](https://doi.org/10.1109/CAVS51000.2020.9334579)]
- **Enhancing Lane Detection with a Lightweight Collaborative Late Fusion Model**  
  Jahn, Lennart Lorenz Freimuth et al.  
  *Robotics and Autonomous Systems*, 2024  
  [[DOI](https://doi.org/10.1016/j.robot.2024.104680)]

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

**Maintained by**: [Your Name]
**Last Updated**: 2026-01
**Paper Version**: Accepted for IEEE T-ITS 2026
