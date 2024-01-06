"""
https://school.programmers.co.kr/learn/courses/30/lessons/42628
"""


# My answer
def solution(operations):
    answer = []
    for operation in operations:
        temp = operation.split()
        if temp[0] == 'I':
            answer.append(int(temp[1]))
        else:
            if temp[1] == '1':
                try:
                    answer.remove(max(answer))
                except:
                    continue
            else:
                try:
                    answer.remove(min(answer))
                except:
                    continue
    return [max(answer), min(answer)] if len(answer) else [0,0]
# 요즘 문제 빠르게 풀기 챌린지 중이라서 그냥 리스트에 max, min 때려 박았는데 통과가 돼버렸다...
# 문제가 요구하는 능력은 다음이다.


# Other's answer
import heapq

def solution(arguments):
    dp_queue = []
    for arg in arguments:
        op, val = arg.split(' ')
        if op == 'I':
            heapq.heappush(dp_queue, int(val))
        else:
            try:
                if val == '1':
                    remove_value = heapq.nlargest(1, dp_queue)[0]
                else:
                    remove_value = heapq.nsmallest(1, dp_queue)[0]
            except IndexError:
                pass
            else:
                dp_queue.remove(remove_value)
                heapq.heapify(dp_queue)             # 제거 후에 heapify를 실행하는게 포인트다.
                                                    # heapq에서 heappop()을 하면 최소값이 pop되고 트리에도 문제가 없다.
    if len(dp_queue) == 0:                          # 다만 최대값을 제거할 때 트리가 깨지는게 문제되므로
        return [0, 0]                               # 최대값을 제거했을 때만 remove + heapify를 수행하면 간결해질거다.
    elif len(dp_queue) == 1:
        return [dp_queue[0], dp_queue[0]]
    else:
        max_value = heapq.nlargest(1, dp_queue)[0]
        min_value = heapq.nsmallest(1, dp_queue)[0]
        return [max_value, min_value]
# 클래스를 이용해서 구현한 사람들도 많이 있었으나 코테 시간 제한을 생각한다면 이게 일단 공부할만 했다.

