def solution(dirs):
    route = set()
    direction = {'D':(0,-1), 'U':(0,1), 'R':(1,0), 'L':(-1,0)}
    cur_pos = [0,0]
    for dir in dirs:
        x, y = cur_pos[0] + direction[dir][0], cur_pos[1] + direction[dir][1]
        if (-6 < x < 6) and (-6 < y < 6):
            before = cur_pos
            after = [x, y]
            if before < after:
                route.add((tuple(before), tuple(after)))
            else:
                route.add((tuple(after), tuple(before)))
            cur_pos = after
            
    return len(route)