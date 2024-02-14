"""
I: a string.
G: Revert the given string.
https://school.programmers.co.kr/learn/courses/30/lessons/120822
"""


# My answer
def solution1(str):
    t =""
    for i in range(len(str)-1, -1, -1):
        t += str[i]
    return t
# 0.01sec. Yes, now I know it is very petty code. It uses so many += operator.


# Others' answer
def solution2(my_string):
    return ''.join(list(reversed(my_string)))
# 0.0075sec. It is slower than following.

def solution3(my_string):
    return my_string[::-1]
# 0.003sec. It is the fastest code.
