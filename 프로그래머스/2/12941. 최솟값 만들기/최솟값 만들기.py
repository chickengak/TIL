def solution(A,B):
    return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True)))