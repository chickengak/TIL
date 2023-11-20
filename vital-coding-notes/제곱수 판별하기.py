"""
Input: an integer
Goal: Check for a perfect square
Result: If n is a perfect square, return 1. else return 2
"""


# My answer
import math

def solution(n):
    sqrt = math.sqrt(n)
    return 1 if sqrt == int(sqrt) else 2


# Others' answer
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
# This function checks whether it is an integer or a float.


def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2
# This function checks through % operator.
