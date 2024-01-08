def solution(startpoint, endpoint):
    distance = endpoint - startpoint
    maximum = int((distance)**0.5)
    acc = [n for n in range(1, maximum)]
    distance -= sum(acc)*2
    share, remainder = divmod(distance, maximum)
    step = len(acc)*2 + share + (1 if remainder else 0)
    print(step)


tcases = int(input())

for _ in range(tcases):
    x, y = [int(i) for i in input().split()]
    solution(x, y)

