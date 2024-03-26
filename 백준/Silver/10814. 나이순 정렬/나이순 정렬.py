people = [(int((temp:=input().split())[0]), temp[1]) for i in range(int(input()))]

print(*[' '.join(map(str, p)) for p in sorted(people, key = lambda x: (x[0]))], sep='\n')