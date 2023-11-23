def solution(dots):
    x = max(dots[0][0], dots[1][0], dots[2][0]) - min(dots[0][0], dots[1][0], dots[2][0])
    y = max(dots[0][1], dots[1][1], dots[2][1]) - min(dots[0][1], dots[1][1], dots[2][1])
    return abs(x * y)