def solution(n):
    cnt_n = bin(n).count("1")
    
    while True:
        n += 1
        cnt = bin(n).count("1")
        if cnt == cnt_n:
            return n
