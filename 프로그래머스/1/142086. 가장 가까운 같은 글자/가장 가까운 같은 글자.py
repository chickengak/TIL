def solution(s):
    d = {}
    res = []
    for i in range(len(s)):
        if s[i] in d:
            res.append(i-d[s[i]])
            d[s[i]] = i
        else:
            res.append(-1)
            d[s[i]] = i
    return res