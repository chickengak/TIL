"""
Input: a list of integers   ( 0 < len(list) < 100 , a <= integer < 1000 )
Goal: Finding the most duplicated integer
Output: integer ( If the result is multiple, return -1 )
"""


# My answer
def solution(array):
    a_dict = {}
    for i in set(array):
        a_dict.setdefault(i,0)
    for i in array:
        a_dict[i] += 1
    ad_max = max(a_dict.values())
    result = [k for k, v in a_dict.items() if v == ad_max]
    return result[0] if len(result) == 1 else -1


# Others' answer
from collections import Counter

def solution(array):
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]
# Counter library!


def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
# It's slower than mine because it uses nested loops.
