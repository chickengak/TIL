def solution(n):
    if n < 100000: return n
    elif n < 300000: return int(n*0.95)
    elif n < 500000: return int(n*0.9)
    else: return int(n*0.8)
