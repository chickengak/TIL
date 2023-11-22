def solution(s):
    s_l = s.split()
    t = None
    sum = 0
    for i in s_l:
        if i != "Z":
            t = int(i)
            sum += t
        else:
            sum -= t
    return sum