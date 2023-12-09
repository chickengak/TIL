from math import gcd

def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm *= int(arr[i]/gcd(lcm, arr[i]))
    return lcm