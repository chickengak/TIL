def solution(n):
    return n.pop(n.index(max(n))) * n.pop(n.index(max(n)))


def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
# 정렬 후 뒤에서부터 세기