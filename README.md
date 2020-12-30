<h1 align="center">📐특정 위치 도달 확인 프로그램📏</h1>

특정 도달 영역을 왔다갔다 했는지 확인하는 프로그램으로 공 혹은 어떤 물체가 이 영역을 왔다 갔다 했는지 확인하기 위한 프로젝트.

배구공이 특정 높이를 넘었는지 바로 판단할 수 있는 프로그램 목적

## 판단 방법

색공간을 기준으로 Hue(색상), Saturation(채도), Value(진하기)로 특정 색을 결정하여 특성 색의 위치가 해당 부분을 넘었는지 확인.

<h3 align="center">프로그램</h3>
<p align="center">
<img alt="Back_and_forth_count_system" src="https://github.com/cwadven/Back_and_forth_count_system/blob/master/assets/seq1.PNG"/>
</p>

## 사용 방법

<h3 align="center">Tracking을 조작 하여 색깔 분류 시키기</h3>
<p align="center">
<img alt="Back_and_forth_count_system" src="https://github.com/cwadven/Back_and_forth_count_system/blob/master/assets/seq2.PNG"/>
</p>

~~~
Tracking 스크롤 바를 이용하여 원하는 색상을 추출한다.
~~~

<h3 align="center">특정색 추출</h3>
<p align="center">
<img alt="Back_and_forth_count_system" src="https://github.com/cwadven/Back_and_forth_count_system/blob/master/assets/seq2.PNG"/>
</p>

~~~
특정색만 나오도록 잘 조정한다.
조정한 값은 어디에 기록한다.

기록한 값을 가지고 volleyball.py 소스코드 58, 59번째 줄 위치에 기록한 값의 숫자를 넣어준다.

(예제)
l_b = np.array([57, 46, 158]) #범위를 결정하기 위해서
u_b = np.array([81, 211, 255]) #범위를 결정하기 위해서
~~~

<h3 align="center">왔다-갔다하는 장면</h3>
<p align="center">
<img alt="volley_ball" src="https://github.com/cwadven/volley_ball/blob/master/assets/seq4.PNG"/>
</p>

~~~
지금 개발자는 중앙을 기준으로 영역을 설정했고, 저기 중앙을 한번 왔다-갔다 하면 0이라는 숫자가 +1 씩 된다.
~~~

## 개발자

**👤 이창우**

- Github : https://github.com/cwadven
- 기술스택 : Opencv
- 개발기간 : <br>
    - 2020 2020년 6월 4일 ~ 2020년 6월 10일

## 환경 구축

~~~
[python 실행 구축 방법]
1. python -m venv myvenv (가상환경 생성)
2. python source myvenv/Script/activates (가상환경 실행)
3. pip install -r requirements.txt (의존성 모듈 설치)
4. python volleyball.py
~~~