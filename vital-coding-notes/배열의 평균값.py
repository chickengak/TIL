"""
Input: list of integers
Goal: Find the median of a list
"""

# My answer
def solution(numbers):
    return sum(i for i in numbers) / len(numbers)


# Others' answers
def solution(numbers):
    return sum(numbers) / len(numbers)
    # No need to use a for loop.


import numpy as np
def solution(numbers):
    return np.mean(numbers)
    #You can also use the numpy library
