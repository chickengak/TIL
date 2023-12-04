from itertools import permutations

def solution(k, dungeons):
    cases = list(permutations(dungeons, len(dungeons)))
    maximum = 0
    for case in cases:
        case_k = k
        cnt = 0
        for c in case:
            if case_k >= c[0]:
                case_k -= c[1]
                cnt +=1
            else:
                maximum = max(maximum, cnt)
                break
        else:
            return cnt
    return maximum