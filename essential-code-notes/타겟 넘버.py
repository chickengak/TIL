"""
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""


# My answer
def dfs(numbers, idx, target, total):
    global answer
    if idx == len(numbers):
        if total == target:
            answer +=1
        return
    else:
        dfs(numbers, idx + 1, target, total+numbers[idx])
        dfs(numbers, idx + 1, target, total-numbers[idx])
    return

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, 0,target, 0)
    return answer
# 다른 DFS 코드들은 내 코드와 비슷하거나 느린 코드들 뿐이었다.



# Other's answer
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
# product를 사용했다. 내 코드보다 40%정도 빨랐다.


def solution(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
    return q.count(target)
# count를 사용하는 독특한 풀이를 보여줬다. 이것도 40%정도 빠르다.


def dfs(nums, i, n, t):
    ret = 0
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer
# 변수명이 애매한것 빼곤 간결하고 컴팩트한 코드라서 가져왔다.
