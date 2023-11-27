"""
Input: a list of integers   ( 2 <= len(list) <= 100 , 10,000 <= integer <= 10,000 )
Goal: Find the maximum product of two integers.
"""


# My answer
def solution(numbers):
    numbers.sort()
    m = numbers[0]
    n = numbers[1]
    o = numbers[-2]
    p = numbers[-1]
    if m*n < o*p:
        return o*p
    else:
        return m*n
    return answer


# Others' answer
def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1], numbers[-2]*numbers[-1])
# Oops I forgot the max(). Now, I don't think I'll ever forget this function.


