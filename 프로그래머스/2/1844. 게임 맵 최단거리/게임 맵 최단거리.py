def solution(maps):
    target_y = len(maps) - 1
    target_x = len(maps[0]) - 1
    searching = [[0,0]]
    cnt = 0
    while True:
        if len(searching)==0:
            return -1
        next_searching = []
        for y, x in searching:
            if y == target_y and x == target_x:
                return cnt + 1

            if y < target_y:
               if maps[y+1][x]:
                   maps[y+1][x] = 0
                   next_searching.append([y+1, x])
            if y > 0:
               if maps[y-1][x]:
                   maps[y - 1][x] = 0
                   next_searching.append([y-1, x])
            if x > 0:
               if maps[y][x-1]:
                   maps[y][x-1] = 0
                   next_searching.append([y, x-1])
            if x < target_x:
               if maps[y][x+1]:
                   maps[y][x + 1] = 0
                   next_searching.append([y, x+1])
        searching = next_searching
        cnt += 1