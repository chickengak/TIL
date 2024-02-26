n, kim, lim = map(int, input().split())

cnt = 0
while True:
    if kim == lim:
        print(cnt)
        break
    kim -= kim//2
    lim -= lim//2
    cnt += 1