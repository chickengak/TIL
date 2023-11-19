def solution(array):
    a_dict = {}
    for i in set(array):
        a_dict.setdefault(i,0)
    for i in array:
        a_dict[i] += 1
    ad_max = max(a_dict.values())
    result = [k for k, v in a_dict.items() if v == ad_max]
    return result[0] if len(result) == 1 else -1
