def solution(my_string):
    s_list = list(my_string.lower())
    s_list.sort()
    return "".join(i for i in s_list)