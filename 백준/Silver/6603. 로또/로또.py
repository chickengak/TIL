from itertools import combinations
while True:
    nums = list(map(int, input().split()))

    if len(nums) == 1:
        break
    k = nums[0]
    s = nums[1:]
    answers = list(combinations(s, 6))
    for ans in answers:
        print(*ans)
    print()