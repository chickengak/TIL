"""
https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""

# My asnwer
def solution(topping):
    answer = 0
    right = set()
    dic = dict()
    for i in range(len(topping)):
        try:
            dic[topping[i]] += 1
        except:
            dic[topping[i]] = 1

    for i in range(len(topping) - 1, 0, -1):
        right.add(topping[i])
        if dic[topping[i]] == 1:
            del (dic[topping[i]])
        else:
            dic[topping[i]] -= 1

        if len(dic) == len(right):
            answer += 1
    return answer
# 좀 고전한 문제다.
# 좌우에서 다가와 중간점을 찾고 거기부터 넓혀가면서 좌우의 토핑개수가 같을 때까지만 탐색하게 했는데
# 다시 생각해보니 그 한계를 넘어서도 좌우의 토핑개수가 같아지는 경우가 발생할 수 있었다.
# 점점 코드는 꼬이고 복잡해지다가 결국 동적으로 찾다간 끝이 없겠다 싶었다.
# 그래서 좌측에게 모든 토핑을 다 할당해주고 롤케이크 오른쪽부터 하나씩 우측에게 줬고 그러면서 중복개수를 제거할 수 있도록 dict와 set을 사용하게 됐다.
# from collections import Counter 를 사용해서 dict를 만드는 사람들도 있던데 실행시간은 그게 그거였다.