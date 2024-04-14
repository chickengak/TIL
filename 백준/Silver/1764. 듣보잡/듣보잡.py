n, m = map(int, input().split())
n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())

for _ in range(m):
    m_set.add(input())

res = sorted(n_set & m_set)
print(len(res), *res, sep='\n')