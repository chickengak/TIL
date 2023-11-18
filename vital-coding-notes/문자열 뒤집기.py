def my_solution(str):
    t =""
    for i in range(len(str)-1, -1, -1):
        t += str[i]
    return t


def solution(my_string):
    return ''.join(list(reversed(my_string)))

def solution(my_string):
    return my_string[::-1]