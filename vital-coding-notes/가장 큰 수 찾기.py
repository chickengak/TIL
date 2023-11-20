"""
I
G
"""


# My answers
def solution(l):
    return [max(l), l.index(max(l))]


def solution(array):
    max = array[0]
    idx = 0
    for i, t in enumerate(array):
        if t > max:
            max = t
            idx = i
    return [max, idx]
# I thought these two functions, but I submitted the first one. Because the code is shorter excluding efficiency.
