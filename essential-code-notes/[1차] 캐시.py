"""
https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""


# My answer
def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities)*5

    for c in cities:
        city = c.lower()
        try:
            idx = cache.index(city)
            answer += 1
            cache = cache[:idx]+cache[idx+1:] +[city]
        except:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache = cache[1:] + [city]
    return answer
# 정석풀이에 try except를 사용했기 때문에 in을 하고 index를 찾을 필요가 없게된 좋은 코드다.
# 사실 자료구조로는 Doubly linked list (이중 연결 리스트)가 최고의 선택인 문제지만, 직접구현해야 하기에 성능저하가 뻔해보여서 그 방법은 스킵했다.


# Other's answer
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
# 나도 사실 deque를 생각했었는데 의외로 파이썬 deque의 효율이 별로라 채용안했었다.
# 실제 둘의 코드 속도는 별차이가 없다. 단, deque에 maxlen을 정하는 방법이 신기해서 넣어봤다.
