import heapq

def solution(book_time):
    answer = 0
    times = [(int(bt[0][:2])*60 + int(bt[0][3:]), int(bt[1][:2])*60 + int(bt[1][3:]) + 10) for bt in book_time]
    print(times)
    times.sort(key=lambda x: (-x[0], -x[1]))
    q = []
    while times:
        pop = times.pop()
        if q and q[0] <= pop[0]:
            heapq.heappop(q)
        heapq.heappush(q, pop[1])
        answer = max(answer, len(q))
    return answer