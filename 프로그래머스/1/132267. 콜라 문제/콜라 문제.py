def solution(a, b, n):
    free = 0
    while True:
        share, t = divmod(n, a)
        free += share*b
        n = share*b + t
        if share == 0 :
            #free += int(t)
            break
    return free