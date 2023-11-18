def solution(n):
    answer = 0
    for i in range(n, 1, -1):
        if not i%2:
            print(i)
            answer += i
    return answer

def solution(n):
    return sum([i for i in range(2, n + 1, 2)])

def solution(n):
    return (n//2)*((n//2)+1)