def solution(score):
    sc_sum = [(n, sum(m)) for n, m in enumerate(score)]
    sc_sum.sort(key=lambda x:x[1], reverse=True)
    temp_v = None
    temp_r = None
    idx = 0
    for i, v in sc_sum:
        idx += 1
        if v != temp_v:
            score[i] = idx
            temp_v = v
            temp_r = idx
        else:
            score[i] = temp_r
    return score
