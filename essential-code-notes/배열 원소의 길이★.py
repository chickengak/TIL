def solution(s):
    return list(map( lambda x: len(x), s))

#map에 lambda를 사용하면 list comprehension보다 오히려 느려질 수 있습니다. 최대한 지양하는게 좋다고 생각합니다

def solution(strlist):
    return list(map(len, strlist))