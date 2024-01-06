"""
https://school.programmers.co.kr/learn/courses/30/lessons/49994
"""


# My answer
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
# 내가 풀었지만 신기하게 풀긴했다. 기억하려고 씀.
# 좌표평면에서 지나간 경로의 합을 출력하는 문제로 같은 길을 중복으로 지나간 경우를 제거하는게 키포인트였다.
# 중복을 제거하기위해 set을 사용했고, set에 list는 못 넣어도 tuple은 넣을 수 있었다.
# set으로 중복을 제거할 떄, (1,0)에서 (1,1)로 간 경우와 (1,1)에서 (1,0)을 가는 경우도 중복임을 체크해야 했다.
# 이를 해결하기 위해서 튜플간의 대소관계 if before < after: 를 체크해서 set에 넣었다.
