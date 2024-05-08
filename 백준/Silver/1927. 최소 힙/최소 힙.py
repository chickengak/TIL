import sys
import heapq
n = int(input())
arr = []

for _ in range(n):
    if (x:=int(sys.stdin.readline())) == 0:
        try:
            print(heapq.heappop(arr))
        except IndexError:
            print(0)
    else:
        heapq.heappush(arr, x)
