# Face_Mix

* 2020년 9월 10일 ~ 2020년 9월 22

## 프로젝트의 목적

* **연예인의 얼굴과 매칭하여 성형 추천**
* **나와 가장 닮은 연예인과 가능성 있는 조합**
* **연예인과 호감형으로 합성**
* **내가 원하는 연예인과 합성**

## 주요 기능

* **성별 선택 후 사진 업로드**

![index_page_2](/img/index_page_2.PNG)

* **나와 닮은 상위 3명의 연예인을 알려준다**
1. **닮은 사람중 한명과 Mix**
2. **닮은 사람 모두와 Mix**
3. **닮은 사람이 아닌 선택해서 Mix**

![who_page](/img/who_page.PNG)

1. **선택한 연예인과 Face를 Mix 해서 보여준다**

![mix_page](/img/mix_page.PNG)

2. **상위 3명의 연예인 모두와 합성을 해서 보여준다**

![mix_all_page](/img/mix_all_page.PNG)

3. **상위 3명이 아닌 다른 연예인을 선택해서 합성할 수 있다**

![photo_list_page](/img/photo_list_page.PNG)

* **상위 3명이 아닌 다른 연예인을 선택해서 합성**

![mix_page_2](/img/mix_page_2.PNG)

# 일정 

1. 2020년 9월 10일 : 프로젝트 기획안 작성
2. 2020년 9월 10일 ~ 9월 15일 : 데이터 수집 및 전처리
3. 2020년 9월 10일 ~ 9월 14일 : 모델링 탐색
4. 2020년 9월 14일 ~ 9월 16일 : OPENCV를 활용한 이미지 합성
5. 2020년 9월 15일 ~ 9월 16일 : Django를 이용해 웹 서비스 제작
6. 2020년 9월 17일 ~ 9월 18일 : CSS를 활용한 Servicepage 적용
7. 2020년 9월 21일 : 최종 merge
8. 2020년 9월 22일 : 발표 자료 및 동영상 시연

# 데이터 수집

* 주연급 배우나 아이돌 센터 위주로 자료 수집
* 높은 성능을 얻기 위해 정면과 얼굴 위주로 나온 사진 수집

# 개발환경

* Django

# 사용기술

## 닮은 연예인 찾기

* Face Recognition 라이브러리의 CNN 모델 사용 해서 얼굴인식
* INPUT 이미지의 얼굴 인코딩 값과 기존 배우 데이터의 얼굴 인코딩 값을 유클리드 거리 측정을 통해 유사도 체크

## Face Mix

* 사전 작업으로 두 사진의 face를 추출하고 크기를 같게 만든다
* Dlib를 사용하여 두 사진에서 68개의 landmark 추출
* 배경을 추가하기 위해서 이미지 width, height의 시작점과 끝점 중간점, 8개의 landmark 를 추가하여 총 76개의 landmark를 사용
* Delaunay Triangulation
  * 각 랜드마크를 index를 기준으로 Delaunay Triangulation이 수행된 총 142개의 삼각형 데이터를 미리 저장해서 사용
* Warping images and alpha blending
  * 두 이미지의 landmark를 매칭
  * Delaunay Triangulation로 만들어진 삼각형의 corner에 두 이미지의 landmark들의 아핀 변환을 계산해서 매칭
  * fillConvexPoly을 사용해서 triangular mask를 만들고 warpAffine Function을 사용해서 두 삼각형을 morph
  * BORDER_REFLECT_101을 사용해서 이음새 부분을 자연스럽게 연결
  * alpha blending을 수행

[참고 사이트](https://www.learnopencv.com/face-morph-using-opencv-cpp-python/)

## CSS

* flex
* Bootstrap
* Zipcy님 그림
