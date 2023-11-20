"""
Input: a string (with only alphabet)
Goal: Swap upper cases and lower cases
"""


# My answer
def solution(my_stirng):
    answer = ""
    for i in my_stirng:
        if i.islower(): answer += i.upper()
        else: answer +=i.lower()
    return answer


# Others' answer
def solution(my_string):
    return my_string.swapcase()
# .swapcase()
