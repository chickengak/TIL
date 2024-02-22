"""
I: a string A. And a string B representing pushed A.
G: Return the minimum number of shifts needed to push A to the right and become B. If it's not possible, return -1.
https://school.programmers.co.kr/learn/courses/30/lessons/120921
"""


# My answer
def solution(A, B):
    leng = len(A)
    for i in range(leng):
        if (A[leng - i:] + A[0:leng - i]) == B:
            return i
    return -1


# Others' answer
def solution(A, B):
    return (B * 2).find(A)
# I think it's a nice using of the find method.

