"""
I
G
https://school.programmers.co.kr/learn/courses/30/lessons/120853
"""


def solution(s):
    t = None
    sum = 0
    for i in s.split():
        if i != "Z":
            t = int(i)
            sum += t
        else:
            sum -= t
    return sum


def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer
# s := s.split(" ") means  s = s.split(" "); len(s)

def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)
# It uses pop() instead of