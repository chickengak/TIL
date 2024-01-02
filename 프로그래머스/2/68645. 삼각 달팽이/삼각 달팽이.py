def solution(n):
    answer = [[0 for _ in range(i)] for i in range(1, n + 1)]
    cnt = 1
    end = 1 + sum(i for i in range(1, n + 1))
    pos = [0, 0]

    while cnt != end:
        while cnt != end:
            try:
                if answer[pos[0]][pos[1]] == 0:
                    answer[pos[0]][pos[1]] = cnt
                    cnt += 1
                    pos = [pos[0] + 1, pos[1]]
                else:
                    break
            except:
                break
        pos = [pos[0] - 1, pos[1] + 1]
        while cnt != end:
            try:
                if answer[pos[0]][pos[1]] == 0:
                    answer[pos[0]][pos[1]] = cnt
                    cnt += 1
                    pos = [pos[0], pos[1] + 1]
                else:
                    break
            except:
                break
        pos = [pos[0] - 1, pos[1] - 2]
        while cnt != end:
            try:
                if answer[pos[0]][pos[1]] == 0:
                    answer[pos[0]][pos[1]] = cnt
                    cnt += 1
                    pos = [pos[0] - 1, pos[1] - 1]
                else:
                    break
            except:
                break
        pos = [pos[0] + 2, pos[1] + 1]
    result = []
    for ans in answer:
        result += ans
    return result