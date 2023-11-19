def solution(numbers, direction):
    if direction == "left":
        t = numbers.pop(0)
        numbers.append(t)
    else:
        t = numbers.pop(-1)
        numbers = [t] + numbers
    return numbers