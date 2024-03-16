n_row, m_col = list(map(int, input().split()))
mat = [list(map(int, list(input()))) for _ in range(n_row)]

max_len = min(n_row, m_col)
answer = 1
finished = False
for cur_len in range(max_len, 1, -1):
    for row in range(n_row-cur_len+1):
        for col in range(m_col-cur_len+1):
            if mat[row][col] == mat[row+cur_len-1][col] == mat[row][col+cur_len-1] == mat[row+cur_len-1][col+cur_len-1]:
                answer = cur_len
                finished = True
                break
        if finished: break
    if finished: break
print(answer**2)