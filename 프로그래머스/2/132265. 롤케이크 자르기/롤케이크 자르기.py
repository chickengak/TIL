def solution(topping):
    answer = 0
    right = set()
    dic = dict()
    for i in range(len(topping)):
        try:
            dic[topping[i]] += 1
        except:
            dic[topping[i]] = 1
    
    for i in range(len(topping)-1, 0, -1):
        right.add(topping[i])
        if dic[topping[i]] == 1:
            del(dic[topping[i]])
        else:
            dic[topping[i]] -= 1
        
        if len(dic) == len(right):
            answer += 1
    return answer