direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def check_field(board, x, y, col, row):
    cur_nodes = {(y, x)}
    while cur_nodes:
        next_nodes = set()
        for y, x in cur_nodes:
            board[y][x] = 0
            for y_, x_ in direction:
                if (0 <= x + x_ < col) and (0 <= y + y_ < row) and board[y + y_][x + x_] == 1:
                    board[y + y_][x + x_] = 0
                    next_nodes.add((y + y_, x + x_))
        cur_nodes = next_nodes
    return


tcase = int(input())

for _ in range(tcase):
    col, row, cabbage = [int(i) for i in input().split()]
    board = [[0] * col for _ in range(row)]
    for _ in range(cabbage):
        x, y = [int(i) for i in input().split()]
        board[y][x] = 1

    answer = 0
    for y in range(row):
        for x in range(col):
            if board[y][x] == 1:
                check_field(board, x, y, col, row)
                answer += 1
    print(answer)