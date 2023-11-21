def solution(before, after):
    l = list(after)
    for i in before:
        try:
            l.remove(i)
        except:
            return 0
    return 1