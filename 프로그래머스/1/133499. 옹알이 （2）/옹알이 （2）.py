def solution(babbling):
    dic = { "aya":"+", "ye":"-", "woo":"*", "ma":"/"}
    cnt = 0
    for b in babbling:
        for d in dic:
            b = b.replace(d, dic[d])
        if ("++" in b) | ("--" in b) | ("**" in b) | ("//" in b):
            continue
        for dv in dic.values():
            b = b.replace(dv, "")
        if b == "":
            cnt += 1
    return cnt