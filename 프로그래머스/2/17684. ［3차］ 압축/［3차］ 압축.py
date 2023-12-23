def solution(msg):
    dic = dict()
    for i in range(1,27):
        dic[chr(i+64)] = i
    start = 0
    end = 1
    answer = []
    finish = False
    while not finish:
        temp = msg[start:end]
        while temp in dic:
            if end < len(msg):
                end+=1
                temp = msg[start:end]
                continue
            finish = True
            break
        # end 까지 자르면 없음. or end가 맨끝임.
        if not finish:
            answer.append(dic[msg[start:end-1]])
        else:
            answer.append(dic[msg[start:end]])
            break
        dic[temp] = len(dic)+1
        start = end-1
    return answer