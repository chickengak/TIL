# Statistics - Probability 확률변수와 확률분포
확률변수는 취할 수 있는 값이 이산이냐 연속이냐에 따라 이산형 확률변수와 연속형 확률변수 두 가지로 구분된다.
<br>
<br>

# 이산형 확률변수

# 1차원 이산형 확률변수
<br>

## 확률질량함수 - 1차원 이산형 확률변수의 정의
__확률변수는 변수가 취할 수 있는 값과 그 값이 나오는 확률에 의해 정의된다.__  
이를 1차원 이산형 확률변수에 대입하여  
$P(X = x_k) = p_k　　(k=1,2,3,...)$ 라는 확률을 정의할 수 있고,  
$f(x) = P(X=x)$　 　 이 때, 확률은 확률변수가 취할 수 있는 값 x를 인수로 하는 함수로 볼 수 있는데,  
이를 __확률질량함수__ Probability Mass Function PDF 또는 확률함수라고 한다.

확률변수가 취할 수 있는 값과 그 확률의 구체적인 대응을 확률분포 Probability Distribution 라고 한다. 따라서 확률변수의 확률분포가 결정되면 그 확률변수의 움직임이 정해진다.  

불공정한 주사위로 확률변수를 구현해보자.
```
x_set = np.array([1,2,3,4,5,6])      # 확률변수가 취할 수 있는 값.

def f(x):                            # 확률변수
    if x in x_set:
        return x / 21
    else:
        return 0
```

확률변수가 취할 수 있는 값의 집합과 확률변수의 세트가 확률분포다. 이 확률분포에 의해 확률변수 X의 동작이 결정된다.  
```
X = [x_set, f]            # 확률변수 X의 정의.
```
이제 확률변수로부터 각 x의 확률 p를 구해보고 막대그래프로 그려보자.
```
prob = np.array([f(x_k) for x_k in x_set])
dict(zip(x_set, prob))
    # {1: 0.048, 2: 0.095, 3: 0.143, 4:0.190, 5: 0.238, 6: 0.286}

fig = plt.figure((10,6)); ax = fig.add_subplot(111)
ax.bar(x_set, prob)
ax.set_xlabel("dice"); ax.set_ylabel("probability")
plt.show()
```
<br>

## 확률의 성질
확률의 중요한 2가지 성질.
1. 확률은 절대적으로 0 이상
2. 모든 확률을 더하면 1  
$f(x_k) >= 0$  
$\displaystyle\sum_{k} f(x_k) = 1$

이 성질을 만족해야 확률이 올바른 것이고 코드로 확인하는 방법은 아래와 같다.
```
np.all(prob >= 0)               # True
np.sum(prob)                    # 1.000
```

## 누적분포함수
확률변수 X가 x이하가 될 때의 확률을 구하는 함수로 누적분포함수 Cumulative Distribution Funcion CDF 라고 한다.  
$F(x) = P(X \leq x) = \displaystyle\sum_{x_k \leq x} f(x_k)$  

```
def F(x):
    return np.sum(f(x_k) for x_k in x_set if x_k <= x)
```

## 확률변수의 변환
확률변수의 변환이란 확률변수 X에 2를 곱하고 3을 더한 2X+3과 같은 것으로,  
확률변수를 배우는 이유는 나중에 __표준화할 때__ 요긴하게 쓰이기 때문이다. 원래 표준화할 때는 평균을 빼고 표준편차로 나누지만, 여기 예시에서는 역으로 진행하겠다.  

그러면 2X+3으로 변환한 확률변수도 확률변수일까?  

우리는 이미 앞에서 주사위로 변환했었기 때문에 확률변수가 성립한다는 사실을 안다.

```
y_set = 2 * x_set + 3
prob = np.array([f(x_k) for x_k in x_set])
dict(zip(y_set, prob))
    # {5: 0.048, 7: 0.095, 9: 0.143, 11:0.190, 13: 0.238, 15: 0.286}
```
Y의 확률변수도 구할 수 있지만, 이 책에서는 거기까지 나가지 안흔다. 확률벼ㅓㄴ수의 변환을 정의할 수 있고, 변환한 후에도 확률변수가 된다는것만 알면된다랄까


# 1차원 이산형 확률변수의 지표

## 기댓값
데이터의 평균은 모두 합하고 개수로 나누면 됐다. 하지만 확률변수의 평균은 어떻게 구할까?

확률변수의 평균이란 확률변수를 무제한으로 시행하여 얻어진 실현값의 평균을 말한다.  
물론 직접 무제한으로 시행할순 없기에, **확률변수가 취할 수 있는 값과 그 확률의 곱들의 합**으로 정의한다.

$E(X) = \displaystyle\sum_{k} x_k\cdot f(x_k)$

확률변수의 평균은 __기댓값__ Expected value 라고 하며 $\mu$ 혹은 $E(X)$로 표기한다.

```
np.sum([x_k * f(x_k) for x_k in x_set])

sample = np.random.choice(x_set, int(1e6), p=prob)
np.mean(sample)                          # 샘플로 테스트한 결과 4.333으로 동일.
```
<br>

이번엔 변환한 확률변수의 기댓값을 확인해보자. X를 2X+3으로 변환하면 다음과 같다.  

$E(Y) = E(2X+3) = \displaystyle\sum_{k} (2x_k+3)\cdot f(x_k)$  
이를 더 일반화하면

$E(g(X)) = \displaystyle\sum_{k} g(x_k) \cdot f(x_k)$  

```
def E(X, g=lambda x:x):
    x_set, f = X
    return np.sum([g(x_k) * f(x_k) for x_k in x_set])
```
g에 기본값을 줬기 때문에 따로 변환한 확률변수를 입력하지 않으면 확률변수 X를 리턴받는다.

<br>

기댓값에는 선형성이라는 중요한 성질이 있다. 이 성질을 사용하여 aX + b와 같은 형태로 빠르게 구할 수도 있다.

$E(aX + b)) = a\cdot E(X) + b$  
```
E(X, g=lambda x: 2*x +3); 2*E(X) +3     # 실제로 이 둘은 11.667로 같다.
```
<br>

## 분산
확률변수의 분산도 데이터의 분산과 마찬가지로 산포도를 나타내는 지표가 된다.  
이산형 확률변수에서 분산은 편차 제곱의 기댓값으로 정의된다.

$V(X) = \displaystyle\sum_{k} (x_k - \mu)^2 \cdot f(x_k)$

분산은 $\sigma^2$ 혹은 $V(X)$ 로 표기한다.

```
mean = E(x)
np.sum([ (x_k - mean)**2 * f(x_k) for x_k in x_set]) # 불공정한 주사위로 분산을 구함
```
<br>

이번엔 변환한 확률변수의 분산을 확인해보자.

$V(2X+3) = \displaystyle\sum_{k} ((2x_k+3) - \mu)^2 \cdot f(x_k)$

$V(g(X)) = \displaystyle\sum_{k} (g(x_k) - E(g(X)) )^2 \cdot f(x_k)$

```
def V(X, g=lambda x: x):
    x_set, f = X
    return np.sum([ (g(x_k) - E(X, g))**2 * f(x_k)  for x_k in x_set])
```
<br>

기댓값과 달리 분산에는 선형성이 없지만, V(X) 를 이용해 변환된 확률변수의 분산을 구할 순 있다.

$V(aX + b) = a^2\cdot V(X)$

```
V(X, g=lambda x: 2*x+3); 2**2 * V(X)    #8.889로 동일하다.
```

<br>
<br>

# 2차원 이산형 확률변수

## 결합확률분포 - 2차원 이산형 확률변수
2차원 확률변수에서는 1차원 확률분포 2개를 동시에 다룬다. (X, Y)  

$\{ (x_i, y_i) | i = 1,2,...; j = 1,2,... \}$  

$P(X=x_i, Y=y_j) = p_{ij}　　(i = 1,2,...; j = 1,2,...)$

이와 같이 확률변수(X, Y)의 움직임을 동시에 고려한 분포를 __결합확률분포__ Joint probability distribution 또는 결합분포 라고 한다.

앞선 내용과 마찬가지로 공분산이 0 되는 것을 방지하고자, A와 B 눈의 합을 X, A의 눈을 Y로 하겠다.  
X는 {2,3,4,5,6,7,8,9,10,11,12}를 취하고, Y는 {1,2,3,4,5,6}을 취하게 된다.  
확률은 서로 결합확률을 구하면 된다.  

2차원 확률분포의 확률은 x와 y를 인수로 취하는 함수라고 볼 수 있다. 이 $f_{XY}(x,y)$ 함수를 __결합확률함수__ Joint probability function 이라고 한다.
```
x_set = np.arange(2, 13)
y_set = np.arange(1, 7)

def f_XY(x, y):
    if 1 <= y <= 6 and 1 <= x-y <= 6:
        return y * (x-y) / 441
    else:
        return 0

XY = [x_set, y_set, f_XY]
```

결합확률분포를 보기 편하게 히트맵으로 그려보자.

```
prob = np.array([ [ f_XY(x_i, y_j) for y_j in y_set ] for x_i in x_set ])

fig = plt.figure((10,8)); ax = fig.add_subplot(111)

c = ax.pcolor(prob)
ax.set_xticks(np.arange(prob.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(prob.shape[0]) + 0.5, minor=False)
ax.set_xticklabels(np.arange(1, 7), minor=False)
ax.set_yticklabels(np.arange(2, 13), minor=False)

ax.invert_yaxis()   # y축을 내림차순의 숫자가 되게 위아래를 역전시킴.
ax.xaxis.tick_top()    # x축 눈금을 그래프 위쪽에 표시
fig.colorbar(c, ax=ax)
plt.show()

np.all(prob >= 0)          # True    확률의 성질 만족.
np.sum(prob)               # 1.000   확률의 성질 만족.
```
<br>

## 주변확률분포
확률변수 (X, Y)에서 하나에만 흥미가 있을 때.  
만약 X 만의 움직임이 궁금하다면, $f_{XY}$에서 Y가 취할 수 있는 값 모두를 대입한 다음 모두 더한

$f_X(x) = \displaystyle\sum_{k} f_{XY}(x, y_k)$

이 형태로 구할 수 있다. 이러한 $f_X(x)$를 X의 __주변확률분포__ Marginal Probability Distribution 라고 한다.  

```
def f_X(x):
    return np.sum([f_XY(x, y_k) for y_k in y_set])

def f_Y(y):
    return np.sum([f_XY(x_k, y) for x_k in x_set])

X = [x_set, f_X]
Y = [y_set, f_Y]
```
막대그래프로 직접 확인해보자.
```
prob_x = np.array([f_X(x_k) for x_k in x_set])
prob_y = np.array([f_Y(y_k) for y_k in y_set])

fig = plt.figure(figsize=(12,4))
ax1 = fig.add_subplot(121); ax2 = fig.add_subplot(122)

ax1.bar(x_set, prob_x)
ax1.set_xlabel("X_value"); ax1.set_ylabel("propability")
ax1.set_xticks(x_set)

ax2.bar(y_set, prob_y)
ax2.set_xlabel("Y_value"); ax2.set_ylabel("probability")
ax2.set_xticks(y_set)
plt.show()
```

<br>
<br>

# 2차원 이산형 확률변수의 지표
2차원 이산형 확률변수에 관해서는 기댓값이나 분산이라는 지표와 함께 3장에서 공부한 공분산이나 상관계수라는 지표를 정의할 수 있다.

## 기댓값
1차원 이산형 확률변수 즉, 확률질량함수때와 마찬가지로 $x_i$ 와 확률의 곱으로 구할 수 있다.



<br>
<br>
<br>
<br>

카이제곱 분포를 하는 이유? 범주형 데이터 처리하려고. 추론통계
- 적합도 테스트: 빈도 또는 범주형 데이터 셋이 특정 이론적 분포와 일치하는 지 확인할 때
- 분할표의 독립 테스트: 분할표(교차)를 분석할 때 사용, 두 범주형 변수 사이에 유의미한 연관성을 확인할 때
    - ex) 성별과 특정 제품에 대한 선호도 사이에 관계가 있는지 테스트
- 변형 테스트: 추론 통계에서 카이제곱 분포는 표본의 관측 분산이 예상 분산과 크게 다른지 유무확인 (기본 모집단에 대한 정규 분포를 가정)
- 분산 및 표준편차에 대한 신뢰구간: 모 집단 평균을 알수 없는 경우 카이제곱 분포를 사용하면 모집단 분산 및 표준 편차에 대한 신뢰구간을 구성.
- 균질성 테스트: 독립성 검정과 유사하지만 다양한 모집단에 걸친 범주형 변수의 분포를 비교.
    - ex) 연령대 분포가 여러지역에서 유사한지 확인


F 분포을 하는 이유 ? Fisher-Snedecor, ANOVA의 F-통계량 계산의 핵심, 가설 검정 및 분산 분석  
- ANOVA(분산 분석): 세 개 이상의 그룹의 평균을 비교하여 적어도 하나의 그룹 평균이 다른 그룹 평균과 통계적으로 다른지 확인하는 데 사용
- 분산에 대한 가설 검정: 모집단이 정규 분포를 따른다는 가정 하에 두 모집단의 분산을 비교하는 검정에 사용
    - 등분산에 대한 F-검정으로 두 개의 서로 다른 샘플에 유사한 분산이 있는지 확인하려는 경우에 유용
- 회귀 분석: 다중회귀분석에서는 모델의 전반적인 유의성을 검정하기 위해 F-분포를 사용
    - 예측 변수가 없는 모델(절편만 있음)을 예측 변수가 있는 지정된 모델과 비교하여 추가된 예측 변수가 모델을 크게 향상시키는지 확인
- 품질 관리: 다양한 생산 프로세스 또는 배치의 차이를 비교하여 제품 품질의 일관성을 보장등에 사용




# 요점 정리
## 이산형 분포
### 베르누이 분포
성공과 실패만이 있음. ex) 동전 던지기, 주사위

### 이항 분포
베르누이를 따르는 확률에서, n번 시도 후 성공 횟수가 궁금할 때.  
`stats.binom(n, p)`

### 기하 분포
베르누이를 따르는 확률에서, 처음 성공까지 걸리는 횟수가 궁금할 때.

### 포아송 분포
단위 시간당 사건이 몇번 발생했는지 궁금할 때,   
여기서 단위 시간은 단위 부피, 단위 공간 등도 가능하다는 점 유의.  
대체로 발생확률이 적은 곳에 사용.
`stats.poison(n)`

## 연속형 분포
### 지수 분포
단위 시간에서 포아송 확률과정을 따르는 사건이 발생할 때, 사건이 한 번 발생한 후 그 다음 사건이 발생할 때까지 걸리는 시간이 궁금함.  
여기도 단위 시간은 단위 부피, 단위 공간 등도 가능하다는 점 유의.  
단위 시간당 발생횟수가 m인 포아송 사건을 따를 때, 지수 분포에서 궁금한 소요시간의 평균은 $\lambda = \frac{1}{m}$ 이다.

### 감마 분포?

### 정규분포
$X \sim N[\mu, \sigma^2]$ 완벽한 대칭형의 종모양.  
`stats.norm(loc, scale)`  
**표준정규분포**: 평균이 0이고, 분산이 1인 정규분포. 정규분포를 따르는 X를 $\frac{X-\mu}{\sigma}$ 하면 만들 수 있다.  
표준정규 확률변수의 (1-$\alpha$)분위수: $Z_\alpha$

#### 연속형확률변수의 분포 중에서 정규모집단에서 나온 표본통계량들의 분포를 설명할 때 자주 사용되는 카이제곱, t분포, f분포. 다른 말로는 정규모집단에 대한 추론에 자주 활용되는 확률분포라고 한다.

### 카이제곱 분포
$X\sim X^2[k]$ 서로 독립인 표준 정규가 제곱해서 더해진 값들의 분포. k가 표준 정규의 개수이며 카이제곱의 모수인 자유도다.  
오른쪽 꼬리가 길게 늘어진 비대칭형. 자유도k가 늘어날 수록 퍼진 정규분포모양이됨.  

### t 분포
$X\sim t[k]$ 독립인 표준정규 Z와 자유도가 k인 카이제곱 U의 콜라보다. $X = \frac{Z}{\sqrt{U/k}}$  
0을 중심으로 대칭인 종모양. 분산이 표준정규보다 크다.  
자유도 k가 커짐에 따라 산포가 줄어들어서 표준정규분포에 수렴함.

### f 분포
$X\sim F[k_1,k_2]$ $k_1$자유도인 카이제곱 U와 $k_2$자유도인 카이제곱 V가 서로 독립일 때, 두 카이제곱의 콜라보다. $X = \frac{U/k_1}{V/k_2}$  
카이제곱처럼 오른쪽 꼬리가 길게 늘어진 비대칭형. 2개의 카이제곱 확률변수들의 비율로 정의되므로 음의 값을 가질 수 없다.  



