"""
https://school.programmers.co.kr/learn/courses/30/lessons/76501
"""


# My answer
def solution(absolutes, signs):
    return sum(absolutes[i] if signs[i] else absolutes[i]*-1 for i in range(len(signs)))


# Others' answer
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
# I think it's a nice use of zip. I haven't used this often. Now I will use it appropriately.

