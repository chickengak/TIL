"""
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""


# My answers
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
# 일단 졸려서 한글로 쓰겠다. 우선 내 코드가 제일 빠르다. 의외로 쉬운곳에서 애먹고 있었는데 그것도 모르고 계속 최적화를 했더니 가장 빠른 코드가 됐다.
# 아래 코드도 내 코드인데, 쓸데없는 인덱싱을 덜기 위해 target 리스트에 보관하던 x,y 좌표를 target_y, target_x로 분리했다.
# while문에 not in 연산이 있는데 이를 따로 탈출조건으로 빼버려서 in연산을 지웠다.
# 어차피 정수형 좌표이기 때문에 4개의 if의 +-1 <= 연산을 <으로 바꿨다.
# 사실 여기까지 최적화해도 시간효율에서 통과가 안돼서 당황했다. 그러나 넓은 공간이 있는경우엔 이미 지나온 곳을 벽으로 만들어주는 maps[y][x] = 0이 if 바깥에 있어서
# 수많은 중복연산을 일으킨다는 사실을 파악했고, 이를 next_searching.append를 수행하면서 0으로 바꾸게 즉, 어차피 현재 cnt(혹은 step)에서 여기까지 이미 최단거리로 올 수 있는 방법이 있는 경우
# 중복 연산을 중지하도록 바꾸니까 통과할 수 있었다. 편하게 코딩하다가 최적화를 꽤 많이 놓친 문제니까 꼭 기억하자.


def solution(maps):
    target = [len(maps) - 1, len(maps[0]) - 1]
    searching = [[0,0]]
    cnt = 0
    while target not in searching:
        if len(searching)==0:
            return -1
        next_searching = []
        for y, x in searching:
            maps[y][x] = 0
            if y+1 <= target[0]:
               if maps[y+1][x]:
                    next_searching.append([y+1, x])
            if y-1 >= 0:
               if maps[y-1][x]:
                    next_searching.append([y-1, x])
            if x-1 >= 0:
               if maps[y][x-1]:
                    next_searching.append([y, x-1])
            if x+1 <= target[1]:
               if maps[y][x+1]:
                    next_searching.append([y, x+1])
        searching = next_searching
        cnt += 1
    return cnt+1
# 위에서 비교군으로 설명한 내 구버전 코드다.

