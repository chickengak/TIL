def solution(s):
    stack = []
    for i in s[::-1]:
        try:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        except:
            stack.append(i)
    
    return 1 if len(stack) == 0 else 0