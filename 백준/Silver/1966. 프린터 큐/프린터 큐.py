from collections import deque
for _ in range(tcases:=int(input())):
    n, m = list(map(int, input().split()))

    q1 = deque(map(int, input().split()))
    q2 = deque(range(len(q1)))
    length = len(q1)

    while True:
        maximum = max(q1)
        while q1[0] != maximum:
            q1.append(q1.popleft())
            q2.append(q2.popleft())

        q1.popleft()
        if q2.popleft() == m:
            print(length - len(q1))
            break