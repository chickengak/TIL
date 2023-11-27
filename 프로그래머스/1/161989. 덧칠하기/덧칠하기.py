def solution(n, m, section):
    t = 0
    cnt = 0
    for i in section:
        if i > t:
            cnt += 1
            t = i+m-1
    return cnt