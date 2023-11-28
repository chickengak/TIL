from math import sqrt
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        sq = sqrt(i)
        if sq != int(sq):
            answer += i
        else:
            answer -= i
    return answer