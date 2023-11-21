def solution(emergency):
    temp = []
    for idx, val in enumerate(emergency):
        temp.append((idx, val))
    temp.sort(key=lambda x: x[1])
    length = len(temp)
    return [length-i[0] for i in temp]