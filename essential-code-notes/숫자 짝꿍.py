"""
https://school.programmers.co.kr/learn/courses/30/lessons/131128
"""


# My answer
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
# My code was the best one because it had a time complexity of O(2^n). And I got a fairly high score of 6 points.
# Following code was simply brought in to explore usage of the library.


# Others' answer
from collections import Counter
def solution(X, Y):
    x, y = list(X), list(Y)
    arr = []
    answer = ""

    c_x, c_y = Counter(x) , Counter(y)
    for key in c_x.keys():
        if key in c_y.keys():
            arr.append((int(key), min(c_x[key], c_y[key])))

    if not arr:
        return "-1"
    elif len(arr) == 1 and arr[0][0] == 0:
        return "0"

    arr = sorted(arr, key = lambda x : x[0], reverse= True)

    for ar in arr:
        answer += str(ar[0]) * int(ar[1])
    return answer


from collections import defaultdict
def solution(X, Y):
    d = defaultdict(int)
    temp = ''
    if len(X) < len(Y):
        X, Y = Y, X
    for i in X:
        d[i] += 1

    for j in Y:
        if d[j] > 0:
            d[j] -= 1
            temp += j
    if len(set(temp)) == 1 and temp[0] == '0':
        return '0'
    elif temp == '':
        return '-1'
    else:
        return ''.join(sorted(temp, reverse = True))

