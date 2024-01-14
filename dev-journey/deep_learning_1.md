## Deep Learning 딥러닝
#### 딥러닝의 범주와 구분  
![](etc/deep_learning.PNG)

#### 좋은 딥러닝의 3가지 요소
1. 구현 실력 Implementation Skills: tensorflow, pytorch...
2. 수학 실력 Math Skills: Linear Algebra, Probability
3. 최신 트랜드 Knowing a lot of recent Papers

#### 딥러닝의 주요 요소
- Data
    - 데이터는 해결하고자 하는 문제 유형에 따라 달라진다.  
      Data depend on the type of the problem to solve.
- Model : 데이터를 학습할 모델, 데이터를 내가 알고 싶어하는 클래스 레이블로 바꾸는 것.
    - 모델의 성질에 따라 결과가 바뀔 수 있기 때문에 태크닉들이 필요.
- Loss : a proxy of what we want to achieve.
    - 모델을 어떻게 학습할 지. 아래는 주로 사용하는 예시지 데이터와 목적에 따라 다른 선택이 필요할 수 있다. layer마다 들어있는 weight의 parameter를 어떻게 업데이트할지에 대한 기준.
    - 단순히 loss가 줄어든다고 우리가 원하는 목표를 이룬다는 보장이 없음. 
    - Regression Task: MSE
    - Classification Task: CE (Cross Entrophy)
    - Probabilistic Task: MLE
- Algorithm : optimization algorithm
    - 학습한 데이터만이 아니라 새로운 데이터에도 잘 작동하는지에 대한 알고리즘.


## Neural Networks
Neural networks are computing systems vaguely inspired by the biological neural networks that constitute animal brains.  
신경망이 뉴런을 모방했다곤 보기 힘들다.(역전파 등을 고려하면) 때문에 뉴런에서 영감을 받았다 정도가 적당하다고.

하늘을 날고 싶다고 새를 모방한게 아닌 새에서 영감을 받아 비행기를 만든것과 비슷한 이치다.

In other words, Neural networks are function approximators that stack affine transformations followed by nonlinear transformations.

### 인공 뉴런 Aritificial Neuron
- 노드와 엣지로 구성
- 하나의 노드안에서 입력과 가중치를 곱하고 더하는 선형구조.
- Activation function(활성 함수)을 통해 비선형 구조(non-linear)를 표현 가능.

### 인공 신경망 Artificial Neural Network
- 여러 개의 인공뉴런들이 모여 연결된 형태
- 뉴런들이 모인 하나의 단위를 층(layer)라고 하며, 여러 층(multi layer)으로 쌓을 수 있음.
- Input layer, 1~n Hidden layer, Output layer

&nbsp;

# Basic
### Tensor 텐서



&nbsp;

## Optimization
Important Concepts in Optimization
- Generalization
- Under-fitting vs. Over-fitting
- Cross validation
- Bias and Variance Trade-off
- Bootstrapping
- Bagging and boosting  
&nbsp;

### Generalizaion  
How well the learned model will behave on unseeen data.  
일반화 성능이 오를 수록 좋을까?

### Under-fitting vs. Over-fitting
![](etc/underfitting_overfitting.PNG)

### Cross-validation  
Cross-validation is a model validation technique for assessing how the model will generalize to an independent (test) data set.  
train data를 k개로 나누고 k-1개로 학습 후 남은 하나로 validation을 진행하는 방법.  
이를 통해 validation data와 train data를 합칠 수 있기 때문에 train data가 늘어나는 효과를 볼 수 있다.
![](etc/cross_validation.PNG)

Bias and Variance Trade-off



Gradient Descent
- First-order iterative optimization algorithm for finding a local minimum of a differentiable function.