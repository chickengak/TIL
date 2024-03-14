n = int(input())
mat = [list(input()) for _ in range(n)]

connected = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if mat[j][k] == "Y" or (mat[j][i] == "Y" and mat[i][k] == "Y"):
                connected[j][k] = 1

answer = 0
for row in connected:
    answer = max(answer, sum(row))
print(answer)
