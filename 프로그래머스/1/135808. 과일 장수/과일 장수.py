def solution(k, m, score):
    score_dict = {i:0 for i in range(k, 0,-1)}
    for s in score:
        score_dict[s] +=1
    answer = 0
    toss = 0
    for key, val in score_dict.items():
        share, remainder = divmod(val+toss, m)
        answer += key*m*share
        toss = remainder
    return answer