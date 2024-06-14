import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())

result = list(combinations(range(1, n+1), m))
for res in result:
    print(*res)