import numpy as np
global board
def recursive(x_start, x_end, y_start, y_end):
    if sum(sum(board[y_start:y_end, x_start:x_end])) == (x_end-x_start)**2: # 1로 차있다면
        return np.array([0, 1])
    elif sum(sum(board[y_start:y_end, x_start:x_end])) == 0: # 0으로 차있다면
        return np.array([1, 0])
    else:       # 더 쪼개야 함
        l = (x_end-x_start)//2   # 현 정사각형의 한 변 길이의 절반
        return recursive(x_start, x_start + l, y_start, y_start + l) + recursive(x_start, x_start + l, y_start + l, y_end) + recursive(x_start + l, x_end, y_start, y_start + l) + recursive(x_start + l, x_end, y_start + l, y_end)

def solution(arr):
    global board
    board = np.array(arr)
    length = len(board)

    return recursive(0, length, 0, length).tolist()