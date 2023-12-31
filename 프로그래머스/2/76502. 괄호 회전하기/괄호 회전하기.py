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
    
#     if len(s)%2:
#         return 0
#     cnt = 0
#     stack = []
#     for idx in range(-1, len(s)-1):
#         c = s[idx]
#         if c == '(':
#             stack.append(c)
#             if s[idx+1] ==')':
#                 cnt += 1
#         elif c == '{':
#             stack.append(c)
#             if s[idx+1] =='}':
#                 cnt += 1
#         elif c == '[':
#             stack.append(c)
#             if s[idx+1] ==']':
#                 cnt += 1
#         elif c == ')':
#             try:
#                 if stack[-1] == '(':
#                     stack.pop()
#             except:
#                 stack.append(c)
#         elif c == '}':
#             try:
#                 if stack[-1] == '{':
#                     stack.pop()
#             except:
#                 stack.append(c)
#         else:
#             try:
#                 if stack[-1] == '[':
#                     stack.pop()
#             except:
#                 stack.append(c)

#     for i in range(len(stack)//2):
#         temp = (stack[-i-1], stack[i])
#         #print(temp)
#         if temp == ('[', ']') or temp == ('{', '}') or temp == ('(', ')') :
#             continue
#         else:
#             return 0
#     return cnt