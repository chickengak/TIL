"""
I
G
"""


# My answer
def solution(age):
    return "".join(chr(ord(i)+49) for i in str(age))


# Others' answer
import string
def solution(age):
    return "".join(map(lambda v: string.ascii_lowercase[int(v)], str(age)))


def solution(age):
    aa = str(age)
    return aa.translate(str.maketrans('0123456789', 'abcdefghij'))


