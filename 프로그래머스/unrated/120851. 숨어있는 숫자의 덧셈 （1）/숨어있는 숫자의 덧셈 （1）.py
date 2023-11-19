def solution(string):
    sum = 0
    for i in string:
        if 47 < ord(i) < 58:
            sum += int(i)
    return sum