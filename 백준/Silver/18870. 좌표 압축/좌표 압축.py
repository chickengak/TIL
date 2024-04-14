n = input()
nums = list(map(int, input().split()))
nums_dict = dict()

for idx, value in enumerate(sorted(set(nums))):
    nums_dict[value] = idx

print(*[nums_dict[num] for num in nums], sep=' ')