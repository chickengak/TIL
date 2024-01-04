def solution(m, n, puddles):
    board = [[0 for _ in range(m)] for _ in range(n)]
    for x,y in puddles:
        board[y - 1][x - 1] = -1
    #print(board)
    board[0][0]=1
    for y in range(n):
        for x in range(m):
            if board[y][x] == -1:
                continue
            if y+1 < n and board[y+1][x] != -1:
                board[y+1][x] += board[y][x]
            if x+1 < m and board[y][x+1] != -1:
                board[y][x+1] += board[y][x]
                
    return board[-1][-1] % 1000000007