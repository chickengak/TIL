"""
I: a list of integers. and an integer n
G: Return the value in the integers closest to n.
https://school.programmers.co.kr/learn/courses/30/lessons/120890
"""


# My answer
def solution(array, n):
    array.sort()
    a_dif = [abs(i-n) for i in array]
    return array[a_dif.index(min(a_dif))]

# I got the highest score of 10 points!
# So nice code


# Others' answer
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
# I heard that the lambda can make code slower. I think That's why I got 10 points.
