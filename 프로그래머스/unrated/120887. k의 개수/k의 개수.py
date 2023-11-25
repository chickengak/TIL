def solution(a, b, k):
    ans = 0
    k = str(k)
    for i in range(a, b + 1):
        ans += str(i).count(k)
    return ans