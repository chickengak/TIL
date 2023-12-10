"""
https://school.programmers.co.kr/learn/courses/30/lessons/43162

챗지피티의 평가도 나랑 같았다.
첫 번째 코드 (solution1): 이 코드는 while 루프와 for 루프를 중첩하여 사용하며, 각 루프에서 리스트와 집합 연산을 수행합니다. 이러한 중첩된 루프와 여러 데이터 구조의 사용이 상대적으로 더 많은 시간을 소요하게 만듭니다.
두 번째 코드 (solution2): 이 코드는 while 루프와 리스트를 주로 사용하여 네트워크를 탐색합니다. 더 간단한 데이터 구조와 효율적인 루프 구조 덕분에 실행 시간이 빨라집니다.
세 번째 코드 (solution3): 재귀 함수를 사용하여 깊이 우선 탐색(DFS)을 구현합니다. 이 방식은 효율적이지만, 재귀 호출의 오버헤드가 있어 두 번째 코드보다 약간 느립니다.
"""


# My answer
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
# 0.0015 sec
# I used a 4-level nested loop, but in implementing BFS,
# I prevented duplicate exploration, which made my answer two to three times faster than others' answers.




# Other's answer
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    while sum(visited) != n:
        searching = [visited.index(0),]
        answer += 1

        while searching:
            target_node = searching.pop()
            for node_num, connected in enumerate(computers[target_node]):
                if connected and not visited[node_num]:
                    visited[node_num] = 1
                    searching.append(node_num)

    return answer
# 0.0006 sec. This is the fastest answer.
# I used a set -set approach, putting all BFS results into a set. And took the set difference.
# However, in this answer, a list was used for appending and popping during searching.
# This allowed to eliminate the third loop in my code, the first for loop.
# And because using 0 and 1 in the list, he could achieve faster code execution with simple indexing, without the need for set-set operations.


def visit(k, graph, visited):
    visited[k] = 1
    for i in range(len(graph[k])):
        if visited[i] == 0 and graph[k][i] == 1:
            visit(i, graph, visited)

def solution(n, computers):
    visited = [0] * n
    answer = 0

    for i in range(n):
        if visited[i] == 0:
            visit(i, computers, visited)
            answer += 1

    return answer
# 0.0007sec. This was the second fastest answer.
# Because he used DFS, recursive functions were applied.
# The overall approach was similar to the one above,
# but there was a slight performance decrease in the part where the 'visited' was checked every time during the recursive calls.


from collections import deque
def solution(n, computers):
    list_visit = [-i-1 for i in range(n)]
    list_node = [[] for _ in range(n)]
    for i in range(n):
        for node, j in enumerate(computers[i]):
            if node == i:
                continue
            if j:
                list_node[i].append(node)
    for i in range(n):
        if list_visit[i] >= 0:
            continue
        list_queue = deque()
        list_queue.append(i)
        while list_queue:
            now = list_queue.popleft()
            for next_i in list_node[now]:
                if list_visit[next_i] < 0:
                    list_visit[next_i] = i
                    list_queue.append(next_i)
    answer = (len(set(list_visit)))
    return answer
# Used deque