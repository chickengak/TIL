def solution(n):
    first = []
    second = []
    sqrt = n**0.5
    for i in range(1,int(sqrt)+1):
        if n%i == 0:
            first.append(i)
            if i != sqrt:
                second.append(n//i)
    return first + second[::-1]