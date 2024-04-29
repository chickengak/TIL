n = int(input())
branches = dict()
for _ in range(int(input())):
    s, e = list(map(int, input().split()))
    try:
        branches[s].append(e)
    except:
        branches[s] = [e]
    try:
        branches[e].append(s)
    except:
        branches[e] = [s]

ans = -1
check = [0] * (n+1)
visit = [1]
next_visit = set()
while visit:
    for v in visit:
        if check[v] == 0:
            check[v] = 1
            ans += 1
            try:
                next_visit.update(branches[v])
            except:
                pass
    visit = list(next_visit)
    next_visit = set()

print(ans)