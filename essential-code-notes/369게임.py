"""
I
G
"""


# My answer
def solution(order):
    answer = 0
    for i in str(order):
        if i == "3" or i == "6" or i == "9":
            answer += 1
    return answer


# Others' answer
def solution(order):
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')


def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))


def solution(order):
    answer = len([1 for ch in str(order) if ch in "369"])
    return answer

