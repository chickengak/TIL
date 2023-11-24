import numpy as np

def solution(board):
    board = np.array(board)
    locations = np.column_stack(np.where(board == 1))
    for r, c in locations:
        board[max(r - 1, 0):min(r + 2, len(board)), max(c - 1, 0):min(c + 2, len(board))] = 1
    return np.count_nonzero(board == 0)
