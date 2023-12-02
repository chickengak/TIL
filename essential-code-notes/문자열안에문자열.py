"""
I: two strings.     (1 <= two strings' length <= 100)
G: If str2 is in str1, return 1. Otherwise, return 2.
https://school.programmers.co.kr/learn/courses/30/lessons/120908
"""


# My answer
def solution1(str1, str2):
    return (str2 in str1)*-1+2
# in operater is as fast as 25% faster than not in operater


# Others' answer
def solution2(str1, str2):
    return 1 + int(str2 not in str1)
# It is slower than mine.
