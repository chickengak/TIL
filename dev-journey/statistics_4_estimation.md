# Statics -추정 Estimation
지금까지는 사실 추측통계를 배우기 위한 준비과정이었다.  
추측통계는 추정과 검정이 있고, 추정에는 점추정과 구간추정이 있다.  
점추정은 추정하고 싶은 모수를 하나의 수치로 추정하는 방법이고, 구간추정은 모수를 구간으로 측정하는 방법이다.  

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('dev-journey/etc/ch4_scores400.csv')
scores = np.array(df['score'])
p_mean = np.mean(scores)                # 모평균 population mean   69.53
p_var = np.var(scores)                  # 모분산 population variance   206.6691
```
응시자가 많은 시험점수는 정규분포를 따른다고 근사할 수 있다.  
정규분포라는 가정이 얼마나 타당한지 성적 히스토그램과 정규분포를 중첩시켜보자.
```
fig = plt.figure(figsize = (10,6))
ax = fig.add_subplot(111)

xs = np.arange(101)
rv = stats.norm(p_mean, np.sqrt(p_var))
ax.plot(xs, rv.pdf(xs))
ax.hist(scores, bins=100, range=(0,100), density=True)
plt.show()                                          # 정규분포에 가까운 특징 확인

np.random.seed(0)
n = 20
sample = np.random.choice(scores, 20)               # 표본 추출
s_mean = np.mean(sample)                            # 표본 평균
s_var = np.var(sample, ddof=1)                      # 표본 분산 (책이 잘못계산해서 자유도를 늘림;)

np.random.seed(1111)
samples = np.random.choice(scores, (10000, 20))     # 20개인 표본을 10000번 추출
```

<br>
<br>
<br>

# 점추정　Point Estimation

## 모평균을 점추정
앞선 내용을 통해 무작위 추출로 얻은 20명의 시험점수는 기댓값이 $\mu$ 이고 분산이 $\sigma^2$ 인 확률분포를 따르고, 서로 독립인 확률변수 $X_1, X_2, ..., X_{20}$ 라고 볼 수 있다. 그리고 그것으로부터 계산되는 표본평균 $\bar X = \frac{X_1 + X_2 + ... + X_{20}}{20}$ 도 확률변수가 되고, 시행할 때마다 얻게 되는 결과는 다르다.  

이 표본 평균 $\bar X$ 의 기댓값은 $E(\bar X) = \mu$ 가 되므로 모평균과 일치한다.  
이렇게 추정량의 기댓값이 추측하려는 모수가 되는 성질을 __불편성__ unbiasedness 라고 하며, 불편성을 가진 추정량을 __불편추정량__ unbiased estimator 라고 한다.  
이를 반대로 말하면, 추정량의 편향은 추정량의 기대값과 실제 모수값과의 차이를 의미한다. 그러므로 불편성이 있는 추정량은 표본의 크기가 증가하더라도 추정량의 편향이 모수에서 멀어지지 않는 특성을 가진다.

표본 평균의 기댓값이 모평균인 것 $E(\bar X) = \mu$ 을 대수의 법칙으로 확인하자.
```
samples_means = np.mean(samples, axis=1)
np.mean(samples_means)                       # 69.538
```
이정도의 근사면 일치한다고 볼 수 있다. 표본평균이 모평균을 잘 추정할 수 있는 근거 중 하나가 바로 이 불편성이다.  

불편성 외에도 추정량이 가지고 있으면 좋은 성질이 있는데 이 성질이 바로 __일치성__ consistency 이고, 일치성을 가진 추정량을 __일치추정량__ consistent estimator 라고 한다. 일치성은 표본 크기 $n$ 이 커질수록 모수에 수렵해가는 성질이다. 
```
np.mean(np.random.choice(scores, int(1e7)))     # 69.5352
```
모평균에 근사해 간다.

요약하면, **불편성**은 추정량의 편향을 나타내며 추정량이 평균적으로 모수에 얼마나 가까운지를 나타내고, **일치성**은 표본 크기가 커짐에 따라 추정량이 모수에 점점 가까워지는 특성을 나타냅니다. **좋은 추정량**은 불편성과 일치성을 모두 만족하는 추정량입니다.

<br>

## 모분산을 점추정
표본평균과 마찬가지로 표본분산 $\displaystyle\frac{1}{n}\displaystyle\sum_{i=1}^{n}(X_i-\bar X)^2$ 은 확률변수가 되었으므로, 시행할 때마다 결과가 달라진다.

표본분산의 기댓값이 모분산인지 대수의 법칙으로 확인하자.
```
samples_vars = np.var(samples, axis=1)
np.mean(samples_vars)                       # 206.7839x 196.3442

samples_u_vars = np.var(samples, axis=1, ddof=1)
np.mean(samples_u_vars)                      # 206.678

u_var = np.var(sample, ddof=1)              # 158.253
```
$S^2 = \sigma^2$ 표본분산의 기댓값도 모분산과 비교해 불편성과 일치성을 보여준다. 그러므로 표본분산도 좋은 추정량임을 알 수 있다. 이렇게 표본 크기가 큰 경우 표본 분산을 모분산의 불편 추정량으로 사용할 수 있으며, 편향 보정을 위해 (n-1)로 나눌 필요가 없습니다. 하지만 표본 크기가 작을 때는 (n-1)로 나눈 불편 분산을 사용하여 모분산을 추정하는 것이 더 적절합니다.

결과적으로,  
추정량은 불편성과 일치성을 가져야 좋은 추정량이 된다.  
> - 불편성: 기댓값이 추측하길 원하는 모수가 되는 성질
> - 일치성: 표본 크기를 키우면 추측하길 원하는 모수로 수렴하는 성질

> $X_1, X_2, ..., X_n$ 이 서로 독립이고 기댓값이 $\mu$ , 분산이 $\sigma^2$ 인 확률분포를 따를 때, 표본평균 $\bar X$ 와 불편분산 $s^2$ 은 각각 모평균인 $\mu$ 와 모분산인 $\sigma^2$ 에 대해서 불편성과 일치성을 지닌 추정량이 된다.

<br>
<br>
<br>

# 구간추정　Interval Estimation
표본평균과 불편분산이 각각 모평균과 모분산의 좋은 추정량이 된다고 배웠지만, 어쨋든 확률변수이므로, 우연히 편향된 표본을 추출해버리는 경우엔 예상과 다른 추정이 될 수도 있다. 그래서 사전에 예상되는 오차를 예측하고 모평균이 이 범위에 있다는 주장을 할 수 있다면 보다 좋은 추정이 될 것이다.

## 정규분포의 모평균 구간 추정 - 모분산을 알고 있을 때
모집단을 정규분포로 가정했으므로, 표본 평균 $\bar X$ 는  $N \left(\mu, \displaystyle\frac{\sigma^2}{n}\right)$ 을 따른다. 결국 표본평균이라는 추정량은 기댓값 그 자체인 모평균 $\mu$ 와 표준편차 $\displaystyle\sqrt \frac{\sigma^2}{n}$ 로  분산되어 있다. 이와 같은 추정량의 표준편차를 **표준오차** standard error 라고 한다.

$X_1, X_2, ..., X_n \sim{iid}　N(\mu, \sigma^2)$ 일 때, 모분산 $\sigma^2$ 을 알면, 신뢰수준 100(1 - $\alpha$)%인 신뢰구간은  
$\left[ \bar X - z_{\alpha/2} \displaystyle\sqrt \frac{\sigma^2}{n} , \bar X - z_{1 - \alpha/2} \displaystyle\sqrt \frac{\sigma^2}{n} \right]$ 이 된다.

파이썬으로 구현해보자.
```
rv = stats.norm()
lcl = s_mean - rv.isf(0.025) * np.sqrt(p_var/n)         # 64.0996
ucl = s_mean - rv.isf(0.975) * np.sqrt(p_var/n)         # 76.7004
```
모평균 값인 69.53이 구간내에 포함됐음을 확인할 수 있다.  

이 95% 신뢰구간 [64.1, 76.7]을 모평균이 95% 확률로 구간안에 들어간다고 해석하고 싶겠지만 그렇게 해석하면 안 된다. 이 신뢰구간을 구하는 구간추정을 계속하면 100번 중 95번의 비율로 모평균이 포함된다는 뜻이기 때문이다. 즉, 모평균은 바뀌지 않는 하나의 값으로 이미 정해져 있고 표본에 의해 구간만 바뀌는 상황이다.  
```
모평균의 구간추정 시뮬레이션 스킵
```

신뢰구간 구하기를 1만번 계산해서 실제로 95% 확률로 신리구간이 모평균을 포함하는지 확인해보자.
```
rv = stats.norm()
cnt = 0

for sample_ in samples:
    s_mean_ = np.mean(sample_)
    lcl = s_mean_ - rv.isf(0.025) * np.sqrt(p_var/n)
    ucl = s_mean_ - rv.isf(0.975) * np.sqrt(p_var/n)
    if lcl <= p_mean <= ucl:
        cnt += 1
cnt / len(samples)              # 0.9512
```
<br>

## 정규분포의 모분산 구간추정
모집단으로 정규분포를 가정하고, 모평균은 모른다고 생각하겠다.  

$X_1, X_2, ..., X_n \sim{iid}　N(\mu, \sigma^2)$ 일 때, 모평균 $\mu$ 를 모른다면, 신뢰수준 100(1 - $\alpha$)%인 신뢰구간은  
$\left[ \displaystyle\frac{(n-1)s^2}{\chi_{\alpha/2}^2(n-1)} , \displaystyle\frac{(n-1)s^2}{\chi_{1-\alpha/2}^2(n-1)} \right]$ 이 된다.  

파이썬으로 구현해보자.  
```
rv = stats.chi2(df=n-1)
lcl = (n-1) * u_var / rv.isf(0.025)         # 91.5247
ucl = (n-1) * u_var / rv.isf(0.975)         # 337.5955
```
모분산값인 206.669가 포함된다는 것을 확인할 수 있다.

```
모분산의 구간추정 시뮬레이션 스킵
```

이제 1만번 시행하여 신뢰구간이 모분산을 얼마나 포함하는지 확인해보자.
```
rv = stats.norm()
cnt = 0

for sample_ in samples:
    u_var_ = np.var(sample_, ddof=1)
    lcl = (n-1) * u_var_ / rv.isf(0.025)
    ucl = (n-1) * u_var_ / rv.isf(0.975)
    if lcl <= p_var <= ucl:
        cnt += 1

cnt / len(samples)              # 0.9641
```

<br>

## 정규분포의 모평균 구간추정 - 모분산도 모를 때
사실 모분산을 모르는 상황에서 모평균 구간추정을 하는 경우가 많다.  
모분산을 모른다고 복잡해질건 없고 단지 사용하는 확률분포만 달라질 뿐이다.  
앞서서는 모분산 $\sigma^2$ 를 알고 있기 때문에 표본평균 $\bar X$ 의 표준오차인  $\displaystyle\sqrt \frac{\sigma^2}{n}$ 으로 구간추정을 했다. 하지만 모분산을 모르기 때문에 모분산대신 추정량인 불편분산 $s^2$ 을 사용한 $\displaystyle\sqrt \frac{s^2}{n}$ 을 표준오차로 대신 사용한다.  
<과정생략>

$X_1, X_2, ..., X_n \sim{iid}　N(\mu, \sigma^2)$ 일 때, 모분산 $\sigma^2$ 를 모른다면, 신뢰수준 100(1 - $\alpha$)%인 신뢰구간은  
$\left[ \bar X - t_{\alpha/2}(n-1) \displaystyle\sqrt \frac{s^2}{n} , \bar X - t_{1 - \alpha/2}(n-1) \displaystyle\sqrt \frac{s^2}{n} \right]$ 이 된다.  

파이썬으로 구현해보자.
```
rv = stats.t(df=n-1)
lcl = s_mean - rv.isf(0.025) * np.sqrt(u_var/n)         # 64.5124
ucl = s_mean - rv.isf(0.975) * np.sqrt(u_var/n)         # 76.2876
```
모평균값인 69.53이 포함됨을 확인할 수 있다.


## 베르누이 분포의 모평균 구간추정
정규분포를 따르지 않고 베르누이를 따르는 데이터들. 즉, 찬반과 같은 2진 변수로 구성된 데이터의 모평균 구간추정은 방법이 다르다. 우선, 모집단의 비율을 $p$ 라고 하고 $Bern(p)$를 따르는 확률변수를 가정하자.
```
enquete_df = pd.read ... 스킵
```

$X_1, X_2, ..., X_n \sim{iid}　Bern(p)$ 일 때, 신뢰수준 100(1 - $\alpha$)%인 신뢰구간은  
$\left[ \bar X - z_{\alpha/2} \displaystyle\sqrt \frac{\bar X(1-\bar X)}{n} , \bar X - z_{1 - \alpha/2} \displaystyle\sqrt \frac{\bar X(1-\bar X)}{n} \right]$ 이 된다.  

파이썬으로 구현해보자.
```
rv = stats.norm()
lcl = s_mean - rv.isf(0.025) * np.sqrt(s_mean*(1-s_mean)/n)     # 0.681
ucl = s_mean - rv.isf(0.975) * np.sqrt(s_mean*(1-s_mean)/n)     # 0.737
```

## 포아송 분포의 모평균 구간추정
단위 시간당 발생하는 건수를 설명하는 분포인 포아송 분포 $Poi(\lambda)$ 을 생각해보자. 포아송 분포 $Poi(\lambda)$ 의 기댓값과 분산은 모두 $\lambda$ 였기 때문에 표본평균 $\bar X$ 의 기댓값은 $\lambda$ 가 되고, 분산은 $\frac{\lambda}{n}$ 이 된다.

$X_1, X_2, ..., X_n \sim{iid}　Poi(\lambda)$ 일 때, 신뢰수준 100(1 - $\alpha$)%인 신뢰구간은  
$\left[ \bar X - z_{\alpha/2} \displaystyle\sqrt \frac{\bar X}{n} , \bar X - z_{1 - \alpha/2} \displaystyle\sqrt \frac{\bar X}{n} \right]$ 이 된다. 

파이썬으로 구현해보자.
```
rv = stats.norm()
lcl = s_mean - rv.isf(0.025) * np.sqrt(s_mean/n)     # 0.681
ucl = s_mean - rv.isf(0.975) * np.sqrt(s_mean/n)  
```