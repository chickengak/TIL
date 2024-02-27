directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
mat = [[0]*n for _ in range(n)]

for _ in range(k:=int(input())):
    row, col = map(int, input().split())
    mat[row-1][col-1] = 'A'

temp_commands = []
cur_d = 0
for _ in range((L:=int(input()))):
    seconds, d = input().split()
    temp_commands.append((int(seconds), (cur_d := (cur_d+1)%4) if d=='D' else (cur_d := (cur_d+3)%4)))

commands = []
commands.append((temp_commands[0][0], 0))
for i in range(len(temp_commands)-1):
    commands.append((temp_commands[i+1][0] - temp_commands[i][0], temp_commands[i][1]))
commands.append((100, temp_commands[-1][1]))

mat[0][0] = 1
length = 1
runnig_time = 1
y, x = 0, 0
finish = False

for t, d in commands:
    while t:
        runnig_time += 1
        r, c = y + directions[d][0] ,  x + directions[d][1]
        if r < 0 or c < 0 or r == n or c == n:
            finish = True
            break

        if mat[r][c] == 'A':
            length += 1
        elif mat[r][c] >= runnig_time - length:
            finish = True
            break
        mat[r][c] = runnig_time
        y, x = r, c
        t -= 1
    if finish: break

print(runnig_time - 1)