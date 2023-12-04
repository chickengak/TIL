"""
https://school.programmers.co.kr/learn/courses/30/lessons/176963
"""


# My answer
def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    for p in photo:
        temp = 0
        for person in p:
            try:
                temp += dic[person]
            except:
                continue
        answer.append(temp)
    return answer
# Remember dict(zip(list, list)). In addition, my code was the fastest code.