def solution(my_stirng):
    answer = ""
    for i in my_stirng:
        if i.islower(): answer += i.upper()
        else: answer +=i.lower()
    return answer