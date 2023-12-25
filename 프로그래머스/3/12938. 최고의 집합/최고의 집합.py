def solution(n, s):
    if n > s:
        return [-1]
    share = s//n
    answer = [share] * n
    for i in range(n-1, n-1-s%n, -1):
        answer[i] += 1
    return answer