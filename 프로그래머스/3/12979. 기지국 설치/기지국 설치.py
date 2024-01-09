def solution(n, stations, w):
    answer = 0
    # stations_set = set()
    # for station in stations:
    #     stations_set.update(list(range(station-w-1, station+w)))

    idx = 0
    num = 1
    while num <= n:
        if (idx < len(stations)) and (stations[idx]-w <= num <= stations[idx]+w):
            num = stations[idx]+w+1
            idx +=1
        else:
        #elif num < stations[idx]-w:
            num += w*2+1
            answer +=1

    return answer