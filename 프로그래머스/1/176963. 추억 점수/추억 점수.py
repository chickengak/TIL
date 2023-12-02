def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    for p in photo:
        temp = 0
        for person in p:
            try:
                temp += dic[person]
            except:
                continue
        answer.append(temp)
    return answer