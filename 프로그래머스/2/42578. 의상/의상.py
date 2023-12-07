from math import factorial

def solution(clothes):
    dic = dict()
    for c in clothes:
        try:
            dic[c[1]].append(c[0])
        except:
            dic[c[1]] = [c[0]]
    ans = 1
    for k in dic:
        ans*=(len(dic[k])+1)
            
    return ans-1