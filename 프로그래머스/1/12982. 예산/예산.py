def solution(d, budget):
    sum_d = 0
    cnt = 0
    for i in sorted(d):
        sum_d += i
        if sum_d > budget:
            return cnt
        cnt += 1
    return cnt
