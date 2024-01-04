"""
https://school.programmers.co.kr/learn/courses/30/lessons/87390
"""


# My answer
def solution(n, left, right):
    share, remainder = divmod(left, n)  # share행 remainder열이 left 위치.
    target_share, target_remainder = divmod(right, n)
    answer = []

    while share != target_share:
        if share >= remainder:
            answer += [share + 1] * (share - remainder + 1)
        answer += list(range(max(share + 2, remainder + 1), n + 1))
        share += 1
        remainder = 0

    #if target_share >= target_remainder:
    if answer:
        answer += [share + 1] * min(share+1,target_remainder+1)
    else:
        #remainder = 0
        answer += [share + 1] * (share - 0 + 1)
        answer += list(range(max(share + 2, 0 + 1), n + 1))
        answer = answer[remainder:target_remainder+1]       # 같은 줄에서 시작하고 끝날 떄
        return answer
    if target_share <= target_remainder:
        answer += list(range(remainder +1 if share ==0 and target_share==0 else max(share + 2, remainder + 1), target_remainder + 2))
    return answer
# 꽤 오래 걸린 문제다. 풀다보니 문제가 산으로 간 경우다.
# 하.. 똑같은 규칙을 찾긴 했는데... 멍청하게 구현했다. divmod를 쓰면 좌표를 알 수 있다는 것에 꽂힌게 화근이다.
# 정말 이런 개똥코드 처음인데 치욕스럽다 잘하자


# Other's answer
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer
