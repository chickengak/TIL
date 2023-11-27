"""
I
G
https://school.programmers.co.kr/learn/courses/30/lessons/120864
"""


# My answer
def solution(my_string):
    temp = []
    check = False
    for i in my_string:
        if i.isdigit():
            if check:
                temp[-1] = temp[-1] + i
            else:
                temp.append(i)
                check = True
        else:
            check = False
    return  sum(int(i) for i in temp)
# I got a pretty high score of 6 points!


# Othes' answer
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())
# This code is changing the string.


import re
def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])
# re library? I have to check this out.

