answer = 0
for _ in range(n:=int(input())):
    word = input()
    distinct = set()
    pre = 'NONE'
    for c in word:
        if c == pre:
            continue
        elif c in distinct:
            break
        else:
            distinct.add(c)
            pre = c
    else:
        answer += 1
print(answer)