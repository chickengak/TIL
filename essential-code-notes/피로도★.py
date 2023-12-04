"""
https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""


# My answer
from itertools import permutations

def solution(k, dungeons):
    cases = list(permutations(dungeons, len(dungeons)))
    maximum = 0
    for case in cases:
        case_k = k
        cnt = 0
        for c in case:
            if case_k >= c[0]:
                case_k -= c[1]
                cnt +=1
            else:
                maximum = max(maximum, cnt)
                break
        else:
            return cnt
    return maximum


# Other's answer
answer = []

def solution(k, dungeons):

    def dfs(k, dungeons, depth):
        temp = True
        for d in range(len(dungeons)):
            dun = dungeons[d]
            if dun[0] <= k and dun[1] <= k:
                temp_dungeons = dungeons[:]
                del temp_dungeons[d]
                dfs(k-dun[1], temp_dungeons, depth+1)
                temp = False
        if temp:
            global answer
            answer.append(depth)
    dfs(k, dungeons, 0)

    return max(answer)
# The best DFS
