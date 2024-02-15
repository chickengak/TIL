"""
Input: a list of integers   ( 1 <= len(list) <= 1000 , 0 <= integer <= 1000 )
Goal: Reverse the list
https://school.programmers.co.kr/learn/courses/30/lessons/120821
"""


# My answer
def solution(num_list):
    res = []
    while num_list:
        res += [num_list.pop()]
    return res


# Ohters' answer
def solution(num_list):
    return num_list[::-1]
    # I didn't know :: in list index. But now I can apply it.


def solution(num_list):
    num_list.reverse()
    return num_list
    # Same here
