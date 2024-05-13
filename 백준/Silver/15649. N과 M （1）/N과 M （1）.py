import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
answer = list(permutations(range(1, n + 1), m))

for ans in answer:
    print(*ans, sep=' ')