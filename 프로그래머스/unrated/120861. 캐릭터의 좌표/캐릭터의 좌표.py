def solution(keyinput, board):
    pos = [0, 0]
    x_max, y_max = board[0]//2, board[1]//2
    for i in keyinput:
        if i == "left":
            pos[0] -= 1 if pos[0] > x_max*-1 else 0
        elif i == "up":
            pos[1] += 1 if pos[1] < y_max else 0
        elif i == "down":
            pos[1] -= 1 if pos[1] > y_max*-1 else 0
        else:
            pos[0] += 1 if pos[0] < x_max else 0
    return pos