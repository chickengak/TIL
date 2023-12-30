"""
https://school.programmers.co.kr/learn/courses/30/lessons/17679
"""


# My answer
def solution(m, n, board):
    answer = 0
    # myboard =[[0]*m]*n
    myboard = [[0] * m for _ in range(n)]
    for i in range(m):  # 높이 row
        for j in range(n):  # col
            myboard[j][-1 - i] = board[i][j]

    go = True
    erase = set()
    while go:
        go = False
        for i in range(1, n):
            for j in range(len(myboard[i]) - 1, 0, -1):
                try:
                    if myboard[i][j] == myboard[i - 1][j] == myboard[i][j - 1] == myboard[i - 1][j - 1]:
                        erase.add((i, j))
                        erase.add((i - 1, j))
                        erase.add((i, j - 1))
                        erase.add((i - 1, j - 1))
                except:
                    continue
        else:
            answer += len(erase)
            for r, c in sorted(list(erase), key=lambda x: (x[0], -x[1])):
                myboard[r].pop(c)
                go = True
            erase = set()

    return answer
# myboard =[[0]*m]*n 마이보드를 이따구로 만들었더니 모든 row들이 다 같은 주소를 참조하는 사고가 발생했다.
# 앞으로 매우 주의해야할 거 같다.


# Other's answer
def solution(m, n, board):
    board.reverse()
    field = [list(cols) for cols in zip(*board)]
    answer = 0

    while True:
        bomb = set()
        for row in range(n - 1):
            for col in range(m - 1):
                try:
                    if field[row][col] == field[row + 1][col] == field[row][col + 1] == field[row + 1][col + 1]:
                        bomb.update({(row, col), (row + 1, col), (row, col + 1), (row + 1, col + 1)})
                except:
                    break

        if not len(bomb):
            break

        for r, c in bomb:
            field[r][c] = ''
            answer += 1

        for row in range(n):
            field[row] = list(''.join(field[row]))

    return answer
# 개념은 같으나 리스트로 바꾸는 효율이 좋고, update를 사용했기 때문에 add 4번보다 빨랐다.

