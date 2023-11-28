def solution(keymap, targets):
    dic = {}
    for i in range(65, 91):
        dic.update({chr(i): None})

    for key in keymap:
        for i, v in enumerate(key):
            try:
                if dic[v] > i:
                    dic[v] = i
            except:
                dic[v] = i

    res = []
    for target in targets:
        sum_k = 0
        for t in target:
            try:
                sum_k += dic[t]
            except:
                res.append(-1)
                break
        else:
            res.append(sum_k + len(target))
    return res