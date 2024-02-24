n, m = map(int, input().split())
mat = []
answers = []
 
for _ in range(n):
    mat.append(input())
 
for i in range(n-7):
    for j in range(m-7):
        case1 = 0
        case2 = 0
 
        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row + col) % 2 == 0:
                    if mat[row][col] != 'B':
                        case1 += 1
                    if mat[row][col] != 'W':
                        case2 += 1
                else:
                    if mat[row][col] != 'W':
                        case1 += 1
                    if mat[row][col] != 'B':
                        case2 += 1
 
        answers.append(case1)
        answers.append(case2)
 
print(min(answers))