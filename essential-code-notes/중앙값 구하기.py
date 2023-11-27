def solution(l):
    l.sort()
    return l[int(len(l)/2)]

def solution(array):
    return sorted(array)[len(array) // 2]

#l.sort().index() 이렇게 두개식을 못 달기 때문에 위처럼 하면 1줄 코딩 가능.