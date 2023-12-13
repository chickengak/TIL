def solution(k, tangerine):
    tang_dict = dict()
    for tang in tangerine:
        try:
            tang_dict[tang] += 1
        except:
            tang_dict[tang] = 1
    tang_count = sorted(tang_dict.values(), reverse=True)
    answer = 0
    for tang in tang_count:
        k -= tang
        answer += 1
        if k < 1: break
        
    return answer