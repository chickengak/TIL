n = int(input())
mat = [[0]*101 for _ in range(101)]
total = 0

for _ in range(n):
    x, y = list(map(int, input().split()))

    for y_ in range(10):
        for x_ in range(10):
            if mat[y + y_][x + x_] == 0:
                total += 1
                mat[y + y_][x + x_] = 1

print(total)