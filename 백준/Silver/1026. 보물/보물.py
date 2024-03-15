_ = input()
a = sorted(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0
while a:
    answer += a.pop() * b.pop(b.index(min(b)))
print(answer)