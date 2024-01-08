DP Dynamic Programming
- BFS처럼 최단거리, DFS처럼 최댓값 등을 구해야 하는데 경우의 수가 너무 많을 때 사용.
- 중복되는 연산을 최소화 시키는게 포인트
- 연산한 내용을 기억하고 있어야 한다. (어떤 정보를 남겨야 하고 어떤 정보를 누적해야 하는지가 중요)
- DP 삼각형
- set 활용
- DP 사각형: 제한된 방향으로 진행하며 경우의 수가 누적될 때

Two Point Search


Queue / Deque  
- Queue 두 개가 서로에게 pop, append를 할 경우, q1과 q2는 하나의 이어진 리스트로 볼 수 있다.
    - 하나가 일방적으로 pop, append할 경우 q1 + q2. 서로 pop, append할 경우 q1 + q2 + q1


heapq
- 이중 우선 순위 힙: 일반 힙을 만들고, 최소값은 heappop으로 빼고 최대값은 nlargest로 찾아 remove




&nbsp;

알면 좋은 함수  
math.comb(n, k)  combination. n개에서 k개를 선택하는 경우의 수