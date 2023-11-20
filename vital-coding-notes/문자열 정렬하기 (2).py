"""
I
G
"""


# My answer
def solution(my_string):
    s_list = list(my_string.lower())
    s_list.sort()
    return "".join(i for i in s_list)


# Others' answer
def solution(my_string):
    return ''.join(sorted(my_string.lower()))

