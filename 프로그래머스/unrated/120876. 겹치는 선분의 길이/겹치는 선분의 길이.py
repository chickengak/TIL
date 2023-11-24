def solution(lines):
    dots = []
    for i, j in lines:
        dots.extend(range(i, j))
    dots_d = {}
    for i in set(dots):
        dots_d[i] = dots.count(i)
    return sum(1 for v in dots_d.values() if v > 1)