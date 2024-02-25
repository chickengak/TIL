n, m = map(int, input().split())
sales = []
min_whole = 1001
min_item = 1001
for _ in range(m):
    mw, mi = map(int, (input().split()))
    if mw < min_whole:
        min_whole = mw
    if mi < min_item:
        min_item = mi

calcs = []
share, remainder = divmod(n, 6)
calcs.append((share+1 if remainder else share)*min_whole)
calcs.append(min_whole*share + min_item*remainder)
calcs.append(n*min_item)

print(min(calcs))