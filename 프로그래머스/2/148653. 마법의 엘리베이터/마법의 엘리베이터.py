def solution(storey):
    rstorey = str(storey)[::-1]
    idx = 0
    answer = 0
    while idx < len(rstorey):
        num = int(rstorey[idx])
        if num <= 4:
            answer += num
            storey -= num * 10**idx
        elif num >= 6:
            answer += (10 - num)
            storey += (10 - num) * 10**idx
        else:  # num == 5
            if idx == len(rstorey)-1: # 맨 앞이 5
                answer += num
                storey -= num * 10 ** idx
            else:
                if (int(rstorey[idx+1]) <= 4) or (idx+1 == len(rstorey)-1 and rstorey[idx+1] == 5):
                    answer += num
                    storey -= num * 10**idx
                else:
                    answer += (10 - num)
                    storey += (10 - num) * 10 ** idx
        rstorey = str(storey)[::-1]
        idx += 1
    return answer