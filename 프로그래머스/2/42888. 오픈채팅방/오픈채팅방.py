def solution(record):
    answer = []
    dic = dict()
    passes = []
    for i in range(len(record)-1,-1,-1):
        rec = record[i].split()
        if (rec[1] not in dic) and (rec[0] != 'Leave') :
            dic[rec[1]] = rec[2]
        if rec[0] != 'Change':
            passes.append([rec[0], rec[1]])
    
    for i in range(len(passes)-1, -1,-1):
        if passes[i][0] == 'Enter':
            answer.append(f"{dic[passes[i][1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{dic[passes[i][1]]}님이 나갔습니다.")

    return answer