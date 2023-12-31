
def solution(board, moves):
    answer = 0
    stack = []
    rotate = []
    for i in range(len(board)):
        temp = list()
        for j in range(len(board)-1,-1,-1):
            if board[j][i] == 0:
                break
            temp.append(board[j][i])
        rotate.append(temp)
    for move in moves:
        pick = None
        try:
            pick = rotate[move-1].pop()
        except:
            continue
        
        try:
            if stack[-1] == pick:
                stack.pop()
                answer +=2
            else:
                stack.append(pick)
        except:
            stack.append(pick)
    
    return answer