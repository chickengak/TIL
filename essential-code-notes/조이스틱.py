"""
https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""


# My answer
import re
def solution1(name):
    if (set(name) == {"A",}):
        return 0
    p = re.compile('[' + "A" + ']+').finditer(name)
    left_right_step = len(name)-1
    for i in p:
        x = (len(name)-i.end())*2-1+i.start()  # 역주행 후 정주행.
        y = (0 if i.start()-1<0 else i.start()-1)*2 + (len(name)-i.end()) # 정주행 후 역주행.
        left_right_step = min(x,y,left_right_step)
    up_down_step = 0
    for c in name:  #65~90
        if ord(c) < 79:
            up_down_step += ord(c)-65
        else:
            up_down_step += abs(ord(c)-91)

    return left_right_step+ up_down_step
# 0.43 sec.
# 편하게 풀려고 re를 쓴게 성능저하의 원인같다. 그렇다고 막 느리진 않다. 꽤 높은 5점을 받기도 했고, 극히 일부 코드를 제외하면 내 코드가 빨랐다.
# 그래도 re 사용을 자제해야할거 같다.


# Other's answer
def solution2(name):
    answer = 0
    for i in range(len(name)):#상하먼저구하기
        x=ord(name[i])-ord("A")
        y=ord("Z")-ord(name[i])+1
        answer+=(x if x<y else y)

    tmp=0
    shift=len(name)-1
    for i in range(len(name)):
        if name[i]=="A":
            tmp=i
            while(tmp<len(name) and name[tmp]=="A"):
                tmp+=1
            left=(0 if i==0 else i-1)
            right=len(name)-tmp
            shift=min(shift,left+right+min(left,right))
    answer+=shift
    return answer
# 0.19 sec
# 연산은 나와 기본적으로 같으나 while로 연속된 A구간을 직접 찾았다.
