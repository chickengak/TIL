# from math import factorial
# def solution(n):
#     share, remainder = divmod(n,2)
#     answer = 0
#     while share:
#         answer += factorial(share+remainder)/(factorial(share)*factorial(remainder))
#         share -=1
#         remainder +=2
#     return answer+1
    
def solution(n):
    if n == 1:
        return 1 % 1234567
    elif n == 2:
        return 2 % 1234567
    else:
        a,b = 1,2
        for _ in range(n-2):
            a, b  = b, a+b
        return b % 1234567