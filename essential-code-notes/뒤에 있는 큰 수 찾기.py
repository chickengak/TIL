"""
https://school.programmers.co.kr/learn/courses/30/lessons/154539
"""


# My answer
def solution(numbers):
    answer = [-1]*(len(numbers))
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer
# 이 문제도 꽤나 고전했던 문제다.
# 입력되는 numbers의 길이가 100만이었기 때문에 2중루프로 대충 푸는 것은 불가능했고
# 선형으로 지나가면서 필요에 따라 되돌아와 값을 채우는 방식이 필요했다.
# 생각만큼 구현이 힘들어서 힌트를 기웃기웃했었다.