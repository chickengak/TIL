def solution(operations):
    answer = []
    for operation in operations:
        temp = operation.split()
        if temp[0] == 'I':
            answer.append(int(temp[1]))
        else:
            if temp[1] == '1':
                try:
                    answer.remove(max(answer))
                except:
                    continue
            else:
                try:
                    answer.remove(min(answer))
                except:
                    continue
    return [max(answer), min(answer)] if len(answer) else [0,0]