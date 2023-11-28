def solution(ingredient):
    cnt = 0
    l = []
    for i in ingredient:
        l.append(i)
        if l[-4:] == [1,2,3,1]:
            del l[-4:]
            cnt +=1
    return cnt