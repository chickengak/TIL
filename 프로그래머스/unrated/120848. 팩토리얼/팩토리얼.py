def solution(n):
    m = 1
    res = 1
    for i in range(2, n+1):
        if m*i > n:
            break
        else:
            m *= i
            res = i
    return res