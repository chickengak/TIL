def solution(t, p):
    start = p[0]
    l_p = len(p)
    cnt = 0
    for i in range(len(t)-l_p+1):
        if t[i] <= start:
            if t[i:i+l_p] <= p:
                cnt += 1
    return cnt