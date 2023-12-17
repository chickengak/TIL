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