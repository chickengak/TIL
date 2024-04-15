# Statics -가설 검정 Hypothesis Testing

모수 평균 $\mu$ 모수 표준편차 분산 $\sigma \sigma^2$  
통계량 평균$\bar x$ 통계량 표준편차 $S S^2$

확률표본  
모집단의 변수 X의 확률분포함수를 f(x)라고 가정.  
모집단 f(x)로부터의 확률표본(iid표본) $X_1,X_2,...,X_n$ 은 다음의 두가지 성질을 만족하는 모집단 f(x)로부터의 표본을 뜻함.
- $X_1,X_2,...,X_n$ 은 서로 독립임.
- $X_1,X_2,...,X_n$ 은 모두 동일하게 f(x)의 분포를 따름.  

통계량: 확률표본 $X_1,X_2,...,X_n$ 의 함수  
 - 통계량의 예: 표본평균 $\bar x = \Sigma_{i=1}^{n} X_i/n$  

 표본분포: 통계량의 확률분포  
 - 표본분포의 예: 각 확률표본들의 평균이 그리는 분포모양.  
 표본이 비록 n개지만, 이들로 확률표본 뽑는 시도를 수없이 많이하면 표본평균이 모평균에 가까워진다. 표본분산은 평균으로 더욱 향해서 점점 더 뾰족해진다.

 표본추출방법
 - 단순임의 추출법(simple random sampling)
 - 계통추출법(systematic sampling)
 - 집락추출법(cluster sampling)
 - 층화추출법(stratified sampling)

<br>
<br>

# 1표본 가설 검정

## 정규분포의 모평균에 대한 검정 -모분산을 알고 있을 때
```python
def pmean_test(sample, mean0, p_var, alpha=0.05):
    s_mean = np.mean(sample)
    n = len(sample)
    rv = stats.norm()
    interval = rv.interval(1-alpha)

    z = (s_mean - mean0) / np.sqrt(p_var/n)
    if interval[0] <= z <= interval[1]:
        print('귀무가설을 채택')
    else:
        print('귀무가설을 기각')

    if z < 0:
        p = rv.cdf(z) * 2
    else:
        p = (1 - rv.cdf(z)) * 2
    print(f'p값은 {p:.3f}')

pmean_test(sample, 130, 9)
# 귀무가설을 채택
# p값은 0.053
```

## 정규분포의 모분산에 대한 검정
```python
def pvar_test(sample, var0, alpha=0.05):
    u_var = np.var(sample, ddof=1)
    n = len(sample)
    rv = stats.chi2(df=n-1)
    interval = rv.interval(1-alpha)
    
    y = (n-1) * u_var / var0
    if interval[0] <= y <= interval[1]:
        print('귀무가설을 채택')
    else:
        print('귀무가설을 기각')

    if y < rv.isf(0.5):
        p = rv.cdf(y) * 2
    else:
        p = (1 - rv.cdf(y)) * 2
    print(f'p값은 {p:.3f}')

pvar_test(sample, 9)
# 귀무가설을 채택
# p값은 0.085
```

## 정규분포의 모평균에 대한 검정 - 모분산을 모를 때
모분산을 모르는 상황에서 정규분포의 모평균에 대한 검정을 **1표본 t 검정** 1-sample t-test 이라고 한다. 그리고 **t 검정통계량**이라고 하는 $t=({\bar X - \mu_0}) / \displaystyle\sqrt\frac{s^2}{n}$ 을 검정통계량으로 사용한다. 그리고 자유도가 $n-1$ 인 t분포를 따른다.
```python
def pmean_test(sample, mean0, alpha=0.05):
    s_mean = np.mean(sample)
    u_var = np.var(sample, ddof=1)
    n = len(sample)
    rv = stats.t(df=n-1)
    interval = rv.interval(1-alpha)

    t = (s_mean - mean0) / np.sqrt(u_var/n)
    if interval[0] <= t <= interval[1]:
        print('귀무가설을 채택')
    else:
        print('귀무가설을 기각')

    if t < 0:
        p = rv.cdf(t) * 2
    else:
        p = (1 - rv.cdf(t)) * 2
    print(f'p값은 {p:.3f}')

pmean_test(sample, 130)
# 귀무가설을 채택
# p값은 0.169
```

1표본 t검정은 **ttest_1samp** 함수로 구현되어 있기도 하다.
```python
t, p = stats.ttest_1samp(sample, 130)

(-1.455, 0.169)
```

<br>
<br>

# 2표본 가설 검정

|             | **정규분포 가정 O** | **정규분포 가정 X** |
|:-----------:|:----------------:|:-------------------:|
| **대응분포** | 대응비교 t 검정   | 윌콕슨의 부호순위검정 |
| **독립표본** | 독립비교 t 검정   | 만 · 위트니의 U 검정 |

- 대응표본: 두 데이터에서 서로 대응하는 동일한 개체에 대해 각각 다른 조건으로 측정한 것.
    - ex) 피검자를 약을 투여하기 전후로 비교
- 독립표본: 두 데이터에서 개체가 다른 데이터로 되어 있는 독립 표본.
    - ex) 피검자를 반씩 나눠서 절반만 A약 테스트하고 나머지는 대조군으로 냅둠.

## 대응비교 t 검정 　Paired t-test
대응하는 데이터이기 때문에 각각의 데이터에서 발생하는 차이를 이용하면 된다.

- 귀무가설 $\mu_{after}$ - $\mu_{before}$ = 0 　 즉, $\mu_{diff}$ = 0
- 대립가설 $\mu_{after}$ - $\mu_{before}$ ≠ 0 　 즉, $\mu_{diff}$ ≠ 0  

전과 후의 차이가 없다면 즉, 두데이터가 서로 영향을 안미친다면, 그 차이는 임의로 분산되어 평균이 0인 분포가 될거다.  

더 나아가 그 차이가 각각 독립이고 동일한 정규분포를 따르고 있다고 가정할 수 있다면, 이 검정을 모분산을 모를 때 정규분포의 모평균에 대한 검정인 1표본 t검정으로 볼 수 있다. 
```python
t, p = stats.ttest_1samp(diff_list, 0)

t, p = stats.ttest_rel(after_list, before_list)

# p = 0.040
```
p 값이 유의수준(0.05)보다 작기 때문에 귀무가설은 기각된다.


## 독립비교 t 검정 　Independent t-test
정규분포를 가정할 수 있는 경우 평균값의 차이에 대한 검정이다.

- 귀무가설 $\mu_1$ - $\mu_2$ = 0
- 대립가설 $\mu_1$ - $\mu_2$ ≠ 0

대응이 없는 데이터라서 이번엔 차이를 구해도 아무 의미가 없다.

```python
t, p = stats.ttest_ind(data1_list, data2_list, equal_var=False)
                    # equal_var=False를 지정해야 웰치의 방법으로 계산된다.
# p = 0.087
```
p값이 유의수준보다 크기 때문에 귀무가설이 채택된다.

## 윌콕슨의 부호순위검정 　Wilcoxon signed-rank test
대응표본에서 차이에 정규분포를 가정할 수 없는 경우, 중앙값의 차이에 대한 검정이다.  
단, 모집단이 정규분포를 따르는 경우에도 쓸 수 있지만 대응비교 t 검정의 검정력이 더 높기 때문에 무의미해진다.  
```python
t, p = stats.wilcoxon(after_list, before_list)
t, p = stats.wilcoxon(before_list, after_list) # 순서는 상관없다.

# p = 0.038
```
유의수준보다 낮으니 귀무가설은 기각된다. 두 데이터의 차이는 있다.

## 만 · 위트니의 U 검정 　Mann-Whitney rank test
대응되는 데이터가 없는 2표본 모집단에 정규분포를 가정할 수 없는 경우, 중앙값의 차이에 대한 검정이다. 윌콕슨의 순위합검정이라고도 한다.
```python
t, p = stats.mannwhitneyu(data1_list, data2_list, alternative='two-sided')

# p = 0.059
```
p값이 유의수준보다 크기 때문에 귀무가설이 채택된다.

## 카이제곱검정　독립성 검정
독립성 검정 Test for indepnedence 은 두 변수 X와 Y에 관해서 'X와 Y가 독립이다' 라는 귀무가설과 'X와 Y가 독립이 아니다' 라는 대립가설에 의해 수행하는 감정이다. 독립성 검정에는 카이제곱분포가 사용되기 때문에 카이제곱검정 Chi-square test 라고도 한다.  

```python
chi2, p, dof, ef = stats.chi2_contingency(crosstab_dataframe, correction=False)

# chi2 = 3.750, p = 0.053, dof = 1
```
검정통계량, p값, 자유도, 기대도수까지 출력된다.