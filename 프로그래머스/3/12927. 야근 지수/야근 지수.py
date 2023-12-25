def solution(n, works):
    works.sort(reverse=True)
    time = 0
    stop = False
    while not stop:
        if time == n:
            break
        temp = works[0]
        time +=1
        works[0] -=1
        for i in range(1, len(works)):
            if works[i] != temp or time == n:
                break
            time +=1
            works[i] -=1
    return sum([ max(work, 0)**2 for work in works])