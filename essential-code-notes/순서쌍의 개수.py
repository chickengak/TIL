"""
Input: integer  ( i <= integer <= 1,000,000)
Goal: Number of ordered pairs
"""


# My answer
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
# My answer is optimized than Others' answer. I win lol.


# Others' answer
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))
# Well it can be short code, but it's too slow.
