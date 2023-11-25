def solution(n):
    m = 0
    res = 0
    while not m == n:
        m += 1
        res += 1
        while (not res % 3) | ("3" in str(res)) :
            res += 1
    return res