"""
I: a string.
G: Change the given string to lowercase. And return it sorted.
https://school.programmers.co.kr/learn/courses/30/lessons/120911
"""


# My answer
def solution1(my_string):
    s_list = list(my_string.lower())
    s_list.sort()
    return "".join(i for i in s_list)
# I thought the running time of these two answers would be almost the same.
# But the running time of these two answers differed by twice as much.
# I should be more more careful when coding in the future.
# running time = 0.025


# Others' answer
def solution2(my_string):
    return ''.join(sorted(my_string.lower()))
# running time = 0.012


