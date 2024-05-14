import sys
col, row = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
ones = []
zeros = 0
directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
cnt = 0

for r in range(row):
    for c in range(col):
        if mat[r][c] == -1:
            pass
        elif mat[r][c] == 1:
            ones.append((r, c))
        elif mat[r][c] == 0:
            zeros += 1

while ones:
    new_ones = set()
    flag = False
    for one in ones:
        for direction in directions:
            if (0 <= (y:= one[0]+direction[0]) < row) and (0 <= (x:= one[1]+direction[1]) < col) and mat[y][x] == 0:
                new_ones.add((y, x))
                mat[y][x] = 1
                zeros -= 1
                flag = True
    ones = list(new_ones)
    if flag: cnt += 1

if zeros > 0:
    print(-1)
else:
    print(cnt)
