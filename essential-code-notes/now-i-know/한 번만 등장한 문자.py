"""
https://school.programmers.co.kr/learn/courses/30/lessons/120896
"""


# My answer
def solution(s):
    return "".join(sorted(i for i in set(s) if s.count(i) == 1))
# I used a set. so I could reduce the number of loops.


# Others' answer
from collections import Counter

def solution(s):
    counter = Counter(s)
    unqiue_alphabets = filter(lambda alphabet: counter[alphabet] == 1, counter.keys())
    return ''.join(sorted(unqiue_alphabets))
# filter with lambda and collections library... I think it is very useless.
# But I have to know and lean about the collections library and the Counter method.

