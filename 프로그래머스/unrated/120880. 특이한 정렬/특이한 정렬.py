def solution(numlist, n):
    nums = []
    for v in numlist:
        nums.append([v, abs(v-n), v > n])
    nums.sort(key=lambda x: (x[1], -x[2]))
    return [i[0] for i in nums]