"""
Input: a string
Goal: Return the sum of single-digit natural numbers in a string
"""


# My answer
def solution(string):
    sum = 0
    for i in string:
        if 47 < ord(i) < 58:
            sum += int(i)
    return sum


# Others' answer
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
# isdigit function


def solution(my_string):
    answer = 0
    for c in my_string:
        if c.isnumeric():
            answer += int(c)
    return answer
# isnumeric function


def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except:
            pass

    return answer
# try except

