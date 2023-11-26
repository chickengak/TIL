"""
I
G
https://school.programmers.co.kr/learn/courses/30/lessons/120860
"""


# My answer
def solution(dots):
    x = max(dots[0][0], dots[1][0], dots[2][0]) - min(dots[0][0], dots[1][0], dots[2][0])
    y = max(dots[0][1], dots[1][1], dots[2][1]) - min(dots[0][1], dots[1][1], dots[2][1])
    return abs(x * y)


# Others' answer
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
# My code utilized the constraint that only four dots are input.
# Of course, since a rectangle has four dots, I made good use of it.
# However, I should be aware that there is also such a method.
