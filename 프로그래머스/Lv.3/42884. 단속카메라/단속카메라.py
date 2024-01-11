def solution(routes):
    answer = 0
    routes.sort(key=lambda x : (x[1], x[0]))    # 나가는 순으로 정렬
    from_idx = 0
    while from_idx < len(routes):
        to_idx = from_idx
        while to_idx+1 < len(routes) and routes[to_idx+1][0] <= routes[from_idx][1]:
            to_idx += 1
        answer +=1
        from_idx = to_idx + 1
    return answer
