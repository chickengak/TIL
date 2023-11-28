
def solution(price, money, count):
    ans = price*sum(list(range(1, count+1)))
    return (money-ans)*-1 if money-ans < 0 else 0