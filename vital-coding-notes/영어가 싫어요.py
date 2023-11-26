"""
I
G
https://school.programmers.co.kr/learn/courses/30/lessons/120894/solution_groups?language=python3&type=my
"""


# My answer
def solution(numbers):
    answer = ""
    while numbers:
        if numbers[0] == "t":
            if numbers[1] == "w":
                answer += "2"
                numbers = numbers[3:]
            else:
                answer += "3"
                numbers = numbers[5:]
        elif numbers[0] == "f":
            if numbers[1] == "o":
                answer += "4"
                numbers = numbers[4:]
            else:
                answer += "5"
                numbers = numbers[4:]
        elif numbers[0] == "s":
            if numbers[1] == "i":
                answer += "6"
                numbers = numbers[3:]
            else:
                answer += "7"
                numbers = numbers[5:]
        elif numbers[0] == "o":
            answer += "1"
            numbers = numbers[3:]
        elif numbers[0] == "e":
            answer += "8"
            numbers = numbers[5:]
        elif numbers[0] == "n":
            answer += "9"
            numbers = numbers[4:]
        else:
            answer += "0"
            numbers = numbers[4:]
    return int(answer)


# Others' answer
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)
#
