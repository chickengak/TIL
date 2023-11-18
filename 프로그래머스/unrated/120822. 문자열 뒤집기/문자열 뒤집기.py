def solution(str):
    t =""
    for i in range(len(str)-1, -1, -1):
        t += str[i]
    return t