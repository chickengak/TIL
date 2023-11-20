"""
I
G
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


# Others' Answers
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]


from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

