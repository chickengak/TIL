from collections import deque

n, k = list(map(int, input().split()))

dq = deque(range(1, n + 1))
answer = []

while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())
    answer.append(dq.popleft())

print('<', end='')
print(*answer, sep=', ', end='>')