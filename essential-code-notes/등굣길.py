"""
https://school.programmers.co.kr/learn/courses/30/lessons/42898
"""


# My answer
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
# 꽤 오래 걸린 문제다. 결국 아이디어를 찾지 못 해서 곁눈질 보기로 아이디어를 가져와 구현했다.
# list로 구현했을 땐, 그러니까 모든 경로의 경우의 수를 봐야하니까 list + BFS로 했을 땐,
# 연산이 너무 많아져서 시간초과가 떴다.
# 아이디어를 어떻게 하면 잘 끌어낼 지 고민해봐야 할 거 같다.


# Other's answer
def solution(m,n,puddles):
    grid = [[0]*(m+1) for i in range(n+1)] #왼쪽, 위로 한줄씩 만들어서 IndexError 방지
    if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
        for a, b in puddles:
            grid[b][a] = -1                #미리 -1로 체크
    grid[1][1] = 1
    for j in range(1,n+1):
        for k in range(1,m+1):
            if j == k == 1:                #(1,1)은 1로 만들어두고, 0이 되지 않도록
                continue
            if grid[j][k] == -1:           #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
                grid[j][k] = 0
                continue
            grid[j][k] = (grid[j][k-1] + grid[j-1][k])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식

    return grid[n][m]
