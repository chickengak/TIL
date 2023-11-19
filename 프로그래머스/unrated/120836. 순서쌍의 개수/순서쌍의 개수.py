import math

def solution(n):
    answer = 0
    sqrt = math.sqrt(n)
    for i in range(1, int(sqrt)+1):
        if not (n % i):
            if i == sqrt:
                answer += 0.5
            else:
                answer += 1
    return int(answer*2)