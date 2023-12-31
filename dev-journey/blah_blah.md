
### 컴파일러 vs 인터프리터

|       | 컴파일러             | 인터프리터                        |
|-------|------------------|------------------------------|
| 작동방식  | **소스코드를 기계어로 먼저 번역** <br> 해당 플랫폼에 최적화되어 프로그램을 실행. | 별도의 번역과정 없이 <br> **소스코드를 실행시점에 해석**하여 <br> 컴퓨터가 처리할 수 있게 함. |
| 장단점   | 실행속도가 빠름. <br> 한 번의 많은 기억장소 필요  | 실행속도가 느림. <br> 간단히 작성, 메모리가 적게 필요 |
| 주요 언어 | C, 자바,C++,C#...  | 파이썬, 스칼라..                   |

<br>

### 파이썬 특징
- 객체 지향
- Dynamic Typing 동적 타이핑 언어: 프로그램이 실행되는 시점에 프로그램이 사용해야할 데이터의 타입을 결정함.

<br>

### 복제
```python
a = [1,2,3,4,5]
b = a[:]
a[0]=100
'''
a = [100,2,3,4,5]
b = [1,2,3,4,5]
'''


a = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
c = a[:]
c[0][0]=100
'''
a = [[100, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
c = [[100, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
[:] 복제는 1차원에서만 작동.
'''


import copy
d = copy.deepcopy(a)        # 2차원 이상의 행렬은 deepcopy
a = [0][0] = 99
'''
a = [[99, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
d = [[100, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
'''


# m * n 0행렬 만들기
m = 3; n = 4
mat = [[0]*n]*m             # 이라믄 안돼
mat[0][0] = 7
'''
mat =   [[7, 0, 0, 0],
         [7, 0, 0, 0],
         [7, 0, 0, 0]]
         모든 행이 같은 리스트를 참조함
'''


mat = [[0]*n for _ in range(m)]
mat[0][0] = 7
'''
mat =   [[7, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
         이제야 모든 행이 다른 리스트를 참조함
'''
```


<br>

### all, any
```python
boolean_list = [True, False, True, False, True]
all(boolean_list)           # False
any(boolean_list)           # True 
```


<br>

## **Function Type Hints & Functino Docstring**
Type hits의 장점: mypy, IDE, linter 등을 통해 코드의 발생가능한 오류를 사전에 확인 가능  
Docstring: VScode에서 확장프로그램을 쓰면 쉬움. crtl+shift+P → Generate Docstring
```python
def func01(name: str, age: int) -> str:
    '''
    Returns the self-introduction in a string.

        Parameters:
            name (str): The name you want to print.
            age (int): The age you want to print.

        Returns:
            f"" (str): A string formatted using the provided parameters.
    '''
    return f"Hi, My name is {name}. And I'm {age} years old."
```

### 함수 작성 가이드
- 함수는 가능하면 짧게 작성할 것(줄 수를 줄일 것)
- 함수 이름에 함수의 역할, 의도가 명확히 드러나게 해야 함
- 인자로 받은 값 자체를 바꾸진 말 것. 임시 변수에 복제할 것
- 공통적으로 사용되는 코드는 함수로 변환
- 복잡한 수식 -> 식별이 가능한 이름의 함수로 변환 ex) 근의 공식
- 복잡한 조건 -> 식별 가능한 이름의 함수로 변환

### 코딩 컨벤션
구글 파이썬 코딩 컨벤션  
- 함수명, 변수명은 sanke_case
- 클래스명은 CamelCase
- flake8 모듈로 체크 가능.
- black 모듈을 이용하면 자동 수정 가능.

<br>



### set
```python
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

s1.union(s2)
s1 | s2             # 합집합

s1 ^ s2             # symmetric difference 대칭차집합

s1 & s2
s1 - s2
```
counter  namedtuple

## **collections**
### deque ( queue )
파이썬에선 queue도 deque로 씀.  
Linked-List 형태임.  
deque(데크)의 원어는 Double-Ended Queue
```python
from collections import deque

deq = deque([2,3,4], maxlen = 5)    # maxlen은 선택옵션

deq.append(5)
deq.appendleft(1)

deq.pop()
deq.popleft()

deq.extend(array)
deq.extendleft(array)

deq.remove(value)    # value를 데크에서 찾아서 삭제. 못 찾으면 에러.

deq.rotate(n)     # 데크를 n만큼 회전. 양수면 오른쪽, 음수면 왼쪽

deq.reverse()

copied_deq = deq.copy()      # 얕은 복사

deq.count("3")

deq.index(value, start, stop)   # value의 인덱스를 출력. start와 stop은 옵션.
                                # 못 찾으면 에러.
deq.insert(idx, value)      # idx 위치에 value를 삽입.

deq.clear()
```

### defaultdict
dict는 없는 key를 호출하면 에러가 나는데  
에러 대신 기본값이 출력되게 바꾼 dict임. 텍스트에서 각 단어가 몇 번 등장하는 지에 유용.

```python
d = dict()
d["ABC"]                # Error


from collections import defaultdict

d = defaultdict(lambda : 0)
d["ABC"]                        # 0
```

### Counter
 Counter 객체는 사전(dictionary)의 하위 클래스로, 해시 가능한 객체를 카운팅하는 데 적합.
```python
from collections import Counter

text = "banana"
char_count = Counter(text)          # Counter({'a': 3, 'n': 2, 'b': 1})
```

### namedtuple
Tuple 형태로 Data 구조체를 저장하는 방법.  
namedtuple은 튜플(tuple)의 하위 클래스로, 각 요소에 이름을 할당할 수 있어 코드의 가독성을 높여줍니다.
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(11, y=22)

p       # Point(x=11, y=22)
p.x     # 11
p.y     # 22
```

<br>

## Pythonic Code
- split & join
- list comprehension
- enumerate & zip
- lambda & map & reduce (코드의 직관성이 떨어져서 권장은 안함)
- generator
- asterisk (*) 

```python
""" 리스트 컴프리헨션 핵꿀팁 """

list01 = ['1', '2', '3']
list02 = ['A', 'B', 'C']

[i+j for i in list01 for j in list02]
[[i+j for i in list01] for j in list02]

# ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
# [['1A', '2A', '3A'], ['1B', '2B', '3B'], ['1C', '2C', '3C']]

for i in list01:
    for j in list02:
        res.append(i+j)

for j in list02:
    row = list()
    for i in list01:
        row.append(i+j)
    res.append(row)



""" enumerate로 dict 만들기 """
text = 'The Samsung Group is a South Korean multinational conglomerate headquartered in Samsung Town, Seoul.'

d = {v.lower() : i for i, v in enumerate(list(set(text.split())))}

for i, values in enumerate(zip(list01, list02)):
    print(i, values)



""" map은 인자 두개도 가능 """
ex = [1, 2, 3, 4, 5]
list(map(lambda x: x**2, ex))               # [1, 4, 9, 16, 25]

list(map(lambda x, y: x + y, ex, ex))       # [2, 4, 6, 8, 10]

# 허나 map 보다는 list comprehension이 권장됨. 실제로 lambda가 느리긴 함

[x**2 for x in ex]

[x + y for x, y in zip(ex, ex)]



""" reduce는 대용량 데이터를 다룰때 많이 씀 """
from functools import reduce

reduce(lambda x, y: x + y, ex)  # 근데 이건 sum 쓰면 되는디

reduce(lambda x, y: x * y, ex)
```

### generator　iterable object

```python
ex = [1, 2, 3, 4, 5]
iter_obj = iter(ex)       # <list_iterator object at 0x000002206C9C0C40>
print(next(iter_obj))     # 1
print(next(iter_obj))     # 2
print(next(iter_obj))     # 3


def general_list(value):
    result = []
    for i in range(value):
        result.append(i)
    return result                # 일반적인 리스트 형태.

def generator_list(value):       # 호출해야 값이 리턴됨. 메모리주소만 저장된 상태
    result = []                  # 리스트 자체를 리턴하는 것보다 메모리 절약이 됨
    for i in range(value):       # 대용량 데이터를 가져올 때는 권장된다고.
        yield i

# list comprehension과 유사한 형태로 generator형태의 list를 만들 수 있다
# [] 대신 ()를 쓰면 됨.
generator_ex = (n * n for n in range(500))
type(generator_ex)                  # <class 'generator'>
```
**generator를 써야할 때**
- list 타입의 테이터를 반환해주는 함수는 generator로 만들어라.
    - 읽기 쉬운 장점. 중간 과정에서 loop이 중단될 수 있을 때!
- 큰 데이터를 처리할 대는 generator expression을 고려해라.
    - 데이터가 커도 처리의 어려움이 없다.
- 파일 데이터를 처리할 때도 generator를 쓰자.


### asterisk (*)　
*args 여러개의 값을 튜플형태의 가변인자로 넣는거  
*kwargs 여러개의 값을 딕트형태의 가변인자로 넣는거. 파라미터 이름을 따로 정하지 않고 입력하는 방법
```python
def asterisk_test(a, b, *args):
    print(a, b, args)

asterisk_test(1, 2, 3, 4, 5)    # 1 2 (3, 4, 5)


def kwargs_test(**kwargs):
    print(kwargs)

kwargs_test(first=3, second=4, third = 5)   # {'first': 3, 'second': 4, 'third': 5}


def args_kwargs(one, two, *args, **kwargs):     # 사실 이렇게 복잡할 경우는 없다
    print(one, two)
    print(args)
    print(kwargs)

args_kwargs(1, 2, 3, 4, 5, 6, first=3, second=4, third = 5)
'''
1 2
(3, 4, 5, 6)
{'first': 3, 'second': 4, 'third': 5}
'''

args_kwargs(one=1, two =2, first=3, second=4, third = 5)
''' 1 2   ()    {'first': 3, 'second': 4, 'third': 5} '''



# asterisk를 이용한 Unpacking
ex = [1, 2, 3, 4, 5]
print(ex)       # [1, 2, 3, 4, 5]
print(*ex)      # 1 2 3 4 5

def asterisk_unpack(*args):
    print(*args)

asterisk_unpack(1,2, [3,4,5])

data = {'b':1, 'c':2, 'd':3}        # 흠... 이건 뭐 어따 쓰지?
print(*data)            # b c d
def func(a,b,c,d):
    print(a,b,c,d)
func(10, **data)        # 10 1 2 3




# ----- zip 과 함께 Unpacking-----------  ★★★
arr = ([1, 2], [3, 4], [5, 6], [7, 8], [9, 10])

for x in zip(arr):
    print(x)
'''                 개억지네 ㅋㅋㅋ 쓸모없음
([1, 2],)
([3, 4],)
([5, 6],)
([7, 8],)
([9, 10],)
'''

for x in zip(*arr):
    temp.append(x)
temp        # [(1, 3, 5, 7, 9), (2, 4, 6, 8, 10)] ★★★

# 5x2 행렬이 순식간에 2x5로 ㄷㄷㄷ
```

<br>
<br>

### 삼항연산자 = Ternary operators


### is
== 연산은 값이 같은지를 확인하지만 is 연산은 메모리주소가 같은지를 확인한다.
```python
a = 100
b = 100
a is b          # True

a = 300
b = 300
a is b          # False

'''
위와 같은 결과가 발생하는 이유.
파이썬은 -5 ~ 256 까지의 자주 쓰이는 수는 같은 메모리주소를 참조하게 했기 때문에
발생하는 현상.
'''
```

### Call by Reference
"Call by Reference"는 프로그래밍에서 함수에 인자를 전달하는 방식 중 하나입니다. 이 방식에서는 실제 인자의 주소가 함수에 전달됩니다. 즉, 함수 내에서 인자의 값이 변경되면, 그 변경사항이 호출한 골짜기의 실제 인자에도 반영됩니다.

Python에서는 엄밀히 말하면 "Call by Reference"를 지원하지 않습니다. Python은 "Call by Object Reference"를 사용합니다. 이는 객체의 참조(즉, 메모리 주소)가 함수에 전달되지만, 객체 자체가 전달되는 것은 아니라는 것을 의미합니다. 이로 인해 객체가 변경 가능(mutable)인 경우 함수 내에서의 변경이 외부 객체에 영향을 미칠 수 있습니다.
```python
def spam(eggs):
    eggs.append(1)      # 기존 객체의 주소값에 [1] 추가
    eggs = [2, 3]       # 새로운 객체 생성

ham = [0]
spam(ham)
print(ham)      # [0, 1]



def swap_value(x, y):
    temp = x
    x = y
    y = temp

def swap_offset(offset_x, offset_y):
    temp = a[offset_x]
    a[offset_x] = a[offset_y]
    a[offset_y] = temp

def swap_reference(list, offset_x, offset_y):
    temp = list[offset_x]
    list[offset_x] = list[offset_y]
    list[offset_y] = temp
```

<br>

### raw string \b \e
```python
raw_str = '파이썬\t파삼썬'
print(raw_str)              # 파이썬    파삼썬
파이썬	파삼썬

raw_str = r'파이썬\t파삼썬'
print(raw_str)              # 파이썬\t파삼썬

print('asdf\b')             # asd    백스페이스임

print('asdf\e')             # ESC키임
'''
<input>:1: SyntaxWarning: invalid escape sequence '\e'
<input>:1: SyntaxWarning: invalid escape sequence '\e'
asdf\e
'''
```

