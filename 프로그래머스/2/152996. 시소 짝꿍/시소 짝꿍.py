from collections import Counter

def solution(weights):
    answer = 0
    wdict = Counter(weights)
    for k, v in wdict.items():
        if v > 1:
            answer += v*(v-1)/2
        if wdict[k/2]:
            answer += v*wdict[k/2]
        if wdict[k/3*2]:
            answer += v*wdict[k/3*2]
        if wdict[k/4*3]:
            answer += v*wdict[k/4*3]
    return answer