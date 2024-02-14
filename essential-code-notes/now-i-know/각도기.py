"""
I: an integer representing an angle.  0 < a <= 180
G: Return 1 for an acute angle, 2 for a right angle, 3 for an obtuse angle, and 4 for a straight angle.
https://school.programmers.co.kr/learn/courses/30/lessons/120829
"""



def solution(a):
    if a < 90: return 1
    elif a==90: return 2
    elif a<180: return 3
    else: return 4


def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer
# Mathematics
