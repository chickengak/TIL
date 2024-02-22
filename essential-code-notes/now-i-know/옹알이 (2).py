"""
https://school.programmers.co.kr/learn/courses/30/lessons/133499
"""


# My answer
def solution(babbling):
    dic = { "aya":"+", "ye":"-", "woo":"*", "ma":"/"}
    cnt = 0
    for b in babbling:
        for d in dic:
            b = b.replace(d, dic[d])
        if ("++" in b) | ("--" in b) | ("**" in b) | ("//" in b):
            continue
        for dv in dic.values():
            b = b.replace(dv, "")
        if b == "":
            cnt += 1
    return cnt


# Others' answer
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
# The logic is almost same. But it uses less replace.


def solution(babbling):
    count = 0
    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            count += 1
    return count
# I brought it because it's cool how replace was used multiple times.
