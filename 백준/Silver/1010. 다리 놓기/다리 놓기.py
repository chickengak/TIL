from math import factorial

tcase = int(input())

for _ in range(tcase):
    a, b = [int(i) for i in input().split()]
    if a > b:
        a, b = b, a
    
    print(factorial(b)//factorial(b-a)//factorial(a))