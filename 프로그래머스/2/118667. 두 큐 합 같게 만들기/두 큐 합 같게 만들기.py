from collections import deque

def solution(queue1, queue2):
    cnt = 0
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while cnt < (len(queue1)+len(queue2))*4:
        if sum_queue1 == sum_queue2:
            return cnt
        if sum_queue1 > sum_queue2:
            temp = queue1.popleft()
            sum_queue1 -= temp
            sum_queue2 += temp
            queue2.append(temp)
        else:
            temp = queue2.popleft()
            sum_queue2 -= temp
            sum_queue1 += temp
            queue1.append(temp)
        cnt += 1
    return -1