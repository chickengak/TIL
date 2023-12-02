"""
I: a list of integers and n
G: Return a list containing the input integers up to n
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
# 0.023 sec.
# This is my first answer. And the second one is without the nested loop.


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
# 0.013 sec.
# My second answer is using the slicing. So I reduced the use of the append method.
