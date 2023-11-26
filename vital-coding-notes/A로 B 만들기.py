"""
I
G
https://school.programmers.co.kr/learn/courses/30/lessons/120886
"""


# My answer
def solution(before, after):
    l = list(after)
    for i in before:
        try:
            l.remove(i)
        except:
            return 0
    return 1
# I got a pretty high score of 4 points.
# It doesn't seem bad to me either. Nice use of try & except.
