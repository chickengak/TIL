n, m = list(map(int, input().split()))
picks = list(map(int, input().split()))
nums = list(range(1, n+1))

answer = 0
cur_idx = 0
for pick in picks:
    idx = nums.index(pick)
    dif = abs(idx - cur_idx)
    if dif > len(nums)//2:
        dif = len(nums) - dif
    answer += dif
    nums.pop(idx)
    if idx < len(nums):
        cur_idx = idx
    else:
        cur_idx = 0
print(answer)