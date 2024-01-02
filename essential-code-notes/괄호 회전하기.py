"""
https://school.programmers.co.kr/learn/courses/30/lessons/76502
"""


# My answer
from collections import deque
def solution(s):
    answer = 0
    deq = deque(s)
    for _ in range(len(s)):
        stack=[]
        for c in deq:
            if len(stack) and (c == ']') and (stack[-1] == '['):
                stack.pop()
            elif len(stack) and (c == ')') and (stack[-1] == '('):
                stack.pop()
            elif len(stack) and (c == '}') and (stack[-1] == '{'):
                stack.pop()
            else:
                stack.append(c)
        
        if len(stack) == 0:
            answer +=1
        deq.rotate(1)
    return answer
# 뭔가 규칙성을 찾아서 O(n)이 될 거 같아서 헛짓만 하다가 결국 deque로 풀었던 문제다.
# deque로 구현해서 매번 n 만큼 탐색하기 때문에 n^2이다. 꽤 느릴 줄 알았는데 나쁘진 않은 속도였다.
# 아... 규칙 찾을 수 있었는데...



def solution2(s):
    if len(s)%2:
        return 0
    cnt = 0
    stack = []
    for idx in range(-1, len(s)-1):
        c = s[idx]
        if c == '(':
            stack.append(c)
            if s[idx+1] ==')':
                cnt += 1
        elif c == '{':
            stack.append(c)
            if s[idx+1] =='}':
                cnt += 1
        elif c == '[':
            stack.append(c)
            if s[idx+1] ==']':
                cnt += 1
        elif c == ')':
            try:
                if stack[-1] == '(':
                    stack.pop()
            except:
                stack.append(c)
        elif c == '}':
            try:
                if stack[-1] == '{':
                    stack.pop()
            except:
                stack.append(c)
        else:
            try:
                if stack[-1] == '[':
                    stack.pop()
            except:
                stack.append(c)

    for i in range(len(stack)//2):
        temp = (stack[-i-1], stack[i])
        #print(temp)
        if temp == ('[', ']') or temp == ('{', '}') or temp == ('(', ')') :
            continue
        else:
            return 0
    return cnt