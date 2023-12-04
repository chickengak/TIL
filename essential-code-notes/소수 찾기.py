"""
https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""


# My answer
from itertools import permutations

def solution1(numbers):
    n_list = list(numbers)
    cases = set()
    for i in range(1, len(numbers) + 1):
        for permu in list(permutations(n_list, i)):
            temp = ""
            for p in permu:
                temp += p
            cases.add(int(temp))
    cnt = 0
    for case in cases:
        if case == 0 or case==1:
            continue
        for i in range(2, int(case**0.5)+1):
            if case%i == 0:
                break
        else:
            cnt +=1
    return cnt
# 0.29sec. My code was the fastest code.


import math
def check_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True

number_set = set()
def permutation(base, array):
    if base:
        number_set.add(int(base))

    for i, s in enumerate(array):
        permutation(base + s, array[:i] + array[i+1:])

def solution2(numbers):
    permutation("", list(numbers))
    answer = len(list(filter(check_prime, number_set)))
    return answer
# 0.68sec. Interesting in permutation function.


