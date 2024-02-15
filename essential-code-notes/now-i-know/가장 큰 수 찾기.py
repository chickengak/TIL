"""
I: a list of integers
G: Find the biggest number and its index.
https://school.programmers.co.kr/learn/courses/30/lessons/120899
"""


# My answers
def solution(l):
    return [max(l), l.index(max(l))]
# 0.01sec


def solution(array):
    max = array[0]
    idx = 0
    for i, t in enumerate(array):
        if t > max:
            max = t
            idx = i
    return [max, idx]
#0.009sec
# I thought these two functions, but I submitted the first one. Because the code is shorter excluding efficiency.
# Yes I know, the max method's time complexity is O(n).
