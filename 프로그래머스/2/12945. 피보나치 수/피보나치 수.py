def solution(n):
    a = 0
    b = 1
    chk = True
    for i in range(n-1):
        if chk:
            a += b
            chk = False
        else:
            b += a
            chk = True
    return b%1234567 if chk else a%1234567