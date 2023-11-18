def solution(a):
    if a < 90: return 1
    elif a==90: return 2
    elif a<180: return 3
    else: return 4


def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer