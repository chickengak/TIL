from math import factorial

def solution(n, k):
    answer = []
    nums = list(range(1, n+1))
    f = factorial(n-1)
    n_ = n - 1
    k_ = k - 1
    while True:
        share, remainder = divmod(k_, f)
        answer.append(nums.pop(share))
        if f == 2:
            if remainder:
                answer += nums[::-1]
            else:
                answer += nums
            break
        f = f // n_
        n_ -= 1
        k_ = remainder
    
    return answer