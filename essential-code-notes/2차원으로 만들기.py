"""
I
G
https://school.programmers.co.kr/learn/courses/30/lessons/120842
"""


# My answers
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        t_l = []
        for j in range(i, i+n):
            t_l.append(num_list[j])
        answer.append(t_l)
    return answer
#It's my first answer. and second is what I removed nested loop.


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

