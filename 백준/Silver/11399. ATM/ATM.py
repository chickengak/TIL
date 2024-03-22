n = int(input())
people = sorted(map(int, input().split()))
answer = 0
for idx, val in enumerate(people):
    answer += (n - idx) * val
print(answer)