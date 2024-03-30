coordinates = [list(map(int, input().split())) for _ in range(int(input()))]
for coordinate in sorted(coordinates, key=lambda x: (x[0], x[1])):
    print(*coordinate)