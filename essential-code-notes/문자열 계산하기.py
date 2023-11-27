"""
I:
G:
https://school.programmers.co.kr/learn/courses/30/lessons/120902
"""


# My answer
def solution(my_string):
    s_list = [int(i) if i.isdigit() else i for i in my_string.split()]
    res = s_list[0]
    for i in range(1, len(s_list), 2):
        if s_list[i] == "+":
            res += s_list[i+1]
        else:
            res -= s_list[i+1]
    return res


# Others' answers
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))


solution=eval

