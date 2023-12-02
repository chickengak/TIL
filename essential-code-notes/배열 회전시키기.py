"""
I: a list of integers. And a string direction 
G: push the list in the given direction.
https://school.programmers.co.kr/learn/courses/30/lessons/120844
"""


# My answer
def solution(numbers, direction):
    if direction == "left":
        t = numbers.pop(0)
        numbers.append(t)
    else:
        t = numbers.pop(-1)
        numbers = [t] + numbers
    return numbers
# My answer was faster than Others' answers


# Others' answers
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
# Slicing was slower than pop.


from collections import deque

def solution2(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)
# It was very slow.

