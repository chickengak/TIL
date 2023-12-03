def solution(s):
    cnt = 0
    cnt_0 = 0
    
    while s != "1":
        cnt_1 = s.count("1")
        cnt_0 += len(s) - cnt_1
        s = bin(cnt_1)[2:]
        cnt += 1
        
    return [cnt, cnt_0]