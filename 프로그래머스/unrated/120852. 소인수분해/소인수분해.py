def solution(n):
    res = set()
    d = 2
    while d <= n:
        if n % d == 0:
            res.add(d)
            n = n / d
        else:
            d = d + 1
    return sorted(list(res))