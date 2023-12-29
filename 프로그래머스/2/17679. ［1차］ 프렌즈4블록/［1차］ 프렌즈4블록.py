def solution(m, n, board):
    answer = 0
    #myboard =[[0]*m]*n
    myboard =  [ [0]*m for _ in range(n)]
    for i in range(m): # 높이 row
        for j in range(n): # col
            myboard[j][-1-i] = board[i][j]
    
    go = True
    erase = set()
    while go:
        go = False
        for i in range(1, n):
            for j in range(len(myboard[i])-1, 0, -1):
                try:
                    if myboard[i][j] == myboard[i-1][j] == myboard[i][j-1] == myboard[i-1][j-1]:
                        erase.add((i,j))
                        erase.add((i-1,j))
                        erase.add((i,j-1))
                        erase.add((i-1,j-1))
                except:
                    continue
        else:
            answer += len(erase)
            for r, c in sorted(list(erase), key= lambda x : (x[0], -x[1])):
                myboard[r].pop(c)
                go = True
            erase = set()

    return answer