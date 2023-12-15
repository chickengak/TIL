"""
https://school.programmers.co.kr/learn/courses/30/lessons/131701
"""


# My asnwer
def solution(elements):
    comb_sum = set(elements)
    elements = elements*2
    for i in range(len(elements)//2):
        for n in range(2, len(elements)//2, 1):
            comb_sum.add(sum(elements[i:i+n]))

    return len(comb_sum)+1
# 어떻게 보면 가장 간단한 방법이긴 했으나 무수한 슬라이싱때문에 속도가 많이 느렸다.


# Other's answer
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)
# 길이 별로 잘라서 모으는게 아니라, 하나 주인공 잡고 거기서부터 모든 길이를 다 자르는 방식이라서 내 코드보다 월등히 빨랐다.
# 약 20배가량 빨랐다.

