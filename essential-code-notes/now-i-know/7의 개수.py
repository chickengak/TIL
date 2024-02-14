"""
I: a list of integers
G: Find all "7" in integers
https://school.programmers.co.kr/learn/courses/30/lessons/120912
"""


# My answer
def cnt7(n):
    share, remainder = divmod(n, 10)
    if share > 0:
        return 1 + cnt7(share) if remainder == 7 else cnt7(share)
    else:
        return 1 if remainder == 7 else 0

def solution(array):
    return sum(cnt7(i) for i in array)
# 0.022sec. I used recursion and mathematics.


# Others' answer
def solution(array):
    return str(array).count('7')
# 0.01sec.
# But there was such a simple answer. It converted list to str and counted 7.
