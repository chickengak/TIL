def solution(absolutes, signs):
    return sum(absolutes[i] if signs[i] else absolutes[i]*-1 for i in range(len(signs)))
