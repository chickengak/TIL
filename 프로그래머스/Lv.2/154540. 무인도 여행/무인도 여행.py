def solution(maps):
    maps = list(map(list, maps))
    answer = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == 'X':
                continue
            total = 0
            cur_visit = {(row, col)}
            while cur_visit:
                next_visit = set()
                for y, x in list(cur_visit):
                    total += int(maps[y][x])
                    maps[y][x] = 'X'
                    for y_, x_ in directions:
                        y_, x_ = y_ + y, x_ + x
                        if (-1 < y_ < len(maps)) and (-1 < x_ < len(maps[0])) and maps[y_][x_]!='X':
                            next_visit.add((y_, x_))
                cur_visit = next_visit
            answer.append(total)
    return sorted(answer) if answer else [-1]