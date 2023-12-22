def solution(dartResult):
    is_num = True
    scores = []
    digit = ''
    for d in dartResult:
        if d.isdigit():
            if not is_num:
                try:
                    if int(digit):
                        scores.append(digit)
                except:
                    pass
                digit = ''
            digit += d
            is_num = True
        elif is_num and (not d.isdigit()):
            is_num = False
            digit = int(digit)
            if d == 'D':
                digit = digit ** 2
            elif d == 'T':
                digit = digit ** 3
        else:
            if d == '#':
                digit *= -1
            else:
                if len(scores):
                    scores[-1] *= 2
                digit *= 2
    else:
        scores.append(digit)

    return sum(scores)