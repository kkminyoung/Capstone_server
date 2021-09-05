# Capstone_flask
### Abnormal detection 활용한 자동편집 블랙박스 어플리케이션
<img src="https://user-images.githubusercontent.com/61506233/100989312-15140e80-3594-11eb-956e-30632ad1a4c9.png" width="20%"> 

## 프로젝트 소개
### 개발 배경
도로의 CCTV 역할을 하는 블랙박스는 현대사회에서 각종 사고 및 범죄 발생시 필수적인 증거 자료 활용되고있다. 
하지만 촬영한 블랙박스 영상은 대용량 파일이기에 저장/보관/관리하는데에 어려움이 존재한다. 실제로, 블랙박스 영상에서 원하는 부분을 가져오려면 전체영상을 일일이 돌려봐야하는 시간적/자원적 비효율성이 존재했다. 기존의 블랙박스는 센서를 이용하여 본인 차량에 충격이 탐지되었을 때에만 따로 저장할 수 있기 때문에, 본인 차량의 충격 감지상황 이외에 발생할 수 있는 사고 및 범죄에 대한 영상증거물을 확보하기 어렵다. 

### 개발 내용
따라서 본 프로젝트에서는 비정상적인 상황을 탐지하고 이 부분만 따로 저장할 수 있도록 하는 기능을 제공하여 블랙박스 영상관리를 효율적으로 할 수 있도록 돕는다.

자동편집 상황 예시)
폭력, 납치, 기물파손, 배회, 폭행, 싸움, 절도, 실신, 침입, 투기, 강도, 납치, 주취행동 등 


### 기능
#### 1) 블랙박스 촬영 & 업로드
![image](https://user-images.githubusercontent.com/61506233/132123455-bb46236a-b393-40f9-9881-8d2ac2c8fcca.png)
- 스마트폰 카메라를 이용하여 영상을 촬영
- 시간, 주소 정보를 화면에 표시 

#### 2) 동영상 편집
![image](https://user-images.githubusercontent.com/61506233/132123349-c864cc8a-7b5f-4b57-9cb3-4dd3455a4cca.png)
- 저장된 영상을 불러와서 편집해주는 서비스 제공
- 동영상 편집
   - 2-1) 충격 탐지 시 저장
     - 본인 차량의 충격 탐지 시 영상 저장
   - 2-2) abnormal event detection 탐지 시 저장
     - 비정상적인 상황에 대한 영상 저장

### 기술설명
#### 1. 충격탐지 
- 기존기술 사용(안드로이드 API)
#### 2. Abnormal Event 탐지
- 딥러닝 사용(Vision)

### System Overview
![image](https://user-images.githubusercontent.com/61506233/100989472-41c82600-3594-11eb-9ce9-3675edf1dbdb.png)


![image](https://user-images.githubusercontent.com/61506233/132123502-ec94e2a5-3636-48ba-bf0a-63a9d78a3b4b.png)


## 시연영상
[![매직박스 시연영상](https://img.youtube.com/vi/Kn-Pr8kC0nc/0.jpg)](https://www.youtube.com/watch?v=Kn-Pr8kC0nc&feature=youtu.be)

![temp](https://user-images.githubusercontent.com/61506233/118226604-3f161900-b4c2-11eb-86bd-c919d5af8b86.gif)


## Reference
- [1] Yao, Y., Xu, M., Wang, Y., Crandall, D.J., Atkins, "Unsupervised traffic accident detection in first-person videos", in IROS, 2019  
- [2] W. Sultani, C. Chen, and M. Shah, "Real-World Anomaly Detection in Surveillance Videos", in CVPR, 2018
- [3] K. He, G. Gkioxari, P. Dollar, and R. Girshick, “Mask R-CNN,” in ICCV, 2017 
- [4] N. Wojke, A. Bewley, and D. Paulus, “Simple online and realtime tracking with a deep association metric,” in ICIP, 2017 
- [5] E. Ilg, N. Mayer, T. Saikia, M. Keuper, A. Dosovitskiy, and T. Brox, “Flownet 2.0: Evolution of optical flow estimation with deep networks,” in CVPR, 2017. 
- [6] R. Mur-Artal and J. D. Tardos, “Orb-slam2: An open-source slam ´ system for monocular, stereo, and rgb-d cameras,” T-RO, 2017. 


## License
Code is under the [Apache Licence v2](https://github.com/kkminyoung/Capstone_model/blob/master/LICENSE)

# 프로젝트 레파지토리 정리
- 안드로이드 repository : https://github.com/kkminyoung/Capstone_android
- 딥러닝 & 서버 repository : https://github.com/Kim-Ha-Jeong/Capstone_server

