from math import ceil

def solution(n, t):
    temp = ceil(t/n)-(n//2)
    return list(range(temp, temp+n))