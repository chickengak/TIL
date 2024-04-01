import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

answer = 0
for coin in reversed(coins):
    share = k // coin
    answer += share
    k = k - (share * coin)
    if k == 0:
        break
        
print(answer)