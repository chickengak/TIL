"""
I
G
https://school.programmers.co.kr/learn/courses/30/lessons/120884
"""


# My answer
def solution(chicken):
    free_chicken = 0
    share = chicken
    remainder = 0
    while share:
        share, t = divmod(share, 10)
        free_chicken += share
        remainder += t
        if remainder > 9:
            free_chicken += 1
            remainder -= 9
    return free_chicken


# Others' answer
def solution(chicken):
    return int(chicken*0.11111111111)


def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer