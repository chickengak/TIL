"""
Input: integer
Goal: Sum of the Digits of the Input
Output: integer
"""


# My answer
def solution(n):
    return sum([int(i) for i in str(n)])


# The others' answer
def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer

