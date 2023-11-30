def solution(s):
    s = [int(i) for i in s.split()]
    return f"{min(s)} {max(s)}"