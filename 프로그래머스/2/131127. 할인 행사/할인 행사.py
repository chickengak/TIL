def solution(want, number, discount):
    target = dict(zip(want,number))
    want_dict = {w:0  for w in want}
    answer = 0
    for i in range(len(discount)):
        try:
            want_dict[discount[i]] += 1
        except:
            pass
        if i>9:
            try:
                want_dict[discount[i-10]] -=1
            except:
                pass
        if want_dict == target:
            answer +=1
    return answer