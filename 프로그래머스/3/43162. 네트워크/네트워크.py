def solution(n, computers):
    all_coms = set(range(n))
    cnt = 0
    visited = set()
                                                                      
    while len(visited) != n:
        visit = {(all_coms - visited).pop(), }  # new_visiting           
        
        while True:
            
            for v in list(visit):     # 방문해야할 노드를 방문시작
                visited.add(v)
                for i in range(n):         # 다음 방문할 노드 탐색
                    if computers[v][i]:
                        visit.add(i)             

            next_visit = visit - visited
            if len(next_visit) == 0:      # BFS로 탐색한 결과 더 이상 새로운 노드가 없을경우 멈춤.
                cnt +=1
                break
            visit = next_visit        # 아직 방문할 곳이 있을 경우, 방문해야하는 곳을 다음 루프에 넘겨줌.

    return cnt