def solution(n):
    g, n = divmod(n, 5)
    a, n = divmod(n, 3)
    return g + a + n