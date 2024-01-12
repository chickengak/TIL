def solution(new_id):

    answer = ''

    for c in new_id:
        temp = ord(c)
        if 64 < temp < 91:
            answer += chr(temp+32)
        elif (96 < temp < 123) or (47 < temp < 58) or (temp in [45, 95] ):
            answer += c
        elif temp == 46:
            if answer[-1:] != c:
                answer += c
    if answer and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 15:
        answer = answer[:15]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) < 3:
        if len(answer) <2:
            if len(answer) <1:
                return 'aaa'
            return answer + answer[-1]*2
        return answer + answer[-1]
    return answer