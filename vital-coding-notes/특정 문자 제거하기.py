"""
Input: string, letter
Goal: Remove the letter from the string
"""


# My answer
def solution(string, l):
    return "".join([i for i in list(string) if i != l])


# Others' answer
def solution(my_string, letter):
    return my_string.replace(letter, '')
    # We can use .replace