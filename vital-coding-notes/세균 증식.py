"""
Input: integers ( 1 <= first integer <= 10 , 1 <= second interger <= 15)
Goal: n bacteria double every t hours
"""


# My answer
def solution(n, t):
    return n*(2**t)


# Others' answer
def solution(n, t):
    return n << t
# Bitwise operator. holy
