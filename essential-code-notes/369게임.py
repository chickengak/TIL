"""
I: an integer
G: Play the 369 game with the input integers and return the number of times clapping.
https://school.programmers.co.kr/learn/courses/30/lessons/120891
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
# This and following answers are using the count method 3 times. Count method's time complexity is O(n).
# So it can cause performance degradation.

def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))


def solution(order):
    answer = len([1 for ch in str(order) if ch in "369"])
    return answer
# It uses the in method. Its time complexity is almost same of mine.
