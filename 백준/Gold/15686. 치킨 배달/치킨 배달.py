from itertools import combinations
n, m = list(map(int, input().split()))
two_list = []
one_list = []
for row in range(n):   # 1, 2 위치 저장
    row_input = list(map(int, input().split()))
    for col in range(n):
        if row_input[col] == 1:
            one_list.append((row, col))
        elif row_input[col] == 2:
            two_list.append((row, col))

table = [[0] * len(two_list) for _ in range(len(one_list))]
for row, one in enumerate(one_list):   # 각 집(1)에서 치킨집(2)까지의 모든 거리를 미리 table에 계산
    for col, two in enumerate(two_list):
        table[row][col] = abs(one[0] - two[0]) + abs(one[1] - two[1])

if m == len(two_list):
    print(sum([min(i) for i in table]))
else:       # 치킨집의 조합을 만들고 각 조합마다의 거리를 table에서 찾고 최소값을 리턴
    combs = list(combinations(range(len(two_list)), m))
    minimum = 999999999

    for comb in combs:
        total = 0
        for row in table:
            temp = []
            for col in comb:
                temp.append(row[col])
            total += min(temp)
        if total < minimum:
            minimum = total

    print(minimum)