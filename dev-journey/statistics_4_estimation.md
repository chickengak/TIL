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
sample = np.random.choice(scores, 20)               # 표본 추출
s_mean = np.mean(sample)                            # 표본 평균
s_var = np.var(sample, ddof=1)                      # 표본 분산 (책이 잘못계산해서 자유도를 늘림;)

np.random.seed(1111)
samples = np.random.choice(scores, (20, 10000))     # 20개인 표본을 10000번 추출
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
np.mean(samples_vars)                       # 206.7839
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



