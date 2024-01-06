def solution(n):
    answer = 1
    pre = 1
    for _ in range(1, n):
        temp = answer
        answer = (answer + pre) % 1000000007
        pre = temp
    return answer