def solution(n):
    s = 0
    for i in range(9, n+1, 2):
        for j in range(3, int(n**0.5)+1, 2):
            if i%j == 0 and i != j:
                s += 1
                break
    return max(s + (n//2) -1, 0)