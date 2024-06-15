import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = [list(map(int,list(input().strip()))) for _ in range(n)]
b = [list(map(int,list(input().strip()))) for _ in range(n)]

def flip(x,y):
    for ii in range(3):
        for jj in range(3):
            a[x+ii][y+jj] = 1 - a[x+ii][y+jj]
def sol():
    if a == b:
        return 0

    cnt = 0
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                flip(i,j)
                cnt += 1

            if a == b:
                return cnt
    return -1

print(sol())
