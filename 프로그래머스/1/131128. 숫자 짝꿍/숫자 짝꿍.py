def solution(X, Y):
    dic ={"9":[0, 0], "8":[0, 0], "7":[0, 0], "6":[0, 0], "5":[0, 0], "4":[0, 0], "3":[0, 0], "2":[0, 0], "1":[0, 0], "0":[0, 0]}
    for i in str(X):
        dic[i][0] +=1
    for i in str(Y):
        dic[i][1] += 1
    ans = ""
    for k, v in dic.items():
        ans += k*min(v)
    return "-1" if len(ans) == 0 else "0" if len(ans) == min(dic["0"]) else ans