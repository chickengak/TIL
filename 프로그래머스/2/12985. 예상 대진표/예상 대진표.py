def solution(n,a,b):
    answer = 0
    
    while b != a:
        if a%2:
            a = a//2 +1
        else:
            a = a//2
        if b%2:
            b = b//2 +1
        else:
            b = b//2
        answer +=1
    return answer