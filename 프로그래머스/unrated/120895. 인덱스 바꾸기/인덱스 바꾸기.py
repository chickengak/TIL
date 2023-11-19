def solution(str, num1, num2):
    return str[:num1] + str[num2] + str[num1+1: num2] + str[num1] + str[num2+1:]