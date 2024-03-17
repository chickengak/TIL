n = int(input())
answer = min(99, n)
if n > 110:
    for num in range(111, n + 1):
        temp = str(num)
        if (int(temp[0]) - int(temp[1])) == (int(temp[1]) - int(temp[2])):
            answer += 1

print(answer)
