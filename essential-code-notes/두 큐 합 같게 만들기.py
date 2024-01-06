"""
https://school.programmers.co.kr/learn/courses/30/lessons/118667
"""


# My answer
from collections import deque

def solution(queue1, queue2):
    cnt = 0
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    end = len(queue1)*3
    # while cnt < (len(queue1)+len(queue2))*3:
    while cnt < end:                        # while문 종료 조건을 수정함.
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
# 일단 문제 풀이의 접근 방식은 평범하다. 단, return -1을 하려면 pop, append로 완전탐색을 끝마치고 -1을 리턴하기 때문에
# 길이가 긴데 -1을 리턴하는 경우엔 다소 시간이 걸린다.
# 우선, 두 개의 큐가 서로에게 pop, insert를 하는 경우라서 결국엔 1 열로 세운것과 같다. 그래서 완전 탐색을 위해서는 3n으로 가능.


# Other's answer
def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) // 2
    cur = sum(queue1)
    queue3 = queue1 + queue2 + queue1

    s = 0                               # start 시작점 의미
    e = len(queue1) - 1                 # end 끝점 의미     s와 e는 각각 q3의 첫 번째 q1의 시작점과 끝점을 의미
    answer = 0
    while True:
        if cur == target:
            return answer
        if cur < target:                # q2가 클 때
            e += 1
            if e >= len(queue3):        # q3 인덱스를 넘어가면 종료
                return -1
            cur += queue3[e]            # q2의 요소 하나를 빼서 q1에 더한 역할.
        else:
            cur -= queue3[s]            # q1의 요소 하나를 빼서 q2로 옮긴 역할
            s += 1
        answer += 1
# 3.80 sec
# 이해하기 쉽게 주석 좀 달음. 리스트를 붙여 버려서 실제로 pop, append를 하지 않게 구현함.
# 의외로 queue에 직접 pop, append를 한거랑 시간은 비슷하다.


def solution(queue1, queue2):
    indicator2=sum(queue1)-int(sum(queue1+queue2)/2)
    answer=0
    sub_list=(queue1+queue2+queue1)[::-1]
    add_list=(queue2+queue1+queue2)[::-1]
    while indicator2!=0:
        try:
            if indicator2>0:
                indicator2-=sub_list.pop()
            else:
                indicator2+=add_list.pop()
        except:                             # list에서 pop을 할 수 없는 경우 즉, 리스트가 빈 경우 오류 발생
            return -1       
        answer+=1
    return answer
# 1.24 sec
# 주석 좀 달아봄. 이게 가장 빠른 코드였다.
# 메모리는 더 썼지만, indexing 대신 pop만을 썼고, pop을 쓰기위해 뒤집는 [::-1]연산이 예상외로 매우 빨랐으며
# try except의 간결함 덕분에 연산이 빨랐다고 평가할 수 있다.
# 이는 사람의 눈으로 봤을 때는 앞선 코드가 더 간결하고 빠를 것으로 예상했던 것과는 정말 다른 결과였다.
# 인덱싱이 아무리 빠르다고 해도 pop과 try except의 아성을 넘을 수 없다는 결과가 신기했다.
