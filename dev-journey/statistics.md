# Statistics

<br>
<br>

# 데이터

## 질적 변수 vs 양적 변수

### 질적 변수
> 1. 매우 좋음　　2. 좋음　　3. 보통　　4. 나쁨　　5. 매우 나쁨  
> A형　　B형　　O형　　AB형  

흡연여부, 남성과 여성 같이 값이 2개인 질적 변수는 __2진변수__ 라고 한다. True or False라서 1과 0으로 표현 가능하지만, 질적변수다.

#### __명의 척도__ = __명목 척도__
명의 척도의 목적은 구별하는 것으로, 학생번호나 전화번호, 성별 등이 있다.

#### __순서 척도__ = __서열 척도__
순서 관계나 __대소 관계__ 에 대한 의미만 있을 때. 성적 순위나 설문조사 만족도 등이 있다.  
8등과 4등의 차이가 8등과 12등과의 차이와 같다고 말하기 힘들고, 4등이 8등의 두배라고 하기 힘든 상황의 변수를 말함.

### 양적 변수
> 시험점수, 키

#### __간격 척도__ = __등간 척도__
간격 척도는 대소 관계와 함께 그 __차이__ 에도 의미를 두는 변수. 연도나 온도 등이 있다.  
60도는 30도보다 높은 온도이므로 대소 관계에 의미가 있고 그 차이도 의미가 있다.  
하지만 60도는 30도보다 2배 높은 온도라고 말할 수 없기에 간격 척도다.

#### __비례 척도__ = __비율 척도__
비례 척도는 __대소 관계, 차이, 비__ 모두 의미가 있는 변수. 길이, 무게 등이 있다.  
50cm와 100cm는 2배 차이라고 말할 수 있다.

- 간격 척도와 비례 척도 구분 Tip
    - 0이 없음을 뜻하는지 확인하면 된다.

<br>

## 이산형 변수 vs 연속형 변수
### 이산형 변수
0, 1, 2, 3, ... 같이 하나하나의 값을 취하는 변수.
### 연속형 변수
연속적인 값을 취하기에 두 숫자 사이에도 반드시 숫가가 있음. 계속 쪼개짐.

<br>
<br>
<br>

# 1차원 데이터
```
# 데이터 가져오기
df = pd.read_csv("etc/ch2_scores_em.csv", index_col="student number")
scores = np.array(df["english"])[:10]
scores_df = pd.DataFrame({"score":scores}, index=pd.Index(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]), name = "studnet")
```
<br>

## 대표값
### 평균값 mean
다 아는 일반적인 평균. 시그마나 엑스바로 표현.
```
np.mean(scores)
score_df.mean()
```


### 중앙값 median
데이터를 크기 순으로 나열했을 때, 정중앙에 위치하는 값을 중앙값이라고 한다.  
중앙값은 평균값에 비해 이상값에 강하다.  
[1, 2, 3, 4, 5, 6, 1000]이 있을 때, 아주 큰 이상값 하나 때문에 평균값은 150이 되는데 이럴 때, 중앙값 4를 쓰는게 바람직할 수 있다.  
데이터가 짝수개일 때는 중앙에 있는 값 두개의 평균값을 중앙값으로 본다.
```
np.median(scores)
scores_df.median()
```


### 최빈값 mode
데이터에서 가장 많이 등장한 값.  
최빈값은 기본적으로 질적 데이터의 대푯값을 구할 때 사용하는 지표다. 시험점수같은 양적 데이터에서 최빈값을 구하는 것은 무의미해지기 쉽상이다.
```
pd.Series([1, 1, 1, 2, 2, 3]).mode()
```
<br>

## 산포도
### 분산 variance
__편차 deviation__ 은 각 데이터가 평균으로부터 얼마나 떨어져 있는 지를 보여준다. 이 때, 떨어진 정도는 음수와 양수 모두 가능하다.  
하지만 편차의 대푯값으로 평균을 선택하면 편차 평균 즉, 모든 편차의 합은 0이 된다.  
그래서 서로 다른 데이터더라도 평균만 같으면 두 데이터를 구분하고 분석할 수 없는 상황을 초래한다.<br>  
그 결과 평균에서 각각 10의 거리만큼 떨어진 +10인 값과 -10인 값을 동일한 산포도를 갖고 있다고 취급하자는 발상에서 __편차의 제곱 즉, 분산__ 을 정의하게 된다.
```
np.var(scores)
scores_df.var(ddof=0)
# Numpy는 표본분산이 default인 반면, Pandas는 불편분산이 default라 ddof라는 매개변수를 통해 표본분산으로 바꿨다.
```
분산은 $S^2$ 이라고 표기한다.  
분산을 면적의 평균이라고 보기도 한다. 한 변의 길이가 편차인 정사각형과 같기 때문.


### 표준편차 standard deviation
분산은 편차보다 산포도를 잘 보여주는것 같지만 제곱되면서 단위가 단위$^2$이 됐다. 때문에 한 눈에 파악하기 힘든 단위로 생기는 문제를 해결하고자 분산에 제곱근을 취한 __표준편차__ 를 정의하게 된다.
```
np.std(scores, ddof=0)
```
표준편차는 원래의 데이터와 동일한 단위를 쓰므로, 동일한차원으로 그릴 수 있다.
이 때, 평균 ± 표준편차구간을 1 시그마 구간, 평균 ±2 표준편차구간을 2 시그마 구간, 평균 ±3 표준편차구간을 3 시그마 구간이라고 한다. 이때, 각 구간은 정규분포의 약 68.27%, 95.45%, 99.73% 범위를 포함한다.

### 범위 range
범위는 데이터 전체를 보지 않고 최댓값과 최솟값만으로 산포도를 표현한다.  
간단히 계산 가능하지만 이상값에 약하다.
```
np.max(scores) - np.min(scores)
```

### 사분위 범위 IQR, interquartile range
범위가 이상값에 약하다는 단점을 커버하기 위해 상위수%와 하위수%를 이용한다.  
데이터의 하위 25%, 50%, 75%에 위치하는 값을 보고 이를 각각 제1사분위수, 제2사분위수, 제3분위수라고 하며 Q1, Q2, Q3라고도 표현한다. 그리고 Q3 - Q1을 __사분위 범위, IQR__ 이라고 한다.
```
scores_Q1 = np.percentile(scores, 25)
scores_Q3 = np.percentile(scores, 75)
scores_IQR = scores_Q3 - scores_Q1
```
#### 분산은 평균에 대해 정의되는 산포도인 반면, IQR은 중앙값에 대해 정의되는 산포도의 지표라고 해석할 수 있다.
<br>

## 데이터 정규화 normalization
똑같은 60점이라도, 평균이 30점인 시험에서 60점을 받은 것과 평균이 90점인 시험에서 60점을 받은 것은 상대적인 결과가 다르다. 점수라는 지표는 그 시험의 평균이나 분산에 따라 평가가 달라진다. 그러므로 평균이나 분산에 의존하지 않고도 데이터의 상대적인 위치관계를 알 수 있다면 편리할거다.  
이 처럼 데이터를 통일된 지표로 변환하는 것을 __정규화__ 라고 한다.  
### 표준화 standardization
데이터에서 평균을 빼고 표준편차로 나누는 작업을 __표준화__ 라고 한다.  
표준화된 데이터는 표준화 변량 standardized data 혹은 Z 점수 z-score 라고 한다.
```
z = (scores - np.mean(scores)) / np.std(scores)
np.mean(z)              # 0  표준화된 데이터의 평균은 0
np.std(z, ddof=0)       # 1  표준화된 데이터의 표준편차는 1
```
원본 데이터와 동일한 단위를 쓰는 표준편차로 나눴기 때문에, 표준화된 데이터엔 단위가 없다.

### 편찻값
편찻값은 평균이 50, 표준편차가 10이 되도록 정규화한 값이다.  
```
z = 50 + 10 * (scores - np.mean(scores)) / np.std(scores)
```
<br>

## 1차원 데이터 시각화
```
english_scores = np.array(df["english"])   # 50명 영어점수 다 가져오기.
```

### 도수분포표 frequency distribution
분할된 구간에 데이터 개수를 표로 표현한 것.  
시험 점수를 0-10점, 10-20점, ... 구간으로 나눠서 도수분포표를 만든다면, 0~10점이라는 구간을 __계급 class__ 라고 하고, 각 계급에 속한 학생 수를 __도수 frequency__ 라고 하고, 각 구간의 폭을 __계급폭__ 이라 하고, 계급의 개수를 __계급수__ 라고 한다.
```
# bins로 계급수를. range로 최솟값과 최댓값을 지정.
freq, _ = np.histogram(english_scores, bins=10, range=(0, 100))
```
도수분포표를 이용하면 양적데이터도 최빈값을 구할 수 있다.    <br>  
__계급값__ : 각 계급을 대표하는값. 계급의 중간값을 이용.　　ex) 70~80의 계급값은 75.  
```
class_value = [(i+(i+10))//2 for i in range(0, 100, 10)]
```
__상대도수__ : 전체 데이터에서 해당 계급의 데이터가 갖는 비율.  
```
rel_freq = freq / freq.sum()
```
__누적상대도수__ : 상대도수의 누적합.
```
cum_rel_freq = np.cumsum(rel_freq)
```


### 히스토그램 histogram
히스토그램은 도수분포표를 막대그래프로 만든 것.
```
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
freq, _, _ = ax.hist(english_scores, bins=10, range=(0, 100))
ax.set_xlabel("score")
ax.set_ylabel("person number")
ax.set_xticks(np.linspace(0, 100, 10+1))
ax.set_ytics(np.arange(0, freq.max()+1))
plt.show()
```
계급폭을 10으로 했지만, 계급폭을 4로하고 계급수를 25로 하면 더욱 세부적으로 볼 수 있다.  
__도수분포표와 히스토그램은 계급수에 따라 모양이 크게 변하기 때문에, 데이터에 따라 적절한 값으로 설정하는 것이 매우 중요하다.__  
누적상대도수의 꺾은선 그래프와 함께 볼 수도 있다.
```
```

### 상자그림 box plot
상자그림은 데이터의 분포와 이상값을 시각적으로 파악하기 쉽다.  
분위수 범위의 Q1, Q2, Q3, IQR을 사용해 표현한다. 상자는 Q1부터 Q3를 의미하고 상자안의 가로선은 Q2다. 수염은 각각 Q1, Q3로부터 1.5 IQR만큼 떨어진 범위를 나타낸다. 그리고 이 전체 구간에 포함되지 못 한 데이터는 이상값으로 취급하고 점으로 표시한다.
```
fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
ax.boxplot(english_scores, labels=["english"])
plt.show()
```

<br>
<br>
<br>

# 2차원 데이터
이젠 두 개의 데이터가 대응되는 자료를 다뤄보자. 영어와 수학점수를 가져온다.
```
df = pd.read_csv("../data/ch2_scores_em.csv", index="student number")
en_scores, ma_scores = np.array(df["english"])[:10], np.array(df["mathematics"])[:10]
scores_df = pd.DataFrame({english: en_scores, mathematics: ma_scores}, index=pd.Index(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], name="student"))
```

## 두 데이터의 상관관계 지표
상관관계에는 __양의 상관관계, 음의 상관관계, 무상관__ 이 있다.  

### 공분산 covariance
공분산은 분산에 가까운 지표다.  
x축 데이터의 평균과 y축 데이터의 평균으로부터 각 데이터들이 떨어진 거리, 즉, x축 편차와 y축 편차의 곱으로 이뤄진 지표다. 때문에 1, 3사분면의 데이터는 양수가 나오지만 2, 4분면의 데이터는 음수가 나온다. 이 덕에 __±부호가 붙은 면적이 탄생하고 이 면적들의 평균을 상관관계의 지표로 만든게 공분산__ 이다.  
공분산이 양수면 양의값이 되는 데이터가 많은 양의 산관관계가 되고, 음수면 음의 상관관계, __공분산이 0에 가까우면 무상관__ 이 된다.  
공분산은 $Sxy$ 로 표기한다.
```
summary_df = scores_df.copy()
summary_df["english_deviation"] = summary_df["english"] - summary_df["english"].mean()
summary_df["mathematics_deviation"] = summary_df["mathematics"] - summary_df["mathematics"].mean()
summary_df["product_of_deviations"] = summary_df["english_deviation"] * summary_df["mathematics"]
summary_df["product_of_deviations"].mean()

cov_numpy = np.cov(en_scores, ma_scores, ddof=0)
cov_numpy[0,1], cov_numpy[1,0]
```
numpy의 cov()메소드는 공분산 행렬 또는 분산공분산행렬이라고 불리는 값으로 리턴한다.  
[0,1]과 [1,0]의 값이 우리가 얻고자 하는 영어와 수학의 공분산이고, [0,0]은 영어와 영어의 공분산, [1,1]은 수학과 수학의 공분산이다. 같은 데이터를 공분산했기에 각 데이터의 분산과 같다.

### 상관계수 correlation coefficient
앞선 공분산에선 영어점수와 수학점수의 상관관계를 봤기 때문에 단위가 점수$^2$이다. 하지만 키와 점수의 상관관계를 본다면 단위가 cm x 점수가 된다.  
따라서 단위에 의존하지 않고 상관관계를 보여줄 지표를 만들기 위해 공분산을 각 데이터의 표준편차로 나누고 이를 __상관계수__ 라고 정의하게 된다.  
상관계수는 $r$ $_x$ $_y$ 라고 표기한다.  
상관계수는 반드시 -1 ~ 1 사이의 값을 취하고, 데이터가 양의 상관관계에 놓여 있을수록 1에 가까워지고, 음의 상관관계면 -1에 가까워지며, 무상관이면 0에 가까워진다.
```
np.cov(en_scores, ma_scores, ddof=0)[0,1] / (np.std(en_scores) * np.std(ma_scores))

np.corrcoef(en_scores, ma_scores)

scores_df.corr()
```
앞선 공분산과 마찬가지로 np.corrcoef()랑 scores_df.corr() 메소드는 상관행렬로 리턴된다.

## 2차원 데이터 시각화

### 산점도 scatter
```
english_scores = np.array(df["english"]); math_scores = np.array(df["mathematics])
fig = plt.figure(figsize=(8,8)); ax = fig.add_subplot(111)
# 산점도
ax.scatter(english_scores, math_scores)
ax.set_xlabel("english"); ax.set_ylabel("math")
plt.show()
```

### 회귀직선 regression line
회귀직선은 두 데이터 사이의 관계를 더욱 잘 나타내는 직선이다.  
직선이기 때문에 데이터의 경향을 더 쉽게 이해할 수 있다. 산점도와 같이 그리면 데이터를 이해하기 더욱 쉬워진다. 
```
 # 계수 β_0과 β_1을 구한다.
poly_fit = np.polyfit(english_scores, math_scores, 1)
 # β_0 + β_1  x를 반환하는 함수를 작성.
poly_1d = np.poly1d(poly_fit)
 # 직선을 그리기 위해 x좌표를 생성
xs = np.linspace(english_scores.min(), english_scores.max())
 # xs에 대응하는 y좌표를 구한다.
ys = poly_1d(xs)

fig = plt.figure(figsize=(8,8)); ax = fig.add_subplot(111)
ax.scatter(english_scores, math_scores)
ax.plot(xs, ys, color="gray", label=f"{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x")
ax.set_xlabels("english"); ax.set_ylabels("mathematics")
plt.show()
```

### 히트맵 heat map
히트맵은 히스토그램의 2차원 버전이다.
```
fig = plt.figure(figsize=(10,8)); ax = fig.add_subplot(111)
c = ax.hist2d(english_scores, math_scores, bins=[9,8], range=[(35,80), (55,95)])
ax.set_xlabel("english"); ax.set_ylabel("mathematics")
ax.set_xticks(c[1])
ax.set_yticks(c[2])
fig.colorbar(c[3], ax=ax); plt.show()
```
여기서는 영어점수가 35-80점까지 5점간격, 수학점수가 55-95점까지 5점간격이 되도록 bins와 range를 정했다.

## 앤스컴의 예
수치로만 데이터를 정리하면 많은 정보를 잃어버릴 수 있으니 주의해야 한다.  
예를 들면, 동일해 보이는 지표를 가진 데이터라도 그림으로 그리면 전혀 다른 데이터일 수 있기 때문이다.  
평균이나 분산이라는 지표가 많은 의미를 갖지만, 이러한 지표들을 과신하면 안된다. 앤스컴의 예는 __데이터를 분석할 때 가능하면 그림을 그려야 한다는 것__ 을 알려준다.
```
코드와 그래프는 스킵
```



